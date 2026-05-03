import WrongNoteItem from "../components/WrongNoteItem";
import "../styles/WrongNote.css";
import wrongAnswers from "../mockup/wrongAnswers.json";


export default function WrongNotePage() {
  const data = wrongAnswers.wrongAnswers;

  return (
    <div className="page-container">
      <h2 className="title">📝 오답 노트</h2>

      <div className="list">
        {data.map((item) => (
          <WrongNoteItem key={item.id} item={item} />
        ))}
      </div>

      <button className="review-btn">복습하기</button>
    </div>
  );
}