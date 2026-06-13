<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">로지스틱 회귀 — 이름은 회귀지만 분류 모델</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    로지스틱 회귀는 이름에 '회귀'가 들어 있지만 <b>분류 모델</b>입니다.<br><br>
    내부적으로 선형 방정식
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 8px; border-radius: 6px; font-family: monospace;">w·X + b</span>
    를 계산하고, 그 결과를 <b>시그모이드 함수</b>에 통과시켜 0과 1 사이의 확률로 바꿉니다.<br><br>
    이 확률값에 threshold를 적용해서 최종 클래스를 결정합니다. sklearn에서는
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">LogisticRegression()</span>
    으로 바로 사용할 수 있습니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🔄 <b>내부 흐름</b> — X 입력 → w·X + b → 시그모이드 → 확률(0~1) → threshold → 클래스 0 or 1
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155;">
      ❓ <b>이름이 헷갈리는 이유</b> — 계산 방식은 회귀처럼 선형이지만, 출력이 확률 → 분류 문제에 사용
    </div>
  </div>
</div>

<br>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 12px; overflow: hidden; font-family: 'JetBrains Mono', monospace; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 10px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #6060a0; margin-left: 8px; font-size: 12px;">📄 reference.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; font-family: 'Nunito', sans-serif;">
      참고 코드 ← 보고 채워요
    </div>
  </div>
  <div style="padding: 15px; color: #cdd6f4; font-size: 13px; line-height: 1.6; overflow-x: auto;">
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><span style="color: #cba6f7;">from</span> sklearn.linear_model <span style="color: #cba6f7;">import</span> LogisticRegression

<span style="color: #545478; font-style: italic;"># 모델 생성 — 수식 구현 없이 한 줄로</span>
model = LogisticRegression()

<span style="color: #545478; font-style: italic;"># 내부 흐름: X → w·X+b → 시그모이드 → 확률 → threshold → 클래스</span>
model.fit(X_train, y_train)
preds = model.predict(X_test)  <span style="color: #545478; font-style: italic;"># [1, 0, 1, 0, ...]</span></code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">로지스틱 회귀 = 분류 모델. 선형 계산 → 시그모이드 → 확률 → threshold → 클래스 결정.</div>
</div>
