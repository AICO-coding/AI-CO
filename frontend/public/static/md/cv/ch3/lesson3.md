<div style="background:#fff7ed;border:2px solid #fdba74;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">⚡</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Activation Function — 활성화 함수
      </div>
      <div style="font-size:14px;color:#64748b;">
        신경망이 복잡한 패턴을 학습할 수 있게 만드는 핵심 요소입니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #fed7aa;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      신경망은 기본적으로 덧셈과 곱셈 연산을 수행합니다.
    </div>
    <div>
      하지만 덧셈과 곱셈만 반복하면 아무리 Layer를 많이 쌓아도
      결국 하나의 단순한 수식과 크게 다르지 않습니다.
    </div>
    <div>
      이렇게 되면 고양이와 강아지처럼 복잡한 패턴을 구분하기 어려워집니다.
    </div>
    <div>
      그래서 사용하는 것이
      <strong style="color:#ea580c;">Activation Function</strong>
      입니다.
    </div>
    <div>
      Activation Function은 신경망에
      <strong>비선형성(Non-Linearity)</strong>
      을 추가하여 복잡한 관계를 학습할 수 있도록 도와줍니다.
    </div>
    <div>
      CNN에서 가장 많이 사용하는 Activation Function은 ReLU입니다.
    </div>
    <div>
      ReLU는 양수는 그대로 통과시키고 음수는 0으로 만듭니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

<pre style="margin:0;color:#cbd5e1;font-family:monospace;line-height:1.9;">
ReLU(x)

x > 0 → x

x ≤ 0 → 0
</pre>

  </div>

  <div style="margin-top:18px;background:white;border:1.5px solid #fed7aa;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">

    <div>
      예를 들어 Convolution 결과가 아래와 같다고 가정해봅시다.
    </div>

<pre style="margin-top:10px;background:#fff7ed;padding:12px;border-radius:10px;">
[-3, 5, -1, 8]
</pre>

    <div>
      ReLU를 적용하면
    </div>

<pre style="margin-top:10px;background:#fff7ed;padding:12px;border-radius:10px;">
[0, 5, 0, 8]
</pre>

    <div>
      와 같이 음수가 제거됩니다.
    </div>

    <div>
      이를 통해 중요한 특징은 유지하고 불필요한 정보는 줄일 수 있습니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#ffedd5;border:2px solid #fdba74;border-radius:14px;padding:14px;">
    💡 핵심<br>
    Activation Function은 신경망에 비선형성을 추가한다.<br>
    CNN에서는 ReLU가 가장 많이 사용된다.
  </div>

</div>