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
.ctag-ch23 { background:var(--blL); color:var(--bl); border-color:var(--blB); }
.ctag-ch34 { background:var(--puL); color:var(--pu2); border-color:var(--puB); }
.ctag-ch4  { background:var(--puL); color:var(--pu2); border-color:var(--puB); }
.ctag-ch45 { background:var(--puL); color:var(--pu2); border-color:var(--puB); }
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
  <div class="m-title">CIFAR-10 이미지 분류 미션</div>
  <div class="m-sub">32×32 픽셀 컬러 이미지 60,000장으로 10가지 사물을 분류합니다.<br>이미지 구조 이해 → Conv Block 구현 → VGG 모델 조립 → 학습 → 평가의 완전한 파이프라인을 구현하세요.</div>
</div>

<div class="ml-sec">학습 목표</div>
<div class="obj-list">
  <div class="obj-item"><div class="obj-n">①</div><span>CHW 구조와 Tensor shape 이해 <strong style="color:var(--or)">(pixel → RGB → Tensor)</strong></span></div>
  <div class="obj-item"><div class="obj-n">②</div><span>Conv → ReLU → MaxPool 흐름 직접 구현</span></div>
  <div class="obj-item"><div class="obj-n">③</div><span>Channel 증가 패턴으로 VGG 스타일 모델 조립</span></div>
  <div class="obj-item"><div class="obj-n">④</div><span>zero_grad → backward → step 학습 루프 체득</span></div>
  <div class="obj-item"><div class="obj-n">⑤</div><span>train/eval 모드 전환 · Accuracy 직접 계산</span></div>
</div>

<div class="ml-sec">데이터셋 (60,000장 · 10클래스)</div>
<div class="feat-box">
  <div class="feat-row"><span class="feat-name">이미지 크기</span><span class="feat-desc">32×32 픽셀 · RGB 3채널</span></div>
  <div class="feat-row"><span class="feat-name">Tensor shape <span class="feat-star">★</span></span><span class="feat-desc">CHW 구조: (3, 32, 32)</span></div>
  <div class="feat-row"><span class="feat-name">Train / Test</span><span class="feat-desc">50,000장 / 10,000장</span></div>
  <div class="feat-row"><span class="feat-name">클래스</span><span class="feat-desc">비행기·자동차·새·고양이·사슴·개·개구리·말·배·트럭</span></div>
  <div class="feat-row"><span class="feat-name">전처리</span><span class="feat-desc">ToTensor + Normalize(0.5, 0.5)</span></div>
</div>

<div class="ml-sec">Shape 변화 흐름</div>
<div class="shape-flow">
  <span class="shape-node">(N,3,32,32)</span><span class="shape-arr">→</span>
  <span class="shape-node">Block1</span><span class="shape-arr">→</span>
  <span class="shape-node">(N,64,16,16)</span><span class="shape-arr">→</span>
  <span class="shape-node">Block2</span><span class="shape-arr">→</span>
  <span class="shape-node">(N,128,8,8)</span><span class="shape-arr">→</span>
  <span class="shape-node">Block3</span><span class="shape-arr">→</span>
  <span class="shape-node">(N,256,4,4)</span><span class="shape-arr">→</span>
  <span class="shape-node">Flatten</span><span class="shape-arr">→</span>
  <span class="shape-node">(N,4096)</span><span class="shape-arr">→</span>
  <span class="shape-node">(N,10)</span>
</div>

<div class="ml-sec">TODO 가이드라인</div>
<div class="todo-list">
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">1</div><span class="todo-ctag ctag-ch1">Ch1</span><span class="todo-title">이미지 Tensor shape 확인</span></div>
    <div class="todo-body">CIFAR-10 이미지는 CHW 구조입니다. C=채널(RGB), H=높이, W=너비로 구성됩니다.<div class="hint-box">💡 torch.Tensor의 .shape 속성 · shape[0]=C, shape[1]=H, shape[2]=W</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">2</div><span class="todo-ctag ctag-ch1">Ch1</span><span class="todo-title">DataLoader 설정</span></div>
    <div class="todo-body">학습 데이터는 매 에폭 순서를 섞어 과적합을 방지하고, 평가 데이터는 섞지 않습니다.<div class="hint-box">💡 batch_size=64 · train shuffle=True · test shuffle=False</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">3</div><span class="todo-ctag ctag-ch23">Ch2·3</span><span class="todo-title">Conv Block 구현</span></div>
    <div class="todo-body">3×3 kernel + padding=1이면 Feature Map 크기가 유지됩니다. MaxPool(2×2)로 크기를 절반으로 줄입니다.<div class="hint-box">💡 kernel_size=3, padding=1 → 출력 크기 유지 · MaxPool stride=2 → 크기 절반</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">4</div><span class="todo-ctag ctag-ch34">Ch3·4</span><span class="todo-title">VGG 모델 조립</span></div>
    <div class="todo-body">Channel 증가 패턴 3→64→128→256으로 features를 쌓고, Flatten 후 FC Layer로 classifier를 구성하세요.<div class="hint-box">💡 Flatten() → Linear(256×4×4=4096, 512) → Dropout(0.5) → Linear(512, 10)</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">5</div><span class="todo-ctag ctag-ch4">Ch4</span><span class="todo-title">forward() 구현</span></div>
    <div class="todo-body">self.features로 Conv Block을 통과시키고, self.classifier로 FC Layer를 통과시켜 최종 예측값을 반환하세요.<div class="hint-box">💡 self.features(x) → self.classifier(x) 순서</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">6</div><span class="todo-ctag ctag-ch4">Ch4</span><span class="todo-title">손실함수 + 옵티마이저</span></div>
    <div class="todo-body">분류 문제에는 CrossEntropyLoss를 사용합니다. Softmax + NLLLoss를 합친 함수입니다.<div class="hint-box">💡 분류=CrossEntropyLoss · 옵티마이저=Adam</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">7</div><span class="todo-ctag ctag-ch45">Ch4·5</span><span class="todo-title">학습 루프 구현</span></div>
    <div class="todo-body">학습 모드 전환 → gradient 초기화 → 역전파 순서를 반드시 지켜야 합니다. argmax로 예측 클래스를 추출하세요.<div class="hint-box">💡 model.train() → opt.zero_grad() → loss.backward() · argmax(dim=1)=클래스 인덱스</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">8</div><span class="todo-ctag ctag-ch5">Ch5</span><span class="todo-title">평가 + Accuracy 계산</span></div>
    <div class="todo-body">eval 모드로 Dropout을 비활성화하고 no_grad로 메모리를 절약합니다. 맞춘 개수를 합산해 Accuracy를 계산하세요.<div class="hint-box">💡 model.eval() · torch.no_grad() · .sum()으로 True 개수 합산</div></div>
  </div>
</div>

<div class="ml-sec">핵심 공식</div>
<div class="formula-box">
  Output Size  = (Input - Kernel + 2×Padding) / Stride + 1<br>
  3×3 Conv, padding=1, stride=1  →  크기 유지<br>
  MaxPool(2×2), stride=2         →  크기 절반<br>
  Accuracy = 맞춘 개수 / 전체 개수 × 100
</div>

<div class="acc-wrap">
  <div class="acc-labels">
    <span class="acc-lbl">Test Accuracy 달성도</span>
    <span class="acc-val" id="accDisp">0.0%</span>
  </div>
  <div class="acc-bar"><div class="acc-fill" id="accFill"></div></div>
  <div class="acc-goal">목표: Test Accuracy ≥ 70%</div>
</div>

</div>