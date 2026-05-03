export default function WrongNoteItem({ item }) {
  return (
    <div className="wrong-card">
      <div className="wrong-header">
        <span className="track">{item.track}</span>
        <span className="meta">{item.sourceType} · {item.date}</span>
      </div>

      <div className="question">
        {item.problem.question}
      </div>

      <div className="answer-box">
        <span className="wrong">✖ {item.userAnswer}</span>
        <span className="correct">✔ {item.correctAnswer}</span>
      </div>
    </div>
  );
}