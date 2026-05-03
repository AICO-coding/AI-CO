import { useState } from "react";
import "../styles/Track.css";

const tracks = [
  {
    id: "ml",
    emoji: "🤖",
    name: "머신러닝",
    sub: "필수 트랙 · 6챕터 · 회귀 완전 정복",
    color: "ml",
    progress: 0,
    done: 0,
    total: 6,
    chapters: [
      {
        id: 1,
        title: "Tensor & Numpy",
        sub: "shape · reshape · matmul 핵심",
        tags: ["빈칸", "퀴즈"],
        xp: 60,
        state: "active",
      },
      {
        id: 2,
        title: "선형 회귀 학습 루프",
        sub: "y = wx + b · MSELoss · optimizer",
        tags: ["빈칸", "파라미터", "퀴즈"],
        xp: 100,
        state: "lock",
      },
      {
        id: 3,
        title: "Dataset & DataLoader",
        sub: "train/test split · batch 학습",
        tags: ["빈칸", "파라미터"],
        xp: 100,
        state: "lock",
      },
      {
        id: 4,
        title: "nn.Module 모델 구조화",
        sub: "단순 → 다중 회귀 확장",
        tags: ["빈칸", "퀴즈"],
        xp: 120,
        state: "lock",
      },
      {
        id: 5,
        title: "학습 고도화",
        sub: "train/eval · loss 시각화 · 모델 저장",
        tags: ["빈칸", "파라미터", "퀴즈"],
        xp: 120,
        state: "lock",
      },
      {
        id: 6,
        title: "🏆 Mission: 보스턴 집값 예측",
        sub: "5단계 프로젝트 완성",
        tags: ["실행", "퀴즈"],
        xp: 300,
        state: "lock",
      },
    ],
  },
  {
    id: "cv",
    emoji: "👁️",
    name: "컴퓨터 비전",
    sub: "이미지 인식과 처리 · 10챕터",
    color: "cv",
    progress: 20,
    done: 2,
    total: 10,
    chapters: [
      {
        id: 1,
        title: "이미지 기초",
        sub: "픽셀 · 채널 · 텐서 변환",
        tags: ["빈칸", "퀴즈"],
        xp: 60,
        state: "done",
      },
      {
        id: 2,
        title: "필터와 컨볼루션",
        sub: "커널 · stride · padding",
        tags: ["빈칸", "파라미터"],
        xp: 80,
        state: "done",
      },
      {
        id: 3,
        title: "엣지 검출",
        sub: "Sobel · Canny · Laplacian",
        tags: ["빈칸", "퀴즈"],
        xp: 100,
        state: "active",
      },
      {
        id: 4,
        title: "객체 검출",
        sub: "YOLO · anchor box · NMS",
        tags: ["빈칸", "파라미터", "퀴즈"],
        xp: 120,
        state: "lock",
      },
      {
        id: 5,
        title: "시맨틱 분할",
        sub: "U-Net · FCN · 마스크",
        tags: ["빈칸", "퀴즈"],
        xp: 120,
        state: "lock",
      },
      {
        id: 6,
        title: "GAN 기초",
        sub: "Generator · Discriminator",
        tags: ["빈칸", "파라미터"],
        xp: 150,
        state: "lock",
      },
      {
        id: 7,
        title: "이미지 생성",
        sub: "DCGAN · StyleGAN",
        tags: ["빈칸", "퀴즈"],
        xp: 150,
        state: "lock",
      },
      {
        id: 8,
        title: "스타일 전이",
        sub: "Content loss · Style loss",
        tags: ["빈칸", "파라미터", "퀴즈"],
        xp: 150,
        state: "lock",
      },
      {
        id: 9,
        title: "ViT",
        sub: "Patch embedding · Attention",
        tags: ["빈칸", "퀴즈"],
        xp: 200,
        state: "lock",
      },
      {
        id: 10,
        title: "🏆 Mission: 이미지 분류기",
        sub: "5단계 프로젝트 완성",
        tags: ["실행", "퀴즈"],
        xp: 300,
        state: "lock",
      },
    ],
  },
  {
    id: "nlp",
    emoji: "💬",
    name: "자연어 처리",
    sub: "텍스트 이해와 생성 · 10챕터",
    color: "nlp",
    progress: 0,
    done: 0,
    total: 10,
    chapters: [
      {
        id: 1,
        title: "텍스트 전처리",
        sub: "토큰화 · 정규화 · 임베딩",
        tags: ["빈칸", "퀴즈"],
        xp: 60,
        state: "active",
      },
      {
        id: 2,
        title: "Word2Vec",
        sub: "CBOW · Skip-gram · 유사도",
        tags: ["빈칸", "파라미터"],
        xp: 80,
        state: "lock",
      },
      {
        id: 3,
        title: "RNN과 LSTM",
        sub: "시퀀스 · 게이트 · 기울기 소실",
        tags: ["빈칸", "퀴즈"],
        xp: 100,
        state: "lock",
      },
      {
        id: 4,
        title: "Seq2Seq",
        sub: "인코더 · 디코더 · 번역",
        tags: ["빈칸", "파라미터", "퀴즈"],
        xp: 120,
        state: "lock",
      },
      {
        id: 5,
        title: "어텐션 메커니즘",
        sub: "Query · Key · Value",
        tags: ["빈칸", "퀴즈"],
        xp: 120,
        state: "lock",
      },
      {
        id: 6,
        title: "트랜스포머",
        sub: "Multi-head · Positional encoding",
        tags: ["빈칸", "파라미터"],
        xp: 150,
        state: "lock",
      },
      {
        id: 7,
        title: "BERT",
        sub: "Masked LM · Fine-tuning",
        tags: ["빈칸", "퀴즈"],
        xp: 150,
        state: "lock",
      },
      {
        id: 8,
        title: "GPT",
        sub: "Autoregressive · Prompt",
        tags: ["빈칸", "파라미터", "퀴즈"],
        xp: 150,
        state: "lock",
      },
      {
        id: 9,
        title: "파인튜닝",
        sub: "LoRA · PEFT · 데이터셋",
        tags: ["빈칸", "퀴즈"],
        xp: 200,
        state: "lock",
      },
      {
        id: 10,
        title: "🏆 Mission: 감성 분석기",
        sub: "5단계 프로젝트 완성",
        tags: ["실행", "퀴즈"],
        xp: 300,
        state: "lock",
      },
    ],
  },
];

function Track() {
  const [selected, setSelected] = useState(null);

  if (!selected) {
    return (
      <div className="track-wrap">
        <div className="track-page-title">📚 학습 트랙</div>
        <div className="track-page-sub">학습할 트랙을 선택해주세요!</div>

        <div className="track-page-grid">
          {tracks.map((track) => (
            <div
              key={track.id}
              className={`track-page-card tc-${track.color}`}
              onClick={() => setSelected(track)}
            >
              <span className="tc-emoji">{track.emoji}</span>
              <div className="tc-name">{track.name}</div>
              <div className="tc-sub">{track.sub}</div>
              <div className="tc-prog-wrap">
                <div
                  className={`tc-prog tc-prog-${track.color}`}
                  style={{ width: `${track.progress}%` }}
                ></div>
              </div>
              <div className="tc-info">
                {track.progress === 0
                  ? "아직 시작 전이에요!"
                  : `${track.progress}% 완료 · ${track.done}/${track.total} 챕터`}
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="track-wrap">
      <button className="track-back" onClick={() => setSelected(null)}>
        ← 트랙 목록으로
      </button>

      <div className="chap-header">
        <div className="chap-header-top">
          <span className="chap-h-emoji">{selected.emoji}</span>
          <div>
            <div className="chap-h-name">{selected.name}</div>
            <div className="chap-h-sub">{selected.sub}</div>
          </div>
        </div>
        <div className="chap-h-prog">
          <div className="chap-h-bar">
            <div
              className={`chap-h-fill fill-${selected.color}`}
              style={{ width: `${selected.progress}%` }}
            ></div>
          </div>
          <div className={`chap-h-pct pct-${selected.color}`}>
            {selected.progress}%
          </div>
        </div>
      </div>

      <div className="chap-list">
        {selected.chapters.map((chap) => (
          <div key={chap.id} className={`chap-item chap-${chap.state}`}>

            <div className={`chap-num-badge num-${chap.state}`}>
              {chap.state === "done" ? "✓" : chap.state === "active" ? chap.id : "🔒"}
            </div>

            <div className="chap-content">
              <div className="chap-title">{chap.title}</div>
              <div className="chap-sub">{chap.sub}</div>
              <div className="chap-tags">
                {chap.tags.map((tag) => (
                  <span key={tag} className="chap-tag">{tag}</span>
                ))}
              </div>
            </div>

            <div className="chap-right">
              <div className={`chap-xp xp-${selected.color}`}>+{chap.xp} XP</div>
              {chap.state !== "lock" && (
                <div className="chap-arrow">→</div>
              )}
            </div>

          </div>
        ))}
      </div>
    </div>
  );
}

export default Track;