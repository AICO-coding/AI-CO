<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">레이블(Label)이란?</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-weight: 700;">레이블 (Label)</span>
    — 훈련 데이터에서 각 샘플의 <b>정답</b>입니다.<br><br>
    모델을 학습시키려면 <b>입력(X)</b>과 <b>정답(y)</b>이 필요합니다. 이 정답 y가 바로 레이블입니다.<br><br>
    모델은 자신이 예측한 값과 실제 레이블을 비교해서 틀렸는지 맞았는지를 판단합니다.<br>
    틀리면 <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 6px; font-weight: 700;">loss</span> 가 발생하고, loss를 줄이는 방향으로 가중치가 업데이트되며 학습이 진행됩니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🍎 <b>입력(X)</b>: 사과 사진 &nbsp;→&nbsp; <b>레이블(y)</b>: <span style="color: #1681c4; font-weight: 700;">사과</span>
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🐱 <b>입력(X)</b>: 고양이 사진 &nbsp;→&nbsp; <b>레이블(y)</b>: <span style="color: #1681c4; font-weight: 700;">고양이</span>
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155; line-height: 1.8;">
      🔄 <b>학습 흐름</b><br>
      모델 예측: <span style="color: #FF6B00; font-weight: 700;">고양이</span> &nbsp;/&nbsp; 실제 레이블: <span style="color: #1681c4; font-weight: 700;">강아지</span><br>
      → 예측이 틀림 → <span style="color: #FF6B00; font-weight: 700;">loss</span> 계산 → 모델 가중치 업데이트 → 다음엔 더 잘 맞추도록 학습
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">레이블 = 정답. 모델은 예측값과 레이블을 비교해서 틀리면 스스로 수정하며 학습합니다.</div>
</div>
