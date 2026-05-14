from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.userModels import User
from app.schemas.dailySchemas import (
    DailyResponse,
    DailySubmitRequest,
    DailySubmitResponse,
    DailyResultResponse,
)
from app.services.daily.daily_service import (
    get_today_daily_service,
    submit_today_daily_service,
    get_today_daily_result_service,
)


router = APIRouter(
    prefix="/daily",
    tags=["Daily"],
)


@router.get(
    "",
    response_model=DailyResponse,
    summary="오늘의 데일리 문제 조회",
    description="오늘 날짜 기준 데일리 문제 5개를 조회합니다. 오늘 문제가 없으면 새로 생성합니다.",
)
def get_today_daily(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_today_daily_service(
        db=db,
        user_id=current_user.id,
    )


@router.post(
    "/submit",
    response_model=DailySubmitResponse,
    summary="데일리 답안 제출",
    description="오늘의 데일리 5문제를 채점하고 결과를 저장합니다. 틀린 문제는 오답노트에 자동 저장됩니다.",
)
def submit_today_daily(
    request: DailySubmitRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return submit_today_daily_service(
        request=request,
        db=db,
        user_id=current_user.id,
    )


@router.get(
    "/result",
    response_model=DailyResultResponse,
    summary="오늘의 데일리 결과 조회",
    description="오늘 제출한 데일리 결과를 조회합니다.",
)
def get_today_daily_result(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_today_daily_result_service(
        db=db,
        user_id=current_user.id,
    )