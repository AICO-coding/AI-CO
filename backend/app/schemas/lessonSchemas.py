from pydantic import BaseModel
from typing import Any, Union


class LessonResponse(BaseModel):
    lessonId: int
    lessonType: str
    orderIndex: int
    isCompleted: bool
    part: str | None = None
    markdownUrl: str | None = None   # concept_image/concept_code/parameter
    imageUrl: str | None = None      # concept_image
    problemId: int | None = None     # code_fill/multiple_choice
    hints: list[Any] | None = None   # code_fill/multiple_choice
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
    answers: dict[str, str]


class MultipleChoiceSubmit(BaseModel):
    lessonId: int
    problemId: int
    answer: int


class SubmitResponse(BaseModel):
    isCorrect: bool
    correctAnswer: Any | None = None


class HintRequest(BaseModel):
    problemId: int
    hintLevel: int


class HintResponse(BaseModel):
    xpDeducted: int
    hintsUsed: int


class RevealRequest(BaseModel):
    problemId: int


class RevealResponse(BaseModel):
    answer: dict[str, Any]
    xpDeducted: int


class ChapterCompleteResponse(BaseModel):
    chapter: str
    isCompleted: bool
    chapterXP: int
    xpDeducted: int
    xpEarned: int
    hintUsed: int
