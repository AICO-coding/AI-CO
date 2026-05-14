from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field


class DailyProblemItem(BaseModel):
    dailyProblemId: int = Field(..., description="데일리 문제 ID")
    track: str = Field(..., description="트랙명", example="ML")
    chapter: str = Field(..., description="챕터명", example="ch1")
    problemType: str = Field(..., description="문제 유형", example="multiple_choice")
    content: Any = Field(..., description="문제 내용")


class DailyResponse(BaseModel):
    date: str = Field(..., description="데일리 날짜")
    dailyProblems: list[DailyProblemItem]
    isCompleted: bool = Field(..., description="오늘 데일리 제출 여부")
    expiresAt: str = Field(..., description="오늘 데일리 만료 시간")


class DailySubmitAnswerItem(BaseModel):
    dailyProblemId: int = Field(..., description="daily_problems.id", example=1)
    answer: Any = Field(..., description="사용자가 제출한 답", example={"answer": 1})


class DailySubmitRequest(BaseModel):
    answers: list[DailySubmitAnswerItem]


class DailySubmitResultItem(BaseModel):
    dailyProblemId: int
    track: str
    chapter: str
    problemType: str
    content: Any
    userAnswer: Any
    correctAnswer: Any
    isCorrect: bool
    explanation: str | None = None
    wrongAnswerId: int | None = None


class DailySubmitResponse(BaseModel):
    date: str
    score: int = Field(..., description="맞힌 문제 수")
    totalProblems: int = Field(..., description="전체 문제 수")
    xpEarned: int = Field(..., description="획득 XP")
    isPerfect: bool = Field(..., description="5문제 모두 정답 여부")
    results: list[DailySubmitResultItem]


class DailyResultResponse(BaseModel):
    date: str
    score: int
    totalProblems: int
    xpEarned: int
    isPerfect: bool
    results: Any
    completedAt: datetime