<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
문장 임베딩 (Sentence Embedding)
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 7px; border-radius:6px; font-weight:900;">sentence-transformers</code>로 문장 유사도를 직접 계산하고, 단어 임베딩과 비교합니다.
</p>

</div>

<br>

<!-- 실습 코드 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💻 코드로 맛보기 — 문장 유사도 계산
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">sentence-transformers</code> 라이브러리를 이용하면 간단하게 사용할 수 있습니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 sentence_embedding.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      문장 임베딩
    </div>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.9; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;"># 설치: pip install sentence-transformers</span>
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">sentence_transformers</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">SentenceTransformer</span>
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">sklearn.metrics.pairwise</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">cosine_similarity</span>
<span style="color:#cba6f7;">import</span> <span style="color:#89dceb;">numpy</span> <span style="color:#cba6f7;">as</span> <span style="color:#cdd6f4;">np</span>

<span style="color:#6c7086;"># ① 사전 학습된 다국어 문장 임베딩 모델 불러오기</span>
<span style="color:#cdd6f4;">model = SentenceTransformer(</span><span style="color:#a6e3a1;">'paraphrase-multilingual-MiniLM-L12-v2'</span><span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># ② 비교할 문장들</span>
<span style="color:#cdd6f4;">sentences = [</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"나는 고양이를 좋아한다"</span><span style="color:#cdd6f4;">,      </span><span style="color:#6c7086;"># 문장 A</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"나는 강아지를 좋아한다"</span><span style="color:#cdd6f4;">,      </span><span style="color:#6c7086;"># 문장 B  (A와 유사)</span>
<span style="color:#cdd6f4;">    </span><span style="color:#a6e3a1;">"오늘 날씨가 매우 맑다"</span><span style="color:#cdd6f4;">,       </span><span style="color:#6c7086;"># 문장 C  (A와 다름)</span>
<span style="color:#cdd6f4;">]</span>

<span style="color:#6c7086;"># ③ 문장을 벡터로 변환 (임베딩)</span>
<span style="color:#cdd6f4;">embeddings = model.encode(sentences)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"벡터 크기: {embeddings.shape}"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#6c7086;"># 출력: (3, 384) → 3개 문장, 각각 384차원 벡터</span>

<span style="color:#6c7086;"># ④ 문장 간 코사인 유사도 계산</span>
<span style="color:#cdd6f4;">sim_AB = cosine_similarity([embeddings[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">]], [embeddings[</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">]])[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">][</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">]</span>
<span style="color:#cdd6f4;">sim_AC = cosine_similarity([embeddings[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">]], [embeddings[</span><span style="color:#89dceb;">2</span><span style="color:#cdd6f4;">]])[</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">][</span><span style="color:#89dceb;">0</span><span style="color:#cdd6f4;">]</span>

<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"\n[문장 유사도 비교]"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"문장 A: '{sentences[0]}'"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"문장 B: '{sentences[1]}'"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"문장 C: '{sentences[2]}'"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"\nA ↔ B 유사도: {sim_AB:.4f}  ← 고양이/강아지, 같은 패턴"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"A ↔ C 유사도: {sim_AC:.4f}  ← 완전히 다른 주제"</span><span style="color:#cdd6f4;">)</span></div>
</div>

<!-- 출력 결과 -->
<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">출력 결과 예시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">벡터 크기: (3, 384)</span>

<span style="color:#a6e3a1;">[문장 유사도 비교]</span>
<span style="color:#cdd6f4;">문장 A: '나는 고양이를 좋아한다'</span>
<span style="color:#cdd6f4;">문장 B: '나는 강아지를 좋아한다'</span>
<span style="color:#cdd6f4;">문장 C: '오늘 날씨가 매우 맑다'</span>

<span style="color:#a6e3a1;">A ↔ B 유사도: 0.8923</span>  <span style="color:#6c7086;">← 고양이/강아지, 같은 패턴</span>
<span style="color:#ff5f57;">A ↔ C 유사도: 0.1247</span>  <span style="color:#6c7086;">← 완전히 다른 주제</span></div>
</div>

<!-- 유사도 비교 시각화 -->
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 14px;">
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:6px;">A ↔ B (고양이 vs 강아지)</div>
    <div style="font-size:28px; font-weight:900; color:#1681c4; margin-bottom:4px;">0.8923</div>
    <div style="background:#c2e4ff; border-radius:999px; height:8px; margin-top:8px; overflow:hidden;">
      <div style="background:#1681c4; height:100%; width:89%; border-radius:999px;"></div>
    </div>
    <div style="font-size:12px; color:#475569; margin-top:6px;">매우 유사한 문장</div>
  </div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:6px;">A ↔ C (고양이 vs 날씨)</div>
    <div style="font-size:28px; font-weight:900; color:#FF6B00; margin-bottom:4px;">0.1247</div>
    <div style="background:#ffd0b0; border-radius:999px; height:8px; margin-top:8px; overflow:hidden;">
      <div style="background:#FF6B00; height:100%; width:12%; border-radius:999px;"></div>
    </div>
    <div style="font-size:12px; color:#475569; margin-top:6px;">완전히 다른 문장</div>
  </div>
</div>

<div style="margin-top: 12px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> BoW나 TF-IDF로는 이런 유사도를 제대로 계산하기 어렵습니다.<br>
문장 임베딩은 <b style="color:#FF6B00;">실제 의미 기반</b>으로 유사도를 측정합니다.
</div>

</div>

<br>

<!-- 비교 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔍 단어 임베딩 vs 문장 임베딩 비교
</h2>

<div style="display: grid; gap: 8px; margin-top: 16px;">

  <div style="display:grid; grid-template-columns:110px 1fr 1fr; gap:8px;">
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">항목</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">단어 임베딩 (Word2Vec)</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">문장 임베딩 (BERT 등)</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 1fr; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; display:flex; align-items:center; justify-content:center; text-align:center;">표현 단위</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; display:flex; align-items:center;">단어 하나</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; color:#1681c4; font-weight:900; display:flex; align-items:center;">문장 전체</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 1fr; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; display:flex; align-items:center; justify-content:center; text-align:center;">문맥 반영</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; display:flex; align-items:center;">❌ 항상 같은 벡터</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; color:#1681c4; display:flex; align-items:center;">✅ 문맥에 따라 다른 벡터</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 1fr; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; display:flex; align-items:center; justify-content:center; text-align:center;">동음이의어</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; display:flex; align-items:center;">❌ 구분 불가</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; color:#1681c4; display:flex; align-items:center;">✅ 문맥으로 구분 가능</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 1fr; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; display:flex; align-items:center; justify-content:center; text-align:center;">벡터 크기</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155; display:flex; align-items:center;">50~300차원</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155; display:flex; align-items:center;">768~1024차원</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 1fr; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; display:flex; align-items:center; justify-content:center; text-align:center;">계산 비용</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; color:#1681c4; font-weight:900; display:flex; align-items:center;">✅ 낮음</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; display:flex; align-items:center;">🔺 높음</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 1fr; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; display:flex; align-items:center; justify-content:center; text-align:center;">활용 예</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155; display:flex; align-items:center;">유사 단어 검색</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155; display:flex; align-items:center;">문서 분류, 질의응답, 번역</div>
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
    <b style="color:#FF6B00;">문장 임베딩</b>은 문장 전체를 <b style="color:#FF6B00;">하나의 벡터</b>로 표현하는 방법입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    단어 임베딩과 달리, <b style="color:#FF6B00;">문장 전체 문맥</b>을 보고 각 단어의 의미를 결정합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    "배"(신체/선박/과일)처럼 <b style="color:#FF6B00;">동음이의어도 문맥에 따라 다른 벡터</b>로 표현됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    대표 모델은 <b style="color:#FF6B00;">BERT</b>이며, ChatGPT·Claude 같은 최신 AI의 기반 기술입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    계산 비용이 높지만, <b style="color:#FF6B00;">가장 풍부하고 정확한 텍스트 표현</b>을 제공합니다.
  </div>
</div>

</div>

</div>