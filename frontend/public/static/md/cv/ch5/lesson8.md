<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">💻</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        실습: VGG16 구조 살펴보기
      </div>
      <div style="font-size:14px;color:#64748b;">
        실제 PyTorch 코드 형태의 VGG Block
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #e2e8f0;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    아래 코드는 VGG16의 첫 번째 Block을 단순화한 예시입니다.
    VGG는 이런 구조를 반복하여 깊은 네트워크를 구성합니다.
  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;line-height:1.8;white-space:pre;">
import torch.nn as nn

block = nn.Sequential(

    nn.Conv2d(
        in_channels=3,
        out_channels=64,
        kernel_size=3,
        padding=1
    ),

    nn.ReLU(),

    nn.Conv2d(
        in_channels=64,
        out_channels=64,
        kernel_size=3,
        padding=1
    ),

    nn.ReLU(),

    nn.MaxPool2d(
        kernel_size=2,
        stride=2
    )

)
  </div>

  <div style="margin-top:18px;background:#f1f5f9;border:1.5px solid #cbd5e1;border-radius:14px;padding:16px;">
    <b>코드 설명</b><br><br>
    <b>Conv2d</b><br>
    이미지 특징을 추출합니다.
    <br><br>
    <b>ReLU</b><br>
    비선형성을 추가하여 복잡한 패턴을 학습합니다.
    <br><br>
    <b>두 번째 Conv</b><br>
    이전 특징을 조합하여 더 복잡한 특징을 만듭니다.
    <br><br>
    <b>MaxPool2d</b><br>
    Feature Map 크기를 절반으로 줄여 계산량을 감소시킵니다.

  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #93c5fd;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    VGG16은 Conv → ReLU를 반복한 뒤 MaxPool을 적용하는 Block 구조를 사용합니다.
  </div>

</div>