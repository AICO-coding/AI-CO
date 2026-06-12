<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Ch2 루프 + Ch3 DataLoader + Ch4 모델 — 처음으로 합치기</h3>

  <div style="line-height: 1.85; color: #334155; font-size: 14px; margin-bottom: 16px;">
    지금까지 배운 세 가지를 <b style="color: #1681c4;">처음으로 하나의 코드</b>로 연결해요.<br>
    iris 데이터 4개 특성 → 1개 수치 예측하는 MLP를 직접 완성해보세요.
  </div>

  <div style="display: flex; flex-direction: column; gap: 6px; margin-bottom: 16px;">
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 8px 14px; font-size: 13px; color: #334155; display: flex; align-items: center; gap: 8px;">
      <span style="color: #FF6B00; font-weight: 900; font-family: monospace;">blank1</span>
      <span style="color: #94a3b8;">→</span>
      <span>iris의 입력 특성 수 (숫자)</span>
    </div>
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 8px 14px; font-size: 13px; color: #334155; display: flex; align-items: center; gap: 8px;">
      <span style="color: #FF6B00; font-weight: 900; font-family: monospace;">blank2</span>
      <span style="color: #94a3b8;">→</span>
      <span>비선형 활성화 함수 이름</span>
    </div>
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 8px 14px; font-size: 13px; color: #334155; display: flex; align-items: center; gap: 8px;">
      <span style="color: #FF6B00; font-weight: 900; font-family: monospace;">blank3</span>
      <span style="color: #94a3b8;">→</span>
      <span>Sequential 블록 이름 (self.???)</span>
    </div>
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 8px 14px; font-size: 13px; color: #334155; display: flex; align-items: center; gap: 8px;">
      <span style="color: #FF6B00; font-weight: 900; font-family: monospace;">blank4</span>
      <span style="color: #94a3b8;">→</span>
      <span>Ch2에서 배운 회귀 손실함수</span>
    </div>
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 8px 14px; font-size: 13px; color: #334155; display: flex; align-items: center; gap: 8px;">
      <span style="color: #FF6B00; font-weight: 900; font-family: monospace;">blank5</span>
      <span style="color: #94a3b8;">→</span>
      <span>Ch2에서 배운 옵티마이저</span>
    </div>
  </div>

  <div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 12px 14px; border-radius: 10px; color: #0f172a; font-weight: bold; font-size: 13px; display: flex; align-items: flex-start; gap: 10px;">
    <div style="color: #FF6B00; font-size: 16px; margin-top: -2px;">⚡</div>
    <div style="line-height: 1.6;">L2·L3 참고 코드를 보면서 채워요. 특히 blank1은 iris 데이터의 컬럼 수를 생각해봐요!</div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <div style="color: #94a3b8; font-size: 12px; font-weight: 800; margin-bottom: 6px; display: flex; align-items: center; gap: 5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.6;">
    미션에서도 동일한 구조예요. iris → California Housing으로 데이터만 바뀌고<br>
    nn.Module 구조, 학습 루프 패턴은 완전히 같아요.
  </div>
</div>