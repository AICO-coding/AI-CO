<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Attention Mask와 실제 입력 조립
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
BERT의 실제 입력은 세 가지 배열로 구성됩니다.<br>
<b style="color:#1681c4;">Input IDs · Token Type IDs · Attention Mask</b>가 어떻게 조립되는지 알아봅니다.
</p>

</div>

<br>

<!-- 최대 입력 길이 + 패딩 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📏 BERT의 최대 입력 길이와 패딩
</h2>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center; margin-bottom: 18px;">
BERT-Base 최대 <b>512개 토큰</b> = 약 350~400개 한국어 단어 분량
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
512토큰보다 <b>짧은 문장</b>은 빈 자리를 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 7px; border-radius:6px; font-weight:900;">[PAD]</code> 토큰으로 채웁니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">패딩 예시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">짧은 문장 (3개 토큰):</span>
<span style="color:#a6e3a1;">[CLS] 안녕하세요 [SEP]</span>

<span style="color:#6c7086;">512 길이로 패딩 후:</span>
<span style="color:#a6e3a1;">[CLS] 안녕하세요 [SEP]</span> <span style="color:#94a3b8;">[PAD] [PAD] [PAD] ... [PAD]</span>
<span style="color:#6c7086;"> ←── 3개 진짜 ──→  ←─────── 509개 패딩 ────────→</span></div>
</div>

</div>

<br>

<!-- Attention Mask -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎭 Attention Mask: "진짜 토큰과 패딩을 구분"
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 16px;">
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 7px; border-radius:6px; font-weight:900;">[PAD]</code>는 의미 없는 빈 자리입니다. Self-Attention이 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 7px; border-radius:6px;">[PAD]</code>에도 주의를 기울이면 <b>잡음(noise)이 생깁니다.</b>
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Attention Mask 예시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">토큰:            </span><span style="color:#a6e3a1;">[CLS]  안녕하세요  [SEP]</span>  <span style="color:#94a3b8;">[PAD]  [PAD]  ...  [PAD]</span>
<span style="color:#6c7086;">Attention Mask:  </span><span style="color:#a6e3a1;">  1         1       1  </span>  <span style="color:#f38ba8;">  0      0    ...    0</span>
<span style="color:#6c7086;">                  ↑ 진짜                    ↑ 가짜 (무시)</span></div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 16px;">

  <div style="background:#f0fdf4; border:2px solid #86efac; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:28px; font-weight:900; color:#16a34a; margin-bottom:6px;">1</div>
    <div style="font-size:13px; font-weight:900; color:#16a34a; margin-bottom:4px;">진짜 토큰</div>
    <div style="font-size:12px; color:#475569; line-height:1.5;">정상적으로 Attention 계산</div>
  </div>

  <div style="background:#fff1f2; border:2px solid #fca5a5; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:28px; font-weight:900; color:#dc2626; margin-bottom:6px;">0</div>
    <div style="font-size:13px; font-weight:900; color:#dc2626; margin-bottom:4px;">패딩 토큰</div>
    <div style="font-size:12px; color:#475569; line-height:1.5;">Attention에서 무시 (매우 낮은 점수 부여)</div>
  </div>

</div>

</div>

<br>

<!-- Token Type IDs -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔁 Token Type IDs (= 세그먼트 ID)
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
세그먼트 임베딩을 적용하기 위해 각 토큰이 <b>문장 A인지 B인지</b> 알려주는 Token Type IDs도 함께 준비합니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Token Type IDs 예시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">입력:          </span><span style="color:#cdd6f4;">[CLS] 질문입니다 [SEP] 이것이 답입니다 [SEP]</span>
<span style="color:#6c7086;">Token Type IDs:</span><span style="color:#f9e2af;">  0       0       0  </span><span style="color:#89dceb;">    1       1        1     1</span>
<span style="color:#6c7086;">               </span><span style="color:#f9e2af;">  A       A       A  </span><span style="color:#89dceb;">    B       B        B     B</span></div>
</div>

</div>

<br>

<!-- 5단계 조립 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🏗️ BERT 입력 조립: 5단계 전체 흐름
</h2>

<div style="display: grid; gap: 8px; margin-top: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">STEP 1</div>
    <div style="flex:1;">
      <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:5px;">원문 문장 준비</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#a6e3a1; line-height:1.9;">
        문장A: "오늘 날씨가 좋다"<br>문장B: "공원에 가고 싶다"
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">STEP 2</div>
    <div style="flex:1;">
      <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:5px;">토크나이징 (WordPiece)</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#cdd6f4; line-height:1.9; overflow-x:auto; white-space:pre;">오늘 / 날씨 / ##가 / 좋 / ##다
공원 / ##에 / 가고 / 싶 / ##다</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">STEP 3</div>
    <div style="flex:1;">
      <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:5px;">특수 토큰 추가 (총 12개 토큰)</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#cdd6f4; line-height:1.9; overflow-x:auto; white-space:pre;"><span style="color:#f38ba8;">[CLS]</span> <span style="color:#a6e3a1;">오늘 날씨가 좋다</span> <span style="color:#f38ba8;">[SEP]</span> <span style="color:#89dceb;">공원에 가고 싶다</span> <span style="color:#f38ba8;">[SEP]</span></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">STEP 4</div>
    <div style="flex:1;">
      <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:5px;">패딩 추가 (최대 길이 맞추기 → 총 512개)</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#cdd6f4; line-height:1.9; overflow-x:auto; white-space:pre;"><span style="color:#a6e3a1;">[CLS] 오늘 날씨가 좋다 [SEP] 공원에 가고 싶다 [SEP]</span> <span style="color:#94a3b8;">[PAD] [PAD] ...</span></div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">STEP 5</div>
    <div style="flex:1;">
      <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:8px;">세 가지 ID 배열 완성</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:12px 14px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.2; overflow-x:auto; white-space:pre;"><span style="color:#f9e2af;">Input IDs:      </span><span style="color:#cdd6f4;">[101, 2345, 1234, ..., 102, 0, 0, ...]</span>  <span style="color:#6c7086;">← 토큰 ID</span>
<span style="color:#89dceb;">Token Type IDs: </span><span style="color:#cdd6f4;">[  0,    0,    0, ...,   1, 0, 0, ...]</span>  <span style="color:#6c7086;">← 세그먼트 A/B</span>
<span style="color:#a6e3a1;">Attention Mask: </span><span style="color:#cdd6f4;">[  1,    1,    1, ...,   1, 0, 0, ...]</span>  <span style="color:#6c7086;">← 진짜/패딩</span></div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 실제 코드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💻 실제 코드로 보면 이렇습니다
</h2>

<div style="background-color: #1e1e2e; border-radius: 16px; overflow: hidden; margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 bert_input.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      BERT 입력 조립
    </div>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.0; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">transformers</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">BertTokenizer</span>

<span style="color:#cdd6f4;">tokenizer = BertTokenizer.from_pretrained(</span><span style="color:#a6e3a1;">'bert-base-multilingual-cased'</span><span style="color:#cdd6f4;">)</span>

<span style="color:#cdd6f4;">sentence_a = </span><span style="color:#a6e3a1;">"오늘 날씨가 좋다"</span>
<span style="color:#cdd6f4;">sentence_b = </span><span style="color:#a6e3a1;">"공원에 가고 싶다"</span>

<span style="color:#cdd6f4;">inputs = tokenizer(</span>
<span style="color:#cdd6f4;">    sentence_a,</span>
<span style="color:#cdd6f4;">    sentence_b,</span>
<span style="color:#cdd6f4;">    max_length=</span><span style="color:#89dceb;">512</span><span style="color:#cdd6f4;">,        </span><span style="color:#6c7086;"># 최대 길이</span>
<span style="color:#cdd6f4;">    padding=</span><span style="color:#a6e3a1;">'max_length'</span><span style="color:#cdd6f4;">,  </span><span style="color:#6c7086;"># 패딩으로 채우기</span>
<span style="color:#cdd6f4;">    truncation=</span><span style="color:#89dceb;">True</span><span style="color:#cdd6f4;">,       </span><span style="color:#6c7086;"># 512 초과 시 자르기</span>
<span style="color:#cdd6f4;">    return_tensors=</span><span style="color:#a6e3a1;">'pt'</span><span style="color:#cdd6f4;">    </span><span style="color:#6c7086;"># PyTorch 텐서로 반환</span>
<span style="color:#cdd6f4;">)</span>

<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(inputs[</span><span style="color:#a6e3a1;">'input_ids'</span><span style="color:#cdd6f4;">])       </span><span style="color:#6c7086;"># 토큰 ID</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(inputs[</span><span style="color:#a6e3a1;">'token_type_ids'</span><span style="color:#cdd6f4;">])  </span><span style="color:#6c7086;"># 세그먼트 ID</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(inputs[</span><span style="color:#a6e3a1;">'attention_mask'</span><span style="color:#cdd6f4;">])  </span><span style="color:#6c7086;"># Attention Mask</span></div>
</div>

</div>

<br>

<!-- 전체 요약 표 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 BERT 입력 구조 전체 요약
</h2>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 18px; display:grid; grid-template-columns:140px 1fr 1fr; gap:12px; align-items:center;">
    <div style="font-family:Consolas,monospace; font-size:13px; font-weight:900; color:#FF6B00;">Input IDs</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">각 토큰의 고유 번호</div>
    <div style="font-size:12px; color:#64748b; line-height:1.5;">0 ~ 약 3만 (어휘 사전 크기)</div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 18px; display:grid; grid-template-columns:140px 1fr 1fr; gap:12px; align-items:center;">
    <div style="font-family:Consolas,monospace; font-size:13px; font-weight:900; color:#1681c4;">Token Type IDs</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">문장 A(0)인지 B(1)인지</div>
    <div style="font-size:12px; color:#64748b; line-height:1.5;">0 또는 1</div>
  </div>

  <div style="background:#f0fdf4; border:2px solid #86efac; border-radius:12px; padding:14px 18px; display:grid; grid-template-columns:140px 1fr 1fr; gap:12px; align-items:center;">
    <div style="font-family:Consolas,monospace; font-size:13px; font-weight:900; color:#16a34a;">Attention Mask</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">진짜 토큰(1)인지 패딩(0)인지</div>
    <div style="font-size:12px; color:#64748b; line-height:1.5;">0 또는 1</div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 18px; display:grid; grid-template-columns:140px 1fr 1fr; gap:12px; align-items:center;">
    <div style="font-size:12px; font-weight:900; color:#64748b;">(내부 처리)<br>3가지 임베딩 합산</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">토큰+세그먼트+위치 벡터 합</div>
    <div style="font-size:12px; color:#64748b; line-height:1.5;">768차원 실수 벡터</div>
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
    BERT는 최대 <b style="color:#FF6B00;">512 토큰</b>을 받으며, 짧은 입력은 <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 6px; border-radius:4px;">[PAD]</code>로 채웁니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">Attention Mask</b>는 진짜 토큰(1)과 패딩(0)을 구분해서 Self-Attention이 패딩을 무시하게 합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    실제 BERT 입력은 <b style="color:#FF6B00;">Input IDs, Token Type IDs, Attention Mask</b> 세 가지 배열로 구성됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이 세 배열이 내부에서 <b style="color:#FF6B00;">3가지 임베딩으로 변환·합산</b>된 후 인코더로 전달됩니다.
  </div>
</div>

</div>

</div>