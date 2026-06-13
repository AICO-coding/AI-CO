<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">predict_proba — 확률값으로 받기</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 8px; border-radius: 6px; font-family: monospace;">predict()</span>
    는 클래스 번호만 돌려줍니다. 모델이 얼마나 확신하는지는 알 수 없습니다. 확률값이 필요할 때는
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">predict_proba()</span>
    를 씁니다.<br><br>
    결과는 <b>2열짜리 배열</b>입니다. 첫 번째 열이 클래스 0 확률, 두 번째 열이 클래스 1 확률입니다. 두 값의 합은 항상 1입니다.<br><br>
    클래스 1 확률만 꺼내려면
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 6px; font-family: monospace;">[:, 1]</span>
    로 슬라이싱합니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      📋 <b>열 의미</b> — 열 0 = 클래스 0 확률 / 열 1 = 클래스 1 확률. 두 값의 합 = 1
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
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><span style="color: #545478; font-style: italic;"># 2열짜리 배열 반환: [클래스 0 확률, 클래스 1 확률]</span>
proba = model.predict_proba(X_test)
print(proba)
<span style="color: #545478; font-style: italic;"># [[0.12, 0.88],</span>
<span style="color: #545478; font-style: italic;">#  [0.73, 0.27],</span>
<span style="color: #545478; font-style: italic;">#  [0.41, 0.59]]</span>

<span style="color: #545478; font-style: italic;"># 클래스 1 확률만 꺼내기</span>
proba_class1 = model.predict_proba(X_test)[:, <span style="color: #fab387;">1</span>]
print(proba_class1)  <span style="color: #545478; font-style: italic;"># [0.88, 0.27, 0.59]</span></code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">predict_proba() → 2열 배열 반환. [:, 1]로 클래스 1 확률만 꺼낼 수 있습니다. 두 열의 합은 항상 1.</div>
</div>
