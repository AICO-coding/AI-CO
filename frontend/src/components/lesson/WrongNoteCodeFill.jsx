import '../../styles/CodeFill.css';
import '../../styles/WrongNote.css';

export default function WrongNoteCodeFill({ detail }) {
  const problem = detail.problem;
  const template = problem.content?.template ?? '';
  const correctAnswer = detail.correctAnswer ?? problem.answer ?? {};
  const userAnswer = detail.userAnswer ?? {};

  const renderTemplate = () => {
    return template.split(/({{.*?}})/g).map((part, idx) => {
      const match = part.match(/{{(.*?)}}/);
      if (!match) return <span key={idx}>{part}</span>;

      const key = match[1];
      const correct = correctAnswer[key] ?? '';
      const user =
        userAnswer && typeof userAnswer === 'object' ? (userAnswer[key] ?? '') : '';
      const isUserWrong = user !== '' && user !== correct;

      return (
        <span key={`${key}-${idx}`} className="wn-codefill-slot">
          {isUserWrong && <span className="wn-codefill-wrong">{user}</span>}
          <span className="wn-codefill-correct">{correct}</span>
        </span>
      );
    });
  };

  return (
    <div className="wn-quiz-layout">
      <div className="quiz-left">
        <div className="quiz-info-card">
          <div className="quiz-label">CODE FILL</div>
          <div className="quiz-title">{problem.chapter}</div>
          <div className="quiz-desc">
            초록색이 정답, 빨간색(취소선)이 내가 입력한 오답입니다.
          </div>
        </div>
      </div>

      <div className="quiz-wrap" style={{ overflow: 'auto' }}>
        <div
          className="code-editor"
          style={{ borderRadius: 18, marginBottom: problem.explanation ? 16 : 0 }}
        >
          <div className="code-editor-header">
            <div className="dots">
              <span />
              <span />
              <span />
            </div>
            <div className="code-editor-title">practice.py</div>
          </div>
          <div className="code-editor-body">
            <div className="codefill-code">{renderTemplate()}</div>
          </div>
        </div>

        {problem.explanation && (
          <div className="wn-explanation">
            <span className="wn-explanation-label">해설</span>
            {problem.explanation}
          </div>
        )}
      </div>
    </div>
  );
}
