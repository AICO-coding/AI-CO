<div style="background:#ecfdf5;border:2px solid #86efac;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">⚙️</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
Optimizer — 모델을 학습시키는 엔진
</div>
<div style="font-size:14px;color:#64748b;">
Loss를 줄이는 방향으로 가중치를 업데이트합니다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #bbf7d0;border-radius:14px;padding:18px;font-size:14px;line-height:2;color:#334155;">

Forward를 수행하면 예측값이 생성됩니다.

이후 Loss를 계산하여
현재 모델이 얼마나 틀렸는지 알 수 있습니다.

하지만 Loss를 계산했다고 해서
모델이 자동으로 똑똑해지는 것은 아닙니다.

Loss를 줄이도록
모델의 Weight(가중치)를 수정해야 합니다.

이 역할을 수행하는 것이 Optimizer입니다.

Optimizer는 Backward에서 계산된 Gradient를 이용하여
Weight를 조금씩 업데이트합니다.

대표적으로

• SGD<br>
• Momentum<br>
• Adam

등이 사용됩니다.

현재 딥러닝에서는 Adam을 가장 많이 사용합니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;white-space:pre;">
Forward
   ↓
Loss
   ↓
Backward
   ↓
Optimizer
   ↓
Weight Update
</div>

<div style="margin-top:18px;background:#dcfce7;border:2px solid #86efac;border-radius:14px;padding:14px;">
💡 핵심:<br>
Optimizer는 Loss를 줄이는 방향으로 모델의 가중치를 수정합니다.
</div>

</div>