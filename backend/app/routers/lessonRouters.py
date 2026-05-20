from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.userModels import User
from app.schemas.lessonSchemas import ChapterLessonsResponse
from app.services.lesson.lesson_service import get_chapter_lessons_service

router = APIRouter(prefix="/tracks", tags=["Tracks"])


@router.get("/{track}/chapters/{chapter}/lessons", response_model=ChapterLessonsResponse)
def get_chapter_lessons(
    track: str,
    chapter: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """특정 트랙/챕터의 레슨 목록 조회"""
    result = get_chapter_lessons_service(
        db=db,
        user_id=current_user.id,
        track=track,
        chapter=chapter
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 트랙/챕터의 lessons이 없습니다."
        )

    return result
