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
TF-IDF의
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">세 가지 한계</span>
와 실전에서 자주 쓰는 파라미터를 정리합니다.
</p>

</div>

<br>

<!-- 한계 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
⚠️ TF-IDF의 한계
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
TF-IDF는 BoW보다 발전했지만 여전히 한계가 있습니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<!-- 한계 1 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 1. 단어 순서를 무시한다</div>
  <p style="margin: 0 0 12px 0; font-size:14px; color:#475569; line-height:1.7;">
    BoW와 동일하게, 단어가 문장 어디에 있는지는 반영하지 않습니다.
  </p>
  <div style="background:#1e1e2e; border-radius:10px; padding:11px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"나는 고양이를 좋아한다"</span>  <span style="color:#ff5f57;">=</span>  <span style="color:#a6e3a1;">"좋아한다 고양이를 나는"</span>
→ <span style="color:#ff5f57;">TF-IDF 벡터가 동일하게 나옵니다.</span></div>
</div>

<!-- 한계 2 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 2. 단어 의미를 모른다</div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.7;">
      <b style="color:#FF6B00;">"기쁘다"</b>와 <b style="color:#FF6B00;">"행복하다"</b><br>
      → 비슷한 의미지만 <b>완전히 다른 단어</b>로 취급
    </div>
    <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.7;">
      <b style="color:#FF6B00;">"배"(과일)</b> vs <b style="color:#FF6B00;">"배"(신체)</b><br>
      → 같은 단어지만 다른 의미 <b>구분 불가</b>
    </div>
  </div>
</div>

<!-- 한계 3 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 3. 희소 벡터 문제</div>
  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.7; margin-bottom:12px;">
    단어 사전 크기만큼의 긴 벡터에 <b style="color:#FF6B00;">대부분 0이 채워집니다.</b>
  </div>
  <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    <span style="color:#FF6B00; font-weight:900;">💡</span> 이 한계들을 해결하기 위해 다음에 배울 <b style="color:#FF6B00;">단어 임베딩(Word Embedding)</b>이 등장합니다!
  </div>
</div>

</div>
</div>

<br>

<!-- 파라미터 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 TF-IDF 주요 파라미터
</h2>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">TfidfVectorizer 파라미터 예시</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#cdd6f4;">tfidf_vectorizer = TfidfVectorizer(</span>
<span style="color:#cdd6f4;">    max_features=</span><span style="color:#89dceb;">1000</span><span style="color:#cdd6f4;">,       </span><span style="color:#6c7086;"># 상위 1000개 단어만 사용</span>
<span style="color:#cdd6f4;">    min_df=</span><span style="color:#89dceb;">2</span><span style="color:#cdd6f4;">,                </span><span style="color:#6c7086;"># 최소 2개 문서에 등장한 단어만 포함</span>
<span style="color:#cdd6f4;">    max_df=</span><span style="color:#89dceb;">0.9</span><span style="color:#cdd6f4;">,              </span><span style="color:#6c7086;"># 90% 이상 문서에 등장하는 단어 제외</span>
<span style="color:#cdd6f4;">    sublinear_tf=</span><span style="color:#89dceb;">True</span><span style="color:#cdd6f4;">,       </span><span style="color:#6c7086;"># TF에 log 적용 → 빈도 폭발 방지</span>
<span style="color:#cdd6f4;">    ngram_range=(</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">, </span><span style="color:#89dceb;">2</span><span style="color:#cdd6f4;">),      </span><span style="color:#6c7086;"># 단어 1개 + 연속 2개 단어쌍 포함</span>
<span style="color:#cdd6f4;">)</span></div>
</div>

<div style="display: grid; gap: 10px;">

  <div style="display:grid; grid-template-columns:150px 1fr; gap:10px; align-items:center;">
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">파라미터</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">역할</div>
  </div>

  <div style="display:grid; grid-template-columns:150px 1fr; gap:10px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-family:Consolas, monospace; font-size:12px; font-weight:900; color:#1681c4; text-align:center;">max_features</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 14px; border-radius:10px; font-size:13px; color:#334155;">너무 많은 단어 → 상위 N개만 사용</div>
  </div>

  <div style="display:grid; grid-template-columns:150px 1fr; gap:10px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-family:Consolas, monospace; font-size:12px; font-weight:900; color:#1681c4; text-align:center;">min_df</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 14px; border-radius:10px; font-size:13px; color:#334155;">희귀 오타·신조어 제거</div>
  </div>

  <div style="display:grid; grid-template-columns:150px 1fr; gap:10px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-family:Consolas, monospace; font-size:12px; font-weight:900; color:#1681c4; text-align:center;">max_df</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 14px; border-radius:10px; font-size:13px; color:#334155;">너무 흔한 단어 자동 제거</div>
  </div>

  <div style="display:grid; grid-template-columns:150px 1fr; gap:10px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-family:Consolas, monospace; font-size:12px; font-weight:900; color:#1681c4; text-align:center;">sublinear_tf</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 14px; border-radius:10px; font-size:13px; color:#334155;">단어가 10번 나와도 TF를 10이 아닌 log(10)으로 계산</div>
  </div>

  <div style="display:grid; grid-template-columns:150px 1fr; gap:10px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-family:Consolas, monospace; font-size:12px; font-weight:900; color:#1681c4; text-align:center;">ngram_range</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 14px; border-radius:10px; font-size:13px; color:#334155;">"인공 지능"처럼 연속 단어 묶음을 하나의 단위로 포함</div>
  </div>

</div>
</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;">
<span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리
</div>

<div style="display: grid; gap: 8px;">
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">TF-IDF = TF(문서 내 빈도) × IDF(전체 문서 희귀도)</b>로 단어 중요도를 계산합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    "모든 문서에 자주 등장하는 단어"는 <b style="color:#FF6B00;">자동으로 낮은 점수</b>를 받습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    "이 문서에만 특별히 자주 등장하는 단어"가 <b style="color:#FF6B00;">높은 점수</b>를 받습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    BoW보다 훨씬 <b style="color:#FF6B00;">의미 있는 단어 표현</b>이 가능하지만, 단어 순서와 의미는 여전히 모릅니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    문서 분류, 검색 엔진, 키워드 추출 등 <b style="color:#FF6B00;">실무에서도 활발히 사용</b>됩니다.
  </div>
</div>

</div>

</div>