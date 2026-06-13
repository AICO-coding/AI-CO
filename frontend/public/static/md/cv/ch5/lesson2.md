<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">💻</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
실습: CNN Layer를 깊게 쌓기
</div>
<div style="font-size:14px;color:#64748b;">
Layer를 여러 개 쌓아 복잡한 특징을 학습합니다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #e2e8f0;border-radius:14px;padding:18px;line-height:1.9;font-size:14px;color:#334155;">

첫 번째 Layer는 Edge를 찾고,
두 번째 Layer는 Edge를 조합하여 더 복잡한 특징을 찾습니다.

Layer를 여러 개 쌓을수록
더 추상적인 특징을 학습할 수 있습니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;line-height:1.8;white-space:pre;">
import torch.nn as nn

model = nn.Sequential(
    nn.Conv2d(3, 64, 3, padding=1),

    nn.ReLU(),

    nn.Conv2d(64, 64, 3, padding=1),

    nn.ReLU()
)
</div>

<div style="margin-top:18px;background:#f1f5f9;border:1.5px solid #cbd5e1;border-radius:14px;padding:16px;">

<b>코드 설명</b><br><br>

<b>nn.Conv2d(3, 64, 3)</b><br>
입력 채널 3(RGB)를 받아
64개의 Feature Map을 생성합니다.
<br><br>

<b>nn.ReLU()</b><br>
비선형성을 추가하여
복잡한 패턴을 학습할 수 있게 만듭니다.
<br><br>

두 개의 Conv Layer를 연속으로 사용하면
더 복잡한 특징을 추출할 수 있습니다.

</div>

<div style="margin-top:18px;background:#e0f2fe;border:2px solid #7dd3fc;border-radius:14px;padding:14px;">
💡 핵심:<br>
깊은 CNN은 Layer마다 특징을 점점 추상화합니다.
</div>

</div>