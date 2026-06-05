import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { QuizItem } from '../components/QuizItem';
import '../styles/DailyTask.css';

const API_BASE = 'http://210.125.96.59:8000';

export default function DailyTask() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [dailyData, setDailyData] = useState(null);
  const [answers, setAnswers] = useState({});
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState(null);

  useEffect(() => {
    fetchDaily();
  }, []);

  const fetchDaily = async () => {
    const token = localStorage.getItem('accessToken');
    try {
      const res = await fetch(`${API_BASE}/daily`, {
        headers: token ? { Authorization: `Bearer ${token}` } : {},
      });
      const data = await res.json();
      setDailyData(data);

      if (data.isCompleted) {
        await fetchResult();
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const fetchResult = async () => {
    const token = localStorage.getItem('accessToken');
    try {
      const res = await fetch(`${API_BASE}/daily/result`, {
        headers: token ? { Authorization: `Bearer ${token}` } : {},
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleSelect = (dailyProblemId, answer) => {
    setAnswers((prev) => ({ ...prev, [dailyProblemId]: answer }));
  };

  const handleSubmit = async () => {
    if (!dailyData) return;

    const unanswered = dailyData.dailyProblems.filter(
      (p) => answers[p.dailyProblemId] == null,
    );
    if (unanswered.length > 0) {
      alert('모든 문제에 답을 선택해주세요.');
      return;
    }

    const token = localStorage.getItem('accessToken');
    setSubmitting(true);
    try {
      const res = await fetch(`${API_BASE}/daily/submit`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(token ? { Authorization: `Bearer ${token}` } : {}),
        },
        body: JSON.stringify({
          answers: dailyData.dailyProblems.map((p) => ({
            dailyProblemId: p.dailyProblemId,
            answer: { answer: answers[p.dailyProblemId] },
          })),
        }),
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
      alert('제출 중 오류가 발생했습니다.');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) return null;

  if (result) {
    const resultList = result.results ?? [];
    const completedAt = result.completedAt
      ? new Date(result.completedAt).toLocaleTimeString('ko-KR', {
          hour: '2-digit',
          minute: '2-digit',
        })
      : null;

    return (
      <div className="page-container">
        <div className="page-inner">
          <div className="daily-score-card">
            {result.isPerfect && (
              <div className="daily-score-perfect">🎉 퍼펙트!</div>
            )}
            <div className="daily-score-main">
              <span className="daily-score-num">{result.score}</span>
              <span className="daily-score-total">
                / {result.totalProblems}
              </span>
            </div>
            <div className="daily-score-meta">
              <span className="daily-score-xp">+{result.xpEarned} XP</span>
              {completedAt && (
                <span className="daily-score-time">{completedAt} 완료</span>
              )}
            </div>
          </div>

          <div className="daily-result-list">
            {resultList.map((item, idx) => (
              <div
                key={item.dailyProblemId ?? idx}
                className={`daily-result-item ${item.isCorrect ? 'correct' : 'wrong'}`}
              >
                <div className="daily-result-item-header">
                  <span className="daily-result-item-num">Q{idx + 1}</span>
                  <span
                    className={`daily-result-badge ${item.isCorrect ? 'correct' : 'wrong'}`}
                  >
                    {item.isCorrect ? '✅ 정답' : '❌ 오답'}
                  </span>
                </div>

                <div className="daily-result-item-question">
                  {item.content?.question}
                </div>

                {!item.isCorrect && (
                  <div className="daily-result-answer-row">
                    <div className="daily-result-answer-box wrong">
                      <span className="daily-result-answer-label">내 답</span>
                      <span className="daily-result-answer-text">
                        {item.content?.choices?.[item.userAnswer?.answer - 1] ??
                          '-'}
                      </span>
                    </div>
                    <div className="daily-result-answer-box correct">
                      <span className="daily-result-answer-label">정답</span>
                      <span className="daily-result-answer-text">
                        {item.content?.choices?.[
                          item.correctAnswer?.answer - 1
                        ] ?? '-'}
                      </span>
                    </div>
                  </div>
                )}

                {item.explanation && (
                  <div className="daily-result-explanation">
                    <span className="daily-result-explanation-label">해설</span>
                    {item.explanation}
                  </div>
                )}
              </div>
            ))}
          </div>
          <button className="home-btn" onClick={() => navigate('/home')}>
            홈으로 돌아가기
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="page-container">
      <div className="page-inner">
        <div className="header-card">
          <div className="header-title">{dailyData?.date} 데일리 퀴즈</div>
          <div className="header-desc">AI가 오늘 생성한 문제입니다.</div>
        </div>

        {dailyData?.dailyProblems.map((problem) => (
          <QuizItem
            key={problem.dailyProblemId}
            question={problem.content?.question}
            options={problem.content?.choices ?? []}
            onSelect={(answer) => handleSelect(problem.dailyProblemId, answer)}
          />
        ))}

        <div className="submit-box">
          <button
            className="submit-btn"
            onClick={handleSubmit}
            disabled={submitting}
          >
            {submitting ? '채점 중...' : '제출하기'}
          </button>
        </div>
        <button className="home-btn" onClick={() => navigate('/home')}>
          홈으로 돌아가기
        </button>
      </div>
    </div>
  );
}
