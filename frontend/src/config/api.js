// 배포 환경별 백엔드 API 주소
// 로컬 개발: frontend/.env 에 VITE_API_URL=http://localhost:8000 설정
// 배포(Vercel): 프로젝트 환경변수에 VITE_API_URL=https://<render-service>.onrender.com 설정
export const API_BASE_URL =
  import.meta.env.VITE_API_URL || 'http://210.125.96.59:8000';
