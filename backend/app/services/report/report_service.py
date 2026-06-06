import json
from sqlalchemy.orm import Session
from sqlalchemy import func
from anthropic import Anthropic
from app.core.config import ANTHROPIC_API_KEY
from app.models.progressModels import Progress
from app.models.reportModels import Report
from app.models.problemModels import Problem
from app.models.lessonModels import Lesson
from app.models.noteModels import WrongAnswer


client = Anthropic(api_key=ANTHROPIC_API_KEY)


def count_wrong_answers(db: Session, user_id: int, track: str, chapter: str) -> int:
    """틀린 문제 개수"""
    wrong_answers = db.query(WrongAnswer).filter(
        WrongAnswer.user_id == user_id,
        WrongAnswer.source_type == "learning"
    ).all()

    wrong_problem_ids = {wa.track_problem_id for wa in wrong_answers}

    lessons = db.query(Lesson).filter(
        func.upper(Lesson.track) == track.upper(),
        Lesson.chapter == chapter,
        Lesson.lesson_type.in_(["code_fill", "multiple_choice"])
    ).all()

    wrong_count = sum(1 for lesson in lessons if lesson.problem_id in wrong_problem_ids)
    return wrong_count


def get_chapter_title(db: Session, track: str, chapter: str) -> str:
    lesson = db.query(Lesson).filter(
        func.upper(Lesson.track) == track.upper(),
        Lesson.chapter == chapter
    ).order_by(Lesson.order_index).first()

    if lesson and lesson.title:
        return lesson.title

    return chapter


def get_problem_title(db: Session, problem_id: int) -> str:
    """문제 제목 조회"""
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if problem and problem.content:
        return problem.content.get("title", f"문제 {problem_id}")
    return f"문제 {problem_id}"


def build_wrong_problems_list(db: Session, user_id: int, track: str, chapter: str) -> list:
    """틀린 문제 목록 구성"""
    wrong_answers = db.query(WrongAnswer).filter(
        WrongAnswer.user_id == user_id,
        WrongAnswer.source_type == "learning"
    ).all()

    wrong_problems = []
    for wa in wrong_answers:
        if wa.track_problem:
            problem = wa.track_problem

            # 문제가 해당 트랙/챕터에 속하는지 확인
            if (problem.track.upper() == track.upper() and
                problem.chapter == chapter):

                wrong_problems.append({
                    "problemId": problem.id,
                    "title": problem.content.get("title", "문제") if problem.content else "문제",
                    "userAnswer": wa.user_answer,
                    "correctAnswer": problem.answer,
                    "explanation": problem.explanation,
                    "type": "code_fill" if isinstance(wa.user_answer, dict) else "multiple_choice"
                })

    return wrong_problems


def build_hint_usage(db: Session, user_id: int, track: str, chapter: str) -> dict:
    """문제별 힌트 사용 패턴"""
    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        func.upper(Progress.track) == track.upper(),
        Progress.chapter == chapter
    ).first()

    hint_usage = {}
    if progress and progress.report:
        for p in progress.report.get("problems", []):
            problem_title = get_problem_title(db, p["problemId"])
            hints_used = p.get("hintsUsed", 0)
            if hints_used > 0:
                hint_usage[problem_title] = hints_used

    return hint_usage


def check_reveal_used(db: Session, user_id: int, track: str, chapter: str) -> bool:
    """정답 공개 사용 여부"""
    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        func.upper(Progress.track) == track.upper(),
        Progress.chapter == chapter
    ).first()

    if progress and progress.report:
        for p in progress.report.get("problems", []):
            if p.get("usedReveal", False):
                return True

    return False


def generate_ai_report(
    chapter_title: str,
    track: str,
    total_problems: int,
    wrong_count: int,
    hint_usage: dict,
    wrong_problems: list,
    reveal_used: bool
) -> dict:
    """Claude API를 사용해 AI 리포트 생성"""

    correct_count = total_problems - wrong_count
    accuracy_rate = int((correct_count / total_problems) * 100) if total_problems > 0 else 0

    # 약점 개념 추출
    weak_concepts = [p["title"] for p in wrong_problems[:3]]

    # 힌트 사용 문제들
    hint_problems = ", ".join([f"{title}({count}회)" for title, count in list(hint_usage.items())[:3]])

    # 프롬프트 구성
    prompt = f"""당신은 AI-CO 딥러닝 학습 플랫폼의 "코냥이" 튜터입니다.
학생이 '{chapter_title}' 챕터를 완료했습니다. 학습 진도를 분석해서 개인화된 피드백을 제공하세요.

## 📊 학습 현황
- **챕터**: {chapter_title}
- **정답률**: {accuracy_rate}% ({correct_count}/{total_problems})
- **틀린 문제**: {', '.join(weak_concepts) if weak_concepts else '없음'}
- **힌트 사용 패턴**: {hint_problems if hint_problems else '없음'}
- **정답 공개**: {'사용함' if reveal_used else '미사용'}

{format_wrong_problems_for_prompt(wrong_problems)}

## 생성 가이드

### 상황별 피드백 규칙:
1. **정답률 100% + 힌트 0** → "완벽하게 이해했어요! 개념이 탄탄하네요."
2. **정답률 100% + 힌트 사용** → "전체 다 맞췄어요! 다만 {{약점}}은 한번 더 확인하면 좋을 것 같아요."
3. **정답 있음 + 정답공개 사용** → "정답을 봤다는 건 이 부분이 아직 완전히 내 것이 아니라는 신호예요."
4. **오답 있음** → "{{오답 문제}}에서 실수했네요. 특히 {{오개념}}을 다시 확인하면 좋을 것 같아요."

## 응답 형식 (JSON only - 설명 없이)

다음 5가지를 JSON으로만 응답하세요:

1. **weakConcepts**: 약점 개념 배열 (문자열, 최대 3개)
2. **cobotComment**: 2-3줄의 친근한 피드백 (이모지 포함 가능, 위 규칙 따를 것)
3. **summary**: 3-4줄 챕터 요약 ("~을/를 배웠어요" 형식)
4. **keyPoint**: 2-3줄 핵심 포인트 ("A는 ~, B는 ~" 형식)
5. **nextChapter**: 3-4줄 다음 챕터와의 연관성
6. **opensource**: 추천 자료 3개 배열 (객체: name, desc, url)

예시 응답:
{{
  "weakConcepts": ["개념1", "개념2"],
  "cobotComment": "개념1과 개념2에서 집중이 필요해 보여요. 이 부분들을 다시 한 번 복습하면 다음 단계로 나아가기가 훨씬 수월할 거예요! 👍",
  "summary": "이번 챕터에서는 핵심 개념들을 체계적으로 배웠어요. {{chapter_title}}의 주요 내용을 이해하고, 실제 구현을 통해 개념을 심화할 수 있었네요.",
  "keyPoint": "핵심 원리 1은 {{설명}}, 핵심 원리 2는 {{설명}} 두 가지가 이번 챕터의 핵심이에요.",
  "nextChapter": "다음 챕터에서는 이번 챕터에서 배운 내용이 {{방식}}으로 활용돼요. 지금의 기초가 다음 단계를 이해하는 데 중요하니까 복습해 두면 좋을 것 같아요!",
  "opensource": [
    {{"name": "자료 제목 1", "desc": "자료 설명", "url": "https://example.com"}},
    {{"name": "자료 제목 2", "desc": "자료 설명", "url": "https://example.com"}},
    {{"name": "자료 제목 3", "desc": "자료 설명", "url": "https://example.com"}}
  ]
}}

이 프롬프트에 대해 JSON만 응답하세요. 절대로 설명을 추가하지 마세요."""

    try:
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2048,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response_text = message.content[0].text

        # JSON 파싱
        try:
            ai_report = json.loads(response_text)
        except json.JSONDecodeError:
            # JSON 파싱 실패 시 텍스트에서 JSON 추출 시도
            json_start = response_text.find('{')
            json_end = response_text.rfind('}') + 1
            if json_start != -1 and json_end > json_start:
                ai_report = json.loads(response_text[json_start:json_end])
            else:
                raise ValueError("JSON 파싱 실패")

        return ai_report

    except Exception as e:
        print(f"Claude API 오류: {e}")
        return get_fallback_report(chapter_title, weak_concepts)


def format_wrong_problems_for_prompt(wrong_problems: list) -> str:
    """틀린 문제 포맷팅"""
    if not wrong_problems:
        return ""

    formatted = "\n## 틀린 문제 상세\n"
    for i, p in enumerate(wrong_problems, 1):
        formatted += f"\n{i}. **{p['title']}**\n"
        formatted += f"   - 유저 답: {p['userAnswer']}\n"
        formatted += f"   - 정답: {p['correctAnswer']}\n"
        if p.get('explanation'):
            formatted += f"   - 해설: {p['explanation']}\n"

    return formatted


def get_fallback_report(chapter_title: str, weak_concepts: list) -> dict:
    """API 실패 시 폴백 리포트"""
    return {
        "weakConcepts": weak_concepts,
        "cobotComment": f"{chapter_title} 챕터 완료를 축하합니다! 리포트 생성 중 일시적 오류가 발생했어요. 잠시 후 다시 시도해주세요.",
        "summary": f"{chapter_title}의 핵심 개념들을 학습했습니다.",
        "keyPoint": "학습한 내용을 토대로 다음 챕터를 준비해주세요.",
        "nextChapter": "다음 챕터에서 더 깊이 있는 내용을 다룰 예정입니다.",
        "opensource": [
            {
                "name": "공식 문서",
                "desc": "해당 주제의 공식 문서를 참고해주세요.",
                "url": "https://pytorch.org/docs/"
            }
        ]
    }


def generate_report_background(user_id: int, track: str, chapter: str):
    """백그라운드에서 비동기로 AI 리포트 생성"""
    from app.core.database import SessionLocal

    db = SessionLocal()

    try:
        # [1] progress 조회
        progress = db.query(Progress).filter(
            Progress.user_id == user_id,
            func.upper(Progress.track) == track.upper(),
            Progress.chapter == chapter
        ).first()

        if not progress:
            print(f"⚠️ Progress 없음: {user_id} - {track} {chapter}")
            return

        # [2] 챕터 정보 조회
        chapter_title = get_chapter_title(db, track, chapter)

        # [3] 통계 계산
        lessons = db.query(Lesson).filter(
            func.upper(Lesson.track) == track.upper(),
            Lesson.chapter == chapter,
            Lesson.lesson_type.in_(["code_fill", "multiple_choice"])
        ).all()

        total_problems = len(lessons)
        wrong_count = count_wrong_answers(db, user_id, track, chapter)

        # [4] 힌트/정답공개 패턴
        hint_usage = build_hint_usage(db, user_id, track, chapter)
        reveal_used = check_reveal_used(db, user_id, track, chapter)

        # [5] 틀린 문제 상세
        wrong_problems = build_wrong_problems_list(db, user_id, track, chapter)

        # [6] Claude API 호출
        ai_report = generate_ai_report(
            chapter_title=chapter_title,
            track=track,
            total_problems=total_problems,
            wrong_count=wrong_count,
            hint_usage=hint_usage,
            wrong_problems=wrong_problems,
            reveal_used=reveal_used
        )

        # [7] progress 집계값과 AI 리포트 병합
        combined_report = {
            "track": track,
            "chapter": chapter,
            "chapterTitle": chapter_title,
            "completedAt": progress.completed_at.isoformat() if progress.completed_at else None,
            "totalProblems": total_problems,
            "xpEarned": progress.xp_earned,
            "wrongCount": wrong_count,
            "hintCount": progress.hint_used,
            **ai_report
        }

        # [8] reports 테이블에 저장
        report = Report(
            user_id=user_id,
            track=track,
            chapter=chapter,
            progress_id=progress.id,
            ai_report=combined_report
        )
        db.add(report)
        db.commit()

        print(f"✅ 리포트 생성 완료: {user_id} - {track} {chapter}")

    except Exception as e:
        print(f"❌ 리포트 생성 실패: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()

    finally:
        db.close()


def get_report_service(
    db: Session,
    user_id: int,
    track: str,
    chapter: str
) -> dict | None:
    """리포트 조회"""

    # progress 조회
    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        func.upper(Progress.track) == track.upper(),
        Progress.chapter == chapter
    ).first()

    if not progress:
        return None

    # reports 조회
    report = db.query(Report).filter(
        Report.user_id == user_id,
        Report.track == track,
        Report.chapter == chapter
    ).first()

    if not report:
        # 아직 생성 중
        return {
            "status": "pending",
            "message": "리포트를 생성 중입니다. 잠시 후 다시 확인해주세요."
        }

    # 완료된 리포트 반환
    total_problems = report.ai_report.get("totalProblems", 0)
    wrong_count = report.ai_report.get("wrongCount", 0)
    correct_count = total_problems - wrong_count

    # 학점 계산
    accuracy_rate = int((correct_count / total_problems) * 100) if total_problems > 0 else 0
    grade = calculate_grade(accuracy_rate)

    return {
        "status": "completed",
        "grade": grade,
        **report.ai_report  # track, chapter, chapterTitle, completedAt, totalProblems, xpEarned, wrongCount, hintCount, weakConcepts, cobotComment 등
    }


def get_reports_list_service(
    db: Session,
    user_id: int,
    track: str
) -> dict | None:
    """트랙 내 모든 완료된 리포트 요약 목록"""

    reports = db.query(Report).filter(
        Report.user_id == user_id,
        Report.track == track
    ).all()

    if not reports:
        return None

    reports_list = []
    for report in reports:
        progress = report.progress
        chapter_title = get_chapter_title(db, track, report.chapter)

        reports_list.append({
            "chapter": report.chapter,
            "title": chapter_title,
            "completedAt": progress.completed_at.isoformat() if progress.completed_at else None
        })

    return {
        "track": track,
        "reports": reports_list
    }


def calculate_grade(accuracy_rate: int) -> str:
    """정답률에 따른 학점 계산"""
    if accuracy_rate >= 95:
        return "A+"
    elif accuracy_rate >= 90:
        return "A"
    elif accuracy_rate >= 85:
        return "B+"
    elif accuracy_rate >= 80:
        return "B"
    elif accuracy_rate >= 75:
        return "B-"
    elif accuracy_rate >= 70:
        return "C+"
    elif accuracy_rate >= 60:
        return "C"
    else:
        return "D"
