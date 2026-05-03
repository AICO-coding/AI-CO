import { Link } from 'react-router-dom';
import '../styles/Home.css';

function Home() {
  return (
    <div className="home-wrap">

      {/* 히어로 카드 */}
      <div className="home-hero">
        <div>
          <div className="hero-title">안녕하세요! 코딩 도장에 오신 걸 환영해요 🎉</div>
          <div className="hero-sub">
            AI를 이해하면서 직접 짜는 것, 그게 진짜 실력이에요.<br />
            오늘도 코봇과 함께 한 챕터 완성해봐요!
          </div>
          <Link to="/track" className="hero-btn">학습 시작하기 →</Link>
        </div>
        <img src="/src/assets/cobot.png" alt="코봇" className="hero-cobot" />
      </div>

      {/* 오늘의 태스크 */}
      <div className="sec-title">📋 오늘의 태스크</div>
      <Link to="/daily" className="daily-card">
        <div className="daily-top">
          <div className="daily-title">데일리 챌린지</div>
          <div className="daily-badge">⏰ 3시간 후 마감</div>
        </div>
        <div className="daily-prog-row">
          <div className="daily-prog-wrap">
            <div className="daily-prog-fill" style={{ width: '40%' }}></div>
          </div>
          <span className="daily-prog-txt">2 / 5</span>
        </div>
        <div className="daily-info">🧠 3문제 남았어요! 클릭해서 이어풀기 →</div>
      </Link>


      {/* 학습 트랙 */}
      <div className="sec-title">📚 학습 트랙</div>
      <div className="track-grid">

        <Link to="/track/ml" className="track-card tc-ml">
          <span className="tc-emoji">🤖</span>
          <div className="tc-name">머신러닝</div>
          <div className="tc-sub">ML 기초부터 심화까지</div>
          <div className="tc-prog-wrap">
            <div className="tc-prog tc-prog-ml" style={{ width: '45%' }}></div>
          </div>
          <div className="tc-info">45% 완료 · 5/11 챕터</div>
        </Link>

        <Link to="/track/cv" className="track-card tc-cv">
          <span className="tc-emoji">👁️</span>
          <div className="tc-name">컴퓨터 비전</div>
          <div className="tc-sub">이미지 인식과 처리</div>
          <div className="tc-prog-wrap">
            <div className="tc-prog tc-prog-cv" style={{ width: '20%' }}></div>
          </div>
          <div className="tc-info">20% 완료 · 2/10 챕터</div>
        </Link>

        <Link to="/track/nlp" className="track-card tc-nlp">
          <span className="tc-emoji">💬</span>
          <div className="tc-name">자연어 처리</div>
          <div className="tc-sub">텍스트 이해와 생성</div>
          <div className="tc-prog-wrap">
            <div className="tc-prog tc-prog-nlp" style={{ width: '0%' }}></div>
          </div>
          <div className="tc-info">아직 시작 전이에요!</div>
        </Link>
      </div>

    </div>
  );
}

export default Home;