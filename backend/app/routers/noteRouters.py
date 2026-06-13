from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.userModels import User
from app.schemas.noteSchemas import (
    WrongAnswerListResponse,
    WrongAnswerDetailResponse,
    ReviewProblemResponse,
    ReviewSubmitRequest,
    ReviewSubmitResponse,
    DeleteWrongAnswerResponse,
)
from app.services.note.note_service import (
    get_wrong_answers_service,
    get_review_wrong_answers_service,
    submit_review_answers_service,
    get_wrong_answer_detail_service,
    delete_wrong_answer_service,
)


router = APIRouter(
    prefix="/wrong-answers",
    tags=["Wrong Answers"],
)



@router.get(
    "",
    response_model=WrongAnswerListResponse,
    summary="오답 목록 조회",
)
def get_wrong_answers(
    track: str | None = Query(default=None, description="트랙명 예: ML, CV, NLP"),
    source_type: str | None = Query(default=None, description="오답 발생 위치: learning 또는 daily"),
    is_resolved: bool | None = Query(default=None, description="복습 해결 여부"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_wrong_answers_service(
        db=db,
        user_id=current_user.id,
        track=track,
        source_type=source_type,
        is_resolved=is_resolved,
    )


@router.get(
    "/review",
    response_model=ReviewProblemResponse,
    summary="오답 복습 문제 조회",
)
def get_review_wrong_answers(
    track: str | None = Query(default=None, description="트랙명 예: ML"),
    source_type: str | None = Query(default=None, description="오답 발생 위치: learning 또는 daily"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_review_wrong_answers_service(
        db=db,
        user_id=current_user.id,
        track=track,
        source_type=source_type,
    )


@router.post(
    "/review",
    response_model=ReviewSubmitResponse,
    summary="오답 복습 제출",
)
def submit_review_answers(
    request: ReviewSubmitRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return submit_review_answers_service(
        request=request,
        db=db,
        user_id=current_user.id,
    )


@router.get(
    "/{wrong_answer_id}",
    response_model=WrongAnswerDetailResponse,
    summary="오답 상세 조회",
)
def get_wrong_answer_detail(
    wrong_answer_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_wrong_answer_detail_service(
        wrong_answer_id=wrong_answer_id,
        db=db,
        user_id=current_user.id,
    )


@router.delete(
    "/{wrong_answer_id}",
    response_model=DeleteWrongAnswerResponse,
    summary="오답 삭제",
)
def delete_wrong_answer(
    wrong_answer_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return delete_wrong_answer_service(
        wrong_answer_id=wrong_answer_id,
        db=db,
        user_id=current_user.id,
    )