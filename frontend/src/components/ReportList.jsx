import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

import '../styles/ReportList.css';

export default function ReportList() {
  const { trackId } = useParams();
  const navigate = useNavigate();

  const [report, setReport] = useState(null);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState('');

  useEffect(() => {
    const fetchReport = async () => {
      try {
        const token = localStorage.getItem('accessToken');

        const res = await fetch(
          `http://210.125.96.59:8000/reports/${trackId}`,
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
  }, [trackId]);

  if (loading) return null;

  if (error) {
    return <div>❌ {error}</div>;
  }

  return (
    <div className="report-wrap">
      <div className="report-hero">
        <div>
          <div className="report-hero-eyebrow">SUMMARY REPORT</div>

          <div className="report-hero-title">{report.track} 요약 리포트</div>

          <div className="report-hero-sub">
            완료한 챕터의 리포트를 확인할 수 있습니다.
          </div>
        </div>

        <div className="report-hero-count">{report.reports.length}개</div>
      </div>

      <div className="report-list">
        {report.reports.map((item) => (
          <div key={item.chapter} className="report-row">
            <div className="report-center">
              <div className="report-chapter">{item.chapter}</div>

              <div className="report-title">{item.title}</div>

              <div className="report-subtext">
                완료일 :{' '}
                {new Date(item.completedAt).toLocaleDateString('ko-KR')}
              </div>
            </div>

            <div className="report-right">
              <button
                className="report-btn"
                onClick={() => navigate(`/reports/${trackId}/${item.chapter}`)}
              >
                리포트 보기
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
