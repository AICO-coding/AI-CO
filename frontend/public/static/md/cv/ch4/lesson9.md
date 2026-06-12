<div style="background:#fef2f2;border:2px solid #fca5a5;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">🔙</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
Backward — 틀린 이유를 계산하는 과정
</div>
<div style="font-size:14px;color:#64748b;">
Gradient를 계산하여 학습 방향을 찾습니다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #fecaca;border-radius:14px;padding:18px;font-size:14px;line-height:2;color:#334155;">

Loss가 계산되면

"어떤 Weight가 문제였는가?"

를 알아야 합니다.

Backward는 Loss를 기준으로
모든 Weight에 대한 Gradient를 계산합니다.

Gradient는

"어느 방향으로 이동해야 Loss가 줄어드는가"

를 나타냅니다.

Optimizer는 이 Gradient를 이용하여
Weight를 업데이트합니다.

즉

Forward는 결과를 만들고

Backward는 수정 방향을 찾습니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;white-space:pre;">
Forward
   ↓
Loss
   ↓
Backward
   ↓
Gradient 생성
</div>

<div style="margin-top:18px;background:#fee2e2;border:2px solid #fca5a5;border-radius:14px;padding:14px;">
💡 핵심:<br>
Backward는 Loss를 줄이기 위한 Gradient를 계산합니다.
</div>

</div>