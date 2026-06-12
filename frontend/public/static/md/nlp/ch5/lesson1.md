<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Transformer가 등장한 이유 — RNN은 왜 부족했을까?
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
RNN의 구조적 한계를 이해하고,
<b style="color:#1681c4;">Transformer가 왜 등장했는지</b>를 함께 알아봅니다.
</p>

</div>

<br>

<!-- Attention 복습 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📌 잠깐, 챕터 4에서 배운 Attention을 기억하시나요?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
우리는 챕터 4에서 <b>Attention(어텐션)</b>을 배웠습니다.<br>
어텐션은 "문장 안에서 어떤 단어에 집중해야 할지"를 계산하는 방법이었습니다.
</p>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; margin-top: 12px;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 그런데 Attention이 등장하기 전, NLP에서 문장을 처리하던 방식이 있었습니다.<br>
바로 <b style="color:#FF6B00;">RNN(Recurrent Neural Network, 순환 신경망)</b>입니다.
</div>

</div>

<br>

<!-- RNN이란 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔁 RNN이란?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
RNN은 문장을 <b>왼쪽에서 오른쪽으로 한 단어씩 순서대로</b> 읽는 방식입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 18px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">RNN 처리 방식</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">예시: "나는 어제 맛있는 밥을 먹었다"</span>

<span style="color:#a6e3a1;">"나는"</span> → <span style="color:#a6e3a1;">"어제"</span> → <span style="color:#a6e3a1;">"맛있는"</span> → <span style="color:#a6e3a1;">"밥을"</span> → <span style="color:#a6e3a1;">"먹었다"</span>
  <span style="color:#89dceb;">↓</span>         <span style="color:#89dceb;">↓</span>         <span style="color:#89dceb;">↓</span>           <span style="color:#89dceb;">↓</span>         <span style="color:#89dceb;">↓</span>
<span style="color:#cba6f7;">기억1</span>     <span style="color:#cba6f7;">기억2</span>     <span style="color:#cba6f7;">기억3</span>       <span style="color:#cba6f7;">기억4</span>     <span style="color:#cba6f7;">기억5</span></div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📖 비유:</span> 책을 처음부터 끝까지 <b>한 줄씩 읽으면서 메모를 이어 써 내려가는 것</b>과 같습니다.<br>
앞 단어를 읽을 때마다 <b style="color:#1681c4;">기억(hidden state)</b>을 만들어서 다음 단어로 넘겨줍니다.
</div>

</div>

<br>

<!-- RNN의 3가지 한계 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
⚠️ RNN의 3가지 치명적인 한계
</h2>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<!-- 한계 1 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 1. 긴 문장에서 앞 내용을 잊어버린다 (장기 의존성 문제)</div>

  <p style="font-size:14px; color:#334155; line-height:1.7; margin: 0 0 12px 0;">
  RNN은 앞 단어의 기억을 계속 뒤로 전달합니다. 그런데 문장이 길어질수록 <b style="color:#FF6B00;">앞에서 만든 기억이 희미해집니다.</b>
  </p>

  <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; line-height:2; margin-bottom:12px;">
    "나는 어제 친구와 함께 오랫동안 기다렸다가 <span style="color:#f38ba8;">드디어 먹었다</span>"
  </div>

  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.7;">
    "먹었다"의 주어가 "<b>나는</b>"임을 파악하려면 문장 맨 앞까지 거슬러 가야 합니다.<br>
    RNN은 이 거리가 멀수록 연결이 약해져서 관계를 제대로 파악하지 못합니다.<br>
    → 이것을 <b style="color:#FF6B00;">장기 의존성(Long-term Dependency) 문제</b>라고 합니다.
  </div>
</div>

<!-- 한계 2 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 2. 병렬 처리가 불가능하다 (느린 학습 속도)</div>

  <p style="font-size:14px; color:#334155; line-height:1.7; margin: 0 0 12px 0;">
  RNN은 반드시 <b>순서대로</b> 처리해야 합니다. "나는"을 처리해야 "어제"를 처리할 수 있고, "어제"를 처리해야 "맛있는"을 처리할 수 있습니다.
  </p>

  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.7;">
    마치 10명이 줄 서서 <b>한 명씩 순서대로만</b> 입장할 수 있는 것과 같습니다.<br>
    GPU는 많은 계산을 <b>동시에</b> 처리할 수 있는데, RNN은 이 장점을 전혀 살리지 못합니다.<br>
    → 문장이 길어질수록, 데이터가 많아질수록 <b style="color:#FF6B00;">학습이 매우 느려집니다.</b>
  </div>
</div>

<!-- 한계 3 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 3. 먼 단어끼리의 관계를 잘 파악하지 못한다</div>

  <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; line-height:2; margin-bottom:12px;">
    "The <span style="color:#89dceb;">animal</span> didn't cross the street because <span style="color:#f38ba8;">it</span> was too tired."
  </div>

  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.7;">
    "<b>it</b>"이 "<b>animal(동물)</b>"을 가리키는지 "<b>street(길)</b>"을 가리키는지 파악하려면 문장 전체를 한 번에 봐야 합니다.<br>
    RNN은 왼쪽에서 오른쪽으로만 흐르기 때문에, "it"에 도달했을 때 이미 <b style="color:#FF6B00;">"animal"과의 연결이 약해져 있습니다.</b>
  </div>
</div>

</div>

</div>

<br>

<!-- LSTM, GRU -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💡 LSTM, GRU도 있지만...
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
RNN의 한계를 보완하기 위해 <b>LSTM(Long Short-Term Memory)</b>과 <b>GRU(Gated Recurrent Unit)</b>가 등장했습니다.<br>
이들은 "어떤 기억을 오래 유지할지"를 학습하는 <b style="color:#1681c4;">게이트(Gate) 구조</b>를 추가했습니다.
</p>

<div style="display: grid; gap: 8px; margin-top: 14px;">
  <div style="background:#f8fafc; border-left:4px solid #94a3b8; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    순서대로 처리해야 한다는 <b>구조 자체가 변하지 않았습니다.</b>
  </div>
  <div style="background:#f8fafc; border-left:4px solid #94a3b8; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b>병렬 처리 불가</b> 문제는 여전히 남아있습니다.
  </div>
  <div style="background:#f8fafc; border-left:4px solid #94a3b8; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    매우 긴 문장에서는 여전히 <b>앞 내용을 잊는 문제</b>가 발생합니다.
  </div>
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="font-size: 15px; font-weight: 900; margin-bottom: 14px;">
<span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리
</div>

<div style="overflow-x: auto; margin-bottom: 14px;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; border-radius:8px 0 0 0; font-weight:900;">문제</th>
      <th style="padding:10px 14px; text-align:left; border-radius:0 8px 0 0; font-weight:900;">설명</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">장기 의존성 문제</td>
      <td style="padding:10px 14px; color:#334155;">문장이 길면 앞 내용을 잊어버림</td>
    </tr>
    <tr style="background:#fff8f4; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">순차 처리</td>
      <td style="padding:10px 14px; color:#334155;">병렬 처리 불가 → 학습이 느림</td>
    </tr>
    <tr style="background:#fff;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">먼 단어 관계 파악 어려움</td>
      <td style="padding:10px 14px; color:#334155;">멀리 있는 단어끼리 연결이 약해짐</td>
    </tr>
  </tbody>
</table>
</div>

<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
"문장을 한 단어씩 순서대로 읽어야 한다"는 <b style="color:#FF6B00;">RNN의 구조 자체가 한계</b>였습니다.<br>
이 한계를 근본적으로 해결한 것이 바로 <b style="color:#FF6B00;">Transformer</b>입니다.
</div>

</div>

</div>