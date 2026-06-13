from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
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
from app.services.report.report_service import generate_report_background

router = APIRouter(prefix="/tracks", tags=["Tracks"])


@router.get("", summary="비로그인용 전체 트랙 목록 조회")
def get_public_tracks():
    return {
        "tracks": [
            {
                "track": "ML-분류",
                "title": "머신러닝 - 분류",
                "description": "분류 알고리즘의 기본 개념과 모델 학습 과정을 학습합니다.",
            },
            {
                "track": "ML-회귀",
                "title": "머신러닝 - 회귀",
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


@router.post(
    "/{track}/chapters/{chapter}/complete",
    response_model=ChapterCompleteResponse,
    summary="챕터 완료",
    responses={
        200: {
            "description": "챕터 완료 성공",
            "content": {
                "application/json": {
                    "examples": {
                        "첫 학습 완료": {
                            "summary": "첫 학습 완료 (XP 지급)",
                            "value": {
                                "chapter": "ch1",
                                "isCompleted": True,
                                "isFirstCompletion": True,
                                "baseXP": 50,
                                "xpDeducted": 10,
                                "xpEarned": 40,
                                "hintUsed": 1,
                                "revealUsed": 1,
                            },
                        },
                        "복습 완료": {
                            "summary": "복습 완료 (이번 복습에서 차감된 XP 포함)",
                            "value": {
                                "chapter": "ch1",
                                "isCompleted": True,
                                "isFirstCompletion": False,
                                "xpDeducted": 10,
                                "hintUsed": 1,
                                "revealUsed": 1,
                            },
                        },
                    }
                }
            },
        }
    },
)
def complete_chapter(
    track: str,
    chapter: str,
    background_tasks: BackgroundTasks,
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

    if result.get("isFirstCompletion"):
        background_tasks.add_task(
            generate_report_background,
            user_id=current_user.id,
            track=track,
            chapter=chapter
        )

    return result