<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Dropout Rate — 과적합 방지 실험</h3>

  <div style="line-height: 1.85; color: #334155; font-size: 14px; margin-bottom: 16px;">
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 1px 6px; border-radius: 4px; font-family: 'JetBrains Mono', monospace; font-size: 12.5px;">Dropout(p)</span>의 p 값을 바꾸면<br>
    train loss와 val loss의 <b style="color: #1681c4;">gap이 어떻게 변하는지</b> 직접 확인해봐요.
  </div>

  <div style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 16px;">
    <div style="background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 10px 14px; font-size: 13px; display: flex; justify-content: space-between; align-items: center;">
      <span style="font-family: 'JetBrains Mono', monospace; color: #e11d48; font-weight: 800;">p = 0.0</span>
      <span style="color: #64748b;">Dropout 없음 → 과적합 가장 심함</span>
    </div>
    <div style="background: #fff8f0; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; font-size: 13px; display: flex; justify-content: space-between; align-items: center;">
      <span style="font-family: 'JetBrains Mono', monospace; color: #FF6B00; font-weight: 800;">p = 0.2</span>
      <span style="color: #64748b;">약한 정규화 → 일반적인 시작점</span>
    </div>
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 10px 14px; font-size: 13px; display: flex; justify-content: space-between; align-items: center;">
      <span style="font-family: 'JetBrains Mono', monospace; color: #1681c4; font-weight: 800;">p = 0.5</span>
      <span style="color: #64748b;">절반 끄기 → gap 줄어들지만 학습 느려짐</span>
    </div>
    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 14px; font-size: 13px; display: flex; justify-content: space-between; align-items: center;">
      <span style="font-family: 'JetBrains Mono', monospace; color: #64748b; font-weight: 800;">p = 0.8</span>
      <span style="color: #64748b;">너무 많이 끄면 → 과소적합 위험</span>
    </div>
  </div>

  <div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 12px 14px; border-radius: 10px; color: #0f172a; font-weight: bold; font-size: 13px; display: flex; align-items: flex-start; gap: 10px;">
    <div style="color: #FF6B00; font-size: 16px; margin-top: -2px;">⚡</div>
    <div style="line-height: 1.6;">슬라이더를 움직이면서 train/val loss gap이 어떻게 달라지는지 확인해봐요!</div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <div style="color: #94a3b8; font-size: 12px; font-weight: 800; margin-bottom: 6px; display: flex; align-items: center; gap: 5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.6;">
    미션에서 Dropout rate를 직접 튜닝할 수 있어요.<br>
    val loss가 train loss보다 많이 높으면 과적합 신호예요.
  </div>
</div>