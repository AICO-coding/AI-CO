<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Softmax — 점수를 확률 분포로 변환</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Softmax</span>
    는 여러 개의 logit(점수)을 받아 <b>합이 1인 확률 분포</b>로 변환합니다.<br>
    공식:
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 8px; border-radius: 4px; font-family: monospace;">softmax(zᵢ) = e^zᵢ / Σe^zⱼ</span><br><br>
    각 클래스의 확률이 0~1 사이이고, 전체 합이 반드시 1이 됩니다. 가장 큰 logit이 가장 높은 확률을 갖고, 최종 예측 클래스는 확률이 가장 높은 클래스입니다. 코드에서는
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace;">argmax</span>
    로 찾습니다.<br><br>
    Sigmoid는 각 출력을 <b>독립적으로</b> 0~1로 압축합니다. Softmax는 모든 출력을 <b>연동해서</b> 합이 1이 되도록 조정합니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #dcfce7; border-radius: 8px; padding: 10px 14px; color: #166534;">
      🎯 <b>예측 클래스 결정</b> — 확률 [0.659, 0.242, 0.099] → argmax → <b>클래스 0</b> (가장 높은 확률)
    </div>
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      ⚖️ <b>Sigmoid vs Softmax</b> — Sigmoid: 출력 1개, 이진 분류 / Softmax: 출력 N개, 다중 분류
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
<span style="color: #cba6f7;">import</span> torch.nn.functional <span style="color: #cba6f7;">as</span> F

logits = torch.tensor([<span style="color: #fab387;">2.0</span>, <span style="color: #fab387;">1.0</span>, <span style="color: #fab387;">0.1</span>])
probs = F.softmax(logits, dim=<span style="color: #fab387;">0</span>)
print(probs)         <span style="color: #545478; font-style: italic;"># tensor([0.659, 0.242, 0.099])</span>
print(probs.sum())   <span style="color: #545478; font-style: italic;"># tensor(1.000) ← 합은 항상 1</span>

pred = torch.argmax(probs)
print(pred)          <span style="color: #545478; font-style: italic;"># tensor(0) ← 클래스 0이 가장 높음</span></code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">Softmax = 모든 클래스 확률의 합 1. 가장 높은 확률의 클래스가 예측값. argmax로 찾습니다.</div>
</div>
