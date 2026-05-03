from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
#from app.core.security import get_current_user
from app.models.userModels import User
from app.core.database import get_db
from app.schemas.chatSchemas import ChatRequest, ChatResponse, ChatHistoryResponse
from app.services.chatbot.chat_messages import save_chat_messages, fetch_today_history

router = APIRouter(prefix="/chat", tags=["Chat"])

# AI 연동 전 임시 더미 응답 (나중에 이 함수를 konaing_service.ask_konaing() 으로 교체하면 됨)
def _generate_reply(track: str, chapter: str, message: str) -> str:
    return f"[{track} / {chapter}] 에 대한 코냥이의 답변이 여기에 들어올 예정이에요"

###### 테스트 후 주석 제거
# # POST /chat 
# @router.post(
#     "",
#     response_model=ChatResponse,
#     status_code=status.HTTP_200_OK,
#     summary="코냥이에게 질문",
# )
# def chat(
#     body: ChatRequest,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user),
# ):
#     """
#     개념 공부 화면에서만 질문 가능.
#     - 400: track 또는 chapter 누락
#     - 403: 문제풀이 화면에서 호출 시 (프론트에서 제어)
#     """
#     # track / chapter 유효성 검사 
#     if not body.track or not body.chapter:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="track과 chapter는 필수값입니다.",
#         )

#     reply = _generate_reply(body.track, body.chapter, body.message)

#     saved = save_chat_messages(
#         db=db,
#         user_id=current_user.id,
#         track=body.track,
#         chapter=body.chapter,
#         user_message=body.message,
#         assistant_reply=reply,
#     )

#     return ChatResponse(
#         reply=reply,
#         savedAt=saved.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
#         expiresAt=saved.expires_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
#     )

# # GET /chat/history
# @router.get(
#     "/history",
#     response_model=ChatHistoryResponse,
#     status_code=status.HTTP_200_OK,
#     summary="오늘의 대화 기록 조회",
# )
# def get_chat_history(
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user),
# ):
#     """
#     오늘 날짜(KST) 기준 대화 기록 반환.
#     - 404: 오늘 대화 기록 없음
#     """
#     history = fetch_today_history(db, user_id=current_user.id)

#     if not history:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="오늘의 대화 기록이 없습니다.",
#         )

#     return history



##### 테스트용
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
):
    # 로그인/JWT 연동 전 테스트용
    current_user_id = 1

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
        user_id=current_user_id,
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
):
    # 로그인/JWT 연동 전 테스트용
    current_user_id = 1

    history = fetch_today_history(db, user_id=current_user_id)

    if not history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="오늘의 대화 기록이 없습니다.",
        )

    return history