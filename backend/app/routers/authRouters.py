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


@router.post(
    "/google/login",
    response_model=GoogleLoginResponse,
    summary="Google ID Token 검증 후 로그인",
)
def google_login(
    body: GoogleLoginRequest,
    db: Session = Depends(get_db),
):
    """
    Google ID Token으로 로그인

    - 기존 회원: accessToken, refreshToken 반환
    - 신규 회원: 자동 회원가입 후 accessToken, refreshToken 반환
    """

    try:
        print("Google login request received")
        print("idToken exists:", bool(body.idToken))
        print("idToken startswith:", body.idToken[:30] if body.idToken else None)

        idinfo = verify_google_token(body.idToken)

    except ValueError as e:
        print("google_login error:", repr(e))

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"유효하지 않은 Google ID 토큰입니다. 원인: {str(e)}",
        )

    google_id: str | None = idinfo.get("sub")
    email: str | None = idinfo.get("email")

    if not google_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Google 계정 ID 정보를 가져올 수 없습니다.",
        )

    if not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Google 계정 이메일 정보를 가져올 수 없습니다.",
        )

    # 기존 유저 조회
    user = get_user_by_google_id(db, google_id)

    # 신규 회원이면 자동 회원가입
    if user is None:
        user = create_user(
            db=db,
            google_id=google_id,
            email=email,
            gender="UNKNOWN",
        )

    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    return GoogleLoginResponse(
        userId=user.id,
        nickname=user.nickname,
        accessToken=access_token,
        refreshToken=refresh_token,
    )


@router.post(
    "/google/signup",
    response_model=SignupResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Google 회원가입",
)
def google_signup(
    body: SignupRequest,
    db: Session = Depends(get_db),
):

    if not body.googleId or not body.email or not body.gender:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="필수 정보를 모두 입력해야 합니다.",
        )

    # 이미 가입된 유저인지 확인
    existing_user = get_user_by_google_id(db, body.googleId)

    if existing_user is not None:
        access_token = create_access_token(existing_user.id)
        refresh_token = create_refresh_token(existing_user.id)

        return SignupResponse(
            userId=existing_user.id,
            accessToken=access_token,
            refreshToken=refresh_token,
        )

    # 신규 유저 생성
    user = create_user(
        db=db,
        google_id=body.googleId,
        email=body.email,
        gender=body.gender,
    )

    # 토큰 발급
    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    return SignupResponse(
        userId=user.id,
        accessToken=access_token,
        refreshToken=refresh_token,
    )


@router.post(
    "/nickname",
    response_model=NicknameResponse,
    summary="닉네임 설정",
)
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


@router.post(
    "/refresh",
    response_model=RefreshResponse,
    summary="Refresh Token으로 Access Token 재발급",
)
def refresh_token(
    body: RefreshRequest,
    db: Session = Depends(get_db),
):
    """Refresh Token으로 새 Access Token 발급"""

    try:
        payload = jwt.decode(
            body.refreshToken,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM],
        )

        user_id: str | None = payload.get("sub")
        token_type: str | None = payload.get("type")

        if user_id is None or token_type != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="유효하지 않거나 만료된 Refresh Token입니다.",
            )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유효하지 않거나 만료된 Refresh Token입니다.",
        )

    user = db.query(User).filter(User.id == int(user_id)).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유효하지 않거나 만료된 Refresh Token입니다.",
        )

    access_token = create_access_token(user.id)

    return RefreshResponse(accessToken=access_token)