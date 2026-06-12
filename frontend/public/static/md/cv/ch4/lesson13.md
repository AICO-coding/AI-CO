<div style="background:#fff1f2;border:2px solid #fda4af;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">⚠️</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
Overfitting — 문제를 외워버린 상태
</div>
<div style="font-size:14px;color:#64748b;">
학습 데이터에는 강하지만 새로운 데이터에는 약합니다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #fecdd3;border-radius:14px;padding:18px;font-size:14px;line-height:2;color:#334155;">

모델의 목표는

학습 데이터뿐 아니라

처음 보는 데이터도 잘 맞추는 것입니다.

하지만 모델이 학습 데이터를 너무 많이 외우면
Overfitting이 발생합니다.

이 경우

Training Accuracy는 매우 높지만

Validation Accuracy는 낮아집니다.

즉

공부를 이해한 것이 아니라

답을 암기한 상태와 비슷합니다.

이를 방지하기 위해

• Data Augmentation<br>
• Dropout<br>
• Early Stopping<br>
• Weight Decay

등을 사용합니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;white-space:pre;">
Train Accuracy = 99%

Validation Accuracy = 71%

→ Overfitting
</div>

<div style="margin-top:18px;background:#ffe4e6;border:2px solid #fda4af;border-radius:14px;padding:14px;">
💡 핵심:<br>
Overfitting은 학습 데이터를 지나치게 외워 일반화 성능이 떨어지는 현상입니다.
</div>

</div>