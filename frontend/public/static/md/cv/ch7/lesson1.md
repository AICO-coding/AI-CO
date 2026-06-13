<div style="background:#eff6ff;border:2px solid #93c5fd;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🧱</div>
    <div>
      <div style="font-size:22px;font-weight:900;color:#1e3a8a;">
        VGG 구조 조립
      </div>
      <div style="font-size:14px;color:#64748b;">
        작은 블록을 반복하여 거대한 CNN을 만드는 방법
      </div>
    </div>
  </div>

  <div style="background:white;border-radius:14px;padding:20px;line-height:2;color:#334155;">
    <p>
      VGG는 복잡한 구조를 사용하지 않습니다.
      대신 아주 단순한 구조를 반복해서 깊은 신경망을 만듭니다.
    </p>
    <p>
      가장 기본적인 블록은
      Conv → ReLU → Conv → ReLU → MaxPool 형태입니다.
    </p>
    <p>
      이 블록을 여러 번 쌓아가면서
      점점 더 많은 특징을 추출하게 됩니다.
    </p>
    <p>
      초기 Layer는 선, 모서리, 색상 같은 단순한 특징을 학습합니다.
      하지만 Layer가 깊어질수록 얼굴, 바퀴, 동물 형태 같은
      복잡한 특징을 학습하게 됩니다.
    </p>
    <p>
      VGG16은 이러한 블록을 총 13개의 Convolution Layer와
      3개의 Fully Connected Layer로 구성하여
      총 16개의 학습 가능한 Layer를 가집니다.
    </p>

  </div>

  <div style="margin-top:20px;background:#0f172a;color:#cbd5e1;border-radius:14px;padding:18px;font-family:monospace;line-height:1.8;white-space:pre;">
Input
 ↓
Conv
 ↓
ReLU
 ↓
Conv
 ↓
ReLU
 ↓
MaxPool
 ↓
다음 Block
  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #60a5fa;border-radius:14px;padding:14px;">
    💡 핵심<br>
    VGG는 복잡한 Layer 대신 단순한 Block을 반복하여 깊은 CNN을 만든다.
  </div>

</div>