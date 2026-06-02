import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

import "../styles/Track.css";

export default function Track() {
  const navigate = useNavigate();

  const [trackData, setTrackData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTracks = async () => {
      try {
        const token = localStorage.getItem("accessToken");

        const res = await fetch(
          "http://210.125.96.59:8000/tracks",
          {
            headers: {
              ...(token && {
                Authorization: `Bearer ${token}`,
              }),
            },
          }
        );

        if (res.status === 401) {
          throw new Error("로그인이 필요합니다.");
        }

        const data = await res.json();
        setTrackData(data);
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
        <button onClick={() => (window.location.href = "/login")}>
          로그인 하러가기
        </button>
      </div>
    );
  }

  // 👉 데이터 없으면 아무것도 안 그림
  if (!trackData) return null;

  return (
    <div className="track-wrap">
      <div className="track-page-title">
        📚 학습 트랙
      </div>

      <div className="track-page-sub">
        원하는 AI 분야를 선택하세요.
      </div>

      <div className="track-page-grid">
        {trackData.tracks.map((track) => (
          <div
            key={track.track}
            className="track-page-card"
            onClick={() =>
              navigate(
                `/tracks/${track.track.toLowerCase()}/chapters`
              )
            }
          >
            <div className="track-card-top">
              <div className="tc-name">
                📌 {track.track}
              </div>
            </div>

            <div className="tc-progress-wrap">
              <div className="tc-progress-bar">
                <div
                  className="tc-progress-fill"
                  style={{
                    width: `${track.completionRate}%`,
                  }}
                />
              </div>

              <div className="tc-progress-text">
                {track.completionRate}% 완료
              </div>
            </div>

          </div>
        ))}
      </div>
    </div>
  );
}