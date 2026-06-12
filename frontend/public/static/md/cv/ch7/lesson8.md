<div style="background:#f8fafc;border:2px solid #bbf7d0;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;gap:12px;align-items:center;margin-bottom:20px;">
<div style="font-size:30px;">💻</div>
<div>
<div style="font-size:22px;font-weight:900;color:#166534;">
실습 : Accuracy 계산
</div>
<div style="font-size:14px;color:#64748b;">
예측 결과 분석하기
</div>
</div>
</div>

<div style="background:white;padding:20px;border-radius:14px;color:#334155;line-height:2;">

<p>
torch.max()는 가장 큰 점수를 가진 클래스를 선택합니다.
</p>

<p>
predicted와 labels가 같은지 비교하여
정답 개수를 계산합니다.
</p>

<p>
최종적으로 정답 수를 전체 데이터 수로 나누어 Accuracy를 구합니다.
</p>

</div>

<div style="margin-top:18px;background:#0f172a;color:#e2e8f0;border-radius:14px;padding:20px;font-family:monospace;white-space:pre;line-height:1.7;">
_, predicted = torch.max(outputs, 1)

correct += (predicted == labels).sum().item()

total += labels.size(0)

accuracy = 100 * correct / total
</div>

<div style="margin-top:18px;background:#dcfce7;border:2px solid #4ade80;border-radius:14px;padding:14px;">
💡 핵심<br>
정답 개수 ÷ 전체 개수로 Accuracy를 계산한다.
</div>

</div>