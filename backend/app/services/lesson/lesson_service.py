from sqlalchemy.orm import Session
from app.models.lessonModels import Lesson
from app.models.progressModels import Progress
from app.models.problemModels import Problem
from app.models.noteModels import WrongAnswer


def complete_lesson_service(db: Session, user_id: int, track: str, chapter: str, lesson_id: int):
    """concept_image, concept_code, parameter 타입 레슨 완료 처리"""
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        return None

    # concept_image, concept_code, parameter만 완료 가능
    if lesson.lesson_type not in ("concept_image", "concept_code", "parameter"):
        return None

    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        Progress.track == track,
        Progress.chapter == chapter
    ).first()

    if not progress:
        progress = Progress(
            user_id=user_id,
            track=track,
            chapter=chapter,
            report={"completedLessons": []}
        )
        db.add(progress)

    if not progress.report:
        progress.report = {}

    completed_lessons = progress.report.get("completedLessons", [])
    if lesson_id not in completed_lessons:
        completed_lessons.append(lesson_id)
        progress.report["completedLessons"] = completed_lessons

    # 전체 lessons 개수 조회
    total_lessons = db.query(Lesson).filter(
        Lesson.track == track,
        Lesson.chapter == chapter
    ).count()

    # completion_rate 계산
    completion_rate = int(len(completed_lessons) / total_lessons * 100) if total_lessons > 0 else 0
    progress.completion_rate = completion_rate

    db.commit()

    return {
        "lessonId": lesson_id,
        "isCompleted": True,
        "chapterCompletionRate": completion_rate
    }


def submit_answer_service(db: Session, user_id: int, track: str, chapter: str, lesson_id: int, problem_id: int, answers: dict | int):
    """code_fill, multiple_choice 답안 채점"""
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        return None

    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        return None

    # 답안 비교
    is_correct = False

    if lesson.lesson_type == "code_fill":
        # answers는 dict
        problem_answer = problem.answer
        if isinstance(problem_answer, dict) and problem_answer == answers:
            is_correct = True
    elif lesson.lesson_type == "multiple_choice":
        # answer는 int
        problem_answer = problem.answer.get("correctAnswer") if isinstance(problem.answer, dict) else problem.answer
        if problem_answer == answers:
            is_correct = True

    # 정답인 경우만 progress.report 업데이트
    if is_correct:
        progress = db.query(Progress).filter(
            Progress.user_id == user_id,
            Progress.track == track,
            Progress.chapter == chapter
        ).first()

        if not progress:
            progress = Progress(
                user_id=user_id,
                track=track,
                chapter=chapter,
                report={"problems": []}
            )
            db.add(progress)

        if not progress.report:
            progress.report = {}

        problems = progress.report.get("problems", [])
        problem_entry = next((p for p in problems if p["problemId"] == problem_id), None)

        if not problem_entry:
            problem_entry = {"problemId": problem_id, "hintsUsed": 0, "usedReveal": False}
            problems.append(problem_entry)

        progress.report["problems"] = problems
        db.commit()

    return {"isCorrect": is_correct}


def get_chapter_lessons_service(db: Session, user_id: int, track: str, chapter: str):
    """특정 트랙/챕터의 lessons 조회 및 진도 정보 합산"""

    # 1. lessons 조회 (track, chapter 필터, order_index ASC)
    lessons = db.query(Lesson).filter(
        Lesson.track == track,
        Lesson.chapter == chapter
    ).order_by(Lesson.order_index.asc()).all()

    # 결과 없으면 404
    if not lessons:
        return None

    # 2. progress 조회 (user_id, track, chapter)
    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        Progress.track == track,
        Progress.chapter == chapter
    ).first()

    # 진도 정보 추출
    completion_rate = progress.completion_rate if progress else 0
    last_lesson_id = progress.last_lesson_id if progress else None

    # 3. isCompleted 계산 (progress.report JSONB)
    completed_lessons = set()
    if progress and progress.report:
        completed_ids = progress.report.get("completedLessons", [])
        completed_lessons = set(completed_ids)

    # 4. lessons 변환
    lesson_responses = []
    for lesson in lessons:
        is_completed = lesson.id in completed_lessons
        content = dict(lesson.content) if lesson.content else {}

        lesson_data = {
            "lessonId": lesson.id,
            "lessonType": lesson.lesson_type,
            "title": lesson.title,
            "orderIndex": lesson.order_index,
            "isCompleted": is_completed,
            "part": lesson.part,
        }

        # concept_image/concept_code/parameter → markdownUrl 최상위 꺼내기
        if lesson.lesson_type in ("concept_image", "concept_code", "parameter"):
            markdown_url = content.pop("markdownUrl", None)
            image_url = content.pop("imageUrl", None)

            lesson_data["markdownUrl"] = markdown_url
            if image_url:
                lesson_data["imageUrl"] = image_url

            lesson_data["content"] = content if content else None

        # code_fill/multiple_choice → problemId 최상위, content 그대로
        elif lesson.lesson_type in ("code_fill", "multiple_choice"):
            lesson_data["problemId"] = lesson.problem_id
            lesson_data["content"] = content

        lesson_responses.append(lesson_data)

    return {
        "track": track,
        "chapter": chapter,
        "completionRate": completion_rate,
        "lastLessonId": last_lesson_id,
        "lessons": lesson_responses
    }


def hint_service(db: Session, user_id: int, track: str, chapter: str, problem_id: int, hint_level: int):
    """힌트 사용 처리"""
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        return None

    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        Progress.track == track,
        Progress.chapter == chapter
    ).first()

    if not progress:
        progress = Progress(
            user_id=user_id,
            track=track,
            chapter=chapter,
            report={"problems": []}
        )
        db.add(progress)

    if not progress.report:
        progress.report = {}

    problems = progress.report.get("problems", [])
    problem_entry = next((p for p in problems if p["problemId"] == problem_id), None)

    if not problem_entry:
        problem_entry = {"problemId": problem_id, "hintsUsed": 0, "usedReveal": False, "usedHintLevels": []}
        problems.append(problem_entry)

    used_levels = problem_entry.get("usedHintLevels", [])
    if hint_level in used_levels:
        return {"error": "이미 해당 레벨의 힌트를 사용했습니다."}

    used_levels.append(hint_level)
    problem_entry["usedHintLevels"] = used_levels
    problem_entry["hintsUsed"] = len(used_levels)

    progress.report["problems"] = problems
    progress.hint_used = sum(p["hintsUsed"] for p in problems)

    db.commit()

    xp_deducted = -5
    return {
        "xpDeducted": xp_deducted,
        "hintsUsed": problem_entry["hintsUsed"]
    }


def reveal_answer_service(db: Session, user_id: int, track: str, chapter: str, problem_id: int):
    """정답 공개 처리"""
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        return None

    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        Progress.track == track,
        Progress.chapter == chapter
    ).first()

    if not progress:
        return None

    if not progress.report:
        progress.report = {}

    problems = progress.report.get("problems", [])
    problem_entry = next((p for p in problems if p["problemId"] == problem_id), None)

    if not problem_entry:
        return None

    hints_used = problem_entry.get("hintsUsed", 0)
    if hints_used < 2:
        return {"error": "힌트를 최소 2회 이상 사용해야 정답을 공개할 수 있습니다."}

    problem_entry["usedReveal"] = True
    progress.report["problems"] = problems

    wrong_answer = WrongAnswer(
        user_id=user_id,
        track_problem_id=problem_id,
        source_type="learning",
        user_answer={"revealed": True}
    )
    db.add(wrong_answer)

    db.commit()

    return {
        "answer": problem.answer,
        "xpDeducted": -10
    }


def complete_chapter_service(db: Session, user_id: int, track: str, chapter: str):
    """챕터 완료 처리"""
    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        Progress.track == track,
        Progress.chapter == chapter
    ).first()

    if not progress:
        return None

    if not progress.report:
        progress.report = {}

    # 모든 레슨이 완료됐는지 확인
    completed_lessons = set(progress.report.get("completedLessons", []))
    all_lessons = db.query(Lesson).filter(
        Lesson.track == track,
        Lesson.chapter == chapter
    ).count()

    if len(completed_lessons) < all_lessons:
        return {"error": "완료하지 않은 레슨이 있습니다."}

    # XP 계산
    problems = progress.report.get("problems", [])
    total_hints_used = sum(p.get("hintsUsed", 0) for p in problems)
    total_reveal_used = sum(1 for p in problems if p.get("usedReveal", False))

    base_xp = 100
    xp_deducted = (total_hints_used * 5) + (total_reveal_used * 10)
    xp_earned = base_xp - xp_deducted

    # 진도 업데이트
    progress.is_completed = True
    progress.xp_earned = xp_earned
    progress.hint_used = total_hints_used

    db.commit()

    return {
        "chapter": chapter,
        "isCompleted": True,
        "chapterXP": base_xp,
        "xpDeducted": xp_deducted,
        "xpEarned": xp_earned,
        "hintUsed": total_hints_used
    }
