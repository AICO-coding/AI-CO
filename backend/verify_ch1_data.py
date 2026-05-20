"""
Ch1 데이터 삽입 확인 스크립트
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.lessonModels import Lesson
from app.models.problemModels import Problem
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

def verify():
    """데이터 확인"""
    try:
        lessons = db.query(Lesson).filter(Lesson.chapter == "ch1").all()
        problems = db.query(Problem).filter(Problem.chapter == "ch1").all()

        print("\n" + "="*60)
        print("📊 Ch1 데이터 확인")
        print("="*60)

        print(f"\n✅ Lessons ({len(lessons)}개):")
        for lesson in lessons:
            print(f"  - ID {lesson.id}: {lesson.title} ({lesson.lesson_type}) - part: {lesson.part}")

        print(f"\n✅ Problems ({len(problems)}개):")
        for problem in problems:
            print(f"  - ID {problem.id}: {problem.problem_type} - answer: {problem.answer}")

        if len(lessons) > 0 and len(problems) > 0:
            print("\n✨ 데이터가 정상 삽입되었습니다!")
        else:
            print("\n❌ 데이터가 없습니다!")

    except Exception as e:
        print(f"❌ 오류: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    verify()
