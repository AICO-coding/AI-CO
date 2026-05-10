from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.userModels import User
from app.schemas.progressSchemas import AllProgressResponse, TrackProgressResponse
from app.services.progress.progress_service import (
    get_all_progress_service,
    get_track_progress_service,
)

router = APIRouter(prefix="/progress", tags=["Progress"])


@router.get("", response_model=AllProgressResponse)
def get_all_progress(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """유저의 전체 트랙별 학습 진도 조회"""
    return get_all_progress_service(db=db, user_id=current_user.id)


@router.get("/{track}", response_model=TrackProgressResponse)
def get_track_progress(
    track: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """특정 트랙의 챕터별 학습 진도 조회"""
    result = get_track_progress_service(db=db, user_id=current_user.id, track=track)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="유효하지 않은 트랙입니다. ML, CV, NLP 중 하나를 입력하세요."
        )
    return result
