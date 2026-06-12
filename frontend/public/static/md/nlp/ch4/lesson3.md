<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
  Chapter 04 · Attention
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Attention Score란?
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Attention Score는
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">"이 두 단어가 얼마나 관련 있는가"</span>
를 숫자 하나로 표현한 값입니다.<br>
이 점수를 어떻게 계산하는지, 그 핵심 도구인 <b style="color:#1681c4;">내적(Dot Product)</b>부터 이해해봅니다.
</p>

</div>

<br>

<!-- Attention Score란 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎯 Attention Score — 관련성을 숫자로
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
4-2에서 배운 Attention의 첫 번째 단계, <b>"점수 계산"</b>을 더 깊이 들여다봅니다.<br>
Attention Score는 <b style="color:#FF6B00;">현재 처리 중인 단어(Query)</b>와 <b style="color:#1681c4;">참조할 단어(Key)</b> 사이의 관련성 점수입니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 18px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:8px;">Query (질문하는 단어)</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      지금 내가 표현하려는 단어입니다.<br>
      예: <b>"먹었다"</b>를 처리하는 중이라면, "먹었다"가 Query
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:8px;">Key (비교 대상 단어)</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      문장 안의 모든 단어가 각각 Key가 됩니다.<br>
      예: "나는", "사과를", "먹었다" 각각이 Key
    </div>
  </div>

</div>

<div style="margin-top: 14px; background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; font-size:14px; color:#334155; line-height:1.8;">
  <b style="color:#FF6B00;">Attention Score</b> = Query 벡터와 Key 벡터 사이의 <b style="color:#1681c4;">유사도(관련성)</b><br>
  점수가 높을수록 → 두 단어가 서로 밀접하게 연관되어 있음<br>
  점수가 낮을수록 → 두 단어가 별로 관련 없음
</div>

</div>

<br>

<!-- 내적 개념 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📐 핵심 도구 — 내적(Dot Product)
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Attention Score를 계산하는 가장 기본적인 방법이 <b style="color:#1681c4;">내적</b>입니다.<br>
두 벡터의 내적은 <b>"같은 위치의 숫자끼리 곱하고 모두 더하는"</b> 연산입니다.
</p>

<!-- 내적 계산 예시 -->
<div style="background:#0f172a; border-radius:14px; padding:20px; font-family:'JetBrains Mono', Consolas, monospace; font-size:14px; color:#cdd6f4; line-height:2.2; margin:16px 0; overflow-x:auto;">
<span style="color:#6c7086;">예시: "사과를"과 "먹었다"의 내적</span><br><br>
<span style="color:#a6e3a1;">v("사과를")  </span> = [<span style="color:#89dceb;">0.8</span>, <span style="color:#89dceb;">1.0</span>, <span style="color:#89dceb;">0.3</span>, <span style="color:#89dceb;">0.2</span>]<br>
<span style="color:#f38ba8;">v("먹었다")  </span> = [<span style="color:#f38ba8;">0.2</span>, <span style="color:#f38ba8;">0.9</span>, <span style="color:#f38ba8;">1.0</span>, <span style="color:#f38ba8;">0.7</span>]<br><br>
<span style="color:#6c7086;">내적 계산:</span><br>
= (<span style="color:#89dceb;">0.8</span> × <span style="color:#f38ba8;">0.2</span>) + (<span style="color:#89dceb;">1.0</span> × <span style="color:#f38ba8;">0.9</span>) + (<span style="color:#89dceb;">0.3</span> × <span style="color:#f38ba8;">1.0</span>) + (<span style="color:#89dceb;">0.2</span> × <span style="color:#f38ba8;">0.7</span>)<br>
= 0.16 + 0.90 + 0.30 + 0.14<br>
= <span style="color:#c3e88d; font-weight:900;">1.50</span>  <span style="color:#6c7086;">← Attention Score</span>
</div>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:4px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:6px;">내적이 크다 = ?</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      두 벡터가 <b>비슷한 방향</b>을 가리킵니다.<br>
      → 두 단어가 <b style="color:#FF6B00;">의미적으로 가깝거나 관련</b>이 높다는 신호
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:6px;">내적이 작다(또는 음수) = ?</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      두 벡터가 <b>다른 방향</b>을 가리킵니다.<br>
      → 두 단어가 <b style="color:#1681c4;">의미적으로 멀거나 관련</b>이 낮다는 신호
    </div>
  </div>

</div>

</div>

<br>

<!-- 직관적 이해 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧲 내적의 직관 — 화살표가 같은 방향일수록 점수가 높다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
벡터를 화살표로 생각하면 내적의 의미를 직관적으로 이해할 수 있습니다.
</p>

<div style="display:grid; gap:12px; margin-top:16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:16px; align-items:center;">
    <div style="font-size:28px; min-width:40px; text-align:center;">→→</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:4px;">같은 방향</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">내적이 <b style="color:#FF6B00;">크게 양수</b> → 두 단어가 강하게 연관</div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:16px; align-items:center;">
    <div style="font-size:28px; min-width:40px; text-align:center;">→↑</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:4px;">직각 방향</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">내적이 <b style="color:#1681c4;">0에 가까움</b> → 두 단어가 관련 없음</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:16px; align-items:center;">
    <div style="font-size:28px; min-width:40px; text-align:center;">→←</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:4px;">반대 방향</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">내적이 <b style="color:#94a3b8;">음수</b> → 두 단어가 반대 의미를 가짐</div>
    </div>
  </div>

</div>

<div style="margin-top:16px; background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:14px 18px; font-size:14px; color:#334155; line-height:1.8;">
  <span style="color:#FF6B00; font-weight:900;">💡 비유</span><br>
  "사과"와 "먹다"는 자주 같이 쓰이는 단어 → 비슷한 방향의 벡터 → 내적이 큼<br>
  "사과"와 "주다" (대화에서 잘 함께 등장 X) → 다른 방향의 벡터 → 내적이 작음
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size:15px; font-weight:900; margin-bottom:10px;"><span style="color:#FF6B00; font-size:18px;">⚡</span> 핵심 정리</div>
<div style="display:grid; gap:8px;">
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Attention Score = <b style="color:#FF6B00;">Query 벡터 · Key 벡터</b>의 내적값 (관련성 점수)
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    내적이 클수록 두 단어는 서로 <b style="color:#FF6B00;">관련성이 높음</b>, 작을수록 낮음
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    다음 화면에서는 이 점수에 <b style="color:#FF6B00;">왜 √d로 나누는지</b>(Scaling) 배웁니다.
  </div>
</div>
</div>

</div>