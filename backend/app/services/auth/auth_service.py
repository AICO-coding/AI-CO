from typing import Optional
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from sqlalchemy.orm import Session
from app.core.config import GOOGLE_CLIENT_ID
from app.models.userModels import User


# Google ID Token 검증
def verify_google_token(id_token_str: str) -> dict:
    if not id_token_str:
        raise ValueError("Google ID Token이 비어 있습니다.")

    if not GOOGLE_CLIENT_ID:
        raise ValueError("서버의 GOOGLE_CLIENT_ID가 설정되지 않았습니다.")

    try:
        idinfo = id_token.verify_oauth2_token(
            id_token_str,
            google_requests.Request(),
            GOOGLE_CLIENT_ID,
            clock_skew_in_seconds=10,
        )

        return idinfo

    except ValueError as e:
        print("Google token verify error:", repr(e))
        print("GOOGLE_CLIENT_ID in server:", GOOGLE_CLIENT_ID)
        print("received token startswith:", id_token_str[:30] if id_token_str else None)

        raise ValueError(str(e))
    

def get_user_by_google_id(db: Session, google_id: str) -> Optional[User]:
    """Google ID로 유저 조회"""
    return db.query(User).filter(User.google_id == google_id).first()


def create_user(
    db: Session,
    google_id: str,
    email: str,
    gender: str = "UNKNOWN",
) -> User:
    user = User(
        google_id=google_id,
        email=email,
        gender=gender,
        xp=100,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# 닉네임 업데이트
def update_nickname(db: Session, user: User, nickname: str) -> User:
    user.nickname = nickname

    db.commit()
    db.refresh(user)

    return user