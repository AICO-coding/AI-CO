# AI 코딩 학습 플랫폼 'AICO'

</br>

> **AICO**는 ML/CV/NLP를 단계별로 학습할 수 있는 인터랙티브 교육 플랫폼입니다.  
> 학습 트랙 빈칸 채우기, 객관식 문제, 인터랙티브 실험, 챕터 미션, 일일 퀴즈, 오답노트, AI 리포트를 통해 완결된 학습 사이클을 제공합니다.
</br>

![Frame](https://github.com/user-attachments/assets/01158b53-9f9e-4ea8-98d4-06c6f332c753)
</br>

</br>

😽🤖 Service [overview](https://github.com/user-attachments/files/28928182/default.pdf) and [demo video](https://www.youtube.com/watch?v=We1TV7phG-Y) 

</br>

## 주요 기능

### 학습 트랙
ML-분류 · ML-회귀 · CV · NLP 4개 트랙, 트랙별 7개 이상의 챕터 제공

| 레슨 타입 | 설명 |
|---|---|
| `concept_image` | 이미지 + 개념 설명 |
| `concept_code` | 코드 블록 + 설명 |
| `code_fill` | 빈칸 채우기 코딩 문제 |
| `multiple_choice` | 객관식 문제 |
| `parameter` | 인터랙티브 실험 |

- 챕터 완료 시 XP 지급, 진도 저장
- 단계별 힌트 / 정답 공개 기능 제공
- 챕터 완료 후 AI 요약 리포트 자동 생성

### 최종 미션 
- 트랙의 모든 챕터 완료 시 잠금 해제
- 빈칸 채우기 형식의 전체 코드 완성 문제
- Modal T4 GPU에서 실제 실행 후 정확도 / R² 기준 합격 판정
- 실행 중 Server-Sent Events(SSE)로 실시간 로그 스트리밍
- 힌트 사용 시 XP 차감, 합격 시 XP 지급 + 성공 모달

### 데일리 퀴즈
- 매일 트랙별 AI 생성 문제 5개 제공
- 제출 후 정답 / 오답 · 해설 확인
- 오답은 오답노트에 자동 등록

### 오답노트
- 학습 문제 · 데일리 퀴즈 오답 자동 수집
- 트랙별 분류, 복습 모드 (순차 풀이 + 최종 채점)
- 데일리 오답: 날짜별 캘린더로 확인

### AI 챗봇 코냥이
- 현재 챕터 · 레슨 컨텍스트 기반 질의응답
- Claude API + RAG
- 학습 중 언제든지 사이드 패널로 호출 가능

### AI 요약 리포트
- 챕터 완료 시 백그라운드에서 자동 생성
- 입력: 정답률, 오답 문제 목록, 힌트 사용 패턴, 정답 공개 여부
- 개인화 피드백 생성
- 출력: 약점 개념, 코냥이 코멘트, 챕터 요약, 핵심 포인트, 다음 챕터 연계, 추천 자료
- A+ ~ D 등급 자동 산출

</br>



<table>
  <tr>
    <td><img width="500" src="https://github.com/user-attachments/assets/a8adbafb-1561-4091-973a-3b5b33ce9def"></td>
    <td><img width="500" src="https://github.com/user-attachments/assets/aedc8c97-92e1-479f-a7de-6903123a766d"></td>
    <td><img width="500" src="https://github.com/user-attachments/assets/e4c7bc90-7aae-42b8-bf31-adf4f806a208"></td>
  </tr>
  <tr>
    <td align="center"><b>홈 화면</b></td>
    <td align="center"><b>학습 트랙 챕터 목록</b></td>
    <td align="center"><b>학습 트랙 화면</b></td>
  </tr>
</table>

<table>
  <tr>
    <td><img width="500" src="https://github.com/user-attachments/assets/38fbf1ac-8c8a-44e5-8a4d-31b69ee0ebc5"></td>
    <td><img width="500" src="https://github.com/user-attachments/assets/e617da3a-0634-4a3c-a96c-2005fd1165ec"></td>
    <td><img width="500" src="https://github.com/user-attachments/assets/3edd62de-a01d-4bb4-92d0-b6d50b96034d"></td>
  </tr>
  <tr>
    <td align="center"><b>요약 리포트</b></td>
    <td align="center"><b>데일리 태스크</b></td>
    <td align="center"><b>오답노트</b></td>
  </tr>
</table>

</br></br>


## 학습 플로우

```
로그인 (Google OAuth)
    │
    ▼
트랙 선택 (ML-분류 / ML-회귀 / CV / NLP)
    │
    ▼
챕터 학습
    ├─ 개념 설명 (이미지, 코드, 인터랙티브 실험)
    ├─ 문제 풀기 (빈칸 채우기 / 객관식)
    │       └─ 오답 → 오답노트 자동 등록
    └─ 챕터 완료 → XP 지급 + AI 리포트 생성
    │
    ▼
전체 챕터 완료 → 미션 잠금 해제
    │
    ▼
종합 미션
    ├─ 빈칸 채우기로 전체 코드 완성
    ├─ Modal GPU에서 실제 실행 (SSE 스트리밍)
    └─ 합격 → XP 지급

데일리 퀴즈 (매일 리셋)
    └─ AI 생성 문제 → 오답노트 연계

오답노트 복습
    └─ 복습 모드 → 순차 풀이 → 최종 채점
```

</br>

## 기술 스택

| 영역 | 기술 |
|---|---|
| Frontend | React 18, React Router v6, Vite |
| Backend | FastAPI, SQLAlchemy, Alembic |
| Database | PostgreSQL |
| AI | Anthropic Claude API |
| GPU 실행 | Modal (T4 GPU, serverless) |
| Vector DB | ChromaDB |
| 인증 | Google OAuth 2.0 + JWT |
| 배포 | Vercel (Frontend), Render (Backend), Docker |

</br>

## 아키텍처

```
[Browser]
    │
    ├─ React SPA (Vite)
    │       ├─ 학습 페이지 (Lesson / Mission)
    │       ├─ 데일리 퀴즈 (DailyTask)
    │       ├─ 오답노트 (WrongNote)
    │       ├─ AI 챗봇 (ChatBot)
    │       └─ 리포트 (Report)
    │
    └─ FastAPI Server
            ├─ /auth          Google OAuth + JWT
            ├─ /tracks        챕터·레슨 조회, 진도 관리
            ├─ /daily         데일리 문제 생성·채점
            ├─ /wrong-answers  오답노트 CRUD + 복습 채점
            ├─ /mission       코드 실행(SSE) + 채점 + 제출
            ├─ /reports       AI 리포트 생성·조회
            └─ /chat          Claude + RAG 챗봇
                    │
                    ├─ PostgreSQL (진도, 문제, 오답, 리포트)
                    ├─ ChromaDB  (강의 자료 벡터)
                    ├─ Anthropic Claude API
                    └─ Modal GPU (미션 코드 실행)
```

</br>

## 팀원 및 역할

| 김승연 (ML) | 김윤서 (CV) | 노은서 (ML) | 박주연 (NLP) |
|:------:|:------:|:------:| :------:|
|`FrontEnd` </b><br> AI 챗봇 </b><br> 오답노트 |`FrontEnd` </b><br> 학습트랙 </b><br> 최종미션 |`BackEnd` </b><br> AI 요약 리포트 </b><br> 학습트랙 | `BackEnd` </b><br> AI 데일리 태스크 </b><br> 오답노트 / 배포 |

</br>

## 디렉토리 구조

```
AI-CO/
├── frontend/
│   ├── src/
│   │   ├── pages/           # 페이지 컴포넌트
│   │   ├── components/      # 공통 컴포넌트, 레슨 렌더러
│   │   └── styles/          # CSS
│   └── public/
│       └── static/md/       # 강의 콘텐츠 
│           ├── cv/
│           ├── regression/
│           ├── nlp/
│           └── ml/
└── backend/
    ├── app/
    │   ├── routers/         # API 엔드포인트
    │   ├── models/          # SQLAlchemy 모델
    │   ├── schemas/         # Pydantic 스키마
    │   └── services/        # 비즈니스 로직 
    ├── modal_runner.py      # Modal GPU 실행 함수
    └── alembic/             # DB 마이그레이션
```
