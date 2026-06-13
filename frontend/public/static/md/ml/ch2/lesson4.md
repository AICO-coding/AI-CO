<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">fit과 predict</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    sklearn의 모든 지도학습 모델은 동일한 두 단계 인터페이스를 따릅니다.<br><br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">fit(X_train, y_train)</span>
    — 훈련 데이터로 가중치 w와 b를 학습시킵니다. 이 한 줄이 실제 학습 전체입니다.<br><br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">predict(X_test)</span>
    — 학습된 모델로 테스트 데이터의 클래스를 예측합니다. 결과는 클래스 번호(0 또는 1)로 반환됩니다. 내부적으로 threshold=0.5가 적용되어 있습니다.<br><br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">score(X_test, y_test)</span>
    — 정확도(Accuracy)를 바로 계산해줍니다. 전체 샘플 중 올바르게 예측한 비율입니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      model.fit(X_train, y_train)  # 훈련 데이터로 가중치 학습
    </div>
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      model.predict(X_test)  # → [1, 0, 1, 0, 1]  클래스 번호 반환
    </div>
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      model.score(X_test, y_test)  # → 0.85  정확도 반환
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155;">
      ⚠️ <b>주의</b> — fit은 반드시 train 데이터로, score/predict는 test 데이터로. 순서 바꾸면 안 됨
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">fit → 학습 / predict → 클래스 예측 / score → 정확도. fit은 반드시 훈련 데이터로만.</div>
</div>
