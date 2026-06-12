<div style="background:#fff7ed;border:2px solid #fdba74;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">💻</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
실습 — Loss 계산하기
</div>
<div style="font-size:14px;color:#64748b;">
예측값과 정답의 차이를 계산해봅시다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #fed7aa;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">

Loss는 모델의 예측값이 실제 정답과 얼마나 차이가 나는지 측정하는 값입니다.

아래 예제에서는 MSELoss를 사용하여
예측값(pred)과 정답(target)의 오차를 계산합니다.

Loss는 Tensor 형태로 반환되기 때문에
item() 함수를 사용하여 실제 숫자 값으로 변환할 수 있습니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.8;white-space:pre;overflow-x:auto;">
import torch
import torch.nn as nn

criterion = nn.MSELoss()

pred = torch.tensor([0.8])
target = torch.tensor([1.0])

loss = criterion(pred, target)

print(loss.item())
</div>

<div style="margin-top:18px;background:#ffedd5;border:2px solid #fdba74;border-radius:14px;padding:14px;">
💡 결과:<br>
예측값과 정답의 차이를 숫자로 확인할 수 있습니다.
</div>

</div>