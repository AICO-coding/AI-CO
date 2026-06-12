<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Bag of Words (BoW)
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 7px; border-radius:6px; font-weight:900;">CountVectorizer</code>를 활용해 BoW를 직접 구현하고, 코사인 유사도까지 계산합니다.
</p>

</div>

<br>

<!-- 실습 코드 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💻 실습 코드
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
아래 코드를 보고 각 단계가 어떤 역할을 하는지 확인해보세요!
</p>

<!-- 코드 블록 -->
<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 bow_countvectorizer.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      Bag of Words
    </div>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.9; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">sklearn.feature_extraction.text</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">CountVectorizer</span>
<span style="color:#cba6f7;">import</span> <span style="color:#89dceb;">pandas</span> <span style="color:#cba6f7;">as</span> <span style="color:#cdd6f4;">pd</span>

<span style="color:#6c7086;"># ① 예시 문서 준비</span>
<span style="color:#cdd6f4;">corpus = [</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"나는 밥을 먹었다"</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"나는 물을 마셨다"</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"고양이가 밥을 먹었다"</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"고양이가 물을 마셨다"</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">]</span>

<span style="color:#6c7086;"># ② CountVectorizer로 BoW 행렬 생성</span>
<span style="color:#6c7086;">#    CountVectorizer: 텍스트를 단어 빈도 벡터로 변환하는 도구</span>
<span style="color:#cdd6f4;">vectorizer = CountVectorizer()</span>
<span style="color:#cdd6f4;">bow_matrix = vectorizer.fit_transform(corpus)</span>

<span style="color:#6c7086;"># ③ 단어 사전 확인 (알파벳/가나다 순으로 정렬됨)</span>
<span style="color:#cdd6f4;">vocab = vectorizer.get_feature_names_out()</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"단어 사전:"</span><span style="color:#cdd6f4;">, vocab)</span>
<span style="color:#6c7086;"># 출력: ['고양이가' '나는' '마셨다' '먹었다' '밥을' '물을']</span>

<span style="color:#6c7086;"># ④ 결과를 보기 좋은 표(DataFrame)로 출력</span>
<span style="color:#cdd6f4;">bow_df = pd.DataFrame(</span>
<span style="color:#cdd6f4;">    bow_matrix.toarray(),    </span><span style="color:#6c7086;"># 희소 행렬 → 일반 배열로 변환</span>
<span style="color:#cdd6f4;">    columns=vocab,</span>
<span style="color:#cdd6f4;">    index=[</span><span style="color:#a6e3a1;">f"문서{i+1}"</span><span style="color:#cdd6f4;"> </span><span style="color:#cba6f7;">for</span><span style="color:#cdd6f4;"> i </span><span style="color:#cba6f7;">in</span><span style="color:#cdd6f4;"> range(len(corpus))]</span>
<span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"\n[BoW 행렬]"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(bow_df)</span>

<span style="color:#6c7086;"># ⑤ 특정 단어의 인덱스 확인</span>
<span style="color:#cdd6f4;">target_word = </span><span style="color:#a6e3a1;">"밥을"</span>
<span style="color:#cdd6f4;">word_idx = vectorizer.vocabulary_.get(target_word)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"\n'{target_word}'의 인덱스: {word_idx}"</span><span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># ⑥ 특정 문서의 벡터 출력</span>
<span style="color:#cdd6f4;">doc_idx = </span><span style="color:#89dceb;">0</span>  <span style="color:#6c7086;"># 문서 1</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"문서{doc_idx+1}의 BoW 벡터: {bow_matrix.toarray()[doc_idx].tolist()}"</span><span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># ⑦ 두 문서의 유사도 계산 (코사인 유사도)</span>
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">sklearn.metrics.pairwise</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">cosine_similarity</span>

<span style="color:#cdd6f4;">sim_1_3 = cosine_similarity(bow_matrix[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">], bow_matrix[</span><span style="color:#89dceb;">2</span><span style="color:#cdd6f4;">])</span>
<span style="color:#cdd6f4;">sim_1_2 = cosine_similarity(bow_matrix[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">], bow_matrix[</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">])</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"\n문서1 ↔ 문서3 유사도: {sim_1_3[0][0]:.4f}"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"문서1 ↔ 문서2 유사도: {sim_1_2[0][0]:.4f}"</span><span style="color:#cdd6f4;">)</span></div>
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
<span style="color:#6c7086;">단어 사전: ['고양이가' '나는' '마셨다' '먹었다' '밥을' '물을']</span>

<span style="color:#a6e3a1;">[BoW 행렬]</span>
<span style="color:#cdd6f4;">       고양이가  나는  마셨다  먹었다  밥을  물을</span>
<span style="color:#cdd6f4;">문서1        0     1       0       1     1     0</span>
<span style="color:#cdd6f4;">문서2        0     1       1       0     0     1</span>
<span style="color:#cdd6f4;">문서3        1     0       0       1     1     0</span>
<span style="color:#cdd6f4;">문서4        1     0       1       0     0     1</span>

<span style="color:#6c7086;">'밥을'의 인덱스: 4</span>
<span style="color:#6c7086;">문서1의 BoW 벡터: [0, 1, 0, 1, 1, 0]</span>

<span style="color:#a6e3a1;">문서1 ↔ 문서3 유사도: 0.6667</span>
<span style="color:#ff5f57;">문서1 ↔ 문서2 유사도: 0.3333</span></div>
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
    <div style="font-size:15px; font-weight:900; color:#0f172a;">CountVectorizer 생성 및 학습</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#c3e88d; margin-bottom:12px; line-height:1.9;">
    vectorizer = CountVectorizer()<br>
    bow_matrix = vectorizer.fit_transform(corpus)
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; margin-bottom:12px;">
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">fit</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">데이터를 보고 단어 사전을 만듭니다.</div>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">transform</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">학습한 사전으로 데이터를 벡터로 변환합니다.</div>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">fit_transform</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">fit + transform을 <b>한 번에</b> 처리합니다.</div>
    </div>
  </div>
  <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    결과는 <b style="color:#FF6B00;">희소 행렬(Sparse Matrix)</b>로 반환됩니다. (0이 많아서 효율적으로 저장)
  </div>
</div>

<!-- STEP 2 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 2</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">단어 사전 확인</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#c3e88d; margin-bottom:12px;">
    vocab = vectorizer.get_feature_names_out()
  </div>
  <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    학습된 단어 사전의 단어 목록을 가져옵니다.<br>
    <b style="color:#1681c4;">가나다 순으로 자동 정렬</b>되며, 이 순서가 곧 벡터의 각 위치(인덱스)에 해당합니다.
  </div>
</div>

<!-- STEP 3 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 3</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">희소 행렬 → 일반 배열 변환</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#c3e88d; margin-bottom:12px;">
    bow_matrix.toarray()
  </div>
  <div style="background-color: #1e1e2e; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:2; margin-bottom:10px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">희소 행렬 (내부 저장)</span>  →  <span style="color:#a6e3a1;">toarray()</span>  →  <span style="color:#89dceb;">일반 배열 (눈으로 보기 편함)</span>
<span style="color:#6c7086;">[0이 많아 압축 저장]</span>   →              →  <span style="color:#cdd6f4;">[[0,1,0,1,1,0], ...]</span></div>
  <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">.toarray()</code>를 사용하면 우리가 익숙한 <b>2D 배열</b>로 변환됩니다.
  </div>
</div>

<!-- STEP 4 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 4</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">코사인 유사도로 문서 비교</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#c3e88d; margin-bottom:12px; line-height:1.9;">
    from sklearn.metrics.pairwise import cosine_similarity<br>
    sim = cosine_similarity(bow_matrix[0], bow_matrix[2])
  </div>
  <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7; margin-bottom:10px;">
    <b style="color:#1681c4;">코사인 유사도</b>: 두 벡터가 가리키는 방향이 얼마나 비슷한지 측정합니다.<br>
    값의 범위는 <b>0 ~ 1</b>이며, 1에 가까울수록 두 문서가 유사합니다.
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; text-align:center;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">문서1 ↔ 문서3</div>
      <div style="font-size:22px; font-weight:900; color:#1681c4;">0.6667</div>
      <div style="font-size:12px; color:#475569; margin-top:4px;">꽤 비슷함 (밥을, 먹었다 공유)</div>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; text-align:center;">
      <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">문서1 ↔ 문서2</div>
      <div style="font-size:22px; font-weight:900; color:#FF6B00;">0.3333</div>
      <div style="font-size:12px; color:#475569; margin-top:4px;">덜 비슷함 (나는만 공유)</div>
    </div>
  </div>
</div>

</div>
</div>

</div>