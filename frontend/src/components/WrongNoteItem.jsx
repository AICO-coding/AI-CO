import { useNavigate } from "react-router-dom";

const API_BASE = "http://210.125.96.59:8000";

const PROBLEM_TYPE_LABEL = {
  multiple_choice: "객관식",
  code_fill:       "코드 빈칸",
  parameter:       "파라미터",
};

const PROBLEM_TYPE_COLOR = {
  multiple_choice: "type-mc",
  code_fill:       "type-cf",
  parameter:       "type-pm",
};

export default function WrongNoteItem({ item, trackId, onDelete }) {
  const navigate = useNavigate();

  const typeLabel = PROBLEM_TYPE_LABEL[item.problemType] ?? item.problemType;
  const typeColor = PROBLEM_TYPE_COLOR[item.problemType] ?? "";

  async function handleDelete() {
    const token = localStorage.getItem("accessToken");
    try {
      await fetch(`${API_BASE}/wrong-answers/${item.id}`, {
        method: "DELETE",
        headers: token ? { Authorization: `Bearer ${token}` } : {},
      });
      onDelete?.(item.id);
    } catch {
      // 삭제 실패 시 조용히 처리
    }
  }

  return (
    <div
      className="wrong-card"
      onClick={() => navigate(`/wrong-answer/${trackId}/${item.id}`)}
    >
      <div className="wrong-card-top">
        <div className="wrong-card-tags">
          <span className="track-badge">{item.track}</span>
          <span className={`wrong-type-badge ${typeColor}`}>{typeLabel}</span>
        </div>
        <span className={item.isResolved ? "status resolved" : "status unresolved"}>
          {item.isResolved ? "복습완료" : "복습전"}
        </span>
      </div>

      <div className="wrong-card-title">{item.chapter}</div>

      <div className="wrong-card-bottom">
        <span className="wrong-review-count">복습 {item.reviewCount}회</span>
        <button
          className="delete-btn"
          onClick={(e) => { e.stopPropagation(); handleDelete(); }}
        >
          삭제
        </button>
      </div>
    </div>
  );
}
