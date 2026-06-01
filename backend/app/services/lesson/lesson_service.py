from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.orm.attributes import flag_modified
from app.models.lessonModels import Lesson
from app.models.progressModels import Progress
from app.models.problemModels import Problem
from app.models.noteModels import WrongAnswer
from app.models.userModels import User


def complete_lesson_service(db: Session, user_id: int, track: str, chapter: str, lesson_id: int):
    """concept_image, concept_code, parameter 타입 레슨 완료 처리"""

    normalized_track = track.upper()

    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        return None

    if lesson.lesson_type not in ("concept_image", "concept_code", "parameter"):
        return None

    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        func.upper(Progress.track) == normalized_track,
        Progress.chapter == chapter
    ).first()

    if not progress:
        progress = Progress(
            user_id=user_id,
            track=normalized_track,
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

    total_lessons = db.query(Lesson).filter(
        func.upper(Lesson.track) == normalized_track,
        Lesson.chapter == chapter
    ).count()

    completion_rate = int(len(completed_lessons) / total_lessons * 100) if total_lessons > 0 else 0
    progress.completion_rate = completion_rate

    flag_modified(progress, "report")
    db.commit()

    return {
        "lessonId": lesson_id,
        "isCompleted": True,
        "chapterCompletionRate": completion_rate
    }

def submit_answer_service(db: Session, user_id: int, track: str, chapter: str, lesson_id: int, problem_id: int, answers: dict | int):
    """code_fill, multiple_choice 답안 채점"""
    track = track.upper()
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        return None

    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        return None

    # 답안 비교
    is_correct = False

    if lesson.lesson_type == "code_fill":
        problem_answer = problem.answer
        if isinstance(problem_answer, dict) and problem_answer == answers:
            is_correct = True
    elif lesson.lesson_type == "multiple_choice":
        problem_answer = problem.answer.get("correct_index") if isinstance(problem.answer, dict) else problem.answer
        if problem_answer == answers:
            is_correct = True

    # 오답이고 처음 틀린 경우 오답노트 등록
    if not is_correct:
        existing_wrong_answer = db.query(WrongAnswer).filter(
            WrongAnswer.user_id == user_id,
            WrongAnswer.track_problem_id == problem_id,
        ).first()

        if not existing_wrong_answer:
            wrong_answer = WrongAnswer(
                user_id=user_id,
                track_problem_id=problem_id,
                source_type="learning",
                user_answer=answers if isinstance(answers, dict) else {"selectedIndex": answers},
                is_resolved=False,
                review_count=0,
            )
            db.add(wrong_answer)
            db.commit()

    # 정답인 경우만 progress.report 업데이트
    if is_correct:
        progress = db.query(Progress).filter(
            Progress.user_id == user_id,
            func.upper(Progress.track) == track,
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

        completed_lessons = progress.report.get("completedLessons", [])
        if lesson_id not in completed_lessons:
            completed_lessons.append(lesson_id)
            progress.report["completedLessons"] = completed_lessons

        total_lessons = db.query(Lesson).filter(
            func.upper(Lesson.track) == func.upper(lesson.track),
            Lesson.chapter == lesson.chapter
        ).count()
        progress.completion_rate = int(len(completed_lessons) / total_lessons * 100) if total_lessons > 0 else 0

        flag_modified(progress, "report")
        db.commit()

    result = {"isCorrect": is_correct, "correctAnswer": problem_answer}
    if is_correct and problem.explanation:
        result["explanation"] = problem.explanation
    return result


def get_chapter_lessons_service(db: Session, user_id: int, track: str, chapter: str):
    """특정 트랙/챕터의 lessons 조회 및 진도 정보 합산"""

    normalized_track = track.upper()

    # 1. lessons 조회: track은 대소문자 무시, chapter는 그대로 비교
    lessons = db.query(Lesson).filter(
        func.upper(Lesson.track) == normalized_track,
        Lesson.chapter == chapter
    ).order_by(Lesson.order_index.asc()).all()

    # 결과 없으면 404
    if not lessons:
        return None

    # 2. progress 조회: track은 대소문자 무시, chapter는 그대로 비교
    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        func.upper(Progress.track) == normalized_track,
        Progress.chapter == chapter
    ).first()

    completion_rate = progress.completion_rate if progress else 0
    last_lesson_id = progress.last_lesson_id if progress else None

    completed_lessons = set()
    problem_progress_map = {}
    if progress and progress.report:
        completed_ids = progress.report.get("completedLessons", [])
        completed_lessons = set(completed_ids)
        for p in progress.report.get("problems", []):
            problem_progress_map[p["problemId"]] = p

    lesson_responses = []

    for lesson in lessons:
        is_completed = lesson.id in completed_lessons
        content = dict(lesson.content) if lesson.content else {}

        lesson_data = {
            "lessonId": lesson.id,
            "lessonType": lesson.lesson_type,
            "orderIndex": lesson.order_index,
            "isCompleted": is_completed,
            "part": lesson.part,
        }

        if lesson.lesson_type in ("concept_image", "concept_code", "parameter"):
            markdown_url = content.pop("markdownUrl", None)
            image_url = content.pop("imageUrl", None)

            lesson_data["markdownUrl"] = markdown_url

            if image_url:
                lesson_data["imageUrl"] = image_url

            lesson_data["content"] = content if content else None

        elif lesson.lesson_type in ("code_fill", "multiple_choice"):
            lesson_data["problemId"] = lesson.problem_id
            lesson_data["content"] = content
            problem = db.query(Problem).filter(Problem.id == lesson.problem_id).first()
            lesson_data["hints"] = problem.hints if problem else None
            p_entry = problem_progress_map.get(lesson.problem_id, {})
            lesson_data["usedHintLevels"] = p_entry.get("usedHintLevels", [])

        lesson_responses.append(lesson_data)

    return {
        "track": normalized_track,
        "chapter": chapter,
        "completionRate": completion_rate,
        "lastLessonId": last_lesson_id,
        "lessons": lesson_responses,
    }


def hint_service(db: Session, user_id: int, track: str, chapter: str, problem_id: int, hint_level: int):
    """힌트 사용 처리 - 힌트 사용 시 즉시 5 XP 차감"""
    track = track.upper()
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        return None

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        func.upper(Progress.track) == track,
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
        return {
            "xpDeducted": 0,
            "totalXP": user.xp,
            "hintsUsed": problem_entry["hintsUsed"]
        }

    used_levels.append(hint_level)
    problem_entry["usedHintLevels"] = used_levels
    problem_entry["hintsUsed"] = len(used_levels)

    progress.report["problems"] = problems
    progress.hint_used = sum(p["hintsUsed"] for p in problems)

    # 힌트 사용 즉시 5 XP 차감
    user.xp = max(user.xp - 5, 0)

    flag_modified(progress, "report")
    db.commit()

    return {
        "xpDeducted": -5,
        "totalXP": user.xp,
        "hintsUsed": problem_entry["hintsUsed"]
    }


def reveal_answer_service(db: Session, user_id: int, track: str, chapter: str, problem_id: int):
    """정답 공개 처리 - 정답 공개 시 즉시 5 XP 차감"""
    track = track.upper()
    problem = db.query(Problem).filter(Problem.id == problem_id).first()
    if not problem:
        return None

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        func.upper(Progress.track) == track,
        Progress.chapter == chapter
    ).first()

    if not progress:
        return {"error": "힌트를 최소 2회 이상 사용해야 정답을 공개할 수 있습니다."}

    if not progress.report:
        progress.report = {}

    problems = progress.report.get("problems", [])
    problem_entry = next((p for p in problems if p["problemId"] == problem_id), None)

    hints_used = problem_entry.get("hintsUsed", 0) if problem_entry else 0
    if hints_used < 2:
        return {"error": "힌트를 최소 2회 이상 사용해야 정답을 공개할 수 있습니다."}

    already_revealed = problem_entry.get("usedReveal", False) if problem_entry else False
    if already_revealed:
        return {"error": "이미 정답을 공개한 문제입니다."}

    problem_entry["usedReveal"] = True
    progress.report["problems"] = problems

    # 정답 공개 즉시 5 XP 차감
    user.xp = max(user.xp - 5, 0)

    flag_modified(progress, "report")
    db.commit()

    result = {
        "answer": problem.answer,
        "xpDeducted": -5,
        "totalXP": user.xp
    }
    if problem.explanation:
        result["explanation"] = problem.explanation
    return result


def complete_chapter_service(db: Session, user_id: int, track: str, chapter: str):
    """챕터 완료 처리"""
    track = track.upper()

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        func.upper(Progress.track) == track,
        Progress.chapter == chapter
    ).first()

    if not progress:
        return None

    if not progress.report:
        progress.report = {}

    # 모든 레슨이 완료됐는지 확인
    completed_lessons = set(progress.report.get("completedLessons", []))
    all_lessons = db.query(Lesson).filter(
        func.upper(Lesson.track) == track,
        Lesson.chapter == chapter
    ).count()

    if len(completed_lessons) < all_lessons:
        return {"error": "완료하지 않은 레슨이 있습니다."}

    # 이미 완료된 챕터면 중복 XP 지급 방지
    if progress.is_completed:
        return {"error": "이미 완료된 챕터입니다."}

    # 챕터 완료 시 힌트/정답공개 여부와 무관하게 50 XP 지급
    CHAPTER_COMPLETION_XP = 50
    problems = progress.report.get("problems", [])
    total_hints_used = sum(p.get("hintsUsed", 0) for p in problems)

    # 진도 업데이트
    progress.is_completed = True
    progress.xp_earned = CHAPTER_COMPLETION_XP
    progress.hint_used = total_hints_used

    # 유저 총 XP 누적
    user.xp += CHAPTER_COMPLETION_XP

    db.commit()

    return {
        "chapter": chapter,
        "isCompleted": True,
        "chapterXP": CHAPTER_COMPLETION_XP,
        "xpDeducted": 0,
        "xpEarned": CHAPTER_COMPLETION_XP,
        "hintUsed": total_hints_used,
    }
