<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
BERT가 등장한 이유 — 사전학습
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
처음부터 다 가르쳐야 할까요?<br>
<b style="color:#1681c4;">사전학습(Pre-training)</b>과 <b style="color:#1681c4;">미세조정(Fine-tuning)</b> 패러다임이 NLP를 어떻게 바꿨는지 알아봅니다.
</p>

</div>

<br>

<!-- 기존 방식의 문제 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧠 기존 방식의 문제점
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
NLP 모델을 만들 때 전통적인 방식은 <b>과제가 생길 때마다 처음부터 학습</b>시키는 것이었습니다.<br>
이 방식에는 세 가지 큰 문제가 있습니다.
</p>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start;">
    <div style="flex-shrink:0; font-size:24px;">📊</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:4px;">데이터가 많이 필요합니다</div>
      <div style="font-size:14px; color:#475569; line-height:1.7;">레이블이 달린 <b style="color:#FF6B00;">대용량 데이터</b>를 매번 새로 구해야 합니다.</div>
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start;">
    <div style="flex-shrink:0; font-size:24px;">⏱️</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:4px;">시간과 비용이 큽니다</div>
      <div style="font-size:14px; color:#475569; line-height:1.7;"><b style="color:#FF6B00;">매번 처음부터</b> 학습해야 하므로 자원이 많이 들어갑니다.</div>
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start;">
    <div style="flex-shrink:0; font-size:24px;">🔄</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:4px;">언어 지식이 공유되지 않습니다</div>
      <div style="font-size:14px; color:#475569; line-height:1.7;">언어에 대한 일반 지식이 <b style="color:#FF6B00;">모델마다 따로 쌓입니다.</b></div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 비유 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎓 비유로 이해하기: 대학원생 vs. 학부 신입생
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
새로운 과제가 주어졌을 때, 언어 기초가 이미 갖춰진 사람과 처음부터 배우는 사람의 차이를 생각해봅니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:18px 20px;">
    <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:12px; text-align:center;">🎓 대학원생 (BERT)</div>
    <div style="font-size:14px; color:#334155; line-height:1.8;">
      기본 읽기 능력이 <b style="color:#1681c4;">이미 있어서</b><br>
      전공 내용에만 집중할 수 있습니다.<br><br>
      새로운 과제 적응: <b style="color:#1681c4;">빠름 ✅</b>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px;">
    <div style="font-size:15px; font-weight:900; color:#64748b; margin-bottom:12px; text-align:center;">📖 학부 신입생 (기존 모델)</div>
    <div style="font-size:14px; color:#334155; line-height:1.8;">
      단어, 문법, 독해부터<br>
      <b style="color:#FF6B00;">다시 배워야</b> 합니다.<br><br>
      새로운 과제 적응: <b style="color:#FF6B00;">느림 ❌</b>
    </div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 언어 자체에 대한 기초 지식이 미리 쌓여 있다면, 새로운 과제는 <b style="color:#FF6B00;">훨씬 적은 데이터와 시간</b>으로 학습할 수 있습니다. 이것이 <b>사전학습(Pre-training)</b>의 핵심 아이디어입니다.
</div>

</div>

<br>

<!-- 사전학습 + 미세조정 패러다임 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔁 사전학습 + 미세조정 패러다임
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BERT가 가져온 가장 큰 혁신은 <b>학습 방식 자체의 변화</b>입니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<!-- STEP 1 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 1</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">사전학습 (Pre-training) — "언어 자체를 공부한다"</div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">📚 대규모 텍스트 학습</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">위키피디아, 책 등 <b>수십억 개의 문장</b>으로 언어의 구조를 학습합니다.</div>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">🤖 자기지도학습</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">누가 정답을 알려주지 않아도 됩니다. (Self-supervised Learning)</div>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">🧠 언어 사전지식 획득</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">이 단계를 마친 BERT는 <b>언어에 대한 방대한 사전 지식</b>을 갖게 됩니다.</div>
    </div>
  </div>
</div>

<!-- STEP 2 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 2</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">미세조정 (Fine-tuning) — "특정 과제를 짧게 추가 학습"</div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">🎯 소량 데이터로 충분</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">감정 분류, 질의응답 등 <b>원하는 과제 데이터를 소량만 준비</b>합니다.</div>
    </div>
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">⚡ 짧은 추가 학습</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">사전학습된 BERT 위에 <b>짧게 추가 학습</b>만 하면 됩니다.</div>
    </div>
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">🏆 높은 성능</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">적은 데이터로도 <b>높은 성능</b>을 달성할 수 있습니다.</div>
    </div>
  </div>
</div>

</div>

</div>

<br>

<!-- 비교 다이어그램 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 기존 방식 vs. BERT 방식 비교
</h2>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; overflow:hidden;">
    <div style="background:#FF6B00; padding:10px 16px;">
      <div style="font-size:14px; font-weight:900; color:#fff;">❌ 기존 방식</div>
    </div>
    <div style="background:#1e1e2e; padding:16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#f38ba8;">과제 A 데이터 → 모델 A를 처음부터 학습
과제 B 데이터 → 모델 B를 처음부터 학습
과제 C 데이터 → 모델 C를 처음부터 학습</span>
<span style="color:#6c7086;">→ 비용 ↑, 데이터 ↑, 시간 ↑</span></div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; overflow:hidden;">
    <div style="background:#1681c4; padding:10px 16px;">
      <div style="font-size:14px; font-weight:900; color:#fff;">✅ BERT 방식</div>
    </div>
    <div style="background:#1e1e2e; padding:16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">대규모 텍스트 → BERT 사전학습 (1회)
         ↓
    과제 A 미세조정 (소량 데이터)
    과제 B 미세조정 (소량 데이터)
    과제 C 미세조정 (소량 데이터)</span>
<span style="color:#6c7086;">→ 비용 ↓, 데이터 ↓, 시간 ↓</span></div>
  </div>

</div>

</div>

<br>

<!-- BERT가 바꾼 것들 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🌍 BERT가 바꾼 것들
</h2>

<div style="display: grid; gap: 10px; margin-top: 14px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; font-size:22px;">🔍</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">구글 검색 엔진에 BERT가 도입되어 <b style="color:#1681c4;">검색 품질이 대폭 향상</b>됐습니다.</div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; font-size:22px;">🌱</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">이후 RoBERTa, ALBERT, <b style="color:#1681c4;">KoBERT(한국어 특화)</b> 등 BERT 계열 모델들이 쏟아졌습니다.</div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; font-size:22px;">🤖</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">GPT 계열도 같은 사전학습 패러다임을 따르며 발전, 오늘날의 <b style="color:#1681c4;">ChatGPT로 이어집니다.</b></div>
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
    BERT 이전 모델들은 <b style="color:#FF6B00;">문장의 한 방향만 보거나, 문맥 무관 고정 벡터</b>를 사용했습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    BERT는 <b style="color:#FF6B00;">사전학습 + 미세조정</b> 패러다임을 대중화해 NLP 연구와 응용을 완전히 바꿨습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    방대한 텍스트로 먼저 언어를 익히고(사전학습), 특정 과제에 빠르게 적응(미세조정)하는 방식입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이 구조 덕분에 <b style="color:#FF6B00;">적은 데이터로도 강력한 성능</b>을 낼 수 있게 됐습니다.
  </div>
</div>

</div>

</div>