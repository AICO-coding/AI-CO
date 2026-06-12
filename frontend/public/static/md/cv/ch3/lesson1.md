<div style="background:#ecfeff;border:2px solid #a5f3fc;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🔍</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Feature Extraction — 특징 추출
      </div>
      <div style="font-size:14px;color:#64748b;">
        CNN이 이미지에서 중요한 정보만 찾아내는 과정입니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #bae6fd;border-radius:14px;padding:18px;font-size:14px;line-height:2;color:#334155;">
    <div>
      사람이 고양이 사진을 볼 때 모든 픽셀 값을 기억하지는 않습니다.
    </div>
    <div>
      대신 귀의 모양, 눈의 위치, 수염, 털의 패턴 같은 특징을 보고
      "이건 고양이구나"라고 판단합니다.
    </div>
    <div>
      CNN도 비슷한 방식으로 동작합니다.
    </div>
    <div>
      이미지 전체를 그대로 외우는 것이 아니라,
      분류에 도움이 되는 중요한 특징만 찾아냅니다.
    </div>
    <div>
      이러한 특징을 Feature라고 하며,
      특징을 찾아내는 과정을 Feature Extraction이라고 합니다.
    </div>
    <div>
      CNN의 Convolution Layer는 Feature Extraction을 수행하는 핵심 레이어입니다.
    </div>
    <div>
      초반 Layer에서는 Edge(윤곽선), Corner(모서리) 같은 단순한 특징을 학습하고,
      뒤쪽 Layer에서는 눈, 바퀴, 문 손잡이 같은 더 복잡한 특징을 학습합니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

<pre style="margin:0;color:#cbd5e1;font-family:monospace;line-height:1.9;">
고양이 이미지

↓ Layer 1

Edge (윤곽선)

↓ Layer 2

Eye / Ear Pattern

↓ Layer 3

Cat Face

↓ 최종 분류

Cat
</pre>

  </div>

  <div style="margin-top:18px;background:#cffafe;border:2px solid #67e8f9;border-radius:14px;padding:14px;">
    💡 핵심<br>
    CNN은 이미지를 그대로 기억하지 않는다.<br>
    중요한 특징(Feature)을 추출하고 그 특징을 이용해 학습한다.
  </div>

</div>