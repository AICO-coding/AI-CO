<div style="background-color:#e6f5ff;border:2px solid #c2e4ff;border-radius:14px;padding:18px;font-family:'Nunito',sans-serif,'Malgun Gothic';">
  <h3 style="margin-top:0;margin-bottom:14px;color:#0f172a;font-weight:900;font-size:17px;">🧩 학습 루프 완성하기</h3>
  <div style="line-height:1.85;color:#334155;font-size:14px;margin-bottom:16px;">
    <code style="background:#fff;border:1px solid #ffd0b0;color:#FF6B00;padding:1px 6px;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:12px;">y = 3x + 2</code> 관계를 모델이 스스로 학습하는지 확인해요.<br>
    L2·L3에서 배운 내용을 여기서 직접 완성해보세요!
  </div>
  <div style="font-size:13px;font-weight:800;color:#334155;margin-bottom:10px;">TODO 가이드</div>
  <div style="display:flex;flex-direction:column;gap:7px;margin-bottom:16px;">
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;line-height:1.5;display:flex;gap:8px;align-items:flex-start;">
      <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:1px 7px;border-radius:20px;flex-shrink:0;margin-top:2px;">1</span>
      <div><b>blank1</b> — 회귀 손실함수 클래스명 (Mean Squared Error Loss)</div>
    </div>
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;line-height:1.5;display:flex;gap:8px;align-items:flex-start;">
      <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:1px 7px;border-radius:20px;flex-shrink:0;margin-top:2px;">2</span>
      <div><b>blank2</b> — 적응형 학습률 옵티마이저명 (Adaptive Moment Estimation)</div>
    </div>
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;line-height:1.5;display:flex;gap:8px;align-items:flex-start;">
      <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:1px 7px;border-radius:20px;flex-shrink:0;margin-top:2px;">3</span>
      <div><b>blank3</b> — gradient 누적 방지 메서드 <span style="color:#e55a00;">(반드시 backward 전에!)</span></div>
    </div>
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;line-height:1.5;display:flex;gap:8px;align-items:flex-start;">
      <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:1px 7px;border-radius:20px;flex-shrink:0;margin-top:2px;">4</span>
      <div><b>blank4</b> — 역전파 실행 메서드 (gradient 계산)</div>
    </div>
  </div>
  <div style="background-color:#fff3eb;border:2px solid #ffd0b0;padding:12px 14px;border-radius:10px;color:#0f172a;font-weight:bold;font-size:13px;display:flex;align-items:flex-start;gap:10px;">
    <div style="color:#FF6B00;font-size:16px;margin-top:-2px;">⚡</div>
    <div style="line-height:1.6;">학습이 성공하면 기울기 ≈ 3.00, 절편 ≈ 2.00으로 수렴해요!</div>
  </div>
</div>

<br>

<div style="background-color:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:14px 16px;font-family:'Nunito',sans-serif;">
  <div style="color:#94a3b8;font-size:12px;font-weight:800;margin-bottom:6px;display:flex;align-items:center;gap:5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color:#64748b;font-size:13px;line-height:1.6;">
    미션 TODO 7·8에서 같은 패턴을 사용해요.<br>
    데이터만 캘리포니아 집값으로 바뀔 뿐이에요!
  </div>
</div>