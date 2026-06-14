<style>
:root {
  --or:#FF6B00;--or2:#E55A00;--orL:#FFF0E6;--orB:#FFDCC2;
  --gr:#3EC934;--gr2:#2DAA24;--grL:#E8FFE6;--grB:#C2F0BE;
  --pu:#A855F7;--puL:#F5EEFF;--puB:#DBBEFF;--pu2:#8B3FD9;
  --bl:#185FA5;--blL:#E6F1FB;--blB:#B5D4F4;
  --te:#0F6E56;--teL:#E1F5EE;--teB:#9FE1CB;
  --gy:#F5F5F5;--gy2:#EBEBEB;--gy3:#D0D0D0;--gy4:#9A9A9A;--gy5:#5A5A5A;
  --dk:#1A1A2E;--ff:'Nunito',sans-serif;--fm:'JetBrains Mono',monospace;
  --r8:8px;--r12:12px;--r16:16px;
}
.md-wrap { font-family:var(--ff); color:var(--dk); padding:16px; }
.m-header { margin-bottom:16px; padding-bottom:14px; border-bottom:2px solid var(--gy2); }
.m-title  { font-size:15px; font-weight:900; color:var(--dk); margin-bottom:5px; }
.m-sub    { font-size:12px; color:var(--gy4); font-weight:600; line-height:1.6; }
.ml-sec {
  font-size:10px; font-weight:800; color:var(--gy4);
  letter-spacing:.08em; text-transform:uppercase;
  margin:14px 0 8px; padding-bottom:4px; border-bottom:1px solid var(--gy2);
}
.obj-list { display:flex; flex-direction:column; gap:6px; margin-bottom:4px; }
.obj-item { display:flex; align-items:flex-start; gap:8px; font-size:12px; color:var(--gy5); line-height:1.5; }
.obj-n    { width:20px; height:20px; min-width:20px; border-radius:50%;
  background:var(--orL); border:2px solid var(--orB);
  display:flex; align-items:center; justify-content:center;
  font-size:10px; font-weight:800; color:var(--or); margin-top:1px; }
.feat-box  { background:var(--gy); border-radius:var(--r8); padding:8px 10px; }
.feat-row  { display:flex; align-items:center; justify-content:space-between;
  padding:5px 0; border-bottom:1px solid var(--gy2); font-size:12px; }
.feat-row:last-child { border:none; }
.feat-name { font-weight:800; color:var(--dk); font-family:var(--fm); font-size:11px; }
.feat-star { color:var(--or); }
.feat-desc { color:var(--gy4); font-weight:600; font-size:11px; }
.todo-list { display:flex; flex-direction:column; gap:6px; }
.todo-card { border-radius:var(--r8); border:2px solid var(--gy2); overflow:hidden; }
.todo-head { display:flex; align-items:center; gap:7px; padding:7px 10px; background:var(--gy); }
.todo-n    { width:20px; height:20px; min-width:20px; border-radius:50%;
  background:var(--orL); border:2px solid var(--orB);
  display:flex; align-items:center; justify-content:center;
  font-size:10px; font-weight:800; color:var(--or); }
.todo-ctag { font-size:10px; font-weight:800; padding:2px 7px; border-radius:20px; border:1px solid; }
.ctag-ch1  { background:#F1EFE8; color:#5F5E5A; border-color:#D3D1C7; }
.ctag-pre  { background:var(--teL); color:var(--te); border-color:var(--teB); }
.ctag-ch3  { background:var(--puL); color:var(--pu2); border-color:var(--puB); }
.ctag-ch4  { background:var(--blL); color:var(--bl); border-color:var(--blB); }
.ctag-ch5  { background:var(--grL); color:var(--gr2); border-color:var(--grB); }
.todo-title { font-size:12px; font-weight:800; color:var(--dk); flex:1; }
.todo-body  { padding:8px 10px; font-size:11px; color:var(--gy5);
  line-height:1.6; border-top:1px solid var(--gy2); background:#fff; }
.hint-box { margin-top:6px; padding:5px 8px; border-radius:6px;
  background:var(--orL); border:1px solid var(--orB);
  font-size:11px; color:var(--or2); font-weight:700; }
.formula-box { background:var(--dk); color:#E2E8F0; border-radius:var(--r8);
  padding:12px 14px; font-family:var(--fm); font-size:12px; line-height:1.9; }
.shape-flow { display:flex; align-items:center; gap:6px; flex-wrap:wrap; margin-top:8px; }
.shape-node { background:var(--blL); border:1px solid var(--blB); border-radius:6px;
  padding:4px 8px; font-family:var(--fm); font-size:11px; font-weight:800; color:var(--bl); }
.shape-arr { color:var(--gy3); font-size:13px; font-weight:800; }
.acc-wrap { margin-top:14px; }
.acc-labels { display:flex; justify-content:space-between; font-size:11px; margin-bottom:5px; }
.acc-lbl { font-weight:800; color:var(--gy4); }
.acc-val { font-family:var(--fm); font-weight:800; color:var(--gr); }
.acc-bar  { background:var(--gy2); border-radius:20px; height:9px; overflow:hidden; }
.acc-fill { height:100%; border-radius:20px; background:var(--gr); width:0%; transition:width .6s; }
.acc-goal { font-size:10px; color:var(--gy4); margin-top:3px; }
</style>

<div class="md-wrap">

<div class="m-header">
  <div class="m-title">타이타닉 생존자 예측 미션</div>
  <div class="m-sub">타이타닉 승객 정보를 바탕으로 생존 여부를 예측하는 이진 분류 모델을 구현합니다.<br>결측치 처리 → 범주형 인코딩 → 정규화 → Dataset/DataLoader → MLP 분류 모델 → 학습/평가까지, Ch1~Ch8 Classification의 전체 흐름을 체험하세요.</div>
</div>

<div class="ml-sec">학습 목표</div>
<div class="obj-list">
  <div class="obj-item"><div class="obj-n">①</div><span>분류 문제에서 입력 특성 X와 정답 라벨 y를 구분하기</span></div>
  <div class="obj-item"><div class="obj-n">②</div><span>Age, Embarked 같은 결측치를 적절한 값으로 채우기</span></div>
  <div class="obj-item"><div class="obj-n">③</div><span>Sex, Embarked 같은 범주형 데이터를 숫자로 인코딩하기</span></div>
  <div class="obj-item"><div class="obj-n">④</div><span>Dataset/DataLoader로 배치 학습 데이터 구성하기</span></div>
  <div class="obj-item"><div class="obj-n">⑤</div><span>MLP 분류 모델과 CrossEntropyLoss로 생존 여부 학습하기</span></div>
  <div class="obj-item"><div class="obj-n">⑥</div><span>Accuracy로 이진 분류 모델 성능 평가하기</span></div>
</div>

<div class="ml-sec">데이터셋 & 문제 정의</div>
<div class="feat-box">
  <div class="feat-row"><span class="feat-name">데이터</span><span class="feat-desc">Titanic passenger data</span></div>
  <div class="feat-row"><span class="feat-name">입력 특성 <span class="feat-star">★</span></span><span class="feat-desc">Pclass, Sex, Age, SibSp, Parch, Fare, Embarked</span></div>
  <div class="feat-row"><span class="feat-name">정답 라벨</span><span class="feat-desc">Survived: 0=사망, 1=생존</span></div>
  <div class="feat-row"><span class="feat-name">문제 유형</span><span class="feat-desc">Binary Classification</span></div>
  <div class="feat-row"><span class="feat-name">평가 지표</span><span class="feat-desc">Accuracy</span></div>
</div>

<div class="ml-sec">파이프라인 흐름</div>
<div class="shape-flow">
  <span class="shape-node">승객 정보</span><span class="shape-arr">→</span>
  <span class="shape-node">결측치 처리</span><span class="shape-arr">→</span>
  <span class="shape-node">범주형 인코딩</span><span class="shape-arr">→</span>
  <span class="shape-node">StandardScaler</span><span class="shape-arr">→</span>
  <span class="shape-node">Dataset/DataLoader</span><span class="shape-arr">→</span>
  <span class="shape-node">MLP Classifier</span><span class="shape-arr">→</span>
  <span class="shape-node">생존/사망 예측</span>
</div>

<div class="ml-sec">TODO 가이드라인</div>
<div class="todo-list">
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">1</div><span class="todo-ctag ctag-ch1">Ch1</span><span class="todo-title">입력 특성과 라벨 분리</span></div>
    <div class="todo-body">Survived는 정답 라벨이고, 나머지 선택된 승객 정보는 모델 입력으로 사용합니다.<div class="hint-box">💡 X=feature columns · y=Survived</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">2</div><span class="todo-ctag ctag-pre">전처리</span><span class="todo-title">결측치 처리</span></div>
    <div class="todo-body">Age는 중앙값, Embarked는 최빈값으로 채워 데이터 손실을 줄입니다.<div class="hint-box">💡 fillna() · median() · mode()[0]</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">3</div><span class="todo-ctag ctag-pre">전처리</span><span class="todo-title">범주형 인코딩</span></div>
    <div class="todo-body">문자열인 Sex, Embarked는 신경망에 바로 넣을 수 없으므로 숫자 값으로 변환합니다.<div class="hint-box">💡 map({'male':0, 'female':1}) · pd.get_dummies()</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">4</div><span class="todo-ctag ctag-pre">전처리</span><span class="todo-title">정규화와 train/test 분할</span></div>
    <div class="todo-body">특성별 스케일 차이를 줄이기 위해 StandardScaler를 사용하고, 학습/평가 데이터를 분리합니다.<div class="hint-box">💡 train_test_split · scaler.fit_transform(train) · scaler.transform(test)</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">5</div><span class="todo-ctag ctag-ch3">Ch3</span><span class="todo-title">Dataset/DataLoader 구현</span></div>
    <div class="todo-body">입력 X와 라벨 y를 묶어 PyTorch Dataset으로 만들고, DataLoader로 배치 단위 학습을 준비합니다.<div class="hint-box">💡 __len__ · __getitem__ · batch_size=32 · train shuffle=True</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">6</div><span class="todo-ctag ctag-ch4">Ch4</span><span class="todo-title">MLP 분류 모델 구성</span></div>
    <div class="todo-body">입력 특성 수에서 시작해 hidden layer를 거쳐 2개 클래스의 logit을 출력합니다.<div class="hint-box">💡 Linear(input_dim, 64) → ReLU → Dropout → Linear(32, 2)</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">7</div><span class="todo-ctag ctag-ch4">Ch4</span><span class="todo-title">손실함수와 옵티마이저</span></div>
    <div class="todo-body">분류 문제에는 CrossEntropyLoss를 사용합니다. 모델 출력은 Softmax 전의 logit이어야 합니다.<div class="hint-box">💡 CrossEntropyLoss · Adam</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">8</div><span class="todo-ctag ctag-ch5">Ch5</span><span class="todo-title">학습 루프와 평가</span></div>
    <div class="todo-body">train/eval 모드를 구분하고, argmax로 예측 클래스를 구해 Accuracy를 계산합니다.<div class="hint-box">💡 model.train() · opt.zero_grad() · loss.backward() · model.eval() · torch.no_grad()</div></div>
  </div>
</div>

<div class="ml-sec">핵심 공식</div>
<div class="formula-box">
  Classification output = logits for each class<br>
  CrossEntropyLoss = Softmax + Negative Log Likelihood<br>
  Prediction = argmax(logits, dim=1)<br>
  Accuracy = 맞춘 개수 / 전체 개수 × 100
</div>

<div class="acc-wrap">
  <div class="acc-labels">
    <span class="acc-lbl">Test Accuracy 달성도</span>
    <span class="acc-val" id="accDisp">0.0%</span>
  </div>
  <div class="acc-bar"><div class="acc-fill" id="accFill"></div></div>
  <div class="acc-goal">목표: Test Accuracy ≥ 75%</div>
</div>

</div>