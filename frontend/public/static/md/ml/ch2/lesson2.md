<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">왜 데이터를 나눠야 할까?</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    시험 문제를 미리 알고 시험을 보면 점수가 실제 실력보다 높게 나옵니다. 모델도 똑같습니다. 학습에 쓴 데이터로 성능을 평가하면 점수가 부풀려집니다. 모델이 정답을 이미 봤기 때문입니다.<br><br>
    그래서 데이터를 두 덩어리로 나눕니다.
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-weight: 700;">훈련용(train)</span>
    으로 모델을 학습시키고,
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 6px; font-weight: 700;">테스트용(test)</span>
    으로 처음 보는 데이터에서의 성능을 측정합니다.<br><br>
    sklearn의 <b>train_test_split()</b>이 이 역할을 합니다. <b>test_size=0.2</b>는 전체의 20%를 테스트용으로 쓴다는 뜻입니다.<br>
    <b>random_state</b>는 분할 방식을 고정하는 시드값입니다. 같은 숫자를 쓰면 항상 같은 방식으로 나뉩니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155;">
      📚 <b>비유</b> — 훈련 데이터 = 연습문제 / 테스트 데이터 = 실전 시험. 연습문제로 실력을 평가하면 안 됨
    </div>
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      📐 <b>결과 shape</b> — 전체 100개 → X_train.shape: (80, 5) / X_test.shape: (20, 5)
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🔒 <b>random_state 의미</b> — random_state=42 → 항상 같은 방식으로 분할 → 팀원과 결과 재현 가능
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">학습에 쓴 데이터로 평가하면 점수가 부풀려집니다. train으로 학습, test로 평가. 절대 섞으면 안 됩니다.</div>
</div>
