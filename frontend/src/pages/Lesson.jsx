import { useEffect, useMemo, useState } from 'react';

import { useParams, useNavigate } from 'react-router-dom';

import LessonRenderer from '../components/lesson/LessonRenderer';
import ChatBot from '../components/ChatBot';

import '../styles/Lesson.css';

export default function Lesson() {
  const { trackId, chapterId } = useParams();

  const navigate = useNavigate();

  const [lessons, setLessons] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState(null);

  const [currentIndex, setCurrentIndex] = useState(0);

  const [submitHandler, setSubmitHandler] = useState(null);

  const [isSubmitted, setIsSubmitted] = useState(false);

  const [submitResult, setSubmitResult] = useState(null);

  const [chapterResult, setChapterResult] = useState(null);

  const [showResultModal, setShowResultModal] = useState(false);

  useEffect(() => {
    const fetchLessons = async () => {
      try {
        setLoading(true);

        const token = localStorage.getItem('accessToken');

        const res = await fetch(
          `http://210.125.96.59:8000/tracks/${trackId}/chapters/${chapterId}/lessons`,
          {
            headers: {
              ...(token && {
                Authorization: `Bearer ${token}`,
              }),
            },
          },
        );

        if (!res.ok) {
          throw new Error(`HTTP ${res.status}`);
        }

        const data = await res.json();

        console.log('[Lesson API response]', data);

        setLessons(data.lessons || []);
      } catch (err) {
        console.error(err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchLessons();
  }, [trackId, chapterId]);

  const sortedLessons = useMemo(() => {
    return [...lessons].sort((a, b) => a.orderIndex - b.orderIndex);
  }, [lessons]);

  const lesson = sortedLessons[currentIndex];

  useEffect(() => {
    setIsSubmitted(false);
    setSubmitResult(null);
  }, [currentIndex]);

  const completeLesson = async (lessonId) => {
    try {
      const token = localStorage.getItem('accessToken');

      await fetch(
        `http://210.125.96.59:8000/tracks/${trackId}/chapters/${chapterId}/lessons/${lessonId}/complete`,
        {
          method: 'POST',

          headers: {
            'Content-Type': 'application/json',

            ...(token && {
              Authorization: `Bearer ${token}`,
            }),
          },
        },
      );
    } catch (err) {
      console.error(err);
    }
  };

  const handleSubmit = async () => {
    if (!submitHandler) return;
    const success = await submitHandler();
    setSubmitResult(success ? 'correct' : 'wrong');
    if (success) setIsSubmitted(true);
  };

  const goToLesson = async (targetIndex) => {
    if (targetIndex < 0 || targetIndex >= sortedLessons.length) {
      return;
    }

    if (lesson?.lessonId) {
      await completeLesson(lesson.lessonId);
    }

    setCurrentIndex(targetIndex);
  };

  const finishChapter = async () => {
    try {
      if (
        (lesson?.lessonType === 'code_fill' ||
          lesson?.lessonType === 'multiple_choice') &&
        !isSubmitted
      ) {
        alert('먼저 제출해주세요.');

        return;
      }

      if (lesson?.lessonId) {
        await completeLesson(lesson.lessonId);
      }

      const token = localStorage.getItem('accessToken');

      const res = await fetch(
        `http://210.125.96.59:8000/tracks/${trackId}/chapters/${chapterId}/complete`,
        {
          method: 'POST',

          headers: {
            'Content-Type': 'application/json',

            ...(token && {
              Authorization: `Bearer ${token}`,
            }),
          },
        },
      );

      if (!res.ok) {
        throw new Error(`HTTP ${res.status}`);
      }

      const result = await res.json();

      setChapterResult(result);

      setShowResultModal(true);
    } catch (err) {
      console.error(err);

      alert('챕터 완료 처리 중 오류가 발생했습니다.');
    }
  };

  useEffect(() => {
    if (sortedLessons.length > 0) {
      setCurrentIndex(0);
    }
  }, [sortedLessons]);

  const goBack = () => {
    navigate(`/tracks/${trackId}/chapters`);
  };

  if (loading) {
    return null;
  }

  if (error) {
    return <div className="lesson-page">Error: {error}</div>;
  }

  if (!lesson) {
    return <div className="lesson-page">Lesson Not Found</div>;
  }

  const isLastLesson = currentIndex === sortedLessons.length - 1;

  const needsSubmit =
    lesson.lessonType === 'multiple_choice' ||
    lesson.lessonType === 'code_fill';

  return (
    <div className="lesson-page">
      <div className="lesson-topbar">
        <button className="nav-btn nav-btn-secondary" onClick={goBack}>
          📚 챕터로
        </button>

        <div>{chapterId}</div>
        <div>{lesson.title}</div>
        <div>{lesson.lessonType}</div>
      </div>

      <div className="lesson-page-content">
        <LessonRenderer lesson={lesson} registerSubmit={setSubmitHandler} />
      </div>

      <div className="lesson-bottombar">
        <button
          className="nav-btn"
          onClick={() => setCurrentIndex(currentIndex - 1)}
          disabled={currentIndex === 0}
        >
          ← 이전
        </button>

        <div
          style={{
            display: 'flex',
            gap: '12px',
          }}
        >
          {submitResult && (
            <div className={`submit-result ${submitResult}`}>
              {submitResult === 'correct' ? '🎉 정답!' : '😢 오답!'}
            </div>
          )}

          {needsSubmit && !isSubmitted && (
            <button className="nav-btn primary" onClick={handleSubmit}>
              제출하기
            </button>
          )}

          {isLastLesson ? (
            <button
              className="nav-btn primary"
              onClick={finishChapter}
              disabled={needsSubmit && !isSubmitted}
            >
              챕터 완료
            </button>
          ) : (
            <button
              className="nav-btn primary"
              onClick={() => goToLesson(currentIndex + 1)}
              disabled={needsSubmit && !isSubmitted}
            >
              다음
            </button>
          )}
        </div>
      </div>

      <ChatBot
        track={trackId}
        chapter={chapterId}
        lessonType={lesson.lessonType}
      />

      {showResultModal && chapterResult && (
        <div className="result-overlay">
          <div className="result-modal">
            <img
              src="/src/assets/cobot_complete.png"
              alt="코봇"
              className="result-cobot"
            />

            {chapterResult.isFirstCompletion ? (
              <>
                <div className="result-title">챕터 완료</div>

                <div className="result-xp">+{chapterResult.xpEarned} XP</div>

                <div className="result-detail">
                  힌트 사용 : {chapterResult.hintUsed}회
                </div>

                <div className="result-detail">
                  정답 공개 : {chapterResult.revealUsed}회
                </div>
              </>
            ) : (
              <>
                <div className="result-title">복습 완료</div>
              </>
            )}

            <button
              className="result-btn"
              onClick={() => navigate(`/tracks/${trackId}/chapters`)}
            >
              확인
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
