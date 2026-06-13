<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Sigmoid 출력값을 직접 확인해보자</h3>
  <div style="line-height: 2.0; color: #334155; font-size: 14px;">
    z값을 바꿔보세요. 어떤 값이 들어와도 시그모이드 함수가 <b>0과 1 사이</b>로 압축하는 것을 확인할 수 있습니다.<br>
    z가 <b>0</b>일 때 <b>0.5</b>, 양수로 커질수록 <b>1</b>에 가까워지고, 음수로 작아질수록 <b>0</b>에 가까워집니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎚️ <b>슬라이더</b>: z — 시그모이드 함수에 들어가는 입력값. 선형 변환 w·X + b의 결과입니다. (-10 ~ 10)
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155; line-height: 1.8;">
      <b>관찰 포인트</b><br>
      · z = <b>0</b> → σ(z) = <b>0.5</b> (정중앙)<br>
      · z = <b>10</b> → σ(z) ≈ <b>1.000</b> (거의 1)<br>
      · z = <b>-10</b> → σ(z) ≈ <b>0.000</b> (거의 0)<br>
      · z가 ±5를 넘어가면 기울기가 거의 0 → 기울기 소실 구간
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">z=0 → 0.5 / z 크면 → 1 / z 작으면 → 0. 항상 0과 1 사이로 압축됩니다.</div>
</div>
