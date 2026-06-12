<div style="background:#fff7ed;border:2px solid #fdba74;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">📉</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
Loss — 얼마나 틀렸는지 측정하는 값
</div>
<div style="font-size:14px;color:#64748b;">
예측과 정답의 차이를 숫자로 표현합니다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #fed7aa;border-radius:14px;padding:18px;font-size:14px;line-height:2;color:#334155;">

딥러닝 모델은 처음에는 거의 랜덤한 예측을 합니다.

모델이 얼마나 틀렸는지 알기 위해
예측값과 실제 정답을 비교하는 지표가 필요합니다.

이 값을 Loss(손실)라고 부릅니다.

Loss가 크면 예측이 많이 틀렸다는 의미이고,
Loss가 작으면 정답에 가까운 예측을 했다는 의미입니다.

학습의 목표는 Loss를 최소화하는 것입니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;white-space:pre;">
Prediction = 0.95
Target     = 1

Loss ↓ 작음


Prediction = 0.05
Target     = 1

Loss ↑ 큼
</div>

<div style="margin-top:18px;background:#ffedd5;border:2px solid #fdba74;border-radius:14px;padding:14px;">
💡 핵심:<br>
Loss는 모델의 예측이 정답과 얼마나 차이가 나는지 측정하는 값입니다.
</div>

</div>