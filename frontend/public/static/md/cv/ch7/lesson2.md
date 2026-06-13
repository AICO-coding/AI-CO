<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">💻</div>
    <div>
      <div style="font-size:22px;font-weight:900;color:#0f172a;">
        실습 : VGG Block 만들기
      </div>
      <div style="font-size:14px;color:#64748b;">
        Conv → ReLU → Conv → ReLU → MaxPool
      </div>
    </div>
  </div>

  <div style="background:white;border-radius:14px;padding:20px;color:#334155;line-height:2;">
    <p>
      아래 코드는 VGG의 가장 기본적인 Feature Extraction Block입니다.
    </p>
    <p>
      첫 번째 Conv Layer가 입력 이미지에서 특징을 추출합니다.
    </p>
    <p>
      ReLU는 비선형성을 추가하여 더 복잡한 패턴을 학습하게 만듭니다.
    </p>
    <p>
      두 번째 Conv Layer가 특징을 더욱 정교하게 추출합니다.
    </p>
    <p>
      마지막 MaxPool Layer는 Feature Map 크기를 절반으로 줄여
      계산량을 감소시킵니다.
    </p>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:20px;color:#e2e8f0;font-family:monospace;white-space:pre;line-height:1.7;">
import torch.nn as nn

features = nn.Sequential(

    nn.Conv2d(3, 64, 3, padding=1),
    nn.ReLU(),

    nn.Conv2d(64, 64, 3, padding=1),
    nn.ReLU(),

    nn.MaxPool2d(kernel_size=2, stride=2)

)
  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #60a5fa;border-radius:14px;padding:14px;">
    💡 핵심<br>
    VGG는 이러한 Block을 반복적으로 쌓아 깊은 CNN을 구성한다.
  </div>

</div>