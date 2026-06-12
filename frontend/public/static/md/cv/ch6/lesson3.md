<div style="background:#fefce8;border:2px solid #fde047;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🧱</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Padding 유지 — 왜 가장자리에 0을 추가할까?
      </div>
      <div style="font-size:14px;color:#64748b;">
        CNN에서 Feature Map 크기를 유지하기 위한 핵심 기법입니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1px solid #fde68a;border-radius:14px;padding:18px;color:#334155;line-height:2;">
    Convolution을 수행하면 Feature Map 크기는 점점 작아집니다.
    <br><br>
    예를 들어
    224×224 이미지에
    3×3 Kernel을 적용하면
    출력은 222×222가 됩니다.
    <br><br>
    이런 과정이 여러 번 반복되면
    Feature Map이 너무 빠르게 줄어들어
    중요한 정보가 사라질 수 있습니다.
    <br><br>
    이를 해결하기 위해 입력 이미지의 가장자리에
    0을 추가하는 Padding을 사용합니다.
    <br><br>
    특히 CNN에서는
    Kernel Size가 3×3일 때
    Padding=1을 사용하는 경우가 가장 많습니다.
    <br><br>
    이 설정을 사용하면
    입력 크기와 출력 크기가 동일하게 유지됩니다.

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;">
Input
224 × 224<br>

↓<br>

3×3 Conv
Padding = 1<br>

↓<br>

224 × 224
  </div>

  <div style="margin-top:18px;background:#fef9c3;border:2px solid #fde047;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    3×3 Kernel에서는 Padding=1을 사용하면 출력 크기를 유지할 수 있습니다.
  </div>

</div>