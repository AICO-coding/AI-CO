<div style="background:#eff6ff;border:2px solid #93c5fd;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">💻</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        실습 — CNN에서 Shape 변화 확인하기
      </div>
      <div style="font-size:14px;color:#64748b;">
        Conv와 Pool을 거치며 Shape이 어떻게 변하는지 확인해봅시다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1px solid #bfdbfe;border-radius:14px;padding:18px;color:#334155;line-height:2;">
    아래 코드는
    Conv → Pool
    구조를 수행합니다.
    <br><br>
    입력 이미지 Shape은
    (1, 3, 224, 224)
    입니다.
    <br><br>
    여기서 1은 Batch Size입니다.
    <br><br>
    Conv Layer를 통과하면
    Channel 수가 64개로 증가합니다.
    <br><br>
    Pool Layer를 통과하면

    Height와 Width가 절반으로 감소합니다.

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.8;white-space:pre;">
import torch
import torch.nn as nn

x = torch.randn(1, 3, 224, 224)

conv = nn.Conv2d(
    in_channels=3,
    out_channels=64,
    kernel_size=3,
    padding=1
)

pool = nn.MaxPool2d(
    kernel_size=2,
    stride=2
)

x = conv(x)
print(x.shape)

x = pool(x)
print(x.shape)
  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #93c5fd;border-radius:14px;padding:16px;line-height:1.9;">
    <strong>실행 결과</strong><br><br>
    torch.Size([1, 64, 224, 224])<br>
    torch.Size([1, 64, 112, 112])
    <br><br>
    <strong>코드 분석</strong><br><br>
    • Conv2d → Channel 3 → 64 증가<br>
    • Padding=1 → 크기 유지<br>
    • MaxPool2d → Height, Width 절반 감소<br>
    • CNN에서 가장 기본적인 Shape 변화 예시

  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #60a5fa;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    Conv는 Channel을 늘리고, Pool은 공간 크기를 줄인다.
  </div>

</div>