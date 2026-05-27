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
    HintRequest,
    HintResponse,
    RevealRequest,
    RevealResponse,
    ChapterCompleteResponse,
)
from typing import Union
from app.schemas.progressSchemas import AllTracksResponse, TrackChaptersResponse
from app.services.lesson.lesson_service import (
    get_chapter_lessons_service,
    complete_lesson_service,
    submit_answer_service,
    hint_service,
    reveal_answer_service,
    complete_chapter_service,
)
from app.services.progress.progress_service import (
    get_all_progress_service,
    get_track_chapters_service,
)

router = APIRouter(prefix="/tracks", tags=["Tracks"])


@router.get("", response_model=AllTracksResponse, summary="전체 트랙 진도 조회")
def get_all_tracks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """유저의 전체 트랙별 학습 진도 요약 조회"""
    return get_all_progress_service(db=db, user_id=current_user.id)


@router.get("/{track}/chapters", response_model=TrackChaptersResponse, summary="트랙 챕터 조회")
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


@router.get("/{track}/chapters/{chapter}/lessons", response_model=ChapterLessonsResponse, summary="챕터 레슨 조회")
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


@router.post("/{track}/chapters/{chapter}/lessons/{lessonId}/complete", response_model=LessonCompleteResponse, summary="콘텐츠형 레슨 완료")
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


@router.post("/{track}/chapters/{chapter}/submit", response_model=SubmitResponse, summary="답안 제출")
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


@router.post("/{track}/chapters/{chapter}/hint", response_model=HintResponse, summary="힌트 사용")
def use_hint(
    track: str,
    chapter: str,
    payload: HintRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """힌트 사용"""
    result = hint_service(
        db=db,
        user_id=current_user.id,
        track=track,
        chapter=chapter,
        problem_id=payload.problemId,
        hint_level=payload.hintLevel
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 문제입니다."
        )

    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result["error"]
        )

    return result


@router.post("/{track}/chapters/{chapter}/lessons/{lessonId}/reveal", response_model=RevealResponse, summary="정답 공개")
def reveal_answer(
    track: str,
    chapter: str,
    lessonId: int,
    payload: RevealRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """정답 공개"""
    result = reveal_answer_service(
        db=db,
        user_id=current_user.id,
        track=track,
        chapter=chapter,
        problem_id=payload.problemId
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 문제입니다."
        )

    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result["error"]
        )

    return result


@router.post("/{track}/chapters/{chapter}/complete", response_model=ChapterCompleteResponse, summary="챕터 완료")
def complete_chapter(
    track: str,
    chapter: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """챕터 완료"""
    result = complete_chapter_service(
        db=db,
        user_id=current_user.id,
        track=track,
        chapter=chapter
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 챕터입니다."
        )

    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result["error"]
        )

    return result
