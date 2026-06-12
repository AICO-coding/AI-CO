<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">X와 y — 모델에 넣는 데이터의 형태</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    sklearn 모델을 쓰려면 데이터가 정해진 형태여야 합니다. 입력 데이터 X와 정답 레이블 y, 두 가지가 필요합니다.<br><br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-weight: 700;">X</span>
    는 <b>2차원 배열</b>입니다. 행은 샘플(데이터 1개), 열은 특성(feature)입니다. 환자 100명의 데이터에 특성이 5개라면 X의 shape은 <b>(100, 5)</b>입니다.<br><br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 6px; font-weight: 700;">y</span>
    는 <b>1차원 배열</b>입니다. 각 샘플의 정답 클래스 번호가 담깁니다. 환자 100명이면 y의 shape은 <b>(100,)</b>이고, 값은 0 또는 1입니다.<br><br>
    이 구조를 모르면 나중에 코드를 써도 왜 그렇게 쓰는지 이해할 수 없습니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      📐 <b>X shape 읽는 법</b> — X.shape = (100, 5) → 샘플 100개, 특성 5개
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      📐 <b>y shape 읽는 법</b> — y.shape = (100,) → 샘플 100개의 정답. 값은 0(정상) 또는 1(악성)
    </div>
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      print(X.shape)  # (100, 5)<br>
      print(y.shape)  # (100,)<br>
      print(y[:5])    # [0, 1, 0, 0, 1]
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">X는 (샘플 수, 특성 수)의 2차원 배열. y는 (샘플 수,)의 1차원 배열. 값은 0 또는 1.</div>
</div>
