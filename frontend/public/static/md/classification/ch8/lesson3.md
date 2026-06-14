<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">CrossEntropyLoss — 다중 분류의 Loss</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    다중 분류에서는
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-weight: 700;">nn.CrossEntropyLoss()</span>
    를 씁니다. 이 함수는 <b>Softmax + Log + NLL Loss</b>를 한 번에 처리합니다.<br><br>
    그래서 출력층에 Softmax를 직접 붙이지 않아도 됩니다. logit을 그대로 넣으면 내부에서 Softmax를 적용하고 Loss를 계산합니다.<br><br>
    레이블 y는 <b>클래스 번호(정수)</b>로 넣습니다. BCELoss와 달리 원-핫 인코딩 없이 정수 레이블 그대로 사용합니다. 예를 들어 클래스 0이면 0, 클래스 2이면 2를 넣습니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #dcfce7; border-radius: 8px; padding: 10px 14px; color: #166534;">
      ✅ <b>CrossEntropyLoss 장점</b> — Softmax 내장 → 출력층에 Softmax 생략 가능. 수치적으로도 더 안정적
    </div>
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      📌 <b>레이블 형태</b> — BCELoss: float [0.0, 1.0] / CrossEntropyLoss: int [0, 1, 2, ...] (클래스 번호)
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; color: #334155;">
      ⚠️ <b>주의</b> — CrossEntropyLoss 쓸 때 출력층에 Softmax 붙이면 안 됩니다. 내부에서 이미 처리하므로 중복 적용됩니다
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
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><span style="color: #cba6f7;">import</span> torch
<span style="color: #cba6f7;">import</span> torch.nn <span style="color: #cba6f7;">as</span> nn

<span style="color: #545478; font-style: italic;"># 출력층: Softmax 없이 logit 그대로</span>
logits = torch.tensor([[<span style="color: #fab387;">2.0</span>, <span style="color: #fab387;">1.0</span>, <span style="color: #fab387;">0.1</span>]])  <span style="color: #545478; font-style: italic;"># shape: (1, 3)</span>
y = torch.tensor([<span style="color: #fab387;">0</span>])                    <span style="color: #545478; font-style: italic;"># 정수 클래스 번호</span>

criterion = nn.CrossEntropyLoss()
loss = criterion(logits, y)
print(loss)  <span style="color: #545478; font-style: italic;"># tensor(0.4076)</span></code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">CrossEntropyLoss = Softmax 내장. 출력층에 Softmax 생략. 레이블은 정수 그대로. 중복 적용 주의.</div>
</div>
