<div style="background:#ecfeff;border:2px solid #a5f3fc;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🗺️</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Feature Map — 특징만 남긴 결과
      </div>
      <div style="font-size:14px;color:#64748b;">
        Convolution 연산의 출력 결과입니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #bae6fd;border-radius:14px;padding:18px;font-size:14px;line-height:2;color:#334155;">
    <div>
      Kernel이 이미지를 스캔하면 각 위치에서 계산된 결과값들이 생성됩니다.
    </div>
    <div>
      이 결과값들을 모아 만든 새로운 이미지를
      <strong style="color:#0891b2;">Feature Map</strong>
      이라고 합니다.
    </div>
    <div>
      Feature Map은 원본 이미지 전체를 저장하는 것이 아니라
      Kernel이 발견한 특징만 강조해서 표현합니다.
    </div>
    <div>
      하나의 Kernel은 하나의 Feature Map을 생성하며,
      여러 개의 Kernel을 사용하면 여러 개의 Feature Map이 만들어집니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

<pre style="margin:0;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.9;">
Input Image
      ↓
Convolution
      ↓
Feature Map 1 (Edge)

Feature Map 2 (Vertical)

Feature Map 3 (Texture)
</pre>

  </div>

  <div style="margin-top:18px;background:#cffafe;border:2px solid #67e8f9;border-radius:14px;padding:14px 16px;">
    <div style="font-size:13px;font-weight:700;color:#0f172a;line-height:1.8;">
      💡 핵심<br>
      Feature Map은 CNN이 추출한 특징 정보를 담고 있는 새로운 이미지입니다.<br>
      Kernel 하나당 Feature Map 하나가 생성됩니다.
    </div>
  </div>

</div>