<div style="background:#eef7ff;border:2px solid #c2e4ff;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">➡️</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Forward — 모델이 예측을 만드는 과정
      </div>
      <div style="font-size:14px;color:#64748b;">
        입력 데이터가 신경망을 통과하며 예측값을 계산합니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #dbeafe;border-radius:14px;padding:18px;font-size:14px;line-height:2;color:#334155;">
    <div>
      딥러닝 모델은 입력 데이터를 받으면 여러 층(Layer)을 순서대로 통과시킵니다.
    </div>
    <div>
      이 과정을 통해 최종 예측값(Prediction)을 계산하게 되는데,
      이를 <strong style="color:#2563eb;">Forward Propagation</strong> 또는
      <strong style="color:#2563eb;">Forward Pass</strong>라고 부릅니다.
    </div>
    <div>
      CNN에서는 이미지가
      Convolution → ReLU → Pooling →
      Flatten → FC Layer 순서로 이동하며
      최종 클래스 점수를 계산합니다.
    </div>
    <div>
      학습 과정에서 가장 먼저 수행되는 단계가 Forward이며,
      이후 Loss 계산과 Backpropagation이 진행됩니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;white-space:pre;">
Input Image
      ↓
Convolution
      ↓
ReLU
      ↓
Pooling
      ↓
Flatten
      ↓
FC Layer
      ↓
Prediction
  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #93c5fd;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    Forward는 입력 데이터를 모델에 통과시켜 예측값을 계산하는 과정입니다.
  </div>

</div>