<div style="background:#f5f3ff;border:2px solid #c4b5fd;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">🎯</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
CrossEntropyLoss — 분류 문제의 대표 Loss
</div>
<div style="font-size:14px;color:#64748b;">
정답 클래스와 예측 확률을 비교합니다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #ddd6fe;border-radius:14px;padding:18px;font-size:14px;line-height:2;color:#334155;">

CNN 분류 문제에서는
대부분 CrossEntropyLoss를 사용합니다.

모델은 각 클래스에 대한 점수(Logits)를 출력합니다.

CrossEntropyLoss는 이 점수와 실제 정답 클래스를 비교하여
얼마나 틀렸는지 계산합니다.

정답 클래스의 확률이 높을수록 Loss는 작아집니다.

반대로 정답 클래스의 확률이 낮으면
Loss는 크게 증가합니다.

이미지 분류, 객체 분류 등 대부분의 CNN 분류 문제에서 사용됩니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;white-space:pre;">
Output = [2.3, 0.1, 1.0]

Target = 0

정답 클래스 점수 ↑
Loss ↓
</div>

<div style="margin-top:18px;background:#ede9fe;border:2px solid #c4b5fd;border-radius:14px;padding:14px;">
💡 핵심:<br>
CrossEntropyLoss는 분류 문제에서 가장 많이 사용하는 손실 함수입니다.
</div>

</div>