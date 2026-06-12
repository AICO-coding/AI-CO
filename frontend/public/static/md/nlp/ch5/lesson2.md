<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Transformer가 등장한 이유 — Transformer는 어떻게 해결했을까?
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
RNN의 한계를 극복한
<b style="color:#1681c4;">Transformer의 핵심 아이디어</b>와
RNN과의 차이를 비교합니다.
</p>

</div>

<br>

<!-- 논문 소개 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🚀 2017년, 논문 한 편이 세상을 바꿨습니다
</h2>

<div style="background-color: #0f172a; border-radius: 14px; padding: 20px 24px; margin: 16px 0; text-align: center;">
  <div style="font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 16px; font-weight: 900; color: #c3e88d; letter-spacing: 0.5px; margin-bottom: 8px;">"Attention Is All You Need"</div>
  <div style="font-size: 13px; color: #8b8bc7;">구글 연구팀 · 2017년</div>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 0;">
이 논문에서 <b>Transformer(트랜스포머)</b>가 처음 소개되었습니다. 핵심 아이디어는 단순했습니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 15px; font-weight: 900; line-height: 1.8; text-align: center; margin-top: 14px;">
<span style="color: #1681c4;">"RNN처럼 순서대로 읽을 필요 없이,<br>Attention만으로 문장 전체를 한 번에 처리할 수 있다."</span>
</div>

</div>

<br>

<!-- 핵심 아이디어 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
👁️ Transformer의 핵심 아이디어: 전체를 한 번에 본다
</h2>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:10px;">🔁 RNN</div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">
      "나는 → 어제 → 먹었다"<br>
      순서대로 <b>한 단어씩</b> 읽음
    </div>
    <div style="margin-top:10px; font-size:12px; background:#0f172a; color:#6c7086; padding:8px 12px; border-radius:8px; font-family:Consolas,monospace; line-height:1.8;">
      책을 처음부터 끝까지<br>한 줄씩 읽는 것
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">⚡ Transformer</div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">
      문장 전체를 <b>동시에</b> 보며<br>모든 단어 관계를 한꺼번에 계산
    </div>
    <div style="margin-top:10px; font-size:12px; background:#0f172a; color:#89dceb; padding:8px 12px; border-radius:8px; font-family:Consolas,monospace; line-height:1.8;">
      책을 펼쳐 전체를<br>한눈에 훑어보는 것
    </div>
  </div>

</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> "나는"과 "먹었다"가 문장 안에서 서로 멀리 있어도,<br>
Transformer는 <b style="color:#FF6B00;">거리에 상관없이</b> 두 단어의 관계를 직접 계산합니다.
</div>

</div>

<br>

<!-- 3가지 핵심 비교 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 RNN vs. Transformer: 3가지 핵심 비교
</h2>

<!-- 비교 1 -->
<div style="margin-bottom: 20px;">
  <div style="font-size:15px; font-weight:900; color:#0f172a; margin-bottom:10px; padding-bottom:6px; border-bottom:2px solid #e2e8f0;">비교 1. 문장 처리 방식</div>

  <div style="overflow-x: auto;">
  <table style="width:100%; border-collapse:collapse; font-size:14px;">
    <thead>
      <tr style="background:#0f172a; color:#c3e88d;">
        <th style="padding:10px 14px; text-align:left; font-weight:900;">구분</th>
        <th style="padding:10px 14px; text-align:left; font-weight:900;">RNN</th>
        <th style="padding:10px 14px; text-align:left; font-weight:900;">Transformer</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
        <td style="padding:10px 14px; font-weight:900; color:#475569;">처리 방식</td>
        <td style="padding:10px 14px; color:#FF6B00;">왼쪽 → 오른쪽, 순서대로</td>
        <td style="padding:10px 14px; color:#1681c4;">전체 단어를 동시에</td>
      </tr>
      <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
        <td style="padding:10px 14px; font-weight:900; color:#475569;">단어 관계 파악</td>
        <td style="padding:10px 14px; color:#FF6B00;">가까운 단어끼리만 잘 파악</td>
        <td style="padding:10px 14px; color:#1681c4;">먼 단어끼리도 직접 연결</td>
      </tr>
      <tr style="background:#fff;">
        <td style="padding:10px 14px; font-weight:900; color:#475569;">속도</td>
        <td style="padding:10px 14px; color:#FF6B00;">순차적이라 느림</td>
        <td style="padding:10px 14px; color:#1681c4;">병렬 처리로 빠름</td>
      </tr>
    </tbody>
  </table>
  </div>
</div>

<!-- 비교 2 -->
<div style="margin-bottom: 20px;">
  <div style="font-size:15px; font-weight:900; color:#0f172a; margin-bottom:10px; padding-bottom:6px; border-bottom:2px solid #e2e8f0;">비교 2. 장기 의존성 해결</div>

  <div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18);">
    <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">장기 의존성 비교</span>
    </div>
    <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#f38ba8;">[RNN 방식]</span>
<span style="color:#a6e3a1;">"나는"</span> → <span style="color:#a6e3a1;">"어제"</span> → <span style="color:#a6e3a1;">"맛있는"</span> → <span style="color:#a6e3a1;">"밥을"</span> → <span style="color:#a6e3a1;">"먹었다"</span>
    <span style="color:#6c7086;">↑ 기억이 점점 희미해짐</span>

<span style="color:#89dceb;">[Transformer 방식]</span>
<span style="color:#a6e3a1;">"나는"</span> <span style="color:#cba6f7;">←────────────────────── </span><span style="color:#a6e3a1;">"먹었다"</span>
        <span style="color:#6c7086;">(직접 Attention 연결)</span></div>
  </div>
</div>

<!-- 비교 3 -->
<div>
  <div style="font-size:15px; font-weight:900; color:#0f172a; margin-bottom:10px; padding-bottom:6px; border-bottom:2px solid #e2e8f0;">비교 3. 병렬 처리</div>

  <div style="display: grid; gap: 10px;">
    <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 16px;">
      <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:8px;">🔁 RNN — 순서대로만 처리</div>
      <div style="font-family:Consolas,monospace; font-size:13px; color:#475569; line-height:1.9; background:#0f172a; padding:10px 14px; border-radius:8px;">
        <span style="color:#a6e3a1;">"나는"</span><span style="color:#6c7086;"> 처리 완료 → </span><span style="color:#a6e3a1;">"어제"</span><span style="color:#6c7086;"> 처리 시작 → </span><span style="color:#a6e3a1;">"밥을"</span><span style="color:#6c7086;"> 처리 시작 → ...</span>
      </div>
    </div>
    <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px;">
      <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:8px;">⚡ Transformer — 동시에 처리</div>
      <div style="font-family:Consolas,monospace; font-size:13px; color:#89dceb; background:#0f172a; padding:10px 14px; border-radius:8px; line-height:1.9;">
        <span style="color:#a6e3a1;">"나는", "어제", "맛있는", "밥을", "먹었다"</span><span style="color:#cba6f7;"> ← 한꺼번에!</span>
      </div>
    </div>
  </div>

  <div style="margin-top:12px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
  <span style="color: #FF6B00; font-weight: 900;">💡</span> GPU가 가진 병렬 연산 능력을 <b style="color:#FF6B00;">Transformer는 100% 활용</b>할 수 있습니다.<br>
  이것이 Transformer가 대규모 데이터 학습에 적합한 이유입니다.
  </div>
</div>

</div>

<br>

<!-- Attention과 Transformer의 관계 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔗 Attention과 Transformer의 관계
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
챕터 4에서 배운 Attention은 "어떤 단어에 집중할지"를 계산하는 <b>하나의 메커니즘</b>이었습니다.<br>
Transformer는 이 Attention을 <b style="color:#1681c4;">건물의 핵심 부품</b>처럼 사용합니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 14px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; text-align:center;">
    <div style="font-size:28px; margin-bottom:8px;">🔭</div>
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:6px;">Attention</div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">멀리 있는 것을 잘 보는<br><b>도구(망원경)</b></div>
  </div>
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; text-align:center;">
    <div style="font-size:28px; margin-bottom:8px;">🏛️</div>
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:6px;">Transformer</div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">망원경을 여러 개 달아<br>사방을 동시에 보는 <b>관측소</b></div>
  </div>
</div>

<div style="margin-top: 14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> RNN 없이, <b style="color:#1681c4;">Attention만을 가지고</b> 전체 구조를 완성한 것이 Transformer의 혁신입니다.
</div>

</div>

<br>

<!-- Transformer가 바꾼 세상 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🌍 Transformer가 바꾼 세상
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Transformer가 등장한 이후, AI 세계는 완전히 바뀌었습니다.
</p>

<div style="display: grid; gap: 8px; margin-top: 14px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">2018</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4;">BERT <span style="color:#6c7086; font-weight:400; font-size:13px;">— 구글</span></div>
      <div style="font-size:13px; color:#475569;">문서 이해, 검색 엔진</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">2018~</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4;">GPT 시리즈 <span style="color:#6c7086; font-weight:400; font-size:13px;">— OpenAI</span></div>
      <div style="font-size:13px; color:#475569;">글쓰기, 코딩, 대화</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">2022</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4;">ChatGPT <span style="color:#6c7086; font-weight:400; font-size:13px;">— OpenAI</span></div>
      <div style="font-size:13px; color:#475569;">일상적인 AI 어시스턴트</div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">현재</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4;">Claude, 번역기(DeepL, 파파고) 등</div>
      <div style="font-size:13px; color:#475569;">분석, 작성, 추론, 자연스러운 기계 번역</div>
    </div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align: center;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 오늘날 우리가 사용하는 대부분의 AI 언어 모델은<br>
<b style="color:#FF6B00;">Transformer 구조를 기반</b>으로 만들어졌습니다.
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
    RNN은 순서대로 처리하는 구조 때문에 <b style="color:#FF6B00;">느리고, 먼 단어 관계를 잘 못 파악</b>했습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Transformer는 <b style="color:#FF6B00;">Attention만으로</b> 문장 전체를 한 번에 처리합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    거리에 상관없이 <b style="color:#FF6B00;">모든 단어 쌍을 직접 연결</b>할 수 있습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">병렬 처리</b>가 가능해 학습이 빠르고, 대규모 데이터를 다룰 수 있습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    현재 우리가 쓰는 거의 모든 언어 AI의 <b style="color:#FF6B00;">기반 구조</b>입니다.
  </div>
</div>

</div>

</div>