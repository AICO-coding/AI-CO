import re
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.progressModels import Progress
from app.models.lessonModels import Lesson

VALID_TRACKS = {"ML-분류", "ML-회귀", "CV", "NLP"}


def _chapter_sort_key(chapter: str | None):
    if not chapter:
        return ("", 0, "")

    match = re.search(r"\d+", chapter)
    chapter_number = int(match.group()) if match else 0
    chapter_prefix = re.sub(r"\d+", "", chapter)

    return (chapter_prefix, chapter_number, chapter)


def get_all_progress_service(db: Session, user_id: int) -> dict:
    rows = db.query(Progress).filter(Progress.user_id == user_id).all()

    track_map = {}

    for r in rows:
        track = r.track.upper()

        if track not in track_map:
            track_map[track] = {
                "rates": {},
                "xp": 0,
                "hint": 0,
            }

        track_map[track]["rates"][r.chapter] = r.completion_rate
        track_map[track]["xp"] += r.xp_earned
        track_map[track]["hint"] += r.hint_used

    track_chapter_counts = {}
    for track in track_map:
        total = (
            db.query(Lesson.chapter)
            .filter(func.upper(Lesson.track) == track)
            .distinct()
            .count()
        )
        track_chapter_counts[track] = total

    tracks = []

    for track, data in track_map.items():
        total_chapters = track_chapter_counts.get(track, 0)
        if total_chapters > 0:
            avg_rate = int(sum(data["rates"].values()) / total_chapters)
        else:
            avg_rate = int(sum(data["rates"].values()) / len(data["rates"])) if data["rates"] else 0

        tracks.append({
            "track": track,
            "completionRate": avg_rate,
            "totalXp": data["xp"],
            "hintUsed": data["hint"],
        })

    return {"tracks": tracks}


def get_track_chapters_service(db: Session, user_id: int, track: str) -> dict | None:
    track = track.upper()

    if track not in VALID_TRACKS:
        return None

    lessons = (
        db.query(Lesson)
        .filter(func.upper(Lesson.track) == track)
        .all()
    )
    lessons.sort(key=lambda lesson: (
        _chapter_sort_key(lesson.chapter),
        lesson.order_index,
        lesson.id,
    ))

    progress_rows = (
        db.query(Progress)
        .filter(
            Progress.user_id == user_id,
            func.upper(Progress.track) == track
        )
        .all()
    )

    progress_map = {
        progress.chapter: progress
        for progress in progress_rows
    }

    chapters = []

    if lessons:
        prev_completed = True
        seen_chapters = set()

        for lesson in lessons:
            chapter_name = lesson.chapter

            if chapter_name in seen_chapters:
                continue

            seen_chapters.add(chapter_name)

            progress = progress_map.get(chapter_name)

            if progress:
                is_completed = progress.is_completed
                xp_earned = progress.xp_earned
                hint_used = progress.hint_used
                part = progress.part or lesson.part
            else:
                is_completed = False
                xp_earned = 0
                hint_used = 0
                part = lesson.part

            is_locked = not prev_completed

            chapters.append({
                "chapter": chapter_name,
                "title": lesson.title,
                "part": part,
                "isCompleted": is_completed,
                "xpEarned": xp_earned,
                "hintUsed": hint_used,
                "isLocked": is_locked,
            })

            prev_completed = is_completed

    else:
        prev_completed = True

        for progress in sorted(progress_rows, key=lambda row: _chapter_sort_key(row.chapter)):
            is_locked = not prev_completed

            chapters.append({
                "chapter": progress.chapter,
                "title": None,
                "part": progress.part,
                "isCompleted": progress.is_completed,
                "xpEarned": progress.xp_earned,
                "hintUsed": progress.hint_used,
                "isLocked": is_locked,
            })

            prev_completed = progress.is_completed

    return {
        "track": track,
        "chapters": chapters,
    }