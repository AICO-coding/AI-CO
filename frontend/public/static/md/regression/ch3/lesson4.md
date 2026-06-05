<div style="background-color:#e6f5ff;border:2px solid #c2e4ff;border-radius:14px;padding:18px;font-family:'Nunito',sans-serif,'Malgun Gothic';">
  <h3 style="margin-top:0;margin-bottom:14px;color:#0f172a;font-weight:900;font-size:17px;">Batch Size — 얼마나 묶어서 학습할까?</h3>
  <div style="line-height:1.85;color:#334155;font-size:14px;margin-bottom:14px;">
    batch_size는 <b>한 번에 처리할 샘플 수</b>예요.<br>
    작으면 업데이트가 잦고 불안정, 크면 안정적이지만 메모리를 많이 써요.
  </div>
  <div style="display:flex;flex-direction:column;gap:7px;margin-bottom:14px;">
    <div style="background:#fff3eb;border:1px solid #ffd0b0;border-radius:8px;padding:9px 13px;display:flex;align-items:center;justify-content:space-between;">
      <div>
        <code style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#e55a00;">batch_size = 4</code>
        <div style="font-size:11px;color:#94a3b8;margin-top:2px;">50 steps/epoch — loss curve 들쭉날쭉</div>
      </div>
      <span style="font-size:18px;">🌊</span>
    </div>
    <div style="background:#e8ffe6;border:2px solid #C2F0BE;border-radius:8px;padding:9px 13px;display:flex;align-items:center;justify-content:space-between;">
      <div>
        <code style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#2DAA24;">batch_size = 32~64</code>
        <div style="font-size:11px;color:#2DAA24;margin-top:2px;font-weight:700;">3~6 steps/epoch — 속도·안정성 균형 ✓</div>
      </div>
      <span style="font-size:18px;">✅</span>
    </div>
    <div style="background:#f8fafc;border:1px solid #D3D1C7;border-radius:8px;padding:9px 13px;display:flex;align-items:center;justify-content:space-between;">
      <div>
        <code style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#5F5E5A;">batch_size = 전체</code>
        <div style="font-size:11px;color:#94a3b8;margin-top:2px;">1 step/epoch — 매우 안정적이지만 느림</div>
      </div>
      <span style="font-size:18px;">〰</span>
    </div>
  </div>
  <div style="background-color:#fff3eb;border:2px solid #ffd0b0;padding:12px 14px;border-radius:10px;color:#0f172a;font-weight:bold;font-size:13px;display:flex;align-items:flex-start;gap:10px;">
    <div style="color:#FF6B00;font-size:16px;margin-top:-2px;">⚡</div>
    <div style="line-height:1.6;">오른쪽 슬라이더로 batch_size를 바꿔보세요.<br>loss curve의 흔들림 범위(보라색 띠)가 어떻게 달라지는지 확인!<br>
    <span style="font-weight:400;color:#64748b;">프리셋 버튼: 4(불안정) / 64(권장) / 200(전체배치)</span></div>
  </div>
</div>

<br>

<div style="background-color:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:14px 16px;font-family:'Nunito',sans-serif;">
  <div style="color:#94a3b8;font-size:12px;font-weight:800;margin-bottom:6px;display:flex;align-items:center;gap:5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color:#64748b;font-size:13px;line-height:1.6;">
    미션에서 <code style="background:#f1f5f9;padding:1px 5px;border-radius:4px;font-size:12px;">batch_size=64</code>를 사용해요.<br>
    20640 ÷ 64 = <b>323 steps/epoch</b>으로 안정적으로 학습해요.
  </div>
</div>