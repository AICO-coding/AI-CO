<div style="background-color:#e6f5ff;border:2px solid #c2e4ff;border-radius:14px;padding:18px;font-family:'Nunito',sans-serif,'Malgun Gothic';">
  <h3 style="margin-top:0;margin-bottom:14px;color:#0f172a;font-weight:900;font-size:17px;">zero_grad → backward → step</h3>
  <div style="line-height:1.85;color:#334155;font-size:14px;margin-bottom:16px;">
    매 배치마다 반드시 <b>이 순서</b>를 지켜야 해요.<br>
    순서가 틀리거나 하나라도 빠지면 학습이 망가져요.
  </div>
  <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:16px;">
    <div style="background:#fff;border:2px solid #c2e4ff;border-radius:8px;padding:10px 14px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:5px;">
        <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:2px 8px;border-radius:20px;">1단계</span>
        <code style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#FF6B00;">opt.zero_grad()</code>
      </div>
      <div style="font-size:12px;color:#64748b;line-height:1.6;">이전 배치의 gradient 초기화<br><b style="color:#e55a00;">누락 시 gradient 누적 → 파라미터 폭발!</b> PyTorch는 자동 초기화 안 해요.</div>
    </div>
    <div style="background:#fff;border:2px solid #c2e4ff;border-radius:8px;padding:10px 14px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:5px;">
        <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:2px 8px;border-radius:20px;">2단계</span>
        <code style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#FF6B00;">loss.backward()</code>
      </div>
      <div style="font-size:12px;color:#64748b;line-height:1.6;">역전파 실행 — 각 파라미터의 gradient 자동 계산</div>
    </div>
    <div style="background:#fff;border:2px solid #c2e4ff;border-radius:8px;padding:10px 14px;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:5px;">
        <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:2px 8px;border-radius:20px;">3단계</span>
        <code style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#FF6B00;">opt.step()</code>
      </div>
      <div style="font-size:12px;color:#64748b;line-height:1.6;">계산된 gradient로 w, b 파라미터 업데이트 (제공됨 — 채울 필요 없어요)</div>
    </div>
  </div>
  <div style="background-color:#fff3eb;border:2px solid #ffd0b0;padding:12px 14px;border-radius:10px;color:#0f172a;font-weight:bold;font-size:13px;display:flex;align-items:flex-start;gap:10px;">
    <div style="color:#FF6B00;font-size:16px;margin-top:-2px;">⚡</div>
    <div style="line-height:1.6;">실수 1위: zero_grad() 빠뜨리기<br>실수 2위: backward()와 step() 순서 바꾸기</div>
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
<pre style="margin:0;background:transparent;border:none;padding:0;"><code><span style="color:#cba6f7;">for</span> epoch <span style="color:#cba6f7;">in</span> range(<span style="color:#fab387;">100</span>):
    pred = model(x)
    loss = crit(pred, y)
    opt.zero_grad()   <span style="color:#545478;font-style:italic;"># ① gradient 초기화 — 반드시 먼저!</span>
    loss.backward()   <span style="color:#545478;font-style:italic;"># ② 역전파: gradient 계산</span>
    opt.step()        <span style="color:#545478;font-style:italic;"># ③ 파라미터 업데이트</span>
    <span style="color:#cba6f7;">if</span> (epoch+<span style="color:#fab387;">1</span>) % <span style="color:#fab387;">20</span> == <span style="color:#fab387;">0</span>:
        print(f<span style="color:#a6e3a1;">"Epoch {epoch+1} | Loss: {loss.item():.4f}"</span>)</code></pre>
  </div>
</div>

<br>

<div style="background-color:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:14px 16px;font-family:'Nunito',sans-serif;">
  <div style="color:#94a3b8;font-size:12px;font-weight:800;margin-bottom:6px;display:flex;align-items:center;gap:5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color:#64748b;font-size:13px;line-height:1.6;">
    TODO 8에서 <code style="background:#f1f5f9;padding:1px 5px;border-radius:4px;font-size:12px;">opt.zero_grad()</code>와<br>
    <code style="background:#f1f5f9;padding:1px 5px;border-radius:4px;font-size:12px;">loss.backward()</code>를 순서에 맞게 채워요.
  </div>
</div>