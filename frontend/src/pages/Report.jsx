import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';

import '../styles/Report.css';
import { API_BASE_URL } from '../config/api';

export default function Report() {
  const navigate = useNavigate();

  const [trackData, setTrackData] = useState(null);

  const [reportCounts, setReportCounts] = useState({});

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

        const trackRes = await fetch(`${API_BASE_URL}/tracks`, {
          headers,
        });

        if (trackRes.status === 401) {
          throw new Error('로그인이 필요합니다.');
        }

        if (!trackRes.ok) {
          throw new Error('트랙 정보를 불러오지 못했습니다.');
        }

        const trackJson = await trackRes.json();
        setTrackData(trackJson);

        const counts = {};
        await Promise.all(
          trackJson.tracks.map(async (track) => {
            const id = track.track.toLowerCase();
            const res = await fetch(
              `${API_BASE_URL}/reports/${id}`,
              { headers },
            );
            if (res.ok) {
              const data = await res.json();
              counts[track.track] = data.reports?.length ?? 0;
            } else {
              counts[track.track] = 0;
            }
          }),
        );
        setReportCounts(counts);
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
      <div className="track-page-title">📊 요약리포트</div>

      <div className="track-page-sub">
        요약리포트를 확인할 트랙을 선택하세요.
      </div>

      <div className="track-page-grid">
        {trackData.tracks.map((track) => (
          <div
            key={track.track}
            className="track-page-card"
            onClick={() => navigate(`/reports/${track.track.toLowerCase()}`)}
          >
            <div className="track-card-top">
              <div className="tc-name">📌 {track.track}</div>
            </div>

            <div className="tc-report-count">
              요약리포트 개수 : {reportCounts[track.track] ?? 0}개
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
