from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.userModels import User
from app.schemas.lessonSchemas import (
    ChapterLessonsResponse,
    CodeFillSubmit,
    MultipleChoiceSubmit,
    SubmitResponse,
    LessonCompleteResponse,
)
from typing import Union
from app.schemas.progressSchemas import AllTracksResponse, TrackChaptersResponse
from app.services.lesson.lesson_service import (
    get_chapter_lessons_service,
    complete_lesson_service,
    submit_answer_service,
)
from app.services.progress.progress_service import (
    get_all_progress_service,
    get_track_chapters_service,
)

router = APIRouter(prefix="/tracks", tags=["Tracks"])


@router.get("", response_model=AllTracksResponse)
def get_all_tracks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """유저의 전체 트랙별 학습 진도 요약 조회"""
    return get_all_progress_service(db=db, user_id=current_user.id)


@router.get("/{track}/chapters", response_model=TrackChaptersResponse)
def get_track_chapters(
    track: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """특정 트랙의 챕터 목록 및 진도 조회"""
    result = get_track_chapters_service(db=db, user_id=current_user.id, track=track)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="유효하지 않은 트랙입니다. ML, CV, NLP 중 하나를 입력하세요."
        )
    return result


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


@router.post("/{track}/chapters/{chapter}/lessons/{lessonId}/complete", response_model=LessonCompleteResponse)
def complete_lesson(
    track: str,
    chapter: str,
    lessonId: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """레슨 완료 처리 (concept_image, concept_code, parameter 타입만)"""
    result = complete_lesson_service(
        db=db,
        user_id=current_user.id,
        track=track,
        chapter=chapter,
        lesson_id=lessonId
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 레슨입니다."
        )

    return result


@router.post("/{track}/chapters/{chapter}/submit", response_model=SubmitResponse)
def submit_answer(
    track: str,
    chapter: str,
    payload: Union[CodeFillSubmit, MultipleChoiceSubmit],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """답안 제출 및 채점 (code_fill, multiple_choice)"""

    # 타입별 답안 처리
    if isinstance(payload, CodeFillSubmit):
        answers = payload.answers
    else:  # MultipleChoiceSubmit
        answers = payload.answer

    result = submit_answer_service(
        db=db,
        user_id=current_user.id,
        track=track,
        chapter=chapter,
        lesson_id=payload.lessonId,
        problem_id=payload.problemId,
        answers=answers
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 문제입니다."
        )

    return result
