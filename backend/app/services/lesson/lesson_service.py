from sqlalchemy.orm import Session
from app.models.lessonModels import Lesson
from app.models.progressModels import Progress


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
