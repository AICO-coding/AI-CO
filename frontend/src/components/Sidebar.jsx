import { Link } from "react-router-dom";

function Sidebar() {
  return (
  <div style={{ width: "250px", background: "#f5f5f5" }}>
    <h2>CodeDojo</h2>

    <nav>
      <div><Link to="/">홈</Link></div>
      <div><Link to="/track">학습 트랙</Link></div>
      <div><Link to="/daily">데일리 태스크</Link></div>
    </nav>
  </div>
  );
}

export default Sidebar;