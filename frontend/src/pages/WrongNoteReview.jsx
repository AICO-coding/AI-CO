import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import '../styles/WrongNote.css';
import '../styles/CodeFill.css';
import { API_BASE_URL } from '../config/api';

const API_BASE = API_BASE_URL;

function parseJson(value) {
  if (!value || typeof value !== 'string') return value;
  try {
    return JSON.parse(value);
  } catch {
    return value;
  }
}

export default function WrongNoteReview() {
  const { trackId } = useParams();
  const navigate = useNavigate();
  const isDaily = trackId === 'daily';

  const [problems, setProblems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [current, setCurrent] = useState(0);
  const [answers, setAnswers] = useState({});
  const [submitting, setSubmitting] = useState(false);
  const [results, setResults] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    const params = new URLSearchParams();
    if (isDaily) {
      params.set('source_type', 'daily');
    } else {
      params.set('source_type', 'learning');
      params.set('track', trackId.toUpperCase());
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

  function setCodeFillAnswer(wrongAnswerId, key, value) {
    setAnswers((prev) => ({
      ...prev,
      [wrongAnswerId]: {
        ...(prev[wrongAnswerId] && typeof prev[wrongAnswerId] === 'object'
          ? prev[wrongAnswerId]
          : {}),
        [key]: value,
      },
    }));
  }

  async function handleSubmit() {
    const token = localStorage.getItem('accessToken');
    const body = {
      answers: problems.map((p) => {
        const isCodeFill = p.problem?.problemType === 'code_fill';
        const answer = answers[p.wrongAnswerId];
        return {
          wrongAnswerId: p.wrongAnswerId,
          answer: isCodeFill ? (answer ?? {}) : { answer: answer ?? null },
        };
      }),
    };

    setSubmitting(true);
    try {
      const r = await fetch(`${API_BASE}/wrong-answers/review`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(token ? { Authorization: `Bearer ${token}` } : {}),
        },
        body: JSON.stringify(body),
      });
      const data = await r.json();
      setResults(data);
    } catch {
    } finally {
      setSubmitting(false);
    }
  }

  if (loading) return null;

  if (problems.length === 0) {
    return (
      <div className="page-container">
        <button
          className="back-btn"
          onClick={() => navigate(`/wrong-answer/${trackId}`)}
        >
          목록으로
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
              const item = problems.find(
                (p) => p.wrongAnswerId === r.wrongAnswerId,
              );
              return (
                <div
                  key={r.wrongAnswerId}
                  className={`review-result-row ${r.isCorrect ? 'correct' : 'wrong'}`}
                >
                  <span className="review-result-num">Q{i + 1}</span>
                  <span className="review-result-chapter">
                    {item?.problem?.chapter}
                  </span>
                  <span className="review-result-badge">
                    {r.isCorrect ? '정답' : '오답'}
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
  const isCodeFill = problem?.problemType === 'code_fill';
  const isLast = current === problems.length - 1;

  const meta = isDaily && (item.problem?.track || item.problem?.chapter) && (
    <div className="review-problem-meta">
      {item.problem?.track && (
        <span className="track-badge">{item.problem.track}</span>
      )}
      {item.problem?.chapter && (
        <span className="chapter-badge">{item.problem.chapter}</span>
      )}
    </div>
  );

  return (
    <div className="page-container">
      <button
        className="back-btn"
        onClick={() => navigate(`/wrong-answer/${trackId}`)}
      >
        목록으로
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

      {isCodeFill ? (
        <div className="quiz-wrap" style={{ overflow: 'auto' }}>
          {meta}
          <div className="code-editor" style={{ borderRadius: 18 }}>
            <div className="code-editor-header">
              <div className="dots">
                <span />
                <span />
                <span />
              </div>
              <div className="code-editor-title">practice.py</div>
            </div>
            <div className="code-editor-body">
              <div className="codefill-code">
                {(problem?.content?.template ?? '').split(/({{.*?}})/g).map((part, idx) => {
                  const match = part.match(/{{(.*?)}}/);
                  if (!match) return <span key={idx}>{part}</span>;
                  const key = match[1];
                  const val =
                    answers[item.wrongAnswerId] &&
                    typeof answers[item.wrongAnswerId] === 'object'
                      ? (answers[item.wrongAnswerId][key] ?? '')
                      : '';
                  return (
                    <input
                      key={`${key}-${idx}`}
                      className="codefill-blank"
                      value={val}
                      onChange={(e) =>
                        setCodeFillAnswer(item.wrongAnswerId, key, e.target.value)
                      }
                      placeholder={key}
                    />
                  );
                })}
              </div>
            </div>
          </div>
        </div>
      ) : (
        <div className="quiz-wrap">
          {meta}
          <div className="quiz-question">{problem?.content?.question}</div>
          <div className="quiz-choices">
            {(problem?.content?.choices ?? []).map((choice, idx) => (
              <div
                key={idx}
                className={`quiz-choice${answers[item.wrongAnswerId] === idx + 1 ? ' quiz-choice-selected' : ''}`}
                onClick={() => selectAnswer(item.wrongAnswerId, idx)}
              >
                <div className="quiz-choice-index">{idx + 1}</div>
                <div className="quiz-choice-text">{choice}</div>
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="review-nav">
        <button
          className="back-btn"
          onClick={() => setCurrent((c) => c - 1)}
          style={{ visibility: current > 0 ? 'visible' : 'hidden' }}
        >
          &larr; 이전
        </button>
        {isLast ? (
          <button
            className="review-btn"
            onClick={handleSubmit}
            disabled={submitting}
          >
            {submitting ? '제출 중...' : '제출'}
          </button>
        ) : (
          <button
            className="review-btn"
            onClick={() => setCurrent((c) => c + 1)}
          >
            다음
          </button>
        )}
      </div>
    </div>
  );
}
