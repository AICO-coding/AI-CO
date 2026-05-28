from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Union
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


# 비로그인용 전체 트랙 목록 조회
@router.get("", summary="전체 트랙 목록 조회")
def get_public_tracks():
    """
    로그인 없이 전체 트랙 목록을 조회합니다.

    프론트에서 메인 화면, 트랙 선택 화면 등에서 사용할 수 있습니다.
    유저별 진도 정보는 포함하지 않습니다.
    """

    return {
        "tracks": [
            {
                "track": "ML-분류",
                "title": "머신러닝 - 분류",
                "description": "분류 알고리즘의 기본 개념과 모델 학습 과정을 학습합니다.",
            },
            {
                "track": "ML-회기",
                "title": "머신러닝 - 회기",
                "description": "회귀 알고리즘의 기본 개념과 예측 모델 학습 과정을 학습합니다.",
            },
            {
                "track": "CV",
                "title": "컴퓨터 비전",
                "description": "이미지 처리와 컴퓨터 비전 모델의 기본 개념을 학습합니다.",
            },
            {
                "track": "NLP",
                "title": "자연어 처리",
                "description": "텍스트 전처리와 자연어 처리 모델의 기본 개념을 학습합니다.",
            },
        ]
    }


#  로그인 유저용 전체 트랙 진도 조회
@router.get(
    "/progress",
    response_model=AllTracksResponse,
    summary="전체 트랙 진도 조회",
)
def get_all_tracks_progress(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_all_progress_service(db=db, user_id=current_user.id)


# 특정 트랙 챕터 목록 및 진도 조회
@router.get(
    "/{track}/chapters",
    response_model=TrackChaptersResponse,
    summary="트랙 챕터 조회",
)
def get_track_chapters(
    track: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    result = get_track_chapters_service(
        db=db,
        user_id=current_user.id,
        track=track,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="유효하지 않은 트랙입니다. ML, CV, NLP 중 하나를 입력하세요.",
        )
    return result


# 특정 챕터의 레슨 목록 조회
@router.get(
    "/{track}/chapters/{chapter}/lessons",
    response_model=ChapterLessonsResponse,
    summary="챕터 레슨 조회",
)
def get_chapter_lessons(
    track: str,
    chapter: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = get_chapter_lessons_service(
        db=db,
        user_id=current_user.id,
        track=track,
        chapter=chapter,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 트랙/챕터의 lessons이 없습니다.",
        )

    return result


# 콘텐츠형 레슨 완료 처리
@router.post(
    "/{track}/chapters/{chapter}/lessons/{lessonId}/complete",
    response_model=LessonCompleteResponse,
    summary="콘텐츠형 레슨 완료",
)
def complete_lesson(
    track: str,
    chapter: str,
    lessonId: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = complete_lesson_service(
        db=db,
        user_id=current_user.id,
        track=track,
        chapter=chapter,
        lesson_id=lessonId,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 레슨입니다.",
        )

    return result


# 답안 제출
@router.post(
    "/{track}/chapters/{chapter}/submit",
    response_model=SubmitResponse,
    summary="답안 제출",
)
def submit_answer(
    track: str,
    chapter: str,
    payload: Union[CodeFillSubmit, MultipleChoiceSubmit],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if isinstance(payload, CodeFillSubmit):
        answers = payload.answers
    else:
        answers = payload.answer

    result = submit_answer_service(
        db=db,
        user_id=current_user.id,
        track=track,
        chapter=chapter,
        lesson_id=payload.lessonId,
        problem_id=payload.problemId,
        answers=answers,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 문제입니다.",
        )

    return result


# 힌트 사용
@router.post(
    "/{track}/chapters/{chapter}/hint",
    response_model=HintResponse,
    summary="힌트 사용",
)
def use_hint(
    track: str,
    chapter: str,
    payload: HintRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = hint_service(
        db=db,
        user_id=current_user.id,
        track=track,
        chapter=chapter,
        problem_id=payload.problemId,
        hint_level=payload.hintLevel,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 문제입니다.",
        )

    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result["error"],
        )

    return result


# 정답 공개
@router.post(
    "/{track}/chapters/{chapter}/lessons/{lessonId}/reveal",
    response_model=RevealResponse,
    summary="정답 공개",
)
def reveal_answer(
    track: str,
    chapter: str,
    lessonId: int,
    payload: RevealRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = reveal_answer_service(
        db=db,
        user_id=current_user.id,
        track=track,
        chapter=chapter,
        problem_id=payload.problemId,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 문제입니다.",
        )

    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result["error"],
        )

    return result


# 챕터 완료
@router.post(
    "/{track}/chapters/{chapter}/complete",
    response_model=ChapterCompleteResponse,
    summary="챕터 완료",
)
def complete_chapter(
    track: str,
    chapter: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = complete_chapter_service(
        db=db,
        user_id=current_user.id,
        track=track,
        chapter=chapter,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 챕터입니다.",
        )

    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result["error"],
        )

    return result