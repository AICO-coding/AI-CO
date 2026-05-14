export const trackMeta = [
  {
    id: "ml",
    track: "ML",
    emoji: "🤖",
    name: "머신러닝",
    sub: "필수 트랙 · 회귀 + 분류 · 14챕터",
    color: "ml",
    parts: [
      {
        label: "Part 1. 회귀",
        chapters: [
          {
            id: "ml_r1",
            title: "Tensor & Numpy",
            sub: "shape · reshape · matmul 핵심",
            tags: ["빈칸", "퀴즈"],
            xp: 60,
          },
          {
            id: "ml_r2",
            title: "선형 회귀 학습 루프",
            sub: "y = wx + b · MSELoss · optimizer",
            tags: ["빈칸", "파라미터", "퀴즈"],
            xp: 100,
          },
          {
            id: "ml_r3",
            title: "Dataset & DataLoader",
            sub: "train/test split · batch 학습",
            tags: ["빈칸", "파라미터", "퀴즈"],
            xp: 100,
          },
          {
            id: "ml_r4",
            title: "nn.Module로 모델 구조화",
            sub: "단순 → 다중 회귀 확장",
            tags: ["빈칸", "파라미터", "퀴즈"],
            xp: 120,
          },
          {
            id: "ml_r5",
            title: "학습 고도화",
            sub: "train/eval · loss 시각화 · 모델 저장",
            tags: ["빈칸", "파라미터", "퀴즈"],
            xp: 120,
          },
          {
            id: "ml_r_mission",
            title: "🏆 Mission: 캘리포니아 집값 예측",
            sub: "회귀 전 챕터 통합 프로젝트",
            tags: ["실행", "퀴즈"],
            xp: 300,
          },
        ],
      },
      {
        label: "Part 2. 분류",
        chapters: [
          {
            id: "ml_c1",
            title: "분류 문제의 이해",
            sub: "회귀 vs 분류 · Binary vs Multi-class",
            tags: ["퀴즈"],
            xp: 60,
          },
          {
            id: "ml_c2",
            title: "sklearn으로 로지스틱 회귀",
            sub: "fit · predict · predict_proba",
            tags: ["빈칸", "퀴즈"],
            xp: 80,
          },
          {
            id: "ml_c3",
            title: "활성화 함수",
            sub: "Sigmoid · ReLU · Softmax · 언제 어디에",
            tags: ["파라미터", "퀴즈"],
            xp: 100,
          },
          {
            id: "ml_c4",
            title: "Binary Cross Entropy Loss",
            sub: "BCE 수식 · MSE와의 차이 · gradient 관점",
            tags: ["파라미터", "퀴즈"],
            xp: 100,
          },
          {
            id: "ml_c5",
            title: "PyTorch로 분류기 구현",
            sub: "Sigmoid 출력 · BCELoss · train/eval 루프",
            tags: ["빈칸", "파라미터", "퀴즈"],
            xp: 120,
          },
          {
            id: "ml_c6",
            title: "평가지표",
            sub: "Precision · Recall · F1 · Confusion Matrix",
            tags: ["파라미터", "퀴즈"],
            xp: 100,
          },
          {
            id: "ml_c7",
            title: "Bias & Variance",
            sub: "과적합 · 과소적합 · train/val loss 진단",
            tags: ["파라미터", "퀴즈"],
            xp: 120,
          },
          {
            id: "ml_c8",
            title: "Multi-class 분류와 Softmax",
            sub: "Softmax · CrossEntropyLoss · argmax",
            tags: ["빈칸", "파라미터", "퀴즈"],
            xp: 120,
          },
          {
            id: "ml_c_mission",
            title: "🏆 Mission: 타이타닉 생존자 예측",
            sub: "분류 전 챕터 통합 프로젝트 · F1 ≥ 0.78",
            tags: ["실행", "퀴즈"],
            xp: 300,
          },
        ],
      },
    ],
  },
  {
    id: "cv",
    track: "CV",
    emoji: "👁️",
    name: "컴퓨터 비전",
    sub: "이미지 인식과 처리 · 5챕터",
    color: "cv",
    parts: [
      {
        label: "Part 1. CNN 기초",
        chapters: [
          {
            id: "cv_1",
            title: "이미지와 텐서의 이해",
            sub: "픽셀 · RGB · Grayscale · Tensor shape",
            tags: ["퀴즈"],
            xp: 60,
          },
          {
            id: "cv_2",
            title: "이미지 전처리",
            sub: "transforms · Resize · Normalize",
            tags: ["빈칸", "퀴즈"],
            xp: 80,
          },
          {
            id: "cv_3",
            title: "Data Augmentation",
            sub: "RandomFlip · RandomCrop · ColorJitter",
            tags: ["파라미터", "퀴즈"],
            xp: 80,
          },
          {
            id: "cv_4",
            title: "CNN (1) — 합성곱과 구조",
            sub: "convolution · feature map · stride · padding",
            tags: ["빈칸", "파라미터", "퀴즈"],
            xp: 120,
          },
          {
            id: "cv_5",
            title: "CNN (2) — 학습과 평가",
            sub: "optimizer · lr 스케줄 · 모델 평가",
            tags: ["파라미터", "퀴즈"],
            xp: 120,
          },
        ],
      },
    ],
  },
  {
    id: "nlp",
    track: "NLP",
    emoji: "💬",
    name: "자연어 처리",
    sub: "텍스트 이해와 생성 · 7챕터",
    color: "nlp",
    parts: [
      {
        label: "Part 1. NLP 기초",
        chapters: [
          {
            id: "nlp_1",
            title: "NLP 기초 개념",
            sub: "토큰화 · 어휘 구축 · NLP 사례",
            tags: ["빈칸", "퀴즈"],
            xp: 60,
          },
          {
            id: "nlp_2",
            title: "텍스트 표현 — 임베딩",
            sub: "BoW · TF-IDF · Word2Vec",
            tags: ["파라미터", "퀴즈"],
            xp: 80,
          },
          {
            id: "nlp_3",
            title: "시퀀스 모델 — RNN & LSTM",
            sub: "RNN 아이디어 · 기울기 소실 · LSTM 게이트",
            tags: ["빈칸", "파라미터", "퀴즈"],
            xp: 100,
          },
          {
            id: "nlp_4",
            title: "어텐션 메커니즘",
            sub: "LSTM 한계 · 어텐션 가중치 · 시각화",
            tags: ["파라미터", "퀴즈"],
            xp: 120,
          },
          {
            id: "nlp_5",
            title: "트랜스포머",
            sub: "Self-Attention · Multi-Head · Positional Encoding",
            tags: ["빈칸", "파라미터", "퀴즈"],
            xp: 150,
          },
          {
            id: "nlp_6",
            title: "BERT — 양방향 인코더",
            sub: "Masked LM · Fine-tuning · 분류 태스크",
            tags: ["빈칸", "퀴즈"],
            xp: 150,
          },
          {
            id: "nlp_7",
            title: "GPT — 자기회귀 생성",
            sub: "Autoregressive · Prompt · 텍스트 생성",
            tags: ["빈칸", "퀴즈"],
            xp: 150,
          },
        ],
      },
    ],
  },
];

// ─────────────────────────────────────────────────────────────
// 목업 GET /tracks 응답
// 나중에 실제 API 응답과 merge 예정
// ─────────────────────────────────────────────────────────────
export const mockTrackList = {
  tracks: [
    { track: "ML", completionRate: 0, totalXp: 0 },
    { track: "CV", completionRate: 0, totalXp: 0 },
    { track: "NLP", completionRate: 0, totalXp: 0 },
  ],
};

// trackMeta + mockTrackList를 합쳐서 Track.jsx에서 쓸 수 있는 형태로 반환
export function getTrackList() {
  return trackMeta.map((meta) => {
    const stat = mockTrackList.tracks.find((t) => t.track === meta.track) ?? {
      completionRate: 0,
      totalXp: 0,
    };
    return {
      ...meta,
      completionRate: stat.completionRate,
      totalXp: stat.totalXp,
    };
  });
}