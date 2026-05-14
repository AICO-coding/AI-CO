// LoginPage.jsx

import { GoogleLogin } from "@react-oauth/google";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "../styles/Login.css";

export default function Login() {
  const navigate = useNavigate();

  const handleSuccess = async (credentialResponse) => {
    try {
      const token = credentialResponse.credential;
      const response = await axios.post(
        "http://192.168.0.4:8000/auth/google/login",
        {
          idToken: token,
        }
      );
      localStorage.setItem(
        "accessToken",
        response.data.accessToken
      );

      localStorage.setItem(
        "refreshToken",
        response.data.refreshToken
      );

      localStorage.setItem(
        "userId",
        response.data.userId
      );

      localStorage.setItem(
        "nickname",
        response.data.nickname || ""
      );
      if (!response.data.nickname) {
        navigate("/nickname");
        return;
      }
      navigate("/home");

    } catch (error) {
      console.error(error.response?.data);

      alert("로그인 실패");
    }
  };

  return (
    <div className="login-page">
      <div className="login-card">

        <div className="logo">🚀</div>

        <h1 className="login-title">
          AI-CO
        </h1>

        <p className="login-subtitle">
          머신러닝 학습 플랫폼에 오신 것을 환영합니다.
        </p>

        <div className="google-wrapper">
          <GoogleLogin
            onSuccess={handleSuccess}
            onError={() => alert("Google Login Failed")}
          />
        </div>

      </div>
    </div>
  );
}