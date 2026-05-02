import { useState } from "react";
import { QuizItem } from "../components/QuizItem";
import "../styles/DailyTask.css";

export default function DailyTask() {
  const [isGrading, setIsGrading] = useState(false);
  const [isResultOpen, setIsResultOpen] = useState(false);

  const handleSubmit = () => {
    setIsGrading(true);

    setTimeout(() => {
      setIsGrading(false);
      setIsResultOpen(true);
    }, 2000);
  };

  return (
    <div className="page-container">
      <div className="page-inner">
        <div className="header-card">
          <h3>2026년 4월 13일 (일)</h3>
          <h3>AI가 오늘 생성한 문제 — 역전파 기반</h3>
        </div>

        <QuizItem
          question="learning rate가 너무 크면?"
          options={[
            "빠르게 수렴",
            "loss 발산",
            "파라미터 증가",
            "dropout 증가",
          ]}
        />

        <QuizItem
          question="learning rate가 너무 크면?"
          options={[
            "빠르게 수렴",
            "loss 발산",
            "파라미터 증가",
            "dropout 증가",
          ]}
        />

        <div className="submit-box">
          <button className="submit-btn" onClick={handleSubmit}>
            제출하기
          </button>
        </div>
      </div>

      {isGrading && (
        <div className="modal-overlay">
          <div className="modal">
            <p>채점중입니다...</p>
          </div>
        </div>
      )}

      {isResultOpen && (
        <div className="modal-overlay">
          <div className="modal">
            <h3 style={{ marginBottom: "10px" }}>채점 완료!</h3>
            <p style={{ marginBottom: "20px" }}>점수: 80점</p>

            <button
              className="result-btn"
              onClick={() => alert("해설 페이지로 이동")}
            >
              해설 보러가기
            </button>

            <button
              className="close-btn"
              onClick={() => setIsResultOpen(false)}
            >
              닫기
            </button>
          </div>
        </div>
      )}
    </div>
  );
}