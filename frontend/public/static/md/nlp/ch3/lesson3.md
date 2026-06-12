<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
원-핫 인코딩 (One-Hot Encoding)
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
원-핫 인코딩은 단어를 숫자로 바꾸는
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">가장 단순하고 직관적인 방법</span>
입니다.
</p>

</div>

<br>

<!-- 원-핫 인코딩이란 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔢 원-핫 인코딩이란?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
<b>원-핫 인코딩(One-Hot Encoding)</b>은 단어를 숫자로 바꾸는 가장 단순하고 직관적인 방법입니다.<br>
핵심 아이디어는 딱 하나입니다.
</p>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 15px; font-weight: 900; line-height: 1.8; text-align: center; margin: 14px 0;">
<span style="color: #FF6B00;">해당 단어의 위치만 1, 나머지는 전부 0으로 채운다.</span>
</div>

</div>

<br>

<!-- 출석 체크 비유 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📦 비유로 이해하기: 출석 체크
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
반에 학생이 5명 있고, 각각 이름이 있다고 가정합니다.
</p>

<div style="background-color: #0f172a; border-radius: 14px; padding: 14px 20px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; color: #a6e3a1; line-height: 2; margin: 14px 0; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">자리 번호:  </span>1번(철수)  2번(영희)  3번(민수)  4번(지은)  5번(현우)</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">"영희"를 표현하면?</div>
    <div style="background:#0f172a; border-radius:10px; padding:12px; font-family:Consolas, monospace; font-size:14px; text-align:center; margin-bottom:8px;">
      <span style="color:#6c7086;">[0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, 0, 0, 0]</span>
    </div>
    <div style="font-size:13px; color:#475569; text-align:center;">↑ 영희 자리(2번)만 1</div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">"현우"를 표현하면?</div>
    <div style="background:#0f172a; border-radius:10px; padding:12px; font-family:Consolas, monospace; font-size:14px; text-align:center; margin-bottom:8px;">
      <span style="color:#6c7086;">[0, 0, 0, 0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">]</span>
    </div>
    <div style="font-size:13px; color:#475569; text-align:center;">↑ 현우 자리(5번)만 1</div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡 단어도 마찬가지입니다.</span><br>
단어 사전의 각 단어에 번호를 붙이고, 해당 단어 위치만 1로 표시합니다.
</div>

</div>

<br>

<!-- 원-핫 인코딩 예시 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📋 원-핫 인코딩 예시
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
다음 세 문장이 있다고 합시다.
</p>

<div style="background-color: #0f172a; border-radius: 14px; padding: 14px 20px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; color: #a6e3a1; line-height: 2.2; margin: 14px 0;">
나는 밥을 먹었다<br>
나는 물을 마셨다<br>
고양이가 밥을 먹었다
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 12px;">
이 문장에서 등장하는 단어들(단어 사전):
</p>

<div style="background-color: #1e1e2e; border-radius: 12px; padding: 14px 20px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; color: #cdd6f4; line-height: 2.2; margin-bottom: 16px; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">인덱스:  </span><span style="color:#89dceb;">0</span>     <span style="color:#89dceb;">1</span>     <span style="color:#89dceb;">2</span>       <span style="color:#89dceb;">3</span>     <span style="color:#89dceb;">4</span>       <span style="color:#89dceb;">5</span>
<span style="color:#6c7086;">단어:   </span><span style="color:#a6e3a1;">나는</span>  <span style="color:#a6e3a1;">밥을</span>  <span style="color:#a6e3a1;">먹었다</span>  <span style="color:#a6e3a1;">물을</span>  <span style="color:#a6e3a1;">마셨다</span>  <span style="color:#a6e3a1;">고양이가</span></div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
각 단어의 원-핫 벡터:
</p>

<div style="display: grid; gap: 8px;">

  <div style="display:grid; grid-template-columns:110px 1fr; gap:10px; align-items:center;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:8px 12px; border-radius:8px; font-weight:900; font-size:14px; text-align:center;">나는</div>
    <div style="background:#1e1e2e; border-radius:8px; padding:9px 16px; font-family:Consolas, monospace; font-size:13px;">
      <span style="color:#6c7086;">[</span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, 0, 0, 0, 0, 0]</span>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr; gap:10px; align-items:center;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:8px 12px; border-radius:8px; font-weight:900; font-size:14px; text-align:center;">밥을</div>
    <div style="background:#1e1e2e; border-radius:8px; padding:9px 16px; font-family:Consolas, monospace; font-size:13px;">
      <span style="color:#6c7086;">[0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, 0, 0, 0, 0]</span>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr; gap:10px; align-items:center;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:8px 12px; border-radius:8px; font-weight:900; font-size:14px; text-align:center;">먹었다</div>
    <div style="background:#1e1e2e; border-radius:8px; padding:9px 16px; font-family:Consolas, monospace; font-size:13px;">
      <span style="color:#6c7086;">[0, 0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, 0, 0, 0]</span>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr; gap:10px; align-items:center;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:8px 12px; border-radius:8px; font-weight:900; font-size:14px; text-align:center;">물을</div>
    <div style="background:#1e1e2e; border-radius:8px; padding:9px 16px; font-family:Consolas, monospace; font-size:13px;">
      <span style="color:#6c7086;">[0, 0, 0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, 0, 0]</span>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr; gap:10px; align-items:center;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:8px 12px; border-radius:8px; font-weight:900; font-size:14px; text-align:center;">마셨다</div>
    <div style="background:#1e1e2e; border-radius:8px; padding:9px 16px; font-family:Consolas, monospace; font-size:13px;">
      <span style="color:#6c7086;">[0, 0, 0, 0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, 0]</span>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr; gap:10px; align-items:center;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:8px 12px; border-radius:8px; font-weight:900; font-size:14px; text-align:center;">고양이가</div>
    <div style="background:#1e1e2e; border-radius:8px; padding:9px 16px; font-family:Consolas, monospace; font-size:13px;">
      <span style="color:#6c7086;">[0, 0, 0, 0, 0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">]</span>
    </div>
  </div>

</div>

</div>

</div>