<div style="background:#fff7ed;border:2px solid #fed7aa;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🧱</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Padding — 가장자리 정보 보존
      </div>
      <div style="font-size:14px;color:#64748b;">
        이미지 외곽에 값을 추가하여 정보 손실을 줄입니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #ffedd5;border-radius:14px;padding:18px;font-size:14px;line-height:2;color:#334155;">
    <div>
      Convolution을 여러 번 수행하면
      이미지 크기는 점점 작아집니다.
    </div>
    <div>
      특히 가장자리 픽셀은 Kernel이 충분히 덮지 못하기 때문에
      중요한 정보가 사라질 수 있습니다.
    </div>
    <div>
      이를 해결하기 위해 이미지 바깥쪽에
      0을 추가하는 기법을 Padding이라고 합니다.
    </div>
    <div>
      Padding을 사용하면 출력 크기를 유지하거나
      가장자리 특징을 더 잘 학습할 수 있습니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;">
Original

[1 2]
[3 4]

Padding = 1

[0 0 0 0]
[0 1 2 0]
[0 3 4 0]
[0 0 0 0]
  </div>

  <div style="margin-top:18px;background:#fff3eb;border:2px solid #ffd0b0;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    Padding은 가장자리 정보를 보호하고 출력 크기를 조절합니다.
  </div>

</div>