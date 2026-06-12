<div style="background:#eff6ff;border:2px solid #93c5fd;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">💻</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
실습 — Accuracy 계산하기
</div>
<div style="font-size:14px;color:#64748b;">
예측 클래스 번호를 구해봅시다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #bfdbfe;border-radius:14px;padding:18px;color:#334155;line-height:2;">

CNN 출력은 클래스별 점수(Logits)입니다.

Accuracy를 계산하기 위해서는
가장 큰 값을 가진 클래스 번호를 찾아야 합니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.8;white-space:pre;">
output = torch.tensor([
    [0.2, 3.5, 1.1]
])

pred = output.{{blank1}}(dim=1)

print(pred)
</div>

<div style="margin-top:18px;background:#dbeafe;border:2px solid #93c5fd;border-radius:14px;padding:14px;">
💡 힌트:<br>
가장 큰 값의 위치를 반환하는 함수입니다.
</div>

</div>