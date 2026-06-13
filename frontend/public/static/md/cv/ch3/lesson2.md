<div style="background:#f0fdf4;border:2px solid #bbf7d0;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

<div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
<div style="font-size:30px;">⚙️</div>
<div>
<div style="font-size:20px;font-weight:900;color:#0f172a;">
Conv → ReLU → Pool
</div>
<div style="font-size:14px;color:#64748b;">
CNN이 특징을 학습하는 기본 구조입니다.
</div>
</div>
</div>

<div style="background:white;border-radius:14px;padding:18px;border:1.5px solid #bbf7d0;color:#334155;line-height:2;">

<div>
CNN은 보통 Convolution, ReLU, Pooling을 하나의 묶음처럼 반복합니다.
</div>

<div>
각 단계는 서로 다른 역할을 수행합니다.
</div>

<div>
<strong>① Convolution</strong><br>
Kernel을 사용하여 이미지 속 특징을 찾습니다.
</div>

<div>
<strong>② ReLU</strong><br>
음수 값을 제거하여 중요한 특징만 남깁니다.
</div>

<div>
<strong>③ Pooling</strong><br>
Feature Map의 크기를 줄여 계산량을 감소시킵니다.
</div>

<div>
이 과정을 여러 번 반복하면 CNN은 점점 복잡한 특징을 학습할 수 있습니다.
</div>

</div>

<div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;">

<pre style="margin:0;color:#cbd5e1;font-family:monospace;">
Input

↓ Convolution

Feature 추출

↓ ReLU

중요한 정보만 유지

↓ Pooling

크기 축소

↓ 다음 Layer
</pre>

</div>

<div style="margin-top:18px;background:#dcfce7;border:2px solid #86efac;border-radius:14px;padding:14px;">
💡 핵심<br>
CNN은 Conv → ReLU → Pool 구조를 반복하면서
점점 더 의미 있는 특징을 학습한다.
</div>

</div>