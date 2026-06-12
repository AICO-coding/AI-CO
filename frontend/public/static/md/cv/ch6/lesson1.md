<div style="background:#eff6ff;border:2px solid #93c5fd;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🏗️</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Conv Stack — Convolution Layer를 여러 번 쌓는 이유
      </div>
      <div style="font-size:14px;color:#64748b;">
        깊은 CNN은 여러 개의 Conv Layer를 연속으로 사용합니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1px solid #dbeafe;border-radius:14px;padding:18px;color:#334155;line-height:2;">
    CNN은 일반적으로 Convolution Layer를 한 번만 사용하지 않습니다.
    <br><br>
    여러 개의 Conv Layer를 연속으로 연결하여
    점점 더 복잡한 특징을 학습합니다.
    <br><br>
    첫 번째 Conv Layer는 Edge(경계선)나 단순한 방향성을 학습합니다.
    <br>
    두 번째 Conv Layer는 여러 Edge를 조합하여 Texture(질감)을 학습합니다.
    <br>
    세 번째 Conv Layer는 물체의 Shape(형태)를 이해하기 시작합니다.
    <br><br>
    즉 Layer가 깊어질수록 단순한 특징에서 복잡한 특징으로 발전합니다.
    <br><br>
    이것이 CNN이 강아지, 자동차, 사람 얼굴 같은 복잡한 객체를<br>
    인식할 수 있는 이유입니다.

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;">
Input Image<br>
      ↓<br>

Conv 1
(Edge)<br>
      ↓<br>

Conv 2
(Texture)<br>
      ↓<br>

Conv 3
(Shape)<br>
      ↓<br>

Object Feature
  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #93c5fd;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    Conv Stack은 여러 Conv Layer를 쌓아 단순 특징 → 복잡한 특징으로 발전시키는 CNN의 핵심 구조입니다.
  </div>

</div>