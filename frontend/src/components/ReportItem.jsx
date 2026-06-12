import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';

import '../styles/ReportItem.css';

export default function ReportItem() {
  const { trackId, chapterId } = useParams();
  const navigate = useNavigate();

  const [report, setReport] = useState(null);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState('');

  useEffect(() => {
    const fetchReport = async () => {
      try {
        const token = localStorage.getItem('accessToken');

        const res = await fetch(
          `http://210.125.96.59:8000/reports/${trackId}/${chapterId}`,
          {
            headers: {
              ...(token && {
                Authorization: `Bearer ${token}`,
              }),
            },
          },
        );

        if (!res.ok) {
          throw new Error('리포트를 불러오지 못했습니다.');
        }

        const data = await res.json();

        setReport(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchReport();
  }, [trackId, chapterId]);

  if (loading) return null;

  if (error) return <div>❌ {error}</div>;

  return (
    <div className="report-detail-wrap">
      <div className="report-header">
        <div>
          <div className="report-chapter">
            CH.{report.chapter} · {report.track} 트랙 리포트
          </div>

          <div className="report-title-2">{report.chapterTitle}</div>

          <div className="report-meta">
            📅 {new Date(report.completedAt).toLocaleDateString('ko-KR')}
            &nbsp;&nbsp;•&nbsp;&nbsp;
            {report.totalProblems}문제
          </div>
        </div>

        <div className="report-grade">{report.grade}</div>
      </div>
      <section className="report-section">
        <h3>🏅 성과 요약</h3>

        <div className="summary-grid">
          <div className="summary-card xp">
            <div className="summary-value">{report.xpEarned}</div>

            <div className="summary-label">획득 XP</div>
          </div>

          <div className="summary-card wrong">
            <div className="summary-value">{report.wrongCount}</div>

            <div className="summary-label">오답 문제</div>
          </div>

          <div className="summary-card hint">
            <div className="summary-value">{report.hintCount}</div>

            <div className="summary-label">힌트 사용</div>
          </div>
        </div>
      </section>

      <section className="report-section">
        <h3>🤖 코냥이의 취약점 분석</h3>

        <div className="cobot-box">
          <div className="cobot-comment">{report.cobotComment}</div>

          {report.weakConcepts.length > 0 && (
            <div className="weak-tags">
              {report.weakConcepts.map((concept) => (
                <span key={concept} className="weak-tag">
                  {concept}
                </span>
              ))}
            </div>
          )}
        </div>
      </section>

      <section className="report-section">
        <h3>📖 이번 챕터에서 배운 것</h3>

        <div className="content-card">{report.summary}</div>

        <div className="keypoint-card">
          ⚡ 핵심 포인트
          <p>{report.keyPoint}</p>
        </div>

        <div className="next-card">
          👉 다음 챕터
          <p>{report.nextChapter}</p>
        </div>
      </section>

      <section className="report-section">
        <h3>📚 추천 학습 자료</h3>

        <div className="opensource-list">
          {report.opensource.map((item, idx) => (
            <a
              key={idx}
              href={item.url}
              target="_blank"
              rel="noreferrer"
              className="resource-card"
            >
              <div className="resource-name">{item.name}</div>

              <div className="resource-desc">{item.desc}</div>
            </a>
          ))}
        </div>
      </section>

      <button className="report-back-btn" onClick={() => navigate(-1)}>
        이전 페이지로
      </button>
    </div>
  );
}
