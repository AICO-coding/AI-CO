<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">💻</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        실습: Receptive Field 키우기
      </div>
      <div style="font-size:14px;color:#64748b;">
        Layer를 추가하면 Receptive Field가 증가합니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #e2e8f0;border-radius:14px;padding:18px;font-size:14px;color:#334155;line-height:2;">

    아래 코드는 3×3 Convolution을
    세 번 연속 수행하는 예시입니다.

    Layer가 깊어질수록
    각 뉴런이 참고하는 입력 영역이 넓어집니다.

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

    nn.ReLU(),

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
    )

)
  </div>

  <div style="margin-top:18px;background:#f1f5f9;border:1.5px solid #cbd5e1;border-radius:14px;padding:16px;">

    <b>코드 설명</b><br><br>

    <b>첫 번째 Conv</b><br>
    입력 이미지의 작은 영역(3×3)을 관찰합니다.
    <br><br>

    <b>두 번째 Conv</b><br>
    첫 번째 Conv 결과를 다시 분석합니다.
    따라서 더 넓은 영역을 볼 수 있습니다.
    <br><br>

    <b>세 번째 Conv</b><br>
    Receptive Field가 더욱 커집니다.
    <br><br>

    <b>padding=1</b><br>
    Feature Map 크기를 유지하면서
    정보를 안정적으로 전달합니다.

  </div>

  <div style="margin-top:18px;background:#fef3c7;border:2px solid #fcd34d;border-radius:14px;padding:14px;">

    <b>Receptive Field 변화</b><br><br>

    Conv 1개
    → 약 3×3<br><br>

    Conv 2개
    → 약 5×5<br><br>

    Conv 3개
    → 약 7×7

  </div>

  <div style="margin-top:18px;background:#fde68a;border:2px solid #facc15;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    CNN은 Layer를 깊게 쌓을수록 Receptive Field가 커지고,
    더 넓은 문맥(Context)을 이해할 수 있습니다.
  </div>

</div>