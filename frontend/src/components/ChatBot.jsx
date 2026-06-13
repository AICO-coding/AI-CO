import { useState, useEffect, useRef } from 'react';
import '../styles/ChatBot.css';
import cobotImg from '../assets/cobot.png';
import cobotThinkingImg from '../assets/cobot_thinking.png';
import { API_BASE_URL } from '../config/api';

const CONCEPT_TYPES = ['concept_image', 'concept_code', 'parameter'];
const API_BASE = API_BASE_URL;

export default function ChatBot({ track, chapter, lessonType }) {
  const [isOpen, setIsOpen] = useState(false);
  const [isVisible, setIsVisible] = useState(true);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [historyLoaded, setHistoryLoaded] = useState(false);
  const messagesEndRef = useRef(null);

  const isConceptLesson = CONCEPT_TYPES.includes(lessonType);

  useEffect(() => {
    if (!isOpen || historyLoaded) return;

    const fetchHistory = async () => {
      try {
        const token = localStorage.getItem('accessToken');
        const res = await fetch(`${API_BASE}/chat/history`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        if (res.ok) {
          const data = await res.json();
          setMessages(
            data.messages.map((m) => ({ role: m.role, content: m.content })),
          );
        }
      } catch {
        // 기록 없으면 빈 상태로 시작
      }
      setHistoryLoaded(true);
    };

    fetchHistory();
  }, [isOpen, historyLoaded]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const userMessage = input.trim();
    setInput('');
    setMessages((prev) => [...prev, { role: 'user', content: userMessage }]);
    setLoading(true);

    try {
      const token = localStorage.getItem('accessToken');
      const res = await fetch(`${API_BASE}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ track, chapter, message: userMessage }),
      });

      if (res.ok) {
        const data = await res.json();
        setMessages((prev) => [
          ...prev,
          { role: 'assistant', content: data.reply },
        ]);
      } else {
        throw new Error('서버 오류');
      }
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: '오류가 발생했어요. 잠시 후 다시 시도해주세요.',
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  if (!isConceptLesson) return null;

  return (
    <div className="chatbot-wrapper">
      {isOpen && (
        <div className="chatbot-panel">
          <div className="chatbot-header">
            <img
              src={cobotImg}
              alt="코냥이"
              className="chatbot-header-avatar"
            />
            <div className="chatbot-header-info">
              <div className="chatbot-header-name">코냥이</div>
              <div className="chatbot-header-sub">궁금한 거 물어봐요!</div>
            </div>
            <button
              className="chatbot-close-btn"
              onClick={() => setIsOpen(false)}
            >
              ✕
            </button>
          </div>

          <div className="chatbot-messages">
            {messages.length === 0 && !loading && (
              <div className="chatbot-empty">
                <img
                  src={cobotImg}
                  alt="코냥이"
                  className="chatbot-empty-img"
                />
                <p>
                  지금 배우는 내용이 궁금하면
                  <br />
                  편하게 물어봐요!
                </p>
              </div>
            )}

            {messages.map((msg, i) => (
              <div key={i} className={`chatbot-message ${msg.role}`}>
                {msg.role === 'assistant' && (
                  <img
                    src={cobotImg}
                    alt="코냥이"
                    className="chatbot-msg-avatar"
                  />
                )}
                <div className="chatbot-bubble">{msg.content}</div>
              </div>
            ))}

            {loading && (
              <div className="chatbot-message assistant">
                <img
                  src={cobotThinkingImg}
                  alt="생각 중"
                  className="chatbot-msg-avatar chatbot-msg-avatar--thinking"
                />
                <div className="chatbot-bubble chatbot-typing">
                  <span />
                  <span />
                  <span />
                </div>
              </div>
            )}

            <div ref={messagesEndRef} />
          </div>

          <div className="chatbot-input-area">
            <textarea
              className="chatbot-input"
              placeholder="질문을 입력하세요... (Enter로 전송)"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              rows={1}
              disabled={loading}
            />
            <button
              className="chatbot-send-btn"
              onClick={sendMessage}
              disabled={!input.trim() || loading}
            >
              ↑
            </button>
          </div>
        </div>
      )}

      {isVisible ? (
        <button
          className={`chatbot-toggle-btn ${isOpen ? 'open' : ''}`}
          onClick={() => setIsOpen((prev) => !prev)}
          title="코냥이에게 질문하기"
        >
          <img
            src={isOpen ? cobotThinkingImg : cobotImg}
            alt="코냥이"
            className="chatbot-toggle-img"
          />
          {!isOpen && <span className="chatbot-toggle-label">코냥이</span>}
          {!isOpen && (
            <span
              className="chatbot-x-btn"
              onClick={(e) => {
                e.stopPropagation();
                setIsVisible(false);
                setIsOpen(false);
              }}
            >
              ✕
            </span>
          )}
        </button>
      ) : (
        <button
          className="chatbot-recall-btn"
          onClick={() => setIsVisible(true)}
          title="코냥이 열기"
        >
          <img src={cobotImg} alt="코냥이" className="chatbot-recall-img" />
        </button>
      )}
    </div>
  );
}
