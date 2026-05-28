from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.core.database import get_db
from app.models.userModels import User
from app.schemas.userSchemas import UserResponse, XpResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(
    current_user: User = Depends(get_current_user),
):
    """현재 유저 정보 조회 (userId, nickname, xp, createdAt)"""
    return UserResponse(
        id=current_user.id,
        nickname=current_user.nickname,
        xp=current_user.xp,
        createdAt=current_user.created_at,
    )


@router.get("/xp", response_model=XpResponse, status_code=status.HTTP_200_OK)
def get_xp(
    current_user: User = Depends(get_current_user),
):
    """현재 유저의 총 XP 및 트랙별 XP 조회"""
    return XpResponse(
        xp=current_user.xp,
        tracks={"ML-분류": 0, "ML-회귀": 0, "CV": 0, "NLP": 0},
    )
