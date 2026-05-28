from datetime import datetime, date, time, timezone, timedelta
from typing import Any
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
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


def generate_default_daily_problem_payloads() -> list[dict[str, Any]]:
    return [
        {
            "track": "ML-회기",
            "chapter": "ch1",
            "problem_type": "multiple_choice",
            "content": {
                "question": "다음 중 선형 회귀에 대한 설명으로 옳은 것은?",
                "choices": [
                    "입력과 출력의 관계를 선형식으로 표현한다",
                    "이미지만 분류한다",
                    "강화학습 알고리즘이다",
                    "데이터베이스 정규화 기법이다",
                ],
            },
            "answer": {"answer": 1},
            "explanation": "선형 회귀는 입력 변수와 출력 변수의 관계를 선형식으로 표현해 값을 예측하는 모델입니다.",
            "hints": ["입력과 출력 사이의 관계를 생각해보세요."],
        },
        {
            "track": "ML-분류",
            "chapter": "ch1",
            "problem_type": "multiple_choice",
            "content": {
                "question": "분류 문제의 목표로 가장 알맞은 것은?",
                "choices": [
                    "연속적인 숫자 예측",
                    "데이터를 정해진 클래스 중 하나로 구분",
                    "데이터베이스 테이블 생성",
                    "이미지 해상도 증가",
                ],
            },
            "answer": {"answer": 2},
            "explanation": "분류는 입력 데이터를 정해진 클래스 중 하나로 구분하는 문제입니다.",
            "hints": ["분류는 카테고리를 예측하는 문제입니다."],
        },
        {
            "track": "ML-회기",
            "chapter": "ch2",
            "problem_type": "multiple_choice",
            "content": {
                "question": "과적합에 대한 설명으로 옳은 것은?",
                "choices": [
                    "훈련 데이터에는 잘 맞지만 새로운 데이터에는 성능이 낮은 상태",
                    "항상 좋은 모델 상태",
                    "데이터가 전혀 없는 상태",
                    "정답이 여러 개인 상태",
                ],
            },
            "answer": {"answer": 1},
            "explanation": "과적합은 모델이 훈련 데이터에 지나치게 맞춰져 새로운 데이터에는 일반화가 잘 안 되는 상태입니다.",
            "hints": ["훈련 데이터와 새로운 데이터 성능 차이를 생각해보세요."],
        },
        {
            "track": "CV",
            "chapter": "ch1",
            "problem_type": "multiple_choice",
            "content": {
                "question": "CNN에서 합성곱 층의 주요 역할은?",
                "choices": [
                    "이미지의 지역적 특징 추출",
                    "문장을 토큰으로 분리",
                    "정답 라벨 삭제",
                    "데이터베이스 인덱스 생성",
                ],
            },
            "answer": {"answer": 1},
            "explanation": "CNN의 합성곱 층은 이미지의 지역적인 패턴이나 특징을 추출하는 데 사용됩니다.",
            "hints": ["이미지에서 작은 영역의 특징을 찾는 과정을 생각해보세요."],
        },
        {
            "track": "NLP",
            "chapter": "ch1",
            "problem_type": "multiple_choice",
            "content": {
                "question": "토큰화의 의미로 가장 적절한 것은?",
                "choices": [
                    "문장을 작은 단위로 나누는 과정",
                    "이미지를 회전하는 과정",
                    "모델의 파라미터를 삭제하는 과정",
                    "데이터를 암호화하는 과정",
                ],
            },
            "answer": {"answer": 1},
            "explanation": "토큰화는 문장을 단어, 서브워드, 문자 등 작은 단위로 나누는 과정입니다.",
            "hints": ["문장을 모델이 처리하기 쉬운 단위로 나누는 과정입니다."],
        },
    ]


def generate_ai_daily_problem_payloads(
    db: Session,
    user_id: int,
) -> list[dict[str, Any]]:
    """
    실제 AI 문제 생성 연결은 이 함수에서 구현하면 됨.

    현재는 progress를 조회한 뒤, 테스트용 샘플 문제를 반환함.
    이후 OpenAI API 등을 연결할 때 progress_summary를 프롬프트에 넣으면 됨.
    """

    progress_summary = get_user_progress_summary(
        db=db,
        user_id=user_id,
    )

    # 추후 AI 프롬프트에 progress_summary 사용
    # 예:
    # prompt = build_daily_prompt(progress_summary)
    # ai_response = call_ai(prompt)
    # return parse_ai_response(ai_response)

    return generate_default_daily_problem_payloads()


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
) -> list[DailyProblem]:
    payloads = generate_ai_daily_problem_payloads(
        db=db,
        user_id=user_id,
    )

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
            track=payload["track"],
            chapter=payload["chapter"],
            problem_type=payload["problem_type"],
            content=payload["content"],
            answer=payload["answer"],
            explanation=payload.get("explanation"),
            hints=payload.get("hints"),
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
        track=problem.track,
        chapter=problem.chapter,
        problemType=problem.problem_type,
        content=problem.content,
    )


def get_today_daily_service(
    db: Session,
    user_id: int,
) -> DailyResponse:
    today = get_today_kst()

    daily_problems = get_or_create_today_daily_problems(
        db=db,
        user_id=user_id,
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

    daily_problems = get_or_create_today_daily_problems(
        db=db,
        user_id=user_id,
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

        is_correct = user_answer == correct_answer

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
            "track": problem.track,
            "chapter": problem.chapter,
            "problemType": problem.problem_type,
            "content": problem.content,
            "userAnswer": user_answer,
            "correctAnswer": problem.answer,
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