<div style="background:#f5f3ff;border:2px solid #ddd6fe;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">📐</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Output Size — 출력 크기 계산
      </div>
      <div style="font-size:14px;color:#64748b;margin-top:4px;">
        Convolution 이후 Feature Map의 크기를 계산하는 방법입니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #e9d5ff;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      Convolution을 수행하면 입력 이미지(Input Image)가
      새로운 Feature Map으로 변환됩니다.
    </div>
    <div>
      이때 Feature Map의 크기를
      <strong style="color:#7c3aed;">Output Size</strong>
      라고 합니다.
    </div>
    <div>
      Output Size는 입력 크기뿐만 아니라
      <strong>Kernel 크기, Padding, Stride</strong>
      에 의해 결정됩니다.
    </div>
    <div>
      따라서 CNN을 설계할 때는 각 레이어를 통과한 후
      출력 크기가 어떻게 변하는지 계산하는 것이 중요합니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;line-height:2;font-family:'JetBrains Mono',monospace;font-size:13px;overflow-x:auto;">

Output Size Formula

Output = ((W - K + 2P) / S) + 1

W : Input Size
K : Kernel Size
P : Padding
S : Stride

  </div>

  <div style="margin-top:18px;background:white;border:1.5px solid #e9d5ff;border-radius:14px;padding:18px;">
    <div style="font-size:15px;font-weight:800;color:#0f172a;margin-bottom:12px;">
      예제 계산
    </div>
    <div style="font-size:14px;color:#334155;line-height:2;">
      Input Size = 28 × 28<br>
      Kernel Size = 3 × 3<br>
      Padding = 0<br>
      Stride = 1
    </div>
    <div style="margin-top:12px;background:#faf5ff;border-radius:10px;padding:12px;font-family:'JetBrains Mono',monospace;font-size:13px;color:#4c1d95;line-height:1.8;">
      Output
      = ((28 - 3 + 0) / 1) + 1
      = 26
    </div>
    <div style="margin-top:10px;font-size:14px;color:#334155;">
      따라서 출력 Feature Map의 크기는
      <strong style="color:#7c3aed;">26 × 26</strong>
      이 됩니다.
    </div>

  </div>

  <div style="margin-top:18px;background:white;border:1.5px solid #e9d5ff;border-radius:14px;padding:18px;">
    <div style="font-size:15px;font-weight:800;color:#0f172a;margin-bottom:12px;">
      Output Size에 영향을 주는 요소
    </div>
    <div style="font-size:14px;color:#334155;line-height:2;">
      <strong style="color:#7c3aed;">Kernel 크기 증가</strong><br>
      → 한 번에 보는 영역이 커짐<br>
      → Output Size 감소
      <br><br>
      <strong style="color:#7c3aed;">Padding 증가</strong><br>
      → 이미지 주변에 공간 추가<br>
      → Output Size 증가
      <br><br>
      <strong style="color:#7c3aed;">Stride 증가</strong><br>
      → Kernel이 더 크게 이동<br>
      → Output Size 감소
    </div>

  </div>

  <div style="margin-top:18px;background:#ede9fe;border:2px solid #c4b5fd;border-radius:14px;padding:14px 16px;">
    <div style="font-size:13px;font-weight:700;color:#0f172a;line-height:1.8;">
      💡 핵심<br>
      Output Size는 Kernel, Padding, Stride에 의해 결정됩니다.<br>
      CNN을 설계할 때 각 레이어의 출력 크기를 계산하는 것은 매우 중요합니다.
    </div>
  </div>

</div>