<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">은닉층 크기 — 표현력 vs 과적합</h3>

  <div style="line-height: 1.85; color: #334155; font-size: 14px; margin-bottom: 16px;">
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 1px 6px; border-radius: 4px; font-family: 'JetBrains Mono', monospace; font-size: 12.5px;">hidden_size</span>가 클수록 모델이 더 복잡한 패턴을 학습할 수 있어요.<br>
    하지만 너무 크면 <b style="color: #e11d48;">훈련 데이터에만 맞춰지는 과적합</b>이 일어나요.
  </div>

  <div style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 16px;">
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 10px 14px; font-size: 13px; display: flex; justify-content: space-between; align-items: center;">
      <span style="font-family: 'JetBrains Mono', monospace; color: #1681c4; font-weight: 800;">hidden_size = 8</span>
      <span style="color: #64748b;">표현력 부족 → 과소적합 위험</span>
    </div>
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 10px 14px; font-size: 13px; display: flex; justify-content: space-between; align-items: center;">
      <span style="font-family: 'JetBrains Mono', monospace; color: #1681c4; font-weight: 800;">hidden_size = 32</span>
      <span style="color: #64748b;">균형 지점 (작은 데이터셋)</span>
    </div>
    <div style="background: #fff8f0; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; font-size: 13px; display: flex; justify-content: space-between; align-items: center;">
      <span style="font-family: 'JetBrains Mono', monospace; color: #FF6B00; font-weight: 800;">hidden_size = 128</span>
      <span style="color: #64748b;">train loss ↓ 이지만 val loss 벌어지기 시작</span>
    </div>
    <div style="background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px; padding: 10px 14px; font-size: 13px; display: flex; justify-content: space-between; align-items: center;">
      <span style="font-family: 'JetBrains Mono', monospace; color: #e11d48; font-weight: 800;">hidden_size = 512</span>
      <span style="color: #64748b;">과적합 — val loss 높아지고 일반화 실패</span>
    </div>
  </div>

  <div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 12px 14px; border-radius: 10px; color: #0f172a; font-weight: bold; font-size: 13px; display: flex; align-items: flex-start; gap: 10px;">
    <div style="color: #FF6B00; font-size: 16px; margin-top: -2px;">⚡</div>
    <div style="line-height: 1.6;">슬라이더를 움직이면서 train loss와 val loss의 차이(gap)를 직접 확인해보세요!</div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <div style="color: #94a3b8; font-size: 12px; font-weight: 800; margin-bottom: 6px; display: flex; align-items: center; gap: 5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.6;">
    미션에서 hidden_size를 직접 튜닝할 수 있어요.<br>
    val loss가 올라가기 시작하는 지점이 과적합 시작 신호예요.
  </div>
</div>