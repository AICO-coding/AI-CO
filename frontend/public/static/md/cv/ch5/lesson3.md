<div style="background:#fefce8;border:2px solid #fde68a;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">👀</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Receptive Field란?
      </div>
      <div style="font-size:14px;color:#64748b;">
        CNN이 한 번에 볼 수 있는 이미지 영역의 크기
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #fde68a;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      CNN은 사람처럼 이미지 전체를 한 번에 보는 것이 아니라
      작은 영역을 조금씩 살펴보며 특징을 찾습니다.
    </div>
    <div>
      이때 특정 뉴런이 입력 이미지에서
      실제로 참고하는 영역을
      <strong style="color:#ca8a04;">Receptive Field</strong>라고 합니다.
    </div>
    <div>
      쉽게 말하면,
      CNN의 뉴런이 "볼 수 있는 시야 범위"라고 생각하면 됩니다.
    </div>
    <div>
      예를 들어 3×3 Kernel을 사용하면
      첫 번째 Convolution Layer의 뉴런은
      이미지의 3×3 영역만 볼 수 있습니다.
    </div>
    <div>
      하지만 Layer를 여러 개 쌓으면
      Receptive Field가 점점 커집니다.
    </div>
    <div>
      따라서 깊은 CNN은
      이미지의 더 넓은 영역을 이해할 수 있게 됩니다.
    </div>
    <div>
      자동차를 분류한다고 가정해봅시다.
    </div>
    <div style="margin-left:12px;">
      • 얕은 Layer → 바퀴 일부<br>
      • 중간 Layer → 차문<br>
      • 깊은 Layer → 자동차 전체
    </div>
    <div>
      이처럼 Receptive Field가 커질수록
      더 큰 구조를 인식할 수 있습니다.
    </div>
  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;white-space:pre;">
Layer 1
[ 3 × 3 ]

      ↓

Layer 2
[ 5 × 5 ]

      ↓

Layer 3
[ 7 × 7 ]

      ↓

Receptive Field 증가
  </div>

  <div style="margin-top:18px;background:#fef3c7;border:2px solid #fcd34d;border-radius:14px;padding:14px;">

    <b>왜 중요할까?</b><br><br>

    작은 Receptive Field
    → 세부 특징만 확인 가능<br><br>

    큰 Receptive Field
    → 물체 전체 구조 이해 가능

  </div>

  <div style="margin-top:18px;background:#fde68a;border:2px solid #facc15;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    Receptive Field는 CNN이 볼 수 있는 입력 영역의 크기이며,
    Layer가 깊어질수록 점점 커집니다.
  </div>

</div>