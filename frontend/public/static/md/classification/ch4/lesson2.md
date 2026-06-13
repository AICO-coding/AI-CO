<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">분류에 MSE를 쓰면 안 되는 이유</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    회귀에서는 예측값과 정답의 차이를 제곱한
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 6px; font-weight: 700;">MSE</span>
    를 Loss로 씁니다. 분류에도 그냥 MSE를 쓰면 안 될까요?<br><br>
    분류 모델의 출력은 시그모이드를 통과한 확률값입니다. 시그모이드는 S자 곡선 모양이라 MSE와 합쳐지면 Loss 곡선이 <b>울퉁불퉁</b>해집니다. 울퉁불퉁한 곡선에는 가짜 최솟값(local minimum)이 많아서 학습이 엉뚱한 곳에서 멈출 수 있습니다.<br><br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-weight: 700;">Binary Cross Entropy Loss</span>
    는 시그모이드 출력과 궁합이 맞도록 설계되어 Loss 곡선이 <b>매끄럽게</b> 만들어집니다. 학습이 안정적으로 최솟값을 찾아갑니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #fee2e2; border-radius: 12px; padding: 12px 15px; color: #991b1b;">
      ❌ <b>MSE의 문제</b> — 시그모이드 + MSE → Loss 곡선이 울퉁불퉁 → 학습이 엉뚱한 곳에서 멈출 수 있음
    </div>
    <div style="background: #dcfce7; border-radius: 12px; padding: 12px 15px; color: #166534;">
      ✅ <b>BCE의 장점</b> — 시그모이드 + BCE → Loss 곡선이 매끄러움 → 학습이 안정적으로 최솟값을 찾아감
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      📌 <b>결론</b> — 분류 문제에는 항상 Binary Cross Entropy Loss를 씁니다
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">시그모이드 + MSE = Loss 곡선 울퉁불퉁 → 학습 불안정. 분류에는 BCE Loss를 써야 합니다.</div>
</div>
