<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">학습 루프 — 4단계를 반복한다</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    PyTorch 학습은 매 에폭(epoch)마다 같은 4단계를 반복합니다. <b>이 순서는 반드시 지켜야 합니다.</b>
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      <b>① optimizer.zero_grad()</b> — 이전 스텝의 기울기를 초기화합니다. PyTorch는 기울기를 자동으로 리셋하지 않기 때문에 매 스텝마다 직접 초기화해야 합니다. 안 하면 기울기가 누적되어 잘못된 방향으로 업데이트됩니다.
    </div>
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      <b>② pred = model(x)</b> — 모델에 입력을 넣어 예측값을 얻습니다.
    </div>
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      <b>③ loss = criterion(pred, y)</b> — 예측값과 실제 레이블로 Loss를 계산합니다.
    </div>
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      <b>④ loss.backward() → optimizer.step()</b> — 역전파로 기울기를 계산하고, 가중치를 업데이트합니다.
    </div>
    <div style="background: #f1f5f9; border-radius: 8px; padding: 10px 14px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      for epoch in range(100):<br>
      &nbsp;&nbsp;&nbsp;&nbsp;optimizer.zero_grad()&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 1. 기울기 초기화<br>
      &nbsp;&nbsp;&nbsp;&nbsp;pred = model(X_train)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 2. 예측<br>
      &nbsp;&nbsp;&nbsp;&nbsp;loss = criterion(pred, y_train)&nbsp;&nbsp;# 3. Loss 계산<br>
      &nbsp;&nbsp;&nbsp;&nbsp;loss.backward()&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 4. 역전파<br>
      &nbsp;&nbsp;&nbsp;&nbsp;optimizer.step()&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 5. 가중치 업데이트
    </div>
    <div style="background: #fee2e2; border-radius: 8px; padding: 10px 14px; color: #991b1b;">
      ⚠️ <b>zero_grad 빠트리면</b> — 기울기가 매 스텝 누적 → 잘못된 방향으로 업데이트 → 학습 망가짐
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; color: #334155;">
      🔄 <b>epoch 의미</b> — 전체 훈련 데이터를 한 번 다 훑는 것. 100 epoch = 훈련 데이터를 100번 반복 학습
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">zero_grad → 예측 → Loss → backward → step. 이 순서는 절대 바꾸면 안 됩니다. zero_grad를 빠트리면 학습이 망가집니다.</div>
</div>
