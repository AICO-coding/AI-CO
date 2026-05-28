from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.progressModels import Progress
from app.models.lessonModels import Lesson

VALID_TRACKS = {"ML-분류", "ML-회기", "CV", "NLP"}


def get_all_progress_service(db: Session, user_id: int) -> dict:
    """유저의 전체 트랙별 진도 집계 조회"""
    rows = db.query(Progress).filter(Progress.user_id == user_id).all()

    track_map = {}

    for r in rows:
        track = r.track.upper()

        if track not in track_map:
            track_map[track] = {
                "rates": [],
                "xp": 0,
                "hint": 0,
            }

        track_map[track]["rates"].append(r.completion_rate)
        track_map[track]["xp"] += r.xp_earned
        track_map[track]["hint"] += r.hint_used

    tracks = []

    for track, data in track_map.items():
        avg_rate = int(sum(data["rates"]) / len(data["rates"])) if data["rates"] else 0

        tracks.append({
            "track": track,
            "completionRate": avg_rate,
            "totalXp": data["xp"],
            "hintUsed": data["hint"],
        })

    return {"tracks": tracks}


def get_track_chapters_service(db: Session, user_id: int, track: str) -> dict | None:
    """특정 트랙의 챕터별 진도 조회"""
    track = track.upper()

    if track not in VALID_TRACKS:
        return None

    # 1. Lesson 테이블에서 해당 트랙의 lesson 전체 조회
    # order_index 기준으로 정렬해두면 각 chapter의 첫 번째 lesson을 챕터 대표값으로 사용할 수 있음
    lessons = (
        db.query(Lesson)
        .filter(func.upper(Lesson.track) == track)
        .order_by(Lesson.order_index.asc())
        .all()
    )

    # 2. Progress 테이블에서 해당 유저의 진도 조회
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

    # 3. Lesson에 챕터가 있으면 Lesson 기준으로 응답 구성
    if lessons:
        prev_completed = True
        seen_chapters = set()

        for lesson in lessons:
            chapter_name = lesson.chapter

            # 이미 응답에 넣은 챕터면 건너뜀
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

    # 4. Lesson에 데이터가 없으면 Progress 기준으로라도 응답 구성
    else:
        prev_completed = True

        for progress in progress_rows:
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