import { useNavigate } from "react-router-dom";

const API_BASE = "http://210.125.96.59:8000";

const PROBLEM_TYPE_LABEL = {
  multiple_choice: "객관식",
  code_fill:       "코드 빈칸",
  parameter:       "파라미터",
};

export default function WrongNoteItem({ item, trackId, onDelete }) {
  const navigate = useNavigate();

  const typeLabel = PROBLEM_TYPE_LABEL[item.problemType] ?? item.problemType;

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
    <div className="wrong-card">
      <div className="wrong-header">
        <span className="track-badge">{item.track}</span>
        <span className="chapter-badge">{item.chapter}</span>
      </div>

      <div className="wrong-body">
        <p className="wrong-title">{item.chapter}</p>
        <p className="wrong-meta">문제 유형: {typeLabel}</p>
        <p className="wrong-meta">복습 횟수: {item.reviewCount}회</p>
      </div>

      <div className="wrong-footer">
        <span className={item.isResolved ? "status resolved" : "status unresolved"}>
          {item.isResolved ? "복습완료" : "복습전"}
        </span>
        <div className="wrong-footer-actions">
          <button
            className="detail-btn"
            onClick={() => navigate(`/wrong-answer/${trackId}/${item.id}`)}
          >
            상세보기
          </button>
          <button className="delete-btn" onClick={handleDelete}>
            삭제
          </button>
        </div>
      </div>
    </div>
  );
}
