<style>
:root {
  --or:#FF6B00;--or2:#E55A00;--orL:#FFF0E6;--orB:#FFDCC2;
  --gr:#3EC934;--gr2:#2DAA24;--grL:#E8FFE6;--grB:#C2F0BE;
  --pu:#A855F7;--puL:#F5EEFF;--puB:#DBBEFF;--pu2:#8B3FD9;
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
.ctag-pre  { background:#E1F5EE; color:#085041; border-color:#9FE1CB; }
.ctag-ch3  { background:var(--puL); color:var(--pu2); border-color:var(--puB); }
.ctag-ch45 { background:var(--puL); color:var(--pu2); border-color:var(--puB); }
.ctag-ch4  { background:var(--puL); color:var(--pu2); border-color:var(--puB); }
.ctag-ch2  { background:#E6F1FB; color:#185FA5; border-color:#B5D4F4; }
.ctag-ch25 { background:#E6F1FB; color:#185FA5; border-color:#B5D4F4; }
.ctag-ch5  { background:var(--grL); color:var(--gr2); border-color:var(--grB); }
.todo-title { font-size:12px; font-weight:800; color:var(--dk); flex:1; }
.todo-body  { padding:8px 10px; font-size:11px; color:var(--gy5);
  line-height:1.6; border-top:1px solid var(--gy2); background:#fff; }
.hint-box { margin-top:6px; padding:5px 8px; border-radius:6px;
  background:var(--orL); border:1px solid var(--orB);
  font-size:11px; color:var(--or2); font-weight:700; }
.formula-box { background:var(--dk); color:#E2E8F0; border-radius:var(--r8);
  padding:12px 14px; font-family:var(--fm); font-size:12px; line-height:1.9; }
.r2-wrap { margin-top:14px; }
.r2-labels { display:flex; justify-content:space-between; font-size:11px; margin-bottom:5px; }
.r2-lbl { font-weight:800; color:var(--gy4); }
.r2-val { font-family:var(--fm); font-weight:800; color:var(--gr); }
.r2-bar  { background:var(--gy2); border-radius:20px; height:9px; overflow:hidden; }
.r2-fill { height:100%; border-radius:20px; background:var(--gr); width:0%; transition:width .6s; }
.r2-goal { font-size:10px; color:var(--gy4); margin-top:3px; }
</style>

<div class="md-wrap">

<div class="m-header">
  <div class="m-title">캘리포니아 집값 예측 미션</div>
  <div class="m-sub">1990년 캘리포니아 인구조사 데이터로 지역별 집값 중앙값을 예측합니다.<br>전처리 → Dataset → 모델 → 학습 → 평가의 완전한 파이프라인을 구현하세요.</div>
</div>

<div class="ml-sec">학습 목표</div>
<div class="obj-list">
  <div class="obj-item"><div class="obj-n">①</div><span>특성 정규화가 왜 필수인지 이해 <strong style="color:var(--or)">(R²가 0.30 → 0.70으로 향상)</strong></span></div>
  <div class="obj-item"><div class="obj-n">②</div><span>Dataset / DataLoader 직접 구현</span></div>
  <div class="obj-item"><div class="obj-n">③</div><span>nn.Module 상속 · forward() 작성</span></div>
  <div class="obj-item"><div class="obj-n">④</div><span>zero_grad → backward → step 순서 체득</span></div>
  <div class="obj-item"><div class="obj-n">⑤</div><span>train/eval 모드 전환 · R² 공식 직접 구현</span></div>
</div>

<div class="ml-sec">데이터셋 (20,640 지역구 · 8특성)</div>
<div class="feat-box">
  <div class="feat-row"><span class="feat-name">MedInc <span class="feat-star">★</span></span><span class="feat-desc">소득 중앙값 · 가장 중요</span></div>
  <div class="feat-row"><span class="feat-name">HouseAge</span><span class="feat-desc">주택 연령 중앙값</span></div>
  <div class="feat-row"><span class="feat-name">AveRooms</span><span class="feat-desc">가구당 평균 방 수</span></div>
  <div class="feat-row"><span class="feat-name">Population</span><span class="feat-desc">지역 인구 (스케일 큼!)</span></div>
  <div class="feat-row"><span class="feat-name">AveOccup</span><span class="feat-desc">평균 거주인 수</span></div>
  <div class="feat-row"><span class="feat-name">Lat / Lon</span><span class="feat-desc">위도 / 경도</span></div>
</div>

<div class="ml-sec">TODO 가이드라인</div>
<div class="todo-list">
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">1</div><span class="todo-ctag ctag-ch1">Ch1</span><span class="todo-title">y shape 변환</span></div>
    <div class="todo-body">MSELoss는 pred(N,1)와 y(N,1)이 같은 shape이어야 합니다. 현재 y는 1D(N,)입니다.<div class="hint-box">💡 Ch1 view() · -1은 나머지 차원 자동 계산</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">2</div><span class="todo-ctag ctag-pre">전처리</span><span class="todo-title">특성 정규화</span></div>
    <div class="todo-body">MedInc(0~15) vs Population(3~35,000) 스케일 차이로 정규화 없이 R²≈0.30, 정규화 후 R²≈0.70+<div class="hint-box">💡 sklearn.preprocessing · 평균0, 분산1 · Standard_____</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">3</div><span class="todo-ctag ctag-ch3">Ch3</span><span class="todo-title">Dataset 구현</span></div>
    <div class="todo-body">DataLoader가 호출하는 필수 메서드 2개: 전체 데이터 수 반환 / idx번째 (X, y) 반환<div class="hint-box">💡 __len__: 데이터 개수 · __getitem__: 인덱스로 샘플 접근</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">4</div><span class="todo-ctag ctag-ch3">Ch3</span><span class="todo-title">DataLoader 설정</span></div>
    <div class="todo-body">PyTorch의 배치 학습 클래스명과 파라미터 2개: 한 번에 처리할 샘플 수, 매 에폭 순서 섞기<div class="hint-box">💡 배치 크기는 2의 거듭제곱 · 과적합 방지를 위해 섞기</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">5</div><span class="todo-ctag ctag-ch45">Ch4·5</span><span class="todo-title">모델 아키텍처</span></div>
    <div class="todo-body">입력 차원(특성 수), 비선형 활성화 함수, 과적합 방지 레이어 3가지를 채우세요<div class="hint-box">💡 입력=데이터 특성 수 · 활성화=ReLU계열 · 정규화=Drop___</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">6</div><span class="todo-ctag ctag-ch4">Ch4</span><span class="todo-title">forward() 구현</span></div>
    <div class="todo-body">nn.Sequential 블록 self.net에 x를 통과시켜 결과를 반환하는 한 줄<div class="hint-box">💡 self.net을 함수처럼 호출 · self.net( __ )</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">7</div><span class="todo-ctag ctag-ch2">Ch2</span><span class="todo-title">손실함수 + 옵티마이저</span></div>
    <div class="todo-body">회귀 손실함수(Ch2에서 직접 구현한 그것)와 적응형 학습률 옵티마이저 선택<div class="hint-box">💡 손실=Mean Squared Error Loss · 옵티마이저=Adaptive Moment Estimation</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">8</div><span class="todo-ctag ctag-ch25">Ch2·5</span><span class="todo-title">학습 루프 3단계</span></div>
    <div class="todo-body">① 학습 모드 전환(Dropout 활성화) → ② gradient 0 초기화 → ③ 역전파 실행<div class="hint-box">💡 순서 고정: model.___() → opt.zero_grad() → loss.backward()</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">9</div><span class="todo-ctag ctag-ch5">Ch5</span><span class="todo-title">평가 + R² 직접 구현</span></div>
    <div class="todo-body">Dropout 비활성화 + gradient 추적 끄기 + R² 공식 직접 구현<div class="hint-box">💡 R² = 1 − SS_res / SS_tot · SS_res=잔차제곱합 · SS_tot=전체분산</div></div>
  </div>
</div>

<div class="ml-sec">핵심 공식</div>
<div class="formula-box">
  MSE  = (1/n) · Σ(ŷ − y)²<br>
  R²   = 1 − SS_res / SS_tot<br>
  SS_res = Σ(y − ŷ)²<br>
  SS_tot = Σ(y − ȳ)²
</div>

<div class="r2-wrap">
  <div class="r2-labels">
    <span class="r2-lbl">R² 달성도</span>
    <span class="r2-val" id="r2Disp">0.000</span>
  </div>
  <div class="r2-bar"><div class="r2-fill" id="r2Fill"></div></div>
  <div class="r2-goal">목표: R² ≥ 0.65</div>
</div>

</div>