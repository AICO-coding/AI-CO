from datetime import datetime, timezone
from typing import Any
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from app.models.noteModels import WrongAnswer
from app.models.problemModels import Problem
from app.schemas.noteSchemas import (
    WrongAnswerCreateRequest,
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


def make_problem_detail(problem: Problem) -> ProblemDetailResponse:
    return ProblemDetailResponse(
        track=problem.track,
        chapter=problem.chapter,
        problemType=problem.problem_type,
        content=problem.content,
        answer=problem.answer,
        hints=problem.hints,
    )


def make_wrong_answer_list_item(wrong_answer: WrongAnswer) -> WrongAnswerListItem:
    problem = wrong_answer.problem

    return WrongAnswerListItem(
        id=wrong_answer.id,
        problemId=wrong_answer.problem_id,
        track=problem.track,
        chapter=problem.chapter,
        problemType=problem.problem_type,
        sourceType=wrong_answer.source_type,
        isResolved=wrong_answer.is_resolved,
        reviewCount=wrong_answer.review_count,
        date=to_date_string(wrong_answer.created_at),
    )


def make_wrong_answer_detail(wrong_answer: WrongAnswer) -> WrongAnswerDetailResponse:
    problem = wrong_answer.problem

    return WrongAnswerDetailResponse(
        id=wrong_answer.id,
        problemId=wrong_answer.problem_id,
        sourceType=wrong_answer.source_type,
        userAnswer=wrong_answer.user_answer,
        correctAnswer=problem.answer,
        isResolved=wrong_answer.is_resolved,
        reviewCount=wrong_answer.review_count,
        date=to_date_string(wrong_answer.created_at),
        lastReviewedAt=wrong_answer.last_reviewed_at,
        problem=make_problem_detail(problem),
    )


def create_wrong_answer_service(
    request: WrongAnswerCreateRequest,
    db: Session,
    user_id: int,
) -> WrongAnswerDetailResponse:
    problem = (
        db.query(Problem)
        .filter(Problem.id == request.problemId)
        .first()
    )

    if problem is None:
        raise HTTPException(status_code=404, detail="Problem not found")

    wrong_answer = WrongAnswer(
        user_id=user_id,
        problem_id=request.problemId,
        source_type=request.sourceType,
        user_answer=request.userAnswer,
        is_resolved=False,
        review_count=0,
    )

    db.add(wrong_answer)
    db.commit()
    db.refresh(wrong_answer)

    wrong_answer = (
        db.query(WrongAnswer)
        .options(joinedload(WrongAnswer.problem))
        .filter(WrongAnswer.id == wrong_answer.id)
        .filter(WrongAnswer.user_id == user_id)
        .first()
    )

    return make_wrong_answer_detail(wrong_answer)


def get_wrong_answers_service(
    db: Session,
    user_id: int,
    track: str | None = None,
    source_type: str | None = None,
    is_resolved: bool | None = None,
) -> WrongAnswerListResponse:
    query = (
        db.query(WrongAnswer)
        .options(joinedload(WrongAnswer.problem))
        .join(Problem, WrongAnswer.problem_id == Problem.id)
        .filter(WrongAnswer.user_id == user_id)
    )

    if track is not None:
        query = query.filter(Problem.track == track)

    if source_type is not None:
        query = query.filter(WrongAnswer.source_type == source_type)

    if is_resolved is not None:
        query = query.filter(WrongAnswer.is_resolved == is_resolved)

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


def get_review_wrong_answers_service(
    db: Session,
    user_id: int,
    limit: int = 5,
    track: str | None = None,
    source_type: str | None = None,
) -> ReviewProblemResponse:
    query = (
        db.query(WrongAnswer)
        .options(joinedload(WrongAnswer.problem))
        .join(Problem, WrongAnswer.problem_id == Problem.id)
        .filter(WrongAnswer.user_id == user_id)
        .filter(WrongAnswer.is_resolved == False)
    )

    if track is not None:
        query = query.filter(Problem.track == track)

    if source_type is not None:
        query = query.filter(WrongAnswer.source_type == source_type)

    wrong_answers = (
        query
        .order_by(WrongAnswer.created_at.desc())
        .limit(limit)
        .all()
    )

    return ReviewProblemResponse(
        wrongAnswers=[
            ReviewProblemItem(
                wrongAnswerId=item.id,
                problemId=item.problem_id,
                sourceType=item.source_type,
                userAnswer=item.user_answer,
                problem=make_problem_detail(item.problem),
            )
            for item in wrong_answers
        ]
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
            .options(joinedload(WrongAnswer.problem))
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
        correct_answer = normalize_answer(wrong_answer.problem.answer)

        is_correct = user_answer == correct_answer

        wrong_answer.review_count += 1
        wrong_answer.last_reviewed_at = datetime.now(timezone.utc)

        if is_correct:
            wrong_answer.is_resolved = True
            correct_count += 1

        results.append(
            ReviewResultItem(
                wrongAnswerId=wrong_answer.id,
                problemId=wrong_answer.problem_id,
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
        .options(joinedload(WrongAnswer.problem))
        .filter(WrongAnswer.id == wrong_answer_id)
        .filter(WrongAnswer.user_id == user_id)
        .first()
    )

    if wrong_answer is None:
        raise HTTPException(status_code=404, detail="Wrong answer not found")

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
        raise HTTPException(status_code=404, detail="Wrong answer not found")

    db.delete(wrong_answer)
    db.commit()

    return DeleteWrongAnswerResponse(
        message="Wrong answer deleted successfully"
    )