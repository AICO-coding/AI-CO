<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Bias(편향) — 모델이 너무 단순할 때</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-weight: 700;">Bias</span>
    는 모델의 예측이 실제 정답으로부터 얼마나 벗어나 있는지를 나타냅니다. Bias가 높으면 훈련 데이터조차 제대로 맞추지 못합니다. 이를
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 6px; font-weight: 700;">과소적합 (underfitting)</span>
    이라고 합니다.<br><br>
    모델이 <b>너무 단순할 때</b> 발생합니다. 복잡한 곡선 형태의 데이터를 직선 하나로 맞추려는 상황입니다. 아무리 훈련해도 직선은 곡선을 따라갈 수 없습니다.<br><br>
    High Bias 상황에서는 <b>훈련 정확도와 테스트 정확도가 모두 낮습니다.</b>
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #fee2e2; border-radius: 12px; padding: 12px 15px; color: #991b1b;">
      📉 <b>High Bias 증상</b> — train 정확도 낮음 + test 정확도 낮음 → 모델이 너무 단순
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🧩 <b>비유</b> — 복잡한 곡선 데이터를 직선으로 맞추려는 것. 아무리 학습해도 한계가 있음
    </div>
    <div style="background: #dcfce7; border-radius: 12px; padding: 12px 15px; color: #166534;">
      🔧 <b>해결 방법</b> — 더 복잡한 모델 사용 / 층·뉴런 수 늘리기 / feature 추가 / 규제 줄이기
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">High Bias = underfitting. train/test 모두 낮음. 모델이 너무 단순해서 패턴을 못 잡는 상태입니다.</div>
</div>
