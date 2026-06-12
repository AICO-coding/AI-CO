<div style="background:#fefce8;border:2px solid #fde047;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">💻</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        실습 — Padding으로 크기 유지하기
      </div>
      <div style="font-size:14px;color:#64748b;">
        Conv Layer에서 padding=1이 어떤 역할을 하는지 확인해봅시다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1px solid #fde68a;border-radius:14px;padding:18px;color:#334155;line-height:2;">
    아래 코드는 가장 기본적인 CNN Layer입니다.
    <br><br>
    Kernel Size는 3×3이며
    Padding은 1로 설정되어 있습니다.
    <br><br>
    이 설정 덕분에
    입력 이미지의 크기는 유지됩니다.
    <br><br>

    VGG, ResNet 등 대부분의 CNN이
    이 구조를 사용합니다.

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.8;white-space:pre;">
import torch.nn as nn

conv = nn.Conv2d(
    in_channels=3,
    out_channels=64,
    kernel_size=3,
    padding=1
)
  </div>

  <div style="margin-top:18px;background:#fef9c3;border:2px solid #fde047;border-radius:14px;padding:16px;line-height:1.9;">
    <strong>코드 분석</strong><br><br>
    • in_channels=3 → RGB 이미지 입력<br>
    • out_channels=64 → 64개의 Feature Map 생성<br>
    • kernel_size=3 → 3×3 Kernel 사용<br>
    • padding=1 → 입력과 출력 크기 유지
    <br><br>

    만약 padding=0이라면

    Feature Map 크기는 계속 감소하게 됩니다.

  </div>

  <div style="margin-top:18px;background:#fef9c3;border:2px solid #fde047;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    CNN에서 padding=1은 Feature Map 크기를 보존하기 위한 가장 대표적인 설정입니다.
  </div>

</div>