<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
[SEP] 토큰
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
<b style="color:#1681c4;">[SEP]</b>는 문장과 문장 사이의 경계를 나타내는 구분자입니다.<br>
왜 필요한지, 어떤 과제에서 어떻게 활용되는지 알아봅니다.
</p>

</div>

<br>

<!-- [SEP] 토큰이란 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
✂️ [SEP] 토큰이란?
</h2>

<div style="display: grid; grid-template-columns: auto 1fr; gap: 20px; align-items: center; margin-bottom: 18px;">
  <div style="background:#64748b; color:#fff; padding:10px 16px; border-radius:12px; font-family:Consolas,monospace; font-size:20px; font-weight:900; white-space:nowrap;">[SEP]</div>
  <div>
    <div style="font-size:15px; font-weight:900; color:#64748b; margin-bottom:4px;">Separator의 약자 — "구분자"</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">단어 그대로 <b>경계를 나타내는</b> 토큰입니다.</div>
  </div>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">두 가지 상황에서 사용됩니다.</p>

<div style="display: grid; gap: 10px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 18px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#64748b; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">① 단일 문장</div>
    <div style="flex:1;">
      <div style="font-size:13px; color:#334155; margin-bottom:6px;">문장의 <b>끝을 표시</b></div>
      <div style="background:#1e1e2e; border-radius:8px; padding:9px 14px; font-family:Consolas,monospace; font-size:13px; color:#cdd6f4; overflow-x:auto; white-space:pre;"><span style="color:#f38ba8;">[CLS]</span> <span style="color:#a6e3a1;">오늘 날씨가 좋다</span> <span style="color:#f38ba8;">[SEP]</span></div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 18px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">② 문장 쌍</div>
    <div style="flex:1;">
      <div style="font-size:13px; color:#334155; margin-bottom:6px;">두 문장 <b>사이 + 마지막</b>에 배치</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:9px 14px; font-family:Consolas,monospace; font-size:13px; color:#cdd6f4; overflow-x:auto; white-space:pre;"><span style="color:#f38ba8;">[CLS]</span> <span style="color:#f9e2af;">문장A</span> <span style="color:#f38ba8;">[SEP]</span> <span style="color:#89dceb;">문장B</span> <span style="color:#f38ba8;">[SEP]</span></div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 왜 필요한가 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🤔 왜 [SEP]가 필요할까요?
</h2>

<div style="display: grid; gap: 14px; margin-top: 14px;">

  <!-- 이유 ① -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">이유 ①</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">두 문장의 경계를 명확히 알려줘야 한다</div>
    </div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#fff1f2; border:1px solid #fca5a5; border-radius:10px; overflow:hidden;">
        <div style="background:#dc2626; padding:6px 12px; font-size:12px; font-weight:900; color:#fff;">❌ [SEP] 없는 경우</div>
        <div style="background:#1e1e2e; padding:10px 12px; font-family:Consolas,monospace; font-size:12px; color:#cdd6f4; line-height:2.0; overflow-x:auto; white-space:pre;"><span style="color:#f38ba8;">[CLS]</span> <span style="color:#cdd6f4;">오늘 날씨가 좋다 공원에 가고 싶다</span> <span style="color:#f38ba8;">[SEP]</span>
<span style="color:#6c7086;">↑ 두 문장 경계가 불분명!</span></div>
      </div>
      <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:10px; overflow:hidden;">
        <div style="background:#16a34a; padding:6px 12px; font-size:12px; font-weight:900; color:#fff;">✅ [SEP] 있는 경우</div>
        <div style="background:#1e1e2e; padding:10px 12px; font-family:Consolas,monospace; font-size:12px; color:#cdd6f4; line-height:2.0; overflow-x:auto; white-space:pre;"><span style="color:#f38ba8;">[CLS]</span> <span style="color:#f9e2af;">오늘 날씨가 좋다</span> <span style="color:#f38ba8;">[SEP]</span> <span style="color:#89dceb;">공원에 가고 싶다</span> <span style="color:#f38ba8;">[SEP]</span>
<span style="color:#6c7086;">↑ 첫 번째 문장 끝, 두 번째 시작 명확</span></div>
      </div>
    </div>
  </div>

  <!-- 이유 ② -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">이유 ②</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">세그먼트 임베딩과 함께 작동</div>
    </div>
    <div style="font-size:14px; color:#334155; line-height:1.8; margin-bottom:12px;">
      세그먼트 임베딩(Token Type IDs)은 <code style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:1px 5px; border-radius:4px; font-weight:900;">[SEP]</code>를 기준으로 A와 B를 나눕니다.
    </div>
    <div style="background:#1e1e2e; border-radius:10px; padding:12px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#cdd6f4;">[CLS] 오늘 날씨가 좋다 [SEP] 공원에 가고 싶다 [SEP]</span>
<span style="color:#f9e2af;">  A    A     A     A    A  </span><span style="color:#89dceb;">    B      B    B    B    B</span></div>
    <div style="margin-top:10px; font-size:13px; color:#475569; line-height:1.7;">
      <span style="color:#1681c4; font-weight:900;">💡</span> <code style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:1px 5px; border-radius:4px;">[SEP]</code>가 없으면 세그먼트 경계를 그을 수 없습니다.
    </div>
  </div>

</div>

</div>

<br>

<!-- 단일 문장 vs 문장 쌍 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📐 단일 문장 vs. 문장 쌍 입력 형식 비교
</h2>

<div style="display: grid; gap: 14px; margin-top: 16px;">

  <!-- 형식 A -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; overflow:hidden;">
    <div style="background:#64748b; padding:10px 16px;">
      <div style="font-size:13px; font-weight:900; color:#fff;">형식 A — 단일 문장 입력 (Single Sentence)</div>
    </div>
    <div style="padding:14px 16px;">
      <div style="font-size:13px; color:#475569; margin-bottom:10px; line-height:1.7;">
        <b>사용 과제:</b> 감정 분류, 스팸 분류, 문서 주제 분류 등
      </div>
      <div style="background:#1e1e2e; border-radius:10px; padding:12px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">입력 형식:</span>
<span style="color:#f38ba8;">[CLS]</span> <span style="color:#6c7086;">+</span> <span style="color:#a6e3a1;">문장 토큰들</span> <span style="color:#6c7086;">+</span> <span style="color:#f38ba8;">[SEP]</span>

<span style="color:#6c7086;">예시:</span>
<span style="color:#f38ba8;">[CLS]</span> <span style="color:#a6e3a1;">이 영화 정말 재미있었어요</span> <span style="color:#f38ba8;">[SEP]</span>
<span style="color:#f9e2af;">  A    A   A     A      A        A</span>

<span style="color:#6c7086;">→ [CLS] 출력 벡터로 긍정/부정 분류</span></div>
    </div>
  </div>

  <!-- 형식 B -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; overflow:hidden;">
    <div style="background:#1681c4; padding:10px 16px;">
      <div style="font-size:13px; font-weight:900; color:#fff;">형식 B — 문장 쌍 입력 (Sentence Pair)</div>
    </div>
    <div style="padding:14px 16px;">
      <div style="font-size:13px; color:#475569; margin-bottom:10px; line-height:1.7;">
        <b>사용 과제:</b> 질의응답, 문장 관계 파악, NSP 등
      </div>
      <div style="background:#1e1e2e; border-radius:10px; padding:12px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">입력 형식:</span>
<span style="color:#f38ba8;">[CLS]</span> <span style="color:#6c7086;">+</span> <span style="color:#f9e2af;">문장A 토큰들</span> <span style="color:#6c7086;">+</span> <span style="color:#f38ba8;">[SEP]</span> <span style="color:#6c7086;">+</span> <span style="color:#89dceb;">문장B 토큰들</span> <span style="color:#6c7086;">+</span> <span style="color:#f38ba8;">[SEP]</span>

<span style="color:#6c7086;">예시 (질의응답):</span>
<span style="color:#f38ba8;">[CLS]</span> <span style="color:#f9e2af;">카페는 어디에 있나요?</span> <span style="color:#f38ba8;">[SEP]</span> <span style="color:#89dceb;">카페는 역 앞에 있습니다.</span> <span style="color:#f38ba8;">[SEP]</span>
<span style="color:#f9e2af;">  A    A      A    A    A    A  </span><span style="color:#89dceb;">   B     B  B   B    B         B</span>

<span style="color:#6c7086;">→ 문장B의 각 토큰 벡터로 답 위치 찾기</span></div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 과제별 활용 방식 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🗺️ 과제별 [CLS] / [SEP] 활용 방식
</h2>

<div style="display: grid; gap: 8px; margin-top: 16px;">

  <div style="display:grid; grid-template-columns:130px 1fr 1fr 1fr; gap:8px; align-items:center;">
    <div style="font-size:12px; font-weight:900; color:#94a3b8; padding:0 4px;">과제</div>
    <div style="font-size:12px; font-weight:900; color:#94a3b8; padding:0 4px;">입력 형식</div>
    <div style="font-size:12px; font-weight:900; color:#94a3b8; padding:0 4px;">[CLS] 역할</div>
    <div style="font-size:12px; font-weight:900; color:#94a3b8; padding:0 4px;">[SEP] 역할</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr 1fr 1fr; gap:8px; align-items:center; background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 8px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; padding:0 4px;">감정 분류</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">문장 1개</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">분류 결과 출력</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">문장 끝 표시</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr 1fr 1fr; gap:8px; align-items:center; background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 8px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; padding:0 4px;">스팸 탐지</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">문장 1개</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">분류 결과 출력</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">문장 끝 표시</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr 1fr 1fr; gap:8px; align-items:center; background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 8px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; padding:0 4px;">자연어 추론</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">전제 + 가설</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">함의/모순/중립 분류</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">두 문장 경계</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr 1fr 1fr; gap:8px; align-items:center; background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 8px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; padding:0 4px;">질의응답</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">질문 + 지문</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">거의 사용 안 함</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">질문/지문 경계</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr 1fr 1fr; gap:8px; align-items:center; background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 8px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; padding:0 4px;">문장 유사도</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">문장A + 문장B</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">유사도 점수 출력</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">두 문장 경계</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr 1fr 1fr; gap:8px; align-items:center; background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 8px;">
    <div style="font-size:13px; font-weight:900; color:#64748b; padding:0 4px;">개체명 인식</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">문장 1개</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">사용 안 함</div>
    <div style="font-size:12px; color:#475569; padding:0 4px;">문장 끝 표시</div>
  </div>

</div>

</div>

<br>

<!-- 실제 코드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📦 실제 토크나이저 출력으로 보기
</h2>

<div style="background-color: #1e1e2e; border-radius: 16px; overflow: hidden; margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 sep_token_example.py</span>
    </div>
    <div style="background-color: rgba(22,129,196,.2); color: #1681c4; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      [SEP] 토큰 확인
    </div>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.0; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">transformers</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">BertTokenizer</span>

<span style="color:#cdd6f4;">tokenizer = BertTokenizer.from_pretrained(</span><span style="color:#a6e3a1;">'bert-base-multilingual-cased'</span><span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># 문장 쌍 입력</span>
<span style="color:#cdd6f4;">result = tokenizer(</span><span style="color:#a6e3a1;">"오늘 날씨 좋다"</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">"공원 가고 싶다"</span><span style="color:#cdd6f4;">)</span>

<span style="color:#cdd6f4;">tokens = tokenizer.convert_ids_to_tokens(result[</span><span style="color:#a6e3a1;">'input_ids'</span><span style="color:#cdd6f4;">])</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(tokens)</span>
<span style="color:#6c7086;"># → ['[CLS]', '오늘', '날씨', '좋다', '[SEP]', '공원', '가고', '싶다', '[SEP]']</span>

<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(result[</span><span style="color:#a6e3a1;">'token_type_ids'</span><span style="color:#cdd6f4;">])</span>
<span style="color:#6c7086;"># → [0, 0, 0, 0, 0, 1, 1, 1, 1]</span>
<span style="color:#6c7086;">#    CLS  A   A   A  SEP  B  B   B  SEP</span></div>
</div>

<div style="display: grid; gap: 8px; margin-top: 14px;">
  <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; line-height:1.7; display:flex; gap:10px; align-items:center;">
    <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 7px; border-radius:6px; font-weight:900; white-space:nowrap;">[CLS]</code>
    <span>의 token_type_id는 <b>0 (문장A 소속)</b>입니다.</span>
  </div>
  <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; line-height:1.7; display:flex; gap:10px; align-items:center;">
    <span style="white-space:nowrap; font-size:12px; font-weight:900; color:#64748b;">첫 번째 [SEP]</span>
    <span>도 <b>0 (문장A의 끝)</b>으로 처리됩니다.</span>
  </div>
  <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; line-height:1.7; display:flex; gap:10px; align-items:center;">
    <span style="white-space:nowrap; font-size:12px; font-weight:900; color:#1681c4;">두 번째 [SEP]</span>
    <span>는 <b style="color:#1681c4;">1 (문장B 소속)</b>으로 처리됩니다.</span>
  </div>
</div>

</div>

<br>

<!-- CLS + SEP 함께 정리 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔁 [CLS]와 [SEP] 함께 정리
</h2>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">BERT 입력 전체 구조</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.6; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">단일 문장:</span>
<span style="color:#f38ba8;">┌─────┐</span><span style="color:#a6e3a1;">┌─────────────────────────┐</span><span style="color:#f38ba8;">┌─────┐</span>
<span style="color:#f38ba8;">│[CLS]│</span><span style="color:#a6e3a1;">│  문장 토큰들             │</span><span style="color:#f38ba8;">│[SEP]│</span>
<span style="color:#f38ba8;">└─────┘</span><span style="color:#a6e3a1;">└─────────────────────────┘</span><span style="color:#f38ba8;">└─────┘</span>
   <span style="color:#f9e2af;">↓ 문장 전체 의미 흡수</span>                        <span style="color:#89dceb;">↓ 문장 끝 신호</span>

<span style="color:#6c7086;">문장 쌍:</span>
<span style="color:#f38ba8;">┌─────┐</span><span style="color:#f9e2af;">┌──────────────┐</span><span style="color:#f38ba8;">┌─────┐</span><span style="color:#89dceb;">┌──────────────┐</span><span style="color:#f38ba8;">┌─────┐</span>
<span style="color:#f38ba8;">│[CLS]│</span><span style="color:#f9e2af;">│  문장A 토큰들 │</span><span style="color:#f38ba8;">│[SEP]│</span><span style="color:#89dceb;">│  문장B 토큰들 │</span><span style="color:#f38ba8;">│[SEP]│</span>
<span style="color:#f38ba8;">└─────┘</span><span style="color:#f9e2af;">└──────────────┘</span><span style="color:#f38ba8;">└─────┘</span><span style="color:#89dceb;">└──────────────┘</span><span style="color:#f38ba8;">└─────┘</span>
   <span style="color:#f9e2af;">↓ 문장 전체 요약</span>     <span style="color:#f38ba8;">↓ 경계 · A/B 구분 기준</span>               <span style="color:#89dceb;">↓ 문장B 끝 신호</span></div>
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
    <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 6px; border-radius:4px;">[SEP]</code>는 문장의 끝, 또는 두 문장 사이의 <b style="color:#FF6B00;">경계선</b> 역할을 합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    문장 쌍 입력에서 <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 6px; border-radius:4px;">[SEP]</code>가 없으면 BERT가 <b style="color:#FF6B00;">어디서 문장이 바뀌는지</b> 알 수 없습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 6px; border-radius:4px;">[SEP]</code>는 <b style="color:#FF6B00;">세그먼트 임베딩(Token Type IDs)</b>의 기준점이 되기도 합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 6px; border-radius:4px;">[CLS]</code> + <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 6px; border-radius:4px;">[SEP]</code>는 BERT가 다양한 과제를 <b style="color:#FF6B00;">하나의 통일된 입력 형식</b>으로 처리할 수 있게 해주는 핵심 설계입니다.
  </div>
</div>

</div>

</div>