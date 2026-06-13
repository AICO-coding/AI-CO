<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Loss — 모델이 얼마나 틀렸는지를 숫자로</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    모델을 학습시키려면 '현재 모델이 얼마나 틀렸는지'를 숫자로 나타내야 합니다. 그 숫자가
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Loss (손실)</span>
    입니다.<br><br>
    Loss가 크면 예측이 실제 레이블과 많이 다른 것입니다. Loss가 0에 가까우면 예측이 정답에 가까운 것입니다. 학습은 이 Loss를 줄이는 방향으로 가중치를 반복해서 업데이트하는 과정입니다.<br><br>
    Loss가 없으면 모델이 얼마나 틀렸는지 알 방법이 없습니다. 방향도 모르고 가중치를 바꾸는 것은 눈 감고 다트를 던지는 것과 같습니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      🎯 <b>Loss의 역할</b> — 예측값과 실제 레이블의 차이를 숫자로 표현 → 이 숫자를 줄이는 방향으로 가중치 업데이트
    </div>
    <div style="background: #fee2e2; border-radius: 8px; padding: 10px 14px; color: #991b1b;">
      📈 <b>Loss가 클 때</b> — 모델 예측: 0.02 / 실제 레이블: 1 → 완전히 틀림 → Loss 큼 → 가중치 크게 수정
    </div>
    <div style="background: #dcfce7; border-radius: 8px; padding: 10px 14px; color: #166534;">
      📉 <b>Loss가 작을 때</b> — 모델 예측: 0.95 / 실제 레이블: 1 → 거의 맞음 → Loss 작음 → 가중치 조금 수정
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; color: #334155;">
      ⚖️ <b>회귀 vs 분류</b> — 회귀: MSE(평균 제곱 오차) 사용 / 분류: Binary Cross Entropy Loss 사용
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">Loss = 예측값과 정답의 차이를 나타내는 숫자. 학습은 Loss를 줄이는 방향으로 가중치를 반복 업데이트하는 과정입니다.</div>
</div>
