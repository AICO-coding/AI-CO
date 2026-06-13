from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from pathlib import Path
from datetime import datetime, timezone
import asyncio
import json
import os
import re
import modal

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
    "ML-회귀": _AICO_ROOT / "frontend" / "public" / "static" / "md" / "regression" / "mission" / "mission.json",
    "CV": _AICO_ROOT / "frontend" / "public" / "static" / "md" / "cv" / "mission" / "mission.json",
    "NLP": _AICO_ROOT / "frontend" / "public" / "static" / "md" / "nlp" / "mission" / "mission.json",
}


class MissionHintRequest(BaseModel):
    track: str
    todoId: int


class MissionHintResponse(BaseModel):
    text: str
    xpDeducted: int


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
    isFirstCompletion: Optional[bool] = None 
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


def _parse_accuracy(stdout: str) -> Optional[float]:
    match = re.search(r"Test Accuracy:\s*([\d.]+)", stdout)
    return float(match.group(1)) if match else None


def _evaluate_passed(track: str, stdout: str) -> tuple[bool, Optional[float], Optional[float]]:
    if track == "CV":
        accuracy = _parse_accuracy(stdout)
        passed = accuracy is not None and accuracy >= 30.0
        return passed, None, accuracy
    else:
        r2 = _parse_r2(stdout)
        passed = r2 is not None and r2 >= 0.65
        return passed, r2, None


def _execute_code(track: str, code: str) -> tuple[str, str, int]:
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


@router.post("/hint", response_model=MissionHintResponse)
def use_mission_hint(
    payload: MissionHintRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    json_path = MISSION_JSON_MAP.get(payload.track)
    if not json_path or not json_path.exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="미션을 찾을 수 없습니다.",
        )

    with open(json_path, encoding="utf-8") as f:
        mission = json.load(f)

    hints = mission["content"].get("hints", [])
    hint = next((h for h in hints if h["todoId"] == payload.todoId), None)
    if not hint:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="힌트를 찾을 수 없습니다.",
        )

    xp_cost = hint.get("xpCost", 10)
    current_user.xp = max(0, current_user.xp - xp_cost)
    db.commit()

    return MissionHintResponse(text=hint["text"], xpDeducted=xp_cost)


@router.post("/run/stream")
async def run_mission_stream(
    payload: MissionRunRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    code = _build_code(payload.track, payload.blanks)
    _check_blacklist(code)

    async def generate():
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None, _execute_code, payload.track, code)

        elapsed = 0
        while not future.done():
            yield f"data: {json.dumps({'type': 'status', 'message': f'GPU 실행 중... {elapsed}s'})}\n\n"
            await asyncio.sleep(1)
            elapsed += 1

        try:
            stdout, stderr, returncode = future.result()
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'message': str(e)})}\n\n"
            return

        for line in stdout.split('\n'):
            yield f"data: {json.dumps({'type': 'stdout', 'line': line})}\n\n"
        if stderr:
            for line in stderr.split('\n'):
                if line:
                    yield f"data: {json.dumps({'type': 'stderr', 'line': line})}\n\n"
        yield f"data: {json.dumps({'type': 'done', 'returncode': returncode})}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")


@router.post("/run", response_model=MissionRunResponse)
def run_mission(
    payload: MissionRunRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    code = _build_code(payload.track, payload.blanks)
    _check_blacklist(code)

    stdout, stderr, returncode = _execute_code(payload.track, code)
    passed, r2, _ = _evaluate_passed(payload.track, stdout)

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
    passed, r2, _ = _evaluate_passed(payload.track, stdout)

    if not passed:
        return MissionSubmitResponse(
            passed=False,
            r2=r2,
            xpEarned=0,
            stdout=stdout,
            stderr=stderr,
            returncode=returncode,
        )

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