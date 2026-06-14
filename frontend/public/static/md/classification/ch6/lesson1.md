<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">정확도(Accuracy)만으로는 부족하다</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-weight: 700;">정확도 (Accuracy)</span>
    는 전체 샘플 중 올바르게 예측한 비율입니다. 직관적이지만 <b>클래스 불균형 데이터</b>에서는 완전히 잘못된 평가로 이어질 수 있습니다.<br><br>
    암 환자 1명, 정상 99명인 데이터에서 모델이 모든 사람을 "정상"으로 예측하면 정확도는 <b>99%</b>입니다. 그런데 실제로는 암 환자를 단 한 명도 잡아내지 못한 <b>쓸모없는 모델</b>입니다.<br><br>
    이런 상황에서는 정확도 하나만 보면 안 됩니다.
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Precision</span>,
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Recall</span>,
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 4px; font-weight: 700;">F1 Score</span>
    를 함께 봐야 합니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      📐 <b>정확도 공식</b> — Accuracy = 맞게 예측한 수 / 전체 샘플 수
    </div>
    <div style="background: #fee2e2; border-radius: 8px; padding: 10px 14px; color: #991b1b;">
      ⚠️ <b>정확도 함정 예시</b> — 암 환자 1명 + 정상 99명 → 모두 정상 예측 → 정확도 99% but 암 환자 0명 탐지
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; color: #334155;">
      ✅ <b>언제 믿을 수 있는가</b> — 클래스 비율이 균등한 경우에만 정확도가 신뢰할 만한 지표가 됩니다
    </div>
    <div style="background: #f1f5f9; border-radius: 8px; padding: 10px 14px; color: #334155;">
      🔍 <b>실제 현업에서도</b> — 사기 탐지, 희귀 질환 진단, 불량품 검출 등 대부분의 실전 문제가 클래스 불균형입니다
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">클래스 불균형 데이터에서 높은 정확도는 함정일 수 있습니다. Precision, Recall, F1 Score를 함께 확인해야 합니다.</div>
</div>
