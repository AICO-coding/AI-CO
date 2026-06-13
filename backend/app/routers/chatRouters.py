from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import anthropic
from app.core.security import get_current_user
from app.core.config import ANTHROPIC_API_KEY
from app.models.userModels import User
from app.core.database import get_db
from app.schemas.chatSchemas import ChatRequest, ChatResponse, ChatHistoryResponse
from app.services.chatbot.chat_messages import save_chat_messages, fetch_today_history
from app.services.chatbot import retriever

router = APIRouter(prefix="/chat", tags=["Chat"])

_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


def _generate_reply(track: str, chapter: str, message: str) -> str:
    try:
        chunks = retriever.search(query=message, track=track, chapter=chapter)
        context = "\n\n---\n\n".join(chunks) if chunks else "관련 학습 내용을 찾지 못했어요."

        response = _client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=(
                f"너는 AI 학습 플랫폼의 친절한 AI 튜터 '코냥이'야.\n"
                f"학생이 '{track}' 트랙의 '{chapter}' 챕터를 공부하고 있어.\n"
                f"아래 학습 내용을 참고해서 학생의 질문에 친절하고 명확하게 답변해줘.\n"
                f"학습 내용에 없는 건 모른다고 솔직하게 말해도 돼.\n\n"
                f"[학습 내용]\n{context}"
            ),
            messages=[{"role": "user", "content": message}],
        )
        return response.content[0].text
    except Exception as e:
        print(f"[ChatBot Error] {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="AI 응답 생성 중 오류가 발생했습니다.",
        )

# POST /chat
@router.post(
    "",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
    summary="코냥이에게 질문",
)
def chat(
    body: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if not body.track or not body.chapter or not body.message.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="track, chapter, message는 필수값입니다.",
        )

    reply = _generate_reply(
        track=body.track,
        chapter=body.chapter,
        message=body.message,
    )

    saved = save_chat_messages(
        db=db,
        user_id=current_user.id,
        track=body.track,
        chapter=body.chapter,
        user_message=body.message,
        assistant_reply=reply,
    )

    return ChatResponse(
        reply=reply,
        savedAt=saved.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
        expiresAt=saved.expires_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
    )

# GET /chat/history
@router.get(
    "/history",
    response_model=ChatHistoryResponse,
    status_code=status.HTTP_200_OK,
    summary="오늘의 대화 기록 조회",
)
def get_chat_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    history = fetch_today_history(db, user_id=current_user.id)

    if not history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="오늘의 대화 기록이 없습니다.",
        )

    return history