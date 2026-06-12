<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
TF-IDF
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 7px; border-radius:6px; font-weight:900;">TfidfVectorizer</code>로 TF-IDF를 구현하고, BoW와 결과를 비교합니다.
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

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 tfidf_vectorizer.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      TF-IDF
    </div>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.9; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">sklearn.feature_extraction.text</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">TfidfVectorizer</span>
<span style="color:#cba6f7;">import</span> <span style="color:#89dceb;">pandas</span> <span style="color:#cba6f7;">as</span> <span style="color:#cdd6f4;">pd</span>

<span style="color:#6c7086;"># ① 예시 문서 준비</span>
<span style="color:#cdd6f4;">corpus = [</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"나는 밥을 먹었다"</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"나는 물을 마셨다"</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"고양이가 밥을 먹었다"</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"고양이가 물을 마셨다"</span><span style="color:#cdd6f4;">,</span>
<span style="color:#cdd6f4;">]</span>

<span style="color:#6c7086;"># ② TfidfVectorizer로 TF-IDF 행렬 생성</span>
<span style="color:#6c7086;">#    BoW의 CountVectorizer와 사용법이 거의 동일합니다.</span>
<span style="color:#cdd6f4;">tfidf_vectorizer = TfidfVectorizer()</span>
<span style="color:#cdd6f4;">tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)</span>

<span style="color:#6c7086;"># ③ 단어 사전 확인</span>
<span style="color:#cdd6f4;">vocab = tfidf_vectorizer.get_feature_names_out()</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"단어 사전:"</span><span style="color:#cdd6f4;">, vocab)</span>

<span style="color:#6c7086;"># ④ TF-IDF 행렬을 보기 좋은 표(DataFrame)로 출력</span>
<span style="color:#cdd6f4;">tfidf_df = pd.DataFrame(</span>
<span style="color:#cdd6f4;">    tfidf_matrix.toarray().round(</span><span style="color:#89dceb;">3</span><span style="color:#cdd6f4;">),    </span><span style="color:#6c7086;"># 소수점 3자리까지 반올림</span>
<span style="color:#cdd6f4;">    columns=vocab,</span>
<span style="color:#cdd6f4;">    index=[</span><span style="color:#a6e3a1;">f"문서{i+1}"</span><span style="color:#cdd6f4;"> </span><span style="color:#cba6f7;">for</span><span style="color:#cdd6f4;"> i </span><span style="color:#cba6f7;">in</span><span style="color:#cdd6f4;"> range(len(corpus))]</span>
<span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"\n[TF-IDF 행렬]"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(tfidf_df)</span>

<span style="color:#6c7086;"># ⑤ BoW 행렬과 나란히 비교</span>
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">sklearn.feature_extraction.text</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">CountVectorizer</span>

<span style="color:#cdd6f4;">bow_vectorizer = CountVectorizer()</span>
<span style="color:#cdd6f4;">bow_matrix = bow_vectorizer.fit_transform(corpus)</span>
<span style="color:#cdd6f4;">bow_df = pd.DataFrame(</span>
<span style="color:#cdd6f4;">    bow_matrix.toarray(),</span>
<span style="color:#cdd6f4;">    columns=bow_vectorizer.get_feature_names_out(),</span>
<span style="color:#cdd6f4;">    index=[</span><span style="color:#a6e3a1;">f"문서{i+1}"</span><span style="color:#cdd6f4;"> </span><span style="color:#cba6f7;">for</span><span style="color:#cdd6f4;"> i </span><span style="color:#cba6f7;">in</span><span style="color:#cdd6f4;"> range(len(corpus))]</span>
<span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"\n[BoW 행렬 (비교용)]"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(bow_df)</span>

<span style="color:#6c7086;"># ⑥ 각 단어의 IDF 값 확인</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"\n[각 단어의 IDF 값]"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">for</span><span style="color:#cdd6f4;"> word, idf </span><span style="color:#cba6f7;">in</span><span style="color:#cdd6f4;"> zip(vocab, tfidf_vectorizer.idf_):</span>
<span style="color:#cdd6f4;">    </span><span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"  '{word}': IDF = {idf:.4f}"</span><span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># ⑦ 두 문서 간 코사인 유사도 비교</span>
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">sklearn.metrics.pairwise</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">cosine_similarity</span>

<span style="color:#cdd6f4;">sim_bow   = cosine_similarity(bow_matrix[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">], bow_matrix[</span><span style="color:#89dceb;">2</span><span style="color:#cdd6f4;">])</span>
<span style="color:#cdd6f4;">sim_tfidf = cosine_similarity(tfidf_matrix[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">], tfidf_matrix[</span><span style="color:#89dceb;">2</span><span style="color:#cdd6f4;">])</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"\n[문서1 ↔ 문서3 유사도 비교]"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"  BoW    유사도: {sim_bow[0][0]:.4f}"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"  TF-IDF 유사도: {sim_tfidf[0][0]:.4f}"</span><span style="color:#cdd6f4;">)</span></div>
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

<span style="color:#a6e3a1;">[TF-IDF 행렬]</span>
<span style="color:#cdd6f4;">       고양이가    나는  마셨다  먹었다    밥을    물을</span>
<span style="color:#cdd6f4;">문서1     0.000   0.579   0.000   0.579   0.579   0.000</span>
<span style="color:#cdd6f4;">문서2     0.000   0.579   0.579   0.000   0.000   0.579</span>
<span style="color:#cdd6f4;">문서3     0.579   0.000   0.000   0.579   0.579   0.000</span>
<span style="color:#cdd6f4;">문서4     0.579   0.000   0.579   0.000   0.000   0.579</span>

<span style="color:#6c7086;">[BoW 행렬 (비교용)]</span>
<span style="color:#6c7086;">       고양이가  나는  마셨다  먹었다  밥을  물을</span>
<span style="color:#6c7086;">문서1         0     1       0       1     1     0</span>
<span style="color:#6c7086;">문서2         0     1       1       0     0     1</span>
<span style="color:#6c7086;">문서3         1     0       0       1     1     0</span>
<span style="color:#6c7086;">문서4         1     0       1       0     0     1</span>

<span style="color:#a6e3a1;">[각 단어의 IDF 값]</span>
<span style="color:#cdd6f4;">  '고양이가': IDF = 1.2877</span>
<span style="color:#cdd6f4;">  '나는':    IDF = 1.2877</span>
<span style="color:#cdd6f4;">  '마셨다':  IDF = 1.2877</span>
<span style="color:#cdd6f4;">  '먹었다':  IDF = 1.2877</span>
<span style="color:#cdd6f4;">  '밥을':    IDF = 1.2877</span>
<span style="color:#cdd6f4;">  '물을':    IDF = 1.2877</span>

<span style="color:#a6e3a1;">[문서1 ↔ 문서3 유사도 비교]</span>
<span style="color:#cdd6f4;">  BoW    유사도: 0.6667</span>
<span style="color:#cdd6f4;">  TF-IDF 유사도: 0.6667</span></div>
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
    <div style="font-size:15px; font-weight:900; color:#0f172a;">TfidfVectorizer 생성 및 학습</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#c3e88d; margin-bottom:12px; line-height:1.9;">
    tfidf_vectorizer = TfidfVectorizer()<br>
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
  </div>
  <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7; margin-bottom:10px;">
    <b style="color:#1681c4;">CountVectorizer(BoW)</b>와 사용법이 거의 동일합니다.<br>
    내부에서 <b>TF × IDF 계산을 자동</b>으로 처리합니다.
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:13px; color:#334155; line-height:1.6;">
      <b style="color:#FF6B00;">fit</b>: 전체 문서를 보고 단어 사전과 <b>IDF 값</b>을 학습합니다.
    </div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:13px; color:#334155; line-height:1.6;">
      결과값은 <b style="color:#1681c4;">0~1 사이의 소수</b>로 이루어진 벡터입니다. (정규화 적용)
    </div>
  </div>
</div>

<!-- STEP 2 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 2</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">IDF 값 확인하기</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#c3e88d; margin-bottom:12px; line-height:1.9;">
    for word, idf in zip(vocab, tfidf_vectorizer.idf_):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;print(f"  '{word}': IDF = {idf:.4f}")
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 12px; text-align:center;">
      <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">IDF = 0.0</div>
      <div style="font-size:12px; color:#475569; line-height:1.6;">모든 문서에 등장<br>→ 중요도 없음</div>
    </div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 12px; text-align:center;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">IDF = 1.0 이상</div>
      <div style="font-size:12px; color:#475569; line-height:1.6;">일부 문서에만 등장<br>→ 어느 정도 중요</div>
    </div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 12px; text-align:center;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">IDF = 매우 큰 값</div>
      <div style="font-size:12px; color:#475569; line-height:1.6;">극소수 문서에만<br>→ 매우 희귀한 단어</div>
    </div>
  </div>
</div>

<!-- STEP 3 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 3</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">BoW vs TF-IDF 비교 포인트</div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
    <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:10px; padding:12px 14px;">
      <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:6px;">BoW 행렬</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 12px; font-family:Consolas, monospace; font-size:13px; color:#89dceb; margin-bottom:8px; text-align:center;">0, 1, 2 ...</div>
      <div style="font-size:13px; color:#475569; text-align:center;">단순 횟수 (정수)</div>
    </div>
    <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:10px; padding:12px 14px;">
      <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:6px;">TF-IDF 행렬</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 12px; font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; margin-bottom:8px; text-align:center;">0.0 ~ 1.0</div>
      <div style="font-size:13px; color:#475569; text-align:center;">중요도 가중치 (소수)</div>
    </div>
  </div>
  <div style="margin-top:10px; background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    문서 수가 많아지고 단어가 다양해질수록 두 방법의 차이가 <b style="color:#FF6B00;">확연해집니다.</b>
  </div>
</div>

</div>
</div>

</div>