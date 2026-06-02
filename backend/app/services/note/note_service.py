from datetime import datetime, timezone
from typing import Any
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from app.models.noteModels import WrongAnswer
from app.models.problemModels import Problem
from app.models.dailyModels import DailyProblem
from app.schemas.noteSchemas import (
    WrongAnswerListItem,
    WrongAnswerListResponse,
    WrongAnswerDetailResponse,
    ProblemDetailResponse,
    ReviewProblemItem,
    ReviewProblemResponse,
    ReviewSubmitRequest,
    ReviewSubmitResponse,
    ReviewResultItem,
    DeleteWrongAnswerResponse,
)


SOURCE_LEARNING = "learning"
SOURCE_DAILY = "daily"


def to_date_string(dt: datetime) -> str:
    return dt.date().isoformat()


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


def get_track_problem_id(wrong_answer: WrongAnswer) -> int | None:
    return wrong_answer.track_problem_id


def get_daily_problem_id(wrong_answer: WrongAnswer) -> int | None:
    return wrong_answer.daily_problem_id


def validate_source_type(source_type: str) -> None:
    if source_type not in [SOURCE_LEARNING, SOURCE_DAILY]:
        raise HTTPException(
            status_code=400,
            detail="sourceType must be learning or daily",
        )


def get_learning_problem(
    db: Session,
    problem_id: int,
) -> Problem:
    problem = (
        db.query(Problem)
        .filter(Problem.id == problem_id)
        .first()
    )

    if problem is None:
        raise HTTPException(
            status_code=404,
            detail="Learning problem not found",
        )

    return problem


def get_daily_problem(
    db: Session,
    daily_problem_id: int,
    user_id: int,
) -> DailyProblem:
    daily_problem = (
        db.query(DailyProblem)
        .filter(DailyProblem.id == daily_problem_id)
        .filter(DailyProblem.user_id == user_id)
        .first()
    )

    if daily_problem is None:
        raise HTTPException(
            status_code=404,
            detail="Daily problem not found",
        )

    return daily_problem


def make_learning_problem_detail(problem: Problem) -> ProblemDetailResponse:
    return ProblemDetailResponse(
        sourceType=SOURCE_LEARNING,
        trackProblemId=problem.id,
        dailyProblemId=None,
        track=problem.track,
        chapter=problem.chapter,
        problemType=problem.problem_type,
        content=problem.content,
        answer=problem.answer,
        explanation=problem.explanation,
        hints=problem.hints,
    )


def make_daily_problem_detail(problem: DailyProblem) -> ProblemDetailResponse:
    return ProblemDetailResponse(
        sourceType=SOURCE_DAILY,
        trackProblemId=None,
        dailyProblemId=problem.id,
        track=None,
        chapter=None,
        problemType=problem.problem_type,
        content=problem.content,
        answer=problem.answer,
        explanation=problem.explanation,
    )


def make_problem_detail_from_wrong_answer(
    wrong_answer: WrongAnswer,
) -> ProblemDetailResponse:
    if wrong_answer.source_type == SOURCE_LEARNING:
        if wrong_answer.track_problem is None:
            raise HTTPException(
                status_code=404,
                detail="Learning problem not found",
            )

        return make_learning_problem_detail(wrong_answer.track_problem)

    if wrong_answer.source_type == SOURCE_DAILY:
        if wrong_answer.daily_problem is None:
            raise HTTPException(
                status_code=404,
                detail="Daily problem not found",
            )

        return make_daily_problem_detail(wrong_answer.daily_problem)

    raise HTTPException(
        status_code=400,
        detail="Invalid sourceType",
    )


def get_correct_answer_from_wrong_answer(wrong_answer: WrongAnswer) -> Any:
    if wrong_answer.source_type == SOURCE_LEARNING:
        if wrong_answer.track_problem is None:
            raise HTTPException(
                status_code=404,
                detail="Learning problem not found",
            )

        return wrong_answer.track_problem.answer

    if wrong_answer.source_type == SOURCE_DAILY:
        if wrong_answer.daily_problem is None:
            raise HTTPException(
                status_code=404,
                detail="Daily problem not found",
            )

        return wrong_answer.daily_problem.answer

    raise HTTPException(
        status_code=400,
        detail="Invalid sourceType",
    )


def make_wrong_answer_list_item(wrong_answer: WrongAnswer) -> WrongAnswerListItem:
    if wrong_answer.source_type == SOURCE_LEARNING:
        problem = wrong_answer.track_problem

        if problem is None:
            raise HTTPException(
                status_code=404,
                detail="Learning problem not found",
            )

        return WrongAnswerListItem(
            id=wrong_answer.id,
            sourceType=wrong_answer.source_type,
            trackProblemId=wrong_answer.track_problem_id,
            dailyProblemId=None,
            track=problem.track,
            chapter=problem.chapter,
            problemType=problem.problem_type,
            isResolved=wrong_answer.is_resolved,
            reviewCount=wrong_answer.review_count,
        )

    if wrong_answer.source_type == SOURCE_DAILY:
        problem = wrong_answer.daily_problem

        if problem is None:
            raise HTTPException(
                status_code=404,
                detail="Daily problem not found",
            )

        return WrongAnswerListItem(
            id=wrong_answer.id,
            sourceType=wrong_answer.source_type,
            trackProblemId=None,
            dailyProblemId=wrong_answer.daily_problem_id,
            track=None,
            chapter=None,
            problemType=problem.problem_type,
            isResolved=wrong_answer.is_resolved,
            reviewCount=wrong_answer.review_count,
        )

    raise HTTPException(
        status_code=400,
        detail="Invalid sourceType",
    )


def make_wrong_answer_detail(wrong_answer: WrongAnswer) -> WrongAnswerDetailResponse:
    problem_detail = make_problem_detail_from_wrong_answer(wrong_answer)
    correct_answer = get_correct_answer_from_wrong_answer(wrong_answer)

    return WrongAnswerDetailResponse(
        id=wrong_answer.id,
        sourceType=wrong_answer.source_type,
        trackProblemId=wrong_answer.track_problem_id,
        dailyProblemId=wrong_answer.daily_problem_id,
        userAnswer=wrong_answer.user_answer,
        correctAnswer=correct_answer,
        isResolved=wrong_answer.is_resolved,
        reviewCount=wrong_answer.review_count,
        date=to_date_string(wrong_answer.created_at),
        lastReviewedAt=wrong_answer.last_reviewed_at,
        problem=problem_detail,
    )



def get_wrong_answers_service(
    db: Session,
    user_id: int,
    track: str | None = None,
    source_type: str | None = None,
    is_resolved: bool | None = None,
) -> WrongAnswerListResponse:
    query = (
        db.query(WrongAnswer)
        .options(
            joinedload(WrongAnswer.track_problem),
            joinedload(WrongAnswer.daily_problem),
        )
        .filter(WrongAnswer.user_id == user_id)
    )

    if source_type is not None:
        validate_source_type(source_type)
        query = query.filter(WrongAnswer.source_type == source_type)

    if is_resolved is not None:
        query = query.filter(WrongAnswer.is_resolved == is_resolved)

    if track is not None:
        query = (
            query
            .outerjoin(Problem, WrongAnswer.track_problem_id == Problem.id)
            .filter(Problem.track == track)
        )

    wrong_answers = (
        query
        .order_by(WrongAnswer.created_at.desc())
        .all()
    )

    return WrongAnswerListResponse(
        wrongAnswers=[
            make_wrong_answer_list_item(item)
            for item in wrong_answers
        ]
    )


REVIEW_LIMIT = 5


def get_review_wrong_answers_service(
    db: Session,
    user_id: int,
    track: str | None = None,
    source_type: str | None = None,
) -> ReviewProblemResponse:
    query = (
        db.query(WrongAnswer)
        .options(
            joinedload(WrongAnswer.track_problem),
            joinedload(WrongAnswer.daily_problem),
        )
        .filter(WrongAnswer.user_id == user_id)
        .filter(WrongAnswer.is_resolved == False)
    )

    if source_type is not None:
        validate_source_type(source_type)
        query = query.filter(WrongAnswer.source_type == source_type)

    if track is not None:
        query = (
            query
            .outerjoin(Problem, WrongAnswer.track_problem_id == Problem.id)
            .filter(Problem.track == track)
        )

    wrong_answers = (
        query
        .order_by(func.random())
        .limit(REVIEW_LIMIT)
        .all()
    )

    review_items: list[ReviewProblemItem] = []

    for item in wrong_answers:
        problem_detail = make_problem_detail_from_wrong_answer(item)

        review_items.append(
            ReviewProblemItem(
                wrongAnswerId=item.id,
                sourceType=item.source_type,
                trackProblemId=item.track_problem_id,
                dailyProblemId=item.daily_problem_id,
                userAnswer=item.user_answer,
                problem=problem_detail,
            )
        )

    return ReviewProblemResponse(
        wrongAnswers=review_items
    )


def submit_review_answers_service(
    request: ReviewSubmitRequest,
    db: Session,
    user_id: int,
) -> ReviewSubmitResponse:
    results: list[ReviewResultItem] = []
    correct_count = 0

    for item in request.answers:
        wrong_answer = (
            db.query(WrongAnswer)
            .options(
                joinedload(WrongAnswer.track_problem),
                joinedload(WrongAnswer.daily_problem),
            )
            .filter(WrongAnswer.id == item.wrongAnswerId)
            .filter(WrongAnswer.user_id == user_id)
            .first()
        )

        if wrong_answer is None:
            raise HTTPException(
                status_code=404,
                detail=f"Wrong answer {item.wrongAnswerId} not found",
            )

        user_answer = normalize_answer(item.answer)
        correct_answer = normalize_answer(
            get_correct_answer_from_wrong_answer(wrong_answer)
        )

        is_multiple_choice = (
            (wrong_answer.source_type == SOURCE_LEARNING and wrong_answer.track_problem and wrong_answer.track_problem.problem_type == "multiple_choice")
            or
            (wrong_answer.source_type == SOURCE_DAILY and wrong_answer.daily_problem and wrong_answer.daily_problem.problem_type == "multiple_choice")
        )

        if is_multiple_choice:
            if isinstance(correct_answer, dict):
                correct_answer = correct_answer.get("correct_index")
            if isinstance(user_answer, dict):
                user_answer = user_answer.get("correct_index") or user_answer.get("answer")

        is_correct = user_answer == correct_answer

        wrong_answer.review_count += 1
        wrong_answer.last_reviewed_at = datetime.now(timezone.utc)

        if is_correct:
            wrong_answer.is_resolved = True
            correct_count += 1

        results.append(
            ReviewResultItem(
                wrongAnswerId=wrong_answer.id,
                sourceType=wrong_answer.source_type,
                trackProblemId=wrong_answer.track_problem_id,
                dailyProblemId=wrong_answer.daily_problem_id,
                isCorrect=is_correct,
            )
        )

    db.commit()

    return ReviewSubmitResponse(
        results=results,
        correctCount=correct_count,
        totalCount=len(request.answers),
    )


def get_wrong_answer_detail_service(
    wrong_answer_id: int,
    db: Session,
    user_id: int,
) -> WrongAnswerDetailResponse:
    wrong_answer = (
        db.query(WrongAnswer)
        .options(
            joinedload(WrongAnswer.track_problem),
            joinedload(WrongAnswer.daily_problem),
        )
        .filter(WrongAnswer.id == wrong_answer_id)
        .filter(WrongAnswer.user_id == user_id)
        .first()
    )

    if wrong_answer is None:
        raise HTTPException(
            status_code=404,
            detail="Wrong answer not found",
        )

    return make_wrong_answer_detail(wrong_answer)


def delete_wrong_answer_service(
    wrong_answer_id: int,
    db: Session,
    user_id: int,
) -> DeleteWrongAnswerResponse:
    wrong_answer = (
        db.query(WrongAnswer)
        .filter(WrongAnswer.id == wrong_answer_id)
        .filter(WrongAnswer.user_id == user_id)
        .first()
    )

    if wrong_answer is None:
        raise HTTPException(
            status_code=404,
            detail="Wrong answer not found",
        )

    db.delete(wrong_answer)
    db.commit()

    return DeleteWrongAnswerResponse(
        message="Wrong answer deleted successfully"
    )