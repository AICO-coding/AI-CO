<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Softmax 출력을 직접 확인해보자</h3>
  <div style="line-height: 2.0; color: #334155; font-size: 14px;">
    세 클래스의 logit 값을 바꿔보세요.<br>
    Softmax가 점수들을 <b>합이 1인 확률</b>로 변환하는 것을 확인할 수 있습니다.<br>
    한 클래스의 logit을 높이면 <b>그 클래스의 확률이 올라가고 나머지는 내려갑니다.</b>
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎚️ <b>슬라이더 1</b>: 클래스 0 logit — 클래스 0에 대한 모델의 점수 (-5 ~ 5)
    </div>
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎚️ <b>슬라이더 2</b>: 클래스 1 logit — 클래스 1에 대한 모델의 점수 (-5 ~ 5)
    </div>
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎚️ <b>슬라이더 3</b>: 클래스 2 logit — 클래스 2에 대한 모델의 점수 (-5 ~ 5)
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155; line-height: 1.8;">
      <b>관찰 포인트</b><br>
      · 세 logit이 같으면 → 확률이 모두 약 <b>0.333</b> (균등 분포)<br>
      · 클래스 0 logit을 크게 올리면 → 클래스 0 확률 급등, 나머지 내려감<br>
      · 세 확률의 합은 항상 <b>1.0</b>
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">logit이 높을수록 해당 클래스 확률이 높아집니다. 세 확률의 합은 항상 1입니다.</div>
</div>
