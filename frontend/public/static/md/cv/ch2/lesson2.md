<div style="background:#eef7ff;border:2px solid #c2e4ff;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🧩</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Kernel — 특징을 찾는 작은 필터
      </div>
      <div style="font-size:14px;color:#64748b;margin-top:4px;">
        CNN은 Kernel을 이용해 이미지 속 중요한 특징을 찾아냅니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #dbeafe;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      <strong style="color:#1681c4;">Kernel(Filter)</strong>
      은 Convolution 연산에 사용되는 작은 행렬입니다.
    </div>
    <div>
      Kernel은 이미지 전체를 한 번에 보는 대신,
      작은 영역을 조금씩 살펴보며 특징을 추출합니다.
    </div>
    <div>
      각 Kernel은 특정 패턴에 민감하게 반응합니다.
      예를 들어 세로선, 가로선, 경계선(Edge) 등을 찾을 수 있습니다.
    </div>
    <div>
      학습이 진행되면 CNN은 어떤 Kernel이 가장 유용한지
      스스로 학습하게 됩니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;font-family:monospace;color:#cbd5e1;line-height:1.8;">
    Example Kernel (3×3)

    [ 1  0 -1 ]
    [ 1  0 -1 ]
    [ 1  0 -1 ]

    → 세로 방향 경계 감지
  </div>

  <div style="margin-top:18px;background:#fff3eb;border:2px solid #ffd0b0;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    Kernel은 이미지 속 특정 패턴을 탐지하는 작은 필터입니다.
  </div>

</div>