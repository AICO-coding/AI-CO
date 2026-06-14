<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Optimizer와 학습률(learning rate)</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-weight: 700;">Optimizer</span>
    는 Loss를 기반으로 가중치를 어떻게 업데이트할지 결정합니다.<br><br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 6px; font-weight: 700;">학습률 (lr)</span>
    은 가중치를 한 번에 얼마나 크게 바꿀지 결정합니다. 일반적으로 <b>0.001</b>을 시작점으로 씁니다.<br><br>
    실무에서는 <b>Adam optimizer</b>를 가장 많이 씁니다. 학습률을 자동으로 조정하는 기능이 있어 대부분의 상황에서 잘 동작합니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #fee2e2; border-radius: 12px; padding: 12px 15px; color: #991b1b;">
      ⬆️ <b>lr이 너무 크면</b> — 가중치가 너무 크게 변함 → Loss가 발산
    </div>
    <div style="background: #fef9c3; border-radius: 12px; padding: 12px 15px; color: #713f12;">
      ⬇️ <b>lr이 너무 작으면</b> — 가중치가 아주 조금씩만 변함 → 학습 매우 느림
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

model = BinaryClassifier()

<span style="color: #545478; font-style: italic;"># Adam optimizer, lr=0.001 (기본 시작점)</span>
optimizer = torch.optim.Adam(
    model.parameters(),  <span style="color: #545478; font-style: italic;"># 모델의 모든 가중치</span>
    lr=<span style="color: #fab387;">0.001</span>
)</code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">lr 너무 크면 발산 / 너무 작으면 느림. 기본값 0.001. 실무 기본 optimizer는 Adam.</div>
</div>
