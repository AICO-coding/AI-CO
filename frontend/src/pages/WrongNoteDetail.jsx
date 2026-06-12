import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import WrongNoteMultipleChoice from '../components/lesson/WrongNoteMultipleChoice';
import WrongNoteCodeFill from '../components/lesson/WrongNoteCodeFill';
import '../styles/WrongNote.css';

const API_BASE = 'http://210.125.96.59:8000';

function parseJson(value) {
  if (!value || typeof value !== 'string') return value;
  try {
    return JSON.parse(value);
  } catch {
    return value;
  }
}

export default function WrongNoteDetail() {
  const { trackId, wrongAnswerId } = useParams();
  const navigate = useNavigate();

  const [detail, setDetail] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    fetch(`${API_BASE}/wrong-answers/${wrongAnswerId}`, {
      headers: token ? { Authorization: `Bearer ${token}` } : {},
    })
      .then((r) => r.json())
      .then((data) => {
        const parsed = {
          ...data,
          userAnswer: parseJson(data.userAnswer),
          correctAnswer: parseJson(data.correctAnswer),
          problem: data.problem
            ? {
                ...data.problem,
                content: parseJson(data.problem.content),
                answer: parseJson(data.problem.answer),
                hints: parseJson(data.problem.hints),
              }
            : null,
        };
        console.log('[WrongNoteDetail]', parsed);
        setDetail(parsed);
      })
      .catch(() => setDetail(null))
      .finally(() => setLoading(false));
  }, [wrongAnswerId]);

  if (loading) return null;

  if (!detail || !detail.problem) {
    return (
      <div className="page-container">
        <button
          className="back-btn"
          onClick={() => navigate(`/wrong-answer/${trackId}`)}
        >
          목록으로
        </button>
        <div className="empty-message">오답 상세 정보를 찾을 수 없습니다.</div>
      </div>
    );
  }

  const problem = detail.problem;

  return (
    <div className="page-container">
      <button
        className="back-btn"
        onClick={() => navigate(`/wrong-answer/${trackId}`)}
      >
        목록으로
      </button>

      <div className="detail-meta-group">
        <div className="detail-meta-left">
          <span className="track-badge">{problem.track}</span>
          <span className="detail-meta-sep">·</span>
          <span className="detail-meta-chapter">{problem.chapter}</span>
        </div>
        <span className={detail.isResolved ? 'wn-status-dot resolved' : 'wn-status-dot unresolved'}>
          {detail.isResolved ? '해결완료' : '미해결'}
        </span>
      </div>

      {problem.problemType === 'code_fill' ? (
        <WrongNoteCodeFill detail={detail} />
      ) : (
        <WrongNoteMultipleChoice detail={detail} />
      )}
    </div>
  );
}
