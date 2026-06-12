<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">BCE Loss를 직접 계산해보자</h3>
  <div style="line-height: 2.0; color: #334155; font-size: 14px;">
    실제 레이블(y)과 모델의 예측 확률(p)을 바꿔보세요.<br>
    예측이 <b>정답에 가까울수록</b> Loss가 낮아지고, <b>틀릴수록</b> 급격히 커지는 것을 확인할 수 있습니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎚️ <b>슬라이더 1</b>: 실제 레이블 y — 샘플의 실제 정답 클래스 (0 또는 1)
    </div>
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎚️ <b>슬라이더 2</b>: 예측 확률 p — 모델이 출력한 클래스 1일 확률 (0.01 ~ 0.99)
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155; line-height: 1.8;">
      <b>관찰 포인트</b><br>
      · y=1, p=0.95 → Loss ≈ <b>0.05</b> (잘 맞춤)<br>
      · y=1, p=0.50 → Loss ≈ <b>0.69</b> (애매한 예측)<br>
      · y=1, p=0.05 → Loss ≈ <b>3.00</b> (완전히 틀림)<br>
      · y=0일 때는 p가 낮을수록 Loss가 낮아지는 것을 확인해보세요
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">확신을 갖고 맞추면 Loss ≈ 0. 확신을 갖고 틀리면 Loss가 매우 커집니다. 애매한 예측(p≈0.5)은 중간 정도의 Loss를 냅니다.</div>
</div>
