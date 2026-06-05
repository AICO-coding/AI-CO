import '../../styles/MultipleChoice.css';
import '../../styles/WrongNote.css';

const STYLE_CORRECT = {
  backgroundColor: '#dcfce7',
  border: '2px solid #16a34a',
  color: '#15803d',
};

const STYLE_WRONG = {
  backgroundColor: '#fee2e2',
  border: '2px solid #dc2626',
  color: '#b91c1c',
};

const STYLE_INDEX_CORRECT = { backgroundColor: '#16a34a', color: '#ffffff' };
const STYLE_INDEX_WRONG = { backgroundColor: '#dc2626', color: '#ffffff' };

function extractIndex(raw) {
  if (raw === null || raw === undefined || raw === '') return -1;

  let value = raw;
  if (typeof raw === 'string') {
    try {
      value = JSON.parse(raw);
    } catch {}
  }

  if (typeof value === 'number') return value - 1;
  if (typeof value === 'string') {
    const n = parseInt(value, 10);
    return isNaN(n) ? -1 : n - 1;
  }
  if (typeof value === 'object' && value !== null) {
    if ('answer' in value) return extractIndex(value.answer);
    if ('selectedIndex' in value) return value.selectedIndex - 1;
    if ('correct_index' in value) return value.correct_index - 1;
  }
  return -1;
}

export default function WrongNoteMultipleChoice({ detail }) {
  const problem = detail.problem;
  const choices = problem.content?.choices ?? [];

  const userIndex = extractIndex(detail.userAnswer);
  const correctIndex = extractIndex(
    detail.correctAnswer ?? detail.problem?.answer,
  );

  console.log(
    '[WrongNote] userAnswer:',
    detail.userAnswer,
    '→ index:',
    userIndex,
  );
  console.log(
    '[WrongNote] correctAnswer:',
    detail.correctAnswer,
    '→ index:',
    correctIndex,
  );

  function choiceStyle(idx) {
    if (idx === correctIndex) return STYLE_CORRECT;
    if (idx === userIndex) return STYLE_WRONG;
    return {};
  }

  function indexStyle(idx) {
    if (idx === correctIndex) return STYLE_INDEX_CORRECT;
    if (idx === userIndex) return STYLE_INDEX_WRONG;
    return {};
  }

  return (
    <div className="quiz-layout">
      <div className="quiz-left">
        <div className="quiz-info-card">
          <div className="quiz-label">MULTIPLE CHOICE</div>
          <div className="quiz-title">{problem.chapter}</div>
          <div className="quiz-desc">
            빨간 선지가 내 오답, 초록 선지가 정답입니다.
          </div>
        </div>
      </div>

      <div className="quiz-wrap">
        <div className="quiz-question">{problem.content?.question}</div>

        <div className="quiz-choices">
          {choices.map((choice, idx) => (
            <div
              key={idx}
              className="quiz-choice wn-choice-readonly"
              style={choiceStyle(idx)}
            >
              <div className="quiz-choice-index" style={indexStyle(idx)}>
                {idx + 1}
              </div>
              <div className="quiz-choice-text">{choice}</div>
            </div>
          ))}
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
