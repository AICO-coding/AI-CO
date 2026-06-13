from pydantic import BaseModel, Field
from typing import Any, Union


class LessonResponse(BaseModel):
    lessonId: int
    lessonType: str
    orderIndex: int
    isCompleted: bool
    part: str | None = None
    markdownUrl: str | None = None   
    imageUrl: str | None = None     
    problemId: int | None = None    
    hints: list[Any] | None = None  
    usedHintLevels: list[int] | None = None  
    content: dict[str, Any] | None = None

    class Config:
        from_attributes = True


class ChapterLessonsResponse(BaseModel):
    track: str
    chapter: str
    completionRate: int
    lastLessonId: int | None
    lessons: list[LessonResponse]


class LessonCompleteResponse(BaseModel):
    lessonId: int
    isCompleted: bool
    chapterCompletionRate: int


class CodeFillSubmit(BaseModel):
    lessonId: int
    problemId: int
    answer: dict[str, str]


class MultipleChoiceSubmit(BaseModel):
    lessonId: int
    problemId: int
    answer: int


class SubmitResponse(BaseModel):
    isCorrect: bool
    correctAnswer: Any | None = None
    explanation: str | None = Field(default=None, description="정답일 경우에만 반환")


class HintRequest(BaseModel):
    problemId: int
    hintLevel: int


class HintResponse(BaseModel):
    xpDeducted: int
    totalXP: int
    hintsUsed: int


class RevealRequest(BaseModel):
    problemId: int


class RevealResponse(BaseModel):
    answer: dict[str, Any]
    xpDeducted: int
    totalXP: int
    explanation: str | None = Field(default=None, description="문제에 설명이 있을 경우에만 반환")


class ChapterCompleteResponse(BaseModel):
    chapter: str
    isCompleted: bool
    isFirstCompletion: bool
    xpDeducted: int | None = None
    hintUsed: int | None = None
    revealUsed: int | None = None
    baseXP: int | None = None
    xpEarned: int | None = None