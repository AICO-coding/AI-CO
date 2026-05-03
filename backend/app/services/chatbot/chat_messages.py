from datetime import datetime, timezone, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from app.models.chatModels import ChatMessage

KST = timezone(timedelta(hours=9))

# KST 오늘 00:00 ~ 23:59:59 를 UTC로 반환
def _today_kst_range_utc() -> tuple[datetime, datetime]:
    now_kst = datetime.now(KST)
    start = now_kst.replace(hour=0, minute=0, second=0, microsecond=0)
    end = now_kst.replace(hour=23, minute=59, second=59, microsecond=0)
    return start.astimezone(timezone.utc), end.astimezone(timezone.utc)


# KST 오늘 23:59:59 를 UTC로 반환
def _get_expires_at() -> datetime:
    now_kst = datetime.now(KST)
    end_kst = now_kst.replace(hour=23, minute=59, second=59, microsecond=0)
    return end_kst.astimezone(timezone.utc)


# 사용자 메시지 + 어시스턴트 답변을 함께 저장하고 assistant 메시지를 반환
def save_chat_messages(
    db: Session,
    user_id: int,
    track: str,
    chapter: str,
    user_message: str,
    assistant_reply: str,
) -> ChatMessage:
    expires_at = _get_expires_at()
    now = datetime.now(timezone.utc)

    user_msg = ChatMessage(
        user_id=user_id,
        track=track,
        chapter=chapter,
        role="user",
        content=user_message,
        created_at=now,
        expires_at=expires_at,
    )
    assistant_msg = ChatMessage(
        user_id=user_id,
        track=track,
        chapter=chapter,
        role="assistant",
        content=assistant_reply,
        created_at=now,
        expires_at=expires_at,
    )

    db.add(user_msg)
    db.add(assistant_msg)
    db.commit()
    db.refresh(assistant_msg)

    return assistant_msg


# 오늘 KST 기준 대화 기록 조회. 없으면 None 반환
def fetch_today_history(db: Session, user_id: int) -> Optional[dict]:
    start_utc, end_utc = _today_kst_range_utc()

    messages = (
        db.query(ChatMessage)
        .filter(
            ChatMessage.user_id == user_id,
            ChatMessage.created_at >= start_utc,
            ChatMessage.created_at <= end_utc,
        )
        .order_by(ChatMessage.created_at.asc())
        .all()
    )

    if not messages:
        return None

    expires_at = _get_expires_at()

    return {
        "date": datetime.now(KST).strftime("%Y-%m-%d"),
        "messages": [
            {
                "role": msg.role,
                "content": msg.content,
                "createdAt": msg.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
            }
            for msg in messages
        ],
        "expiresAt": expires_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }