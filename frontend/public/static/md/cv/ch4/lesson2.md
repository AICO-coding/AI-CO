<div style="background:#eef7ff;border:2px solid #c2e4ff;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">💻</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
실습 — Forward 수행하기
</div>
<div style="font-size:14px;color:#64748b;">
모델에 입력 데이터를 넣어 예측값을 계산해봅시다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #dbeafe;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">

이 코드는 가장 간단한 신경망인 Linear Layer를 생성한 뒤,
입력 데이터를 모델에 통과시켜 예측값을 계산합니다.

Forward는 입력 데이터가 신경망 내부를 지나가며
출력값(Prediction)을 생성하는 과정입니다.

CNN에서도 이미지가 여러 Layer를 통과하며
최종 예측 결과를 만드는 과정 전체를 Forward라고 부릅니다.

아래 코드를 실행하면 입력 데이터 x가 모델을 통과하여
2개의 출력값을 생성합니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.8;white-space:pre;overflow-x:auto;">
import torch
import torch.nn as nn

model = nn.Linear(4, 2)

x = torch.randn(1, 4)

output = model.forward(x)

print(output)
</div>

<div style="margin-top:18px;background:#dbeafe;border:2px solid #93c5fd;border-radius:14px;padding:14px;">
💡 결과:<br>
입력 데이터가 모델을 통과하여 예측값이 생성됩니다.
</div>

</div>