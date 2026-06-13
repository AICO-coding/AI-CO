<div style="background:#fef2f2;border:2px solid #fca5a5;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;gap:12px;align-items:center;margin-bottom:20px;">
<div style="font-size:30px;">⚠️</div>
<div>
<div style="font-size:22px;font-weight:900;color:#991b1b;">
Overfitting 실험
</div>
<div style="font-size:14px;color:#64748b;">
모델이 암기해버리는 현상
</div>
</div>
</div>

<div style="background:white;padding:20px;border-radius:14px;color:#334155;line-height:2;">

<p>
Overfitting은 모델이 학습 데이터를 지나치게 외워버리는 현상입니다.
</p>

<p>
학습 데이터에서는 매우 높은 성능을 보이지만,
새로운 데이터에서는 성능이 크게 떨어집니다.
</p>

<p>
CNN이 너무 깊거나,
Epoch를 지나치게 많이 학습하거나,
데이터가 부족할 때 자주 발생합니다.
</p>

<p>
Train Accuracy는 계속 증가하지만
Validation Accuracy는 감소하는 것이 대표적인 징후입니다.
</p>

<p>
Dropout, Data Augmentation, Early Stopping 등을 사용하여
Overfitting을 줄일 수 있습니다.
</p>

</div>

<div style="margin-top:20px;background:#0f172a;color:#cbd5e1;border-radius:14px;padding:18px;font-family:monospace;white-space:pre;">
Train Accuracy ↑↑↑

Validation Accuracy ↓
</div>

<div style="margin-top:18px;background:#fee2e2;border:2px solid #ef4444;border-radius:14px;padding:14px;">
💡 핵심<br>
Train 성능만 높고 Test 성능이 낮다면 Overfitting일 가능성이 높다.
</div>

</div>