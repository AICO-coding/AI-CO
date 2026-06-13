<style>
:root {
  --or:#FF6B00;--or2:#E55A00;--orL:#FFF0E6;--orB:#FFDCC2;
  --gr:#3EC934;--gr2:#2DAA24;--grL:#E8FFE6;--grB:#C2F0BE;
  --pu:#A855F7;--puL:#F5EEFF;--puB:#DBBEFF;--pu2:#8B3FD9;
  --bl:#185FA5;--blL:#E6F1FB;--blB:#B5D4F4;
  --te:#0F6E56;--teL:#E1F5EE;--teB:#9FE1CB;
  --pk:#D6336C;--pkL:#FFE4ED;--pkB:#FFC2D6;
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
.ctag-ch2  { background:var(--blL); color:var(--bl); border-color:var(--blB); }
.ctag-ch3  { background:var(--puL); color:var(--pu2); border-color:var(--puB); }
.ctag-ch4  { background:var(--grL); color:var(--gr2); border-color:var(--grB); }
.ctag-ch5  { background:var(--teL); color:var(--te); border-color:var(--teB); }
.ctag-ch6  { background:var(--orL); color:var(--or2); border-color:var(--orB); }
.ctag-ch7  { background:var(--pkL); color:var(--pk); border-color:var(--pkB); }
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
.shape-node-pk { background:var(--pkL); border:1px solid var(--pkB); border-radius:6px;
  padding:4px 8px; font-family:var(--fm); font-size:11px; font-weight:800; color:var(--pk); }
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
  <div class="m-title">뉴스 카테고리 분류 + GPT 헤드라인 자동완성 미션</div>
  <div class="m-sub">연합뉴스 제목(KLUE-YNAT) 데이터로 카테고리를 분류하는 BERT와, 그 결과로 헤드라인을 이어 쓰는 GPT를 한 파이프라인에서 구현합니다.<br>토큰화 → 전처리 → 임베딩 → Self-Attention → BERT 분류 → 학습/평가 → GPT 자동완성까지, NLP의 이해(BERT)와 생성(GPT)을 모두 체험하세요.</div>
</div>

<div class="ml-sec">학습 목표</div>
<div class="obj-list">
  <div class="obj-item"><div class="obj-n">①</div><span>문장을 <strong style="color:var(--or)">토큰(Token)</strong>으로 나누고 단어 사전(vocab) 이해하기</span></div>
  <div class="obj-item"><div class="obj-n">②</div><span>padding·truncation·attention_mask로 입력 데이터 전처리</span></div>
  <div class="obj-item"><div class="obj-n">③</div><span>제목·라벨을 Dataset/DataLoader로 구성해 <strong style="color:var(--or)">학습 가능한 벡터</strong>로 변환</span></div>
  <div class="obj-item"><div class="obj-n">④</div><span>Self-Attention으로 문맥이 반영된 [CLS] 벡터 추출</span></div>
  <div class="obj-item"><div class="obj-n">⑤</div><span>Transformer 인코더(BERT)의 레이어·헤드 구조 확인</span></div>
  <div class="obj-item"><div class="obj-n">⑥</div><span>BertForSequenceClassification으로 뉴스 카테고리(7종) Fine-tuning</span></div>
  <div class="obj-item"><div class="obj-n">⑦</div><span>GPT의 <strong style="color:var(--pk)">자기회귀 생성(Autoregressive)</strong>으로 헤드라인 자동완성 · BERT vs GPT 비교</span></div>
</div>

<div class="ml-sec">데이터셋 & 모델</div>
<div class="feat-box">
  <div class="feat-row"><span class="feat-name">데이터</span><span class="feat-desc">KLUE-YNAT 연합뉴스 제목</span></div>
  <div class="feat-row"><span class="feat-name">카테고리 <span class="feat-star">★</span></span><span class="feat-desc">IT과학·경제·사회·생활문화·세계·스포츠·정치 (7종)</span></div>
  <div class="feat-row"><span class="feat-name">실습 규모</span><span class="feat-desc">train 3,000개 / test 500개 (샘플링)</span></div>
  <div class="feat-row"><span class="feat-name">분류 모델</span><span class="feat-desc">klue/bert-base (BertForSequenceClassification)</span></div>
  <div class="feat-row"><span class="feat-name">생성 모델</span><span class="feat-desc">skt/kogpt2-base-v2 (AutoModelForCausalLM)</span></div>
</div>

<div class="ml-sec">파이프라인 흐름</div>
<div class="shape-flow">
  <span class="shape-node">"뉴스 제목"</span><span class="shape-arr">→</span>
  <span class="shape-node">Tokenizer</span><span class="shape-arr">→</span>
  <span class="shape-node">input_ids</span><span class="shape-arr">→</span>
  <span class="shape-node">BERT Self-Attention</span><span class="shape-arr">→</span>
  <span class="shape-node">[CLS]</span><span class="shape-arr">→</span>
  <span class="shape-node">분류 → 카테고리</span><span class="shape-arr">⇒</span>
  <span class="shape-node-pk">GPT 입력 prompt</span><span class="shape-arr">→</span>
  <span class="shape-node-pk">Causal Attention</span><span class="shape-arr">→</span>
  <span class="shape-node-pk">한 토큰씩 생성 ×N</span>
</div>

<div class="ml-sec">TODO 가이드라인</div>
<div class="todo-list">
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">1</div><span class="todo-ctag ctag-ch1">Ch1</span><span class="todo-title">토큰화 & 단어 사전 확인</span></div>
    <div class="todo-body">뉴스 제목을 토큰 단위로 나누고, BERT가 알고 있는 전체 단어 사전 크기를 확인합니다.<div class="hint-box">💡 tokenizer.tokenize(문장) → 토큰 리스트 · tokenizer.vocab_size → 전체 단어 수</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">2</div><span class="todo-ctag ctag-ch2">Ch2</span><span class="todo-title">패딩 & Attention Mask 생성</span></div>
    <div class="todo-body">제목마다 길이가 다르기 때문에 max_length에 맞춰 패딩하고, 실제 토큰과 패딩을 구분하는 attention_mask를 만듭니다.<div class="hint-box">💡 padding='max_length', truncation=True · attention_mask: 1=실제 토큰, 0=패딩</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">3</div><span class="todo-ctag ctag-ch3">Ch3</span><span class="todo-title">Dataset 클래스 완성</span></div>
    <div class="todo-body">전처리한 input_ids·attention_mask·카테고리 라벨을 하나로 묶는 Dataset을 완성하고, 학습/평가용 DataLoader를 구성합니다.<div class="hint-box">💡 __len__은 전체 데이터 개수 · train은 shuffle=True, test는 shuffle=False</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">4</div><span class="todo-ctag ctag-ch4">Ch4</span><span class="todo-title">Self-Attention 결과에서 [CLS] 추출</span></div>
    <div class="todo-body">BERT는 Self-Attention으로 모든 토큰이 서로를 참고한 벡터(last_hidden_state)를 만듭니다. 문장 전체를 대표하는 [CLS] 벡터를 꺼내봅니다.<div class="hint-box">💡 output.last_hidden_state shape = (배치, 시퀀스, hidden) · [CLS]는 인덱스 0</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">5</div><span class="todo-ctag ctag-ch5">Ch5</span><span class="todo-title">Transformer 인코더 구조 확인</span></div>
    <div class="todo-body">BERT는 여러 개의 Transformer 인코더 블록을 쌓은 구조입니다. config에서 레이어 수와 Multi-Head Attention의 head 수를 확인합니다.<div class="hint-box">💡 config.num_hidden_layers = 인코더 블록 수 · config.num_attention_heads = head 수</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">6</div><span class="todo-ctag ctag-ch6">Ch6</span><span class="todo-title">BERT 다중분류 모델 + 옵티마이저</span></div>
    <div class="todo-body">사전학습된 BERT 위에 7개 카테고리용 분류 헤드를 얹은 BertForSequenceClassification을 완성하고, Transformer 계열의 표준 옵티마이저를 설정합니다.<div class="hint-box">💡 num_labels=7 (뉴스 카테고리 7개) · 옵티마이저 = AdamW</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">7</div><span class="todo-ctag ctag-ch6">Ch6</span><span class="todo-title">Fine-tuning 학습 루프</span></div>
    <div class="todo-body">학습 모드 전환 → gradient 초기화 → labels와 함께 forward → 역전파 순서를 지켜야 합니다. BERT 분류 모델은 loss를 직접 계산해 반환합니다.<div class="hint-box">💡 model.train() → opt.zero_grad() → loss.backward() · outputs.loss · argmax(dim=1)=예측 카테고리</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">8</div><span class="todo-ctag ctag-ch6">Ch6</span><span class="todo-title">평가 + 카테고리 예측</span></div>
    <div class="todo-body">eval 모드로 Dropout을 비활성화하고 no_grad로 메모리를 절약합니다. Accuracy를 계산하고, 첫 번째 테스트 기사의 예측 카테고리를 GPT 입력으로 넘겨줍니다.<div class="hint-box">💡 model.eval() · torch.no_grad() · 예측값과 labels를 비교해 정확도 계산</div></div>
  </div>
  <div class="todo-card">
    <div class="todo-head"><div class="todo-n">9</div><span class="todo-ctag ctag-ch7">Ch7</span><span class="todo-title">GPT 헤드라인 자동완성</span></div>
    <div class="todo-body">BERT가 예측한 카테고리를 prompt에 넣고, GPT로 다음 토큰을 한 개씩 예측해 입력에 이어붙이는 자기회귀(Autoregressive) 생성을 직접 구현합니다.<div class="hint-box">💡 torch.no_grad() · outputs.logits에서 마지막 토큰의 분포 추출 · argmax로 다음 토큰 선택 · torch.cat으로 이어붙이기</div></div>
  </div>
</div>

<div class="ml-sec">핵심 공식</div>
<div class="formula-box">
  Self-Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V<br>
  BERT = Transformer Encoder × N layers → 모든 토큰을 동시에 보고 분류 (이해)<br>
  GPT  = Transformer Decoder × N layers → 이전 토큰만 보고 다음 토큰 생성 (생성)<br>
  Accuracy = 맞춘 개수 / 전체 개수 × 100
</div>

<div class="acc-wrap">
  <div class="acc-labels">
    <span class="acc-lbl">Test Accuracy 달성도</span>
    <span class="acc-val" id="accDisp">0.0%</span>
  </div>
  <div class="acc-bar"><div class="acc-fill" id="accFill"></div></div>
  <div class="acc-goal">목표: Test Accuracy ≥ 60% (7개 클래스 분류)</div>
</div>

</div>