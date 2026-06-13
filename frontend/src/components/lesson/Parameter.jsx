import { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeRaw from 'rehype-raw';
import '../../styles/Parameter.css';
import '../../styles/Lesson.css';

export default function Parameter({ lesson }) {
  const [markdown, setMarkdown] = useState('');
  const markdownUrl = lesson?.markdownUrl;
  const htmlUrl = lesson?.content?.htmlUrl;

  useEffect(() => {
    if (!markdownUrl) return;
    fetch(markdownUrl)
      .then((r) => r.text())
      .then(setMarkdown)
      .catch(() => setMarkdown(''));
  }, [markdownUrl]);

  return (
    <div className="param-split">
      <div className="param-md-pane">
        <div className="lesson-markdown-body">
          <ReactMarkdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeRaw]}>
            {markdown}
          </ReactMarkdown>
        </div>
      </div>

      <div className="param-html-pane">
        {htmlUrl ? (
          <iframe
            src={htmlUrl}
            className="param-iframe"
            title="interactive"
            sandbox="allow-scripts allow-same-origin"
          />
        ) : (
          <div className="param-no-html">HTML 콘텐츠가 없습니다.</div>
        )}
      </div>
    </div>
  );
}
