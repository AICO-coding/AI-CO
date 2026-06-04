import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL

# .env 파일 경로를 명시적으로 지정
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path, encoding='utf-8')

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL 환경변수가 설정되지 않았습니다.")

# SQLAlchemy URL 객체 사용 (자동으로 인코딩 처리)
try:
    db_url = URL.create(
        drivername="postgresql+psycopg2",
        username="postgres",
        password="0715",
        host="localhost",
        port=5432,
        database="aico"
    )
    engine = create_engine(db_url, pool_pre_ping=True)
except Exception as e:
    print(f"🔴 엔진 생성 실패: {e}")
    print(f"📝 DB_URL: {db_url if 'db_url' in locals() else 'URL 생성 실패'}")
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