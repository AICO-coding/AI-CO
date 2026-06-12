<div style="background-color:#e6f5ff;border:2px solid #c2e4ff;border-radius:14px;padding:18px;font-family:'Nunito',sans-serif,'Malgun Gothic';">
  <h3 style="margin-top:0;margin-bottom:14px;color:#0f172a;font-weight:900;font-size:17px;">선형회귀 = 직선 하나로 예측하기</h3>
  <div style="line-height:1.85;color:#334155;font-size:14px;margin-bottom:16px;">
    모델이 예측을 한 뒤, 얼마나 틀렸는지 계산하고,<br>
    그 오차를 줄이는 방향으로 스스로 고쳐나가는 과정이에요.
  </div>
  <div style="font-size:13px;font-weight:800;color:#334155;margin-bottom:10px;">학습 루프 4단계</div>
  <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:16px;">
    <div style="display:flex;align-items:center;gap:10px;">
      <div style="width:28px;height:28px;border-radius:50%;background:#FF6B00;color:#fff;font-size:12px;font-weight:900;display:flex;align-items:center;justify-content:center;flex-shrink:0;">1</div>
      <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:8px 12px;flex:1;font-size:13px;color:#334155;"><b>Forward</b> — 입력 데이터 → 예측값(ŷ) 계산</div>
    </div>
    <div style="display:flex;align-items:center;gap:10px;">
      <div style="width:28px;height:28px;border-radius:50%;background:#FF6B00;color:#fff;font-size:12px;font-weight:900;display:flex;align-items:center;justify-content:center;flex-shrink:0;">2</div>
      <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:8px 12px;flex:1;font-size:13px;color:#334155;"><b>Loss</b> — 예측값(ŷ)과 실제값(y)의 오차 계산</div>
    </div>
    <div style="display:flex;align-items:center;gap:10px;">
      <div style="width:28px;height:28px;border-radius:50%;background:#FF6B00;color:#fff;font-size:12px;font-weight:900;display:flex;align-items:center;justify-content:center;flex-shrink:0;">3</div>
      <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:8px 12px;flex:1;font-size:13px;color:#334155;"><b>Backward</b> — 오차를 줄이는 방향 계산 (gradient)</div>
    </div>
    <div style="display:flex;align-items:center;gap:10px;">
      <div style="width:28px;height:28px;border-radius:50%;background:#FF6B00;color:#fff;font-size:12px;font-weight:900;display:flex;align-items:center;justify-content:center;flex-shrink:0;">4</div>
      <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:8px 12px;flex:1;font-size:13px;color:#334155;"><b>Update</b> — gradient 방향으로 파라미터(w, b) 조정</div>
    </div>
  </div>
  <div style="background-color:#fff3eb;border:2px solid #ffd0b0;padding:12px 14px;border-radius:10px;color:#0f172a;font-weight:bold;font-size:13px;display:flex;align-items:flex-start;gap:10px;">
    <div style="color:#FF6B00;font-size:16px;margin-top:-2px;">⚡</div>
    <div style="line-height:1.6;">이 4단계가 수백~수천 번 반복되면서 모델이 점점 정확해져요.<br>오른쪽 그림에서 전체 흐름을 확인하세요!</div>
  </div>
</div>

<br>

<div style="background-color:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:14px 16px;font-family:'Nunito',sans-serif;">
  <div style="color:#94a3b8;font-size:12px;font-weight:800;margin-bottom:6px;display:flex;align-items:center;gap:5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color:#64748b;font-size:13px;line-height:1.6;">
    캘리포니아 미션 TODO 7·8에서<br>이 4단계를 직접 코드로 구현해요.
  </div>
</div>