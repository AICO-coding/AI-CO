from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field


class DailyProblemItem(BaseModel):
    dailyProblemId: int
    problemType: str
    content: Any  # { question, choices } - 정답/힌트 미포함


class DailyResponse(BaseModel):
    date: str
    dailyProblems: list[DailyProblemItem]
    isCompleted: bool = Field(..., description="오늘 제출 완료 여부. true이면 GET /daily/result로 결과 조회")
    expiresAt: str = Field(..., description="KST 기준 당일 23:59:59")


class DailySubmitAnswerItem(BaseModel):
    dailyProblemId: int
    answer: Any  # multiple_choice: { answer: int }


class DailySubmitRequest(BaseModel):
    answers: list[DailySubmitAnswerItem] = Field(..., description="5개 문제 전체 제출 필수")


class DailySubmitResultItem(BaseModel):
    dailyProblemId: int
    problemType: str
    content: Any
    userAnswer: Any
    correctAnswer: Any
    isCorrect: bool
    explanation: str | None = None
    wrongAnswerId: int | None = Field(default=None, description="틀린 문제는 오답노트에 자동 저장. 맞힌 문제는 null")


class DailySubmitResponse(BaseModel):
    date: str
    score: int = Field(..., description="맞힌 문제 수")
    totalProblems: int
    xpEarned: int = Field(..., description="맞힌 문제 1개당 20 XP")
    isPerfect: bool = Field(..., description="5문제 전부 정답 여부")
    results: list[DailySubmitResultItem]


class DailyResultResponse(BaseModel):
    date: str
    score: int
    totalProblems: int
    xpEarned: int
    isPerfect: bool
    results: Any  # DailySubmitResultItem 목록 (JSONB)
    completedAt: datetime
