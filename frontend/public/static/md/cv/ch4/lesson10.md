<div style="background:#fef2f2;border:2px solid #fca5a5;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">💻</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
실습 — Backward 수행하기
</div>
<div style="font-size:14px;color:#64748b;">
Gradient를 계산해봅시다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #fecaca;border-radius:14px;padding:18px;color:#334155;line-height:2;">

Loss를 계산한 후에는
모델이 어느 방향으로 수정되어야 하는지 알아야 합니다.

backward() 함수는 모든 Weight에 대한 Gradient를 계산합니다.

Optimizer는 이 Gradient를 사용하여
모델의 Weight를 업데이트합니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.8;white-space:pre;overflow-x:auto;">
loss = criterion(output, target)

loss.backward()
</div>

<div style="margin-top:18px;background:#fee2e2;border:2px solid #fca5a5;border-radius:14px;padding:14px;">
💡 결과:<br>
Gradient가 계산되어 Weight 업데이트 준비가 완료됩니다.
</div>

</div>