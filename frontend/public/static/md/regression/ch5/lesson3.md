<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">no_grad() + R² 계산</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">torch.no_grad()</span> — gradient 계산 끄기 (메모리·속도↑)<br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">ss_res</span> — 예측 오차 제곱합<br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">ss_tot</span> — 전체 분산 제곱합
  </div>

  <div style="background-color: #0f172a; color: #c3e88d; padding: 15px; border-radius: 10px; font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.8; margin-top: 15px;">
    R² = 1 - SS_res / SS_tot<br>
    <br>
    SS_res = Σ(y - ŷ)²   ← 예측이 얼마나 틀렸나<br>
    SS_tot = Σ(y - ȳ)²   ← 평균 대비 얼마나 퍼져있나<br>
    <br>
    R² = 1.0 → 완벽한 예측<br>
    R² = 0.0 → 평균 예측과 같은 수준
  </div>

  <div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 12px 15px; border-radius: 10px; margin-top: 15px; color: #0f172a; font-weight: bold; font-size: 13px; display: flex; align-items: center; gap: 10px;">
    <span style="color: #FF6B00; font-size: 16px;">⚡</span> no_grad()는 결과값을 바꾸지 않아요. gradient 추적 비용만 없애줘요!
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
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code>model.eval()
<div style="background: rgba(255,107,0,.09); border-left: 2px solid #FF6B00; padding: 0 13px; margin: 0 -15px;"><span style="color: #cba6f7;">with</span> torch.no_grad():        <span style="color: #545478; font-style: italic;"># gradient 끄기</span></div>
    p = model(X_te)

<div style="background: rgba(255,107,0,.09); border-left: 2px solid #FF6B00; padding: 0 13px; margin: 0 -15px;">    ss_res = ((y_te - p)           **<span style="color: #fab387;">2</span>).sum()
    ss_tot = ((y_te - y_te.mean()) **<span style="color: #fab387;">2</span>).sum()</div>
    r2 = (<span style="color: #fab387;">1</span> - ss_res / ss_tot).item()
    print(<span style="color: #a6e3a1;">f"R²: {r2:.4f}"</span>)</code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <div style="color: #94a3b8; font-size: 12px; font-weight: 800; margin-bottom: 6px; display: flex; align-items: center; gap: 5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.6;">
    미션 최종 평가에서 R² 점수를 계산해요.<br>
    캘리포니아 주택 데이터에서 R² 0.7 이상이면 좋은 모델이에요!
  </div>
</div>