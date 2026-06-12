<div style="background:#faf5ff;border:2px solid #c084fc;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;gap:12px;align-items:center;margin-bottom:20px;">
    <div style="font-size:30px;">🎯</div>
    <div>
      <div style="font-size:22px;font-weight:900;color:#6b21a8;">
        Classifier 구현
      </div>
      <div style="font-size:14px;color:#64748b;">
        추출된 특징으로 최종 분류하기
      </div>
    </div>
  </div>

  <div style="background:white;border-radius:14px;padding:20px;color:#334155;line-height:2;">
    <p>
      CNN의 앞부분은 특징을 추출하는 Feature Extractor 역할을 수행합니다.
    </p>
    <p>
      하지만 특징만 추출해서는 어떤 클래스인지 알 수 없습니다.
    </p>
    <p>
      따라서 마지막에는 Fully Connected Layer를 사용하여
      특징 정보를 클래스 점수로 변환합니다.
    </p>
    <p>
      이를 Classifier라고 부릅니다.
    </p>
    <p>
      예를 들어 CIFAR-10 데이터셋에서는
      최종 출력 노드 수가 10개가 됩니다.
    </p>

  </div>

  <div style="margin-top:20px;background:#581c87;color:white;padding:18px;border-radius:14px;font-family:monospace;white-space:pre;">
Feature Vector
       ↓
FC Layer
       ↓
FC Layer
       ↓
10 Class Scores
  </div>

</div>