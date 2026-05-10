from app.core.database import SessionLocal
from app.models.userModels import User
from app.models.progressModels import Progress
from app.models.lessonModels import Lesson
from datetime import datetime, timezone

db = SessionLocal()

# 테스트 유저 조회 또는 생성
test_user = db.query(User).filter(User.google_id == "test_user_001").first()
if not test_user:
    test_user = User(
        google_id="test_user_001",
        email="test@example.com",
        nickname="테스트유저",
        xp=500
    )
    db.add(test_user)
    db.commit()
    db.refresh(test_user)

print(f"[OK] 테스트 유저 생성: ID={test_user.id}, Email={test_user.email}")

# 진도 데이터 생성
progress_data = [
    {"track": "ML", "chapter": "ch1", "is_completed": True, "completion_rate": 100, "xp_earned": 50, "hint_used": 0},
    {"track": "ML", "chapter": "ch2", "is_completed": True, "completion_rate": 80, "xp_earned": 40, "hint_used": 2},
    {"track": "ML", "chapter": "ch3", "is_completed": False, "completion_rate": 50, "xp_earned": 25, "hint_used": 1},
    {"track": "CV", "chapter": "ch1", "is_completed": True, "completion_rate": 100, "xp_earned": 50, "hint_used": 0},
    {"track": "NLP", "chapter": "ch1", "is_completed": False, "completion_rate": 30, "xp_earned": 15, "hint_used": 3},
]

for data in progress_data:
    progress = Progress(
        user_id=test_user.id,
        track=data["track"],
        chapter=data["chapter"],
        is_completed=data["is_completed"],
        completion_rate=data["completion_rate"],
        xp_earned=data["xp_earned"],
        hint_used=data["hint_used"],
        completed_at=datetime.now(timezone.utc) if data["is_completed"] else None
    )
    db.add(progress)

db.commit()
print(f"[OK] 진도 데이터 생성 완료 ({len(progress_data)}개)")

# 테스트 유저 정보 출력
print(f"\n테스트 유저 정보:")
print(f"  User ID: {test_user.id}")
print(f"  Email: {test_user.email}")
print(f"  Nickname: {test_user.nickname}")

db.close()
