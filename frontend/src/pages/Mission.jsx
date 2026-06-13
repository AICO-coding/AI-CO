import { useEffect, useState, useRef, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeRaw from 'rehype-raw';
import '../styles/Mission.css';
import { API_BASE_URL } from '../config/api';

const TRACK_CONFIG = {
  cv: {
    apiName: 'CV',
    title: 'CIFAR-10 이미지 분류',
    chapterRange: 'Ch1~Ch7 종합',
    tech: 'PyTorch · CNN',
    xp: 100,
    jsonUrl: '/static/md/cv/misson/mission.json',
    mdFallback: '/static/md/cv/misson/mission.md',
  },
  'ml-회귀': {
    apiName: 'ML-회귀',
    title: '캘리포니아 집값 예측',
    chapterRange: 'Ch1~Ch5 종합',
    tech: 'PyTorch 완전 구현',
    xp: 150,
    jsonUrl: '/static/md/regression/mission/mission.json',
    mdFallback: '/static/md/regression/mission/mission.md',
  },
  nlp: {
    apiName: 'NLP',
    title: 'NLP 종합 미션',
    chapterRange: 'Ch1~Ch6 종합',
    tech: 'PyTorch · Transformer',
    xp: 100,
    jsonUrl: '/static/md/nlp/mission/mission.json',
    mdFallback: '/static/md/nlp/mission/mission.md',
  },
};

const API_BASE = API_BASE_URL;

export default function Mission() {
  const { trackId } = useParams();
  const navigate = useNavigate();
  const config = TRACK_CONFIG[trackId?.toLowerCase()] || TRACK_CONFIG.cv;

  const [mission, setMission] = useState(null);
  const [markdown, setMarkdown] = useState('');
  const [answers, setAnswers] = useState({});
  const [running, setRunning] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [output, setOutput] = useState(null);
  const [streamLines, setStreamLines] = useState([]);
  const [submitResult, setSubmitResult] = useState(null);
  const [submitData, setSubmitData] = useState(null);
  const [showSuccessModal, setShowSuccessModal] = useState(false);
  const [lastRunTime, setLastRunTime] = useState(null);
  const [showHintList, setShowHintList] = useState(false);
  const [confirmHint, setConfirmHint] = useState(null);
  const [openedHints, setOpenedHints] = useState([]);
  const [leftWidth, setLeftWidth] = useState(360);
  const [outputHeight, setOutputHeight] = useState(160);
  const [elapsed, setElapsed] = useState(0);
  const timerRef = useRef(null);
  const dragging = useRef(false);
  const dragStartX = useRef(0);
  const dragStartWidth = useRef(0);
  const vDragging = useRef(false);
  const vDragStartY = useRef(0);
  const vDragStartHeight = useRef(0);

  const startTimer = () => {
    setElapsed(0);
    timerRef.current = setInterval(() => setElapsed((s) => s + 1), 1000);
  };
  const stopTimer = () => {
    clearInterval(timerRef.current);
    timerRef.current = null;
  };

  const onResizerMouseDown = useCallback((e) => {
    dragging.current = true;
    dragStartX.current = e.clientX;
    dragStartWidth.current = leftWidth;
    document.body.style.cursor = 'col-resize';
    document.body.style.userSelect = 'none';
  }, [leftWidth]);

  const onVResizerMouseDown = useCallback((e) => {
    vDragging.current = true;
    vDragStartY.current = e.clientY;
    vDragStartHeight.current = outputHeight;
    document.body.style.cursor = 'row-resize';
    document.body.style.userSelect = 'none';
  }, [outputHeight]);

  useEffect(() => {
    const onMouseMove = (e) => {
      if (dragging.current) {
        const delta = e.clientX - dragStartX.current;
        const next = Math.min(Math.max(dragStartWidth.current + delta, 200), 700);
        setLeftWidth(next);
      }
      if (vDragging.current) {
        const delta = vDragStartY.current - e.clientY;
        const next = Math.min(Math.max(vDragStartHeight.current + delta, 80), 500);
        setOutputHeight(next);
      }
    };
    const onMouseUp = () => {
      dragging.current = false;
      vDragging.current = false;
      document.body.style.cursor = '';
      document.body.style.userSelect = '';
    };
    window.addEventListener('mousemove', onMouseMove);
    window.addEventListener('mouseup', onMouseUp);
    return () => {
      window.removeEventListener('mousemove', onMouseMove);
      window.removeEventListener('mouseup', onMouseUp);
    };
  }, []);

  useEffect(() => {
    async function load() {
      try {
        const jsonRes = await fetch(config.jsonUrl);
        const data = await jsonRes.json();
        setMission(data);

        const mdUrl = data.content?.markdownUrl || config.mdFallback;
        const mdRes = await fetch(mdUrl);
        const contentType = mdRes.headers.get('content-type') || '';
        if (mdRes.ok && !contentType.includes('text/html')) {
          setMarkdown(await mdRes.text());
          return;
        }
        const fallback = await fetch(config.mdFallback);
        const fallbackType = fallback.headers.get('content-type') || '';
        if (fallback.ok && !fallbackType.includes('text/html')) {
          setMarkdown(await fallback.text());
        }
      } catch (err) {
        void err;
      }
    }
    load();
  }, [trackId]);

  const template = mission?.content?.template || '';
  const hints = mission?.content?.hints || [];
  const totalBlanks = (template.match(/{{.*?}}/g) || []).length;
  const filledCount = Object.values(answers).filter((v) => v.trim()).length;

  const run = async () => {
    setRunning(true);
    setOutput(null);
    setStreamLines([]);
    startTimer();
    try {
      const token = localStorage.getItem('accessToken');
      const res = await fetch(`${API_BASE}/mission/run/stream`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(token && { Authorization: `Bearer ${token}` }),
        },
        body: JSON.stringify({ track: config.apiName, blanks: answers }),
      });

      if (!res.ok) {
        const err = await res.json();
        setOutput({ stdout: '', stderr: err.detail || '오류 발생', returncode: 1, passed: false });
        return;
      }

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';
      const stdoutLines = [];
      const stderrLines = [];
      let returncode = 0;

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const parts = buffer.split('\n\n');
        buffer = parts.pop();
        for (const part of parts) {
          const raw = part.startsWith('data: ') ? part.slice(6) : part;
          if (!raw.trim()) continue;
          try {
            const chunk = JSON.parse(raw);
            if (chunk.type === 'stdout') {
              stdoutLines.push(chunk.line);
            } else if (chunk.type === 'stderr') {
              stderrLines.push(chunk.line);
            } else if (chunk.type === 'status') {
              setStreamLines((prev) => {
                const last = prev[prev.length - 1];
                if (last?.type === 'status') return [...prev.slice(0, -1), { type: 'status', text: chunk.message }];
                return [...prev, { type: 'status', text: chunk.message }];
              });
            } else if (chunk.type === 'error') {
              stderrLines.push(chunk.message);
            } else if (chunk.type === 'done') {
              returncode = chunk.returncode;
            }
          } catch { /* ignore parse errors */ }
        }
      }

      await new Promise((resolve) => {
        if (stdoutLines.length === 0) { resolve(); return; }
        stdoutLines.forEach((line, i) => {
          setTimeout(() => {
            setStreamLines((prev) => [...prev, { type: 'stdout', text: line }]);
            if (i === stdoutLines.length - 1) resolve();
          }, i * 800);
        });
      });
      stderrLines.forEach((line) => {
        setStreamLines((prev) => [...prev, { type: 'stderr', text: line }]);
      });

      setOutput({ stdout: stdoutLines.join('\n'), stderr: stderrLines.join('\n'), returncode, passed: returncode === 0 });
      setLastRunTime(new Date().toLocaleTimeString('ko-KR', { hour: '2-digit', minute: '2-digit' }));
    } catch (err) {
      setOutput({ stdout: '', stderr: String(err), returncode: 1, passed: false });
    } finally {
      stopTimer();
      setRunning(false);
    }
  };

  const submit = async () => {
    if (!output) {
      alert('먼저 실행 버튼으로 코드를 실행해주세요.');
      return;
    }
    setSubmitting(true);
    try {
      const token = localStorage.getItem('accessToken');
      const res = await fetch(`${API_BASE}/mission/submit`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(token && { Authorization: `Bearer ${token}` }),
        },
        body: JSON.stringify({
          track: config.apiName,
          blanks: answers,
          stdout: output.stdout,
          stderr: output.stderr,
          returncode: output.returncode,
        }),
      });
      const data = await res.json();
      setOutput(data);
      setLastRunTime(new Date().toLocaleTimeString('ko-KR', { hour: '2-digit', minute: '2-digit' }));
      setSubmitResult(data.passed ? 'passed' : 'failed');
      if (data.passed) {
        setSubmitData(data);
        setShowSuccessModal(true);
      }
    } catch (err) {
      setOutput({ stdout: '', stderr: String(err), returncode: 1, passed: false });
    } finally {
      setSubmitting(false);
    }
  };

  const reset = () => {
    setAnswers({});
    setOutput(null);
    setSubmitResult(null);
    setLastRunTime(null);
  };

  const useHint = async () => {
    if (!confirmHint) return;
    try {
      const token = localStorage.getItem('accessToken');
      const res = await fetch(`${API_BASE}/mission/hint`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(token && { Authorization: `Bearer ${token}` }),
        },
        body: JSON.stringify({ track: config.apiName, todoId: confirmHint.todoId }),
      });
      if (!res.ok) throw new Error('힌트 요청 실패');
      setOpenedHints((prev) =>
        prev.includes(confirmHint.todoId) ? prev : [...prev, confirmHint.todoId],
      );
      setConfirmHint(null);
      setShowHintList(true);
    } catch (err) {
      console.error(err);
      setConfirmHint(null);
      alert('힌트 요청 중 오류가 발생했습니다.');
    }
  };

  const renderCode = () => {
    if (!template) return null;
    const lines = template.split('\n');
    return lines.map((line, lineIdx) => {
      const parts = line.split(/({{.*?}})/g);
      const isComment = line.trimStart().startsWith('#');
      return (
        <div key={lineIdx} className="code-line">
          <span className="line-num">{lineIdx + 1}</span>
          <span className={`line-content${isComment ? ' code-comment' : ''}`}>
            {parts.map((part, i) => {
              const match = part.match(/{{(.*?)}}/);
              if (!match) return <span key={i}>{part}</span>;
              const key = match[1];
              return (
                <input
                  key={`${key}-${i}`}
                  className="mission-blank"
                  value={answers[key] || ''}
                  placeholder={key}
                  spellCheck={false}
                  style={{ width: `${Math.max((answers[key] || key).length + 2, 4)}ch` }}
                  onChange={(e) =>
                    setAnswers((prev) => ({ ...prev, [key]: e.target.value }))
                  }
                />
              );
            })}
          </span>
        </div>
      );
    });
  };

  const outputStatus = output
    ? output.returncode === 0
      ? 'ok'
      : 'err'
    : 'idle';

  if (!mission) return null;

  return (
    <div className="mission-page">
      <div className="mission-topbar">
        <button
          className="mission-back-btn"
          onClick={() => navigate(`/tracks/${trackId}/chapters`)}
        >
          ←
        </button>
        <div className="mission-topbar-title">
          🏆 Mission. {config.title}
        </div>
        <div className="mission-topbar-meta">
          <span className="meta-chip meta-chip-orange">{config.chapterRange}</span>
          <span className="meta-chip meta-chip-purple">{config.tech}</span>
          <span className="meta-blank-counter">
            <span
              className={`counter-dot ${filledCount === totalBlanks && totalBlanks > 0 ? 'done' : ''}`}
            />
            {filledCount} / {totalBlanks}
          </span>
          <span className="meta-xp">⚡ +{config.xp} XP</span>
        </div>
      </div>

      <div className="mission-body">
        <div className="mission-left" style={{ width: leftWidth, minWidth: leftWidth }}>
          <div className="mission-markdown-body">
            <ReactMarkdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeRaw]}>
              {markdown}
            </ReactMarkdown>
          </div>
        </div>

        <div className="mission-resizer" onMouseDown={onResizerMouseDown} />

        <div className="mission-right">
          <div className="mission-editor">
            <div className="mission-editor-header">
              <div className="editor-dots">
                <span /><span /><span />
              </div>
              <span className="editor-filename">main.py</span>
              <span className="editor-blank-counter">
                <span className={`counter-dot ${filledCount === totalBlanks && totalBlanks > 0 ? 'done' : ''}`} />
                {filledCount} / {totalBlanks}
              </span>
              <span className="editor-lang">Python 3 · PyTorch</span>
            </div>
            <div className="mission-editor-body">
              <div className="mission-code-block">{renderCode()}</div>
            </div>
          </div>

          <div className="mission-v-resizer" onMouseDown={onVResizerMouseDown} />

          <div className="mission-output" style={{ height: outputHeight }}>
            <div className="mission-output-header">
              <span className={`output-dot output-dot-${outputStatus}`} />
              <span className="output-label">출력</span>
              <span className="output-divider">|</span>
              <span className="output-time">
                마지막 실행: {lastRunTime ?? '—'}
              </span>
            </div>
            <div className="mission-output-body">
              {streamLines.length > 0 ? (
                <div className="stream-output">
                  {streamLines.map((item, i) => (
                    <div key={i} className={`stream-line stream-line-${item.type}`}>
                      {item.text}
                    </div>
                  ))}
                </div>
              ) : submitting ? (
                <span className="output-placeholder">채점 중... GPU에서 코드를 실행하고 있습니다 ({elapsed}s)</span>
              ) : running ? (
                <span className="output-placeholder">GPU 연결 중... {elapsed}s</span>
              ) : output ? (
                <>
                  {output.stdout && <pre className="output-stdout">{output.stdout}</pre>}
                  {output.stderr && <pre className="output-stderr">{output.stderr}</pre>}
                  {!output.stdout && !output.stderr && <span className="output-empty">출력 없음</span>}
                </>
              ) : (
                <span className="output-placeholder">실행 버튼을 눌러 코드를 실행하세요.</span>
              )}
            </div>
          </div>
        </div>
      </div>

      <div className="mission-bottombar">
        <div className="mission-btn-group">
          <button
            className="mission-btn btn-run"
            onClick={run}
            disabled={running || submitting}
          >
            ▶ {running ? `실행 중... ${elapsed}s` : '실행'}
          </button>
          <button
            className="mission-btn btn-submit"
            onClick={submit}
            disabled={running || submitting}
          >
            {submitting ? `제출 중... ${elapsed}s` : '제출'}
          </button>
          {hints.length > 0 && (
            <button
              className="mission-btn btn-hint"
              onClick={() => setShowHintList(true)}
              disabled={running || submitting}
            >
              💡 힌트
            </button>
          )}
          <button
            className="mission-btn btn-reset"
            onClick={reset}
            disabled={running || submitting}
          >
            ↺ 초기화
          </button>
        </div>

        <div className="mission-bottombar-right">
          {submitResult && (
            <span
              className={`submit-badge ${submitResult === 'passed' ? 'pass' : 'fail'}`}
            >
              {submitResult === 'passed' ? '🎉 통과!' : '😢 미통과'}
            </span>
          )}
          <button
            className={`mission-btn btn-back-chapter ${submitResult === 'passed' ? 'active' : ''}`}
            onClick={() => navigate(`/tracks/${trackId}/chapters`)}
            disabled={submitResult !== 'passed'}
          >
            챕터로 돌아가기
          </button>
        </div>
      </div>

      {showHintList && (
        <div className="hint-overlay" onClick={() => setShowHintList(false)}>
          <div className="hint-list-popup" onClick={(e) => e.stopPropagation()}>
            <div className="hint-list-header">
              <span>💡 힌트 목록</span>
              <button className="hint-close" onClick={() => setShowHintList(false)}>✕</button>
            </div>
            <div className="hint-list-body">
              {hints.map((hint) => {
                const opened = openedHints.includes(hint.todoId);
                return (
                  <div key={hint.todoId} className={`hint-list-item ${opened ? 'opened' : ''}`}>
                    <div className="hint-list-item-top">
                      <span className="hint-todo-tag">TODO {hint.todoId}</span>
                      <span className="hint-xp-cost">-{hint.xpCost} XP</span>
                      {!opened && (
                        <button
                          className="hint-use-btn"
                          onClick={() => {
                            setShowHintList(false);
                            setConfirmHint(hint);
                          }}
                        >
                          사용하기
                        </button>
                      )}
                    </div>
                    {opened && (
                      <div className="hint-list-item-text">{hint.text}</div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      )}

      {confirmHint && (
        <div className="hint-overlay" onClick={() => setConfirmHint(null)}>
          <div className="hint-confirm-modal" onClick={(e) => e.stopPropagation()}>
            <div className="hint-confirm-title">💡 힌트를 사용하시겠습니까?</div>
            <div className="hint-confirm-desc">
              TODO {confirmHint.todoId} 힌트를 사용합니다.
              <br />
              ⚠️ {confirmHint.xpCost}XP가 차감됩니다.
            </div>
            <div className="hint-confirm-actions">
              <button className="hint-cancel-btn" onClick={() => setConfirmHint(null)}>
                취소
              </button>
              <button className="hint-use-btn" onClick={useHint}>
                사용하기
              </button>
            </div>
          </div>
        </div>
      )}

      {showSuccessModal && submitData && (
        <div className="mission-success-overlay">
          <div className="mission-success-modal">
            {submitData.isFirstCompletion ? (
              <>
                <div className="mission-success-title">미션 완료!</div>
                <div className="mission-success-xp">+{submitData.xpEarned} XP</div>
              </>
            ) : (
              <div className="mission-success-title">미션 복습 완료!</div>
            )}
            <button
              className="mission-success-btn"
              onClick={() => setShowSuccessModal(false)}
            >
              닫기
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
