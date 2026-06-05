<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Ch2~Ch4 루프에 train/eval + R² 추가 — 거의 완성형</h3>

  <div style="line-height: 1.85; color: #334155; font-size: 14px; margin-bottom: 16px;">
    지금까지 배운 모든 것을 합쳐요.<br>
    <b style="color: #1681c4;">학습 루프 + 검증 루프 + R² 계산</b>까지 완성하면 미션 준비 끝!
  </div>

  <div style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 16px;">
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 8px 14px; font-size: 13px; color: #334155; display: flex; align-items: center; gap: 8px;">
      <span style="color: #FF6B00; font-weight: 900; font-family: monospace;">blank1</span>
      <span style="color: #94a3b8;">→</span>
      <span>학습 모드 전환 메서드</span>
    </div>
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 8px 14px; font-size: 13px; color: #334155; display: flex; align-items: center; gap: 8px;">
      <span style="color: #FF6B00; font-weight: 900; font-family: monospace;">blank2</span>
      <span style="color: #94a3b8;">→</span>
      <span>평가 모드 전환 메서드</span>
    </div>
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 8px 14px; font-size: 13px; color: #334155; display: flex; align-items: center; gap: 8px;">
      <span style="color: #FF6B00; font-weight: 900; font-family: monospace;">blank3</span>
      <span style="color: #94a3b8;">→</span>
      <span>gradient 계산 끄는 컨텍스트 매니저</span>
    </div>
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 8px 14px; font-size: 13px; color: #334155; display: flex; align-items: center; gap: 8px;">
      <span style="color: #FF6B00; font-weight: 900; font-family: monospace;">blank4</span>
      <span style="color: #94a3b8;">→</span>
      <span>예측 오차 제곱합 변수명</span>
    </div>
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 8px 14px; font-size: 13px; color: #334155; display: flex; align-items: center; gap: 8px;">
      <span style="color: #FF6B00; font-weight: 900; font-family: monospace;">blank5</span>
      <span style="color: #94a3b8;">→</span>
      <span>전체 분산 제곱합 변수명</span>
    </div>
  </div>

  <div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 12px 14px; border-radius: 10px; color: #0f172a; font-weight: bold; font-size: 13px; display: flex; align-items: flex-start; gap: 10px;">
    <div style="color: #FF6B00; font-size: 16px; margin-top: -2px;">⚡</div>
    <div style="line-height: 1.6;">L2·L3 참고 코드를 보면서 채워요. train/eval 순서와 no_grad 위치를 꼭 확인하세요!</div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <div style="color: #94a3b8; font-size: 12px; font-weight: 800; margin-bottom: 6px; display: flex; align-items: center; gap: 5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.6;">
    이 코드 구조가 미션의 뼈대예요.<br>
    California Housing 데이터로 R² 0.7 이상을 목표로 해봐요!
  </div>
</div>