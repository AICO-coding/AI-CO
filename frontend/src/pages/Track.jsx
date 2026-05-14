import { useState, useEffect } from "react";
import "../styles/Track.css";
import ChapterLearn from "./ChapterLearn";
import { getTrackList } from "../mockup/trackData";
import { getChapterStatus, calcChapterState } from "../mockup/chapterData";

function Track() {
  const [tracks, setTracks] = useState([]);
  const [selected, setSelected] = useState(null);        // 선택된 트랙
  const [chapterMap, setChapterMap] = useState({});      // { chapterId: { isCompleted, xpEarned } }
  const [activeChapter, setActiveChapter] = useState(null); // { id, title }

  // 트랙 목록 로드 (목업 → 나중에 GET /tracks)
  useEffect(() => {
    setTracks(getTrackList());
  }, []);

  // 트랙 선택 시 챕터 상태 로드 (목업 → 나중에 GET /chapters?track=ML)
  useEffect(() => {
    if (!selected) return;
    const status = getChapterStatus(selected.track);
    setChapterMap(status);
  }, [selected]);

  // 트랙의 전체 챕터 id 목록 (순서대로)
  const getAllChapterIds = (track) =>
    track.parts.flatMap((p) => p.chapters.map((c) => c.id));

  // 챕터에 state 붙여서 반환 — 파트별로 독립 계산
  const withState = (track) => {
    return {
      ...track,
      parts: track.parts.map((part) => {
        const partChapterIds = part.chapters.map((c) => c.id); // 파트 내 id만
        return {
          ...part,
          chapters: part.chapters.map((chap) => ({
            ...chap,
            state: calcChapterState(chap.id, partChapterIds, chapterMap),
            xpEarned: chapterMap[chap.id]?.xpEarned ?? 0,
          })),
        };
      }),
    };
  };

  // ── 챕터 학습 화면 ──
  if (activeChapter) {
    return (
      <ChapterLearn
        track={selected.track}
        chapterId={activeChapter.id}
        chapterTitle={activeChapter.title}
        onBack={() => {
          // 돌아올 때 챕터 상태 새로 로드
          const status = getChapterStatus(selected.track);
          setChapterMap(status);
          setActiveChapter(null);
        }}
      />
    );
  }

  // ── 트랙 목록 ──
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
                  style={{ width: `${track.completionRate}%` }}
                ></div>
              </div>
              <div className="tc-info">
                {track.completionRate === 0
                  ? "아직 시작 전이에요!"
                  : `${track.completionRate}% 완료 · ${track.totalXp} XP`}
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  // ── 챕터 목록 ──
  const trackWithState = withState(selected);
  const totalChapters = getAllChapterIds(selected).length;
  const doneCount = Object.values(chapterMap).filter((s) => s.isCompleted).length;

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
              style={{ width: `${selected.completionRate}%` }}
            ></div>
          </div>
          <div className={`chap-h-pct pct-${selected.color}`}>
            {doneCount}/{totalChapters}
          </div>
        </div>
      </div>

      <div className="chap-list">
        {trackWithState.parts.map((part) => (
          <div key={part.label}>
            <div className="chap-part-label">{part.label}</div>
            {part.chapters.map((chap, idx) => (
              <div
                key={chap.id}
                className={`chap-item chap-${chap.state}`}
                onClick={() => {
                  if (chap.state !== "lock") {
                    setActiveChapter({ id: chap.id, title: chap.title });
                  }
                }}
              >
                <div className={`chap-num-badge num-${chap.state}`}>
                  {chap.state === "done" ? "✓" : chap.state === "active" ? idx + 1 : "🔒"}
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
                  <div className={`chap-xp xp-${selected.color}`}>
                    {chap.state === "done" ? `+${chap.xpEarned} XP` : `+${chap.xp} XP`}
                  </div>
                  {chap.state !== "lock" && (
                    <div className="chap-arrow">→</div>
                  )}
                </div>
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Track;