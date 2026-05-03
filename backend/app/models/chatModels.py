# app/models/chatModels.py
from datetime import datetime, timezone
from sqlalchemy import Column, BigInteger, String, Text, DateTime, ForeignKey
from app.core.database import Base


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(
        BigInteger,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    track = Column(String(100), nullable=False)
    chapter = Column(String(100), nullable=False)

    role = Column(String(20), nullable=False)  # "user" 또는 "assistant"
    content = Column(Text, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    expires_at = Column(DateTime(timezone=True), nullable=False)