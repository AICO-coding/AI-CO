import json
import re
import random
from datetime import datetime, date, time, timezone, timedelta
from pathlib import Path
from typing import Any
from anthropic import Anthropic
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.core.config import ANTHROPIC_API_KEY
from app.models.dailyModels import DailyProblem, DailyResult
from app.models.noteModels import WrongAnswer
from app.models.userModels import User
from app.models.progressModels import Progress
from app.schemas.dailySchemas import (
    DailyProblemItem,
    DailyResponse,
    DailySubmitRequest,
    DailySubmitResponse,
    DailySubmitResultItem,
    DailyResultResponse,
)


KST = timezone(timedelta(hours=9))

DAILY_PROBLEM_COUNT = 5
XP_PER_PROBLEM = 20

SOURCE_DAILY = "daily"

TRACK_FOLDER_MAP: dict[str, str] = {
    "NLP": "nlp",
    "CV": "cv",
    "ML-회귀": "regression",
    "ML-분류": "classification",
}

MD_BASE_PATH = Path(__file__).parents[4] / "frontend" / "public" / "static" / "md"

anthropic_client = Anthropic(api_key=ANTHROPIC_API_KEY)


def get_today_kst() -> date:
    return datetime.now(KST).date()


def get_end_of_today_kst() -> datetime:
    today = get_today_kst()
    return datetime.combine(today, time(23, 59, 59), tzinfo=KST)


def to_date_string(value: date) -> str:
    return value.isoformat()


def normalize_answer(answer: Any) -> Any:
    if isinstance(answer, str):
        return answer.strip()

    if isinstance(answer, dict):
        return {
            key: normalize_answer(value)
            for key, value in answer.items()
        }

    if isinstance(answer, list):
        return [
            normalize_answer(value)
            for value in answer
        ]

    return answer


def get_user_progress_summary(
    db: Session,
    user_id: int,
) -> list[dict[str, Any]]:
    progress_list = (
        db.query(Progress)
        .filter(Progress.user_id == user_id)
        .order_by(Progress.completion_rate.asc())
        .all()
    )

    return [
        {
            "track": progress.track,
            "chapter": progress.chapter,
            "isCompleted": progress.is_completed,
            "completionRate": progress.completion_rate,
            "xpEarned": progress.xp_earned,
            "hintUsed": progress.hint_used,
            "report": progress.report,
            "lastLessonId": progress.last_lesson_id,
        }
        for progress in progress_list
    ]


def get_learned_progress(db: Session, user_id: int) -> list[Progress]:
    return (
        db.query(Progress)
        .filter(Progress.user_id == user_id)
        .filter(Progress.completion_rate > 0)
        .all()
    )


def select_chapters_weighted(
    learned: list[Progress],
    n: int = DAILY_PROBLEM_COUNT,
) -> list[Progress]:
    return random.choices(learned, k=n)


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text).strip()


def lesson_sort_key(path: Path) -> int:
    numbers = re.findall(r"\d+", path.stem)
    return int(numbers[-1]) if numbers else 0


def read_chapter_content(track: str, chapter: str) -> str:
    folder = TRACK_FOLDER_MAP.get(track)
    if not folder:
        return ""

    chapter_dir = MD_BASE_PATH / folder / chapter
    if not chapter_dir.exists():
        return ""

    texts = [
        strip_html(md_file.read_text(encoding="utf-8"))
        for md_file in sorted(chapter_dir.glob("*.md"), key=lesson_sort_key)
    ]
    return "\n\n".join(texts)


def build_daily_prompt(selected_chapters: list[Progress]) -> str:
    sections = []
    for i, progress in enumerate(selected_chapters, start=1):
        content = read_chapter_content(progress.track, progress.chapter)
        sections.append(
            f"[문제 {i}] track: {progress.track}, chapter: {progress.chapter}\n"
            f"강의자료:\n{content or '(자료 없음)'}"
        )

    chapters_text = "\n\n---\n\n".join(sections)

    return f"""당신은 AI 학습 플랫폼의 전문 문제 출제자입니다.
학습자가 배운 내용을 제대로 이해했는지 확인하는 복습용 객관식 문제를 출제합니다.

아래 5개 슬롯 각각에 대해 객관식 문제를 1개씩 총 5개 만들어주세요.
같은 챕터가 여러 슬롯에 등장할 경우, 각 슬롯마다 서로 다른 개념을 묻는 문제를 출제하세요.

[문제 품질 기준]
- 강의자료에 명시된 개념·용어·원리를 기반으로 출제할 것
- 단순 암기가 아닌 개념 이해를 확인하는 질문으로 구성할 것
- 질문은 명확하고 모호함이 없어야 하며, 한 가지 정답만 존재해야 함
- 오답 보기는 그럴듯하지만 명확히 틀린 내용으로 구성할 것 (완전히 엉뚱한 보기 금지)
- 보기 길이는 균일하게 맞출 것 (정답 보기만 유독 길거나 짧으면 정답이 노출됨)
- 모든 질문과 보기는 한국어로 작성할 것

[형식 규칙]
- 보기는 반드시 4개
- correct_index: 정답 보기의 번호 (1=첫 번째, 2=두 번째, 3=세 번째, 4=네 번째)
- explanation: 왜 정답인지, 왜 오답들이 틀렸는지 한국어로 2~3문장으로 설명

{chapters_text}

JSON 배열로만 응답하세요. 앞뒤 설명 없이 JSON만:
[
  {{
    "track": "<슬롯에 명시된 track 그대로>",
    "chapter": "<슬롯에 명시된 chapter 그대로>",
    "content": {{
      "question": "<질문>",
      "choices": ["<보기1>", "<보기2>", "<보기3>", "<보기4>"]
    }},
    "answer": {{"correct_index": <1~4>}},
    "explanation": "<정답 및 오답 이유 설명>"
  }},
  ...
]"""


def call_ai_for_daily_problems(selected_chapters: list[Progress]) -> list[dict[str, Any]]:
    prompt = build_daily_prompt(selected_chapters)

    message = anthropic_client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )

    response_text = message.content[0].text

    try:
        problems = json.loads(response_text)
    except json.JSONDecodeError:
        start = response_text.find("[")
        end = response_text.rfind("]") + 1
        if start != -1 and end > start:
            problems = json.loads(response_text[start:end])
        else:
            raise ValueError("AI 응답 JSON 파싱 실패")

    for problem in problems:
        problem["problem_type"] = "multiple_choice"

    return problems


def generate_default_daily_problem_payloads() -> list[dict[str, Any]]:
    return [
        {
            "problem_type": "multiple_choice",
            "track": "ML-회귀",
            "chapter": "ch1",
            "content": {
                "choices": [
                    "입력과 출력의 관계를 선형식으로 표현한다",
                    "이미지만 분류한다",
                    "강화학습 알고리즘이다",
                    "데이터베이스 정규화 기법이다",
                ],
                "question": "다음 중 선형 회귀에 대한 설명으로 옳은 것은?",
            },
            "answer": {"correct_index": 1},
            "explanation": "선형 회귀는 입력 변수와 출력 변수의 관계를 선형식으로 표현해 값을 예측하는 모델입니다.",
        },
        {
            "problem_type": "multiple_choice",
            "track": "ML-분류",
            "chapter": "ch1",
            "content": {
                "choices": [
                    "연속적인 숫자 예측",
                    "데이터를 정해진 클래스 중 하나로 구분",
                    "데이터베이스 테이블 생성",
                    "이미지 해상도 증가",
                ],
                "question": "분류 문제의 목표로 가장 알맞은 것은?",
            },
            "answer": {"correct_index": 2},
            "explanation": "분류는 입력 데이터를 정해진 클래스 중 하나로 구분하는 문제입니다.",
        },
        {
            "problem_type": "multiple_choice",
            "track": "ML-회귀",
            "chapter": "ch2",
            "content": {
                "choices": [
                    "훈련 데이터에는 잘 맞지만 새로운 데이터에는 성능이 낮은 상태",
                    "항상 좋은 모델 상태",
                    "데이터가 전혀 없는 상태",
                    "정답이 여러 개인 상태",
                ],
                "question": "과적합에 대한 설명으로 옳은 것은?",
            },
            "answer": {"correct_index": 1},
            "explanation": "과적합은 모델이 훈련 데이터에 지나치게 맞춰져 새로운 데이터에는 일반화가 잘 안 되는 상태입니다.",
        },
        {
            "problem_type": "multiple_choice",
            "track": "CV",
            "chapter": "ch1",
            "content": {
                "choices": [
                    "이미지의 지역적 특징 추출",
                    "문장을 토큰으로 분리",
                    "정답 라벨 삭제",
                    "데이터베이스 인덱스 생성",
                ],
                "question": "CNN에서 합성곱 층의 주요 역할은?",
            },
            "answer": {"correct_index": 1},
            "explanation": "CNN의 합성곱 층은 이미지의 지역적인 패턴이나 특징을 추출하는 데 사용됩니다.",
        },
        {
            "problem_type": "multiple_choice",
            "track": "NLP",
            "chapter": "ch1",
            "content": {
                "choices": [
                    "문장을 작은 단위로 나누는 과정",
                    "이미지를 회전하는 과정",
                    "모델의 파라미터를 삭제하는 과정",
                    "데이터를 암호화하는 과정",
                ],
                "question": "토큰화의 의미로 가장 적절한 것은?",
            },
            "answer": {"correct_index": 1},
            "explanation": "토큰화는 문장을 단어, 서브워드, 문자 등 작은 단위로 나누는 과정입니다.",
        },
    ]


def generate_ai_daily_problem_payloads(learned: list[Progress]) -> list[dict[str, Any]]:
    selected_chapters = select_chapters_weighted(learned)
    return call_ai_for_daily_problems(selected_chapters)


def get_daily_problems_by_date(
    db: Session,
    user_id: int,
    target_date: date,
) -> list[DailyProblem]:
    return (
        db.query(DailyProblem)
        .filter(DailyProblem.user_id == user_id)
        .filter(DailyProblem.date == target_date)
        .order_by(DailyProblem.problem_order.asc())
        .all()
    )


def create_daily_problems(
    db: Session,
    user_id: int,
    target_date: date,
    learned: list[Progress],
) -> list[DailyProblem]:
    payloads = generate_ai_daily_problem_payloads(learned)

    if len(payloads) != DAILY_PROBLEM_COUNT:
        raise HTTPException(
            status_code=500,
            detail="데일리 문제는 반드시 5개 생성되어야 합니다.",
        )

    daily_problems: list[DailyProblem] = []

    for index, payload in enumerate(payloads, start=1):
        daily_problem = DailyProblem(
            user_id=user_id,
            date=target_date,
            problem_order=index,
            problem_type=payload["problem_type"],
            track=payload.get("track"),
            chapter=payload.get("chapter"),
            content=payload["content"],
            answer=payload["answer"],
            explanation=payload.get("explanation"),
        )

        db.add(daily_problem)
        daily_problems.append(daily_problem)

    db.commit()

    for daily_problem in daily_problems:
        db.refresh(daily_problem)

    return daily_problems


def get_or_create_today_daily_problems(
    db: Session,
    user_id: int,
    learned: list[Progress],
) -> list[DailyProblem]:
    today = get_today_kst()

    daily_problems = get_daily_problems_by_date(
        db=db,
        user_id=user_id,
        target_date=today,
    )

    if daily_problems:
        return daily_problems

    return create_daily_problems(
        db=db,
        user_id=user_id,
        target_date=today,
        learned=learned,
    )


def get_today_daily_result(
    db: Session,
    user_id: int,
) -> DailyResult | None:
    today = get_today_kst()

    return (
        db.query(DailyResult)
        .filter(DailyResult.user_id == user_id)
        .filter(DailyResult.date == today)
        .first()
    )


def make_daily_problem_item(problem: DailyProblem) -> DailyProblemItem:
    return DailyProblemItem(
        dailyProblemId=problem.id,
        problemType=problem.problem_type,
        track=problem.track,
        chapter=problem.chapter,
        content=problem.content,
    )


def get_today_daily_service(
    db: Session,
    user_id: int,
) -> DailyResponse:
    today = get_today_kst()

    learned = get_learned_progress(db=db, user_id=user_id)

    if not learned:
        return DailyResponse(
            date=to_date_string(today),
            dailyProblems=[],
            isCompleted=False,
            expiresAt=get_end_of_today_kst().isoformat(),
            message="데일리 문제는 학습한 챕터를 기반으로 출제돼요. 먼저 챕터 학습을 진행해주세요!",
        )

    daily_problems = get_or_create_today_daily_problems(
        db=db,
        user_id=user_id,
        learned=learned,
    )

    daily_result = get_today_daily_result(
        db=db,
        user_id=user_id,
    )

    return DailyResponse(
        date=to_date_string(today),
        dailyProblems=[
            make_daily_problem_item(problem)
            for problem in daily_problems
        ],
        isCompleted=daily_result is not None,
        expiresAt=get_end_of_today_kst().isoformat(),
    )


def add_xp_to_user_if_possible(
    db: Session,
    user_id: int,
    xp_earned: int,
) -> None:
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return

    if hasattr(User, "xp"):
        current_xp = getattr(user, "xp") or 0
        setattr(user, "xp", current_xp + xp_earned)


def submit_today_daily_service(
    request: DailySubmitRequest,
    db: Session,
    user_id: int,
) -> DailySubmitResponse:
    today = get_today_kst()

    existing_result = get_today_daily_result(
        db=db,
        user_id=user_id,
    )

    if existing_result is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="오늘의 데일리 태스크는 이미 제출되었습니다.",
        )

    learned = get_learned_progress(db=db, user_id=user_id)
    daily_problems = get_or_create_today_daily_problems(
        db=db,
        user_id=user_id,
        learned=learned,
    )

    if len(daily_problems) != DAILY_PROBLEM_COUNT:
        raise HTTPException(
            status_code=500,
            detail="오늘의 데일리 문제가 5개가 아닙니다.",
        )

    submitted_answer_map = {
        item.dailyProblemId: item.answer
        for item in request.answers
    }

    today_problem_ids = {
        problem.id
        for problem in daily_problems
    }

    submitted_problem_ids = set(submitted_answer_map.keys())

    if submitted_problem_ids != today_problem_ids:
        raise HTTPException(
            status_code=400,
            detail="오늘의 데일리 문제 5개에 대한 답안을 모두 제출해야 합니다.",
        )

    correct_count = 0
    result_items: list[dict[str, Any]] = []
    response_result_items: list[DailySubmitResultItem] = []

    for problem in daily_problems:
        user_answer = normalize_answer(submitted_answer_map[problem.id])
        correct_answer = normalize_answer(problem.answer)

        user_index = user_answer.get("answer") if isinstance(user_answer, dict) else user_answer
        correct_index = correct_answer.get("correct_index") if isinstance(correct_answer, dict) else correct_answer
        is_correct = user_index == correct_index

        wrong_answer_id = None

        if is_correct:
            correct_count += 1
        else:
            wrong_answer = WrongAnswer(
                user_id=user_id,
                source_type=SOURCE_DAILY,
                track_problem_id=None,
                daily_problem_id=problem.id,
                user_answer=user_answer,
                is_resolved=False,
                review_count=0,
            )

            db.add(wrong_answer)
            db.flush()

            wrong_answer_id = wrong_answer.id

        result_item = {
            "dailyProblemId": problem.id,
            "problemType": problem.problem_type,
            "track": problem.track,
            "chapter": problem.chapter,
            "content": problem.content,
            "userAnswer": user_answer,
            "correctAnswer": {"answer": correct_index},
            "isCorrect": is_correct,
            "explanation": problem.explanation,
            "wrongAnswerId": wrong_answer_id,
        }

        result_items.append(result_item)

        response_result_items.append(
            DailySubmitResultItem(**result_item)
        )

    total_problems = DAILY_PROBLEM_COUNT
    xp_earned = correct_count * XP_PER_PROBLEM
    is_perfect = correct_count == total_problems

    daily_result = DailyResult(
        user_id=user_id,
        date=today,
        score=correct_count,
        total_problems=total_problems,
        xp_earned=xp_earned,
        is_perfect=is_perfect,
        results=result_items,
    )

    db.add(daily_result)

    add_xp_to_user_if_possible(
        db=db,
        user_id=user_id,
        xp_earned=xp_earned,
    )

    db.commit()

    return DailySubmitResponse(
        date=to_date_string(today),
        score=correct_count,
        totalProblems=total_problems,
        xpEarned=xp_earned,
        isPerfect=is_perfect,
        results=response_result_items,
    )


def get_today_daily_result_service(
    db: Session,
    user_id: int,
) -> DailyResultResponse:
    daily_result = get_today_daily_result(
        db=db,
        user_id=user_id,
    )

    if daily_result is None:
        raise HTTPException(
            status_code=404,
            detail="오늘의 데일리 결과가 없습니다.",
        )

    return DailyResultResponse(
        date=to_date_string(daily_result.date),
        score=daily_result.score,
        totalProblems=daily_result.total_problems,
        xpEarned=daily_result.xp_earned,
        isPerfect=daily_result.is_perfect,
        results=daily_result.results,
        completedAt=daily_result.completed_at,
    )