import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/WrongNote.css';
import { API_BASE_URL } from '../config/api';

const API_BASE = API_BASE_URL;
const TRACKS = ['ML-분류', 'ML-회귀', 'CV', 'NLP'];

function getTrackIcon(track) {
  if (track === 'ML-분류') return '📊';
  if (track === 'ML-회귀') return '📈';
  if (track === 'CV') return '👁';
  if (track === 'NLP') return '💬';
  return '📝';
}

export default function WrongNotePage() {
  const navigate = useNavigate();
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    fetch(`${API_BASE}/wrong-answers`, {
      headers: token ? { Authorization: `Bearer ${token}` } : {},
    })
      .then((r) => r.json())
      .then((data) => setItems(data.wrongAnswers ?? []))
      .catch(() => setItems([]))
      .finally(() => setLoading(false));
  }, []);

  const learningItems = items.filter((i) => i.sourceType === 'learning');
  const dailyItems = items.filter((i) => i.sourceType === 'daily');

  const dailyUnresolved = dailyItems.filter((i) => !i.isResolved).length;
  const dailyRate =
    dailyItems.length > 0
      ? Math.round(
          (dailyItems.filter((i) => i.isResolved).length / dailyItems.length) *
            100,
        )
      : 0;

  return (
    <div className="page-container">
      {!loading && (
        <>
        <div className="wrong-note-header">
          <h2 className="title">오답 노트</h2>
        </div>
        <div className="wn-track-grid">
          {TRACKS.map((track) => {
            const trackItems = learningItems.filter((i) => i.track === track);
            const unresolved = trackItems.filter((i) => !i.isResolved).length;
            const resolved = trackItems.filter((i) => i.isResolved).length;
            const total = trackItems.length;
            const resolvedRate =
              total > 0 ? Math.round((resolved / total) * 100) : 0;

            return (
              <div
                key={track}
                className="wn-track-card"
                onClick={() => navigate(`/wrong-answer/${track.toLowerCase()}`)}
              >
                <div className="wn-track-icon">{getTrackIcon(track)}</div>
                <div className="wn-track-name">{track}</div>
                <div className="wn-track-progress-bar">
                  <div
                    className="wn-track-progress-fill"
                    style={{ width: `${resolvedRate}%` }}
                  />
                </div>
                <div className="wn-track-stats">
                  <span className="wn-unresolved">{unresolved}개 복습전</span>
                  <span className="wn-total">전체 {total}개</span>
                </div>
              </div>
            );
          })}

          <div className="wn-daily-divider" />

          <div
            className="wn-track-card wn-daily-card"
            onClick={() => navigate('/wrong-answer/daily')}
          >
            <div className="wn-track-icon">⚡</div>
            <div className="wn-track-name">데일리 퀴즈</div>
            <div className="wn-track-progress-bar">
              <div
                className="wn-track-progress-fill wn-daily-fill"
                style={{ width: `${dailyRate}%` }}
              />
            </div>
            <div className="wn-track-stats">
              <span className="wn-unresolved">{dailyUnresolved}개 복습전</span>
              <span className="wn-total">전체 {dailyItems.length}개</span>
            </div>
          </div>
        </div>
        </>
      )}
    </div>
  );
}
