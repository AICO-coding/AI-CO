import { useState } from "react";
import "../../styles/Parameter.css"

export default function Parameter() {
  const [rows, setRows] = useState(2);
  const [cols, setCols] = useState(3);

  return (
    <div className="param-layout">
      <div className="param-panel">
        <div className="param-item">
          <label>Rows</label>
          <input
            type="range"
            min="1"
            max="6"
            value={rows}
            onChange={(e) => setRows(e.target.value)}
          />
        </div>

        <div className="param-item">
          <label>Cols</label>
          <input
            type="range"
            min="1"
            max="6"
            value={cols}
            onChange={(e) => setCols(e.target.value)}
          />
        </div>
      </div>

      <div className="param-preview">
        reshape({rows}, {cols})
      </div>
    </div>
  );
}