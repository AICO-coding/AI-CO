const mockChapterData = {
  ML: {
    track: "ML",
    chapters: [
      { chapter: "ml_r1", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_r2", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_r3", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_r4", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_r5", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_r_mission", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_c1", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_c2", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_c3", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_c4", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_c5", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_c6", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_c7", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_c8", isCompleted: false, xpEarned: 0 },
      { chapter: "ml_c_mission", isCompleted: false, xpEarned: 0 },
    ],
  },
  CV: {
    track: "CV",
    chapters: [
      { chapter: "cv_1", isCompleted: false, xpEarned: 0 },
      { chapter: "cv_2", isCompleted: false, xpEarned: 0 },
      { chapter: "cv_3", isCompleted: false, xpEarned: 0 },
      { chapter: "cv_4", isCompleted: false, xpEarned: 0 },
      { chapter: "cv_5", isCompleted: false, xpEarned: 0 },
    ],
  },
  NLP: {
    track: "NLP",
    chapters: [
      { chapter: "nlp_1", isCompleted: false, xpEarned: 0 },
      { chapter: "nlp_2", isCompleted: false, xpEarned: 0 },
      { chapter: "nlp_3", isCompleted: false, xpEarned: 0 },
      { chapter: "nlp_4", isCompleted: false, xpEarned: 0 },
      { chapter: "nlp_5", isCompleted: false, xpEarned: 0 },
      { chapter: "nlp_6", isCompleted: false, xpEarned: 0 },
      { chapter: "nlp_7", isCompleted: false, xpEarned: 0 },
    ],
  },
};

export function getChapterStatus(track) {
  const data = mockChapterData[track.toUpperCase()];
  if (!data) return {};
  return Object.fromEntries(
    data.chapters.map((c) => [c.chapter, { isCompleted: c.isCompleted, xpEarned: c.xpEarned }])
  );
}

// 파트 내 챕터 id 목록 기준으로 state 계산 (파트별 독립)
// → 각 파트의 첫 챕터는 항상 active
export function calcChapterState(chapterId, partChapterIds, statusMap) {
  const status = statusMap[chapterId];
  if (!status) return "lock";
  if (status.isCompleted) return "done";

  const idx = partChapterIds.indexOf(chapterId);
  if (idx === 0) return "active"; // 파트 첫 챕터는 항상 active

  const prevId = partChapterIds[idx - 1];
  if (statusMap[prevId]?.isCompleted) return "active";

  return "lock";
}

// 챕터 완료 처리 (목업 — 나중에 POST /chapters/complete로 교체)
export function completeChapter(track, chapterId, xpEarned) {
  const data = mockChapterData[track.toUpperCase()];
  if (!data) return;
  const chapter = data.chapters.find((c) => c.chapter === chapterId);
  if (chapter) {
    chapter.isCompleted = true;
    chapter.xpEarned = xpEarned;
  }
}