from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field


class WrongAnswerCreateRequest(BaseModel):
    problemId: int = Field(..., description="오답으로 등록할 문제 ID", example=1)
    sourceType: str = Field(..., description="오답 발생 위치: learning 또는 daily", example="learning")
    userAnswer: Any = Field(..., description="사용자가 입력한 답", example={"answer": 2})


class WrongAnswerListItem(BaseModel):
    id: int = Field(..., description="오답 기록 ID")
    problemId: int = Field(..., description="문제 ID")
    track: str = Field(..., description="트랙명", example="ML")
    chapter: str = Field(..., description="챕터명", example="선형 회귀")
    problemType: str = Field(..., description="문제 유형", example="multiple_choice")
    sourceType: str = Field(..., description="오답 발생 위치", example="learning")
    isResolved: bool = Field(..., description="복습 후 해결 여부", example=False)
    reviewCount: int = Field(..., description="복습 횟수", example=0)
    date: str = Field(..., description="오답 등록 날짜", example="2026-05-01")


class WrongAnswerListResponse(BaseModel):
    wrongAnswers: list[WrongAnswerListItem]


class ProblemDetailResponse(BaseModel):
    sourceType: str = Field(..., description="문제 출처: learning 또는 daily")
    trackProblemId: int | None = Field(default=None, description="학습 트랙 문제 ID")
    dailyProblemId: int | None = Field(default=None, description="데일리 문제 ID")
    track: str | None = Field(default=None, description="트랙명")
    chapter: str | None = Field(default=None, description="챕터명")
    problemType: str | None = Field(default=None, description="문제 유형")
    content: Any = Field(..., description="문제 내용")
    answer: Any = Field(..., description="정답")
    explanation: str | None = Field(default=None, description="해설")
    hints: Any = Field(default=None, description="힌트")


class WrongAnswerDetailResponse(BaseModel):
    id: int = Field(..., description="오답 기록 ID")
    problemId: int = Field(..., description="문제 ID")
    sourceType: str = Field(..., description="오답 발생 위치")
    userAnswer: Any = Field(..., description="사용자가 입력한 오답")
    correctAnswer: Any = Field(..., description="정답")
    isResolved: bool = Field(..., description="복습 후 해결 여부")
    reviewCount: int = Field(..., description="복습 횟수")
    date: str = Field(..., description="오답 등록 날짜")
    lastReviewedAt: datetime | None = Field(default=None, description="마지막 복습 시간")
    problem: ProblemDetailResponse = Field(..., description="문제 상세 정보")


class ReviewProblemItem(BaseModel):
    wrongAnswerId: int = Field(..., description="복습 제출 시 사용할 오답 기록 ID")
    problemId: int = Field(..., description="문제 ID")
    sourceType: str = Field(..., description="오답 발생 위치")
    userAnswer: Any = Field(..., description="처음 틀렸을 때 입력한 답")
    problem: ProblemDetailResponse = Field(..., description="복습할 문제 정보")


class ReviewProblemResponse(BaseModel):
    wrongAnswers: list[ReviewProblemItem]


class ReviewSubmitItem(BaseModel):
    wrongAnswerId: int = Field(..., description="채점할 오답 기록 ID", example=1)
    answer: Any = Field(..., description="복습에서 다시 제출한 답", example={"answer": 1})


class ReviewSubmitRequest(BaseModel):
    answers: list[ReviewSubmitItem]


class ReviewResultItem(BaseModel):
    wrongAnswerId: int = Field(..., description="오답 기록 ID")
    problemId: int = Field(..., description="문제 ID")
    isCorrect: bool = Field(..., description="정답 여부")


class ReviewSubmitResponse(BaseModel):
    results: list[ReviewResultItem]
    correctCount: int = Field(..., description="맞힌 문제 수")
    totalCount: int = Field(..., description="제출한 전체 문제 수")


class DeleteWrongAnswerResponse(BaseModel):
    message: str = Field(..., example="Wrong answer deleted successfully")