<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
단어 임베딩 (Word Embedding)
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
대표 임베딩 방법인
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">Word2Vec</span>
의 원리와 놀라운 성질, 그리고 사전 학습 모델을 알아봅니다.
</p>

</div>

<br>

<!-- Word2Vec -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔤 Word2Vec — 주변 단어로 의미를 학습한다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
가장 유명한 단어 임베딩 방법은 <b>Word2Vec</b> (2013, Google)입니다.
</p>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; margin: 14px 0;">
<span style="color: #FF6B00; font-weight: 900;">💡 핵심 아이디어</span><br>
<b>"비슷한 문맥에 등장하는 단어는 비슷한 의미를 가진다"</b>
</div>

<div style="background-color: #0f172a; border-radius: 14px; padding: 14px 20px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; line-height: 2.2; margin-bottom: 16px; overflow-x: auto; white-space: pre;">
<span style="color:#a6e3a1;">"나는 [강아지]를 산책시켰다"</span>
<span style="color:#a6e3a1;">"나는 [개]를 산책시켰다"</span>
<span style="color:#a6e3a1;">"나는 [고양이]를 산책시켰다"</span>
<span style="color:#6c7086;">→ 항상 비슷한 문장 맥락에서 등장 → 비슷한 벡터로 표현</span></div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 16px;">
Word2Vec의 두 가지 학습 방식:
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:8px;">방식 1. CBOW</div>
    <div style="font-size:12px; color:#94a3b8; margin-bottom:10px;">Continuous Bag of Words</div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 12px; font-family:Consolas, monospace; font-size:12px; color:#cdd6f4; line-height:1.9; margin-bottom:10px; text-align:center;">
      "나는 <span style="color:#ff5f57; font-weight:900;">___</span> 를 산책시켰다"<br>
      <span style="color:#6c7086;">→ "강아지"? "개"? "고양이"?</span>
    </div>
    <div style="font-size:13px; color:#334155; line-height:1.7;">주변 단어들을 보고 <b style="color:#1681c4;">가운데 단어를 맞춥니다.</b></div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:8px;">방식 2. Skip-gram</div>
    <div style="font-size:12px; color:#94a3b8; margin-bottom:10px;">Skip-gram</div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 12px; font-family:Consolas, monospace; font-size:12px; color:#cdd6f4; line-height:1.9; margin-bottom:10px; text-align:center;">
      <span style="color:#a6e3a1; font-weight:900;">"강아지"</span><br>
      <span style="color:#6c7086;">→ "나는", "를", "산책시켰다" ...</span>
    </div>
    <div style="font-size:13px; color:#334155; line-height:1.7;">가운데 단어를 보고 <b style="color:#FF6B00;">주변 단어들을 맞춥니다.</b></div>
  </div>

</div>

<div style="margin-top: 12px; background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
두 방식 모두 <b>엄청난 양의 텍스트</b>를 학습시켜서 단어 벡터를 만듭니다.
</div>

</div>

<br>

<!-- 단어 계산 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
✨ 임베딩의 놀라운 성질: 단어 계산이 가능하다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
단어 임베딩의 가장 놀라운 특징은 <b style="color:#1681c4;">단어 간 수학 계산</b>이 가능하다는 것입니다.
</p>

<div style="display: grid; gap: 12px; margin-top: 16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 20px;">
    <div style="display:flex; align-items:center; gap:12px; flex-wrap:wrap; margin-bottom:12px;">
      <span style="font-size:22px;">👑</span>
      <span style="font-size:15px; font-weight:900; color:#1681c4;">왕</span>
      <span style="font-size:18px; color:#94a3b8; font-weight:900;">−</span>
      <span style="font-size:22px;">👨</span>
      <span style="font-size:15px; font-weight:900; color:#1681c4;">남자</span>
      <span style="font-size:18px; color:#94a3b8; font-weight:900;">+</span>
      <span style="font-size:22px;">👩</span>
      <span style="font-size:15px; font-weight:900; color:#1681c4;">여자</span>
      <span style="font-size:18px; color:#94a3b8; font-weight:900;">=</span>
      <span style="font-size:22px;">👑</span>
      <span style="font-size:15px; font-weight:900; color:#FF6B00;">여왕</span>
    </div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:1.9;">
      vec(<span style="color:#a6e3a1;">"왕"</span>) - vec(<span style="color:#a6e3a1;">"남자"</span>) + vec(<span style="color:#a6e3a1;">"여자"</span>) ≈ vec(<span style="color:#ff5f57; font-weight:900;">"여왕"</span>)
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 20px;">
    <div style="display:flex; align-items:center; gap:12px; flex-wrap:wrap; margin-bottom:12px;">
      <span style="font-size:22px;">🇫🇷</span>
      <span style="font-size:15px; font-weight:900; color:#475569;">프랑스</span>
      <span style="font-size:18px; color:#94a3b8; font-weight:900;">−</span>
      <span style="font-size:22px;">🗼</span>
      <span style="font-size:15px; font-weight:900; color:#475569;">파리</span>
      <span style="font-size:18px; color:#94a3b8; font-weight:900;">+</span>
      <span style="font-size:22px;">🏯</span>
      <span style="font-size:15px; font-weight:900; color:#475569;">서울</span>
      <span style="font-size:18px; color:#94a3b8; font-weight:900;">≈</span>
      <span style="font-size:22px;">🇰🇷</span>
      <span style="font-size:15px; font-weight:900; color:#FF6B00;">한국</span>
    </div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:1.9;">
      vec(<span style="color:#a6e3a1;">"프랑스"</span>) - vec(<span style="color:#a6e3a1;">"파리"</span>) + vec(<span style="color:#a6e3a1;">"서울"</span>) ≈ vec(<span style="color:#ff5f57; font-weight:900;">"한국"</span>)
    </div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡 왜 가능한가?</span><br>
임베딩 공간에서 단어들이 <b>의미 관계를 방향으로 표현</b>하기 때문입니다.<br>
"남자 → 왕" 방향 = "여자 → 여왕" 방향 (왕위 관계)<br>
"나라 → 수도" 방향이 일정하게 유지됩니다. (수도 관계)
</div>

</div>

<br>

<!-- 원핫 vs 임베딩 비교 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📏 원-핫 vs 임베딩 벡터 비교
</h2>

<div style="display: grid; gap: 8px; margin-top: 16px;">

  <div style="display:grid; grid-template-columns:130px 1fr 1fr; gap:8px;">
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">항목</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">원-핫 인코딩</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">단어 임베딩</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr 1fr; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; text-align:center; display:flex; align-items:center; justify-content:center;">벡터 크기</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; display:flex; align-items:center;">단어 사전 크기 (수만~수십만)</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; color:#1681c4; font-weight:900; display:flex; align-items:center;">고정 크기 (보통 50~300)</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr 1fr; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; text-align:center; display:flex; align-items:center; justify-content:center;">값의 형태</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; display:flex; align-items:center;">0과 1만 존재</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; color:#1681c4; display:flex; align-items:center;">연속적인 실수</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr 1fr; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; text-align:center; display:flex; align-items:center; justify-content:center;">의미 반영</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; font-weight:900; display:flex; align-items:center;">❌ 불가능</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; color:#1681c4; font-weight:900; display:flex; align-items:center;">✅ 가능</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr 1fr; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; text-align:center; display:flex; align-items:center; justify-content:center;">유사도 계산</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; display:flex; align-items:center;">모든 단어 쌍이 동일하게 0</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; color:#1681c4; display:flex; align-items:center;">비슷한 단어끼리 높은 유사도</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr 1fr; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; text-align:center; display:flex; align-items:center; justify-content:center;">벡터 유형</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; display:flex; align-items:center;">희소 벡터 (대부분 0)</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; color:#1681c4; display:flex; align-items:center;">밀집 벡터 (모든 값이 의미 있음)</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr 1fr; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; text-align:center; display:flex; align-items:center; justify-content:center;">학습 필요</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; display:flex; align-items:center;">❌ 규칙 기반</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; color:#1681c4; display:flex; align-items:center;">✅ 대량 텍스트 학습 필요</div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 밀집 벡터(Dense Vector)</span><br>
임베딩 벡터를 <b>밀집 벡터(Dense Vector)</b>라고 부릅니다.<br>
원-핫처럼 대부분이 0이 아니라, <b>모든 숫자가 의미 있는 값</b>을 가집니다.
</div>

</div>

<br>

<!-- 사전 학습 모델 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🛠️ 사전 학습된 임베딩 모델 사용하기
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Word2Vec을 직접 학습시키려면 엄청난 양의 텍스트와 시간이 필요합니다.<br>
다행히 이미 대량 데이터로 학습된 <b style="color:#1681c4;">사전 학습 모델</b>을 가져다 쓸 수 있습니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 word2vec_pretrained.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      Word2Vec
    </div>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.9; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">gensim.models</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">KeyedVectors</span>

<span style="color:#6c7086;"># 구글이 뉴스 데이터로 학습한 Word2Vec 모델 (영어)</span>
<span style="color:#6c7086;"># 약 300만 단어, 각 단어를 300차원 벡터로 표현</span>
<span style="color:#cdd6f4;">model = KeyedVectors.load_word2vec_format(</span><span style="color:#a6e3a1;">'GoogleNews-vectors.bin'</span><span style="color:#cdd6f4;">, binary=</span><span style="color:#89dceb;">True</span><span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># 단어 벡터 확인</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(model[</span><span style="color:#a6e3a1;">'king'</span><span style="color:#cdd6f4;">].shape)    </span><span style="color:#6c7086;"># (300,) → 300개의 숫자</span>

<span style="color:#6c7086;"># 비슷한 단어 찾기</span>
<span style="color:#cdd6f4;">similar = model.most_similar(</span><span style="color:#a6e3a1;">'king'</span><span style="color:#cdd6f4;">, topn=</span><span style="color:#89dceb;">5</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(similar)</span>
<span style="color:#6c7086;"># [('kings', 0.71), ('queen', 0.65), ('monarch', 0.64), ...]</span>

<span style="color:#6c7086;"># 단어 유추 계산: 왕 - 남자 + 여자 = ?</span>
<span style="color:#cdd6f4;">result = model.most_similar(positive=[</span><span style="color:#a6e3a1;">'king'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'woman'</span><span style="color:#cdd6f4;">], negative=[</span><span style="color:#a6e3a1;">'man'</span><span style="color:#cdd6f4;">], topn=</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(result)</span>
<span style="color:#6c7086;"># [('queen', 0.71)]</span></div>
</div>

</div>

<br>

<!-- 한국어 임베딩 모델 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🌏 한국어 임베딩 모델
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
한국어에도 사전 학습된 임베딩 모델이 있습니다.
</p>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="display:grid; grid-template-columns:150px 1fr auto; gap:12px; align-items:center; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px;">
    <div style="font-family:Consolas, monospace; font-size:13px; font-weight:900; color:#FF6B00;">Word2Vec (한국어)</div>
    <div style="font-size:13px; color:#475569; line-height:1.6;">위키피디아, 뉴스로 학습</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900; white-space:nowrap;">가볍고 빠름</div>
  </div>

  <div style="display:grid; grid-template-columns:150px 1fr auto; gap:12px; align-items:center; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px;">
    <div style="font-family:Consolas, monospace; font-size:13px; font-weight:900; color:#FF6B00;">FastText (한국어)</div>
    <div style="font-size:13px; color:#475569; line-height:1.6;">글자 단위까지 학습</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900; white-space:nowrap;">신조어·오타에 강함</div>
  </div>

  <div style="display:grid; grid-template-columns:150px 1fr auto; gap:12px; align-items:center; background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px;">
    <div style="font-family:Consolas, monospace; font-size:13px; font-weight:900; color:#1681c4;">KoBERT</div>
    <div style="font-size:13px; color:#475569; line-height:1.6;">카카오뱅크 제공, 문맥 반영</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900; white-space:nowrap;">높은 성능</div>
  </div>

  <div style="display:grid; grid-template-columns:150px 1fr auto; gap:12px; align-items:center; background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px;">
    <div style="font-family:Consolas, monospace; font-size:13px; font-weight:900; color:#1681c4;">KoELECTRA</div>
    <div style="font-size:13px; color:#475569; line-height:1.6;">한국어 특화 트랜스포머</div>
    <div style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900; white-space:nowrap;">현재 가장 많이 사용</div>
  </div>

</div>
</div>

</div>