<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">nn.Linear 내부 + ReLU가 필요한 이유</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">nn.Linear(in, out)</span> — 내부: <b style="color: #1681c4;">y = xW<sup>T</sup> + b</b><br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">nn.ReLU()</span> — <b style="color: #1681c4;">max(0, x)</b> : 음수 → 0<br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">비선형성</span> — 없으면 층 아무리 쌓아도 선형 1개와 동일
  </div>

  <div style="background-color: #0f172a; color: #c3e88d; padding: 15px; border-radius: 10px; font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.8; margin-top: 15px;">
    nn.Linear(4, 16)  → 입력 4개 → 출력 16개<br>
    nn.ReLU()         → 음수 제거 → 비선형성 부여<br>
    nn.Linear(16, 1)  → 출력 1개 (예측값)
  </div>

  <div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 12px 15px; border-radius: 10px; margin-top: 15px; color: #0f172a; font-weight: bold; font-size: 13px; display: flex; align-items: center; gap: 10px;">
    <span style="color: #FF6B00; font-size: 16px;">⚡</span> ReLU 없이 Linear 3개 쌓기 = Linear 1개. 반드시 사이에 넣어야 해요!
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
<span style="color: #cba6f7;">import</span> torch.nn <span style="color: #cba6f7;">as</span> nn

<span style="color: #545478; font-style: italic;"># nn.Linear(입력 수, 출력 수)</span>
layer1 = nn.Linear(<span style="color: #fab387;">4</span>, <span style="color: #fab387;">16</span>)   <span style="color: #545478; font-style: italic;"># 4 → 16</span>
relu   = nn.ReLU()             <span style="color: #545478; font-style: italic;"># 비선형성!</span>
layer2 = nn.Linear(<span style="color: #fab387;">16</span>, <span style="color: #fab387;">1</span>)   <span style="color: #545478; font-style: italic;"># 16 → 1</span>

<span style="color: #545478; font-style: italic;"># 데이터 흘려보기</span>
x  = torch.randn(<span style="color: #fab387;">8</span>, <span style="color: #fab387;">4</span>)        <span style="color: #545478; font-style: italic;"># 배치 8개, 특성 4개</span>
h  = relu(layer1(x))           <span style="color: #545478; font-style: italic;"># (8, 16)</span>
out = layer2(h)                <span style="color: #545478; font-style: italic;"># (8, 1)</span></code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: 'Nunito', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">🏆 Mission 연결</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">미션 모델의 각 Linear 숫자가 입력/출력 특성 수를 의미해요. 첫 번째 레이어 입력은 데이터 컬럼 수와 같아야 해요.</div>
</div>