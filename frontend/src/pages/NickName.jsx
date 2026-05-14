import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

export default function Nickname() {
  const [nickname, setNickname] = useState("");

  const navigate = useNavigate();

  const handleSubmit = async () => {
    try {
      const accessToken =
        localStorage.getItem("accessToken");

      await axios.post(
        "http://192.168.0.4:8000/auth/nickname",
        {
          nickname,
        },
        {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        }
      );

      navigate("/home");

    } catch (error) {
      console.error(error.response?.data);

      alert("닉네임 설정 실패");
    }
  };

  return (
    <div className="login-page">
      <div className="login-card">

        <h1 className="login-title">
          닉네임 설정
        </h1>

        <p className="login-subtitle">
          사용할 닉네임을 입력해주세요.
        </p>

        <input
          value={nickname}
          onChange={(e) => setNickname(e.target.value)}
          placeholder="닉네임"
          className="nickname-input"
        />

        <button
          onClick={handleSubmit}
          className="nickname-button"
        >
          시작하기
        </button>

      </div>
    </div>
  );
}