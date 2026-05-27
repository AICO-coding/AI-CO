from pydantic import BaseModel


class TrackSummary(BaseModel):
    track: str
    completionRate: int
    totalXp: int
    hintUsed: int


class AllTracksResponse(BaseModel):
    tracks: list[TrackSummary]


class ChapterProgress(BaseModel):
    chapter: str
    title: str
    part: str | None = None
    isCompleted: bool
    xpEarned: int
    hintUsed: int
    isLocked: bool


class TrackChaptersResponse(BaseModel):
    track: str
    chapters: list[ChapterProgress]
