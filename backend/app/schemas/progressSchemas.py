from pydantic import BaseModel


class TrackSummary(BaseModel):
    track: str
    completionRate: int
    xpEarned: int
    hintUsed: int


class AllProgressResponse(BaseModel):
    tracks: list[TrackSummary]


class ChapterProgress(BaseModel):
    chapter: str
    isCompleted: bool
    completionRate: int
    xpEarned: int
    hintUsed: int


class TrackProgressResponse(BaseModel):
    track: str
    chapters: list[ChapterProgress]
