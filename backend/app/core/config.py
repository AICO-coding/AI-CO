import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / ".env"

# backend/.env를 명시적으로 로드
load_dotenv(dotenv_path=ENV_PATH, encoding="utf-8")


# Google OAuth
GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID", "")

# JWT 설정
JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "")
JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))


# 환경변수 검증
if not GOOGLE_CLIENT_ID:
    raise ValueError(
        f"GOOGLE_CLIENT_ID 환경변수가 설정되지 않았습니다. 확인한 .env 경로: {ENV_PATH}"
    )
if not JWT_SECRET_KEY:
    raise ValueError(
        f"JWT_SECRET_KEY 환경변수가 설정되지 않았습니다. 확인한 .env 경로: {ENV_PATH}"
    )