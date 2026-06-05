from fastapi import APIRouter, Depends, HTTPException, status
from typing import Union
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.userModels import User
from app.schemas.reportSchemas import ReportResponse, ReportPendingResponse, ReportListResponse
from app.services.report.report_service import get_report_service, get_reports_list_service

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get(
    "/{track}",
    response_model=ReportListResponse,
    summary="트랙 리포트 목록 조회",
)
def get_reports_list(
    track: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    트랙 내 완료된 모든 챕터의 리포트 요약 목록을 조회합니다.

    **응답 내용**
    - chapter: 챕터 코드
    - title: 챕터 제목
    - completedAt: 완료 시간

    **상세 리포트는:**
    GET /reports/{track}/{chapter}를 호출하세요
    """

    result = get_reports_list_service(
        db=db,
        user_id=current_user.id,
        track=track
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 트랙의 완료된 리포트가 없습니다.",
        )

    return result


@router.get(
    "/{track}/{chapter}",
    response_model=Union[ReportPendingResponse, ReportResponse],
    summary="챕터 리포트 조회",
    responses={
        200: {
            "content": {
                "application/json": {
                    "examples": {
                        "pending": {
                            "summary": "리포트 생성 중",
                            "value": {
                                "status": "pending",
                                "message": "리포트를 생성 중입니다. 잠시 후 다시 확인해주세요."
                            }
                        },
                        "completed": {
                            "summary": "리포트 완성",
                            "value": {
                                "status": "completed",
                                "track": "ML",
                                "chapter": "01",
                                "chapterTitle": "PyTorch 기초",
                                "completedAt": "2024-01-15T10:30:00",
                                "totalProblems": 5,
                                "grade": "A+",
                                "xpEarned": 100,
                                "wrongCount": 0,
                                "hintCount": 0,
                                "weakConcepts": [],
                                "cobotComment": "완벽하게 이해했어요! 개념이 탄탄하네요. 👍",
                                "summary": "PyTorch의 기초 개념과 Tensor 연산을 모두 습득했습니다.",
                                "keyPoint": "Tensor의 shape, dtype, device 관리가 핵심입니다.",
                                "nextChapter": "다음 챕터에서는 이번 개념들을 활용해 더 복잡한 모델을 구현합니다.",
                                "opensource": [
                                    {
                                        "name": "PyTorch 공식 문서",
                                        "desc": "torch.Tensor 클래스의 모든 메서드 확인",
                                        "url": "https://pytorch.org/docs/stable/tensors.html"
                                    },
                                    {
                                        "name": "CS231n Tutorial",
                                        "desc": "NumPy/PyTorch 비교 자료",
                                        "url": "https://cs231n.github.io/python-numpy-tutorial/"
                                    },
                                    {
                                        "name": "밑바닥부터 시작하는 딥러닝",
                                        "desc": "PyTorch 기초부터 심화까지",
                                        "url": "https://github.com/WegraLee/deep-learning-from-scratch"
                                    }
                                ]
                            }
                        }
                    }
                }
            }
        }
    }
)
def get_report(
    track: str,
    chapter: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    챕터 완료 후 AI 생성 리포트를 조회합니다.

    **동작 방식**
    - POST /complete 호출 후 백그라운드에서 AI 리포트가 생성됩니다
    - status가 "pending"이면 생성 중입니다. 몇 초 후 다시 시도하세요
    - status가 "completed"이면 리포트가 준비되었습니다

    **리포트 내용**
    - grade: 정답률 기반 학점 (A+, A, B+, B, ...)
    - weakConcepts: 약점 개념 분석
    - cobotComment: 개인화된 피드백 (상황별 맞춤형)
    - summary: 챕터 핵심 요약
    - keyPoint: 다음 학습을 위한 포인트
    - nextChapter: 다음 챕터와의 연관성
    - opensource: 추천 학습 자료
    """

    result = get_report_service(db=db, user_id=current_user.id, track=track, chapter=chapter)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 챕터입니다. 먼저 챕터를 완료해주세요.",
        )

    # pending 상태 응답
    if result.get("status") == "pending":
        return ReportPendingResponse()

    # completed 상태 응답
    return result
