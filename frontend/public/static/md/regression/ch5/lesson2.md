<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Dropout + model.train() / model.eval()</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">nn.Dropout(p)</span> — p 비율만큼 뉴런을 랜덤하게 끔<br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">model.train()</span> — 학습 루프 시작 전에 호출<br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">model.eval()</span> — 검증/테스트 전에 호출
  </div>

  <div style="background-color: #0f172a; color: #c3e88d; padding: 15px; border-radius: 10px; font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.8; margin-top: 15px;">
    model.train()  → Dropout 켜짐 (학습 시)<br>
    model.eval()   → Dropout 꺼짐 (검증 시)<br>
    <br>
    for epoch in range(50):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;model.train()   ← 에포크 시작마다 호출<br>
    &nbsp;&nbsp;&nbsp;&nbsp;...<br>
    model.eval()        ← 검증 직전에 호출
  </div>

  <div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 12px 15px; border-radius: 10px; margin-top: 15px; color: #0f172a; font-weight: bold; font-size: 13px; display: flex; align-items: center; gap: 10px;">
    <span style="color: #FF6B00; font-size: 16px;">⚡</span> Dropout(p=0.2)는 20%를 끈다는 뜻이에요. 살리는 비율이 아니에요!
  </div>
</div>

<br>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 12px; overflow: hidden; font-family: 'JetBrains Mono', monospace; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 10px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #6060a0; margin-left: 8px; font-size: 12px;">📄 reference.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; font-family: 'Nunito', sans-serif;">
      참고 코드 ← 보고 채워요
    </div>
  </div>

  <div style="padding: 15px; color: #cdd6f4; font-size: 13px; line-height: 1.6; overflow-x: auto;">
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><span style="color: #cba6f7;">import</span> torch.nn <span style="color: #cba6f7;">as</span> nn

<span style="color: #cba6f7;">class</span> <span style="color: #a6e3a1;">IrisNet</span>(nn.Module):
    <span style="color: #cba6f7;">def</span> <span style="color: #89b4fa;">__init__</span>(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(<span style="color: #fab387;">4</span>, <span style="color: #fab387;">16</span>),
            nn.ReLU(),
<div style="background: rgba(255,107,0,.09); border-left: 2px solid #FF6B00; padding: 0 13px; margin: 0 -15px;">            nn.Dropout(<span style="color: #fab387;">0.2</span>),    <span style="color: #545478; font-style: italic;"># 20% 뉴런 랜덤하게 끄기</span></div>
            nn.Linear(<span style="color: #fab387;">16</span>, <span style="color: #fab387;">1</span>)
        )
    <span style="color: #cba6f7;">def</span> <span style="color: #89b4fa;">forward</span>(self, x):
        <span style="color: #cba6f7;">return</span> self.net(x)

<span style="color: #545478; font-style: italic;"># 학습 루프</span>
<span style="color: #cba6f7;">for</span> epoch <span style="color: #cba6f7;">in</span> range(<span style="color: #fab387;">50</span>):
<div style="background: rgba(255,107,0,.09); border-left: 2px solid #FF6B00; padding: 0 13px; margin: 0 -15px;">    model.train()               <span style="color: #545478; font-style: italic;"># Dropout 켜짐</span></div>
    <span style="color: #cba6f7;">for</span> Xb, yb <span style="color: #cba6f7;">in</span> train_ld:
        pred = model(Xb)
        loss = crit(pred, yb)
        opt.zero_grad() ; loss.backward() ; opt.step()

<div style="background: rgba(255,107,0,.09); border-left: 2px solid #FF6B00; padding: 0 13px; margin: 0 -15px;">model.eval()                    <span style="color: #545478; font-style: italic;"># Dropout 꺼짐</span></div></code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: 'Nunito', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">🏆 Mission 연결</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">미션 학습 루프에서 epoch마다 model.train(), 검증 전 model.eval() 패턴을 그대로 써요.</div>
</div>