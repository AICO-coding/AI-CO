<div style="background:#fef2f2;border:2px solid #fca5a5;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">🎯</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
FC Layer 코드 따라해보기
</div>
<div style="font-size:14px;color:#64748b;">
Fully Connected Layer를 생성해봅시다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #fecaca;border-radius:14px;padding:18px;line-height:2;color:#334155;">

FC Layer는 추출된 특징을 이용하여 최종 클래스를 분류합니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

<pre style="margin:0;color:#cbd5e1;font-family:'JetBrains Mono',monospace;line-height:1.9;">
import torch.nn as nn

fc = nn.Linear(1568, 10)

print(fc)
</pre>

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

<pre style="margin:0;color:#cbd5e1;font-family:'JetBrains Mono',monospace;">
Linear(
  in_features=1568,
  out_features=10
)
</pre>

</div>

<div style="margin-top:18px;background:#fee2e2;border:2px solid #fca5a5;border-radius:14px;padding:14px;">
💡 핵심<br>
nn.Linear는 FC Layer를 생성하며 최종 분류를 수행한다.
</div>

</div>