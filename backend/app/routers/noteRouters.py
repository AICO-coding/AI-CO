from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.userModels import User
from app.schemas.noteSchemas import (
    WrongAnswerCreateRequest,
    WrongAnswerListResponse,
    WrongAnswerDetailResponse,
    ReviewProblemResponse,
    ReviewSubmitRequest,
    ReviewSubmitResponse,
    DeleteWrongAnswerResponse,
)
from app.services.note.note_service import (
    create_wrong_answer_service,
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


@router.post(
    "",
    response_model=WrongAnswerDetailResponse,
    summary="오답 등록",
    description="사용자가 틀린 문제를 오답노트에 등록합니다.",
)
def create_wrong_answer(
    request: WrongAnswerCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_wrong_answer_service(
        request=request,
        db=db,
        user_id=current_user.id,
    )


@router.get(
    "",
    response_model=WrongAnswerListResponse,
    summary="오답 목록 조회",
    description="내 오답노트 목록을 조회합니다. track, source_type, is_resolved로 필터링할 수 있습니다.",
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
    description="아직 해결되지 않은 내 오답을 복습용 문제로 조회합니다.",
)
def get_review_wrong_answers(
    limit: int = Query(default=5, ge=1, le=20, description="조회할 문제 수"),
    track: str | None = Query(default=None, description="트랙명 예: ML"),
    source_type: str | None = Query(default=None, description="오답 발생 위치: learning 또는 daily"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_review_wrong_answers_service(
        db=db,
        user_id=current_user.id,
        limit=limit,
        track=track,
        source_type=source_type,
    )


@router.post(
    "/review",
    response_model=ReviewSubmitResponse,
    summary="오답 복습 제출",
    description="오답 복습 답안을 제출하고 정답 여부를 확인합니다. XP는 부여하지 않습니다.",
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
    description="특정 오답의 상세 정보와 문제 내용을 조회합니다.",
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
    description="오답노트에서 특정 오답 기록을 삭제합니다.",
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