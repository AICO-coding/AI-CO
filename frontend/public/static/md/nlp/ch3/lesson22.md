<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
텍스트 표현 방식 비교
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
네 가지 방법을
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">같은 데이터로 한 번에 비교</span>
하는 실습 코드와 챕터 3 전체를 마무리합니다.
</p>

</div>

<br>

<!-- 실습 코드 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💻 실습 코드
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
네 가지 방법을 같은 데이터로 한 번에 비교해봅시다!
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 text_representation_compare.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      표현 방식 비교
    </div>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.9; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#cba6f7;">import</span> <span style="color:#89dceb;">numpy</span> <span style="color:#cba6f7;">as</span> <span style="color:#cdd6f4;">np</span>
<span style="color:#cba6f7;">import</span> <span style="color:#89dceb;">pandas</span> <span style="color:#cba6f7;">as</span> <span style="color:#cdd6f4;">pd</span>
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">sklearn.feature_extraction.text</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">CountVectorizer, TfidfVectorizer</span>
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">sklearn.metrics.pairwise</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">cosine_similarity</span>

<span style="color:#6c7086;"># ─────────────────────────────────────────</span>
<span style="color:#6c7086;"># 공통 데이터</span>
<span style="color:#6c7086;"># ─────────────────────────────────────────</span>
<span style="color:#cdd6f4;">corpus = [</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"나는 밥을 먹었다"</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"나는 물을 마셨다"</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"고양이가 밥을 먹었다"</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"고양이가 물을 마셨다"</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">]</span>
<span style="color:#cdd6f4;">doc_labels = [</span><span style="color:#a6e3a1;">"문서1"</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">"문서2"</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">"문서3"</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">"문서4"</span><span style="color:#cdd6f4;">]</span>
<span style="color:#cdd6f4;">target = (</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">, </span><span style="color:#89dceb;">2</span><span style="color:#cdd6f4;">)   </span><span style="color:#6c7086;"># 비교할 문서 쌍: 문서1 ↔ 문서3</span>

<span style="color:#6c7086;"># ─────────────────────────────────────────</span>
<span style="color:#6c7086;"># 방법 1. BoW</span>
<span style="color:#6c7086;"># ─────────────────────────────────────────</span>
<span style="color:#cdd6f4;">bow_vec = CountVectorizer()</span>
<span style="color:#cdd6f4;">bow_mat = bow_vec.fit_transform(corpus)</span>
<span style="color:#cdd6f4;">sim_bow  = cosine_similarity(bow_mat[target[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">]], bow_mat[target[</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">]])[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">][</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">]</span>

<span style="color:#6c7086;"># ─────────────────────────────────────────</span>
<span style="color:#6c7086;"># 방법 2. TF-IDF</span>
<span style="color:#6c7086;"># ─────────────────────────────────────────</span>
<span style="color:#cdd6f4;">tfidf_vec = TfidfVectorizer()</span>
<span style="color:#cdd6f4;">tfidf_mat = tfidf_vec.fit_transform(corpus)</span>
<span style="color:#cdd6f4;">sim_tfidf = cosine_similarity(tfidf_mat[target[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">]], tfidf_mat[target[</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">]])[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">][</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">]</span>

<span style="color:#6c7086;"># ─────────────────────────────────────────</span>
<span style="color:#6c7086;"># 방법 3. 단어 임베딩 (Word2Vec 시뮬레이션)</span>
<span style="color:#6c7086;"># ─────────────────────────────────────────</span>
<span style="color:#cdd6f4;">word_vectors = {</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"나는"</span><span style="color:#cdd6f4;">:    np.array([ </span><span style="color:#89dceb;">0.5</span><span style="color:#cdd6f4;">,  </span><span style="color:#89dceb;">0.2</span><span style="color:#cdd6f4;">, -</span><span style="color:#89dceb;">0.1</span><span style="color:#cdd6f4;">,  </span><span style="color:#89dceb;">0.3</span><span style="color:#cdd6f4;">]),</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"밥을"</span><span style="color:#cdd6f4;">:    np.array([ </span><span style="color:#89dceb;">0.3</span><span style="color:#cdd6f4;">, -</span><span style="color:#89dceb;">0.1</span><span style="color:#cdd6f4;">,  </span><span style="color:#89dceb;">0.8</span><span style="color:#cdd6f4;">,  </span><span style="color:#89dceb;">0.4</span><span style="color:#cdd6f4;">]),</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"먹었다"</span><span style="color:#cdd6f4;">:  np.array([ </span><span style="color:#89dceb;">0.3</span><span style="color:#cdd6f4;">, -</span><span style="color:#89dceb;">0.1</span><span style="color:#cdd6f4;">,  </span><span style="color:#89dceb;">0.7</span><span style="color:#cdd6f4;">,  </span><span style="color:#89dceb;">0.4</span><span style="color:#cdd6f4;">]),</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"물을"</span><span style="color:#cdd6f4;">:    np.array([ </span><span style="color:#89dceb;">0.3</span><span style="color:#cdd6f4;">, -</span><span style="color:#89dceb;">0.1</span><span style="color:#cdd6f4;">,  </span><span style="color:#89dceb;">0.75</span><span style="color:#cdd6f4;">, </span><span style="color:#89dceb;">0.38</span><span style="color:#cdd6f4;">]),</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"마셨다"</span><span style="color:#cdd6f4;">:  np.array([ </span><span style="color:#89dceb;">0.28</span><span style="color:#cdd6f4;">,-</span><span style="color:#89dceb;">0.09</span><span style="color:#cdd6f4;">, </span><span style="color:#89dceb;">0.72</span><span style="color:#cdd6f4;">, </span><span style="color:#89dceb;">0.41</span><span style="color:#cdd6f4;">]),</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"고양이가"</span><span style="color:#cdd6f4;">:np.array([-</span><span style="color:#89dceb;">0.2</span><span style="color:#cdd6f4;">,  </span><span style="color:#89dceb;">0.8</span><span style="color:#cdd6f4;">,  </span><span style="color:#89dceb;">0.1</span><span style="color:#cdd6f4;">, -</span><span style="color:#89dceb;">0.3</span><span style="color:#cdd6f4;">]),</span>
<span style="color:#cdd6f4;">}</span>

<span style="color:#cba6f7;">def</span> <span style="color:#89dceb;">sentence_to_embedding</span><span style="color:#cdd6f4;">(sentence, vectors):</span>
<span style="color:#cdd6f4;">    </span><span style="color:#6c7086;">"""문장 내 단어 벡터들의 평균으로 문장 벡터 생성"""</span>
<span style="color:#cdd6f4;">    words = sentence.split()</span>
<span style="color:#cdd6f4;">    vecs  = [vectors[w] </span><span style="color:#cba6f7;">for</span><span style="color:#cdd6f4;"> w </span><span style="color:#cba6f7;">in</span><span style="color:#cdd6f4;"> words </span><span style="color:#cba6f7;">if</span><span style="color:#cdd6f4;"> w </span><span style="color:#cba6f7;">in</span><span style="color:#cdd6f4;"> vectors]</span>
<span style="color:#cdd6f4;">    </span><span style="color:#cba6f7;">return</span><span style="color:#cdd6f4;"> np.mean(vecs, axis=</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">) </span><span style="color:#cba6f7;">if</span><span style="color:#cdd6f4;"> vecs </span><span style="color:#cba6f7;">else</span><span style="color:#cdd6f4;"> np.zeros(</span><span style="color:#89dceb;">4</span><span style="color:#cdd6f4;">)</span>

<span style="color:#cdd6f4;">emb_vecs = np.array([sentence_to_embedding(doc, word_vectors) </span><span style="color:#cba6f7;">for</span><span style="color:#cdd6f4;"> doc </span><span style="color:#cba6f7;">in</span><span style="color:#cdd6f4;"> corpus])</span>
<span style="color:#cdd6f4;">sim_emb   = cosine_similarity([emb_vecs[target[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">]]], [emb_vecs[target[</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">]]])[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">][</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">]</span>

<span style="color:#6c7086;"># ─────────────────────────────────────────</span>
<span style="color:#6c7086;"># 최종 유사도 비교 요약</span>
<span style="color:#6c7086;"># ─────────────────────────────────────────</span>
<span style="color:#cdd6f4;">results = {</span><span style="color:#a6e3a1;">"BoW"</span><span style="color:#cdd6f4;">: sim_bow, </span><span style="color:#a6e3a1;">"TF-IDF"</span><span style="color:#cdd6f4;">: sim_tfidf, </span><span style="color:#a6e3a1;">"단어 임베딩"</span><span style="color:#cdd6f4;">: sim_emb}</span>
<span style="color:#cba6f7;">for</span><span style="color:#cdd6f4;"> method, score </span><span style="color:#cba6f7;">in</span><span style="color:#cdd6f4;"> results.items():</span>
<span style="color:#cdd6f4;">    bar = </span><span style="color:#a6e3a1;">"█"</span><span style="color:#cdd6f4;"> * int(score * </span><span style="color:#89dceb;">20</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cdd6f4;">    </span><span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"  {method:<12} {score:.4f}  {bar}"</span><span style="color:#cdd6f4;">)</span></div>
</div>

<!-- 출력 결과 -->
<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">출력 결과 예시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#a6e3a1;">📊 문서1 ↔ 문서3 유사도 최종 비교</span>
<span style="color:#cdd6f4;">  BoW          0.6667  █████████████</span>
<span style="color:#cdd6f4;">  TF-IDF       0.6667  █████████████</span>
<span style="color:#ff5f57; font-weight:900;">  단어 임베딩  0.9814  ███████████████████</span></div>
</div>

<!-- 유사도 시각화 카드 -->
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-top: 14px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 12px; text-align:center;">
    <div style="font-size:11px; font-weight:900; color:#475569; margin-bottom:6px;">BoW</div>
    <div style="font-size:24px; font-weight:900; color:#475569; margin-bottom:6px;">0.6667</div>
    <div style="background:#e2e8f0; border-radius:999px; height:6px; overflow:hidden;">
      <div style="background:#475569; height:100%; width:67%; border-radius:999px;"></div>
    </div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 12px; text-align:center;">
    <div style="font-size:11px; font-weight:900; color:#FF6B00; margin-bottom:6px;">TF-IDF</div>
    <div style="font-size:24px; font-weight:900; color:#FF6B00; margin-bottom:6px;">0.6667</div>
    <div style="background:#ffd0b0; border-radius:999px; height:6px; overflow:hidden;">
      <div style="background:#FF6B00; height:100%; width:67%; border-radius:999px;"></div>
    </div>
  </div>
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 12px; text-align:center;">
    <div style="font-size:11px; font-weight:900; color:#1681c4; margin-bottom:6px;">단어 임베딩</div>
    <div style="font-size:24px; font-weight:900; color:#1681c4; margin-bottom:6px;">0.9814</div>
    <div style="background:#c2e4ff; border-radius:999px; height:6px; overflow:hidden;">
      <div style="background:#1681c4; height:100%; width:98%; border-radius:999px;"></div>
    </div>
  </div>
</div>

</div>

<br>

<!-- 단계별 설명 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔍 코드 단계별 설명
</h2>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<!-- STEP 1 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 1</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">BoW / TF-IDF 비교</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#c3e88d; margin-bottom:12px; line-height:1.9;">
    bow_vec  = CountVectorizer()<br>
    tfidf_vec = TfidfVectorizer()
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:13px; color:#334155; line-height:1.7;">
      둘 다 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 5px; border-radius:4px;">fit_transform(corpus)</code>으로 동일하게 사용합니다.<br>
      BoW는 <b>정수</b>, TF-IDF는 <b>0~1 사이 소수</b>로 채워집니다.
    </div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:13px; color:#334155; line-height:1.7;">
      이 예시에서는 단어 분포가 단순해 두 유사도가 같게 나옵니다.<br>
      실제 대규모 문서에서는 TF-IDF가 훨씬 의미 있는 차이를 만듭니다.
    </div>
  </div>
</div>

<!-- STEP 2 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 2</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">단어 임베딩으로 문장 벡터 만들기</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#c3e88d; margin-bottom:12px; line-height:1.9;">
    def sentence_to_embedding(sentence, vectors):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;words = sentence.split()<br>
    &nbsp;&nbsp;&nbsp;&nbsp;vecs  = [vectors[w] for w in words if w in vectors]<br>
    &nbsp;&nbsp;&nbsp;&nbsp;return np.mean(vecs, axis=0)
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:13px; color:#334155; line-height:1.7;">
      각 단어 벡터들의 <b style="color:#1681c4;">평균</b>으로 문장 벡터를 만드는 가장 단순한 방식입니다.
    </div>
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:13px; color:#334155; line-height:1.7;">
      실제 문장 임베딩(BERT 등)은 단순 평균이 아닌 훨씬 <b style="color:#1681c4;">정교한 방식</b>을 사용합니다.
    </div>
  </div>
</div>

<!-- STEP 3 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 3</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">유사도 비교 결과 해석</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:11px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">BoW          0.6667</span>  → <span style="color:#cdd6f4;">"밥을", "먹었다" 단어 겹침만 반영</span>
<span style="color:#6c7086;">TF-IDF       0.6667</span>  → <span style="color:#cdd6f4;">이 예시에서는 BoW와 동일 (단어 분포 단순)</span>
<span style="color:#a6e3a1;">단어 임베딩  0.9814</span>  → <span style="color:#ff5f57; font-weight:900;">"밥을 먹었다" 의미 유사성이 더 크게 반영</span></div>
  <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    <span style="color:#FF6B00; font-weight:900;">💡 단어 임베딩에서 유사도가 더 높게 나오는 이유</span><br>
    "나는"과 "고양이가"는 다른 단어지만 문장 구조상 비슷한 역할(주어)을 합니다.<br>
    "밥을 먹었다" 조합이 의미적으로 매우 유사하게 학습되어 있기 때문입니다.
  </div>
</div>

</div>
</div>

<br>

<!-- 어떤 방법이 가장 좋은가 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎯 어떤 방법이 "가장 좋은가"?
</h2>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; margin-bottom: 16px;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 정답은 없습니다. <b>상황에 따라 다릅니다.</b>
</div>

<div style="display: grid; gap: 8px;">

  <div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:11px 14px;">
    <div style="font-size:13px; color:#475569; white-space:nowrap;">📌 빠른 구현이 필요할 때</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">BoW / TF-IDF</div>
  </div>

  <div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:11px 14px;">
    <div style="font-size:13px; color:#475569; white-space:nowrap;">📌 단어 사전이 작고 데이터가 많을 때</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">TF-IDF</div>
  </div>

  <div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px;">
    <div style="font-size:13px; color:#475569; white-space:nowrap;">📌 단어 수준 의미 비교가 필요할 때</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">단어 임베딩</div>
  </div>

  <div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px;">
    <div style="font-size:13px; color:#475569; white-space:nowrap;">📌 문장 전체 이해가 필요할 때</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">문장 임베딩</div>
  </div>

  <div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px;">
    <div style="font-size:13px; color:#475569; white-space:nowrap;">📌 리소스가 제한적일 때</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">TF-IDF 또는 경량 임베딩</div>
  </div>

  <div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#0f172a; border-radius:10px; padding:11px 14px;">
    <div style="font-size:13px; color:#a6e3a1; white-space:nowrap;">📌 높은 정확도가 최우선일 때</div>
    <div style="background:#0d0d1a; color:#c3e88d; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">문장 임베딩 (BERT 계열)</div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡 하이브리드 방식</span><br>
현업에서는 TF-IDF와 BERT를 함께 쓰거나,<br>
빠른 필터링에 TF-IDF → 정교한 순위 결정에 BERT를 사용하는 방식도 많습니다.
</div>

</div>

<br>

<!-- 챕터 3 전체 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 20px 22px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="font-size: 16px; font-weight: 900; margin-bottom: 14px;">
<span style="color: #FF6B00; font-size: 20px;">⚡</span> 챕터 3 전체 핵심 정리
</div>

<div style="display: grid; gap: 8px; margin-bottom: 16px;">
  <div style="display:grid; grid-template-columns:140px 1fr; gap:10px; align-items:center;">
    <div style="background:#0f172a; color:#c3e88d; padding:8px 12px; border-radius:8px; font-size:12px; font-weight:900; text-align:center;">원-핫 인코딩</div>
    <div style="background:#fff; border-left:4px solid #FF6B00; padding:9px 14px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.6;">해당 단어 위치만 1, 나머지는 0</div>
  </div>
  <div style="display:grid; grid-template-columns:140px 1fr; gap:10px; align-items:center;">
    <div style="background:#FF6B00; color:#fff; padding:8px 12px; border-radius:8px; font-size:12px; font-weight:900; text-align:center;">BoW</div>
    <div style="background:#fff; border-left:4px solid #FF6B00; padding:9px 14px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.6;">단어 등장 횟수를 그대로 세어 벡터로</div>
  </div>
  <div style="display:grid; grid-template-columns:140px 1fr; gap:10px; align-items:center;">
    <div style="background:#FF6B00; color:#fff; padding:8px 12px; border-radius:8px; font-size:12px; font-weight:900; text-align:center;">TF-IDF</div>
    <div style="background:#fff; border-left:4px solid #FF6B00; padding:9px 14px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.6;">빈도 × 희귀도 — 이 문서에서만 특별한 단어를 강조</div>
  </div>
  <div style="display:grid; grid-template-columns:140px 1fr; gap:10px; align-items:center;">
    <div style="background:#1681c4; color:#fff; padding:8px 12px; border-radius:8px; font-size:12px; font-weight:900; text-align:center;">단어 임베딩</div>
    <div style="background:#fff; border-left:4px solid #1681c4; padding:9px 14px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.6;">의미가 담긴 밀집 벡터 — 비슷한 단어끼리 가까이</div>
  </div>
  <div style="display:grid; grid-template-columns:140px 1fr; gap:10px; align-items:center;">
    <div style="background:#0f172a; color:#c3e88d; padding:8px 12px; border-radius:8px; font-size:12px; font-weight:900; text-align:center;">문장 임베딩</div>
    <div style="background:#fff; border-left:4px solid #0f172a; padding:9px 14px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.6;">문장 전체 + 문맥까지 하나의 벡터로</div>
  </div>
</div>

<div style="background:#fff; border-radius:10px; padding:14px 16px; font-size:14px; color:#334155; line-height:1.9;">
텍스트 표현은 단순한 <b style="color:#FF6B00;">0/1</b>에서 시작해서, 점점 더 언어의 <b style="color:#1681c4;">의미와 문맥</b>을 담는 방향으로 발전해왔습니다.<br>
이 흐름을 이해하면 <b>NLP의 발전 방향 전체</b>가 보입니다.
</div>

</div>

</div>