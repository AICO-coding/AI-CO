import { useState } from "react";
import { getLessonData } from "../mockup/lessonData";
import { completeChapter } from "../mockup/chapterData";
import "../styles/ChapterLearn.css";

// ─────────────────────────────────────────────────
// 텍스트 블록
// ─────────────────────────────────────────────────
function LessonText({ lesson }) {
  const { text, examples } = lesson.content;
  return (
    <div className="lesson-block lesson-text">
      <div className="lesson-title">{lesson.title}</div>
      <p className="lesson-body">{text}</p>
      {examples && examples.length > 0 && (
        <div className="lesson-examples">
          {examples.map((ex, i) => (
            <div key={i} className="lesson-example-row">
              <span className="ex-label">{ex.label}</span>
              <span className="ex-value">{ex.value}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

// ─────────────────────────────────────────────────
// 객관식 퀴즈 블록
// ─────────────────────────────────────────────────
function LessonQuiz({ lesson, onSubmit, onNext, isLast }) {
  const { problem } = lesson;
  const { question, options } = problem.content;

  const [selected, setSelected] = useState(null);
  const [submitted, setSubmitted] = useState(false);
  const [isCorrect, setIsCorrect] = useState(null);
  const [hintIndex, setHintIndex] = useState(-1);
  const [xpDeducted, setXpDeducted] = useState(0);

  const handleSubmit = () => {
    if (selected === null) return;
    const correct = selected === 1; // 목업: 실제 API 연동 시 서버 채점으로 교체
    setIsCorrect(correct);
    setSubmitted(true);
    onSubmit?.({ problemId: problem.problemId, isCorrect: correct });
  };

  const handleHint = () => {
    const next = hintIndex + 1;
    if (next < problem.hints.length) {
      setHintIndex(next);
      setXpDeducted((prev) => prev + 10);
    }
  };

  return (
    <div className="lesson-block lesson-quiz">
      <div className="quiz-badge">🧩 확인 문제</div>
      <div className="lesson-title">{question}</div>

      <div className="quiz-options">
        {options.map((opt, idx) => (
          <button
            key={idx}
            className={[
              "quiz-opt",
              selected === idx ? "selected" : "",
              submitted && selected === idx && isCorrect ? "correct" : "",
              submitted && selected === idx && !isCorrect ? "wrong" : "",
            ].join(" ")}
            onClick={() => !submitted && setSelected(idx)}
          >
            <span className="opt-idx">{idx + 1}</span>
            {opt}
          </button>
        ))}
      </div>

      {hintIndex >= 0 && (
        <div className="hint-box">
          {problem.hints.slice(0, hintIndex + 1).map((h, i) => (
            <div key={i} className="hint-row">
              <span className="hint-label">💡 힌트 {i + 1}</span>
              <span>{h}</span>
            </div>
          ))}
          {xpDeducted > 0 && <div className="hint-xp">-{xpDeducted} XP 차감</div>}
        </div>
      )}

      {submitted && (
        <div className={`quiz-result ${isCorrect ? "result-ok" : "result-no"}`}>
          {isCorrect ? "✅ 정답!" : "❌ 오답! 다시 생각해보세요."}
        </div>
      )}

      <div className="quiz-actions">
        {!submitted && hintIndex < problem.hints.length - 1 && (
          <button className="btn-hint" onClick={handleHint}>💡 힌트 (-10 XP)</button>
        )}
        {!submitted && (
          <button className="btn-submit" onClick={handleSubmit} disabled={selected === null}>
            제출
          </button>
        )}
        {submitted && (
          <button className="btn-next" onClick={onNext}>
            {isLast ? "챕터 완료 →" : "다음 →"}
          </button>
        )}
      </div>
    </div>
  );
}

// ─────────────────────────────────────────────────
// 코드 빈칸 채우기 블록 (좌우 분할)
// ─────────────────────────────────────────────────
function LessonCodeFill({ lesson, onSubmit, onNext, isLast }) {
  const { problem } = lesson;
  const { question, code_template, blank_count } = problem.content;

  const [answers, setAnswers] = useState(Array(blank_count).fill(""));
  const [submitted, setSubmitted] = useState(false);
  const [isCorrect, setIsCorrect] = useState(null);
  const [hintIndex, setHintIndex] = useState(-1);
  const [xpDeducted, setXpDeducted] = useState(0);

  const renderCode = () => {
    let blankCount = 0;
    const parts = code_template.split("__blank__");
    return parts.map((part, i) => {
      const elements = [<span key={`t${i}`} className="code-text">{part}</span>];
      if (i < parts.length - 1) {
        const idx = blankCount++;
        elements.push(
          <input
            key={`inp${idx}`}
            className={[
              "code-input",
              submitted && isCorrect ? "input-correct" : "",
              submitted && !isCorrect ? "input-wrong" : "",
            ].join(" ")}
            value={answers[idx]}
            onChange={(e) => {
              const next = [...answers];
              next[idx] = e.target.value;
              setAnswers(next);
            }}
            disabled={submitted}
            placeholder="?"
            style={{ width: `${Math.max(answers[idx].length * 9, 60)}px` }}
          />
        );
      }
      return elements;
    });
  };

  const handleSubmit = () => {
    if (answers.some((a) => !a.trim())) return;
    const correct = true; // 목업: 실제 API 연동 시 POST /submit으로 교체
    setIsCorrect(correct);
    setSubmitted(true);
    onSubmit?.({ problemId: problem.problemId, isCorrect: correct });
  };

  const handleHint = () => {
    const next = hintIndex + 1;
    if (next < problem.hints.length) {
      setHintIndex(next);
      setXpDeducted((prev) => prev + 10);
    }
  };

  return (
    <div className="lesson-block lesson-codefill">
      <div className="quiz-badge">💻 코드 빈칸 채우기</div>
      <div className="codefill-split">
        {/* 왼쪽: 문제 설명 */}
        <div className="codefill-left">
          <div className="lesson-title">{lesson.title}</div>
          <p className="lesson-body">{question}</p>

          {hintIndex >= 0 && (
            <div className="hint-box">
              {problem.hints.slice(0, hintIndex + 1).map((h, i) => (
                <div key={i} className="hint-row">
                  <span className="hint-label">💡 힌트 {i + 1}</span>
                  <span>{h}</span>
                </div>
              ))}
              {xpDeducted > 0 && <div className="hint-xp">-{xpDeducted} XP 차감</div>}
            </div>
          )}

          {submitted && (
            <div className={`quiz-result ${isCorrect ? "result-ok" : "result-no"}`}>
              {isCorrect ? "✅ 정답!" : "❌ 다시 시도해보세요."}
            </div>
          )}

          <div className="quiz-actions">
            {!submitted && hintIndex < problem.hints.length - 1 && (
              <button className="btn-hint" onClick={handleHint}>💡 힌트 (-10 XP)</button>
            )}
            {!submitted && (
              <button
                className="btn-submit"
                onClick={handleSubmit}
                disabled={answers.some((a) => !a.trim())}
              >
                제출
              </button>
            )}
            {submitted && (
              <button className="btn-next" onClick={onNext}>
                {isLast ? "챕터 완료 →" : "다음 →"}
              </button>
            )}
          </div>
        </div>

        {/* 오른쪽: 코드 에디터 */}
        <div className="codefill-right">
          <div className="code-editor-bar">
            <span className="editor-dot red" />
            <span className="editor-dot yellow" />
            <span className="editor-dot green" />
            <span className="editor-filename">solution.py</span>
          </div>
          <pre className="code-editor">{renderCode()}</pre>
        </div>
      </div>
    </div>
  );
}

// ─────────────────────────────────────────────────
// contentType에 따라 블록 분기
// ─────────────────────────────────────────────────
function LessonBlock({ lesson, onSubmit, onNext, isLast }) {
  if (lesson.contentType === "text") return <LessonText lesson={lesson} />;
  if (lesson.contentType === "problem") {
    if (lesson.problem.problemType === "code_fill") {
      return <LessonCodeFill lesson={lesson} onSubmit={onSubmit} onNext={onNext} isLast={isLast} />;
    }
    return <LessonQuiz lesson={lesson} onSubmit={onSubmit} onNext={onNext} isLast={isLast} />;
  }
  return null;
}

// ─────────────────────────────────────────────────
// 메인
// ─────────────────────────────────────────────────
export default function ChapterLearn({ track, chapterId, chapterTitle, onBack }) {
  const data = getLessonData(track, chapterId);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [results, setResults] = useState([]);

  if (!data) {
    return (
      <div className="cl-wrap">
        <button className="cl-back" onClick={onBack}>← 트랙으로</button>
        <div className="cl-empty">🚧 준비 중인 챕터입니다.</div>
      </div>
    );
  }

  const lessons = [...data.lessons].sort((a, b) => a.orderIndex - b.orderIndex);
  const total = lessons.length;
  const current = lessons[currentIndex];
  const isLast = currentIndex === total - 1;
  const progress = Math.round(((currentIndex + 1) / total) * 100);

  const handleSubmit = (result) => setResults((prev) => [...prev, result]);

  const handleNext = () => {
    if (isLast) {
      // 챕터 완료 처리 (목업 — 나중에 POST /chapters/complete로 교체)
      completeChapter(track, chapterId, data.lessons.length * 20);
      onBack();
    } else {
      setCurrentIndex((prev) => prev + 1);
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
  };

  // 텍스트 블록은 제출 없이 바로 다음으로 넘어가는 버튼
  const isTextBlock = current.contentType === "text";

  return (
    <div className="cl-wrap">
      {/* 상단 바 */}
      <div className="cl-topbar">
        <button className="cl-back" onClick={onBack}>← 트랙으로</button>
        <div className="cl-page-indicator">{currentIndex + 1} / {total}</div>
      </div>

      {/* 진행 바 */}
      <div className="cl-progressbar">
        <div className="cl-progressbar-fill" style={{ width: `${progress}%` }} />
      </div>

      {/* 챕터 헤더 */}
      <div className="cl-header">
        <div className="cl-chapter-num">{data.track} · {chapterTitle}</div>
      </div>

      {/* 현재 lesson 렌더링 */}
      <LessonBlock
        key={current.lessonId}
        lesson={current}
        onSubmit={handleSubmit}
        onNext={handleNext}
        isLast={isLast}
      />

      {/* 텍스트 블록일 때만 다음 버튼 */}
      {isTextBlock && (
        <button className="cl-next-btn" onClick={handleNext}>
          {isLast ? "챕터 완료 →" : "다음 →"}
        </button>
      )}
    </div>
  );
}