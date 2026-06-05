<div style="background:#f0fdf4;border:2px solid #bbf7d0;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">📦</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#052e16;">
        CHW 구조
      </div>
      <div style="font-size:14px;color:#64748b;margin-top:4px;">
        PyTorch에서 사용하는 표준 이미지 구조예요.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #bbf7d0;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      CHW =
      <strong style="color:#16a34a;">Channel, Height, Width</strong>
    </div>
    <div style="margin-top:10px;">
      예시:
      <strong style="color:#0f172a;">(3, 224, 224)</strong>
    </div>
    <div style="margin-top:10px;padding-left:8px;">
      • 3 → RGB 채널<br>
      • 224 → 높이<br>
      • 224 → 너비
    </div>
    <div style="margin-top:10px;">
      일반 이미지는 보통 HWC 구조지만,<br>
      딥러닝에서는 CHW가 연산 효율이 좋아요.
    </div>

  </div>

  <div style="margin-top:18px;background:#052e16;border-radius:14px;padding:18px;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.9;color:#dcfce7;overflow-x:auto;">
    HWC → (224, 224, 3)<br>
    CHW → (3, 224, 224)

  </div>

  <div style="margin-top:18px;background:#f0fdf4;border:2px solid #86efac;border-radius:14px;padding:14px 16px;display:flex;gap:10px;align-items:flex-start;">
    <div style="font-size:18px;">🚀</div>
    <div style="font-size:13px;font-weight:700;color:#052e16;line-height:1.7;">
      GPU 연산에서는 CHW 구조가 더 효율적이에요.
    </div>

  </div>

</div>