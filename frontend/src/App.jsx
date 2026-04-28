import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Sidebar from "./components/Sidebar";

function App() {
  return (
    <BrowserRouter>
      <div style={{ display: "flex" }}>
        <Sidebar />

        <div style={{ flex: 1, padding: "20px" }}>
          <Routes>
            <Route path="/" element={<Home />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;