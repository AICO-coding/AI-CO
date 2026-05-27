from sqlalchemy.orm import Session
from app.models.lessonModels import Lesson
from app.models.progressModels import Progress
from app.models.problemModels import Problem


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
