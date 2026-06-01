import { useEffect, useState } from "react";

import "../../styles/ConceptImage.css";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";

export default function ConceptImage({ lesson }) {
  const [markdown, setMarkdown] = useState("");

  console.log(markdown);

  useEffect(() => {
  async function loadMarkdown() {
    try {
      const res = await fetch(lesson.markdownUrl);

      if (!res.ok) {
        throw new Error("Markdown fetch failed");
      }

      const text = await res.text();

      setMarkdown(text);
    } catch (err) {
      console.error(err);
    }
  }

  loadMarkdown();
}, [lesson.markdownUrl]);

  return (
    <div className="concept-image-layout">
      <div className="concept-markdown-panel">
        <div className="markdown-body">
          <ReactMarkdown
            remarkPlugins={[remarkGfm]}
            rehypePlugins={[rehypeRaw]}
          >
            {markdown}
          </ReactMarkdown>
        </div>
      </div>
      <div className="concept-image-panel">
        <img
          src={lesson?.imageUrl}
          alt={lesson?.title}
          className="concept-image"
        />
      </div>
    </div>
  );
}