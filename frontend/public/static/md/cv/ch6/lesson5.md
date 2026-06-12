<div style="background:#ecfdf5;border:2px solid #86efac;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">📉</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        MaxPool — 중요한 특징만 남기기
      </div>
      <div style="font-size:14px;color:#64748b;">
        CNN에서 Feature Map 크기를 줄이는 가장 대표적인 방법입니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1px solid #bbf7d0;border-radius:14px;padding:18px;color:#334155;line-height:2;">
    CNN은 Layer가 깊어질수록 Feature Map 개수가 많아지고
    연산량도 빠르게 증가합니다.
    <br><br>
    따라서 어느 시점에서는 Feature Map 크기를 줄여야 합니다.
    <br><br>
    이때 사용하는 방법이 MaxPooling입니다.
    <br><br>
    MaxPool은 작은 영역 안에서
    가장 큰 값(Max Value) 하나만 선택합니다.
    <br><br>
    예를 들어
    2×2 영역이
    <br><br>
    1 3<br>
    2 5
    <br><br>
    라면 결과는 5가 됩니다.
    <br><br>
    즉 특징이 가장 강하게 나타난 부분만 유지하고
    나머지 정보는 제거합니다.
    <br><br>
    이를 통해
    연산량 감소
    <br>
    메모리 사용 감소
    <br>
    과적합 감소
    <br>
    위치 변화에 대한 강인성 증가

    효과를 얻을 수 있습니다.

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;">
224 × 224<br>

↓<br>

MaxPool(2×2)<br>

↓<br>

112 × 112
  </div>

  <div style="margin-top:18px;background:#dcfce7;border:2px solid #86efac;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    MaxPool은 Feature Map의 크기를 줄이면서 가장 중요한 특징만 남기는 다운샘플링 기법입니다.
  </div>

</div>