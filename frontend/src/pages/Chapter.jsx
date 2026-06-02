import { useNavigate, useParams } from "react-router-dom";
import { useEffect, useState } from "react";

import "../styles/Chapter.css";

export default function Chapter() {
  const navigate = useNavigate();
  const { trackId } = useParams();

  const [chapterData, setChapterData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchChapters = async () => {
  try {
    const token = localStorage.getItem("accessToken");
    const normalizedTrackId = trackId?.toLowerCase();

    const url = `http://210.125.96.59:8000/tracks/${normalizedTrackId.toUpperCase()}/chapters`;

    console.log("🚀 API REQUEST URL:", url);

    const res = await fetch(url, {
      headers: {
        ...(token && {
          Authorization: `Bearer ${token}`,
        }),
      },
    });

    console.log("📡 STATUS:", res.status);
    console.log("📡 OK?:", res.ok);

    const raw = await res.text();

    console.log("📦 RAW RESPONSE:");
    console.log(raw);

    if (!res.ok) {
      throw new Error(`HTTP ${res.status}`);
    }

    const data = JSON.parse(raw);

    console.log("✅ PARSED JSON:");
    console.log(data);

    console.log("📊 CHAPTER LIST:");
    console.table(data.chapters);

    setChapterData(data);
  } catch (err) {
    console.error("❌ FETCH ERROR:", err);
    setError(err.message);
  }
};

    if (trackId) fetchChapters();
  }, [trackId]);

  if (error) {
    return (
      <div className="chapter-wrap">
        <p>❌ {error}</p>
        <button onClick={() => (window.location.href = "/login")}>
          로그인
        </button>
      </div>
    );
  }

  if (!chapterData) return null;

  // 진행률
  const progress =
    chapterData.chapters.length
      ? Math.round(
          (chapterData.chapters.filter((c) => c.isCompleted).length /
            chapterData.chapters.length) *
            100
        )
      : 0;

  return (
    <div className="chapter-wrap">
      <div className="chapter-hero">
        <div className="chapter-hero-left">
          <div className="chapter-hero-eyebrow">
            📚 {chapterData.track}
          </div>

          <div className="chapter-hero-progress">
            <div className="chapter-progress-bar">
              <div
                className="chapter-progress-fill"
                style={{ width: `${progress}%` }}
              />
            </div>

            <div className="chapter-progress-text">
              {progress}% 완료
            </div>
          </div>
        </div>
      </div>

      <div className="chapter-list">
        {chapterData.chapters.map((chapter, idx) => {
          const locked = chapter.isLocked;
          const done = chapter.isCompleted;

          return (
            <div
              key={`${chapter.chapter}-${idx}`}
              className={`chapter-row ${locked ? "locked" : ""}`}
            >
            
              <div className="chapter-left">
                <div className={`chapter-checkbox ${done ? "done" : ""}`}>
                  {done ? "✓" : ""}
                </div>
              </div>

              
              <div className="chapter-center">
                <div className="chapter-name">
                  {chapter.chapter}.
                </div>
                <div className="chapter-title">
                   {chapter.title}
                </div>

                <div className="chapter-subtext">
                  {done ? "완료된 챕터" : "진행 가능한 챕터"}
                </div>
              </div>

              
              <div className="chapter-right">
                {!locked && (
                  <button
                    className="chapter-btn"
                    onClick={(e) => {
                      e.stopPropagation();

                      
                      navigate(
                        `/tracks/${trackId}/chapters/${encodeURIComponent(
                          chapter.chapter
                        )}/lessons`
                      );
                    }}
                  >
                    학습하기
                  </button>
                )}

                {locked && (
                  <span className="chapter-lock-text">
                    🔒 잠김
                  </span>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}