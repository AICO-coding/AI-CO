<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">분류 모델은 확률을 출력한다</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    분류 모델은 최종 클래스를 바로 출력하지 않습니다.<br>
    그 전에 먼저 <b>'클래스 1(양성)에 속할 확률'</b>을 계산합니다. 이 값은 반드시 <b>0과 1 사이</b>입니다.<br><br>
    확률로 출력하는 이유는 모델이 <b>얼마나 확신하는지</b> 알 수 있기 때문입니다.<br>
    두 환자 모두 '악성'으로 예측했더라도, 한 명은 99% 확신, 다른 한 명은 51% 확신이라면 의사는 다르게 대응해야 합니다.<br><br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 6px; font-family: monospace;">P(클래스 0)</span>
    = 1 -
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 6px; border-radius: 6px; font-family: monospace;">P(클래스 1)</span>
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #dcfce7; border-radius: 12px; padding: 12px 15px; color: #166534;">
      <b>0.97</b> → 97% 확률로 클래스 1 → <b>클래스 1이라고 강하게 확신</b>
    </div>
    <div style="background: #fef9c3; border-radius: 12px; padding: 12px 15px; color: #713f12;">
      <b>0.51</b> → 51% 확률로 클래스 1 → <b>거의 판단을 못 내리는 상태</b>
    </div>
    <div style="background: #fee2e2; border-radius: 12px; padding: 12px 15px; color: #991b1b;">
      <b>0.08</b> → 8% 확률로 클래스 1 → <b>클래스 0이라고 강하게 확신</b>
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      📐 <b>P(클래스 0) 계산</b> — 클래스 1 확률이 0.73이면 → 클래스 0 확률 = 1 - 0.73 = <span style="color: #1681c4; font-weight: 700;">0.27</span>
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">모델 출력값 = 클래스 1에 속할 확률. 1에 가까울수록 클래스 1 확신, 0에 가까울수록 클래스 0 확신.</div>
</div>
