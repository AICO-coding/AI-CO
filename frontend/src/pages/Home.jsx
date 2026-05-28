import { Link } from "react-router-dom";
import { useEffect, useState } from "react";

import "../styles/Home.css";

function Home() {
  const [trackData, setTrackData] =
    useState(null);

  const [error, setError] =
    useState(null);

  useEffect(() => {
    const fetchTracks = async () => {
      try {
        const token =
          localStorage.getItem("accessToken");

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
          throw new Error(
            "로그인이 필요합니다."
          );
        }

        const data = await res.json();

        console.log(data);

        setTrackData(data);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchTracks();
  }, []);

  if (error) {
    return (
      <div className="home-wrap">
        ❌ {error}
      </div>
    );
  }

  if (!trackData) return null;

  return (
    <div className="home-wrap">
      <div className="home-hero">
        <div>
          <div className="hero-title">
            안녕하세요! 코딩 도장에 오신 걸 환영해요 🎉
          </div>

          <div className="hero-sub">
            AI를 이해하면서 직접 짜는 것,
            그게 진짜 실력이에요.
            <br />
            오늘도 코봇과 함께 한 챕터
            완성해봐요!
          </div>

          <Link
            to="/tracks"
            className="hero-btn"
          >
            학습 시작하기 →
          </Link>
        </div>

        <img
          src="/src/assets/cobot.png"
          alt="코봇"
          className="hero-cobot"
        />
      </div>
      <div className="sec-title">
        📋 오늘의 태스크
      </div>

      <Link
        to="/daily"
        className="daily-card"
      >
        <div className="daily-top">
          <div className="daily-title">
            데일리 챌린지
          </div>

          <div className="daily-badge">
            ⏰ 3시간 후 마감
          </div>
        </div>

        <div className="daily-prog-row">
          <div className="daily-prog-wrap">
            <div
              className="daily-prog-fill"
              style={{ width: "40%" }}
            />
          </div>

          <span className="daily-prog-txt">
            2 / 5
          </span>
        </div>

        <div className="daily-info">
          🧠 3문제 남았어요! 클릭해서
          이어풀기 →
        </div>
      </Link>
      <div className="sec-title">
        📚 학습 트랙
      </div>

      <div className="track-grid">
        {trackData.tracks.map((track) => (
          <Link
            key={track.track}
            to={`/tracks/${track.track.toLowerCase()}/chapters`}
            className="track-card"
          >

            <div className="tc-name">
              📌 {track.track}
            </div>

            <div className="tc-sub">
              AI 학습 트랙
            </div>

            <div className="tc-prog-wrap">
              <div
                className="tc-prog"
                style={{
                  width: `${track.completionRate}%`,
                }}
              />
            </div>

            <div className="tc-info">
              {track.completionRate}% 완료
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default Home;