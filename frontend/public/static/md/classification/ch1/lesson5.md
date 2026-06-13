<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">확률값이 달라지면 어떻게 해석될까?</h3>
  <div style="line-height: 2.0; color: #334155; font-size: 14px;">
    모델이 출력한 확률값을 직접 바꿔보세요.<br>
    확률값이 <b>1에 가까울수록</b> 클래스 1을 강하게 확신하고,<br>
    <b>0에 가까울수록</b> 클래스 0을 강하게 확신합니다.<br>
    <b>0.5에 가까울수록</b> 모델이 판단을 못 내리고 있는 상태입니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎚️ <b>슬라이더</b>: 모델 출력 확률 (0.01 ~ 0.99)
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155; line-height: 1.8;">
      <b>관찰 포인트</b><br>
      · 0.95 이상 → 클래스 1 강하게 확신 / 클래스 0 확률 5% 미만<br>
      · 0.5 근처 → 판단을 못 내리는 불확실한 상태<br>
      · 0.05 이하 → 클래스 0 강하게 확신 / 클래스 0 확률 95% 이상
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">확률값 하나로 모델의 확신 정도를 알 수 있습니다. 0.5에 가까울수록 모델이 헷갈리고 있는 상태입니다.</div>
</div>
