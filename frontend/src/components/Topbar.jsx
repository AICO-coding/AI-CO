import "../styles/Topbar.css";
import logo from '../assets/logo.png';

function Topbar() {
  return (
    <div id="topbar">
      <div className="tb-logo">
        <img src={logo} alt="로고" className="tb-logo-img" />
        AI<span>CO</span>
      </div>
    </div>
  );
}

export default Topbar;
