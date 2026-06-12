

<div style="background:#faf5ff;border:2px solid #d8b4fe;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">📄</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Flatten — 펼치기
      </div>
      <div style="font-size:14px;color:#64748b;">
        Feature Map을 1차원 벡터로 변환하는 과정입니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #e9d5ff;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      CNN의 Convolution Layer와 Pooling Layer를 거치면
      Feature Map이 생성됩니다.
    </div>
    <div>
      Feature Map은 보통
      (채널, 높이, 너비)
      형태의 3차원 데이터입니다.
    </div>
    <div>
      예를 들어 Feature Map의 Shape이
      (32, 7, 7)
      이라고 가정해봅시다.
    </div>
    <div>
      하지만 다음 단계인 FC Layer는
      1차원 형태의 입력만 받을 수 있습니다.
    </div>
    <div>
      따라서 Feature Map을 하나의 긴 벡터로 펼쳐야 합니다.
    </div>
    <div>
      이 과정을 Flatten이라고 합니다.
    </div>
    <div>
      중요한 점은 Flatten은 새로운 특징을 학습하지 않습니다.
    </div>
    <div>
      단순히 데이터의 모양(Shape)만 변경합니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

<pre style="margin:0;color:#cbd5e1;font-family:monospace;line-height:1.9;">
Feature Map

(32, 7, 7)

↓

Flatten

↓

1568
</pre>

  </div>

  <div style="margin-top:18px;background:white;border:1.5px solid #e9d5ff;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">

    <div>
      왜 1568이 될까요?
    </div>

<pre style="margin-top:10px;background:#faf5ff;padding:12px;border-radius:10px;">
32 × 7 × 7

= 1568
</pre>

    <div>
      모든 값을 일렬로 나열하여 하나의 벡터로 만드는 것입니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#f3e8ff;border:2px solid #d8b4fe;border-radius:14px;padding:14px;">
    💡 핵심<br>
    Flatten은 Feature Map의 Shape만 변경한다.<br>
    FC Layer에 입력하기 위해 사용된다.
  </div>

</div>