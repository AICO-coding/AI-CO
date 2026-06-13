from pydantic import BaseModel, Field
from datetime import datetime


class GoogleLoginRequest(BaseModel):
    idToken: str = Field(..., description="Google ID Token")


class GoogleLoginResponse(BaseModel):
    userId: int
    nickname: str | None
    accessToken: str
    refreshToken: str


class GoogleNewUserResponse(BaseModel):
    googleId: str


class SignupRequest(BaseModel):
    googleId: str
    email: str
    gender: str


class SignupResponse(BaseModel):
    userId: int
    accessToken: str
    refreshToken: str


class NicknameRequest(BaseModel):
    nickname: str


class NicknameResponse(BaseModel):
    message: str
    nickname: str


class RefreshRequest(BaseModel):
    refreshToken: str


class RefreshResponse(BaseModel):
    accessToken: str


class UserResponse(BaseModel):
    userId: int = Field(..., alias="id")
    nickname: str | None
    xp: int
    createdAt: datetime

    class Config:
        from_attributes = True
        populate_by_name = True


class XpResponse(BaseModel):
    totalXp: int = Field(..., alias="xp")
    tracks: dict = Field(default_factory=lambda: {"ML-분류": 0, "ML-회귀": 0, "CV": 0, "NLP": 0})

    class Config:
        populate_by_name = True
