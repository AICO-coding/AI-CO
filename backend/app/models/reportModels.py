from sqlalchemy import Column, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    track = Column(String(50), nullable=False)
    chapter = Column(String(100), nullable=False)
    progress_id = Column(BigInteger, ForeignKey("progress.id", ondelete="CASCADE"), nullable=False, unique=True)

    # Claude API로 생성한 AI 리포트 전체 저장
    ai_report = Column(JSONB, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    progress = relationship("Progress", backref="report_data")
