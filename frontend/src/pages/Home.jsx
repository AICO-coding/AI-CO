import { Link } from 'react-router-dom';
import { useEffect, useState } from 'react';

import '../styles/Home.css';
import { API_BASE_URL } from '../config/api';

const API_BASE = API_BASE_URL;

function getTimeLeft(expiresAt) {
  const diff = new Date(expiresAt) - new Date();
  if (diff <= 0) return '마감';
  const hours = Math.floor(diff / 1000 / 60 / 60);
  const minutes = Math.floor((diff / 1000 / 60) % 60);
  if (hours > 0) return `${hours}시간 후 마감`;
  return `${minutes}분 후 마감`;
}

function Home() {
  const [trackData, setTrackData] = useState(null);
  const [progressData, setProgressData] = useState([]);
  const [dailyData, setDailyData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAll = async () => {
      try {
        const token = localStorage.getItem('accessToken');
        const headers = {
          ...(token && { Authorization: `Bearer ${token}` }),
        };

        const [trackRes, progressRes, dailyRes] = await Promise.all([
          fetch(`${API_BASE}/tracks`, { headers }),
          fetch(`${API_BASE}/tracks/progress`, { headers }),
          fetch(`${API_BASE}/daily`, { headers }),
        ]);

        if (trackRes.status === 401 || progressRes.status === 401) {
          throw new Error('로그인이 필요합니다.');
        }

        if (!trackRes.ok || !progressRes.ok) {
          throw new Error('데이터를 불러오지 못했습니다.');
        }

        const trackJson    = await trackRes.json();
        const progressJson = await progressRes.json();

        setTrackData(trackJson);
        setProgressData(progressJson.tracks || []);

        if (dailyRes.ok) {
          setDailyData(await dailyRes.json());
        }
      } catch (err) {
        setError(err.message);
      }
    };

    fetchAll();
  }, []);

  if (error) {
    return <div className="home-wrap">❌ {error}</div>;
  }

  if (!trackData) return null;

  return (
    <div className="home-wrap">
      <div className="home-hero">
        <div>
          <div className="hero-title">
            안녕하세요! 아이코에 오신 걸
            환영해요 🎉
          </div>

          <div className="hero-sub">
            AI를 이해하면서 직접 짜는 것,
            그게 진짜 실력이에요.
            <br />
            오늘도 코냥이와 함께 공부해보아요!
          </div>

          <Link to="/tracks" className="hero-btn">
            학습 시작하기
          </Link>
        </div>

        <img
          src="/src/assets/cobot.png"
          alt="코봇"
          className="hero-cobot"
        />
      </div>

      <div className="sec-title">📋 오늘의 퀴즈</div>

      <Link to="/daily" className={`daily-card${dailyData?.isCompleted ? ' daily-card-done' : ''}`}>
        <div className="daily-top">
          <div>
            <div className="daily-date">{dailyData?.date ?? ''}</div>
            <div className="daily-title">데일리 태스크</div>
          </div>
          {dailyData?.isCompleted ? (
            <div className="daily-badge daily-badge-done">✅ 완료</div>
          ) : (
            <div className="daily-badge">
              ⏰ {dailyData ? getTimeLeft(dailyData.expiresAt) : '...'}
            </div>
          )}
        </div>

        <div className="daily-desc">
          {dailyData?.isCompleted
            ? '오늘 데일리를 완료했어요!'
            : '🧠 오늘의 문제 5개가 기다리고 있어요!'}
        </div>

        <div className="daily-cta">
          {dailyData?.isCompleted ? '결과 보러 가기' : '문제 풀러 가기'}
        </div>
      </Link>

      <div className="sec-title">📚 학습 트랙</div>

      <div className="track-grid">
        {trackData.tracks.map((track) => {
          const progress = progressData.find((p) => p.track === track.track);

          return (
            <Link
              key={track.track}
              to={`/tracks/${track.track.toLowerCase()}/chapters`}
              className="track-card"
            >
              <div className="tc-name">📌 {track.track}</div>

              <div className="tc-prog-wrap">
                <div
                  className="tc-prog"
                  style={{ width: `${progress?.completionRate || 0}%` }}
                />
              </div>

              <div className="tc-info">
                {progress?.completionRate || 0}% 완료
              </div>

              <div className="tc-stats">
                <span>{progress?.totalXp || 0} XP</span>
                <span>힌트 {progress?.hintUsed || 0}회</span>
              </div>
            </Link>
          );
        })}
      </div>
    </div>
  );
}

export default Home;
