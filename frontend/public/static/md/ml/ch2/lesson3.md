<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">로지스틱 회귀 — 이름은 회귀지만 분류 모델</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    로지스틱 회귀는 이름에 '회귀'가 들어 있지만 <b>분류 모델</b>입니다.<br><br>
    내부적으로 선형 방정식
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 8px; border-radius: 6px; font-family: monospace;">w·X + b</span>
    를 계산하고, 그 결과를 <b>시그모이드 함수</b>에 통과시켜 0과 1 사이의 확률로 바꿉니다. 챕터 1에서 배운 바로 그 확률값입니다.<br><br>
    이 확률값에 threshold를 적용해서 최종 클래스를 결정합니다. sklearn에서는
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">LogisticRegression()</span>
    으로 바로 사용할 수 있습니다. 수식을 직접 구현하지 않아도 됩니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🔄 <b>내부 흐름</b> — X 입력 → w·X + b → 시그모이드 → 확률(0~1) → threshold → 클래스 0 or 1
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155;">
      ❓ <b>이름이 헷갈리는 이유</b> — 계산 방식은 회귀처럼 선형이지만, 출력이 확률 → 분류 문제에 사용
    </div>
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      from sklearn.linear_model import LogisticRegression<br>
      model = LogisticRegression()
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">로지스틱 회귀 = 분류 모델. 선형 계산 → 시그모이드 → 확률 → threshold → 클래스 결정.</div>
</div>
