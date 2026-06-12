<div style="background-color:#e6f5ff;border:2px solid #c2e4ff;border-radius:14px;padding:18px;font-family:'Nunito',sans-serif,'Malgun Gothic';">
  <h3 style="margin-top:0;margin-bottom:14px;color:#0f172a;font-weight:900;font-size:17px;">Learning Rate — 얼마나 빠르게 배울까?</h3>
  <div style="line-height:1.85;color:#334155;font-size:14px;margin-bottom:16px;">
    Learning Rate(lr)는 gradient 방향으로 <b>얼마나 크게 이동할지</b> 결정해요.<br>
    너무 작으면 학습이 느리고, 너무 크면 loss가 발산해요.
  </div>
  <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:16px;">
    <div style="background:#fff;border:1px solid #D3D1C7;border-radius:8px;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;">
      <code style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#5F5E5A;background:#F1EFE8;border:1px solid #D3D1C7;padding:2px 8px;border-radius:4px;">lr = 0.0001</code>
      <span style="font-size:12px;color:#64748b;">너무 느림 → 수렴에 수천 에폭</span>
    </div>
    <div style="background:#e8ffe6;border:2px solid #C2F0BE;border-radius:8px;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;">
      <code style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#2DAA24;background:#e8ffe6;border:1px solid #C2F0BE;padding:2px 8px;border-radius:4px;">lr = 0.01</code>
      <span style="font-size:12px;color:#2DAA24;font-weight:800;">적당 ✓ — 안정적으로 수렴</span>
    </div>
    <div style="background:#fff3eb;border:1px solid #ffd0b0;border-radius:8px;padding:10px 14px;display:flex;align-items:center;justify-content:space-between;">
      <code style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#FF6B00;background:#fff3eb;border:1px solid #ffd0b0;padding:2px 8px;border-radius:4px;">lr = 1.0</code>
      <span style="font-size:12px;color:#e55a00;font-weight:800;">너무 큼 → loss 폭발, 학습 실패</span>
    </div>
  </div>
  <div style="background-color:#fff3eb;border:2px solid #ffd0b0;padding:12px 14px;border-radius:10px;color:#0f172a;font-weight:bold;font-size:13px;display:flex;align-items:flex-start;gap:10px;">
    <div style="color:#FF6B00;font-size:16px;margin-top:-2px;">⚡</div>
    <div style="line-height:1.6;">오른쪽 슬라이더로 lr을 직접 바꿔보고<br>loss curve가 수렴하는지 발산하는지 확인해보세요!</div>
  </div>
</div>

<br>

<div style="background-color:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:14px 16px;font-family:'Nunito',sans-serif;">
  <div style="color:#94a3b8;font-size:12px;font-weight:800;margin-bottom:6px;display:flex;align-items:center;gap:5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color:#64748b;font-size:13px;line-height:1.6;">
    미션에서 <code style="background:#f1f5f9;padding:1px 5px;border-radius:4px;font-size:12px;">lr=1e-3</code> (=0.001)으로 설정해요.<br>
    너무 크게 설정하면 R²가 낮아지거나 아예 발산해요.
  </div>
</div>