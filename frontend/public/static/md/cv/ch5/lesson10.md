<div style="background:#f5f3ff;border:2px solid #c4b5fd;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">📈</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        왜 VGG는 Channel 수를 계속 늘릴까?
      </div>
      <div style="font-size:14px;color:#64748b;">
        공간 정보는 줄이고 특징 정보는 늘리는 전략
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #ddd6fe;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      CNN에서는 Layer가 깊어질수록
      Feature Map의 가로·세로 크기(Width, Height)는 점점 작아집니다.
    </div>
    <div>
      대신 Channel 수는 계속 증가합니다.
    </div>
    <div>
      이는 CNN이 학습하는 특징의 종류가
      점점 많아지기 때문입니다.
    </div>
    <div>
      초기 Layer에서는
      단순한 Edge, Corner, Line 등을 학습합니다.
    </div>
    <div>
      하지만 깊은 Layer에서는
      눈, 코, 바퀴, 창문, 동물의 귀처럼
      훨씬 복잡한 특징을 학습해야 합니다.
    </div>
    <div>
      더 다양한 특징을 저장하려면
      더 많은 Channel이 필요합니다.
    </div>
    <div>
      따라서 CNN은
      Feature Map 크기를 줄이는 대신
      Channel 수를 증가시킵니다.
    </div>
    <div>
      이것은 정보를 버리는 것이 아니라
      정보를 압축하면서 더 풍부하게 표현하는 과정입니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;white-space:pre;">
Input
224 × 224 × 3

↓

112 × 112 × 64

↓

56 × 56 × 128

↓

28 × 28 × 256

↓

14 × 14 × 512

↓

7 × 7 × 512
  </div>

  <div style="margin-top:18px;background:#ede9fe;border:2px solid #c4b5fd;border-radius:14px;padding:16px;">
    <b>무슨 의미일까?</b><br><br>

    Width ↓<br>
    Height ↓<br>
    <br>
    대신<br><br>
    Feature 종류 ↑<br>
    표현력 ↑<br>
    추상화 수준 ↑

  </div>

  <div style="margin-top:18px;background:#ddd6fe;border:2px solid #a78bfa;border-radius:14px;padding:16px;">
    <b>VGG16의 Channel 변화</b><br><br>

    3 → 64 → 128 → 256 → 512 → 512
    <br><br>

    Layer가 깊어질수록
    더 많은 특징을 저장할 수 있게 됩니다.

  </div>

  <div style="margin-top:18px;background:#c4b5fd;border:2px solid #8b5cf6;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    CNN은 공간 크기(Width, Height)는 줄이고
    특징의 종류(Channel)는 늘려
    더 풍부한 정보를 학습합니다.
  </div>

</div>