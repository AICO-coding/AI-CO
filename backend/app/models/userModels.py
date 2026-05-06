from sqlalchemy import Column, BigInteger, String, Integer, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    google_id = Column(String(255), unique=True, nullable=False, index=True)
    email = Column(String(255), nullable=True)
    gender = Column(String(10), nullable=True)
    nickname = Column(String(50), nullable=True)
    xp = Column(Integer, nullable=False, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)