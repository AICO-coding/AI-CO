<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 14px; padding: 20px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <h3 style="margin-top: 0; margin-bottom: 14px; color: #0f172a; font-weight: 900; font-size: 17px;">왜 nn.Module을 상속하는가?</h3>

  <div style="line-height: 1.85; color: #334155; font-size: 14px; margin-bottom: 18px;">
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 1px 6px; border-radius: 4px; font-family: 'JetBrains Mono', monospace; font-size: 12.5px;">nn.Linear</span> 하나만 쓰면 되지 않을까요?<br>
    모델이 복잡해질수록 레이어가 수십 개 — 파라미터를 일일이 관리하는 건 불가능해요.
  </div>

  <div style="font-size: 13px; font-weight: 800; color: #334155; margin-bottom: 10px;">nn.Module 상속이 주는 것</div>

  <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 18px;">
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #0f172a; display: flex; align-items: flex-start; gap: 10px;">
      <span style="color: #FF6B00; font-weight: 900; min-width: 20px;">①</span>
      <div>
        <span style="font-weight: 800;">파라미터 자동 등록</span><br>
        <span style="color: #64748b;">self.net = nn.Linear(...) 한 줄이면 W, b 자동 추적</span>
      </div>
    </div>
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #0f172a; display: flex; align-items: flex-start; gap: 10px;">
      <span style="color: #FF6B00; font-weight: 900; min-width: 20px;">②</span>
      <div>
        <span style="font-weight: 800;">model.parameters() 한 번에</span><br>
        <span style="color: #64748b;">optimizer에 넘길 때 모든 파라미터를 자동으로 수집</span>
      </div>
    </div>
    <div style="background: #fff; border: 1px solid #c2e4ff; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #0f172a; display: flex; align-items: flex-start; gap: 10px;">
      <span style="color: #FF6B00; font-weight: 900; min-width: 20px;">③</span>
      <div>
        <span style="font-weight: 800;">train/eval 모드 전환 + 저장/불러오기</span><br>
        <span style="color: #64748b;">model.train(), model.eval(), torch.save() 전부 공짜</span>
      </div>
    </div>
  </div>

  <pre style="background-color: #0f172a; color: #c3e88d; padding: 14px; border-radius: 10px; font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.9; overflow-x: auto; margin: 0;"><code># Module 없이 — 파라미터를 직접 관리해야 함
W1 = torch.randn(8, 128, requires_grad=True)
b1 = torch.zeros(128, requires_grad=True)
W2 = torch.randn(128, 64, requires_grad=True)
# ... optimizer에 [W1, b1, W2, ...] 수동으로 넘겨야 함 😓

# Module 상속 — 자동 관리!
class MLP(nn.Module): ...
opt = torch.optim.Adam(model.parameters())  # 끝! 🎉</code></pre>

  <div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 12px 14px; border-radius: 10px; margin-top: 16px; color: #0f172a; font-weight: bold; font-size: 13px; display: flex; align-items: flex-start; gap: 10px;">
    <div style="color: #FF6B00; font-size: 16px; margin-top: -2px;">⚡</div>
    <div style="line-height: 1.6;">이 챕터의 목표: 8→128→64→1 MLP를<br>nn.Module로 직접 설계하기</div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <div style="color: #94a3b8; font-size: 12px; font-weight: 800; margin-bottom: 6px; display: flex; align-items: center; gap: 5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.6;">
    캘리포니아 미션의 모델도 nn.Module을 상속해서 만들어요.<br>
    파라미터 자동 관리 덕분에 optimizer 한 줄로 연결할 수 있어요.
  </div>
</div>