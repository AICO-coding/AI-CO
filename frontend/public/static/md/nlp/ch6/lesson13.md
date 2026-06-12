<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
BERT의 입력 구조
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
BERT에 문장을 넣기 전, 문장을 작은 조각으로 쪼개야 합니다.<br>
<b style="color:#1681c4;">WordPiece 토크나이저</b>와 <b style="color:#1681c4;">특수 토큰</b>의 역할을 알아봅니다.
</p>

</div>

<br>

<!-- WordPiece란 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
✂️ BERT의 토크나이저: WordPiece
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BERT는 <b>WordPiece</b> 방식으로 문장을 쪼갭니다. 단어 전체를 하나의 토큰으로 쓰지 않고 <b style="color:#1681c4;">자주 쓰이는 조각 단위</b>로 분리합니다.
</p>

<!-- 비유: 레고 블록 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px; margin: 16px 0;">
  <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:12px;">🧱 비유: 레고 블록</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:12px 14px; font-size:13px; color:#334155; line-height:1.7;">
      <b style="color:#1681c4;">흔한 단어</b><br>→ 하나의 블록 그대로
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:12px 14px; font-size:13px; color:#334155; line-height:1.7;">
      <b style="color:#FF6B00;">희귀한 단어</b><br>→ 여러 개의 작은 블록으로 분해
    </div>
  </div>
</div>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">WordPiece 분리 예시 (영어)</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#a6e3a1;">"playing"</span>   <span style="color:#6c7086;">→</span>  <span style="color:#89dceb;">"play"</span> <span style="color:#6c7086;">+</span> <span style="color:#f9e2af;">"##ing"</span>
<span style="color:#a6e3a1;">"unhappy"</span>   <span style="color:#6c7086;">→</span>  <span style="color:#89dceb;">"un"</span> <span style="color:#6c7086;">+</span> <span style="color:#f9e2af;">"##happy"</span>
<span style="color:#a6e3a1;">"unwanted"</span>  <span style="color:#6c7086;">→</span>  <span style="color:#89dceb;">"un"</span> <span style="color:#6c7086;">+</span> <span style="color:#f9e2af;">"##want"</span> <span style="color:#6c7086;">+</span> <span style="color:#f9e2af;">"##ed"</span>
<span style="color:#a6e3a1;">"AI"</span>        <span style="color:#6c7086;">→</span>  <span style="color:#89dceb;">"AI"</span>  <span style="color:#6c7086;">(흔한 단어 → 그대로)</span></div>
</div>

<div style="background:#fff3eb; border:2px solid #ffd0b0; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#FF6B00; font-weight:900;">💡</span> 앞에 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px; font-weight:900;">##</code>이 붙은 조각은 <b style="color:#FF6B00;">앞 조각에 이어지는 부분</b>임을 나타냅니다.
</div>

</div>

<br>

<!-- 왜 쪼갤까 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🤔 왜 통째로 쓰지 않고 쪼갤까요?
</h2>

<div style="display: grid; gap: 14px; margin-top: 16px;">

  <!-- 이유 ① -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">이유 ①</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">처음 보는 단어(미등록어) 문제 해결</div>
    </div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#fff1f2; border:1px solid #fca5a5; border-radius:10px; overflow:hidden;">
        <div style="background:#dc2626; padding:6px 12px; font-size:12px; font-weight:900; color:#fff;">❌ 통째로 쓰는 방식</div>
        <div style="padding:10px 12px; font-family:Consolas,monospace; font-size:12px; color:#334155; line-height:1.8;">
          "ChatGPT" → 사전에 없음<br>→ <b style="color:#dc2626;">[UNK]</b> (모름)
        </div>
      </div>
      <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:10px; overflow:hidden;">
        <div style="background:#16a34a; padding:6px 12px; font-size:12px; font-weight:900; color:#fff;">✅ WordPiece</div>
        <div style="padding:10px 12px; font-family:Consolas,monospace; font-size:12px; color:#334155; line-height:1.8;">
          "ChatGPT" → "Chat" + "##G" + "##PT"<br>→ 의미 있는 조각으로 처리
        </div>
      </div>
    </div>
  </div>

  <!-- 이유 ② -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">이유 ②</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">어휘 사전 크기 절약</div>
    </div>
    <div style="font-size:14px; color:#334155; line-height:1.8; margin-bottom:10px;">
      영어만 해도 단어 수가 수백만 개입니다. 모든 단어를 사전에 넣으면 모델이 너무 커집니다.
    </div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 14px; font-size:14px; color:#1681c4; font-weight:900; text-align:center;">
      WordPiece는 약 <b>3만 개의 조각만으로</b> 거의 모든 단어를 표현할 수 있습니다.
    </div>
  </div>

  <!-- 이유 ③ -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">이유 ③</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">형태소 관계 학습에 유리</div>
    </div>
    <div style="background:#1e1e2e; border-radius:10px; padding:12px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.3; overflow-x:auto; white-space:pre; margin-bottom:10px;">
<span style="color:#a6e3a1;">"play", "playing", "played", "player"</span>
<span style="color:#6c7086;">→ WordPiece: </span><span style="color:#89dceb;">"play"</span><span style="color:#6c7086;"> + </span><span style="color:#f9e2af;">"##ing"</span><span style="color:#6c7086;">,  </span><span style="color:#89dceb;">"play"</span><span style="color:#6c7086;"> + </span><span style="color:#f9e2af;">"##ed"</span><span style="color:#6c7086;">,  </span><span style="color:#89dceb;">"play"</span><span style="color:#6c7086;"> + </span><span style="color:#f9e2af;">"##er"</span></div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.7;">
      공통 조각 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 5px; border-radius:4px; font-weight:900;">"play"</code>를 통해 모두 같은 동사 어근에서 파생됐음을 학습할 수 있습니다.
    </div>
  </div>

</div>

</div>

<br>

<!-- 특수 토큰 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔤 특수 토큰: BERT만의 약속
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BERT는 일반 단어 외에 특별한 역할을 하는 <b>특수 토큰</b>을 사용합니다.
</p>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 10px; border-radius:8px; font-family:Consolas,monospace; font-size:13px; font-weight:900; white-space:nowrap;">[CLS]</div>
    <div>
      <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:3px;">Classification</div>
      <div style="font-size:13px; color:#475569; line-height:1.6;">문장 맨 앞에 붙음. <b style="color:#1681c4;">문장 전체 의미</b>를 담는 특수 자리</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#64748b; color:#fff; padding:5px 10px; border-radius:8px; font-family:Consolas,monospace; font-size:13px; font-weight:900; white-space:nowrap;">[SEP]</div>
    <div>
      <div style="font-size:13px; font-weight:900; color:#64748b; margin-bottom:3px;">Separator</div>
      <div style="font-size:13px; color:#475569; line-height:1.6;">문장과 문장 사이, 또는 문장 끝에 붙는 <b>구분자</b></div>
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:5px 10px; border-radius:8px; font-family:Consolas,monospace; font-size:13px; font-weight:900; white-space:nowrap;">[MASK]</div>
    <div>
      <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:3px;">Mask</div>
      <div style="font-size:13px; color:#475569; line-height:1.6;">MLM 학습 시 <b style="color:#FF6B00;">가려지는 자리</b></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#94a3b8; color:#fff; padding:5px 10px; border-radius:8px; font-family:Consolas,monospace; font-size:13px; font-weight:900; white-space:nowrap;">[PAD]</div>
    <div>
      <div style="font-size:13px; font-weight:900; color:#64748b; margin-bottom:3px;">Padding</div>
      <div style="font-size:13px; color:#475569; line-height:1.6;">문장 길이를 맞추기 위해 채우는 <b>빈 자리</b></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#94a3b8; color:#fff; padding:5px 10px; border-radius:8px; font-family:Consolas,monospace; font-size:13px; font-weight:900; white-space:nowrap;">[UNK]</div>
    <div>
      <div style="font-size:13px; font-weight:900; color:#64748b; margin-bottom:3px;">Unknown</div>
      <div style="font-size:13px; color:#475569; line-height:1.6;">사전에 없는 글자가 나왔을 때</div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 토크나이징 전체 과정 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 토크나이징 전체 과정 예시
</h2>

<div style="display: grid; gap: 8px; margin-top: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">①</div>
    <div style="flex:1;">
      <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:6px;">토크나이저 적용</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:9px 14px; font-family:Consolas,monospace; font-size:13px; color:#cdd6f4; overflow-x:auto; white-space:pre;"><span style="color:#6c7086;">원문: "나는 카페에서 커피를 마셨다"</span>
<span style="color:#a6e3a1;">→ 나는 / 카페 / ##에서 / 커피 / ##를 / 마셨 / ##다</span></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">②</div>
    <div style="flex:1;">
      <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:6px;">특수 토큰 추가</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:9px 14px; font-family:Consolas,monospace; font-size:13px; color:#cdd6f4; overflow-x:auto; white-space:pre;"><span style="color:#f38ba8;">[CLS]</span> <span style="color:#a6e3a1;">/ 나는 / 카페 / ##에서 / 커피 / ##를 / 마셨 / ##다 /</span> <span style="color:#f38ba8;">[SEP]</span></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">③</div>
    <div style="flex:1;">
      <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:6px;">각 토큰에 고유 ID 부여 (정수 변환)</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:9px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;"><span style="color:#89dceb;">[101]  [2399]  [8492]  [2015]  [5642]  [1012]  [7891]  [4412]  [102]</span>
<span style="color:#6c7086;">[CLS]   나는     카페     에서     커피      를       마셨      다      [SEP]</span></div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">④</div>
    <div style="font-size:14px; color:#1681c4; font-weight:900;">이 ID 목록이 BERT의 실제 입력입니다!</div>
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
    BERT는 <b style="color:#FF6B00;">WordPiece</b> 방식으로 문장을 작은 조각(토큰)으로 쪼갭니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이 방식 덕분에 신조어나 희귀 단어도 <b style="color:#FF6B00;">조각으로 분해해 처리</b>할 수 있습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 6px; border-radius:4px;">[CLS]</code>, <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 6px; border-radius:4px;">[SEP]</code>, <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 6px; border-radius:4px;">[MASK]</code> 같은 <b style="color:#FF6B00;">특수 토큰</b>이 BERT 입력의 핵심 구성 요소입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    최종적으로 각 토큰은 <b style="color:#FF6B00;">정수 ID</b>로 변환되어 BERT에 입력됩니다.
  </div>
</div>

</div>

</div>