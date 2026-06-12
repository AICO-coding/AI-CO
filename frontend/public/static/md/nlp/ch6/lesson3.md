<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
BERT의 핵심 아이디어 — 양방향 문맥 이해와 Attention
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
BERT가 기존 모델과 다른 점은 무엇일까요?<br>
<b style="color:#1681c4;">양방향(Bidirectional) 학습</b>과 그 핵심인 <b style="color:#1681c4;">Self-Attention</b>을 이해합니다.
</p>

</div>

<br>

<!-- 세 가지 핵심 아이디어 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔑 BERT의 세 가지 핵심 아이디어
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
이번 화면에서는 <b>① 양방향 학습</b>과 그 핵심 메커니즘인 <b>Self-Attention</b>을 먼저 살펴봅니다.
</p>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:center;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; width:32px; height:32px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:15px; font-weight:900;">①</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:2px;">양방향(Bidirectional) 학습 ← 이번 화면</div>
      <div style="font-size:14px; color:#475569; line-height:1.6;">문장을 앞뒤 동시에 봅니다.</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:center;">
    <div style="flex-shrink:0; background:#64748b; color:#fff; width:32px; height:32px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:15px; font-weight:900;">②</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#64748b; margin-bottom:2px;">Masked Language Model (MLM)</div>
      <div style="font-size:14px; color:#475569; line-height:1.6;">단어를 가리고 맞추며 학습합니다.</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:center;">
    <div style="flex-shrink:0; background:#64748b; color:#fff; width:32px; height:32px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:15px; font-weight:900;">③</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#64748b; margin-bottom:2px;">트랜스포머 인코더 구조</div>
      <div style="font-size:14px; color:#475569; line-height:1.6;">Self-Attention으로 관계를 파악합니다.</div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 양방향 학습 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
👁️ 핵심 아이디어 ① : 양방향(Bidirectional) 학습
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
단어 하나의 의미는 <b>문맥에 따라 달라집니다.</b>
</p>

<div style="background:#0f172a; border-radius:14px; padding:16px 20px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.4; margin:14px 0; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">문장 A:</span> <span style="color:#cdd6f4;">"나는 </span><span style="color:#f9e2af; font-weight:900;">사과</span><span style="color:#cdd6f4;">를 먹었다"  </span><span style="color:#6c7086;">← 과일</span>
<span style="color:#6c7086;">문장 B:</span> <span style="color:#cdd6f4;">"그는 진심으로 </span><span style="color:#f9e2af; font-weight:900;">사과</span><span style="color:#cdd6f4;">를 했다"  </span><span style="color:#6c7086;">← 사죄</span></div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; margin-bottom: 18px;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 두 문장의 "사과"는 전혀 다른 의미입니다. 올바른 의미를 파악하려면 <b style="color:#FF6B00;">앞뒤 단어를 함께</b> 봐야 합니다.
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; overflow:hidden;">
    <div style="background:#FF6B00; padding:10px 16px;">
      <div style="font-size:13px; font-weight:900; color:#fff;">GPT — 단방향 ❌</div>
    </div>
    <div style="background:#1e1e2e; padding:14px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#f38ba8;">나는 → 진심으로 → 사과 →</span>
<span style="color:#6c7086;">왼쪽만 참고
"사과" 의미 파악 불완전</span></div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; overflow:hidden;">
    <div style="background:#1681c4; padding:10px 16px;">
      <div style="font-size:13px; font-weight:900; color:#fff;">BERT — 양방향 ✅</div>
    </div>
    <div style="background:#1e1e2e; padding:14px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">나는 ←→ 진심으로 ←→ 사과 ←→ 했다</span>
<span style="color:#6c7086;">앞뒤 모두 참고
"사과" = 사죄 ✅</span></div>
  </div>

</div>

</div>

<br>

<!-- Self-Attention -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔗 Self-Attention: "이 단어는 다른 어떤 단어와 관련이 있을까?"
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BERT의 양방향 이해를 가능하게 하는 핵심 메커니즘이 <b>Self-Attention</b>입니다.
</p>

<!-- 비유: 회의실 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px; margin:14px 0;">
  <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:12px;">📋 비유: 회의실 대화</div>
  <p style="font-size:14px; color:#334155; line-height:1.8; margin:0 0 12px 0;">
  회의실에 5명이 앉아 있습니다. 발언자가 말할 때 청중 각자가 <b>"이 말이 나와 얼마나 관련 있지?"</b> 라고 점수를 매깁니다.
  </p>
  <div style="background:#1e1e2e; border-radius:12px; padding:14px 18px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#cdd6f4;">발언: </span><span style="color:#a6e3a1;">"그 프로젝트 마감은 내일입니다"</span>

<span style="color:#89dceb;">청중 A</span> <span style="color:#6c7086;">(기획자):</span>  <span style="color:#f9e2af; font-weight:900;">90점</span> <span style="color:#6c7086;">— 직접 관련</span>
<span style="color:#89dceb;">청중 B</span> <span style="color:#6c7086;">(디자이너):</span> <span style="color:#f9e2af; font-weight:900;">70점</span> <span style="color:#6c7086;">— 관련 있음</span>
<span style="color:#89dceb;">청중 C</span> <span style="color:#6c7086;">(총무):</span>    <span style="color:#cdd6f4;">20점</span> <span style="color:#6c7086;">— 별로 관련 없음</span></div>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Self-Attention도 같습니다. 문장의 <b>각 단어가 다른 모든 단어와의 관련도(Attention Score)를 계산</b>합니다.
</p>

<!-- 예시 -->
<div style="background:#0f172a; border-radius:14px; padding:16px 20px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.4; margin:14px 0; overflow-x:auto; white-space:pre;">
<span style="color:#cdd6f4; font-weight:900;">"배가 항구에 들어왔다" — "배" 입장에서 Attention Score:</span>

<span style="color:#89dceb;">배</span>  → <span style="color:#89dceb;">배</span>:    <span style="color:#a6e3a1; font-weight:900;">1.0</span>  <span style="color:#6c7086;">(자기 자신)</span>
<span style="color:#89dceb;">배</span>  → <span style="color:#f9e2af;">항구</span>:  <span style="color:#a6e3a1; font-weight:900;">0.8</span>  <span style="color:#6c7086;">← 높은 점수! (장소 = 선박 의미 단서)</span>
<span style="color:#89dceb;">배</span>  → <span style="color:#f9e2af;">들어</span>:  <span style="color:#a6e3a1; font-weight:900;">0.7</span>  <span style="color:#6c7086;">← 높은 점수! (이동 동사 = 선박 의미 단서)</span>
<span style="color:#89dceb;">배</span>  → <span style="color:#cdd6f4;">에</span>:    <span style="color:#cdd6f4;">0.2</span>
<span style="color:#89dceb;">배</span>  → <span style="color:#cdd6f4;">왔다</span>:  <span style="color:#cdd6f4;">0.3</span></div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8; margin-top:14px;">
<span style="color:#1681c4; font-weight:900;">✅</span> 이 과정을 통해 BERT는 "배" = <b style="color:#1681c4;">선박</b>이라는 것을 파악합니다.
</div>

</div>

<br>

<!-- Q K V -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📐 Self-Attention 작동 원리 (Q · K · V)
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Self-Attention은 각 단어에 대해 세 가지 역할의 벡터를 만듭니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; margin-top: 16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:18px 16px; text-align:center;">
    <div style="font-size:28px; font-weight:900; color:#1681c4; margin-bottom:8px;">Q</div>
    <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:6px;">Query</div>
    <div style="font-size:13px; color:#334155; line-height:1.7;">"나는 무엇을 찾고 있나?"</div>
    <div style="margin-top:10px; background:#fff; border:1px solid #c2e4ff; border-radius:8px; padding:8px; font-size:12px; color:#64748b;">🔍 검색어</div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:18px 16px; text-align:center;">
    <div style="font-size:28px; font-weight:900; color:#1681c4; margin-bottom:8px;">K</div>
    <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:6px;">Key</div>
    <div style="font-size:13px; color:#334155; line-height:1.7;">"나는 어떤 정보를 갖고 있나?"</div>
    <div style="margin-top:10px; background:#fff; border:1px solid #c2e4ff; border-radius:8px; padding:8px; font-size:12px; color:#64748b;">📚 책의 색인</div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 16px; text-align:center;">
    <div style="font-size:28px; font-weight:900; color:#FF6B00; margin-bottom:8px;">V</div>
    <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:6px;">Value</div>
    <div style="font-size:13px; color:#334155; line-height:1.7;">"나의 실제 내용은?"</div>
    <div style="margin-top:10px; background:#fff; border:1px solid #ffd0b0; border-radius:8px; padding:8px; font-size:12px; color:#64748b;">📖 책의 본문</div>
  </div>

</div>

<div style="margin-top:16px; background:#1e1e2e; border-radius:14px; padding:16px 20px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#89dceb;">Q</span><span style="color:#cdd6f4;">와 </span><span style="color:#89dceb;">K</span><span style="color:#cdd6f4;">의 유사도를 계산  →  </span><span style="color:#f9e2af;">Attention Score</span>
<span style="color:#f9e2af;">Score</span><span style="color:#cdd6f4;">가 높은 단어의 </span><span style="color:#a6e3a1;">V</span><span style="color:#cdd6f4;">를 많이 반영  →  </span><span style="color:#a6e3a1;">문맥이 담긴 표현 완성</span></div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;">
<span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리
</div>

<div style="display: grid; gap: 8px;">
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    BERT는 문장 전체를 <b style="color:#FF6B00;">양방향으로 동시에</b> 읽어 문맥을 파악합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이를 가능하게 하는 핵심이 <b style="color:#FF6B00;">Self-Attention</b>으로, 각 단어가 다른 모든 단어와의 관련도를 계산합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    덕분에 "배", "사과"처럼 <b style="color:#FF6B00;">동음이의어나 문맥 의존적 단어</b>도 정확하게 표현할 수 있습니다.
  </div>
</div>

</div>

</div>