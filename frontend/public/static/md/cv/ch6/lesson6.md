<div style="background:#ecfdf5;border:2px solid #86efac;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">💻</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        실습 — MaxPool Layer 생성하기
      </div>
      <div style="font-size:14px;color:#64748b;">
        CNN에서 가장 많이 사용하는 Pooling Layer를 만들어봅시다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1px solid #bbf7d0;border-radius:14px;padding:18px;color:#334155;line-height:2;">
    아래 코드는 CNN에서 가장 많이 사용하는
    MaxPool Layer입니다.
    <br><br>
    kernel_size=2 는
    2×2 영역을 한 번에 살펴본다는 의미입니다.
    <br><br>
    stride=2 는
    Pooling Window가 2칸씩 이동한다는 의미입니다.
    <br><br>
    따라서 Feature Map의 가로와 세로 크기가
    절반으로 감소합니다.
    <br><br>

    예를 들어

    224×224 입력은

    112×112 출력으로 변환됩니다.

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.8;white-space:pre;">
import torch.nn as nn

pool = nn.MaxPool2d(
    kernel_size=2,
    stride=2
)
  </div>

  <div style="margin-top:18px;background:#dcfce7;border:2px solid #86efac;border-radius:14px;padding:16px;line-height:1.9;">
    <strong>코드 분석</strong><br><br>
    • nn.MaxPool2d() → MaxPooling Layer 생성<br>
    • kernel_size=2 → 2×2 영역에서 최대값 선택<br>
    • stride=2 → 2칸씩 이동하며 Pooling 수행<br>
    • 결과적으로 높이와 너비가 절반으로 감소
    <br><br>

    CNN에서는 Conv Block 뒤에
    MaxPool을 배치하는 경우가 매우 많습니다.

  </div>

  <div style="margin-top:18px;background:#dcfce7;border:2px solid #86efac;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    MaxPool(2,2)은 Feature Map 크기를 절반으로 줄이는 CNN의 대표적인 다운샘플링 방법입니다.
  </div>

</div>