import { BrowserRouter, Routes, Route } from "react-router-dom";
import Topbar from "./components/Topbar";
import Sidebar from "./components/Sidebar";
import Home from "./pages/Home";
import DailyTask from "./pages/DailyTask";
import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Topbar />
      <div id="app">
        <Sidebar />
        <div id="main">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/daily" element={<DailyTask />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
