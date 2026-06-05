<div style="background:#ecfeff;border:2px solid #a5f3fc;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🧠</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#082f49;">
        Tensor Shape — 딥러닝용 구조
      </div>
      <div style="font-size:14px;color:#64748b;margin-top:4px;">
        딥러닝은 이미지를 숫자 배열(Tensor)로 처리해요.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #bae6fd;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      예시 shape:
      <strong style="color:#0284c7;">(3, 224, 224)</strong>
    </div>
    <div style="margin-top:10px;padding-left:8px;">
      • 3 → RGB 채널<br>
      • 224 → 높이(Height)<br>
      • 224 → 너비(Width)
    </div>
    <div style="margin-top:10px;">
      모델은 입력 shape이 정해져 있어서
      <strong style="color:#0f172a;">shape이 다르면 에러</strong>가 날 수 있어요.
    </div>

  </div>

  <div style="margin-top:18px;background:#082f49;border-radius:14px;padding:18px;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.9;color:#dbeafe;overflow-x:auto;">
    image tensor<br>
    → (3, 224, 224)

  </div>

  <div style="margin-top:18px;background:#ecfeff;border:2px solid #67e8f9;border-radius:14px;padding:14px 16px;display:flex;gap:10px;align-items:flex-start;">
    <div style="font-size:18px;">⚡</div>
    <div style="font-size:13px;font-weight:700;color:#082f49;line-height:1.7;">
      shape 불일치는 딥러닝 에러의 대표 원인이에요.
    </div>
  </div>
</div>