<div style="background:#f8fafc;border:2px solid #d8b4fe;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;gap:12px;align-items:center;margin-bottom:20px;">
<div style="font-size:30px;">💻</div>
<div>
<div style="font-size:22px;font-weight:900;color:#6b21a8;">
실습 : Classifier 만들기
</div>
<div style="font-size:14px;color:#64748b;">
Fully Connected Layer 구성
</div>
</div>
</div>

<div style="background:white;padding:20px;border-radius:14px;color:#334155;line-height:2;">
<p>
첫 번째 Linear Layer가 Feature Vector를 입력받습니다.
</p>

<p>
중간 ReLU가 비선형성을 추가합니다.
</p>

<p>
마지막 Linear Layer는 각 클래스의 점수를 출력합니다.
</p>
</div>

<div style="margin-top:18px;background:#0f172a;color:#e2e8f0;padding:20px;border-radius:14px;font-family:monospace;white-space:pre;line-height:1.7;">
import torch.nn as nn

classifier = nn.Sequential(

    nn.Linear(512, 512),
    nn.ReLU(),

    nn.Linear(512, 10)

)
</div>

<div style="margin-top:18px;background:#ede9fe;border:2px solid #a78bfa;border-radius:14px;padding:14px;">
💡 핵심<br>
Classifier는 Feature를 최종 클래스 점수로 변환한다.
</div>

</div>