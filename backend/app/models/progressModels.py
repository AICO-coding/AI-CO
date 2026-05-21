from sqlalchemy import BigInteger, Boolean, Column, DateTime, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from app.core.database import Base


class Progress(Base):
    __tablename__ = "progress"
    __table_args__ = (
        UniqueConstraint("user_id", "track", "chapter", name="uq_user_track_chapter"),
    )

    id              = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id         = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    track           = Column(String(50), nullable=False)
    chapter         = Column(String(100), nullable=False)
    is_completed    = Column(Boolean, default=False, nullable=False)
    completion_rate = Column(Integer, default=0, nullable=False)
    xp_earned       = Column(Integer, default=0, nullable=False)
    hint_used       = Column(Integer, default=0, nullable=False)
    report          = Column(JSONB, nullable=True)
    completed_at    = Column(DateTime(timezone=True), nullable=True)
    last_lesson_id  = Column(BigInteger, ForeignKey("lessons.id", ondelete="SET NULL"), nullable=True)
    part            = Column(String(), nullable=True)
