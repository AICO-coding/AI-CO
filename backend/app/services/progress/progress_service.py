from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.progressModels import Progress
from app.models.lessonModels import Lesson

VALID_TRACKS = {"ML", "CV", "NLP"}


def get_all_progress_service(db: Session, user_id: int) -> dict:
    """유저의 전체 트랙별 진도 집계 조회"""
    rows = db.query(Progress).filter(Progress.user_id == user_id).all()

    # track별 그룹핑 후 집계
    track_map = {}
    for r in rows:
        if r.track not in track_map:
            track_map[r.track] = {"rates": [], "xp": 0, "hint": 0}
        track_map[r.track]["rates"].append(r.completion_rate)
        track_map[r.track]["xp"] += r.xp_earned
        track_map[r.track]["hint"] += r.hint_used

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
    """특정 트랙의 챕터별 진도 조회 (isLocked 포함)"""
    if track not in VALID_TRACKS:
        return None

    # Lesson 테이블에서 해당 트랙의 챕터 순서 파악
    chapter_order_rows = (
        db.query(Lesson.chapter, func.min(Lesson.order_index).label("min_order"))
        .filter(Lesson.track == track)
        .group_by(Lesson.chapter)
        .order_by(func.min(Lesson.order_index).asc())
        .all()
    )
    ordered_chapters = [row.chapter for row in chapter_order_rows]

    # Progress 테이블에서 해당 유저+트랙의 챕터별 진도 조회
    progress_rows = db.query(Progress).filter(
        Progress.user_id == user_id,
        Progress.track == track
    ).all()

    # chapter → Progress 행 매핑
    progress_map = {r.chapter: r for r in progress_rows}

    # isLocked 계산 및 응답 구성
    chapters = []
    prev_completed = True  # 첫 챕터는 항상 unlock

    for chapter_name in ordered_chapters:
        progress = progress_map.get(chapter_name)

        if progress is None:
            is_completed = False
            xp_earned = 0
            hint_used = 0
            part = None
        else:
            is_completed = progress.is_completed
            xp_earned = progress.xp_earned
            hint_used = progress.hint_used
            part = progress.part

        is_locked = not prev_completed

        chapters.append({
            "chapter": chapter_name,
            "part": part,
            "isCompleted": is_completed,
            "xpEarned": xp_earned,
            "hintUsed": hint_used,
            "isLocked": is_locked,
        })

        prev_completed = is_completed

    return {"track": track, "chapters": chapters}
