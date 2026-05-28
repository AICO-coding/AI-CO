from pydantic import BaseModel, Field
from datetime import datetime


# Google 로그인 요청
class GoogleLoginRequest(BaseModel):
    idToken: str = Field(..., description="Google ID Token")


# Google 로그인 응답 - 기존 회원
class GoogleLoginResponse(BaseModel):
    userId: int
    nickname: str | None
    accessToken: str
    refreshToken: str


# Google 로그인 응답 - 신규 회원
class GoogleNewUserResponse(BaseModel):
    googleId: str


# 회원가입 요청
class SignupRequest(BaseModel):
    googleId: str
    email: str
    gender: str


# 회원가입 응답
class SignupResponse(BaseModel):
    userId: int
    accessToken: str
    refreshToken: str


# 닉네임 설정 요청
class NicknameRequest(BaseModel):
    nickname: str


# 닉네임 설정 응답
class NicknameResponse(BaseModel):
    message: str
    nickname: str


# Refresh Token 요청
class RefreshRequest(BaseModel):
    refreshToken: str


# Refresh Token 응답
class RefreshResponse(BaseModel):
    accessToken: str


# 유저 정보 응답
class UserResponse(BaseModel):
    userId: int = Field(..., alias="id")
    nickname: str | None
    xp: int
    createdAt: datetime

    class Config:
        from_attributes = True
        populate_by_name = True


# XP 조회 응답
class XpResponse(BaseModel):
    totalXp: int = Field(..., alias="xp")
    tracks: dict = Field(default_factory=lambda: {"ML-분류": 0, "ML-회귀": 0, "CV": 0, "NLP": 0})

    class Config:
        populate_by_name = True
