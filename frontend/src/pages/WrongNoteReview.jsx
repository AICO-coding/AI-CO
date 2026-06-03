import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import "../styles/WrongNote.css";

const API_BASE = "http://210.125.96.59:8000";

function parseJson(value) {
  if (!value || typeof value !== "string") return value;
  try { return JSON.parse(value); } catch { return value; }
}

export default function WrongNoteReview() {
  const { trackId } = useParams();
  const navigate = useNavigate();
  const isDaily = trackId === "daily";

  const [problems, setProblems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [current, setCurrent] = useState(0);
  const [answers, setAnswers] = useState({});
  const [submitting, setSubmitting] = useState(false);
  const [results, setResults] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("accessToken");
    const params = new URLSearchParams();
    if (isDaily) {
      params.set("source_type", "daily");
    } else {
      params.set("source_type", "learning");
      params.set("track", trackId.toUpperCase());
    }

    fetch(`${API_BASE}/wrong-answers/review?${params.toString()}`, {
      headers: token ? { Authorization: `Bearer ${token}` } : {},
    })
      .then((r) => r.json())
      .then((data) => {
        const parsed = (data.wrongAnswers ?? []).map((item) => ({
          ...item,
          problem: item.problem
            ? {
                ...item.problem,
                content: parseJson(item.problem.content),
                answer: parseJson(item.problem.answer),
              }
            : null,
        }));
        setProblems(parsed);
      })
      .catch(() => setProblems([]))
      .finally(() => setLoading(false));
  }, [trackId]);

  function selectAnswer(wrongAnswerId, idx) {
    setAnswers((prev) => ({ ...prev, [wrongAnswerId]: idx + 1 }));
  }

  async function handleSubmit() {
    const token = localStorage.getItem("accessToken");
    const body = {
      answers: problems.map((p) => ({
        wrongAnswerId: p.wrongAnswerId,
        answer: { answer: answers[p.wrongAnswerId] ?? null },
      })),
    };

    setSubmitting(true);
    try {
      const r = await fetch(`${API_BASE}/wrong-answers/review`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...(token ? { Authorization: `Bearer ${token}` } : {}),
        },
        body: JSON.stringify(body),
      });
      const data = await r.json();
      setResults(data);
    } catch {
      // 제출 실패 시 조용히 처리
    } finally {
      setSubmitting(false);
    }
  }

  if (loading) {
    return (
      <div className="page-container">
        <button className="back-btn" onClick={() => navigate(`/wrong-answer/${trackId}`)}>
          &larr; 목록으로
        </button>
        <div className="empty-message">불러오는 중...</div>
      </div>
    );
  }

  if (problems.length === 0) {
    return (
      <div className="page-container">
        <button className="back-btn" onClick={() => navigate(`/wrong-answer/${trackId}`)}>
          &larr; 목록으로
        </button>
        <div className="empty-message">복습할 오답이 없습니다.</div>
      </div>
    );
  }

  if (results) {
    return (
      <div className="page-container">
        <div className="review-result-wrap">
          <div className="review-result-score">
            {results.correctCount} / {results.totalCount}
          </div>
          <div className="review-result-label">정답</div>
          <div className="review-result-list">
            {results.results.map((r, i) => {
              const item = problems.find((p) => p.wrongAnswerId === r.wrongAnswerId);
              return (
                <div
                  key={r.wrongAnswerId}
                  className={`review-result-row ${r.isCorrect ? "correct" : "wrong"}`}
                >
                  <span className="review-result-num">Q{i + 1}</span>
                  <span className="review-result-chapter">
                    {item?.problem?.chapter}
                  </span>
                  <span className="review-result-badge">
                    {r.isCorrect ? "정답" : "오답"}
                  </span>
                </div>
              );
            })}
          </div>
          <button
            className="review-btn"
            onClick={() => navigate(`/wrong-answer/${trackId}`)}
          >
            목록으로
          </button>
        </div>
      </div>
    );
  }

  const item = problems[current];
  const problem = item.problem;
  const choices = problem?.content?.choices ?? [];
  const selected = answers[item.wrongAnswerId];
  const isLast = current === problems.length - 1;

  return (
    <div className="page-container">
      <button className="back-btn" onClick={() => navigate(`/wrong-answer/${trackId}`)}>
        &larr; 목록으로
      </button>

      <div className="review-progress-row">
        <span className="review-progress-text">
          {current + 1} / {problems.length}
        </span>
        <div className="review-progress-bar">
          <div
            className="review-progress-fill"
            style={{ width: `${((current + 1) / problems.length) * 100}%` }}
          />
        </div>
      </div>

      <div className="quiz-wrap">
        <div className="quiz-question">{problem?.content?.question}</div>
        <div className="quiz-choices">
          {choices.map((choice, idx) => (
            <div
              key={idx}
              className={`quiz-choice${selected === idx + 1 ? " quiz-choice-selected" : ""}`}
              onClick={() => selectAnswer(item.wrongAnswerId, idx)}
            >
              <div className="quiz-choice-index">{idx + 1}</div>
              <div className="quiz-choice-text">{choice}</div>
            </div>
          ))}
        </div>
      </div>

      <div className="review-nav">
        <button
          className="back-btn"
          onClick={() => setCurrent((c) => c - 1)}
          style={{ visibility: current > 0 ? "visible" : "hidden" }}
        >
          &larr; 이전
        </button>
        {isLast ? (
          <button
            className="review-btn"
            onClick={handleSubmit}
            disabled={submitting}
          >
            {submitting ? "제출 중..." : "제출"}
          </button>
        ) : (
          <button className="review-btn" onClick={() => setCurrent((c) => c + 1)}>
            다음 &rarr;
          </button>
        )}
      </div>
    </div>
  );
}
