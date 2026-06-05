<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">nn.Module 상속 구조</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">__init__</span> — 레이어 정의 (파라미터 등록)<br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">forward(x)</span> — 데이터 흐름 정의<br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">nn.Sequential</span> — 레이어를 순서대로 묶기
  </div>

  <div style="background-color: #0f172a; color: #c3e88d; padding: 15px; border-radius: 10px; font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.8; margin-top: 15px;">
    class Net(nn.Module):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;__init__  → self.net = nn.Sequential(...)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;forward   → return self.net(x)<br>
    <br>
    model(x) 호출 시 forward가 자동 실행돼요
  </div>

  <div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 12px 15px; border-radius: 10px; margin-top: 15px; color: #0f172a; font-weight: bold; font-size: 13px; display: flex; align-items: center; gap: 10px;">
    <span style="color: #FF6B00; font-size: 16px;">⚡</span> super().__init__() 빠뜨리면 파라미터 등록 자체가 안 돼요! 첫 줄 필수!
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
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><span style="color: #cba6f7;">import</span> torch.nn <span style="color: #cba6f7;">as</span> nn

<span style="color: #cba6f7;">class</span> <span style="color: #a6e3a1;">IrisNet</span>(nn.Module):
    <span style="color: #cba6f7;">def</span> <span style="color: #89b4fa;">__init__</span>(self):
<div style="background: rgba(255,107,0,.09); border-left: 2px solid #FF6B00; padding: 0 13px; margin: 0 -15px;">        super().__init__()          <span style="color: #545478; font-style: italic;"># ← 필수! 빠뜨리면 파라미터 등록 안 됨</span>
        self.net = nn.Sequential(   <span style="color: #545478; font-style: italic;"># 레이어 순서대로 묶기</span>
            nn.Linear(<span style="color: #fab387;">4</span>, <span style="color: #fab387;">16</span>),
            nn.ReLU(),
            nn.Linear(<span style="color: #fab387;">16</span>, <span style="color: #fab387;">1</span>)
        )</div>
    <span style="color: #cba6f7;">def</span> <span style="color: #89b4fa;">forward</span>(self, x):
<div style="background: rgba(255,107,0,.09); border-left: 2px solid #FF6B00; padding: 0 13px; margin: 0 -15px;">        <span style="color: #cba6f7;">return</span> self.net(x)             <span style="color: #545478; font-style: italic;"># Sequential 블록 호출</span></div>

model = IrisNet()
print(model)   <span style="color: #545478; font-style: italic;"># 구조 출력 확인!</span></code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <div style="color: #94a3b8; font-size: 12px; font-weight: 800; margin-bottom: 6px; display: flex; align-items: center; gap: 5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.6;">
    미션 모델도 이 구조 그대로예요. __init__에서 레이어 정의, forward에서 흐름만 써주면 돼요.
  </div>
</div>