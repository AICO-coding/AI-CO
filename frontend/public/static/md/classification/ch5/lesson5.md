<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">학습률이 달라지면 어떻게 되는가?</h3>
  <div style="line-height: 2.0; color: #334155; font-size: 14px;">
    학습률(lr)을 바꿔보세요.<br>
    lr이 <b>너무 크면</b> Loss가 줄어들지 않고 튀고, <b>너무 작으면</b> 학습이 매우 느립니다.<br>
    적절한 lr을 찾는 것이 학습의 핵심 중 하나입니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎚️ <b>슬라이더</b>: 학습률 (learning rate) — 가중치를 한 번에 얼마나 크게 바꿀지 결정합니다 (0.0001 ~ 1.0)
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155; line-height: 1.8;">
      <b>관찰 포인트</b><br>
      · lr = <b>0.001</b> → Loss가 안정적으로 감소 (일반적인 시작점)<br>
      · lr = <b>0.1 이상</b> → Loss가 불안정하게 튀거나 오히려 증가<br>
      · lr = <b>0.00001</b> → Loss가 아주 천천히 줄어듦 (수렴까지 오래 걸림)
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">lr 크면 발산, 작으면 느림. 0.001이 일반적인 출발점. Adam은 lr을 자동 조정해서 선호됩니다.</div>
</div>
