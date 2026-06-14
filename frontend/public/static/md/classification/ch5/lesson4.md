<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">학습 루프 — 4단계를 반복한다</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    PyTorch 학습은 매 에폭(epoch)마다 같은 4단계를 반복합니다. <b>이 순서는 반드시 지켜야 합니다.</b>
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      <b>① optimizer.zero_grad()</b> — 이전 스텝의 기울기 초기화. 안 하면 기울기 누적 → 학습 망가짐
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      <b>② pred = model(x)</b> — 모델에 입력을 넣어 예측값 획득
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      <b>③ loss = criterion(pred, y)</b> — 예측값과 실제 레이블로 Loss 계산
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      <b>④ loss.backward() → optimizer.step()</b> — 역전파 + 가중치 업데이트
    </div>
    <div style="background: #fee2e2; border-radius: 12px; padding: 12px 15px; color: #991b1b;">
      ⚠️ <b>zero_grad 빠트리면</b> — 기울기 누적 → 잘못된 방향으로 업데이트 → 학습 망가짐
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
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; font-family: 'Nunito', sans-serif;">참고 코드 ← 보고 채워요</div>
  </div>
  <div style="padding: 15px; color: #cdd6f4; font-size: 13px; line-height: 1.6; overflow-x: auto;">
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code>criterion = nn.BCELoss()

<span style="color: #cba6f7;">for</span> epoch <span style="color: #cba6f7;">in</span> <span style="color: #cba6f7;">range</span>(<span style="color: #fab387;">100</span>):
    optimizer.zero_grad()              <span style="color: #545478; font-style: italic;"># ① 기울기 초기화</span>
    pred = model(X_train)              <span style="color: #545478; font-style: italic;"># ② 예측</span>
    loss = criterion(pred, y_train)    <span style="color: #545478; font-style: italic;"># ③ Loss 계산</span>
    loss.backward()                    <span style="color: #545478; font-style: italic;"># ④ 역전파</span>
    optimizer.step()                   <span style="color: #545478; font-style: italic;"># ⑤ 가중치 업데이트</span>

    <span style="color: #cba6f7;">if</span> epoch % <span style="color: #fab387;">10</span> == <span style="color: #fab387;">0</span>:
        print(<span style="color: #fab387;">f"epoch {epoch}, loss: {loss.item():.4f}"</span>)</code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">zero_grad → 예측 → Loss → backward → step. 이 순서는 절대 바꾸면 안 됩니다.</div>
</div>
