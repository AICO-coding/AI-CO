<div style="background:#eef2ff;border:2px solid #c7d2fe;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🏗️</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        VGG16 구조 이해하기
      </div>
      <div style="font-size:14px;color:#64748b;">
        가장 유명한 CNN 아키텍처 중 하나
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #c7d2fe;border-radius:14px;padding:18px;font-size:14px;color:#334155;line-height:2;">
    <div>
      VGG16은 2014년 Oxford Visual Geometry Group(VGG)에서 발표한 CNN 모델입니다.
    </div>
    <div>
      ImageNet 대회에서 뛰어난 성능을 기록하며
      딥러닝 역사에서 가장 유명한 모델 중 하나가 되었습니다.
    </div>
    <div>
      이름의 숫자 16은
      학습 가능한 Layer 수가 총 16개라는 의미입니다.
    </div>
    <div>
      VGG16은 복잡한 구조 대신
      3×3 Convolution을 반복적으로 사용하는 매우 단순한 구조를 가집니다.
    </div>
    <div>
      입력 이미지는 여러 Conv Block을 통과하며
      점점 더 추상적인 특징을 학습합니다.
    </div>
    <div>
      초기 Layer는 Edge, Corner를 학습하고,
      깊은 Layer는 얼굴, 바퀴, 눈과 같은 고수준 특징을 학습합니다.
    </div>
  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;white-space:pre;">
Input (224×224×3)

↓
Conv 64
Conv 64
MaxPool

↓
Conv 128
Conv 128
MaxPool

↓
Conv 256
Conv 256
Conv 256
MaxPool

↓
Conv 512
Conv 512
Conv 512
MaxPool

↓
Conv 512
Conv 512
Conv 512
MaxPool

↓
FC 4096
FC 4096
FC 1000
  </div>

  <div style="margin-top:18px;background:#e0e7ff;border:2px solid #a5b4fc;border-radius:14px;padding:16px;">
    <b>왜 성공했을까?</b><br><br>
    • 모든 Conv가 3×3 사용<br>
    • 구조가 단순함<br>
    • ReLU 반복 사용<br>
    • 깊은 Layer 구성<br>
    • 큰 Receptive Field 확보

  </div>

  <div style="margin-top:18px;background:#c7d2fe;border:2px solid #818cf8;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    VGG16은 3×3 Convolution을 반복하여 깊은 CNN을 구성한 대표적인 모델입니다.
  </div>

</div>