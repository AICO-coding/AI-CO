<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Optimizer와 학습률(learning rate)</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Optimizer</span>
    는 Loss를 기반으로 가중치를 어떻게 업데이트할지 결정합니다. Loss가 줄어드는 방향을 계산해서 가중치를 조금씩 움직입니다.<br><br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 4px; font-weight: 700;">학습률 (learning rate, lr)</span>
    은 가중치를 한 번에 얼마나 크게 바꿀지를 결정합니다. lr이 너무 크면 Loss가 불안정하게 튀고, 너무 작으면 학습이 매우 느립니다. 일반적으로 <b>0.001</b>을 시작점으로 씁니다.<br><br>
    실무에서는
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Adam optimizer</span>
    를 가장 많이 씁니다. 학습률을 자동으로 조정하는 기능이 있어 대부분의 상황에서 잘 동작합니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 8px; padding: 10px 14px; color: #334155; font-family: monospace; font-size: 12px;">
      optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    </div>
    <div style="background: #fee2e2; border-radius: 8px; padding: 10px 14px; color: #991b1b;">
      ⬆️ <b>lr이 너무 크면</b> — 가중치가 너무 크게 변함 → Loss가 오히려 커지거나 발산
    </div>
    <div style="background: #fef9c3; border-radius: 8px; padding: 10px 14px; color: #713f12;">
      ⬇️ <b>lr이 너무 작으면</b> — 가중치가 아주 조금씩만 변함 → 학습 수렴에 매우 오랜 시간 필요
    </div>
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      🔧 <b>model.parameters()</b> — 모델 안의 모든 학습 가능한 가중치를 optimizer에 전달하는 코드
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">lr 너무 크면 발산 / 너무 작으면 학습 느림. 기본값 0.001. 실무 기본 optimizer는 Adam.</div>
</div>
