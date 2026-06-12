<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">💻</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        실습: Channel 증가 확인하기
      </div>
      <div style="font-size:14px;color:#64748b;">
        VGG가 왜 64 → 128 → 256 → 512로 증가시키는지 살펴봅시다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #e2e8f0;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">

    아래 코드는 VGG 스타일의 Channel 증가 예시입니다.

    각 Convolution Layer를 통과할 때마다
    Feature Map의 Channel 수가 증가합니다.

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;line-height:1.8;white-space:pre;">
import torch.nn as nn

model = nn.Sequential(

    nn.Conv2d(
        in_channels=3,
        out_channels=64,
        kernel_size=3,
        padding=1
    ),

    nn.Conv2d(
        in_channels=64,
        out_channels=128,
        kernel_size=3,
        padding=1
    ),

    nn.Conv2d(
        in_channels=128,
        out_channels=256,
        kernel_size=3,
        padding=1
    ),

    nn.Conv2d(
        in_channels=256,
        out_channels=512,
        kernel_size=3,
        padding=1
    )

)
  </div>

  <div style="margin-top:18px;background:#f1f5f9;border:1.5px solid #cbd5e1;border-radius:14px;padding:16px;">
    <b>코드 설명</b><br><br>
    <b>첫 번째 Conv</b><br>
    RGB 이미지(3채널)를
    64개의 Feature Map으로 변환합니다.
    <br><br>
    <b>두 번째 Conv</b><br>
    64개의 특징을 조합하여
    128개의 특징으로 확장합니다.
    <br><br>
    <b>세 번째 Conv</b><br>
    더 복잡한 패턴을 학습하기 위해
    256채널로 증가합니다.
    <br><br>
    <b>네 번째 Conv</b><br>
    고수준 특징을 표현하기 위해
    512채널을 사용합니다.

  </div>

  <div style="margin-top:18px;background:#ede9fe;border:2px solid #c4b5fd;border-radius:14px;padding:16px;">
    <b>실제 VGG16 흐름</b><br><br>
    3 → 64<br>
    64 → 128<br>
    128 → 256<br>
    256 → 512<br>
    512 → 512
    <br><br>

    Layer가 깊어질수록
    더 많은 특징을 저장합니다.

  </div>

  <div style="margin-top:18px;background:#ddd6fe;border:2px solid #a78bfa;border-radius:14px;padding:16px;">
    <b>왜 공간 크기는 줄이고 채널은 늘릴까?</b><br><br>
    Width, Height는 줄어들어도<br>
    중요한 특징은 유지됩니다.
    <br><br>

    대신 Channel 수를 늘려
    더 다양한 특징을 저장할 수 있습니다.

  </div>

  <div style="margin-top:18px;background:#c4b5fd;border:2px solid #8b5cf6;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    CNN은 깊어질수록 Channel 수를 늘려
    더 많은 특징을 표현하고 학습합니다.
  </div>

</div>