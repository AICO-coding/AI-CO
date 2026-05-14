import { Link, useLocation } from "react-router-dom";
import "../styles/Sidebar.css"
import cobot from '../assets/cobot.png';

function Sidebar() {
  const location = useLocation();
  const nickname = localStorage.getItem("nickname");

  return (
<div id="sidebar">
  <div className="sb-cobot">
    <img src={cobot} alt="코봇" className="sb-cobot-img" />
    <div className="sb-cobot-txt">안녕! 나는 코봇이야</div>
    <div className="sb-cobot-txt">오늘도 같이 수련하자!</div>
  </div>

  <div className="sb-user-card">
  <div className="sb-user-info">
    <div className="sb-user-name">
      {nickname || "사용자"}
    </div>

    <div className="sb-user-xp">
      14xp
    </div>
  </div>

  </div>

  <div className="sb-progress">
        <div className="sb-proglbl">
          <span>오늘의 진도</span>
          <span>3/8</span>
        </div>
        <div className="sb-progbar">
          <div className="sb-progfill" style={{ width: "40%" }}></div>
        </div>
      </div>


      <div className="sb-section">메뉴</div>

      <Link
        to="/home"
        className={`sb-btn ${location.pathname === "/home" ? "on" : ""}`}
      >
        <span className="sb-icon">🏠</span> 홈
      </Link>

      <Link
        to="/track"
        className={`sb-btn ${location.pathname === "/track" ? "on" : ""}`}
      >
        <span className="sb-icon">📚</span> 학습 트랙
      </Link>

      <Link
        to="/daily"
        className={`sb-btn ${location.pathname === "/daily" ? "on" : ""}`}
      >
        <span className="sb-icon">⚡</span> 데일리 태스크
      </Link>

      <Link
        to="/wrong-answer"
        className={`sb-btn ${location.pathname === "/wrong-answer" ? "on" : ""}`}
      >
        <span className="sb-icon">📝</span> 오답 노트
      </Link>

    </div>
  );
}

export default Sidebar;
