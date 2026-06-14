<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">이진 분류기 전체 코드</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    이진 분류기는 출력이 <b>확률 1개</b>입니다. 마지막 Linear 층의 출력 뉴런을 1개로 설정하고, Sigmoid를 붙여서 0~1 사이 확률로 만듭니다.<br><br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">nn.Sequential</span>
    을 쓰면 층을 순서대로 쌓는 것을 한 번에 정의할 수 있습니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      📐 <b>Linear(8, 16) 의미</b> — 입력 뉴런 8개 → 출력 뉴런 16개. 가중치 행렬 shape = (16, 8)
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎯 <b>마지막 층</b> — nn.Linear(16, 1) → nn.Sigmoid() → 확률 1개 출력
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
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; font-family: 'Nunito', sans-serif;">참고 코드 ← 보고 채워요</div>
  </div>
  <div style="padding: 15px; color: #cdd6f4; font-size: 13px; line-height: 1.6; overflow-x: auto;">
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><span style="color: #cba6f7;">import</span> torch.nn <span style="color: #cba6f7;">as</span> nn

<span style="color: #cba6f7;">class</span> <span style="color: #a6e3a1;">BinaryClassifier</span>(nn.Module):
    <span style="color: #cba6f7;">def</span> <span style="color: #89b4fa;">__init__</span>(self):
        <span style="color: #cba6f7;">super</span>().__init__()
        self.net = nn.Sequential(
            nn.Linear(<span style="color: #fab387;">8</span>, <span style="color: #fab387;">16</span>),   <span style="color: #545478; font-style: italic;"># 입력 8 → 은닉 16</span>
            nn.ReLU(),           <span style="color: #545478; font-style: italic;"># 은닉층 활성화</span>
            nn.Linear(<span style="color: #fab387;">16</span>, <span style="color: #fab387;">1</span>),   <span style="color: #545478; font-style: italic;"># 은닉 16 → 출력 1</span>
            nn.Sigmoid()         <span style="color: #545478; font-style: italic;"># 출력층 → 확률</span>
        )

    <span style="color: #cba6f7;">def</span> <span style="color: #89b4fa;">forward</span>(self, x):
        <span style="color: #cba6f7;">return</span> self.net(x)</code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">이진 분류 출력층 = Linear(n, 1) + Sigmoid(). Sequential로 층을 순서대로 쌓습니다.</div>
</div>
