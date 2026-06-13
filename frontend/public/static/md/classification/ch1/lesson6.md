<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Threshold — 확률을 클래스로 변환하는 기준</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    확률은 0과 1 사이의 연속적인 숫자입니다.<br>
    그런데 최종 예측은 <b>클래스 0 또는 클래스 1</b> 중 하나여야 합니다.<br>
    이 확률값을 최종 클래스로 변환하는 기준이
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-weight: 700;">threshold (임계값)</span>
    입니다.<br><br>
    기본값은 <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">0.5</span> 입니다.<br>
    확률 <b>≥ 0.5</b> → 클래스 1 (양성) &nbsp;&nbsp; 확률 <b>< 0.5</b> → 클래스 0 (음성)
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #dcfce7; border-radius: 8px; padding: 10px 14px; color: #166534;">
      확률 <b>0.73</b> → 0.73 ≥ 0.5 → <b>클래스 1 (양성)</b>
    </div>
    <div style="background: #fee2e2; border-radius: 8px; padding: 10px 14px; color: #991b1b;">
      확률 <b>0.34</b> → 0.34 &lt; 0.5 → <b>클래스 0 (음성)</b>
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; color: #334155; line-height: 1.8;">
      ⚙️ <b>threshold는 바꿀 수 있습니다</b><br>
      · threshold <b>낮추면(0.3)</b> → 더 많이 양성으로 분류 → 암 진단처럼 놓치면 안 될 때<br>
      · threshold <b>높이면(0.7)</b> → 더 적게 양성으로 분류 → 확실한 경우만 양성으로 판정
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
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><span style="color: #545478; font-style: italic;"># threshold 적용해서 최종 클래스 결정</span>
prob = <span style="color: #fab387;">0.73</span>
threshold = <span style="color: #fab387;">0.5</span>

pred = int(prob >= threshold)
print(pred)  <span style="color: #545478; font-style: italic;"># 1 → 클래스 1 (양성)</span>

<span style="color: #545478; font-style: italic;"># threshold를 높이면?</span>
threshold2 = <span style="color: #fab387;">0.8</span>
pred2 = int(prob >= threshold2)
print(pred2)  <span style="color: #545478; font-style: italic;"># 0 → 클래스 0 (음성) ← 같은 확률인데 결과가 바뀜!</span></code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">확률 ≥ threshold → 클래스 1 / 확률 < threshold → 클래스 0. 기본 threshold = 0.5.</div>
</div>