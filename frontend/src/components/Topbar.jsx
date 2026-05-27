import "../styles/Topbar.css";
import logo from "../assets/logo.png";

import { useNavigate } from "react-router-dom";

function Topbar() {

  const navigate = useNavigate();

  const goHome = () => {
    navigate("/home");
  };

  return (
    <div id="topbar">

      <div
        className="tb-logo"
        onClick={goHome}
      >
        <img
          src={logo}
          alt="로고"
          className="tb-logo-img"
        />

        AI<span>CO</span>
      </div>

    </div>
  );
}

export default Topbar;