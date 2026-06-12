<div style="background:#f0fdf4;border:2px solid #bbf7d0;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">👣</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Stride — Kernel의 이동 간격
      </div>
      <div style="font-size:14px;color:#64748b;">
        Kernel이 이미지를 얼마나 빠르게 훑을지 결정합니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #dcfce7;border-radius:14px;padding:18px;font-size:14px;line-height:2;color:#334155;">
    <div>
      <strong style="color:#22c55e;">Stride</strong>
      는 Kernel이 한 번 이동할 때 움직이는 칸 수를 의미합니다.
    </div>
    <div>
      Stride가 1이면 Kernel이 한 칸씩 이동하며
      이미지의 정보를 촘촘하게 살펴봅니다.
    </div>
    <div>
      Stride가 2이면 두 칸씩 건너뛰며 이동하기 때문에
      계산량은 줄지만 일부 정보는 놓칠 수 있습니다.
    </div>
    <div>
      따라서 Stride는
      <strong>연산 속도와 정보 보존 사이의 균형</strong>
      을 결정하는 중요한 하이퍼파라미터입니다.
    </div>
  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;">
    Stride = 1

    □ □ □ □ □

    Stride = 2

    □   □   □
  </div>

  <div style="margin-top:18px;background:#fef3c7;border:2px solid #fde68a;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    Stride가 커질수록 계산량은 줄지만 출력 크기도 작아집니다.
  </div>

</div>