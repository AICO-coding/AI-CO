import { useEffect, useState } from "react";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";

import "../../styles/Lesson.css";

export default function ConceptCode({
  lesson,
  registerSubmit,
}) {

  const [markdown, setMarkdown] =
    useState("");

  const [answers, setAnswers] =
    useState({});

  const [result, setResult] =
    useState(null);
    useEffect(() => {
      setAnswers({});
      setResult(null);
    }, [lesson.lessonId]);

    useEffect(() => {
      registerSubmit?.(
        () => checkAnswers
      );

    }, [answers, lesson]);

    useEffect(() => {

    async function loadMarkdown() {

      const res = await fetch(
        lesson.markdownUrl
      );

      const text =
        await res.text();

      setMarkdown(text);
    }

    loadMarkdown();

  }, [lesson.markdownUrl]);

  const checkAnswers = async () => {

    const blanks =
      lesson.content.blanks;

    let correctCount = 0;

    const detail = {};

    blanks.forEach((blank) => {

      const userAnswer =
        (answers[blank.key] || "")
          .trim();

      const correctAnswer =
        blank.answer.trim();

      const isCorrect =
        userAnswer ===
        correctAnswer;

      if (isCorrect) {
        correctCount++;
      }

      detail[blank.key] = {
        isCorrect,
      };
    });

    const isAllCorrect =
      correctCount === blanks.length;

    setResult({
      detail,
      total: blanks.length,
      correct: correctCount,
      isAllCorrect,
    });

    return isAllCorrect;
  };

  const renderTemplate = () => {

    return lesson.content.template
      .split(/({{.*?}})/g)
      .map((part, idx) => {

        const match =
          part.match(/{{(.*?)}}/);

        if (!match) {
          return (
            <span key={idx}>
              {part}
            </span>
          );
        }

        const key = match[1];

        const isCorrect =
          result?.detail?.[key]
            ?.isCorrect;

        return (
          <input
            key={`${key}-${idx}`}
            className={`code-blank ${
              result
                ? isCorrect
                  ? "correct"
                  : "wrong"
                : ""
            }`}
            value={
              answers[key] || ""
            }
            onChange={(e) =>
              setAnswers({
                ...answers,
                [key]:
                  e.target.value,
              })
            }
          />
        );
      });
  };

  return (
    <div className="concept-layout">

      {/* LEFT */}
      <div className="concept-left">

        <div className="markdown-body">

          <ReactMarkdown
            remarkPlugins={[
              remarkGfm,
            ]}
            rehypePlugins={[
              rehypeRaw,
            ]}
          >
            {markdown}
          </ReactMarkdown>

        </div>

      </div>

      {/* RIGHT */}
      <div className="concept-right">

        <div className="editor-top">
          ← 왼쪽 개념을 참고해서
          빈칸을 채워보세요
        </div>

        <div className="editor-window">

          <div className="editor-header">

            <div className="dots">
              <span />
              <span />
              <span />
            </div>

            <div className="editor-file">
              practice.py
            </div>

          </div>

          <div className="editor-code">
            {renderTemplate()}
          </div>

        </div>

        {result && (

          <div className="result-box">

            {result.isAllCorrect ? (

              <div className="success-text">
                🎉 정답
              </div>

            ) : (

              <div className="fail-text">
                ❌ {result.correct} / {result.total} 정답
              </div>

            )}

          </div>
        )}

      </div>

    </div>
  );
}