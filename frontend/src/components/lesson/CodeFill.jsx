import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeRaw from 'rehype-raw';

import '../../styles/CodeFill.css';
import { API_BASE_URL } from '../../config/api';

export default function CodeFill({ lesson, registerSubmit }) {
  const { trackId, chapterId } = useParams();

  const [markdown, setMarkdown] = useState('');
  const [answers, setAnswers] = useState({});

  const [openedHints, setOpenedHints] = useState([]);
  const [confirmHint, setConfirmHint] = useState(null);
  const [blockedHintLevel, setBlockedHintLevel] = useState(null);
  const [blankResults, setBlankResults] = useState({});

  useEffect(() => {
    setAnswers({});
    setBlankResults({});
    setOpenedHints(lesson.usedHintLevels || []);
    setConfirmHint(null);
    setBlockedHintLevel(null);
  }, [lesson.lessonId]);

  useEffect(() => {
    async function loadMarkdown() {
      const url = lesson.content?.markdownUrl || lesson.markdownUrl;
      if (!url) return;
      const res = await fetch(url);
      const contentType = res.headers.get('content-type') || '';
      if (!res.ok || contentType.includes('text/html')) return;
      const text = await res.text();
      setMarkdown(text);
    }
    loadMarkdown();
  }, [lesson.lessonId]);

  const useHint = async () => {
    if (!confirmHint) return;
    try {
      const token = localStorage.getItem('accessToken');
      const res = await fetch(
        `${API_BASE_URL}/tracks/${trackId}/chapters/${chapterId}/hint`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            ...(token && { Authorization: `Bearer ${token}` }),
          },
          body: JSON.stringify({
            problemId: lesson.problemId,
            hintLevel: confirmHint.level,
          }),
        },
      );
      if (!res.ok) throw new Error('힌트 요청 실패');
      setOpenedHints((prev) =>
        prev.includes(confirmHint.level) ? prev : [...prev, confirmHint.level],
      );
      setConfirmHint(null);
    } catch (err) {
      console.error(err);
      alert('힌트 요청 중 오류가 발생했습니다.');
    }
  };

  const submit = async () => {
    try {
      const token = localStorage.getItem('accessToken');
      const res = await fetch(
        `${API_BASE_URL}/tracks/${trackId}/chapters/${chapterId}/submit`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            ...(token && { Authorization: `Bearer ${token}` }),
          },
          body: JSON.stringify({
            lessonId: lesson.lessonId,
            problemId: lesson.problemId,
            answer: answers,
          }),
        },
      );
      if (!res.ok) throw new Error('답안 제출 실패');
      const data = await res.json();
      console.log('[submit response]', data);

      const results = {};
      if (data.correctAnswer) {
        Object.keys(data.correctAnswer).forEach((k) => {
          results[k] =
            (answers[k] || '').trim() === String(data.correctAnswer[k]).trim()
              ? 'correct'
              : 'wrong';
        });
      } else if (data.results) {
        Object.keys(data.results).forEach((k) => {
          results[k] = data.results[k] ? 'correct' : 'wrong';
        });
      } else {
        Object.keys(answers).forEach((k) => {
          results[k] = data.isCorrect ? 'correct' : 'wrong';
        });
      }
      setBlankResults(results);

      return data.isCorrect;
    } catch (err) {
      console.error(err);
      alert('답안 제출 중 오류가 발생했습니다.');
      return false;
    }
  };

  useEffect(() => {
    registerSubmit?.(() => submit);
  }, [answers, lesson]);

  const renderTemplate = () => {
    return lesson.content.template.split(/({{.*?}})/g).map((part, idx) => {
      const match = part.match(/{{(.*?)}}/);
      if (!match) return <span key={idx}>{part}</span>;
      const key = match[1];
      const resultClass = blankResults[key] ? ` ${blankResults[key]}` : '';
      return (
        <input
          key={`${key}-${idx}`}
          className={`codefill-blank${resultClass}`}
          value={answers[key] || ''}
          onChange={(e) =>
            setAnswers({ ...answers, [key]: e.target.value })
          }
        />
      );
    });
  };

  return (
    <div className="codefill-layout">
      <div className="codefill-left">
        <div className="markdown-card">
          <div className="markdown-title">📘 개념 설명</div>
          <div className="markdown-body">
            <ReactMarkdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeRaw]}>
              {markdown}
            </ReactMarkdown>
          </div>
        </div>

        <div className="quiz-hint-group">
          {(lesson.hints ?? []).map((hint) => {
            const opened = openedHints.includes(hint.level);
            const canOpen =
              hint.level === 1 || openedHints.includes(hint.level - 1);

            return (
              <div
                key={hint.level}
                className={`quiz-hint-dropdown ${opened ? 'open' : ''}`}
              >
                <button
                  className={`quiz-hint-toggle ${!canOpen ? 'disabled' : ''}`}
                  onClick={() => {
                    if (!canOpen) {
                      setBlockedHintLevel(hint.level - 1);
                      return;
                    }
                    if (opened) {
                      setOpenedHints(
                        openedHints.filter((l) => l !== hint.level),
                      );
                      return;
                    }
                    setConfirmHint(hint);
                  }}
                >
                  <span>💡 Hint Level {hint.level}</span>
                  <span className="quiz-hint-arrow">{opened ? '−' : '+'}</span>
                </button>
                {opened && (
                  <div className="quiz-hint-content">{hint.text}</div>
                )}
              </div>
            );
          })}
        </div>

        <div className="mission-card">
          <div className="mission-title">🎯 목표</div>
          <div className="mission-text">빈칸을 모두 채워 코드를 완성하세요.</div>
        </div>
      </div>

      <div className="codefill-right">
        <div className="editor-top">← 개념을 참고해서 코드 완성</div>
        <div className="code-editor">
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
      </div>

      {confirmHint && (
        <div className="hint-confirm-popup">
          <div className="hint-confirm-title">💡 힌트를 사용하시겠습니까?</div>
          <div className="hint-confirm-desc">
            Hint Level {confirmHint.level}을 사용합니다.
            <br />
            ⚠️ 5XP가 차감됩니다.
          </div>
          <div className="hint-confirm-actions">
            <button
              className="hint-cancel-btn"
              onClick={() => setConfirmHint(null)}
            >
              취소
            </button>
            <button className="hint-use-btn" onClick={useHint}>
              사용하기
            </button>
          </div>
        </div>
      )}

      {blockedHintLevel !== null && (
        <div className="hint-confirm-popup">
          <div className="hint-confirm-title">
            ⚠️ 먼저 이전 단계를 완료해주세요
          </div>
          <div className="hint-confirm-desc">
            Hint Level {blockedHintLevel}을 먼저 사용해야 다음 단계를 열 수
            있습니다.
          </div>
          <div className="hint-confirm-actions">
            <button
              className="hint-use-btn"
              onClick={() => setBlockedHintLevel(null)}
            >
              확인
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
