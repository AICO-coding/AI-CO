<div style="background:#fef2f2;border:2px solid #fca5a5;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🎯</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        FC Layer — Fully Connected Layer
      </div>
      <div style="font-size:14px;color:#64748b;">
        추출된 특징을 이용해 최종 판단을 수행하는 레이어입니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #fecaca;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      Convolution Layer의 역할은 특징을 찾는 것입니다.
    </div>
    <div>
      하지만 특징만 찾았다고 해서 분류가 끝나는 것은 아닙니다.
    </div>
    <div>
      이제 CNN은 이 특징들을 보고
      "이 이미지가 무엇인지" 판단해야 합니다.
    </div>
    <div>
      이 역할을 수행하는 것이 FC Layer입니다.
    </div>
    <div>
      FC는 Fully Connected의 약자로
      모든 노드가 서로 연결되어 있다는 의미입니다.
    </div>
    <div>
      FC Layer는 여러 특징들을 종합하여
      각 클래스에 대한 점수(Score)를 계산합니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

<pre style="margin:0;color:#cbd5e1;font-family:monospace;line-height:1.9;">
귀 특징 발견

눈 특징 발견

수염 특징 발견

↓

FC Layer

↓

Cat Score = 9.8
Dog Score = 1.2
Rabbit Score = 0.4
</pre>

  </div>

  <div style="margin-top:18px;background:white;border:1.5px solid #fecaca;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      FC Layer는 지금까지 추출된 특징을 종합하여
      어떤 클래스일 가능성이 높은지 계산합니다.
    </div>
    <div>
      이 점수들은 다음 단계인 Softmax와 Prediction에 사용됩니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#fee2e2;border:2px solid #fca5a5;border-radius:14px;padding:14px;">
    💡 핵심<br>
    FC Layer는 추출된 특징을 바탕으로 클래스별 점수를 계산한다.
  </div>

</div>