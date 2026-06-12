import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom';
import Topbar from './components/Topbar';
import Sidebar from './components/Sidebar';
import Home from './pages/Home';
import DailyTask from './pages/DailyTask';
import Track from './pages/Track';
import WrongNote from './pages/WrongNote';
import WrongNoteTrack from './pages/WrongNoteTrack';
import WrongNoteDetail from './pages/WrongNoteDetail';
import WrongNoteReview from './pages/WrongNoteReview';
import Login from './pages/Login';
import Nickname from './pages/NickName';
import Chapter from './pages/Chapter';
import Lesson from './pages/Lesson';
import Report from './pages/Report';
import ReportList from './components/ReportList';
import ReportItem from './components/ReportItem';
import Mission from './pages/Mission';
import './App.css';

function Layout() {
  const location = useLocation();
  const hideSidebar =
    location.pathname.includes('/lesson') ||
    location.pathname.includes('/mission');

  return (
    <>
      <Topbar />

      <div id="app">
        {!hideSidebar && <Sidebar />}

        <div id="main">
          <Routes>
            <Route path="/home" element={<Home />} />
            <Route path="/daily" element={<DailyTask />} />
            <Route path="/tracks" element={<Track />} />
            <Route path="/reports" element={<Report />} />
            <Route path="/reports/:trackId" element={<ReportList />} />
            <Route
              path="/reports/:trackId/:chapterId"
              element={<ReportItem />}
            />

            <Route path="/tracks/:trackId/chapters" element={<Chapter />} />

            <Route
              path="/tracks/:trackId/chapters/:chapterId/lessons"
              element={<Lesson />}
            />

            <Route
              path="/tracks/:trackId/chapters/:chapterId/lessons/:lessonId"
              element={<Lesson />}
            />
            <Route
              path="/tracks/:trackId/mission"
              element={<Mission />}
            />

            <Route path="/wrong-answer" element={<WrongNote />} />
            <Route path="/wrong-answer/:trackId" element={<WrongNoteTrack />} />
            <Route
              path="/wrong-answer/:trackId/review"
              element={<WrongNoteReview />}
            />
            <Route
              path="/wrong-answer/:trackId/:wrongAnswerId"
              element={<WrongNoteDetail />}
            />
          </Routes>
        </div>
      </div>
    </>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/nickname" element={<Nickname />} />
        <Route path="/*" element={<Layout />} />
      </Routes>
    </BrowserRouter>
  );
}
