<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Confusion Matrix — 예측 결과를 4가지로 분류</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    Confusion Matrix는 모델의 예측 결과를 <b>TP / FP / FN / TN</b> 네 가지로 정리한 표입니다.<br>
    앞 글자는 맞았는지
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 6px; border-radius: 6px; font-family: monospace;">True / False</span>,
    뒷 글자는 어떻게 예측했는지
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 6px; font-family: monospace;">Positive / Negative</span>
    를 나타냅니다.<br><br>
    FP와 FN 중 어느 쪽이 더 치명적인지는 문제마다 다릅니다. 암 진단에서는 <b>FN(환자를 정상으로 판단)</b>이 더 위험합니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #dcfce7; border-radius: 12px; padding: 12px 15px; color: #166534;">
      ✅ <b>TP (True Positive)</b> — 양성으로 예측 → 실제 양성. 맞음.<br>
      &nbsp;&nbsp;&nbsp;&nbsp;예) 암 환자 → 악성으로 예측 → 올바른 탐지
    </div>
    <div style="background: #dcfce7; border-radius: 12px; padding: 12px 15px; color: #166534;">
      ✅ <b>TN (True Negative)</b> — 음성으로 예측 → 실제 음성. 맞음.<br>
      &nbsp;&nbsp;&nbsp;&nbsp;예) 정상인 → 정상으로 예측 → 올바른 음성 판단
    </div>
    <div style="background: #fef9c3; border-radius: 12px; padding: 12px 15px; color: #713f12;">
      ⚠️ <b>FP (False Positive)</b> — 양성으로 예측 → 실제 음성. 틀림. 거짓 경보.<br>
      &nbsp;&nbsp;&nbsp;&nbsp;예) 정상인 → 악성으로 예측 → 불필요한 검사
    </div>
    <div style="background: #fee2e2; border-radius: 12px; padding: 12px 15px; color: #991b1b;">
      ❌ <b>FN (False Negative)</b> — 음성으로 예측 → 실제 양성. 틀림. <b>놓침!</b><br>
      &nbsp;&nbsp;&nbsp;&nbsp;예) 암 환자 → 정상으로 예측 → 가장 위험한 오류
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">TP/TN = 맞음 / FP = 거짓 경보 / FN = 놓침. 암 진단처럼 놓치면 안 되는 경우엔 FN이 가장 치명적입니다.</div>
</div>
