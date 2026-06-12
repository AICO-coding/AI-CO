<div style="background:#eff6ff;border:2px solid #93c5fd;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">📐</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Shape 변화 — CNN 안에서 크기는 어떻게 변할까?
      </div>
      <div style="font-size:14px;color:#64748b;">
        CNN을 통과하면서 이미지 크기가 변하는 과정을 이해해봅시다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1px solid #bfdbfe;border-radius:14px;padding:18px;color:#334155;line-height:2;">
    CNN에서는 Layer를 통과할 때마다
    Tensor의 Shape이 계속 변합니다.
    <br><br>
    처음에는 RGB 이미지가 입력됩니다.
    <br><br>
    예를 들어
    <strong>(3, 224, 224)</strong>
    <br><br>
    는
    <br>
    Channel = 3
    <br>
    Height = 224
    <br>
    Width = 224
    <br><br>
    를 의미합니다.
    <br><br>
    이후 Convolution Layer를 통과하면
    Channel 수는 증가하고
    Feature Map 개수도 늘어납니다.
    <br><br>
    반면 MaxPool을 통과하면
    Height와 Width가 감소합니다.
    <br><br>
    CNN은
    Channel은 증가시키고
    공간 크기는 줄이는 방향으로 학습합니다.
    <br><br>

    이를 통해

    점점 더 복잡한 특징을 표현할 수 있게 됩니다.

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;white-space:pre;">
Input
(3, 224, 224)

↓

Conv2d(3 → 64)

↓

(64, 224, 224)

↓

MaxPool2d(2)

↓

(64, 112, 112)
  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #93c5fd;border-radius:14px;padding:16px;line-height:1.9;">

    <strong>왜 이런 변화가 필요할까?</strong><br><br>

    • Channel 증가 → 더 많은 특징 학습<br>

    • Height 감소 → 계산량 감소<br>

    • Width 감소 → 메모리 절약<br>

    • 깊은 Layer 학습 가능

  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #60a5fa;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    CNN은 깊어질수록 Channel은 증가하고 Height·Width는 감소하는 구조를 가진다.
  </div>

</div>