import { useEffect, useState } from "react";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";

import "../../styles/CodeFill.css";

export default function CodeFill({ lesson }) {

  const [markdown, setMarkdown] = useState("");
  const [answers, setAnswers] = useState({});
  const [openedHint, setOpenedHint] = useState(null);

  useEffect(() => {
    async function loadMarkdown() {

      if (!lesson?.markdownUrl) return;

      const res = await fetch(lesson.markdownUrl);

      const text = await res.text();

      setMarkdown(text);
    }

    loadMarkdown();
  }, [lesson.markdownUrl]);

  const submit = () => {

    const payload = {
      problemId: lesson.problemId,
      answers,
    };

    console.log("submit:", payload);

    const correct = lesson.content.answer;

    const isCorrect = Object.keys(correct).every(
      (key) => correct[key] === answers[key]
    );

    alert(
      isCorrect
        ? "🎉 정답입니다!"
        : "❌ 다시 시도하세요"
    );
  };

  const renderTemplate = () => {
    return lesson.content.template
      .split(/({{.*?}})/g)
      .map((part, idx) => {

        const match = part.match(/{{(.*?)}}/);

        if (!match) {
          return (
            <span key={idx}>
              {part}
            </span>
          );
        }

        const key = match[1];

        return (
          <input
            key={`${key}-${idx}`}
            className="codefill-blank"
            value={answers[key] || ""}
            onChange={(e) =>
              setAnswers({
                ...answers,
                [key]: e.target.value,
              })
            }
          />
        );
      });
  };

  return (
    <div className="codefill-layout">

      <div className="codefill-left">

        <div className="markdown-card">

          <div className="markdown-title">
            📘 개념 설명
          </div>

          <div className="markdown-body">

            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              rehypePlugins={[rehypeRaw]}
            >
              {markdown}
            </ReactMarkdown>

          </div>

        </div>
        <div className="hint-group">

          {lesson.content.hints.map((hint) => {

            const opened =
              openedHint === hint.level;

            return (
              <div
                key={hint.level}
                className={`hint-dropdown ${
                  opened ? "open" : ""
                }`}
              >

                <button
                  className="hint-toggle"
                  onClick={() =>
                    setOpenedHint(
                      opened ? null : hint.level
                    )
                  }
                >
                  💡 Hint {hint.level}

                  <span className="hint-arrow">
                    {opened ? "−" : "+"}
                  </span>
                </button>

                {opened && (
                  <div className="hint-content">
                    {hint.text}
                  </div>
                )}

              </div>
            );
          })}

        </div>
        <div className="mission-card">

          <div className="mission-title">
            🎯 목표
          </div>

          <div className="mission-text">
            빈칸을 모두 채워 코드를 완성하세요.
          </div>

        </div>

      </div>

      <div className="codefill-right">

        <div className="editor-top">
          ← 개념을 참고해서 코드 완성
        </div>

        <div className="code-editor">

          <div className="code-editor-header">

            <div className="dots">
              <span />
              <span />
              <span />
            </div>

            <div className="code-editor-title">
              practice.py
            </div>

            <button
              className="submit-answer-btn"
              onClick={submit}
            >
              제출
            </button>

          </div>

          <div className="code-editor-body">

            <div className="codefill-code">
              {renderTemplate()}
            </div>

          </div>

        </div>

      </div>

    </div>
  );
}