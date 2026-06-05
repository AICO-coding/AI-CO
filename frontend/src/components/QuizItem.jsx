import '../styles/QuizItem.css';
import { useState } from 'react';

export const QuizItem = ({ question, options, onSelect }) => {
  const [selected, setSelected] = useState(null);

  const handleSelect = (idx) => {
    setSelected(idx);
    onSelect?.(idx + 1);
  };

  return (
    <div className="quiz-card">
      <div className="quiz-label">🔵 오늘의 퀴즈</div>
      <div className="quiz-title">{question}</div>

      {options.map((opt, idx) => (
        <button
          key={idx}
          onClick={() => handleSelect(idx)}
          className={`quiz-option ${selected === idx ? 'selected' : ''}`}
        >
          {idx + 1}. {opt}
        </button>
      ))}
    </div>
  );
};
