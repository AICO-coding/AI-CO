<div style="background:#ecfeff;border:2px solid #67e8f9;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;gap:12px;align-items:center;margin-bottom:20px;">
    <div style="font-size:30px;">🚀</div>
    <div>
      <div style="font-size:22px;font-weight:900;color:#0f172a;">
        CIFAR-10 학습
      </div>
      <div style="font-size:14px;color:#64748b;">
        CNN이 실제 이미지 데이터를 학습하는 과정
      </div>
    </div>
  </div>

  <div style="background:white;border-radius:14px;padding:20px;color:#334155;line-height:2;">
    <p>
      CIFAR-10은 컴퓨터 비전에서 가장 널리 사용되는 이미지 분류 데이터셋 중 하나입니다.
    </p>
    <p>
      총 10개의 클래스로 구성되어 있으며,
      비행기, 자동차, 새, 고양이, 사슴, 개, 개구리, 말, 배, 트럭 이미지를 포함합니다.
    </p>
    <p>
      CNN 학습 과정은 크게 5단계로 이루어집니다.
    </p>
    <p>
      ① 이미지를 모델에 입력한다.
      <br>
      ② 모델이 예측값을 출력한다.
      <br>
      ③ Loss를 계산한다.
      <br>
      ④ Backward로 Gradient를 계산한다.
      <br>
      ⑤ Optimizer가 가중치를 업데이트한다.
    </p>
    <p>
      이러한 과정을 수천 번 반복하면서 모델은 점점 더 정확한 특징을 학습하게 됩니다.
    </p>

  </div>

  <div style="margin-top:20px;background:#0f172a;color:#cbd5e1;border-radius:14px;padding:18px;font-family:monospace;white-space:pre;">
Image
  ↓
Forward
  ↓
Loss
  ↓
Backward
  ↓
Optimizer
  ↓
Update
  </div>

  <div style="margin-top:18px;background:#cffafe;border:2px solid #22d3ee;border-radius:14px;padding:14px;">
    💡 핵심<br>
    학습은 Forward → Loss → Backward → Update를 반복하는 과정이다.
  </div>

</div>