<div style="background-color:#e6f5ff;border:2px solid #c2e4ff;border-radius:14px;padding:18px;font-family:'Nunito',sans-serif,'Malgun Gothic';">
  <h3 style="margin-top:0;margin-bottom:14px;color:#0f172a;font-weight:900;font-size:17px;">배치 학습 — 데이터를 나눠서 처리하기</h3>
  <div style="line-height:1.85;color:#334155;font-size:14px;margin-bottom:16px;">
    캘리포니아 데이터는 <b>20,640개</b>의 샘플이에요.<br>
    이걸 한 번에 다 쓰면 메모리도 부족하고, 학습도 잘 안 돼요.<br>
    그래서 작은 <b>배치(batch)</b>로 나눠서 반복 학습해요.
  </div>
  <div style="font-size:13px;font-weight:800;color:#334155;margin-bottom:10px;">핵심 용어 3가지</div>
  <div style="display:flex;flex-direction:column;gap:7px;margin-bottom:16px;">
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;display:flex;align-items:flex-start;gap:10px;">
      <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:2px 8px;border-radius:20px;flex-shrink:0;margin-top:2px;">Epoch</span>
      <span>전체 데이터(20,640개)를 <b>한 번 다 돌리는</b> 단위 — 보통 30~100 epoch 학습</span>
    </div>
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;display:flex;align-items:flex-start;gap:10px;">
      <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:2px 8px;border-radius:20px;flex-shrink:0;margin-top:2px;">Batch</span>
      <span>한 번에 처리하는 <b>샘플 묶음</b> — 보통 32~128개 (2의 거듭제곱)</span>
    </div>
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;display:flex;align-items:flex-start;gap:10px;">
      <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:2px 8px;border-radius:20px;flex-shrink:0;margin-top:2px;">Step</span>
      <span>배치 1번 처리 = <b>gradient update 1회</b> — 1 epoch = 20640 ÷ 64 = 323 steps</span>
    </div>
  </div>
  <div style="background-color:#fff3eb;border:2px solid #ffd0b0;padding:12px 14px;border-radius:10px;color:#0f172a;font-weight:bold;font-size:13px;display:flex;align-items:flex-start;gap:10px;">
    <div style="color:#FF6B00;font-size:16px;margin-top:-2px;">⚡</div>
    <div style="line-height:1.6;">오른쪽 그림에서 전체 데이터가 배치로 쪼개지는 과정을 확인하세요.<br>DataLoader가 이걸 자동으로 처리해줘요!</div>
  </div>
</div>

<br>

<div style="background-color:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:14px 16px;font-family:'Nunito',sans-serif;">
  <div style="color:#94a3b8;font-size:12px;font-weight:800;margin-bottom:6px;display:flex;align-items:center;gap:5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color:#64748b;font-size:13px;line-height:1.6;">
    캘리포니아 미션에서 <code style="background:#f1f5f9;padding:1px 5px;border-radius:4px;font-size:12px;">batch_size=64</code>로 설정해요.<br>
    1 epoch = 20640 ÷ 64 = <b>323번</b>의 gradient update가 일어나요.
  </div>
</div>