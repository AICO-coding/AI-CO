<div style="background:#eff6ff;border:2px solid #93c5fd;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">💻</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        실습 — Conv Stack 직접 만들기
      </div>
      <div style="font-size:14px;color:#64748b;">
        여러 개의 Convolution Layer를 연결해 CNN Block을 구성해봅시다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1px solid #dbeafe;border-radius:14px;padding:18px;color:#334155;line-height:2;">
    아래 코드는 Conv Layer를 세 번 연속으로 사용하는
    Conv Stack 예제입니다.
    <br><br>
    첫 번째 Layer는 RGB 이미지를 입력받아
    64개의 Feature Map을 생성합니다.
    <br><br>
    두 번째 Layer는 이미 추출된 특징을
    더 정교하게 분석합니다.
    <br><br>
    세 번째 Layer에서는 채널 수를 128개로 늘려
    더욱 다양한 특징을 표현합니다.
    <br><br>
    각 Conv 뒤에 ReLU를 추가하여
    CNN이 복잡한 패턴을 학습할 수 있도록 만듭니다.

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.8;white-space:pre;">
import torch.nn as nn

block = nn.Sequential(
    nn.Conv2d(3,64,kernel_size=3,padding=1),
    nn.ReLU(),

    nn.Conv2d(64,64,kernel_size=3,padding=1),
    nn.ReLU(),

    nn.Conv2d(64,128,kernel_size=3,padding=1),
    nn.ReLU()
)
  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #93c5fd;border-radius:14px;padding:16px;line-height:1.9;">
    <strong>코드 분석</strong><br><br>
    • nn.Conv2d(3,64) → RGB(3채널)를 64개 특징맵으로 변환<br>
    • nn.Conv2d(64,64) → 특징을 더욱 세밀하게 분석<br>
    • nn.Conv2d(64,128) → 채널 수를 늘려 더 많은 특징 표현<br>
    • nn.ReLU() → 음수를 제거하고 비선형성을 추가
    <br><br>

    실제 VGG와 같은 CNN도 이러한 Conv Stack을 반복적으로 사용합니다.

  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #93c5fd;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    Conv Stack은 Conv + ReLU를 반복하여 Feature Extraction 능력을 점점 강화하는 구조입니다.
  </div>

</div>