<div style="background:#f5f3ff;border:2px solid #c4b5fd;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">💻</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
실습 — CrossEntropyLoss 사용하기
</div>
<div style="font-size:14px;color:#64748b;">
분류 문제에서 가장 많이 사용하는 Loss 함수입니다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #ddd6fe;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">

CNN 분류 문제에서는 CrossEntropyLoss를 가장 많이 사용합니다.

모델은 클래스별 점수(Logits)를 출력하고,
Loss 함수는 이를 실제 정답과 비교하여
얼마나 틀렸는지 계산합니다.

Loss가 작을수록 모델이 정답에 가까운 예측을 했다는 의미입니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.8;white-space:pre;overflow-x:auto;">
import torch
import torch.nn as nn

criterion = nn.CrossEntropyLoss()

output = torch.tensor([[2.5, 0.1, 0.3]])
target = torch.tensor([0])

loss = criterion(output, target)

print(loss)
</div>

<div style="margin-top:18px;background:#ede9fe;border:2px solid #c4b5fd;border-radius:14px;padding:14px;">
💡 결과:<br>
모델이 정답 클래스를 얼마나 잘 맞췄는지 평가할 수 있습니다.
</div>

</div>