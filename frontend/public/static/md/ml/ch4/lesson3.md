<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Binary Cross Entropy Loss 공식</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    BCE Loss 공식:
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-weight: 700;">L = -[y·log(p) + (1-y)·log(1-p)]</span><br>
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 6px; border-radius: 4px; font-family: monospace;">y</span> = 실제 레이블(0 또는 1) &nbsp;&nbsp;
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 6px; border-radius: 4px; font-family: monospace;">p</span> = 모델이 출력한 클래스 1 확률<br><br>
    <b>y=1(양성)</b>일 때 공식은 <b>-log(p)</b>로 단순해집니다. p가 1에 가까울수록 Loss가 0에 가까워지고, p가 0에 가까울수록 Loss가 무한히 커집니다.<br><br>
    <b>y=0(음성)</b>일 때 공식은 <b>-log(1-p)</b>로 단순해집니다. p가 0에 가까울수록 Loss가 낮아지고, p가 1에 가까울수록 Loss가 커집니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #dcfce7; border-radius: 8px; padding: 10px 14px; color: #166534;">
      ✅ <b>y=1, 잘 맞춘 경우</b> — y=1, p=0.95 → L = -log(0.95) ≈ <b>0.05</b> (Loss 낮음)
    </div>
    <div style="background: #fee2e2; border-radius: 8px; padding: 10px 14px; color: #991b1b;">
      ❌ <b>y=1, 틀린 경우</b> — y=1, p=0.05 → L = -log(0.05) ≈ <b>3.0</b> (Loss 높음)
    </div>
    <div style="background: #dcfce7; border-radius: 8px; padding: 10px 14px; color: #166534;">
      ✅ <b>y=0, 잘 맞춘 경우</b> — y=0, p=0.05 → L = -log(0.95) ≈ <b>0.05</b> (Loss 낮음)
    </div>
    <div style="background: #fee2e2; border-radius: 8px; padding: 10px 14px; color: #991b1b;">
      ❌ <b>y=0, 틀린 경우</b> — y=0, p=0.95 → L = -log(0.05) ≈ <b>3.0</b> (Loss 높음)
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">예측이 정답에 가까울수록 Loss ≈ 0. 예측이 완전히 틀릴수록 Loss가 급격히 커집니다. 맞추면 작은 벌칙, 틀리면 큰 벌칙.</div>
</div>
