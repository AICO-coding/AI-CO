<div style="background:#f8fafc;border:2px solid #fecaca;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;gap:12px;align-items:center;margin-bottom:20px;">
<div style="font-size:30px;">💻</div>
<div>
<div style="font-size:22px;font-weight:900;color:#991b1b;">
실습 : Overfitting 관찰하기
</div>
<div style="font-size:14px;color:#64748b;">
Epoch를 많이 학습시켜보기
</div>
</div>
</div>

<div style="background:white;padding:20px;border-radius:14px;color:#334155;line-height:2;">

<p>
Adam Optimizer를 사용하여 모델을 학습합니다.
</p>

<p>
Epoch를 크게 설정하면
Train Accuracy는 계속 증가할 수 있습니다.
</p>

<p>
하지만 Validation Accuracy는 오히려 감소할 수 있으며
이 현상이 바로 Overfitting입니다.
</p>

</div>

<div style="margin-top:18px;background:#0f172a;color:#e2e8f0;border-radius:14px;padding:20px;font-family:monospace;white-space:pre;line-height:1.7;">
model = VGG()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

for epoch in range(100):
    train()
</div>

<div style="margin-top:18px;background:#fee2e2;border:2px solid #ef4444;border-radius:14px;padding:14px;">
💡 핵심<br>
너무 오래 학습하면 일반화 성능이 오히려 나빠질 수 있다.
</div>

</div>