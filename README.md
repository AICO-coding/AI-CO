# AI-CO — AI 코딩 학습 플랫폼

> **AI-CO**는 딥러닝·머신러닝을 단계별로 학습할 수 있는 인터랙티브 교육 플랫폼입니다.  
> 빈칸 채우기, 객관식 문제, 인터랙티브 실험, 챕터 미션, 일일 퀴즈, 오답노트, AI 리포트를 통해 완결된 학습 사이클을 제공합니다.

---

## 기술 스택

| 영역 | 기술 |
|---|---|
| Frontend | React 18, React Router v6, Vite |
| Backend | FastAPI, SQLAlchemy, Alembic |
| Database | PostgreSQL |
| AI | Anthropic Claude API (Haiku 4.5, Sonnet 4.6) |
| GPU 실행 | Modal (T4 GPU, serverless) |
| Vector DB | ChromaDB |
| 인증 | Google OAuth 2.0 + JWT |
| 배포 | Vercel (Frontend), 자체 서버 (Backend), Docker |

---

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
- 힌트(단계별) / 정답 공개 기능
- 챕터 완료 후 AI 요약 리포트 자동 생성

### 미션 (종합 평가)
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

### AI 챗봇 (코냥이)
- 현재 챕터 · 레슨 컨텍스트 기반 질의응답
- Claude API + RAG
- 학습 중 언제든지 사이드 패널로 호출 가능

### AI 요약 리포트
- 챕터 완료 시 백그라운드에서 자동 생성
- 입력: 정답률, 오답 문제 목록, 힌트 사용 패턴, 정답 공개 여부
- 개인화 피드백 생성
- 출력: 약점 개념, 코냥이 코멘트, 챕터 요약, 핵심 포인트, 다음 챕터 연계, 추천 자료
- A+ ~ D 등급 자동 산출

---

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

---

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

---

## 팀원 및 역할

### 박주연 (Zuyeonn) — Backend / 데일리 태스크

- 프로젝트 초기 세팅 (PostgreSQL 연결, 모델, Alembic 마이그레이션)
- Google OAuth 인증 시스템 및 JWT 구현
- 오답노트 API (CRUD, 데일리 연동, 트랙·챕터 분류)
- 데일리 퀴즈 API (문제 저장, 채점, KST 기준 날짜 처리)
- **Claude API로 데일리 문제 자동 생성** (프롬프트 엔지니어링)
- **AI 요약 리포트 생성** (Claude Haiku, 학습 데이터 기반 개인화 피드백)
- **ChromaDB 벡터 DB 구축** (강의 자료 임베딩, 임베딩 모델 교체)
- **Dockerfile 작성 및 배포 환경 구성**
- NLP 트랙 전체 강의 콘텐츠 제작
- 트랙 정규화, 챕터 완료 처리 로직, XP 시스템 설계

---

### 김윤서 (Kim-Yun-Seo) — Frontend 

- **Google 로그인 프론트엔드 구현**, 닉네임 설정 기능
- **데일리 퀴즈 페이지** 구현 (문제 렌더링, 채점, 결과 표시)
- **오답노트 전체 UI** (트랙별 목록, 날짜 캘린더, 복습 모드, 상세 보기)
- **미션 페이지 전체 개발**
  - 빈칸 채우기 에디터 (동적 너비, 블랭크 카운터)
  - SSE 스트리밍 (실시간 GPU 실행 로그, 에폭별 순차 출력)
  - 수직 / 수평 리사이저, 힌트 시스템, 성공 모달
  - 제출 → 채점 → XP 지급 연동
- **Parameter 레슨 타입** 구현 (마크다운 + 인터랙티브 HTML iframe)
- CodeFill 코드 에디터 UI, 스크롤 버그 수정
- CV 트랙 강의 콘텐츠 제작
- 홈, 리포트, WrongNote 스타일 개선

---

### 노은서 (RohEunSeo) — Backend API / 요약 리포트

- **Google OAuth 로그인 인증 시스템 구현**
- 레슨 조회 API 및 DB 스키마 설계 (Lesson, Progress 모델)
- **Progress API 설계** (학습 진도 조회, 트랙 API로 통합)
- **레슨 완료 + 답안 제출 API** (정답 비교, 오답 등록 연동)
- **힌트 / 정답공개 / 챕터 완료 API** 구현
- **미션 제출 API** 구현
- ML-회귀 트랙 강의 콘텐츠 제작
- 리포트 모델 Claude Haiku 교체

---

### 김승연 (seungyeonkim24) — Frontend UI / 챗봇

- **학습 트랙 목록 페이지** 구현 (Sidebar 레이아웃 포함)
- Sidebar, assets 초기 세팅
- **AI 챗봇 프론트엔드 UI** 구현 (사이드 패널)
- **챗봇 백엔드 구현** (Claude API + ChromaDB RAG 연동)
- DailyTask 메시지 카드 UI
- 오답노트 code_fill 유형 지원 (복습 에디터)
- ML 트랙 강의 콘텐츠 제작
- 데일리 태스크 홈 버튼, 오답노트 카드 UI 개선

---

## 디렉토리 구조

```
AI-CO/
├── frontend/
│   ├── src/
│   │   ├── pages/           # 페이지 컴포넌트
│   │   ├── components/      # 공통 컴포넌트, 레슨 렌더러
│   │   └── styles/          # CSS
│   └── public/
│       └── static/md/       # 강의 콘텐츠 (마크다운, JSON, HTML)
│           ├── cv/
│           ├── regression/
│           ├── nlp/
│           └── ml/
└── backend/
    ├── app/
    │   ├── routers/         # API 엔드포인트
    │   ├── models/          # SQLAlchemy 모델
    │   ├── schemas/         # Pydantic 스키마
    │   └── services/        # 비즈니스 로직 (report, chatbot)
    ├── modal_runner.py      # Modal GPU 실행 함수
    └── alembic/             # DB 마이그레이션
```
