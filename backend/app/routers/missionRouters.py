from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from pathlib import Path
from datetime import datetime, timezone
import os
import re
import json
import modal

# 단순 문자열 대신 정규식 패턴 사용 (점 뒤 eval은 메서드 호출이므로 허용)
_BLACKLIST_PATTERNS = [
    r"os\.system\s*\(",
    r"shutil\.rmtree\s*\(",
    r"__import__\s*\(",
    r"(?<!\w)open\s*\(",
    r"(?<!\.)\beval\s*\(",
    r"(?<!\.)\bexec\s*\(",
]

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.userModels import User
from app.models.progressModels import Progress
from app.services.report.report_service import generate_report_background

router = APIRouter()

MISSION_XP = 100
MISSION_CHAPTER = "mission"

_AICO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
MISSION_JSON_MAP = {
    "ML-회귀": _AICO_ROOT / "frontend" / "public" / "static" / "md" / "regression" / "mission" / "misson.json",
}


class MissionRunRequest(BaseModel):
    track: str
    blanks: dict[str, str]


class MissionRunResponse(BaseModel):
    stdout: str
    stderr: str
    returncode: int
    passed: bool
    r2: Optional[float] = None


class MissionSubmitResponse(BaseModel):
    passed: bool
    r2: Optional[float] = None
    isFirstCompletion: Optional[bool] = None  # 불합격 시 None
    xpEarned: int = 0
    stdout: str
    stderr: str
    returncode: int


def _build_code(track: str, blanks: dict) -> str:
    json_path = MISSION_JSON_MAP.get(track)
    if not json_path or not json_path.exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="미션을 찾을 수 없습니다.",
        )
    with open(json_path, encoding="utf-8") as f:
        mission = json.load(f)

    template: str = mission["content"]["template"]
    for key, value in blanks.items():
        template = template.replace(f"{{{{{key}}}}}", value)
    return template


def _check_blacklist(code: str) -> None:
    for pattern in _BLACKLIST_PATTERNS:
        if re.search(pattern, code):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"허용되지 않는 코드가 포함되어 있습니다: {pattern}",
            )


def _parse_r2(stdout: str) -> Optional[float]:
    match = re.search(r"R[²2]:\s*([\d.]+)", stdout)
    return float(match.group(1)) if match else None


def _execute_code(track: str, code: str) -> tuple[str, str, int]:
    """코드 실행 후 (stdout, stderr, returncode) 반환"""
    if track in ["ML-회귀", "CV", "NLP"]:
        try:
            run_code_gpu = modal.Function.from_name("aico-code-runner", "run_code_gpu")
            result_dict = run_code_gpu.remote(code)
            return result_dict["stdout"], result_dict["stderr"], result_dict["returncode"]
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"GPU 실행 오류: {str(e)}",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="지원하지 않는 트랙입니다.",
        )


@router.post("/run", response_model=MissionRunResponse)
def run_mission(
    payload: MissionRunRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    code = _build_code(payload.track, payload.blanks)
    _check_blacklist(code)

    stdout, stderr, returncode = _execute_code(payload.track, code)
    r2 = _parse_r2(stdout)
    passed = r2 is not None and r2 >= 0.65

    return MissionRunResponse(
        stdout=stdout,
        stderr=stderr,
        returncode=returncode,
        passed=passed,
        r2=r2,
    )


@router.post("/submit", response_model=MissionSubmitResponse)
def submit_mission(
    payload: MissionRunRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    code = _build_code(payload.track, payload.blanks)
    _check_blacklist(code)

    stdout, stderr, returncode = _execute_code(payload.track, code)
    r2 = _parse_r2(stdout)
    passed = r2 is not None and r2 >= 0.65

    # 불합격 시 DB 저장 없이 즉시 반환
    if not passed:
        return MissionSubmitResponse(
            passed=False,
            r2=r2,
            xpEarned=0,
            stdout=stdout,
            stderr=stderr,
            returncode=returncode,
        )

    # Progress upsert (track + chapter="mission")
    progress = (
        db.query(Progress)
        .filter_by(user_id=current_user.id, track=payload.track, chapter=MISSION_CHAPTER)
        .first()
    )

    is_first_completion = progress is None or not progress.is_completed

    if progress is None:
        progress = Progress(
            user_id=current_user.id,
            track=payload.track,
            chapter=MISSION_CHAPTER,
        )
        db.add(progress)

    progress.is_completed = True
    progress.completed_at = datetime.now(timezone.utc)
    if is_first_completion:
        progress.xp_earned = MISSION_XP
        current_user.xp += MISSION_XP

    db.commit()

    if is_first_completion:
        background_tasks.add_task(
            generate_report_background,
            user_id=current_user.id,
            track=payload.track,
            chapter=MISSION_CHAPTER,
        )

    return MissionSubmitResponse(
        passed=True,
        r2=r2,
        isFirstCompletion=is_first_completion,
        xpEarned=MISSION_XP if is_first_completion else 0,
        stdout=stdout,
        stderr=stderr,
        returncode=returncode,
    )
