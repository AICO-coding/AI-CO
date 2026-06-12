<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">PyTorch에서 BCE Loss 쓰기</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    PyTorch에서는
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">nn.BCELoss()</span>
    로 BCE Loss를 바로 사용할 수 있습니다. 모델 출력값(시그모이드를 통과한 확률)과 실제 레이블을 넣으면 Loss를 계산해줍니다.<br><br>
    주의할 점이 있습니다.
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 6px; font-family: monospace;">nn.BCELoss()</span>
    는 모델 출력이 반드시 <b>0~1 사이의 확률값</b>이어야 합니다. 시그모이드를 통과하지 않은 raw 값(logit)을 넣으면 오류가 납니다.<br><br>
    logit을 바로 넣고 싶을 때는
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">nn.BCEWithLogitsLoss()</span>
    를 씁니다. 이 경우 출력층에 Sigmoid를 붙이지 않아도 됩니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      criterion = nn.BCELoss()<br>
      loss = criterion(pred, y)  # pred는 Sigmoid 통과한 확률값
    </div>
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      criterion = nn.BCEWithLogitsLoss()<br>
      loss = criterion(logit, y)  # logit은 Sigmoid 통과 전 raw 값
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155;">
      💼 <b>실무 팁</b> — nn.BCEWithLogitsLoss가 수치적으로 더 안정적이라 실무에서 더 많이 씁니다
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">nn.BCELoss() → Sigmoid 통과한 확률값 입력. nn.BCEWithLogitsLoss() → raw logit 입력 (Sigmoid 불필요). 실무는 후자 선호.</div>
</div>
