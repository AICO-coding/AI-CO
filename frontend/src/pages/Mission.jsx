import { useEffect, useState, useRef, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeRaw from 'rehype-raw';
import '../styles/Mission.css';

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
  regression: {
    apiName: 'ML-회귀',
    title: '캘리포니아 집값 예측',
    chapterRange: 'Ch1~Ch5 종합',
    tech: 'PyTorch 완전 구현',
    xp: 150,
    jsonUrl: '/static/md/regression/mission/mission.json',
    mdFallback: '/static/md/regression/mission/misson.md',
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

const API_BASE = 'http://210.125.96.59:8000';

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
  const [submitResult, setSubmitResult] = useState(null);
  const [lastRunTime, setLastRunTime] = useState(null);
  const [hintIndex, setHintIndex] = useState(0);
  const [showHint, setShowHint] = useState(false);
  const [leftWidth, setLeftWidth] = useState(360);
  const dragging = useRef(false);
  const dragStartX = useRef(0);
  const dragStartWidth = useRef(0);

  const onResizerMouseDown = useCallback((e) => {
    dragging.current = true;
    dragStartX.current = e.clientX;
    dragStartWidth.current = leftWidth;
    document.body.style.cursor = 'col-resize';
    document.body.style.userSelect = 'none';
  }, [leftWidth]);

  useEffect(() => {
    const onMouseMove = (e) => {
      if (!dragging.current) return;
      const delta = e.clientX - dragStartX.current;
      const next = Math.min(Math.max(dragStartWidth.current + delta, 200), 700);
      setLeftWidth(next);
    };
    const onMouseUp = () => {
      dragging.current = false;
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
        if (fallback.ok) setMarkdown(await fallback.text());
      } catch (err) {
        console.error('미션 로드 실패', err);
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
    try {
      const token = localStorage.getItem('accessToken');
      const res = await fetch(`${API_BASE}/mission/run`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(token && { Authorization: `Bearer ${token}` }),
        },
        body: JSON.stringify({ track: config.apiName, blanks: answers }),
      });
      const data = await res.json();
      setOutput(data);
      setLastRunTime(new Date().toLocaleTimeString('ko-KR', { hour: '2-digit', minute: '2-digit' }));
    } catch (err) {
      setOutput({ stdout: '', stderr: String(err), returncode: 1, passed: false });
    } finally {
      setRunning(false);
    }
  };

  const submit = async () => {
    setSubmitting(true);
    setOutput(null);
    try {
      const token = localStorage.getItem('accessToken');
      const res = await fetch(`${API_BASE}/mission/submit`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(token && { Authorization: `Bearer ${token}` }),
        },
        body: JSON.stringify({ track: config.apiName, blanks: answers }),
      });
      const data = await res.json();
      setOutput(data);
      setLastRunTime(new Date().toLocaleTimeString('ko-KR', { hour: '2-digit', minute: '2-digit' }));
      setSubmitResult(data.passed ? 'passed' : 'failed');
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

  const openHint = () => {
    setShowHint(true);
  };

  const cycleHint = (dir) => {
    setHintIndex((prev) => (prev + dir + hints.length) % hints.length);
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

  const currentHint = hints[hintIndex];

  return (
    <div className="mission-page">
      {/* Top bar */}
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

      {/* Body */}
      <div className="mission-body">
        {/* Left: Markdown */}
        <div className="mission-left" style={{ width: leftWidth, minWidth: leftWidth }}>
          <div className="mission-markdown-body">
            <ReactMarkdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeRaw]}>
              {markdown}
            </ReactMarkdown>
          </div>
        </div>

        {/* Resizer */}
        <div className="mission-resizer" onMouseDown={onResizerMouseDown} />

        {/* Right: Editor + Output */}
        <div className="mission-right">
          <div className="mission-editor">
            <div className="mission-editor-header">
              <div className="editor-dots">
                <span /><span /><span />
              </div>
              <span className="editor-filename">main.py</span>
              <span className="editor-lang">Python 3 · PyTorch</span>
            </div>
            <div className="mission-editor-body">
              <div className="mission-code-block">{renderCode()}</div>
            </div>
          </div>

          <div className="mission-output">
            <div className="mission-output-header">
              <span className={`output-dot output-dot-${outputStatus}`} />
              <span className="output-label">출력</span>
              <span className="output-divider">|</span>
              <span className="output-time">
                마지막 실행: {lastRunTime ?? '—'}
              </span>
            </div>
            <div className="mission-output-body">
              {output ? (
                <>
                  {output.stdout && (
                    <pre className="output-stdout">{output.stdout}</pre>
                  )}
                  {output.stderr && (
                    <pre className="output-stderr">{output.stderr}</pre>
                  )}
                  {!output.stdout && !output.stderr && (
                    <span className="output-empty">출력 없음</span>
                  )}
                </>
              ) : (
                <span className="output-placeholder">
                  실행 버튼을 눌러 코드를 실행하세요.
                </span>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Bottom bar */}
      <div className="mission-bottombar">
        <div className="mission-btn-group">
          <button
            className="mission-btn btn-run"
            onClick={run}
            disabled={running || submitting}
          >
            ▶ {running ? '실행 중...' : '실행'}
          </button>
          <button
            className="mission-btn btn-submit"
            onClick={submit}
            disabled={running || submitting}
          >
            {submitting ? '제출 중...' : '제출 →'}
          </button>
          {hints.length > 0 && (
            <button
              className="mission-btn btn-hint"
              onClick={openHint}
              disabled={running || submitting}
            >
              💡 힌트 (-{currentHint?.xpCost ?? 10} XP)
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
          <span className="bottom-blank-counter">
            {filledCount} / {totalBlanks}
          </span>
        </div>
      </div>

      {/* Hint overlay */}
      {showHint && currentHint && (
        <div className="hint-overlay" onClick={() => setShowHint(false)}>
          <div className="hint-popup" onClick={(e) => e.stopPropagation()}>
            <div className="hint-popup-header">
              <span className="hint-todo-tag">TODO {currentHint.todoId}</span>
              <span className="hint-xp-cost">-{currentHint.xpCost} XP</span>
              <button className="hint-close" onClick={() => setShowHint(false)}>✕</button>
            </div>
            <div className="hint-popup-body">{currentHint.text}</div>
            {hints.length > 1 && (
              <div className="hint-popup-nav">
                <button onClick={() => cycleHint(-1)}>← 이전</button>
                <span>{hintIndex + 1} / {hints.length}</span>
                <button onClick={() => cycleHint(1)}>다음 →</button>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
