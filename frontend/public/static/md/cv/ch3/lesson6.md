<div style="background:#faf5ff;border:2px solid #d8b4fe;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">📄</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
Flatten 코드 따라해보기
</div>
<div style="font-size:14px;color:#64748b;">
Feature Map을 FC Layer 입력 형태로 변환해봅시다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #e9d5ff;border-radius:14px;padding:18px;line-height:2;color:#334155;">

Flatten은 데이터를 변경하지 않고 Shape만 변경합니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

<pre style="margin:0;color:#cbd5e1;font-family:'JetBrains Mono',monospace;line-height:1.9;">
import torch

x = torch.randn(32, 7, 7)

y = x.flatten()

print(y.shape)
</pre>

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

<pre style="margin:0;color:#cbd5e1;font-family:'JetBrains Mono',monospace;">
torch.Size([1568])
</pre>

</div>

<div style="margin-top:18px;background:#f3e8ff;border:2px solid #d8b4fe;border-radius:14px;padding:14px;">
💡 핵심<br>
Flatten은 Shape만 변경하며 Feature Map을 1차원으로 만든다.
</div>

</div>