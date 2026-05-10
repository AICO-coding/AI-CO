from sqlalchemy import Column, BigInteger, String, DateTime, Boolean, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class WrongAnswer(Base):
    __tablename__ = "wrong_answers"

    id = Column(BigInteger, primary_key=True, index=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    problem_id = Column(BigInteger, ForeignKey("problems.id"), nullable=False)

    source_type = Column(String(30), nullable=False)
    user_answer = Column(JSONB, nullable=False)

    is_resolved = Column(Boolean, nullable=False, default=False)
    review_count = Column(Integer, nullable=False, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_reviewed_at = Column(DateTime(timezone=True), nullable=True)

    problem = relationship("Problem", back_populates="wrong_answers")