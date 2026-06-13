<div style="background:#eff6ff;border:2px solid #bfdbfe;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🏗️</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        왜 CNN을 깊게 쌓을까?
      </div>
      <div style="font-size:14px;color:#64748b;">
        깊은 네트워크는 더 복잡한 특징을 학습할 수 있습니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #dbeafe;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      CNN의 가장 중요한 아이디어 중 하나는
      <strong style="color:#2563eb;">계층적으로 특징을 추출한다</strong>는 것입니다.
    </div>
    <div>
      첫 번째 Convolution Layer는
      단순한 특징을 학습합니다.
    </div>
    <div style="margin-left:12px;">
      • Edge (윤곽선)<br>
      • Corner (모서리)<br>
      • 방향성 패턴
    </div>
    <div>
      두 번째 Layer는
      이전 Layer가 찾은 Edge들을 조합합니다.
    </div>
    <div style="margin-left:12px;">
      • 눈<br>
      • 코<br>
      • 입
    </div>
    <div>
      더 깊은 Layer에서는
      얼굴 전체, 자동차 전체와 같은
      고수준 특징(High-Level Feature)을 학습합니다.
    </div>
    <div>
      즉 CNN은 층이 깊어질수록
      단순한 특징 → 복잡한 특징으로 발전합니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;white-space:pre;">
Input Image
     ↓
Conv 1
(Edge)

     ↓
Conv 2
(Eye)

     ↓
Conv 3
(Face)

     ↓
Prediction
  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #93c5fd;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    CNN을 깊게 쌓는 이유는 더 복잡하고 추상적인 특징을 학습하기 위해서입니다.
  </div>

</div>