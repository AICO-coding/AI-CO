import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# .env 파일 경로를 명시적으로 지정
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path, encoding='utf-8')

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL 환경변수가 설정되지 않았습니다.")

try:
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
except Exception as e:
    print(f"엔진 생성 실패: {e}")
    raise

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()