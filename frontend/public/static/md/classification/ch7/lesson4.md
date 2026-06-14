<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Dropout과 L2 규제 — overfitting 해결</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    High Variance(overfitting) 상황에서 가장 많이 쓰는 두 가지 해결책이 있습니다.<br><br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Dropout</span>
    은 학습 중 일부 뉴런을 랜덤하게 꺼버리는 기법입니다. 매 스텝마다 다른 뉴런이 꺼지므로 모델이 특정 패턴에 과도하게 의존하지 못합니다. 결과적으로 더 일반적인 패턴을 학습하게 됩니다. <b>p=0.5</b>면 50%의 뉴런이 랜덤하게 꺼집니다.<br><br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 4px; font-weight: 700;">L2 규제 (Weight Decay)</span>
    는 가중치가 너무 커지지 못하도록 페널티를 줍니다. 가중치가 크면 Loss가 커지도록 설계해서, 모델이 특정 특성에 과도하게 의존하는 것을 막습니다. Adam optimizer의 <b>weight_decay</b> 파라미터로 설정합니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      🎲 <b>Dropout 원리</b> — 학습 시 뉴런 일부를 끔 → 특정 패턴 과의존 방지 → 일반화 능력 향상
    </div>
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      ⚖️ <b>L2 규제 원리</b> — 큰 가중치에 페널티 → 가중치를 작게 유지 → 특성 과의존 방지
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; color: #334155;">
      ⚠️ <b>주의</b> — Dropout은 학습 중에만 작동합니다. 평가 시에는 자동으로 꺼집니다. model.eval() 호출 시 비활성화됩니다
    </div>
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
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; font-family: 'Nunito', sans-serif;">참고 코드 ← 보고 채워요</div>
  </div>
  <div style="padding: 15px; color: #cdd6f4; font-size: 13px; line-height: 1.6; overflow-x: auto;">
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><span style="color: #cba6f7;">import</span> torch.nn <span style="color: #cba6f7;">as</span> nn

<span style="color: #cba6f7;">class</span> <span style="color: #a6e3a1;">BinaryClassifier</span>(nn.Module):
    <span style="color: #cba6f7;">def</span> <span style="color: #89b4fa;">__init__</span>(self):
        <span style="color: #cba6f7;">super</span>().__init__()
        self.net = nn.Sequential(
            nn.Linear(<span style="color: #fab387;">8</span>, <span style="color: #fab387;">16</span>),
            nn.ReLU(),
            nn.Dropout(p=<span style="color: #fab387;">0.5</span>),   <span style="color: #545478; font-style: italic;"># 50% 뉴런 랜덤으로 끔</span>
            nn.Linear(<span style="color: #fab387;">16</span>, <span style="color: #fab387;">1</span>),
            nn.Sigmoid()
        )

<span style="color: #545478; font-style: italic;"># L2 규제: weight_decay로 설정</span>
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=<span style="color: #fab387;">0.001</span>,
    weight_decay=<span style="color: #fab387;">1e-4</span>   <span style="color: #545478; font-style: italic;"># L2 규제 강도</span>
)</code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">Dropout = 뉴런 랜덤 끄기 → 일반화 향상 / L2 규제 = 가중치 크기 제한 → 과의존 방지. 둘 다 overfitting 해결책.</div>
</div>
