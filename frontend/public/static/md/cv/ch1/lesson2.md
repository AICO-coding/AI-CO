<div style="background:#eef7ff;border:2px solid #c2e4ff;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🎨</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        RGB — 색을 표현하는 방식
      </div>
      <div style="font-size:14px;color:#64748b;margin-top:4px;">
        이미지는 숫자로 색을 저장해요.
      </div>
    </div>
  </div>
  <div style="background:white;border:1.5px solid #dbeafe;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      각 픽셀은
      <strong style="color:#0f172a;">3개의 숫자</strong>로 구성돼요.
    </div>
    <div style="margin-top:8px;padding-left:8px;">
      • R → Red<br>
      • G → Green<br>
      • B → Blue
    </div>
    <div style="margin-top:10px;">
      <strong style="color:#ef4444;">(255, 0, 0)</strong> → 빨간색<br>
      <strong style="color:#22c55e;">(0, 255, 0)</strong> → 초록색<br>
      <strong style="color:#3b82f6;">(0, 0, 255)</strong> → 파란색
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.9;color:#cbd5e1;overflow-x:auto;">
    pixel = (R, G, B)<br>
    pixel = (255, 120, 30)<br><br>
    image.shape → (224, 224, 3)
  </div>

  <div style="margin-top:18px;background:#fff3eb;border:2px solid #ffd0b0;border-radius:14px;padding:14px 16px;display:flex;gap:10px;align-items:flex-start;">
    <div style="font-size:18px;">💡</div>
    <div style="font-size:13px;font-weight:700;color:#0f172a;line-height:1.7;">
      핵심:<br>
      픽셀 1개 = RGB 숫자 3개 묶음
    </div>

  </div>

</div>