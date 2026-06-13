<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">fit과 predict</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    sklearn의 모든 지도학습 모델은 동일한 두 단계 인터페이스를 따릅니다.<br><br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-weight: 700;">fit(X_train, y_train)</span>
    — 훈련 데이터로 가중치 w와 b를 학습시킵니다. 이 한 줄이 실제 학습 전체입니다.<br><br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-weight: 700;">predict(X_test)</span>
    — 학습된 모델로 테스트 데이터의 클래스를 예측합니다. 결과는 클래스 번호(0 또는 1)로 반환됩니다. 내부적으로 threshold=0.5가 적용되어 있습니다.<br><br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-weight: 700;">score(X_test, y_test)</span>
    — 정확도(Accuracy)를 바로 계산해줍니다. 전체 샘플 중 올바르게 예측한 비율입니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; color: #334155;">
      ⚠️ <b>주의</b> — fit은 반드시 train 데이터로, score/predict는 test 데이터로. 순서 바꾸면 안 됨
    </div>
  </div>
</div>

<br>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 12px; overflow: hidden; font-family: 'JetBrains Mono', monospace; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 10px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #6060a0; margin-left: 8px; font-size: 12px;">📄 reference.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; font-family: 'Nunito', sans-serif;">
      참고 코드 ← 보고 채워요
    </div>
  </div>
  <div style="padding: 15px; color: #cdd6f4; font-size: 13px; line-height: 1.6; overflow-x: auto;">
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><span style="color: #545478; font-style: italic;"># 1. 학습 — train 데이터로만</span>
model.fit(X_train, y_train)

<span style="color: #545478; font-style: italic;"># 2. 예측 — 클래스 번호 반환 (threshold=0.5 내장)</span>
preds = model.predict(X_test)
print(preds)  <span style="color: #545478; font-style: italic;"># [1, 0, 1, 0, 1]</span>

<span style="color: #545478; font-style: italic;"># 3. 정확도 — 올바르게 예측한 비율</span>
acc = model.score(X_test, y_test)
print(acc)    <span style="color: #545478; font-style: italic;"># 0.85</span></code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">fit → 학습 / predict → 클래스 예측 / score → 정확도. fit은 반드시 훈련 데이터로만.</div>
</div>
