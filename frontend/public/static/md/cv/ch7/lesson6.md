<div style="background:#f8fafc;border:2px solid #bae6fd;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;gap:12px;align-items:center;margin-bottom:20px;">
<div style="font-size:30px;">💻</div>
<div>
<div style="font-size:22px;font-weight:900;color:#0369a1;">
실습 : CIFAR-10 학습 루프
</div>
<div style="font-size:14px;color:#64748b;">
PyTorch Training Loop
</div>
</div>
</div>

<div style="background:white;border-radius:14px;padding:20px;color:#334155;line-height:2;">

<p>
optimizer.zero_grad()는 이전 Gradient를 초기화합니다.
</p>

<p>
model(images)는 Forward 연산을 수행합니다.
</p>

<p>
criterion은 Loss를 계산합니다.
</p>

<p>
loss.backward()는 Gradient를 계산합니다.
</p>

<p>
optimizer.step()은 가중치를 업데이트합니다.
</p>

</div>

<div style="margin-top:18px;background:#0f172a;color:#e2e8f0;border-radius:14px;padding:20px;font-family:monospace;white-space:pre;line-height:1.7;">
for images, labels in train_loader:

    optimizer.zero_grad()

    outputs = model(images)

    loss = criterion(outputs, labels)

    loss.backward()

    optimizer.step()
</div>

<div style="margin-top:18px;background:#e0f2fe;border:2px solid #38bdf8;border-radius:14px;padding:14px;">
💡 핵심<br>
Forward → Loss → Backward → Step 순서가 학습의 핵심이다.
</div>

</div>