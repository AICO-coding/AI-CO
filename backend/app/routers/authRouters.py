from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from app.core.config import JWT_SECRET_KEY, JWT_ALGORITHM
from app.core.database import get_db
from app.core.security import create_access_token, create_refresh_token, get_current_user
from app.models.userModels import User
from app.schemas.userSchemas import (
    GoogleLoginRequest,
    GoogleLoginResponse,
    GoogleNewUserResponse,
    SignupRequest,
    SignupResponse,
    NicknameRequest,
    NicknameResponse,
    RefreshRequest,
    RefreshResponse,
)
from app.services.auth.auth_service import (
    verify_google_token,
    get_user_by_google_id,
    create_user,
    update_nickname,
)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/google/login", summary="Google ID Token 검증 후 로그인")
def google_login(
    body: GoogleLoginRequest,
    db: Session = Depends(get_db),
) -> GoogleLoginResponse | GoogleNewUserResponse:
    """
    Google ID Token으로 로그인
    - 기존 회원: userId, nickname, accessToken, refreshToken 반환
    - 신규 회원: googleId 반환 (회원가입 필요)
    """
    try:
        idinfo = verify_google_token(body.idToken)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유효하지 않은 Google ID 토큰입니다.",
        )

    google_id: str = idinfo["sub"]

    # 유저 조회
    user = get_user_by_google_id(db, google_id)
    
    if user is None:
        # 신규 회원: googleId만 반환
        return GoogleNewUserResponse(googleId=google_id)

    # 기존 회원: 토큰 발급
    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    return GoogleLoginResponse(
        userId=user.id,
        nickname=user.nickname,
        accessToken=access_token,
        refreshToken=refresh_token,
    )


@router.post("/google/signup", response_model=SignupResponse, status_code=status.HTTP_201_CREATED)
def google_signup(
    body: SignupRequest,
    db: Session = Depends(get_db),
):
    """신규 회원 가입"""
    # 필수값 검증
    if not body.googleId or not body.email or not body.gender:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="필수 정보를 모두 입력해야 합니다.",
        )

    # 신규 유저 생성
    user = create_user(db, body.googleId, body.email, body.gender)

    # 토큰 발급
    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    return SignupResponse(
        userId=user.id,
        accessToken=access_token,
        refreshToken=refresh_token,
    )


@router.post("/nickname", response_model=NicknameResponse)
def set_nickname(
    body: NicknameRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """닉네임 설정"""
    user = update_nickname(db, current_user, body.nickname)
    return NicknameResponse(
        message="닉네임이 설정되었습니다.",
        nickname=user.nickname,
    )


@router.post("/refresh", response_model=RefreshResponse)
def refresh_token(
    body: RefreshRequest,
    db: Session = Depends(get_db),
):
    """Refresh Token으로 새 Access Token 발급"""
    try:
        payload = jwt.decode(
            body.refreshToken, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM]
        )
        user_id: str = payload.get("sub")
        if user_id is None or payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired refresh token",
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )

    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )

    access_token = create_access_token(user.id)
    return RefreshResponse(accessToken=access_token)
