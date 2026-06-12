<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Precision과 Recall</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-weight: 700;">Precision (정밀도)</span>
    — <b>"양성으로 예측한 것 중 실제 양성의 비율"</b><br>
    공식:
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 8px; border-radius: 6px; font-family: monospace;">TP / (TP + FP)</span>
    거짓 경보를 얼마나 줄였는지를 나타냅니다. Precision이 높으면 양성으로 예측했을 때 믿을 수 있습니다.<br><br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 6px; font-weight: 700;">Recall (재현율)</span>
    — <b>"실제 양성 중 양성으로 예측한 비율"</b><br>
    공식:
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 8px; border-radius: 6px; font-family: monospace;">TP / (TP + FN)</span>
    실제 양성을 얼마나 빠짐없이 잡아냈는지를 나타냅니다. Recall이 높으면 양성 샘플을 거의 놓치지 않습니다.<br><br>
    둘은 <b>트레이드오프</b> 관계입니다. threshold를 낮추면 더 많이 양성으로 예측하므로 Recall이 올라가지만 Precision은 내려갑니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      📊 <b>Precision 예시</b> — 100명 양성 예측 중 70명이 실제 양성 → Precision = 70/100 = 0.7
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      📊 <b>Recall 예시</b> — 실제 양성 80명 중 70명 탐지 → Recall = 70/80 = 0.875
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155;">
      ⚖️ <b>트레이드오프</b> — threshold 낮추면 → Recall↑, Precision↓ &nbsp;/&nbsp; threshold 높이면 → Precision↑, Recall↓
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">Precision = 예측한 양성 중 진짜 양성 비율 / Recall = 실제 양성 중 잡아낸 비율. 둘은 트레이드오프 관계입니다.</div>
</div>
