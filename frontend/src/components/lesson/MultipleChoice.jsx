import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import "../../styles/MultipleChoice.css";

export default function MultipleChoice({
  lesson,
  registerSubmit,
}) {

  const { trackId, chapterId } =
    useParams();

  const [selected, setSelected] =
    useState(null);

  const [isCorrect, setIsCorrect] =
    useState(null);

  const [submitting, setSubmitting] =
  useState(false);

  const [openedHints, setOpenedHints] =
    useState([]);

  const [confirmHint, setConfirmHint] =
    useState(null);

  const [blockedHintLevel, setBlockedHintLevel] =
    useState(null);

  const [confirmReveal, setConfirmReveal] =
    useState(false);

  const [revealedAnswer, setRevealedAnswer] =
    useState(null);

  useEffect(() => {

    setSelected(null);
    setIsCorrect(null);
    setSubmitting(false);
    setOpenedHints([]);
    setConfirmHint(null);
    setBlockedHintLevel(null);
    setConfirmReveal(false);
    setRevealedAnswer(null);

  }, [lesson.lessonId]);

  useEffect(() => {

    registerSubmit?.(
      () => submitAnswer
    );

  }, [selected, lesson]);

  const useHint = async () => {

    if (!confirmHint) return;

    try {

      const token =
        localStorage.getItem(
          "accessToken"
        );

      const res = await fetch(
        `http://210.125.96.59:8000/tracks/${trackId}/chapters/${chapterId}/hint`,
        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json",

            ...(token && {
              Authorization:
                `Bearer ${token}`,
            }),
          },

          body: JSON.stringify({
            problemId:
              lesson.problemId,

            hintLevel:
              confirmHint.level,
          }),
        }
      );

      if (!res.ok) {
        throw new Error(
          "힌트 요청 실패"
        );
      }

      setOpenedHints([
        ...openedHints,
        confirmHint.level,
      ]);

      setConfirmHint(null);

    } catch (err) {

      console.error(err);

      alert(
        "힌트 요청 중 오류가 발생했습니다."
      );
    }
  };

const revealAnswer = async () => {

  try {

    const token =
      localStorage.getItem(
        "accessToken"
      );

    const res = await fetch(
      `http://210.125.96.59:8000/tracks/${trackId}/chapters/${chapterId}/lessons/${lesson.lessonId}/reveal`,
      {
        method: "POST",

        headers: {
          "Content-Type":
            "application/json",

          ...(token && {
            Authorization:
              `Bearer ${token}`,
          }),
        },

        body: JSON.stringify({
          problemId:
            lesson.problemId,
        }),
      }
    );

    if (!res.ok) {
      throw new Error(
        "정답 공개 실패"
      );
    }

    const data =
      await res.json();

    console.log(
      "✅ REVEAL RESULT:",
      data
    );

    setRevealedAnswer(
      data.answer.correct_index
    );

    setConfirmReveal(false);

  } catch (err) {

    console.error(err);

    alert(
      "정답 공개 중 오류가 발생했습니다."
    );
  }
};

  const submitAnswer = async () => {

    if (selected === null) {

      alert(
        "선택지를 선택해주세요."
      );

      return false;
    }

    try {

      setSubmitting(true);

      const token =
        localStorage.getItem(
          "accessToken"
        );

      const res = await fetch(
        `http://210.125.96.59:8000/tracks/${trackId}/chapters/${chapterId}/submit`,
        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json",

            ...(token && {
              Authorization:
                `Bearer ${token}`,
            }),
          },

          body: JSON.stringify({
            lessonId:
              lesson.lessonId,

            problemId:
              lesson.problemId,

            answer:
              selected + 1,
          }),
        }
      );

      if (!res.ok) {
        throw new Error(
          "답안 제출 실패"
        );
      }

      const data =
        await res.json();

      console.log(
        "✅ SUBMIT RESULT:",
        data
      );

      setIsCorrect(
        data.isCorrect
      );

      return data.isCorrect;

    } catch (err) {

      console.error(err);

      alert(
        "답안 제출 중 오류가 발생했습니다."
      );

      return false;

    } finally {

      setSubmitting(false);
    }
  };

  return (
    <div className="quiz-layout">
      <div className="quiz-left">

        <div className="quiz-info-card">

          <div className="quiz-label">
            MULTIPLE CHOICE
          </div>

          <div className="quiz-title">
            {lesson.title}
          </div>

          <div className="quiz-desc">
            정답이라고 생각하는
            선택지를 하나 고르세요.
          </div>

        </div>
        <div className="quiz-hint-group">

          {lesson.hints?.map(
            (hint) => {

              const opened =
                openedHints.includes(
                  hint.level
                );

              const canOpen =
                hint.level === 1 ||
                openedHints.includes(
                  hint.level - 1
                );

              return (
                <div
                  key={hint.level}
                  className={`quiz-hint-dropdown ${
                    opened
                      ? "open"
                      : ""
                  }`}
                >

                  <button
                    className={`quiz-hint-toggle ${
                      !canOpen
                        ? "disabled"
                        : ""
                    }`}
                    onClick={() => {

                      if (!canOpen) {

                        setBlockedHintLevel(
                          hint.level - 1
                        );

                        return;
                      }

                      if (opened) {

                        setOpenedHints(
                          openedHints.filter(
                            (
                              level
                            ) =>
                              level !==
                              hint.level
                          )
                        );

                        return;
                      }

                      setConfirmHint(
                        hint
                      );
                    }}
                  >

                    <span>
                      💡 Hint Level{" "}
                      {hint.level}
                    </span>

                    <span className="quiz-hint-arrow">
                      {opened
                        ? "−"
                        : "+"}
                    </span>

                  </button>

                  {opened && (

                    <div className="quiz-hint-content">
                      {hint.text}
                    </div>

                  )}

                </div>
              );
            }
          )}
            <div
              className={`quiz-hint-dropdown ${
                revealedAnswer !== null
                  ? "open"
                  : ""
              }`}
            >

              <button
                className="quiz-hint-toggle"
                onClick={() => {

                  const lastHintLevel =
                    lesson.hints?.length || 0;

                  const canReveal =
                    openedHints.includes(
                      lastHintLevel
                    );

                  if (!canReveal) {

                    setBlockedHintLevel(
                      lastHintLevel
                    );

                    return;
                  }
                  if (
                    revealedAnswer !== null
                  ) {

                    setRevealedAnswer(
                      null
                    );

                    return;
                  }

                  setConfirmReveal(
                    true
                  );
                }}
              >

                <span>
                  🎯 정답 공개
                </span>

                <span className="quiz-hint-arrow">
                  {revealedAnswer !== null
                    ? "−"
                    : "+"}
                </span>

              </button>

              {revealedAnswer !== null && (

                <div className="quiz-hint-content">
                  🎯 정답: {revealedAnswer}번
                </div>

              )}

            </div>

        </div>

      </div>
      <div className="quiz-wrap">

        <div className="quiz-question">
          {
            lesson.content.question
          }
        </div>

        <div className="quiz-choices">

          {lesson.content.choices.map(
            (choice, idx) => (

              <button
                key={idx}
                className={`quiz-choice
                  ${
                    selected === idx
                      ? "selected"
                      : ""
                  }
                `}
                onClick={() => {

                  setSelected(idx);

                  setIsCorrect(
                    null
                  );
                }}
              >

                <div className="quiz-choice-index">
                  {idx + 1}
                </div>

                <div className="quiz-choice-text">
                  {choice}
                </div>

              </button>
            )
          )}

        </div>
        {isCorrect !== null && (

          <div
            className={`quiz-result ${
              isCorrect
                ? "answer"
                : "fail"
            }`}
          >

            {isCorrect
              ? "🎉 정답"
              : "❌ 오답"}

          </div>
        )}

      </div>
      {confirmHint && (

        <div className="hint-confirm-popup">

          <div className="hint-confirm-title">
            💡 힌트를
            사용하시겠습니까?
          </div>

          <div className="hint-confirm-desc">

            Hint Level{" "}
            {confirmHint.level}
            을 사용합니다.

            <br />

            ⚠️ 5XP가 차감됩니다.

          </div>

          <div className="hint-confirm-actions">

            <button
              className="hint-cancel-btn"
              onClick={() =>
                setConfirmHint(
                  null
                )
              }
            >
              취소
            </button>

            <button
              className="hint-use-btn"
              onClick={useHint}
            >
              사용하기
            </button>

          </div>

        </div>
      )}

      {confirmReveal && (

        <div className="hint-confirm-popup">

          <div className="hint-confirm-title">
            🎯 정답을
            공개하시겠습니까?
          </div>

          <div className="hint-confirm-desc">

            정답을 공개합니다.

            <br />

            ⚠️ 5XP가 차감됩니다.

          </div>

          <div className="hint-confirm-actions">

            <button
              className="hint-cancel-btn"
              onClick={() =>
                setConfirmReveal(
                  false
                )
              }
            >
              취소
            </button>

            <button
              className="hint-use-btn"
              onClick={revealAnswer}
            >
              공개하기
            </button>

          </div>

        </div>
      )}

      {blockedHintLevel !== null && (

        <div className="hint-confirm-popup">

          <div className="hint-confirm-title">
            ⚠️ 먼저 이전 단계를
            완료해주세요
          </div>

          <div className="hint-confirm-desc">

            Hint Level{" "}
            {blockedHintLevel}
            을 먼저 사용해야
            다음 단계를 열 수 있습니다.

          </div>

          <div className="hint-confirm-actions">

            <button
              className="hint-use-btn"
              onClick={() =>
                setBlockedHintLevel(
                  null
                )
              }
            >
              확인
            </button>

          </div>

        </div>
      )}

    </div>
  );
}