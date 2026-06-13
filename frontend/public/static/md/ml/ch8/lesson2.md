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
    <div style="background: #f1f5f9; border-radius: 8px; padding: 10px 14px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      logits = [2.0, 1.0, 0.1]<br>
      softmax → [0.659, 0.242, 0.099]<br>
      합 = 0.659 + 0.242 + 0.099 = 1.0
    </div>
    <div style="background: #dcfce7; border-radius: 8px; padding: 10px 14px; color: #166534;">
      🎯 <b>예측 클래스 결정</b> — 확률 [0.659, 0.242, 0.099] → argmax → <b>클래스 0</b> (가장 높은 확률)
    </div>
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      ⚖️ <b>Sigmoid vs Softmax</b> — Sigmoid: 출력 1개, 이진 분류 / Softmax: 출력 N개, 다중 분류. 합이 1이 되는지가 핵심 차이
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">Softmax = 모든 클래스 확률의 합 1. 가장 높은 확률의 클래스가 예측값. argmax로 찾습니다.</div>
</div>
