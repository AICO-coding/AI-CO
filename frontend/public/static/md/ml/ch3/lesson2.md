<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Sigmoid — 어떤 값이든 0과 1 사이로</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    시그모이드 함수는 어떤 실수값이 들어와도 <b>0과 1 사이</b>의 값으로 압축합니다.<br>
    공식:
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-weight: 700;">σ(z) = 1 / (1 + e^(-z))</span><br><br>
    z가 매우 크면 출력이 1에 가까워지고, z가 매우 작으면 0에 가까워지며, z=0이면 정확히 <b>0.5</b>가 나옵니다. 출력이 0~1 사이이기 때문에 <b>'확률'</b>로 해석할 수 있어 이진 분류의 출력층에 사용합니다.<br><br>
    단점도 있습니다. z의 절댓값이 커질수록 기울기가 거의 0에 가까워집니다. 이를
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 4px; font-weight: 700;">기울기 소실(vanishing gradient)</span>
    이라고 합니다. 기울기가 0에 가까우면 가중치가 거의 업데이트되지 않아 학습이 멈추는 것과 같아집니다. 이 때문에 은닉층에서는 잘 쓰지 않습니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 8px; padding: 10px 14px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      z =  5  → σ(z) ≈ 0.993<br>
      z =  0  → σ(z) = 0.5<br>
      z = -5  → σ(z) ≈ 0.007
    </div>
    <div style="background: #dcfce7; border-radius: 8px; padding: 10px 14px; color: #166534;">
      ✅ <b>이진 분류 출력층에 쓰는 이유</b> — 출력이 0~1 사이 → 클래스 1일 확률로 해석 가능
    </div>
    <div style="background: #fee2e2; border-radius: 8px; padding: 10px 14px; color: #991b1b;">
      ⚠️ <b>단점</b> — z가 매우 크거나 작으면 기울기 ≈ 0 → 가중치 업데이트 거의 안 됨 → 은닉층에는 부적합
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">Sigmoid = 0~1 사이 출력 → 확률로 해석 가능 → 이진 분류 출력층에 사용. 은닉층에는 기울기 소실 문제로 부적합.</div>
</div>
