<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">코드로 Bias-Variance 진단하기</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    실제로 Bias-Variance를 진단하려면 <b>훈련 정확도와 테스트 정확도를 비교</b>하면 됩니다.<br><br>
    sklearn에서는 <b>model.score()</b>, PyTorch에서는 학습 루프 안에서 직접 계산합니다.<br><br>
    두 정확도의 <b>차이(gap)</b>가 크면 overfitting, 둘 다 낮으면 underfitting입니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #fee2e2; border-radius: 8px; padding: 10px 14px; color: #991b1b;">
      📉 train_acc=0.62, test_acc=0.60 → 차이 작음, 둘 다 낮음 → <b>underfitting</b>
    </div>
    <div style="background: #fef9c3; border-radius: 8px; padding: 10px 14px; color: #713f12;">
      ⚠️ train_acc=0.97, test_acc=0.61 → 차이 큼 → <b>overfitting</b>
    </div>
    <div style="background: #dcfce7; border-radius: 8px; padding: 10px 14px; color: #166534;">
      ✅ train_acc=0.92, test_acc=0.89 → 차이 작음, 둘 다 높음 → <b>이상적</b>
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
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><span style="color: #545478; font-style: italic;"># sklearn 버전</span>
train_acc = model.score(X_train, y_train)
test_acc  = model.score(X_test,  y_test)

print(<span style="color: #fab387;">f"train: {train_acc:.3f}"</span>)
print(<span style="color: #fab387;">f"test:  {test_acc:.3f}"</span>)
gap = train_acc - test_acc
print(<span style="color: #fab387;">f"gap:   {gap:.3f}"</span>)

<span style="color: #cba6f7;">if</span> train_acc < <span style="color: #fab387;">0.7</span>:
    print(<span style="color: #fab387;">"→ underfitting (High Bias)"</span>)
<span style="color: #cba6f7;">elif</span> gap > <span style="color: #fab387;">0.1</span>:
    print(<span style="color: #fab387;">"→ overfitting (High Variance)"</span>)
<span style="color: #cba6f7;">else</span>:
    print(<span style="color: #fab387;">"→ 이상적인 모델"</span>)</code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">train_acc와 test_acc를 비교해서 진단. 차이(gap)가 크면 overfitting, 둘 다 낮으면 underfitting.</div>
</div>
