import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import Topbar from "./components/Topbar";
import Sidebar from "./components/Sidebar";
import Home from "./pages/Home";
import DailyTask from "./pages/DailyTask";
import Track from "./pages/Track";
import WrongNote from "./pages/WrongNote";
import Login from "./pages/Login";
import Nickname from "./pages/NickName";
import Chapter from "./pages/Chapter";
import Lesson from "./pages/Lesson";
import "./App.css";

function Layout() {
  const location = useLocation();
  const hideSidebar = location.pathname.includes("/lesson");

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

            <Route
              path="/tracks/:trackId/chapters"
              element={<Chapter />}
            />

            <Route
              path="/tracks/:trackId/chapters/:chapterId/lessons"
              element={<Lesson />}
            />

            <Route
              path="/tracks/:trackId/chapters/:chapterId/lessons/:lessonId"
              element={<Lesson />}
            />
            <Route path="/wrong-answer" element={<WrongNote />} />
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