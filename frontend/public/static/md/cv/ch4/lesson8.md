<div style="background:#ecfdf5;border:2px solid #86efac;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">💻</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
실습 — Adam Optimizer 생성하기
</div>
<div style="font-size:14px;color:#64748b;">
가중치를 업데이트하는 Optimizer를 생성합니다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #bbf7d0;border-radius:14px;padding:18px;color:#334155;line-height:2;">

Optimizer는 Loss를 줄이는 방향으로
모델의 Weight를 수정합니다.

Adam은 현재 딥러닝에서 가장 많이 사용되는 Optimizer입니다.

학습 속도가 빠르고 안정적이기 때문에
대부분의 CNN 모델에서 기본적으로 사용됩니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.8;white-space:pre;overflow-x:auto;">
import torch.optim as optim

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)
</div>

<div style="margin-top:18px;background:#dcfce7;border:2px solid #86efac;border-radius:14px;padding:14px;">
💡 결과:<br>
모델 학습에 사용할 Adam Optimizer가 생성됩니다.
</div>

</div>