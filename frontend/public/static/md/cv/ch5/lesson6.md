<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">💻</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        실습: 3×3 Convolution 여러 번 사용하기
      </div>
      <div style="font-size:14px;color:#64748b;">
        VGG의 핵심 아이디어를 코드로 확인해봅시다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #e2e8f0;border-radius:14px;padding:18px;font-size:14px;color:#334155;line-height:2;">

    VGG는 큰 Kernel을 사용하지 않습니다.

    대신 작은 3×3 Kernel을 여러 번 반복하여
    더 넓은 영역을 관찰합니다.

    아래 코드는 VGG 스타일의
    Convolution Block입니다.

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;line-height:1.8;white-space:pre;">
import torch.nn as nn

block = nn.Sequential(

    nn.Conv2d(
        in_channels=64,
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

    nn.ReLU()

)
  </div>

  <div style="margin-top:18px;background:#f1f5f9;border:1.5px solid #cbd5e1;border-radius:14px;padding:16px;">
    <b>코드 설명</b><br><br>
    <b>kernel_size=3</b><br>
    3×3 Kernel을 사용합니다.
    <br><br>
    <b>padding=1</b><br>
    Feature Map 크기를 유지합니다.
    <br><br>
    <b>첫 번째 Conv</b><br>
    Edge, Texture 같은 기본 특징을 추출합니다.
    <br><br>
    <b>두 번째 Conv</b><br>
    이전 특징을 조합하여
    더 복잡한 패턴을 학습합니다.
    <br><br>
    <b>ReLU</b><br>
    비선형성을 추가하여
    더 복잡한 함수를 표현할 수 있게 합니다.

  </div>

  <div style="margin-top:18px;background:#ecfccb;border:2px solid #a3e635;border-radius:14px;padding:14px;">
    <b>이 블록이 중요한 이유</b><br><br>
    Conv 1회보다<br>
    Conv 2회가 더 넓은 Receptive Field를 가집니다.
    <br><br>

    또한 ReLU가 두 번 들어가므로
    모델의 표현력이 증가합니다.

  </div>

  <div style="margin-top:18px;background:#bbf7d0;border:2px solid #4ade80;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    VGG는 3×3 Conv를 반복하여
    적은 파라미터로 넓은 영역을 보고
    더 복잡한 특징을 학습합니다.
  </div>

</div>