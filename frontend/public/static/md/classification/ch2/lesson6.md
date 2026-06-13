<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">threshold를 바꾸면 predict 결과가 달라진다</h3>
  <div style="line-height: 2.0; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 8px; border-radius: 6px; font-family: monospace;">predict_proba</span>
    로 얻은 확률값과 threshold를 직접 바꿔보세요.<br>
    sklearn의
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 8px; border-radius: 6px; font-family: monospace;">predict()</span>
    는 threshold=0.5가 고정이지만, 확률값에 직접 threshold를 적용하면 기준을 바꿀 수 있습니다.<br>
    <b>같은 확률값</b>이라도 threshold에 따라 클래스 1이 되기도 하고 클래스 0이 되기도 합니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎚️ <b>슬라이더 1</b>: predict_proba 출력값 — 모델이 출력한 클래스 1에 속할 확률 (0.01 ~ 0.99)
    </div>
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎚️ <b>슬라이더 2</b>: Threshold — 이 값 이상이면 클래스 1, 미만이면 클래스 0으로 결정 (0.10 ~ 0.90)
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155; line-height: 1.8;">
      <b>관찰 포인트</b><br>
      · 확률 <b>0.60</b>, threshold <b>0.5</b> → 0.60 ≥ 0.5 → 클래스 1<br>
      · 확률 <b>0.60</b>, threshold <b>0.7</b> → 0.60 &lt; 0.7 → 클래스 0 ← 같은 확률인데 결과가 바뀜!<br>
      · threshold를 <b>낮출수록</b> 클래스 1로 예측되는 경우가 많아짐<br>
      · threshold를 <b>높일수록</b> 클래스 1로 예측되는 경우가 적어짐
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">predict()는 threshold=0.5 고정. predict_proba()로 확률을 직접 받아 threshold를 자유롭게 바꿀 수 있습니다.</div>
</div>
