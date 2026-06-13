<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Sigmoid vs ReLU — 어디에 쓰는가?</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    두 함수는 <b>쓰이는 위치가 다릅니다.</b><br><br>
    <b>은닉층</b>에는
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-weight: 700;">ReLU</span>
    를 씁니다. 기울기 소실 문제가 적고 계산이 빠르기 때문입니다.<br><br>
    <b>이진 분류의 출력층</b>에는
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 6px; font-weight: 700;">Sigmoid</span>
    를 씁니다. 출력이 0~1 사이의 확률로 나와야 하기 때문입니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🧠 <b>은닉층</b> → ReLU 사용. 기울기 소실 없음, 계산 빠름
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎯 <b>이진 분류 출력층</b> → Sigmoid 사용. 출력이 0~1 → 클래스 1일 확률로 해석 가능
    </div>
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

<span style="color: #545478; font-style: italic;"># 은닉층 → ReLU</span>
hidden = nn.Linear(<span style="color: #fab387;">4</span>, <span style="color: #fab387;">8</span>)
act_hidden = nn.ReLU()

<span style="color: #545478; font-style: italic;"># 이진 분류 출력층 → Sigmoid</span>
output = nn.Linear(<span style="color: #fab387;">8</span>, <span style="color: #fab387;">1</span>)
act_output = nn.Sigmoid()  <span style="color: #545478; font-style: italic;"># 0~1 확률 출력</span></code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">은닉층 → ReLU (기울기 소실 없음) / 이진 분류 출력층 → Sigmoid (0~1 확률 출력).</div>
</div>