<div style="background:#fff7ed;border:2px solid #fdba74;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">⚡</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
ReLU 코드 따라해보기
</div>
<div style="font-size:14px;color:#64748b;">
가장 많이 사용하는 Activation Function을 직접 실행해봅시다.
</div>
</div>
</div>

<div style="background:white;border:1.5px solid #fed7aa;border-radius:14px;padding:18px;line-height:2;color:#334155;">

ReLU는 음수를 제거하고 양수만 남기는 함수입니다.
CNN에서는 거의 모든 Layer 뒤에 사용됩니다.

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

<pre style="margin:0;color:#cbd5e1;font-family:'JetBrains Mono',monospace;line-height:1.9;">
import torch
import torch.nn.functional as F

x = torch.tensor([-3., 5., -1., 8.])

y = F.relu(x)

print(y)
</pre>

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

<pre style="margin:0;color:#cbd5e1;font-family:'JetBrains Mono',monospace;">
tensor([0., 5., 0., 8.])
</pre>

</div>

<div style="margin-top:18px;background:#ffedd5;border:2px solid #fdba74;border-radius:14px;padding:14px;">
💡 핵심<br>
ReLU는 음수를 제거하여 중요한 특징만 남긴다.
</div>

</div>