from sqlalchemy import BigInteger, Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from app.core.database import Base


class Lesson(Base):
    __tablename__ = "lessons"

    id          = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    track       = Column(String(50), nullable=False)
    chapter_id  = Column(String(100), nullable=False)
    title       = Column(String(255), nullable=False)
    content_type = Column(String(50), nullable=False)   # text | image | code | markdown | problem
    content     = Column(JSONB, nullable=False)
    problem_id  = Column(BigInteger, ForeignKey("problems.id", ondelete="SET NULL"), nullable=True)
    order_index = Column(Integer, nullable=False)
