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


@router.get("", response_model=DailyResponse, summary="오늘의 데일리 문제 조회")
def get_today_daily(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    오늘의 데일리 문제 5개를 조회합니다.

**동작 방식**
- 오늘 처음 호출하면 문제 5개가 자동 생성되어 저장됨
- 이미 생성된 경우 동일한 문제를 반환 (하루에 문제가 바뀌지 X)

**프론트 분기 처리**
- `isCompleted === false` → 문제 풀기 화면
- `isCompleted === true` → 이미 오늘 제출 완료한 상태. `GET /daily/result` 호출해 결과 화면 보여줌.

**만료**
- 데일리 문제는 KST 기준 당일 23:59:59에 만료됨 (`expiresAt` 참고)
    """
    return get_today_daily_service(db=db, user_id=current_user.id)


@router.post("/submit", response_model=DailySubmitResponse, summary="데일리 답안 제출")
def submit_today_daily(
    request: DailySubmitRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    오늘의 데일리 5문제 전체에 대한 답안을 제출하고 채점합니다.

    - 5개 문제를 모두 제출해야 합니다. 일부만 제출 시 400 에러
    - 오늘 이미 제출한 경우 재제출 불가 (409 에러)
    - 맞힌 문제 1개당 20 XP 지급
    - 틀린 문제는 오답노트에 자동 저장되며, 결과의 `wrongAnswerId`로 참조 가능
    """
    return submit_today_daily_service(request=request, db=db, user_id=current_user.id)


@router.get("/result", response_model=DailyResultResponse, summary="오늘의 데일리 결과 조회")
def get_today_daily_result(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    오늘 제출한 데일리 채점 결과를 조회합니다.

    - `isCompleted: true`인 경우 이 API로 결과 화면 구성
    - `results`에 문제별 정오 여부(`isCorrect`), 정답, 해설이 포함됨
    - 오늘 미제출 시 404 에러
    """
    return get_today_daily_result_service(db=db, user_id=current_user.id)
