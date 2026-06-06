import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';

import '../styles/Track.css';

export default function Track() {
  const navigate = useNavigate();

  const [trackData, setTrackData] = useState(null);

  const [progressData, setProgressData] = useState([]);

  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTracks = async () => {
      try {
        const token = localStorage.getItem('accessToken');

        const headers = {
          ...(token && {
            Authorization: `Bearer ${token}`,
          }),
        };

        const [trackRes, progressRes] = await Promise.all([
          fetch('http://210.125.96.59:8000/tracks', {
            headers,
          }),
          fetch('http://210.125.96.59:8000/tracks/progress', {
            headers,
          }),
        ]);

        if (trackRes.status === 401 || progressRes.status === 401) {
          throw new Error('로그인이 필요합니다.');
        }

        if (!trackRes.ok || !progressRes.ok) {
          throw new Error('트랙 정보를 불러오지 못했습니다.');
        }

        const trackJson = await trackRes.json();

        const progressJson = await progressRes.json();

        setTrackData(trackJson);

        setProgressData(progressJson.tracks || []);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchTracks();
  }, []);

  if (error) {
    return (
      <div className="track-wrap">
        <p>❌ {error}</p>

        <button onClick={() => (window.location.href = '/login')}>
          로그인 하러가기
        </button>
      </div>
    );
  }

  if (!trackData) return null;

  return (
    <div className="track-wrap">
      <div className="track-page-title">📚 학습 트랙</div>

      <div className="track-page-sub">원하는 AI 분야를 선택하세요.</div>

      <div className="track-page-grid">
        {trackData.tracks.map((track) => {
          const progress = progressData.find((p) => p.track === track.track);

          return (
            <div
              key={track.track}
              className="track-page-card"
              onClick={() =>
                navigate(`/tracks/${track.track.toLowerCase()}/chapters`)
              }
            >
              <div className="track-card-top">
                <div className="tc-name">📌 {track.track}</div>
              </div>

              <div className="tc-progress-wrap">
                <div className="tc-progress-bar">
                  <div
                    className="tc-progress-fill"
                    style={{
                      width: `${progress?.completionRate || 0}%`,
                    }}
                  />
                </div>

                <div className="tc-progress-text">
                  {progress?.completionRate || 0}% 완료
                </div>
              </div>

              <div className="tc-stats">
                <div>{progress?.totalXp || 0} XP</div>

                <div>힌트 사용 {progress?.hintUsed || 0}회</div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
