"""
Ch1 Tensor & NumPy 목업 데이터 삽입 스크립트
lessons 테이블 + problems 테이블
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.models.lessonModels import Lesson
from app.models.problemModels import Problem
from app.models.noteModels import WrongAnswer
from app.models.dailyModels import DailyProblem, DailyResult
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# ─── Problems 데이터 ────────────────────────────────────
problems_data = [
    {
        "id": 101,
        "track": "ML",
        "chapter": "ch1",
        "problem_type": "code_fill",
        "content": {
            "instruction": "torch 기본 함수를 사용하여 Tensor 연산을 완성하세요.",
            "template": "import torch\n\n# ① 1D float Tensor 생성\nx = torch.{{blank1}}([1., 2., 3., 4., 5., 6.])\n\n# ② (6,) → (2, 3) 변환\nmat = x.{{blank2}}\nprint(mat.shape)  # torch.Size([2, 3])\n\n# ③ 평균 계산\nprint(x.{{blank3}}())  # tensor(3.5000)\n\n# ④ dtype 확인\nprint(x.{{blank4}})   # torch.float32",
            "blanks": [
                {"key": "blank1"},
                {"key": "blank2"},
                {"key": "blank3"},
                {"key": "blank4"}
            ],
            "hints": [
                {"level": 1, "text": "① torch.te___r  ② .re___pe(행, 열)  ③ .m___n()  ④ .dt___e"},
                {"level": 2, "text": "① 첫 글자: t  ② 첫 글자: r  ③ 첫 글자: m  ④ 첫 글자: d"}
            ]
        },
        "answer": {
            "blank1": "tensor",
            "blank2": "reshape(2, 3)",
            "blank3": "mean",
            "blank4": "dtype"
        },
        "hints": [
            {"level": 1, "text": "① torch.te___r  ② .re___pe(행, 열)  ③ .m___n()  ④ .dt___e"},
            {"level": 2, "text": "① 첫 글자: t  ② 첫 글자: r  ③ 첫 글자: m  ④ 첫 글자: d"}
        ]
    },
    {
        "id": 102,
        "track": "ML",
        "chapter": "ch1",
        "problem_type": "multiple_choice",
        "content": {
            "question": "PyTorch Tensor에 대한 설명으로 틀린 것은?",
            "choices": [
                "① Tensor는 GPU 연산이 가능하지만 ndarray는 불가능하다",
                "② torch.from_numpy()로 만든 Tensor는 원본과 메모리를 공유한다",
                "③ Tensor의 기본 dtype은 float64이다",
                "④ .to('cuda')로 CPU Tensor를 GPU로 전환할 수 있다"
            ],
            "hints": [
                {"level": 1, "text": "NumPy의 기본 dtype과 PyTorch의 기본 dtype을 비교해봐요."},
                {"level": 2, "text": "첫 글자: f (float로 시작하는 타입이에요)"}
            ]
        },
        "answer": {
            "correct_index": 2
        },
        "hints": [
            {"level": 1, "text": "NumPy의 기본 dtype과 PyTorch의 기본 dtype을 비교해봐요."},
            {"level": 2, "text": "첫 글자: f (float로 시작하는 타입이에요)"}
        ]
    }
]

# ─── Lessons 데이터 ────────────────────────────────────
lessons_data = [
    # L1: concept_image
    {
        "id": 1,
        "track": "ML",
        "chapter": "ch1",
        "part": "regression",
        "title": "Tensor란 무엇인가?",
        "lesson_type": "concept_image",
        "order_index": 1,
        "problem_id": None,
        "content": {
            "markdownUrl": "/static/content/ml/ch1/lesson1.md",
            "imageUrl": "/static/content/ml/ch1/tensor_dims.png"
        }
    },
    # L2: concept_code (학습형)
    {
        "id": 2,
        "track": "ML",
        "chapter": "ch1",
        "part": "regression",
        "title": "shape · dtype · reshape",
        "lesson_type": "concept_code",
        "order_index": 2,
        "problem_id": None,
        "content": {
            "markdownUrl": "/static/content/ml/ch1/lesson2.md",
            "template": "import torch\n\nt = torch.tensor([[1., 2.], [3., 4.]])\n\n# 3대 속성\nprint(t.{{blank1}})   # torch.Size([2, 2])\nprint(t.{{blank2}})   # torch.float32\nprint(t.{{blank3}})   # cpu\n\n# reshape: 원소 수 동일하면 자유롭게\nr = torch.arange(6.).{{blank4}}\nprint(r.shape)   # torch.Size([2, 3])",
            "blanks": [
                {"key": "blank1", "answer": "shape"},
                {"key": "blank2", "answer": "dtype"},
                {"key": "blank3", "answer": "device"},
                {"key": "blank4", "answer": "reshape(2, 3)"}
            ]
        }
    },
    # L3: concept_code (학습형)
    {
        "id": 3,
        "track": "ML",
        "chapter": "ch1",
        "part": "regression",
        "title": "NumPy vs Tensor",
        "lesson_type": "concept_code",
        "order_index": 3,
        "problem_id": None,
        "content": {
            "markdownUrl": "/static/content/ml/ch1/lesson3.md",
            "template": "import torch, numpy as np\n\narr = np.array([1., 2., 3.])\n\n# from_numpy: 메모리 공유!\nt = torch.{{blank1}}(arr)\narr[0] = 999.\nprint(t)   # tensor([999., 2., 3.])\n\n# Tensor → NumPy\nback = t.{{blank2}}()   # CPU만 가능!",
            "blanks": [
                {"key": "blank1", "answer": "from_numpy"},
                {"key": "blank2", "answer": "numpy"}
            ]
        }
    },
    # L4: parameter
    {
        "id": 4,
        "track": "ML",
        "chapter": "ch1",
        "part": "regression",
        "title": "reshape 실험",
        "lesson_type": "parameter",
        "order_index": 4,
        "problem_id": None,
        "content": {
            "markdownUrl": "/static/content/ml/ch1/lesson4.md"
        }
    },
    # L5: code_fill (문제형)
    {
        "id": 5,
        "track": "ML",
        "chapter": "ch1",
        "part": "regression",
        "title": "Tensor 기초 구현",
        "lesson_type": "code_fill",
        "order_index": 5,
        "problem_id": 101,
        "content": {
            "instruction": "torch 기본 함수를 사용하여 Tensor 연산을 완성하세요.",
            "template": "import torch\n\n# ① 1D float Tensor 생성\nx = torch.{{blank1}}([1., 2., 3., 4., 5., 6.])\n\n# ② (6,) → (2, 3) 변환\nmat = x.{{blank2}}\nprint(mat.shape)  # torch.Size([2, 3])\n\n# ③ 평균 계산\nprint(x.{{blank3}}())  # tensor(3.5000)\n\n# ④ dtype 확인\nprint(x.{{blank4}})   # torch.float32",
            "blanks": [
                {"key": "blank1"},
                {"key": "blank2"},
                {"key": "blank3"},
                {"key": "blank4"}
            ],
            "hints": [
                {"level": 1, "text": "① torch.te___r  ② .re___pe(행, 열)  ③ .m___n()  ④ .dt___e"},
                {"level": 2, "text": "① 첫 글자: t  ② 첫 글자: r  ③ 첫 글자: m  ④ 첫 글자: d"}
            ]
        }
    },
    # L6: multiple_choice (문제형)
    {
        "id": 6,
        "track": "ML",
        "chapter": "ch1",
        "part": "regression",
        "title": "Ch1 마무리 퀴즈",
        "lesson_type": "multiple_choice",
        "order_index": 6,
        "problem_id": 102,
        "content": {
            "question": "PyTorch Tensor에 대한 설명으로 틀린 것은?",
            "choices": [
                "① Tensor는 GPU 연산이 가능하지만 ndarray는 불가능하다",
                "② torch.from_numpy()로 만든 Tensor는 원본과 메모리를 공유한다",
                "③ Tensor의 기본 dtype은 float64이다",
                "④ .to('cuda')로 CPU Tensor를 GPU로 전환할 수 있다"
            ],
            "hints": [
                {"level": 1, "text": "NumPy의 기본 dtype과 PyTorch의 기본 dtype을 비교해봐요."},
                {"level": 2, "text": "첫 글자: f (float로 시작하는 타입이에요)"}
            ]
        }
    }
]

def seed_data():
    """데이터 삽입"""
    try:
        # 기존 Ch1 데이터 삭제
        print("🔄 기존 Ch1 데이터 삭제 중...")
        db.query(Lesson).filter(Lesson.chapter == "ch1").delete()
        db.query(Problem).filter(Problem.chapter == "ch1").delete()
        db.commit()
        print("✅ 기존 데이터 삭제 완료")

        # Problems 삽입
        print("🔄 Problems 삽입 중...")
        for problem_data in problems_data:
            problem = Problem(**problem_data)
            db.add(problem)
        db.commit()
        print(f"✅ {len(problems_data)}개 Problems 삽입 완료")

        # Lessons 삽입
        print("🔄 Lessons 삽입 중...")
        for lesson_data in lessons_data:
            lesson = Lesson(**lesson_data)
            db.add(lesson)
        db.commit()
        print(f"✅ {len(lessons_data)}개 Lessons 삽입 완료")

        print("\n✨ Ch1 목업 데이터 삽입 완료!")

    except Exception as e:
        db.rollback()
        print(f"❌ 오류 발생: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
