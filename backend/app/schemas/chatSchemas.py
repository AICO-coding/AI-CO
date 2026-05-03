from pydantic import BaseModel, Field
from typing import List


# Request
class ChatRequest(BaseModel):
    track: str = Field(..., description="학습 트랙")
    chapter: str = Field(..., description="현재 챕터")
    message: str = Field(..., description="사용자 질문")


# Response 
class ChatResponse(BaseModel):
    reply: str
    savedAt: str
    expiresAt: str

class ChatMessageItem(BaseModel):
    role: str
    content: str
    createdAt: str

class ChatHistoryResponse(BaseModel):
    date: str
    messages: List[ChatMessageItem]
    expiresAt: str