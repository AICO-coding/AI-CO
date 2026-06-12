<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">Chapter 06 · BERT</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">감정 분류 실습</h1>
<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
한국어 영화 리뷰 데이터를 이용해 <b style="color:#1681c4;">BERT 기반 감정 분류 모델</b>을 미세조정(Fine-tuning)해봅니다.
</p>
</div>

<br>

<!-- 실습 개요 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🛠️ 실습 개요</h2>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px;">
<tr>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#FF6B00; white-space:nowrap; width:110px;">모델</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;"><span style="font-family:Consolas,monospace; background:#fff; border:1px solid #e2e8f0; padding:2px 6px; border-radius:4px;">klue/bert-base</span> (한국어 특화 BERT)</td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#1681c4; white-space:nowrap;">데이터</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">NSMC (네이버 영화 리뷰 감정 분석 데이터셋)</td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#FF6B00; white-space:nowrap;">과제</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">리뷰 문장 → 긍정(1) / 부정(0) 분류</td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#1681c4; white-space:nowrap;">라이브러리</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;"><span style="font-family:Consolas,monospace; background:#fff; border:1px solid #e2e8f0; padding:2px 6px; border-radius:4px;">transformers</span>, <span style="font-family:Consolas,monospace; background:#fff; border:1px solid #e2e8f0; padding:2px 6px; border-radius:4px;">datasets</span>, <span style="font-family:Consolas,monospace; background:#fff; border:1px solid #e2e8f0; padding:2px 6px; border-radius:4px;">torch</span></td>
</tr>
</table>

</div>

<br>

<!-- STEP 1 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">STEP 1</span>
라이브러리 설치 및 임포트
</h2>

<div style="background-color: #1e1e2e; border-radius: 16px; overflow: hidden; margin-top: 16px;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
<div style="display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 01_imports.py</span>
</div>
</div>
<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.0; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#6c7086;"># 필요한 패키지 설치 (최초 1회)</span>
<span style="color:#6c7086;"># pip install transformers datasets torch</span>

<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">transformers</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">(</span>
<span style="color:#cdd6f4;">    BertTokenizer,           </span><span style="color:#6c7086;"># 토크나이저</span>
<span style="color:#cdd6f4;">    BertForSequenceClassification,  </span><span style="color:#6c7086;"># 문장 분류용 BERT 모델</span>
<span style="color:#cdd6f4;">    TrainingArguments,       </span><span style="color:#6c7086;"># 학습 설정</span>
<span style="color:#cdd6f4;">    Trainer                  </span><span style="color:#6c7086;"># 학습 실행 도우미</span>
<span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">datasets</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">load_dataset   </span><span style="color:#6c7086;"># 데이터셋 불러오기</span>
<span style="color:#cba6f7;">import</span> <span style="color:#89dceb;">torch</span>
<span style="color:#cba6f7;">import</span> <span style="color:#89dceb;">numpy</span> <span style="color:#cba6f7;">as</span> <span style="color:#cdd6f4;">np</span>
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">sklearn.metrics</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">accuracy_score</span></div>
</div>

</div>

<br>

<!-- STEP 2 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">STEP 2</span>
데이터셋 불러오기
</h2>

<div style="background-color: #1e1e2e; border-radius: 16px; overflow: hidden; margin-top: 16px;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
<div style="display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 02_dataset.py</span>
</div>
</div>
<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.0; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#6c7086;"># NSMC 데이터셋 로드 (네이버 영화 리뷰 감정 분류)</span>
<span style="color:#6c7086;"># 긍정(1) / 부정(0) 레이블이 달린 리뷰 20만 건</span>
<span style="color:#cdd6f4;">dataset = load_dataset(</span><span style="color:#a6e3a1;">"nsmc"</span><span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># 데이터 구조 확인</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(dataset)</span>
<span style="color:#6c7086;"># DatasetDict({</span>
<span style="color:#6c7086;">#     train: Dataset({features: ['id', 'document', 'label'], num_rows: 150000})</span>
<span style="color:#6c7086;">#     test:  Dataset({features: ['id', 'document', 'label'], num_rows: 50000})</span>
<span style="color:#6c7086;"># })</span>

<span style="color:#6c7086;"># 샘플 확인</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(dataset[</span><span style="color:#a6e3a1;">'train'</span><span style="color:#cdd6f4;">][</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">])</span>
<span style="color:#6c7086;"># {'id': '9976970', 'document': '아 더빙.. 진짜 짜증나네요 목소리', 'label': 0}</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(dataset[</span><span style="color:#a6e3a1;">'train'</span><span style="color:#cdd6f4;">][</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">])</span>
<span style="color:#6c7086;"># {'id': '3819312', 'document': '흠...포스터보고 초딩영화줄....', 'label': 1}</span></div>
</div>

</div>

<br>

<!-- STEP 3 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">STEP 3</span>
토크나이저 준비 및 전처리
</h2>

<div style="background-color: #1e1e2e; border-radius: 16px; overflow: hidden; margin-top: 16px;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
<div style="display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 03_tokenize.py</span>
</div>
</div>
<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.0; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#6c7086;"># 한국어 특화 BERT 토크나이저 로드</span>
<span style="color:#cdd6f4;">MODEL_NAME = </span><span style="color:#a6e3a1;">"klue/bert-base"</span>
<span style="color:#cdd6f4;">tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)</span>

<span style="color:#6c7086;"># 토크나이징 함수 정의</span>
<span style="color:#cba6f7;">def</span> <span style="color:#89dceb;">tokenize_function</span><span style="color:#cdd6f4;">(examples):</span>
<span style="color:#cba6f7;">    return</span> <span style="color:#cdd6f4;">tokenizer(</span>
<span style="color:#cdd6f4;">        examples[</span><span style="color:#a6e3a1;">'document'</span><span style="color:#cdd6f4;">],   </span><span style="color:#6c7086;"># 리뷰 텍스트</span>
<span style="color:#cdd6f4;">        padding=</span><span style="color:#a6e3a1;">'max_length'</span><span style="color:#cdd6f4;">,   </span><span style="color:#6c7086;"># 최대 길이(128)까지 [PAD]로 채우기</span>
<span style="color:#cdd6f4;">        truncation=</span><span style="color:#89dceb;">True</span><span style="color:#cdd6f4;">,        </span><span style="color:#6c7086;"># 128 초과 시 잘라내기</span>
<span style="color:#cdd6f4;">        max_length=</span><span style="color:#89dceb;">128</span>          <span style="color:#6c7086;"># 최대 토큰 수 (속도를 위해 128로 설정)</span>
<span style="color:#cdd6f4;">    )</span>

<span style="color:#6c7086;"># 전체 데이터셋에 토크나이저 적용</span>
<span style="color:#cdd6f4;">tokenized_dataset = dataset.map(tokenize_function, batched=</span><span style="color:#89dceb;">True</span><span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># 불필요한 컬럼 제거, 레이블 컬럼 이름 통일</span>
<span style="color:#cdd6f4;">tokenized_dataset = tokenized_dataset.remove_columns([</span><span style="color:#a6e3a1;">'id'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'document'</span><span style="color:#cdd6f4;">])</span>
<span style="color:#cdd6f4;">tokenized_dataset = tokenized_dataset.rename_column(</span><span style="color:#a6e3a1;">'label'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'labels'</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cdd6f4;">tokenized_dataset.set_format(</span><span style="color:#a6e3a1;">'torch'</span><span style="color:#cdd6f4;">)  </span><span style="color:#6c7086;"># PyTorch 텐서 형식으로</span>

<span style="color:#6c7086;"># 학습/검증 데이터 분리</span>
<span style="color:#cdd6f4;">train_dataset = tokenized_dataset[</span><span style="color:#a6e3a1;">'train'</span><span style="color:#cdd6f4;">]</span>
<span style="color:#cdd6f4;">eval_dataset  = tokenized_dataset[</span><span style="color:#a6e3a1;">'test'</span><span style="color:#cdd6f4;">]</span>

<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"학습 데이터: {len(train_dataset)}개"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"검증 데이터: {len(eval_dataset)}개"</span><span style="color:#cdd6f4;">)</span></div>
</div>

</div>

<br>

<!-- STEP 4 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">STEP 4</span>
BERT 분류 모델 불러오기
</h2>

<div style="background-color: #1e1e2e; border-radius: 16px; overflow: hidden; margin-top: 16px;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
<div style="display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 04_model.py</span>
</div>
</div>
<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.0; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#6c7086;"># 문장 분류용 BERT 모델 로드</span>
<span style="color:#6c7086;"># BertForSequenceClassification = BERT + 분류기(Linear Layer)</span>
<span style="color:#cdd6f4;">model = BertForSequenceClassification.from_pretrained(</span>
<span style="color:#cdd6f4;">    MODEL_NAME,</span>
<span style="color:#cdd6f4;">    num_labels=</span><span style="color:#89dceb;">2</span>    <span style="color:#6c7086;"># 분류 클래스 수: 긍정(1), 부정(0)</span>
<span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># 모델 구조 간략 확인</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(model.config.hidden_size)    </span><span style="color:#6c7086;"># 768 (벡터 차원)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(model.config.num_labels)     </span><span style="color:#6c7086;"># 2   (분류 클래스 수)</span>

<span style="color:#6c7086;"># 파라미터 수 확인</span>
<span style="color:#cdd6f4;">total_params = </span><span style="color:#cba6f7;">sum</span><span style="color:#cdd6f4;">(p.numel() </span><span style="color:#cba6f7;">for</span><span style="color:#cdd6f4;"> p </span><span style="color:#cba6f7;">in</span><span style="color:#cdd6f4;"> model.parameters())</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"전체 파라미터 수: {total_params:,}"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#6c7086;"># → 약 110,617,090개 (약 1.1억 개)</span></div>
</div>

</div>

<br>

<!-- STEP 5 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">STEP 5</span>
평가 지표 정의
</h2>

<div style="background-color: #1e1e2e; border-radius: 16px; overflow: hidden; margin-top: 16px;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
<div style="display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 05_metrics.py</span>
</div>
</div>
<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.0; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#cba6f7;">def</span> <span style="color:#89dceb;">compute_metrics</span><span style="color:#cdd6f4;">(eval_pred):</span>
<span style="color:#a6e3a1;">    """</span>
<span style="color:#a6e3a1;">    Trainer가 평가할 때 호출하는 함수</span>
<span style="color:#a6e3a1;">    eval_pred: (예측 로짓값, 정답 레이블) 튜플</span>
<span style="color:#a6e3a1;">    """</span>
<span style="color:#cdd6f4;">    logits, labels = eval_pred</span>

<span style="color:#6c7086;">    # 로짓 → 예측 클래스 (가장 높은 값의 인덱스)</span>
<span style="color:#cdd6f4;">    predictions = np.argmax(logits, axis=-</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;">    # 정확도 계산</span>
<span style="color:#cdd6f4;">    acc = accuracy_score(labels, predictions)</span>
<span style="color:#cba6f7;">    return</span> <span style="color:#cdd6f4;">{</span><span style="color:#a6e3a1;">"accuracy"</span><span style="color:#cdd6f4;">: acc}</span></div>
</div>

</div>

<br>

<!-- STEP 6 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">STEP 6</span>
학습 설정 및 실행
</h2>

<div style="background-color: #1e1e2e; border-radius: 16px; overflow: hidden; margin-top: 16px;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
<div style="display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 06_train.py</span>
</div>
<div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">학습률 작게!</div>
</div>
<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.0; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#6c7086;"># 학습 하이퍼파라미터 설정</span>
<span style="color:#cdd6f4;">training_args = TrainingArguments(</span>
<span style="color:#cdd6f4;">    output_dir=</span><span style="color:#a6e3a1;">"./bert_sentiment"</span><span style="color:#cdd6f4;">,      </span><span style="color:#6c7086;"># 모델 저장 경로</span>
<span style="color:#cdd6f4;">    num_train_epochs=</span><span style="color:#89dceb;">3</span><span style="color:#cdd6f4;">,                 </span><span style="color:#6c7086;"># 전체 데이터 반복 횟수</span>
<span style="color:#cdd6f4;">    per_device_train_batch_size=</span><span style="color:#89dceb;">32</span><span style="color:#cdd6f4;">,     </span><span style="color:#6c7086;"># 배치 크기 (한 번에 32개 문장)</span>
<span style="color:#cdd6f4;">    per_device_eval_batch_size=</span><span style="color:#89dceb;">64</span><span style="color:#cdd6f4;">,      </span><span style="color:#6c7086;"># 평가 배치 크기</span>
<span style="color:#cdd6f4;">    learning_rate=</span><span style="color:#f9e2af; font-weight:900;">2e-5</span><span style="color:#cdd6f4;">,                 </span><span style="color:#f9e2af;"># 학습률 (미세조정은 작게!)</span>
<span style="color:#cdd6f4;">    warmup_steps=</span><span style="color:#89dceb;">500</span><span style="color:#cdd6f4;">,                   </span><span style="color:#6c7086;"># 초반 학습률 천천히 올리기</span>
<span style="color:#cdd6f4;">    weight_decay=</span><span style="color:#89dceb;">0.01</span><span style="color:#cdd6f4;">,                  </span><span style="color:#6c7086;"># 과적합 방지</span>
<span style="color:#cdd6f4;">    evaluation_strategy=</span><span style="color:#a6e3a1;">"epoch"</span><span style="color:#cdd6f4;">,        </span><span style="color:#6c7086;"># 매 에폭마다 평가</span>
<span style="color:#cdd6f4;">    save_strategy=</span><span style="color:#a6e3a1;">"epoch"</span><span style="color:#cdd6f4;">,              </span><span style="color:#6c7086;"># 매 에폭마다 저장</span>
<span style="color:#cdd6f4;">    load_best_model_at_end=</span><span style="color:#89dceb;">True</span><span style="color:#cdd6f4;">,        </span><span style="color:#6c7086;"># 가장 좋은 모델 자동 선택</span>
<span style="color:#cdd6f4;">    logging_steps=</span><span style="color:#89dceb;">100</span><span style="color:#cdd6f4;">,                  </span><span style="color:#6c7086;"># 100 스텝마다 로그 출력</span>
<span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># Trainer 생성 및 학습 실행</span>
<span style="color:#cdd6f4;">trainer = Trainer(</span>
<span style="color:#cdd6f4;">    model=model,</span>
<span style="color:#cdd6f4;">    args=training_args,</span>
<span style="color:#cdd6f4;">    train_dataset=train_dataset,</span>
<span style="color:#cdd6f4;">    eval_dataset=eval_dataset,</span>
<span style="color:#cdd6f4;">    compute_metrics=compute_metrics,</span>
<span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># 학습 시작!</span>
<span style="color:#cdd6f4;">trainer.train()</span></div>
</div>

</div>

<br>

<!-- STEP 7 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">STEP 7</span>
새 문장으로 예측하기
</h2>

<div style="background-color: #1e1e2e; border-radius: 16px; overflow: hidden; margin-top: 16px;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
<div style="display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 07_predict.py</span>
</div>
</div>
<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.0; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#cba6f7;">def</span> <span style="color:#89dceb;">predict_sentiment</span><span style="color:#cdd6f4;">(text):</span>
<span style="color:#a6e3a1;">    """</span>
<span style="color:#a6e3a1;">    입력 문장의 감정(긍정/부정)을 예측하는 함수</span>
<span style="color:#a6e3a1;">    """</span>
<span style="color:#6c7086;">    # 토크나이징</span>
<span style="color:#cdd6f4;">    inputs = tokenizer(</span>
<span style="color:#cdd6f4;">        text,</span>
<span style="color:#cdd6f4;">        return_tensors=</span><span style="color:#a6e3a1;">'pt'</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">        padding=</span><span style="color:#89dceb;">True</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">        truncation=</span><span style="color:#89dceb;">True</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">        max_length=</span><span style="color:#89dceb;">128</span>
<span style="color:#cdd6f4;">    )</span>

<span style="color:#6c7086;">    # 예측 (gradient 계산 불필요)</span>
<span style="color:#cba6f7;">    with</span> <span style="color:#cdd6f4;">torch.no_grad():</span>
<span style="color:#cdd6f4;">        outputs = model(**inputs)</span>

<span style="color:#6c7086;">    # 로짓 → 확률 → 클래스</span>
<span style="color:#cdd6f4;">    logits = outputs.logits</span>
<span style="color:#cdd6f4;">    probs  = torch.softmax(logits, dim=-</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cdd6f4;">    pred   = torch.argmax(probs, dim=-</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">).item()</span>

<span style="color:#cdd6f4;">    label_map = {</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">: </span><span style="color:#a6e3a1;">"부정 😞"</span><span style="color:#cdd6f4;">, </span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">: </span><span style="color:#a6e3a1;">"긍정 😊"</span><span style="color:#cdd6f4;">}</span>
<span style="color:#cba6f7;">    print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"입력: {text}"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">    print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"예측: {label_map[pred]}"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">    print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"긍정 확률: {probs[0][1].item():.2%}"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">    print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"부정 확률: {probs[0][0].item():.2%}"</span><span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># 테스트</span>
<span style="color:#cdd6f4;">predict_sentiment(</span><span style="color:#a6e3a1;">"이 영화 정말 감동적이고 최고였어요!"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cdd6f4;">predict_sentiment(</span><span style="color:#a6e3a1;">"배우 연기도 별로고 스토리도 너무 지루했어요."</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cdd6f4;">predict_sentiment(</span><span style="color:#a6e3a1;">"그냥 그저 그런 영화였습니다."</span><span style="color:#cdd6f4;">)</span></div>
</div>

</div>

<br>

<!-- STEP 8 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">STEP 8</span>
모델 저장 및 불러오기
</h2>

<div style="background-color: #1e1e2e; border-radius: 16px; overflow: hidden; margin-top: 16px;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
<div style="display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 08_save_load.py</span>
</div>
</div>
<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.0; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#6c7086;"># 모델과 토크나이저 저장</span>
<span style="color:#cdd6f4;">model.save_pretrained(</span><span style="color:#a6e3a1;">"./my_sentiment_model"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cdd6f4;">tokenizer.save_pretrained(</span><span style="color:#a6e3a1;">"./my_sentiment_model"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"모델 저장 완료!"</span><span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># 나중에 불러오기</span>
<span style="color:#cdd6f4;">loaded_model = BertForSequenceClassification.from_pretrained(</span><span style="color:#a6e3a1;">"./my_sentiment_model"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cdd6f4;">loaded_tokenizer = BertTokenizer.from_pretrained(</span><span style="color:#a6e3a1;">"./my_sentiment_model"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"모델 불러오기 완료!"</span><span style="color:#cdd6f4;">)</span></div>
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;"><span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리</div>
<div style="display: grid; gap: 8px;">
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;"><span style="font-family:Consolas,monospace; background:#fff3eb; border:1px solid #ffd0b0; padding:1px 6px; border-radius:4px;">BertForSequenceClassification</span> = <b style="color:#FF6B00;">사전학습된 BERT + 분류기 Linear Layer</b> 패키지입니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">토크나이저로 입력을 만들고 → BERT 통과 → CLS 벡터 → 분류기 → 결과가 전체 흐름입니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;"><span style="font-family:Consolas,monospace; background:#fff3eb; border:1px solid #ffd0b0; padding:1px 6px; border-radius:4px;">TrainingArguments</span>와 <span style="font-family:Consolas,monospace; background:#fff3eb; border:1px solid #ffd0b0; padding:1px 6px; border-radius:4px;">Trainer</span>를 사용하면 <b style="color:#FF6B00;">복잡한 학습 루프를 몇 줄로</b> 처리할 수 있습니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">학습률은 <b style="color:#FF6B00;">2e-5 ~ 5e-5</b>처럼 매우 작게 설정해야 사전학습 지식을 유지하면서 미세조정됩니다.</div>
</div>
</div>

</div>