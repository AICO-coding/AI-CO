<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Masked Language Modeling (MLM)
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
BERT는 어떻게 "언어를 이해"하도록 학습될까요?<br>
사람이 레이블을 달지 않아도 대규모 학습을 가능하게 하는 <b style="color:#1681c4;">MLM</b>의 핵심 아이디어를 알아봅니다.
</p>

</div>

<br>

<!-- 레이블 문제 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🤔 정답을 어떻게 만들까요?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BERT는 위키피디아, 책 등 <b>수십억 문장</b>으로 사전학습됩니다. 여기서 중요한 질문이 있습니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center; margin: 14px 0 18px 0;">
"정답을 어떻게 만들어요? 사람이 일일이 달아줘야 하나요?"
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">

  <div style="background:#fff1f2; border:2px solid #fca5a5; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#dc2626; margin-bottom:8px;">❌ 기존 방식의 문제</div>
    <div style="font-size:13px; color:#334155; line-height:1.8;">
      감정 분류 모델은 "긍정/부정" 같은 레이블이 필요합니다.<br>
      수십억 문장에 사람이 직접 레이블을 붙이는 건 <b style="color:#dc2626;">불가능</b>합니다.
    </div>
  </div>

  <div style="background:#f0fdf4; border:2px solid #86efac; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#16a34a; margin-bottom:8px;">✅ BERT의 해법: MLM</div>
    <div style="font-size:13px; color:#334155; line-height:1.8;">
      원문 자체를 정답으로 활용합니다.<br>
      <b style="color:#16a34a;">레이블이 필요 없는</b> 자기지도학습(Self-supervised Learning)입니다.
    </div>
  </div>

</div>

</div>

<br>

<!-- 핵심 아이디어 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💡 핵심 아이디어: "원문 자체가 정답"
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">MLM의 핵심은 단순합니다.</p>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:900;">①</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">원래 문장에서 일부 단어를 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 7px; border-radius:6px; font-weight:900;">[MASK]</code>로 가린다</div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:900;">②</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">모델에게 <b style="color:#1681c4;">"가려진 단어가 뭐였을까?"</b> 맞히게 한다</div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:900;">③</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">원래 단어와 비교해서 맞으면 OK, 틀리면 수정 → <b style="color:#1681c4;">원문이 곧 정답!</b></div>
  </div>

</div>

</div>

<br>

<!-- 비유: 빈칸 채우기 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📚 비유: 빈칸 채우기 교재
</h2>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center; margin-bottom: 18px;">
"나는 오늘 ____에서 커피를 마셨다."
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
이 문제를 제대로 풀려면 앞뒤 문맥을 <b>동시에</b> 고려해야 합니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px;">
    <div style="font-size:13px; font-weight:900; color:#64748b; margin-bottom:6px;">⬅️ 앞 문맥</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">"나는 오늘"<br>→ 일상적인 상황</div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px;">
    <div style="font-size:13px; font-weight:900; color:#64748b; margin-bottom:6px;">➡️ 뒤 문맥</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">"에서 커피를 마셨다"<br>→ 커피를 파는 장소</div>
  </div>

</div>

<div style="background:#fff3eb; border:2px solid #ffd0b0; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#FF6B00; font-weight:900;">💡</span> BERT는 이런 빈칸 채우기를 <b style="color:#FF6B00;">수십억 번 반복</b>하면서 언어의 구조, 문법, 단어 간 의미 관계를 스스로 터득합니다.
</div>

</div>

<br>

<!-- 기존 방식과의 비교 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🚧 왜 기존 방식으로는 안 됐나요?
</h2>

<div style="display: grid; gap: 14px; margin-top: 14px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; overflow:hidden;">
    <div style="background:#FF6B00; padding:10px 16px;">
      <div style="font-size:13px; font-weight:900; color:#fff;">❌ GPT 방식 — 다음 단어 예측 (단방향)</div>
    </div>
    <div style="background:#1e1e2e; padding:16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.3; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">입력: "나는 오늘 카페"</span>
<span style="color:#f38ba8;">예측: → "에서" (항상 왼쪽만 보고 오른쪽 예측)</span>

<span style="color:#6c7086;">→ 오른쪽 문맥을 학습에 활용할 수 없습니다.</span></div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; overflow:hidden;">
    <div style="background:#64748b; padding:10px 16px;">
      <div style="font-size:13px; font-weight:900; color:#fff;">⚠️ ELMo 방식 — 양방향이지만 따로따로</div>
    </div>
    <div style="background:#1e1e2e; padding:16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.3; overflow-x:auto; white-space:pre;">
<span style="color:#f9e2af;">왼→오 방향 LM 따로 학습</span>
<span style="color:#f9e2af;">오→왼 방향 LM 따로 학습</span>
<span style="color:#6c7086;">결과를 단순히 합침</span>
<span style="color:#6c7086;">→ 두 방향이 서로 "보이지 않는" 상태로 따로 학습됨</span></div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; overflow:hidden;">
    <div style="background:#1681c4; padding:10px 16px;">
      <div style="font-size:13px; font-weight:900; color:#fff;">✅ BERT MLM — 앞뒤를 동시에</div>
    </div>
    <div style="background:#1e1e2e; padding:16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.3; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">하나의 모델이 앞뒤를 동시에 보면서 빈칸을 채움</span>
<span style="color:#6c7086;">→ 진정한 양방향 이해 학습 가능 ✅</span></div>
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
    MLM은 문장의 일부를 <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 6px; border-radius:4px;">[MASK]</code>로 가리고 원래 단어를 맞히는 학습 방식입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">원문 자체가 정답</b>이라 사람이 레이블을 달 필요 없이 대규모 학습이 가능합니다 (자기지도학습).
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    기존 단방향 예측과 달리 <b style="color:#FF6B00;">앞뒤 문맥을 동시에</b> 활용하도록 모델을 훈련시킵니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이것이 BERT가 진정한 <b style="color:#FF6B00;">양방향 이해</b>를 학습할 수 있는 비결입니다.
  </div>
</div>

</div>

</div>