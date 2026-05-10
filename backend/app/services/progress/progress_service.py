from sqlalchemy.orm import Session
from app.models.progressModels import Progress

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
            "xpEarned": data["xp"],
            "hintUsed": data["hint"],
        })

    return {"tracks": tracks}


def get_track_progress_service(db: Session, user_id: int, track: str) -> dict | None:
    """특정 트랙의 챕터별 진도 조회"""
    if track not in VALID_TRACKS:
        return None

    rows = db.query(Progress).filter(
        Progress.user_id == user_id,
        Progress.track == track
    ).all()

    chapters = [
        {
            "chapter": r.chapter,
            "isCompleted": r.is_completed,
            "completionRate": r.completion_rate,
            "xpEarned": r.xp_earned,
            "hintUsed": r.hint_used,
        }
        for r in rows
    ]

    return {"track": track, "chapters": chapters}
