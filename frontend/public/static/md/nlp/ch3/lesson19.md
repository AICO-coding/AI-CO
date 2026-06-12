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
문맥을 이해하는 원리와 대표 모델
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">BERT</span>
, 그리고 모델의 발전 흐름을 알아봅니다.
</p>

</div>

<br>

<!-- 문맥 이해 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧠 문맥을 이해한다는 것
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
문장 임베딩의 핵심은 <b style="color:#1681c4;">문맥(Context)을 이해</b>한다는 것입니다.<br>
같은 단어라도 문장에 따라 <b>다른 벡터</b>를 만들어냅니다.
</p>

<div style="display: grid; gap: 8px; margin-top: 14px;">

  <div style="display:grid; grid-template-columns:auto 1fr auto; gap:12px; align-items:center; background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:12px 16px;">
    <div style="background:#1681c4; color:#fff; padding:4px 10px; border-radius:6px; font-family:Consolas, monospace; font-size:13px; font-weight:900; white-space:nowrap;">"배"</div>
    <div style="font-size:13px; color:#334155; font-family:Consolas, monospace;">"나는 배가 고프다"</div>
    <div style="background:#0f172a; color:#89dceb; padding:5px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:12px; white-space:nowrap;">[0.3, -0.1, 0.8, ...]<br><span style="color:#6c7086; font-size:11px;">신체 기관 의미</span></div>
  </div>

  <div style="display:grid; grid-template-columns:auto 1fr auto; gap:12px; align-items:center; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px;">
    <div style="background:#475569; color:#fff; padding:4px 10px; border-radius:6px; font-family:Consolas, monospace; font-size:13px; font-weight:900; white-space:nowrap;">"배"</div>
    <div style="font-size:13px; color:#334155; font-family:Consolas, monospace;">"배를 타고 떠났다"</div>
    <div style="background:#0f172a; color:#89dceb; padding:5px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:12px; white-space:nowrap;">[-0.5, 0.7, 0.2, ...]<br><span style="color:#6c7086; font-size:11px;">선박 의미</span></div>
  </div>

  <div style="display:grid; grid-template-columns:auto 1fr auto; gap:12px; align-items:center; background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:12px 16px;">
    <div style="background:#FF6B00; color:#fff; padding:4px 10px; border-radius:6px; font-family:Consolas, monospace; font-size:13px; font-weight:900; white-space:nowrap;">"배"</div>
    <div style="font-size:13px; color:#334155; font-family:Consolas, monospace;">"배가 맛있게 익었다"</div>
    <div style="background:#0f172a; color:#89dceb; padding:5px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:12px; white-space:nowrap;">[0.6, 0.4, -0.3, ...]<br><span style="color:#6c7086; font-size:11px;">과일 의미</span></div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 같은 "배"지만 <b>문장 전체를 읽고 나서</b> 그 의미에 맞는 벡터를 할당합니다.
</div>

</div>

<br>

<!-- 번역가 비유 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📰 비유로 이해하기: 번역가의 독해 방식
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
단어 임베딩과 문장 임베딩의 차이를 번역가에 비유해봅시다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:10px;">❌ 단어 임베딩 방식 번역가</div>
    <div style="font-size:13px; color:#475569; line-height:1.8; margin-bottom:10px;">단어장을 펼쳐서 단어 하나씩 뜻을 찾아 번역합니다.</div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 12px; font-family:Consolas, monospace; font-size:12px; color:#cdd6f4; line-height:1.9;">
      <span style="color:#a6e3a1;">"I saw her duck."</span><br>
      <span style="color:#6c7086;">duck = 오리로 무조건 번역</span><br>
      <span style="color:#ff5f57;">→ 실제론 "몸을 숙이는 것"일 수도</span>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">✅ 문장 임베딩 방식 번역가</div>
    <div style="font-size:13px; color:#475569; line-height:1.8; margin-bottom:10px;">문장 전체를 먼저 읽고 문맥을 파악한 뒤 번역합니다.</div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 12px; font-family:Consolas, monospace; font-size:12px; color:#cdd6f4; line-height:1.9;">
      <span style="color:#a6e3a1;">"I saw her duck."</span><br>
      <span style="color:#6c7086;">앞뒤 상황 → duck의 의미 판단</span><br>
      <span style="color:#a6e3a1;">→ 훨씬 자연스럽고 정확한 번역</span>
    </div>
  </div>

</div>

</div>

<br>

<!-- BERT 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🏛️ 대표 모델: BERT
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
문장 임베딩의 가장 대표적인 모델은 <b>BERT</b> (2018, Google)입니다.
</p>

<div style="background:#0f172a; border-radius:12px; padding:12px 18px; font-family:Consolas, monospace; font-size:13px; color:#89dceb; margin: 14px 0; line-height: 1.8; text-align:center; letter-spacing:0.3px;">
  <span style="color:#ff5f57; font-weight:900;">B</span>idirectional
  <span style="color:#ff5f57; font-weight:900;">E</span>ncoder
  <span style="color:#ff5f57; font-weight:900;">R</span>epresentations from
  <span style="color:#ff5f57; font-weight:900;">T</span>ransformers
</div>

<div style="display: grid; gap: 14px; margin-top: 4px;">

<!-- 특징 1 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 12px; border-radius:999px; font-size:12px; font-weight:900; white-space:nowrap;">특징 1</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">양방향(Bidirectional) 문맥 이해</div>
  </div>
  <p style="margin:0 0 12px 0; font-size:14px; color:#475569; line-height:1.7;">기존 모델들은 문장을 왼쪽→오른쪽으로만 읽었습니다.<br>
  BERT는 <b style="color:#FF6B00;">양쪽 방향을 동시에</b> 읽고 문맥을 파악합니다.</p>
  <div style="background:#1e1e2e; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">기존 모델: </span><span style="color:#a6e3a1;">"나는 배가"</span> <span style="color:#ff5f57;">→</span> <span style="color:#6c7086;">다음 단어를 예측 (왼→오른쪽만)</span>

<span style="color:#6c7086;">BERT:  </span><span style="color:#a6e3a1;">"나는 <span style="color:#ff5f57; font-weight:900;">[MASK]</span>가 고프다"</span>
       <span style="color:#89dceb;">← 왼쪽("나는")과 오른쪽("고프다")을 동시에 보고 [MASK] 예측</span>
       <span style="color:#a6e3a1;">→ "배"가 신체 기관임을 맥락으로 파악 가능</span></div>
</div>

<!-- 특징 2 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 12px; border-radius:999px; font-size:12px; font-weight:900; white-space:nowrap;">특징 2</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">대규모 사전 학습 (Pre-training)</div>
  </div>
  <p style="margin:0 0 12px 0; font-size:14px; color:#475569; line-height:1.7;">BERT는 위키피디아 전체, 수십억 개의 문장으로 <b style="color:#1681c4;">미리 학습</b>합니다.<br>
  이미 언어의 구조와 의미를 깊이 이해한 상태입니다.</p>
  <div style="display:grid; grid-template-columns:1fr auto 1fr; gap:10px; align-items:center;">
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 14px; font-size:13px; color:#334155; line-height:1.7; text-align:center;">
      <b style="color:#1681c4;">사전 학습</b><br>
      <span style="font-size:12px; color:#475569;">(Pre-training)</span><br>
      대규모 텍스트로<br>언어 이해
    </div>
    <div style="font-size:22px; color:#1681c4; font-weight:900; text-align:center;">→</div>
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 14px; font-size:13px; color:#334155; line-height:1.7; text-align:center;">
      <b style="color:#FF6B00;">미세 조정</b><br>
      <span style="font-size:12px; color:#475569;">(Fine-tuning)</span><br>
      특정 작업에 맞게<br>조금만 추가 학습
    </div>
  </div>
</div>

<!-- 특징 3 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 12px; border-radius:999px; font-size:12px; font-weight:900; white-space:nowrap;">특징 3</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">트랜스포머(Transformer) 구조</div>
  </div>
  <p style="margin:0 0 12px 0; font-size:14px; color:#475569; line-height:1.7;">BERT는 <b style="color:#FF6B00;">어텐션(Attention)</b>이라는 메커니즘을 사용합니다.<br>
  문장 안에서 각 단어가 다른 단어들과 얼마나 관련 있는지를 계산합니다.</p>
  <div style="background:#1e1e2e; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"나는 배가 고프다"</span>

<span style="color:#89dceb;">"고프다"</span><span style="color:#6c7086;">가 가장 주목하는 단어 → </span><span style="color:#ff5f57; font-weight:900;">"배"</span> <span style="color:#6c7086;">(신체 기관)</span>
<span style="color:#89dceb;">"배"</span><span style="color:#6c7086;">가 가장 주목하는 단어    → </span><span style="color:#ff5f57; font-weight:900;">"고프다"</span><span style="color:#6c7086;">, </span><span style="color:#ff5f57; font-weight:900;">"나는"</span></div>
</div>

</div>
</div>

<br>

<!-- 모델 발전사 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 BERT 이후 등장한 모델들
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BERT 이후로 더 강력한 문장 임베딩 모델들이 계속 나왔습니다.
</p>

<div style="display: grid; gap: 8px; margin-top: 16px;">

  <div style="display:grid; grid-template-columns:60px 130px 1fr; gap:10px; align-items:center; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px;">
    <div style="font-size:13px; font-weight:900; color:#94a3b8; text-align:center;">2018</div>
    <div style="background:#0f172a; color:#c3e88d; padding:5px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px; font-weight:900; text-align:center;">BERT</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">Google · 양방향 트랜스포머 · <b>언어 이해의 혁신</b></div>
  </div>

  <div style="display:grid; grid-template-columns:60px 130px 1fr; gap:10px; align-items:center; background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:12px 16px;">
    <div style="font-size:13px; font-weight:900; color:#94a3b8; text-align:center;">2019</div>
    <div style="display:grid; gap:4px;">
      <div style="background:#f8fafc; border:1px solid #e2e8f0; color:#475569; padding:4px 8px; border-radius:6px; font-family:Consolas, monospace; font-size:12px; font-weight:900; text-align:center;">RoBERTa</div>
      <div style="background:#f8fafc; border:1px solid #e2e8f0; color:#475569; padding:4px 8px; border-radius:6px; font-family:Consolas, monospace; font-size:12px; font-weight:900; text-align:center;">GPT-2</div>
    </div>
    <div style="font-size:13px; color:#334155; line-height:1.8;">Facebook · BERT를 더 오래·더 많이 학습<br>OpenAI · 텍스트 생성에 특화</div>
  </div>

  <div style="display:grid; grid-template-columns:60px 130px 1fr; gap:10px; align-items:center; background:#eef7ff; border:1px solid #c2e4ff; border-radius:12px; padding:12px 16px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; text-align:center;">2020</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; color:#1681c4; padding:5px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px; font-weight:900; text-align:center;">GPT-3</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">OpenAI · 1,750억 개 파라미터 · <b>범용 언어 모델</b></div>
  </div>

  <div style="display:grid; grid-template-columns:60px 130px 1fr; gap:10px; align-items:center; background:#eef7ff; border:1px solid #c2e4ff; border-radius:12px; padding:12px 16px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; text-align:center;">2022</div>
    <div style="background:#1681c4; color:#fff; padding:5px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px; font-weight:900; text-align:center;">ChatGPT</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">OpenAI · GPT 기반 <b>대화 특화</b> 모델</div>
  </div>

  <div style="display:grid; grid-template-columns:60px 130px 1fr; gap:10px; align-items:center; background:#0f172a; border-radius:12px; padding:12px 16px;">
    <div style="font-size:13px; font-weight:900; color:#c3e88d; text-align:center;">2023</div>
    <div style="display:grid; gap:4px;">
      <div style="background:#0d0d1a; color:#c3e88d; padding:4px 8px; border-radius:6px; font-family:Consolas, monospace; font-size:12px; font-weight:900; text-align:center;">GPT-4</div>
      <div style="background:#0d0d1a; color:#c3e88d; padding:4px 8px; border-radius:6px; font-family:Consolas, monospace; font-size:12px; font-weight:900; text-align:center;">Claude</div>
    </div>
    <div style="font-size:13px; color:#a6e3a1; line-height:1.8;">OpenAI · 멀티모달(텍스트+이미지) 이해<br>Anthropic · 안전성 중심 대화 모델</div>
  </div>

  <div style="display:grid; grid-template-columns:60px 130px 1fr; gap:10px; align-items:center; background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:12px 16px;">
    <div style="font-size:13px; font-weight:900; color:#94a3b8; text-align:center;">2024~</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; color:#94a3b8; padding:5px 10px; border-radius:8px; font-size:12px; font-weight:900; text-align:center;">계속 발전 중</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">다양한 모델 계속 등장 중...</div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌</span> 우리가 지금 사용하는 <b>ChatGPT, Claude</b> 같은 AI 도구들이<br>
바로 이 문장 임베딩 기술을 기반으로 만들어졌습니다.
</div>

</div>

<br>

<!-- 한국어 모델 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🇰🇷 한국어 문장 임베딩 모델
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
한국어에 특화된 문장 임베딩 모델도 있습니다.
</p>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="display:grid; grid-template-columns:130px 80px 1fr; gap:10px; align-items:center; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px;">
    <div style="font-family:Consolas, monospace; font-size:13px; font-weight:900; color:#FF6B00;">KoBERT</div>
    <div style="font-size:12px; color:#475569; font-weight:900;">SKT</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">한국어 위키·뉴스 학습, BERT 기반</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 80px 1fr; gap:10px; align-items:center; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px;">
    <div style="font-family:Consolas, monospace; font-size:13px; font-weight:900; color:#FF6B00;">KoELECTRA</div>
    <div style="font-size:12px; color:#475569; font-weight:900;">모노레포</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">효율적인 학습 방식, 높은 성능</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 80px 1fr; gap:10px; align-items:center; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px;">
    <div style="font-family:Consolas, monospace; font-size:13px; font-weight:900; color:#FF6B00;">KoSimCSE</div>
    <div style="font-size:12px; color:#475569; font-weight:900;"> — </div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">문장 유사도에 특화</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 80px 1fr; gap:10px; align-items:center; background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:12px 16px;">
    <div style="font-family:Consolas, monospace; font-size:13px; font-weight:900; color:#1681c4;">HyperCLOVA</div>
    <div style="font-size:12px; color:#1681c4; font-weight:900;">네이버</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">한국어 최대 규모 언어 모델</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 80px 1fr; gap:10px; align-items:center; background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:12px 16px;">
    <div style="font-family:Consolas, monospace; font-size:13px; font-weight:900; color:#1681c4;">EXAONE</div>
    <div style="font-size:12px; color:#1681c4; font-weight:900;">LG AI연구원</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">한국어·영어 이중언어 모델</div>
  </div>

</div>
</div>

</div>