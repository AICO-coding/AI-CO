<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Masked Self-Attention
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Decoder가 다음 단어를 만들 때
<b style="color:#1681c4;">미래 단어를 보지 못하도록 가리는</b>
Masked Self-Attention의 이유와 동작 방식을 알아봅니다.
</p>

</div>

<br>

<!-- Decoder에서만 등장하는 특별한 Attention -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎭 Decoder에서만 등장하는 특별한 Attention
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Encoder의 Self-Attention과 Decoder의 Self-Attention은 이름이 비슷하지만,
<b style="color:#1681c4;">결정적인 차이</b>가 하나 있습니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin: 16px 0;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:10px;">Encoder Self-Attention</div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 12px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:1.9; margin-bottom:10px; text-align:center;">
      모든 단어를<br>
      <span style="color:#a6e3a1; font-weight:900;">서로 자유롭게 참고</span>
    </div>
    <div style="font-size:13px; color:#334155; line-height:1.7;">
      입력 문장을 <b style="color:#FF6B00;">전체적으로 이해</b>해야 하므로 문장 전체를 볼 수 있습니다.
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:10px;">Decoder Self-Attention</div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 12px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:1.9; margin-bottom:10px; text-align:center;">
      앞에 나온 단어만 참고<br>
      <span style="color:#ff5f57; font-weight:900;">뒤 단어는 가림</span>
    </div>
    <div style="font-size:13px; color:#334155; line-height:1.7;">
      단어를 <b style="color:#1681c4;">순서대로 생성</b>해야 하므로 미래 단어를 볼 수 없습니다.
    </div>
  </div>

</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌 핵심</span><br>
Decoder에서는 뒤 단어를 <b>의도적으로 가립니다.</b><br>
이 “가린다”는 동작이 <b style="color:#1681c4;">Mask(마스크)</b>이고,
이 방식의 Self-Attention을 <b style="color:#1681c4;">Masked Self-Attention</b>이라고 부릅니다.
</div>

</div>

<br>

<!-- 왜 가려야 할까요 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🤔 왜 가려야 할까요? — “치팅” 문제
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
번역 시험을 보는 학생을 상상해봅시다.
</p>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px; margin: 16px 0;">
  <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:12px;">시험 문제</div>
  <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; line-height:1.9; margin-bottom:14px;">
    "나는 밥을 먹었다"를 영어로 번역하시오.
  </div>

  <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
    <div style="background:#fff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px;">
      <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:8px;">학생 A</div>
      <div style="font-size:13px; color:#334155; line-height:1.7;">정직하게 단어를 하나씩 떠올리며 번역합니다.</div>
    </div>
    <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 16px;">
      <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:8px;">학생 B</div>
      <div style="font-size:13px; color:#334155; line-height:1.7;">이미 완성된 답안지를 보면서 그대로 옮겨 씁니다.</div>
    </div>
  </div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">⚠️</span>
학생 B는 시험 점수는 높을 수 있지만, 실제 번역 능력은 기르지 못합니다.<br>
딥러닝 학습에서도 <b style="color:#FF6B00;">정답을 미리 보면</b> 똑같은 문제가 생깁니다.
</div>

</div>

<br>

<!-- 마스킹 없이 학습하면 생기는 문제 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
⚠️ 마스킹 없이 학습하면 생기는 문제
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Transformer를 학습할 때는 정답 번역문을 알고 있는 상태에서 학습합니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">학습 데이터 예시</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.1; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">입력:</span>  <span style="color:#a6e3a1;">"나는 밥을 먹었다"</span>
<span style="color:#6c7086;">정답:</span>  <span style="color:#a6e3a1;">"I ate rice"</span></div>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
마스킹이 없다면, <b style="color:#FF6B00;">“ate”를 예측하는 학습 과정</b>에서 Decoder가 아래 단어들을 볼 수 있습니다.
</p>

<div style="display:grid; gap:10px; margin: 14px 0;">
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; font-size:18px;">✅</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      <b style="color:#1681c4;">"I"</b> — 이미 생성된 단어라서 참고해도 됩니다.
    </div>
  </div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; font-size:18px;">⚠️</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      <b style="color:#FF6B00;">"ate"</b> — 지금 예측해야 할 단어인데 이미 보여버립니다.
    </div>
  </div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; font-size:18px;">⚠️</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      <b style="color:#FF6B00;">"rice"</b> — 아직 생성하지 않은 미래 단어인데 보여버립니다.
    </div>
  </div>
</div>

<div style="background:#0f172a; border-radius:14px; padding:14px 18px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin: 16px 0;">
<span style="color:#f38ba8;">[학습할 때]</span>  정답 <span style="color:#a6e3a1;">"I ate rice"</span> 전체를 보면서 베낌 → 점수 높음
<span style="color:#89dceb;">[실제 사용]</span>  <span style="color:#a6e3a1;">"I"</span>만 있고 뒤에 뭐가 올지 모름 → 성능이 크게 떨어짐</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 Train-Test Mismatch</span><br>
학습할 때의 조건과 실제 사용할 때의 조건이 달라지는 문제를
<b style="color:#FF6B00;">Train-Test Mismatch</b>라고 합니다.
</div>

</div>

<br>

<!-- 해결책 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
✅ 해결책: 마스킹으로 미래를 차단한다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Masked Self-Attention은 각 단어가
<b style="color:#1681c4;">자신보다 뒤에 있는 단어를 볼 수 없도록</b> 강제합니다.
</p>

<div style="display:grid; gap:10px; margin: 16px 0;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">예측 1</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">“I”를 예측할 때</div>
      <div style="display:flex; gap:8px; flex-wrap:wrap;">
        <span style="background:#eef7ff; border:1px solid #c2e4ff; color:#1681c4; padding:7px 11px; border-radius:999px; font-size:13px; font-weight:900;">✅ &lt;시작&gt;</span>
        <span style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:7px 11px; border-radius:999px; font-size:13px; font-weight:900;">❌ ate</span>
        <span style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:7px 11px; border-radius:999px; font-size:13px; font-weight:900;">❌ rice</span>
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">예측 2</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">“ate”를 예측할 때</div>
      <div style="display:flex; gap:8px; flex-wrap:wrap;">
        <span style="background:#eef7ff; border:1px solid #c2e4ff; color:#1681c4; padding:7px 11px; border-radius:999px; font-size:13px; font-weight:900;">✅ &lt;시작&gt;</span>
        <span style="background:#eef7ff; border:1px solid #c2e4ff; color:#1681c4; padding:7px 11px; border-radius:999px; font-size:13px; font-weight:900;">✅ I</span>
        <span style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:7px 11px; border-radius:999px; font-size:13px; font-weight:900;">❌ rice</span>
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">예측 3</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">“rice”를 예측할 때</div>
      <div style="display:flex; gap:8px; flex-wrap:wrap;">
        <span style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:7px 11px; border-radius:999px; font-size:13px; font-weight:900;">✅ &lt;시작&gt;</span>
        <span style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:7px 11px; border-radius:999px; font-size:13px; font-weight:900;">✅ I</span>
        <span style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:7px 11px; border-radius:999px; font-size:13px; font-weight:900;">✅ ate</span>
      </div>
    </div>
  </div>

</div>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">마스킹 적용 후 볼 수 있는 범위</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.1; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">예측 위치</span>       <span style="color:#89dceb;">&lt;시작&gt;</span>     <span style="color:#89dceb;">I</span>       <span style="color:#89dceb;">ate</span>     <span style="color:#89dceb;">rice</span>
<span style="color:#cba6f7;">I 예측</span>          <span style="color:#a6e3a1;">볼 수 있음</span>   <span style="color:#ff5f57;">가림</span>    <span style="color:#ff5f57;">가림</span>    <span style="color:#ff5f57;">가림</span>
<span style="color:#cba6f7;">ate 예측</span>        <span style="color:#a6e3a1;">볼 수 있음</span>   <span style="color:#a6e3a1;">볼 수 있음</span> <span style="color:#ff5f57;">가림</span>    <span style="color:#ff5f57;">가림</span>
<span style="color:#cba6f7;">rice 예측</span>       <span style="color:#a6e3a1;">볼 수 있음</span>   <span style="color:#a6e3a1;">볼 수 있음</span> <span style="color:#a6e3a1;">볼 수 있음</span> <span style="color:#ff5f57;">가림</span></div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span>
이렇게 하면 학습할 때도 실제 사용할 때와 같은 조건이 됩니다.<br>
즉, 모델은 <b style="color:#1681c4;">앞에 있는 것만 보고 다음 단어를 예측하는 능력</b>을 제대로 기를 수 있습니다.
</div>

</div>

<br>

<!-- 마스크라는 이름의 유래 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧢 “마스크”라는 이름의 유래
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
“마스크(Mask)”는 <b style="color:#1681c4;">가면</b> 또는 <b style="color:#1681c4;">덮개</b>를 뜻합니다.
</p>

<div style="background:#0f172a; border-radius:14px; padding:16px 20px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre; margin: 16px 0;">
<span style="color:#89dceb;">&lt;시작&gt;</span>     <span style="color:#89dceb;">I</span>        <span style="color:#f38ba8;">ate</span>      <span style="color:#f38ba8;">rice</span>
<span style="color:#a6e3a1;">[볼 수 있음]</span>  <span style="color:#a6e3a1;">[볼 수 있음]</span> <span style="color:#ff5f57;">[가림!]</span>  <span style="color:#ff5f57;">[가림!]</span>

<span style="color:#6c7086;">"ate"를 예측하는 시점에서 이후 단어들을 마스크로 가린 모습</span></div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">비유</span><br>
마치 시험지에서 아직 보지 말아야 할 문제에 <b>종이를 덮어두는 것</b>과 같습니다.
</div>

</div>

<br>

<!-- 받아쓰기 시험 비유 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🏫 비유: 받아쓰기 시험
</h2>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 16px 18px; border-radius: 14px; margin: 16px 0;">
  <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">
    선생님이 문장을 천천히 읽어줍니다.
  </div>
  <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; line-height:1.9; text-align:center;">
    "I" / "ate" / "rice"
  </div>
</div>

<div style="display:grid; gap:10px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900;">1</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">“I”를 받아쓸 때: 아직 “ate”와 “rice”는 듣지 못했습니다.</div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900;">2</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">“ate”를 받아쓸 때: “I”는 들었지만 “rice”는 아직 모릅니다.</div>
  </div>
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900;">3</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">“rice”를 받아쓸 때: “I”와 “ate”를 모두 들었습니다.</div>
  </div>
</div>

<div style="margin-top:14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span>
Masked Self-Attention은 이 받아쓰기 시험과 동일한 방식으로 동작합니다.<br>
<b style="color:#1681c4;">이미 들은 것, 즉 이전 단어만 참고해서 다음 단어를 예측</b>합니다.
</div>

</div>

<br>

<!-- 비교 표 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🆚 Encoder Self-Attention vs Masked Self-Attention
</h2>

<div style="overflow-x: auto; margin-top: 14px;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; font-weight:900;">구분</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">Encoder Self-Attention</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">Masked Self-Attention</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#0f172a;">사용 위치</td>
      <td style="padding:10px 14px; color:#475569;">Encoder</td>
      <td style="padding:10px 14px; color:#1681c4; font-weight:900;">Decoder</td>
    </tr>
    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#0f172a;">볼 수 있는 범위</td>
      <td style="padding:10px 14px; color:#475569;">문장 전체 <span style="color:#94a3b8;">(양방향)</span></td>
      <td style="padding:10px 14px; color:#1681c4; font-weight:900;">현재 위치까지만 <span style="color:#94a3b8;">(단방향)</span></td>
    </tr>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#0f172a;">이유</td>
      <td style="padding:10px 14px; color:#475569;">입력 이해 시 전체 문맥 필요</td>
      <td style="padding:10px 14px; color:#1681c4;">생성 시 미래 정보 차단 필요</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 14px; font-weight:900; color:#0f172a;">학습 방식</td>
      <td style="padding:10px 14px; color:#475569;">전체 단어 간 관계 파악</td>
      <td style="padding:10px 14px; color:#1681c4;">앞만 보고 다음 예측하는 능력 훈련</td>
    </tr>
  </tbody>
</table>
</div>

<div style="margin-top:14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span>
Encoder는 입력 문장 <b>전체</b>를 이해해야 하므로 양방향으로 봐도 됩니다.<br>
Decoder는 단어를 <b>순서대로 생성</b>해야 하므로 앞만 볼 수 있어야 합니다.
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
    <b style="color:#FF6B00;">Masked Self-Attention</b>은 Decoder에서 사용하며, 현재 위치 이후의 단어들을 가립니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    마스킹이 없으면 모델이 학습 중 <b style="color:#FF6B00;">정답을 미리 보는 치팅</b>을 하게 됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    치팅으로 학습된 모델은 실제 상황에서 뒤 단어를 볼 수 없기 때문에 성능이 크게 떨어질 수 있습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    마스킹은 학습 환경과 실제 사용 환경을 <b style="color:#FF6B00;">동일하게 맞추는 장치</b>입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    받아쓰기 시험처럼, <b style="color:#FF6B00;">이미 들은 것만 참고해서 다음 단어를 예측</b>하는 훈련입니다.
  </div>
</div>

<div style="margin-top:12px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span>
다음 페이지에서는 마스킹이 <b style="color:#1681c4;">실제 계산에서 어떻게 구현되는지</b>를 살펴봅니다.
</div>

</div>

</div>
