<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">PyTorch로 다중 분류기 만들기</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    다중 분류기는 이진 분류기와 구조가 거의 같습니다. 바뀌는 것은 <b>출력층 뉴런 수</b>와 <b>Loss 함수</b>뿐입니다.<br><br>
    출력층을 <b>nn.Linear(hidden, num_classes)</b>로 설정합니다. 클래스가 3개면 3, 10개면 10을 넣습니다.<br><br>
    예측 시에는 logit에서 argmax로 가장 높은 점수의 클래스를 찾습니다. 나머지 학습 루프는 <b>이진 분류와 완전히 동일합니다.</b>
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      📐 <b>출력층 설정</b> — nn.Linear(16, 3): 클래스 3개 / nn.Linear(16, 10): 클래스 10개
    </div>
    <div style="background: #dcfce7; border-radius: 8px; padding: 10px 14px; color: #166534;">
      ✅ <b>이진 분류와 동일한 것</b> — zero_grad → 예측 → Loss → backward → step 학습 루프
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; color: #334155;">
      🔄 <b>이진 분류와 다른 것</b> — Linear(n, N클래스) / CrossEntropyLoss / 예측: argmax
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

<span style="color: #cba6f7;">class</span> <span style="color: #a6e3a1;">MultiClassifier</span>(nn.Module):
    <span style="color: #cba6f7;">def</span> <span style="color: #89b4fa;">__init__</span>(self, num_classes=<span style="color: #fab387;">3</span>):
        <span style="color: #cba6f7;">super</span>().__init__()
        self.net = nn.Sequential(
            nn.Linear(<span style="color: #fab387;">8</span>, <span style="color: #fab387;">16</span>),
            nn.ReLU(),
            nn.Linear(<span style="color: #fab387;">16</span>, num_classes)  <span style="color: #545478; font-style: italic;"># Softmax 없음!</span>
        )

    <span style="color: #cba6f7;">def</span> <span style="color: #89b4fa;">forward</span>(self, x):
        <span style="color: #cba6f7;">return</span> self.net(x)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=<span style="color: #fab387;">0.001</span>)

<span style="color: #545478; font-style: italic;"># 학습 루프 (이진 분류와 동일)</span>
<span style="color: #cba6f7;">for</span> epoch <span style="color: #cba6f7;">in</span> <span style="color: #cba6f7;">range</span>(<span style="color: #fab387;">100</span>):
    optimizer.zero_grad()
    pred = model(X_train)
    loss = criterion(pred, y_train)  <span style="color: #545478; font-style: italic;"># y는 정수 클래스 번호</span>
    loss.backward()
    optimizer.step()

<span style="color: #545478; font-style: italic;"># 예측: argmax로 가장 높은 클래스</span>
preds = model(X_test).argmax(dim=<span style="color: #fab387;">1</span>)</code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">다중 분류기: Linear(n, N클래스) + CrossEntropyLoss. Softmax 생략. 예측은 argmax. 학습 루프는 이진 분류와 동일.</div>
</div>
