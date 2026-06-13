<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">모델 복잡도를 바꾸면 어떻게 되는가?</h3>
  <div style="line-height: 2.0; color: #334155; font-size: 14px;">
    모델 복잡도(층 수)를 바꿔보세요.<br>
    복잡도가 <b>너무 낮으면</b> train/test 정확도가 모두 낮고(underfitting),<br>
    <b>너무 높으면</b> train은 높지만 test가 낮아집니다(overfitting).<br>
    적절한 복잡도를 찾는 것이 목표입니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 8px; padding: 10px 14px; color: #334155;">
      🎚️ <b>슬라이더</b>: 모델 복잡도 (층 수) — 신경망의 은닉층 수. 늘릴수록 모델이 복잡해집니다. (1 ~ 10층)
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; color: #334155; line-height: 1.8;">
      <b>관찰 포인트</b><br>
      · 층 수 <b>1~2</b> → train/test 모두 낮음 → underfitting<br>
      · 층 수 <b>3~5</b> → train/test 모두 높음 → 이상적<br>
      · 층 수 <b>8~10</b> → train 높음, test 낮음 → overfitting
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">복잡도 너무 낮으면 underfitting, 너무 높으면 overfitting. train/test 정확도를 함께 보면서 적절한 복잡도를 찾아야 합니다.</div>
</div>
