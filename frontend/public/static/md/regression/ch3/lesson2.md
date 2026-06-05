<div style="background-color:#e6f5ff;border:2px solid #c2e4ff;border-radius:14px;padding:18px;font-family:'Nunito',sans-serif,'Malgun Gothic';">
  <h3 style="margin-top:0;margin-bottom:14px;color:#0f172a;font-weight:900;font-size:17px;">특성 정규화 — StandardScaler</h3>
  <div style="line-height:1.85;color:#334155;font-size:14px;margin-bottom:14px;">
    캘리포니아 데이터의 특성들은 <b>스케일이 천차만별</b>이에요.<br>
    이 상태로 학습하면 gradient가 특정 특성 쪽으로만 크게 계산돼서 학습이 불안정해요.
  </div>
  <div style="background:#fff;border:1px solid #ffd0b0;border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:13px;">
    <div style="display:flex;gap:6px;align-items:center;margin-bottom:6px;">
      <span style="color:#FF6B00;font-weight:900;">⚠</span>
      <b style="color:#0f172a;">정규화 전 스케일 차이</b>
    </div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:12px;line-height:1.8;color:#334155;">
      MedInc &nbsp;&nbsp;: <span style="color:#2DAA24;">0 ~ 15</span><br>
      Population: <span style="color:#FF4444;">3 ~ 35,000</span> ← 이 특성이 gradient를 독점!<br>
      <span style="color:#94a3b8;font-size:11px;">→ 정규화 없이 R²≈0.30 &nbsp;/&nbsp; 정규화 후 R²≈0.70+</span>
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:14px;">
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;line-height:1.6;">
      <code style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#FF6B00;background:#fff3eb;border:1px solid #ffd0b0;padding:1px 5px;border-radius:4px;">fit_transform(X_tr)</code>
      &nbsp;— train에 <b>fit + transform 동시 적용</b><br>
      <span style="color:#94a3b8;font-size:12px;">train의 평균/표준편차를 계산하고, 그걸로 변환</span>
    </div>
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;line-height:1.6;">
      <code style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#FF6B00;background:#fff3eb;border:1px solid #ffd0b0;padding:1px 5px;border-radius:4px;">transform(X_te)</code>
      &nbsp;— test에는 <b>transform만!</b><br>
      <span style="color:#FF4444;font-size:12px;font-weight:800;">⚠ test에 fit하면 데이터 누출(leakage)! 절대 안 돼요</span>
    </div>
  </div>
  <div style="background-color:#fff3eb;border:2px solid #ffd0b0;padding:12px 14px;border-radius:10px;color:#0f172a;font-weight:bold;font-size:13px;display:flex;align-items:flex-start;gap:10px;">
    <div style="color:#FF6B00;font-size:16px;margin-top:-2px;">⚡</div>
    <div style="line-height:1.6;">scaler는 반드시 train 데이터로만 fit해요.<br>test는 "미래 데이터" — 학습 때 보면 안 돼요!</div>
  </div>
</div>

<br>

<div style="background-color:#1e1e2e;border:2px solid #e2e8f0;border-radius:12px;overflow:hidden;font-family:'JetBrains Mono',monospace;box-shadow:0 4px 6px rgba(0,0,0,0.1);">
  <div style="background-color:#0d0d1a;border-bottom:1px solid #1a1a2e;padding:10px 15px;display:flex;align-items:center;justify-content:space-between;">
    <div style="display:flex;align-items:center;gap:6px;">
      <div style="width:10px;height:10px;background:#ff5f57;border-radius:50%;"></div>
      <div style="width:10px;height:10px;background:#ffbd2e;border-radius:50%;"></div>
      <div style="width:10px;height:10px;background:#28ca41;border-radius:50%;"></div>
      <span style="color:#6060a0;margin-left:8px;font-size:12px;">📄 reference.py</span>
    </div>
    <div style="background-color:rgba(255,107,0,.2);color:#FF6B00;padding:4px 10px;border-radius:12px;font-size:11px;font-weight:800;font-family:'Nunito',sans-serif;">참고 코드 ← 보고 채워요</div>
  </div>
  <div style="padding:15px;color:#cdd6f4;font-size:13px;line-height:1.6;overflow-x:auto;">
<pre style="margin:0;background:transparent;border:none;padding:0;"><code><span style="color:#cba6f7;">from</span> sklearn.preprocessing <span style="color:#cba6f7;">import</span> StandardScaler

<span style="color:#545478;font-style:italic;"># ① 정규화 클래스 인스턴스화</span>
scaler = StandardScaler()

<span style="color:#545478;font-style:italic;"># ② train: fit + transform 동시에</span>
X_tr = torch.FloatTensor(scaler.fit_transform(X_tr))   <span style="color:#545478;font-style:italic;"># fit은 train만!</span>

<span style="color:#545478;font-style:italic;"># ③ test: transform만 (fit 절대 안 됨!)</span>
X_te = torch.FloatTensor(scaler.transform(X_te))</code></pre>
  </div>
</div>

<br>

<div style="background-color:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:14px 16px;font-family:'Nunito',sans-serif;">
  <div style="color:#94a3b8;font-size:12px;font-weight:800;margin-bottom:6px;display:flex;align-items:center;gap:5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color:#64748b;font-size:13px;line-height:1.6;">
    TODO 2에서 <code style="background:#f1f5f9;padding:1px 5px;border-radius:4px;font-size:12px;">StandardScaler()</code> 인스턴스를 만들어요.<br>
    정규화 후 R²가 0.30 → 0.70으로 향상하는 걸 직접 확인해요!
  </div>
</div>