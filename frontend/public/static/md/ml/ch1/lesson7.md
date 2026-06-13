<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Threshold를 직접 바꿔보자</h3>
  <div style="line-height: 2.0; color: #334155; font-size: 14px;">
    모델 출력 확률과 threshold를 직접 바꿔보세요.<br>
    <b>같은 확률값</b>이라도 threshold에 따라 클래스 1이 되기도 하고 클래스 0이 되기도 합니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 8px; padding: 10px 14px; color: #334155;">
      🎚️ <b>슬라이더 1</b>: 모델 출력 확률 (0.01 ~ 0.99)
    </div>
    <div style="background: #f1f5f9; border-radius: 8px; padding: 10px 14px; color: #334155;">
      🎚️ <b>슬라이더 2</b>: Threshold (0.10 ~ 0.90)
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; color: #334155; line-height: 1.8;">
      <b>관찰 포인트</b><br>
      · 확률 <b>0.73</b>, threshold <b>0.5</b> → 0.73 ≥ 0.5 → 클래스 1<br>
      · 확률 <b>0.73</b>, threshold <b>0.8</b> → 0.73 &lt; 0.8 → 클래스 0 ← 같은 확률인데 결과가 바뀜!<br>
      · threshold를 <b>낮출수록</b> 클래스 1로 예측되는 경우가 많아짐<br>
      · threshold를 <b>높일수록</b> 클래스 1로 예측되는 경우가 적어짐
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">모델의 확률이 같아도 threshold를 바꾸면 최종 예측이 달라집니다. threshold는 상황에 맞게 조정할 수 있습니다.</div>
</div>
