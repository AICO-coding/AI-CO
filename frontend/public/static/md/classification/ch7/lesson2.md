<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Variance(분산) — 모델이 너무 복잡할 때</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Variance</span>
    는 모델이 훈련 데이터에 얼마나 민감하게 반응하는지를 나타냅니다. Variance가 높으면 훈련 데이터는 거의 완벽하게 맞추지만, 본 적 없는 데이터에서 성능이 크게 떨어집니다. 이를
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 4px; font-weight: 700;">과적합 (overfitting)</span>
    이라고 합니다.<br><br>
    모델이 <b>너무 복잡할 때</b> 발생합니다. 훈련 데이터의 노이즈까지 전부 외워버려서 새 데이터에 일반화가 되지 않는 상태입니다.<br><br>
    High Variance 상황에서는 <b>훈련 정확도는 높지만 테스트 정확도가 크게 낮습니다.</b> train과 test 정확도의 차이가 크면 overfitting을 의심해야 합니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #fee2e2; border-radius: 8px; padding: 10px 14px; color: #991b1b;">
      📉 <b>High Variance 증상</b> — train 정확도 높음 + test 정확도 낮음 → 훈련 데이터에만 맞춰짐
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; color: #334155;">
      🧩 <b>비유</b> — 연습문제 답을 통째로 외운 학생. 실전 시험에서 조금만 변형돼도 틀림
    </div>
    <div style="background: #dcfce7; border-radius: 8px; padding: 10px 14px; color: #166534;">
      🔧 <b>해결 방법</b> — 데이터 더 수집 / Dropout 추가 / L2 규제 강화 / 층·뉴런 수 줄이기 / Early Stopping
    </div>
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      📌 <b>진단 방법</b> — train 높은데 test 낮은가? → YES → High Variance (overfitting)
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">High Variance = overfitting. train 높음, test 낮음. 훈련 데이터를 통째로 외워서 새 데이터에 일반화 안 됨.</div>
</div>
