<div style="background:#eef7ff;border:2px solid #c2e4ff;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">💻</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Kernel 코드 따라해보기
      </div>
      <div style="font-size:14px;color:#64748b;margin-top:4px;">
        PyTorch로 3×3 Kernel을 사용하는 Convolution Layer를 만들어봅시다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #dbeafe;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      지금까지 Kernel이 이미지 속 특징을 추출하는 작은 필터라는 것을 배웠습니다.
    </div>

    <div>
      PyTorch에서는
      <strong style="color:#1681c4;">nn.Conv2d()</strong>
      를 사용하여 Convolution Layer를 생성할 수 있습니다.
    </div>

    <div>
      아래 코드를 직접 입력하며 각 파라미터의 의미를 확인해보세요.
    </div>
  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">
    <pre style="margin:0;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.9;">
import torch.nn as nn

conv = nn.Conv2d(
    in_channels=1,
    out_channels=16,
    kernel_size=3
)

print(conv)
    </pre>
  </div>

  <div style="margin-top:18px;background:white;border:1.5px solid #dbeafe;border-radius:14px;padding:18px;">

    <div style="font-size:15px;font-weight:800;color:#0f172a;margin-bottom:12px;">
      코드 설명
    </div>

    <div style="font-size:14px;color:#334155;line-height:2;">

      <strong style="color:#1681c4;">in_channels=1</strong><br>
      입력 이미지의 채널(Channel) 수입니다.<br>
      흑백(Grayscale) 이미지는 1개의 채널을 사용합니다.

      <br><br>

      <strong style="color:#1681c4;">out_channels=16</strong><br>
      생성할 Kernel의 개수입니다.<br>
      Kernel이 16개라면 16개의 Feature Map이 생성됩니다.

      <br><br>

      <strong style="color:#1681c4;">kernel_size=3</strong><br>
      Kernel의 크기를 의미합니다.<br>
      즉, 3×3 Kernel을 사용한다는 뜻입니다.

    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

    <div style="font-size:14px;font-weight:700;color:white;margin-bottom:10px;">
      실행 결과
    </div>

    <pre style="margin:0;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.9;">
Conv2d(
    1, 16,
    kernel_size=(3, 3),
    stride=(1, 1)
)
    </pre>

  </div>

  <div style="margin-top:18px;background:#ecfeff;border:2px solid #bae6fd;border-radius:14px;padding:14px 16px;">
    <div style="font-size:13px;font-weight:700;color:#0f172a;line-height:1.8;">
      📌 확인해보기<br>
      kernel_size를 5로 변경하면 어떤 크기의 Kernel이 생성될까요?
    </div>
  </div>

  <div style="margin-top:18px;background:#fff3eb;border:2px solid #ffd0b0;border-radius:14px;padding:14px 16px;">
    <div style="font-size:13px;font-weight:700;color:#0f172a;line-height:1.8;">
      💡 핵심<br>
      • nn.Conv2d()는 Convolution Layer를 생성한다.<br>
      • kernel_size=3은 3×3 Kernel을 의미한다.<br>
      • out_channels 개수만큼 Feature Map이 생성된다.
    </div>
  </div>

</div>