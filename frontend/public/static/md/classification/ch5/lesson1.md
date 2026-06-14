<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">PyTorch 신경망의 기본 구조</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    PyTorch에서 신경망은
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">nn.Module</span>
    을 상속한 클래스로 만듭니다. 구조는 항상 같습니다.
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">__init__</span>
    과
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">forward</span>
    , 두 메서드만 기억하면 됩니다.<br><br>
    <b>__init__</b>에는 모델에서 쓸 층(layer)을 정의합니다.<br>
    <b>forward</b>에는 데이터가 층을 통과하는 순서를 정의합니다.<br><br>
    model(x)라고 쓰면 내부적으로 forward(x)가 자동 호출됩니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🏗️ <b>__init__ 역할</b> — 층을 정의하는 곳. 어떤 층을 쓸지 선언만 합니다
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      ➡️ <b>forward 역할</b> — 데이터가 흐르는 순서를 정의하는 곳
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

<span style="color: #cba6f7;">class</span> <span style="color: #a6e3a1;">MyModel</span>(nn.Module):
    <span style="color: #cba6f7;">def</span> <span style="color: #89b4fa;">__init__</span>(self):
        <span style="color: #cba6f7;">super</span>().__init__()
        <span style="color: #545478; font-style: italic;"># 층 정의</span>
        self.fc = nn.Linear(<span style="color: #fab387;">4</span>, <span style="color: #fab387;">1</span>)

    <span style="color: #cba6f7;">def</span> <span style="color: #89b4fa;">forward</span>(self, x):
        <span style="color: #545478; font-style: italic;"># 데이터 흐름 정의</span>
        <span style="color: #cba6f7;">return</span> self.fc(x)

model = MyModel()
pred = model(x)  <span style="color: #545478; font-style: italic;"># forward(x) 자동 실행</span></code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">__init__ = 층 목록 정의 / forward = 데이터 흐름 정의. model(x) 호출 시 forward(x)가 자동 실행됩니다.</div>
</div>
