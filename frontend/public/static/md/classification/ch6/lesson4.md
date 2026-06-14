<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">F1 Score — Precision과 Recall을 하나로</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    Precision과 Recall은 트레이드오프 관계입니다. 둘을 균형 있게 반영하는 지표가
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-weight: 700;">F1 Score</span>
    입니다.<br><br>
    공식:
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-weight: 700;">F1 = 2 × (Precision × Recall) / (Precision + Recall)</span><br><br>
    단순 평균이 아닌 <b>조화평균</b>을 씁니다. 조화평균은 두 값 중 하나가 매우 낮으면 결과도 낮게 나옵니다. Precision=1.0, Recall=0.1이면 단순 평균은 0.55지만 F1은 <b>0.182</b>입니다. 한쪽만 좋아서는 F1이 높게 나오지 않습니다.<br><br>
    클래스 불균형 데이터에서 정확도 대신 <b>F1 Score를 주요 지표</b>로 씁니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      📐 <b>F1 계산 예시</b> — Precision=0.8, Recall=0.6 → F1 = 2×(0.8×0.6)/(0.8+0.6) ≈ <b>0.686</b>
    </div>
    <div style="background: #fee2e2; border-radius: 8px; padding: 10px 14px; color: #991b1b;">
      ⚠️ <b>한쪽만 높으면</b> — Precision=1.0, Recall=0.1 → F1 ≈ 0.182. 한쪽만 좋아서는 안 됨
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
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; font-family: 'Nunito', sans-serif;">참고 코드 ← 보고 채워요</div>
  </div>
  <div style="padding: 15px; color: #cdd6f4; font-size: 13px; line-height: 1.6; overflow-x: auto;">
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><span style="color: #cba6f7;">from</span> sklearn.metrics <span style="color: #cba6f7;">import</span> f1_score

precision = <span style="color: #fab387;">0.8</span>
recall = <span style="color: #fab387;">0.6</span>

<span style="color: #545478; font-style: italic;"># 직접 계산</span>
f1 = <span style="color: #fab387;">2</span> * (precision * recall) / (precision + recall)
print(f1)  <span style="color: #545478; font-style: italic;"># 0.6857</span>

<span style="color: #545478; font-style: italic;"># sklearn으로 계산</span>
f1 = f1_score(y_test, preds)
print(f1)</code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">F1 = 조화평균(Precision, Recall). 한쪽만 높으면 F1도 낮습니다. 클래스 불균형 데이터의 핵심 평가 지표입니다.</div>
</div>
