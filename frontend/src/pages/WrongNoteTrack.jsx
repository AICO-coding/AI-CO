import { useEffect, useState, useMemo, useRef } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import WrongNoteItem from '../components/WrongNoteItem';
import '../styles/WrongNote.css';

const API_BASE = 'http://210.125.96.59:8000';

const PROBLEM_TYPE_LABEL = {
  multiple_choice: '객관식',
  code_fill: '코드 빈칸',
  parameter: '파라미터',
};

const WEEKDAYS = ['일', '월', '화', '수', '목', '금', '토'];
const MONTHS = [
  '1월',
  '2월',
  '3월',
  '4월',
  '5월',
  '6월',
  '7월',
  '8월',
  '9월',
  '10월',
  '11월',
  '12월',
];

function formatDate(year, month, day) {
  return `${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
}

export default function WrongNoteTrack() {
  const { trackId } = useParams();
  const navigate = useNavigate();

  const isDaily = trackId === 'daily';
  const trackName = isDaily ? '데일리 퀴즈' : trackId.toUpperCase();

  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  const today = new Date();
  const [currentYear, setCurrentYear] = useState(today.getFullYear());
  const [currentMonth, setCurrentMonth] = useState(today.getMonth());
  const [selectedDate, setSelectedDate] = useState(null);
  const resultRef = useRef(null);

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    const params = new URLSearchParams();
    if (isDaily) {
      params.set('source_type', 'daily');
    } else {
      params.set('source_type', 'learning');
      params.set('track', trackName);
    }

    fetch(`${API_BASE}/wrong-answers?${params.toString()}`, {
      headers: token ? { Authorization: `Bearer ${token}` } : {},
    })
      .then((r) => r.json())
      .then((data) => setItems(data.wrongAnswers ?? []))
      .catch(() => setItems([]))
      .finally(() => setLoading(false));
  }, [trackId]);

  const dateMap = useMemo(() => {
    const map = {};
    for (const item of items) {
      const key = item.date ?? '날짜 없음';
      if (!map[key]) map[key] = [];
      map[key].push(item);
    }
    return map;
  }, [items]);

  const calendarDays = useMemo(() => {
    const firstDay = new Date(currentYear, currentMonth, 1).getDay();
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
    const days = [];
    for (let i = 0; i < firstDay; i++) days.push(null);
    for (let d = 1; d <= daysInMonth; d++) days.push(d);
    return days;
  }, [currentYear, currentMonth]);

  function prevMonth() {
    if (currentMonth === 0) {
      setCurrentYear((y) => y - 1);
      setCurrentMonth(11);
    } else setCurrentMonth((m) => m - 1);
    setSelectedDate(null);
  }

  function nextMonth() {
    if (currentMonth === 11) {
      setCurrentYear((y) => y + 1);
      setCurrentMonth(0);
    } else setCurrentMonth((m) => m + 1);
    setSelectedDate(null);
  }

  function handleDayClick(day) {
    const dateStr = formatDate(currentYear, currentMonth, day);
    setSelectedDate((prev) => (prev === dateStr ? null : dateStr));
    setTimeout(() => {
      resultRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 50);
  }

  function handleDelete(deletedId) {
    setItems((prev) => prev.filter((i) => i.id !== deletedId));
  }

  async function handleRowDelete(id) {
    const token = localStorage.getItem('accessToken');
    try {
      await fetch(`${API_BASE}/wrong-answers/${id}`, {
        method: 'DELETE',
        headers: token ? { Authorization: `Bearer ${token}` } : {},
      });
      handleDelete(id);
    } catch {}
  }

  const selectedItems = selectedDate ? (dateMap[selectedDate] ?? []) : [];
  const todayStr = formatDate(
    today.getFullYear(),
    today.getMonth(),
    today.getDate(),
  );

  return (
    <div className="page-container">
      <div className="wrong-note-header">
        <button className="back-btn" onClick={() => navigate('/wrong-answer')}>
          목록으로
        </button>
        <h2 className="title">{trackName} 오답</h2>
        <button
          className="review-btn"
          onClick={() => navigate(`/wrong-answer/${trackId}/review`)}
        >
          복습하기
        </button>
      </div>

      {!loading && isDaily ? (
        <>
          <div className="wn-calendar">
            <div className="wn-cal-header">
              <button className="wn-cal-nav" onClick={prevMonth}>
                ‹
              </button>
              <span className="wn-cal-title">
                {currentYear}년 {MONTHS[currentMonth]}
              </span>
              <button className="wn-cal-nav" onClick={nextMonth}>
                ›
              </button>
            </div>

            <div className="wn-cal-grid">
              {WEEKDAYS.map((w) => (
                <div key={w} className="wn-cal-weekday">
                  {w}
                </div>
              ))}
              {calendarDays.map((day, idx) => {
                if (!day)
                  return (
                    <div key={`empty-${idx}`} className="wn-cal-day empty" />
                  );

                const dateStr = formatDate(currentYear, currentMonth, day);
                const hasItems = !!dateMap[dateStr]?.length;
                const count = dateMap[dateStr]?.length ?? 0;
                const isSelected = dateStr === selectedDate;
                const isToday = dateStr === todayStr;

                return (
                  <div
                    key={dateStr}
                    className={[
                      'wn-cal-day',
                      hasItems ? 'has-items' : '',
                      isSelected ? 'selected' : '',
                      isToday ? 'today' : '',
                    ]
                      .filter(Boolean)
                      .join(' ')}
                    onClick={() => handleDayClick(day)}
                  >
                    <span className="wn-cal-day-num">{day}</span>
                    {hasItems && <span className="wn-cal-badge">{count}</span>}
                  </div>
                );
              })}
            </div>

            {items.length === 0 && (
              <p className="wn-cal-empty">아직 데일리 오답이 없습니다.</p>
            )}
          </div>

          {selectedDate && (
            <div className="wn-daily-group" ref={resultRef}>
              <div className="wn-daily-date-header">
                <span className="wn-daily-date-icon">📅</span>
                {selectedDate}
                <span className="wn-daily-date-count">
                  {selectedItems.length}문제
                </span>
              </div>
              {selectedItems.length === 0 ? (
                <div
                  className="empty-message"
                  style={{ borderRadius: 0, border: 'none' }}
                >
                  이 날짜의 오답이 없습니다.
                </div>
              ) : (
                selectedItems.map((item) => (
                  <div
                    key={item.id}
                    className="wn-daily-row"
                    onClick={() => navigate(`/wrong-answer/${trackId}/${item.id}`)}
                  >
                    <div className="wn-daily-row-left">
                      <div className="wn-daily-row-meta">
                        {item.track && (
                          <span className="track-badge">{item.track}</span>
                        )}
                        {item.chapter && (
                          <span className="wn-daily-chapter-text">
                            {item.chapter}
                            {item.title && <span className="wrong-card-subtitle"> · {item.title}</span>}
                          </span>
                        )}
                      </div>
                      <span className="wn-daily-type-badge">
                        {PROBLEM_TYPE_LABEL[item.problemType] ?? item.problemType}
                      </span>
                    </div>
                    <div className="wn-daily-row-right">
                      <span className={item.isResolved ? 'status resolved' : 'status unresolved'}>
                        {item.isResolved ? '해결완료' : '미해결'}
                      </span>
                      <button
                        className="wn-daily-delete-btn"
                        onClick={(e) => { e.stopPropagation(); handleRowDelete(item.id); }}
                      >
                        ✕
                      </button>
                    </div>
                  </div>
                ))
              )}
            </div>
          )}
        </>
      ) : (
        <div className="list">
          {items.length > 0 ? (
            items.map((item) => (
              <WrongNoteItem
                key={item.id}
                item={item}
                trackId={trackId}
                onDelete={handleDelete}
              />
            ))
          ) : (
            <div className="empty-message">이 트랙의 오답이 없습니다.</div>
          )}
        </div>
      )}
    </div>
  );
}
