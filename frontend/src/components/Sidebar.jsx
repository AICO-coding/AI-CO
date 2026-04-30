import { Link, useLocation } from "react-router-dom";
import "./Sidebar.css";

function Sidebar() {
  const location = useLocation();

  return (
    <div id="sidebar">
      <div className="sb-cobot">
        <span className="sb-cobot-img">🤖</span>
        <div className="sb-cobot-txt">안녕! 나는 코봇이야</div>
        <div className="sb-cobot-txt">오늘도 같이 수련하자!</div>
      </div>

      <div className="sb-section">메뉴</div>

      <Link
        to="/"
        className={`sb-btn ${location.pathname === "/" ? "on" : ""}`}
      >
        <span className="sb-icon">🏠</span> 홈
      </Link>

      <Link
        to="/track"
        className={`sb-btn ${location.pathname === "/track" ? "on" : ""}`}
      >
        <span className="sb-icon">📚</span> 학습 트랙
        <span className="sb-badge">3</span>
      </Link>

      <Link
        to="/daily"
        className={`sb-btn ${location.pathname === "/daily" ? "on" : ""}`}
      >
        <span className="sb-icon">⚡</span> 데일리 태스크
      </Link>

      <div className="sb-progress">
        <div className="sb-proglbl">
          <span>오늘의 진도</span>
          <span>40%</span>
        </div>
        <div className="sb-progbar">
          <div className="sb-progfill" style={{ width: "40%" }}></div>
        </div>
      </div>
    </div>
  );
}

export default Sidebar;
