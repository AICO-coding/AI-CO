<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">shape · dtype · device — 3대 속성</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">.shape</span> — 텐서의 모양 (에러 원인 1위!)<br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">.dtype</span> — 기본값 <b style="color: #1681c4;">float32</b><br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">.device</span> — cpu 또는 cuda
  </div>

  <div style="background-color: #0f172a; color: #c3e88d; padding: 15px; border-radius: 10px; font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.8; margin-top: 15px;">
    t.shape   → torch.Size([2, 2])<br>
    t.dtype   → torch.float32 <span style="color: #94a3b8;">← 딥러닝 기본!</span><br>
    t.device  → device('cpu')
  </div>

  <div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 12px 15px; border-radius: 10px; margin-top: 15px; color: #0f172a; font-weight: bold; font-size: 13px; display: flex; align-items: center; gap: 10px;">
    <span style="color: #FF6B00; font-size: 16px;">⚡</span> shape 불일치 = 에러 1위! 연산 전 .shape 꼭 확인!
  </div>
</div>

<br>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 12px; overflow: hidden; font-family: 'JetBrains Mono', monospace; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 10px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #6060a0; margin-left: 8px; font-size: 12px;">📄 reference.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; font-family: 'Nunito', sans-serif;">
      참고 코드 ← 보고 채워요
    </div>
  </div>
  
  <div style="padding: 15px; color: #cdd6f4; font-size: 13px; line-height: 1.6; overflow-x: auto;">
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><span style="color: #cba6f7;">import</span> torch

t = torch.tensor([[<span style="color: #fab387;">1.</span>, <span style="color: #fab387;">2.</span>], [<span style="color: #fab387;">3.</span>, <span style="color: #fab387;">4.</span>]])

<span style="color: #545478; font-style: italic;"># 3대 속성</span>
print(t.shape)   <span style="color: #545478; font-style: italic;"># torch.Size([2, 2])</span>
print(t.dtype)   <span style="color: #545478; font-style: italic;"># torch.float32</span>
print(t.device)  <span style="color: #545478; font-style: italic;"># cpu</span>

<span style="color: #545478; font-style: italic;"># reshape: 원소 수 동일하면 자유롭게</span>
r = torch.arange(<span style="color: #fab387;">6.</span>).reshape(<span style="color: #fab387;">2</span>, <span style="color: #fab387;">3</span>)
print(r.shape)   <span style="color: #545478; font-style: italic;"># torch.Size([2, 3])</span></code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: 'Nunito', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">🏆 Mission 연결</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">미션에서 X.reshape(-1, 1)로 입력 데이터 shape을 맞춰요.</div>
</div>