<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Threshold — 확률을 클래스로 변환하는 기준</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    확률은 0과 1 사이의 연속적인 숫자입니다.<br>
    그런데 최종 예측은 <b>클래스 0 또는 클래스 1</b> 중 하나여야 합니다.<br>
    이 확률값을 최종 클래스로 변환하는 기준이
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-weight: 700;">threshold (임계값)</span>
    입니다.<br><br>
    기본값은 <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 6px; font-family: monospace; font-size: 13px;">0.5</span> 입니다.<br>
    확률 <b>≥ 0.5</b> → 클래스 1 (양성) &nbsp;&nbsp; 확률 <b>< 0.5</b> → 클래스 0 (음성)
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #dcfce7; border-radius: 12px; padding: 12px 15px; color: #166534;">
      확률 <b>0.73</b> → 0.73 ≥ 0.5 → <b>클래스 1 (양성)</b>
    </div>
    <div style="background: #fee2e2; border-radius: 12px; padding: 12px 15px; color: #991b1b;">
      확률 <b>0.34</b> → 0.34 &lt; 0.5 → <b>클래스 0 (음성)</b>
    </div>
    <div style="background: #fef9c3; border-radius: 12px; padding: 12px 15px; color: #713f12;">
      확률 <b>0.50</b> → 0.50 ≥ 0.5 → <b>클래스 1 (양성)</b> &nbsp; ← 경계값은 양성으로 처리
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155; line-height: 1.8;">
      ⚙️ <b>threshold는 바꿀 수 있습니다</b><br>
      · threshold <b>낮추면(0.3)</b> → 더 많이 양성으로 분류 → 암 진단처럼 놓치면 안 될 때<br>
      · threshold <b>높이면(0.7)</b> → 더 적게 양성으로 분류 → 확실한 경우만 양성으로 판정<br>
      → 자세한 내용은 <b>챕터 6 (평가지표)</b>에서 다룹니다.
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">확률 ≥ threshold → 클래스 1 / 확률 < threshold → 클래스 0. 기본 threshold = 0.5.</div>
</div>
