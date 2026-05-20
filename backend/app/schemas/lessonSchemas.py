from pydantic import BaseModel
from typing import Any


class LessonResponse(BaseModel):
    lessonId: int
    lessonType: str
    title: str
    orderIndex: int
    isCompleted: bool
    part: str | None = None
    markdownUrl: str | None = None   # concept_image/concept_code/parameter
    imageUrl: str | None = None      # concept_image
    problemId: int | None = None     # code_fill/multiple_choice
    content: dict[str, Any] | None = None

    class Config:
        from_attributes = True


class ChapterLessonsResponse(BaseModel):
    track: str
    chapter: str
    completionRate: int
    lastLessonId: int | None
    lessons: list[LessonResponse]
