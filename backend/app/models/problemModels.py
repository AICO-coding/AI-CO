from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Problem(Base):
    __tablename__ = "problems"

    id = Column(BigInteger, primary_key=True, index=True)

    track = Column(String(50), nullable=False)
    chapter = Column(String(100), nullable=False)
    problem_type = Column(String(50), nullable=False)

    content = Column(JSONB, nullable=False)
    answer = Column(JSONB, nullable=False)
    hints = Column(JSONB, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    wrong_answers = relationship("WrongAnswer", back_populates="problem")