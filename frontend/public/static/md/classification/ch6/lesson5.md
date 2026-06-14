<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">sklearn으로 평가지표 한번에 계산하기</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    sklearn의
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-weight: 700;">classification_report()</span>
    를 쓰면 Precision, Recall, F1 Score를 한 번에 볼 수 있습니다.<br><br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-weight: 700;">confusion_matrix()</span>
    는 TP/FP/FN/TN 값을 행렬로 출력합니다.<br><br>
    두 함수 모두 <b>y_test(실제값)</b>와 <b>preds(예측값)</b>를 인자로 받습니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      📋 <b>classification_report 출력 예시</b><br>
      <pre style="margin: 6px 0 0; font-family: monospace; font-size: 11px; color: #334155; background: #f8fafc; padding: 8px; border-radius: 6px;">
              precision  recall  f1-score  support
           0       0.95    0.98      0.96       50
           1       0.88    0.73      0.80       15
accuracy                            0.93       65</pre>
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
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><span style="color: #cba6f7;">from</span> sklearn.metrics <span style="color: #cba6f7;">import</span> classification_report, confusion_matrix

<span style="color: #545478; font-style: italic;"># Precision, Recall, F1 한번에</span>
print(classification_report(y_test, preds))

<span style="color: #545478; font-style: italic;"># Confusion Matrix</span>
cm = confusion_matrix(y_test, preds)
print(cm)
<span style="color: #545478; font-style: italic;"># [[TN, FP],</span>
<span style="color: #545478; font-style: italic;">#  [FN, TP]]</span>

<span style="color: #545478; font-style: italic;"># 개별 지표</span>
<span style="color: #cba6f7;">from</span> sklearn.metrics <span style="color: #cba6f7;">import</span> precision_score, recall_score, f1_score
print(precision_score(y_test, preds))
print(recall_score(y_test, preds))
print(f1_score(y_test, preds))</code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">classification_report()로 Precision/Recall/F1을 한 번에 확인. confusion_matrix()로 TP/FP/FN/TN 확인.</div>
</div>
