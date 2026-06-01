import {
  useEffect,
  useMemo,
  useState,
} from "react";

import {
  useParams,
  useNavigate,
} from "react-router-dom";

import LessonRenderer from "../components/lesson/LessonRenderer";

import "../styles/Lesson.css";

export default function Lesson() {

  const { trackId, chapterId } =
    useParams();

  const navigate = useNavigate();

  const [lessons, setLessons] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState(null);

  const [currentIndex, setCurrentIndex] =
    useState(0);

  const [submitHandler, setSubmitHandler] =
    useState(null);

  useEffect(() => {

    const fetchLessons = async () => {

      try {

        setLoading(true);

        const token =
          localStorage.getItem("accessToken");

        const res = await fetch(
          `http://210.125.96.59:8000/tracks/${trackId}/chapters/${chapterId}/lessons`,
          {
            headers: {
              ...(token && {
                Authorization: `Bearer ${token}`,
              }),
            },
          }
        );

        if (!res.ok) {
          throw new Error(`HTTP ${res.status}`);
        }

        const data = await res.json();

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
    return [...lessons].sort(
      (a, b) => a.orderIndex - b.orderIndex
    );
  }, [lessons]);

  const lesson = sortedLessons[currentIndex];
  const completeLesson = async (lessonId) => {

    try {

      const token =
        localStorage.getItem("accessToken");

      await fetch(
        `http://210.125.96.59:8000/tracks/${trackId}/chapters/${chapterId}/lessons/${lessonId}/complete`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            ...(token && {
              Authorization: `Bearer ${token}`,
            }),
          },
        }
      );

    } catch (err) {
      console.error(err);
    }
  };

  const goToLesson = async (targetIndex) => {

    if (
      targetIndex < 0 ||
      targetIndex >= sortedLessons.length
    ) return;

    if (
      lesson?.lessonType === "code_fill" ||
      lesson?.lessonType === "multiple_choice"
    ) {

      if (!submitHandler) {
        alert("제출 함수를 찾을 수 없습니다.");
        return;
      }

      const success = await submitHandler();
      if (!success) return;

    } else {

      if (lesson?.lessonId) {
        await completeLesson(lesson.lessonId);
      }
    }

    setCurrentIndex(targetIndex);
  };

  const finishChapter = async () => {

    try {

      const token =
        localStorage.getItem("accessToken");
      if (
        lesson?.lessonType === "code_fill" ||
        lesson?.lessonType === "multiple_choice"
      ) {

        if (!submitHandler) {
          alert("제출 함수를 찾을 수 없습니다.");
          return;
        }

        const success = await submitHandler();
        if (!success) return;

      } else {

        if (lesson?.lessonId) {
          await completeLesson(lesson.lessonId);
        }
      }

      const res = await fetch(
        `http://210.125.96.59:8000/tracks/${trackId}/chapters/${chapterId}/complete`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            ...(token && {
              Authorization: `Bearer ${token}`,
            }),
          },
        }
      );

      if (!res.ok) {
        throw new Error(`HTTP ${res.status}`);
      }

      navigate(`/tracks/${trackId}/chapters`);

    } catch (err) {
      console.error(err);
      alert("챕터 완료 처리 중 오류가 발생했습니다.");
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
    return <div className="lesson-page">Loading...</div>;
  }

  if (error) {
    return <div className="lesson-page">Error: {error}</div>;
  }

  if (!lesson) {
    return <div className="lesson-page">Lesson Not Found</div>;
  }

  const isLastLesson =
    currentIndex === sortedLessons.length - 1;

  return (
    <div className="lesson-page">

      <div className="lesson-topbar">

        <button
          className="nav-btn nav-btn-secondary"
          onClick={goBack}
        >
          📚 챕터로
        </button>

        <div>{chapterId}</div>
        <div>{lesson.title}</div>
        <div>{lesson.lessonType}</div>

      </div>
      <div className="lesson-page-content">

        <LessonRenderer
          lesson={lesson}
          registerSubmit={setSubmitHandler}
        />

      </div>

      <div className="lesson-bottombar">

        <button
          className="nav-btn"
          onClick={() =>
            setCurrentIndex(currentIndex - 1)
          }
          disabled={currentIndex === 0}
        >
          ← 이전
        </button>

        {isLastLesson ? (

          <button
            className="nav-btn primary"
            onClick={finishChapter}
          >
            챕터 완료
          </button>

        ) : (

          <button
            className="nav-btn primary"
            onClick={() =>
              goToLesson(currentIndex + 1)
            }
          >
            다음 →
          </button>

        )}

      </div>

    </div>
  );
}