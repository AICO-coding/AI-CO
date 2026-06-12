<div style="background:#f0f9ff;border:2px solid #7dd3fc;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🏆</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Prediction — 최종 예측
      </div>
      <div style="font-size:14px;color:#64748b;">
        CNN이 가장 가능성이 높은 클래스를 선택하는 단계입니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #bae6fd;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      FC Layer는 클래스별 점수(Score)를 계산합니다.
    </div>
    <div>
      하지만 점수만 보고서는 확률을 알기 어렵습니다.
    </div>
    <div>
      그래서 보통 Softmax 함수를 사용하여
      점수를 확률로 변환합니다.
    </div>
    <div>
      확률의 총합은 항상 100%가 됩니다.
    </div>
    <div>
      CNN은 가장 높은 확률을 가진 클래스를
      최종 결과로 선택합니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

<pre style="margin:0;color:#cbd5e1;font-family:monospace;line-height:1.9;">
Cat     → 97%

Dog     → 2%

Rabbit  → 1%

↓

Prediction

Cat
</pre>

  </div>

  <div style="margin-top:18px;background:white;border:1.5px solid #bae6fd;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      위 예시에서는 Cat의 확률이 가장 높습니다.
    </div>
    <div>
      따라서 CNN은 이 이미지를 고양이로 예측합니다.
    </div>
    <div>
      실제 이미지 분류 모델들은 수백 개 또는 수천 개의 클래스 중에서
      가장 높은 확률을 가진 클래스를 선택합니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #93c5fd;border-radius:14px;padding:14px;">
    💡 핵심<br>
    Prediction은 가장 높은 확률을 가진 클래스를 선택하는 단계이다.<br>
    CNN의 최종 출력 결과이다.
  </div>

</div>