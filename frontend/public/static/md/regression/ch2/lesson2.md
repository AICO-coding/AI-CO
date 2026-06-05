<div style="background-color:#e6f5ff;border:2px solid #c2e4ff;border-radius:14px;padding:18px;font-family:'Nunito',sans-serif,'Malgun Gothic';">
  <h3 style="margin-top:0;margin-bottom:14px;color:#0f172a;font-weight:900;font-size:17px;">MSE Loss · Adam 옵티마이저</h3>
  <div style="line-height:1.85;color:#334155;font-size:14px;margin-bottom:16px;">
    모델이 얼마나 틀렸는지 측정하는 <b>Loss 함수</b>와<br>
    파라미터를 어떻게 업데이트할지 결정하는 <b>Optimizer</b>를 설정해요.
  </div>
  <div style="display:flex;flex-direction:column;gap:10px;margin-bottom:16px;">
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:10px 14px;font-size:13px;color:#334155;line-height:1.7;">
      <span style="background:#fff;border:1px solid #ffd0b0;color:#FF6B00;padding:1px 6px;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:12px;">nn.MSELoss()</span>
      &nbsp;— 예측값과 실제값의 <b>차이를 제곱해서 평균</b><br>
      <span style="color:#94a3b8;font-size:12px;">왜 제곱? → 음수 오차와 양수 오차를 같은 크기로 취급, 큰 오차에 더 큰 패널티</span>
    </div>
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:10px 14px;font-size:13px;color:#334155;line-height:1.7;">
      <span style="background:#fff;border:1px solid #ffd0b0;color:#FF6B00;padding:1px 6px;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:12px;">torch.optim.Adam()</span>
      &nbsp;— <b>적응형 학습률</b> 옵티마이저<br>
      <span style="color:#94a3b8;font-size:12px;">파라미터마다 학습률 자동 조절 → SGD보다 빠르고 안정적으로 수렴</span>
    </div>
  </div>
  <div style="background-color:#fff3eb;border:2px solid #ffd0b0;padding:12px 14px;border-radius:10px;color:#0f172a;font-weight:bold;font-size:13px;display:flex;align-items:flex-start;gap:10px;">
    <div style="color:#FF6B00;font-size:16px;margin-top:-2px;">⚡</div>
    <div style="line-height:1.6;">Loss 함수와 Optimizer는 학습 시작 전 딱 한 번만 설정해요.<br>매 배치마다 반복 설정하지 않아요!</div>
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
<pre style="margin:0;background:transparent;border:none;padding:0;"><code><span style="color:#cba6f7;">import</span> torch, torch.nn <span style="color:#cba6f7;">as</span> nn

model = nn.Linear(<span style="color:#fab387;">1</span>, <span style="color:#fab387;">1</span>)

<span style="color:#545478;font-style:italic;"># ① Loss 함수 설정 — 회귀 문제의 표준</span>
crit = nn.MSELoss()

<span style="color:#545478;font-style:italic;"># ② Optimizer 설정 — 적응형 학습률</span>
opt = torch.optim.Adam(model.parameters(), lr=<span style="color:#fab387;">0.01</span>)

<span style="color:#545478;font-style:italic;"># 사용 예시</span>
pred = model(torch.tensor([[<span style="color:#fab387;">1.0</span>]]))
y    = torch.tensor([[<span style="color:#fab387;">3.0</span>]])
loss = crit(pred, y)
print(loss)  <span style="color:#545478;font-style:italic;"># tensor(X.XXXX, grad_fn=&lt;MseLossBackward&gt;)</span></code></pre>
  </div>
</div>

<br>

<div style="background-color:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:14px 16px;font-family:'Nunito',sans-serif;">
  <div style="color:#94a3b8;font-size:12px;font-weight:800;margin-bottom:6px;display:flex;align-items:center;gap:5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color:#64748b;font-size:13px;line-height:1.6;">
    TODO 7에서 <code style="background:#f1f5f9;padding:1px 5px;border-radius:4px;font-size:12px;">crit = nn.MSELoss()</code>와<br>
    <code style="background:#f1f5f9;padding:1px 5px;border-radius:4px;font-size:12px;">opt = torch.optim.Adam(...)</code>을 직접 채워요.
  </div>
</div>