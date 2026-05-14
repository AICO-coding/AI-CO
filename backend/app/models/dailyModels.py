from sqlalchemy import (
    Column,
    BigInteger,
    Integer,
    String,
    Date,
    DateTime,
    Boolean,
    ForeignKey,
    UniqueConstraint,
    Index,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base


class DailyProblem(Base):
    __tablename__ = "daily_problems"

    id = Column(BigInteger, primary_key=True, index=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)

    problem_order = Column(Integer, nullable=False)

    track = Column(String(50), nullable=False)
    chapter = Column(String(100), nullable=False)
    problem_type = Column(String(50), nullable=False)

    content = Column(JSONB, nullable=False)
    answer = Column(JSONB, nullable=False)
    explanation = Column(String, nullable=True)
    hints = Column(JSONB, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    wrong_answers = relationship("WrongAnswer", back_populates="daily_problem")

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "date",
            "problem_order",
            name="uq_daily_problem_user_date_order",
        ),
        Index("ix_daily_problems_user_date", "user_id", "date"),
    )


class DailyResult(Base):
    __tablename__ = "daily_results"

    id = Column(BigInteger, primary_key=True, index=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)

    score = Column(Integer, nullable=False)
    total_problems = Column(Integer, nullable=False)
    xp_earned = Column(Integer, nullable=False)
    is_perfect = Column(Boolean, nullable=False)

    results = Column(JSONB, nullable=False)

    completed_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "date",
            name="uq_daily_result_user_date",
        ),
        Index("ix_daily_results_user_date", "user_id", "date"),
    )