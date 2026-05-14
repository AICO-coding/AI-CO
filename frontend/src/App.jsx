import { BrowserRouter, Routes, Route } from "react-router-dom";
import Topbar from "./components/Topbar";
import Sidebar from "./components/Sidebar";
import Home from "./pages/Home";
import DailyTask from "./pages/DailyTask";
import Track from "./pages/Track";
import WrongNote from "./pages/WrongNote";
import "./App.css";
import Login from "./pages/Login";
import Nickname from "./pages/NickName";


function Layout() {
  return (
    <>
      <Topbar />

      <div id="app">
        <Sidebar />

        <div id="main">
          <Routes>
            <Route path="/home" element={<Home />} />
            <Route path="/daily" element={<DailyTask />} />
            <Route path="/track" element={<Track />} />
            <Route path="/wrong-answer" element={<WrongNote />} />
          </Routes>
        </div>
      </div>
    </>
  );
}

function App() {
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

export default App;