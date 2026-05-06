from typing import Optional
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from sqlalchemy.orm import Session

from app.core.config import GOOGLE_CLIENT_ID
from app.models.userModels import User


def verify_google_token(id_token_str: str) -> dict:
    """Google ID Token 검증"""
    try:
        idinfo = id_token.verify_oauth2_token(
            id_token_str,
            google_requests.Request(),
            GOOGLE_CLIENT_ID,
        )
        return idinfo
    except ValueError:
        raise ValueError("유효하지 않은 Google ID 토큰입니다.")


def get_user_by_google_id(db: Session, google_id: str) -> Optional[User]:
    """Google ID로 유저 조회"""
    return db.query(User).filter(User.google_id == google_id).first()


def create_user(db: Session, google_id: str, email: str, gender: str) -> User:
    """신규 유저 생성"""
    user = User(google_id=google_id, email=email, gender=gender)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_nickname(db: Session, user: User, nickname: str) -> User:
    """닉네임 업데이트"""
    user.nickname = nickname
    db.commit()
    db.refresh(user)
    return user
