from pydantic import BaseModel
from typing import Any, Optional


class OpensourceResource(BaseModel):
    name: str
    desc: str
    url: str


class AIReportContent(BaseModel):
    weakConcepts: list[str] = []
    cobotComment: str
    summary: str
    keyPoint: str
    nextChapter: str
    opensource: list[OpensourceResource]


class ReportResponse(BaseModel):
    track: str
    chapter: str
    chapterTitle: str
    completedAt: str
    totalProblems: int
    grade: str

    xpEarned: int
    wrongCount: int
    hintCount: int

    weakConcepts: list[str]
    cobotComment: str
    summary: str
    keyPoint: str
    nextChapter: str
    opensource: list[OpensourceResource]

    class Config:
        from_attributes = True


class ReportPendingResponse(BaseModel):
    status: str = "pending"
    message: str = "리포트를 생성 중입니다. 잠시 후 다시 확인해주세요."
