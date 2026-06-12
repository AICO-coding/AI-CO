<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Bag of Words (BoW)
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
BoW는
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">단어의 순서는 무시하고, 등장 횟수만 세어</span>
문서를 벡터로 표현하는 방법입니다.
</p>

</div>

<br>

<!-- BoW란 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎒 Bag of Words란?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
<b>Bag of Words(BoW)</b>를 직역하면 <b style="color:#1681c4;">"단어들의 가방"</b>입니다.<br>
이름이 왜 "가방"일까요?
</p>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8; margin: 14px 0;">
<span style="color: #FF6B00; font-weight: 900;">🎒 가방 비유</span><br>
책 한 권을 가방에 넣고 마구 흔들면, 단어들이 가방 안에 뒤죽박죽 섞입니다.<br>
순서는 사라지고, <b>"어떤 단어가 몇 개 들어있는지만 남습니다."</b>
</div>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">BoW 흐름 예시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">문장:</span>  <span style="color:#a6e3a1;">"나는 학교에 갔다. 학교에서 공부를 했다."</span>
         <span style="color:#6c7086;">↓ 가방에 넣고 흔들기</span>
<span style="color:#6c7086;">가방 안: </span><span style="color:#89dceb;">{나는:1, 학교에:2, 갔다:1, 학교에서:1, 공부를:1, 했다:1}</span>
         <span style="color:#6c7086;">↓</span>
<span style="color:#ff5f57;">"학교에"가 2번으로 가장 많이 등장 → 이 문장에서 중요한 단어</span></div>
</div>

<div style="margin-top: 14px; background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align: center; font-weight: 900;">
단어의 순서는 무시하고, <span style="color:#FF6B00;">등장 횟수만 셉니다.</span>
</div>

</div>

<br>

<!-- BoW 만드는 방법 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📦 BoW 만드는 방법 (손으로 해보기)
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
다음 세 문장을 BoW로 표현해봅시다.
</p>

<div style="background-color: #0f172a; border-radius: 14px; padding: 14px 20px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; line-height: 2.2; margin: 14px 0;">
  <span style="color:#6c7086;">문서 1: </span><span style="color:#a6e3a1;">"나는 밥을 먹었다"</span><br>
  <span style="color:#6c7086;">문서 2: </span><span style="color:#a6e3a1;">"나는 물을 마셨다"</span><br>
  <span style="color:#6c7086;">문서 3: </span><span style="color:#a6e3a1;">"고양이가 밥을 먹었다"</span>
</div>

<div style="display: grid; gap: 14px; margin-top: 18px;">

<!-- STEP 1 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 1</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">전체 단어 사전 만들기</div>
  </div>
  <p style="margin:0 0 12px 0; font-size:14px; color:#475569; line-height:1.7;">
    세 문장에 등장하는 모든 단어를 모읍니다. (중복 제거)
  </p>
  <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">단어 사전 = </span><span style="color:#a6e3a1;">[고양이가, 나는, 마셨다, 먹었다, 밥을, 물을]</span>
<span style="color:#6c7086;">인덱스   =      </span><span style="color:#89dceb;">0       1      2       3      4     5</span></div>
</div>

<!-- STEP 2 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 2</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">각 문서에서 단어 등장 횟수 세기</div>
  </div>
  <div style="overflow-x:auto;">
  <table style="width:100%; border-collapse:collapse; font-size:13px; text-align:center;">
    <thead>
      <tr style="background:#0f172a; color:#c3e88d;">
        <th style="padding:9px 12px; text-align:left; font-weight:900; border-radius:8px 0 0 0;"></th>
        <th style="padding:9px 8px; font-weight:900;">고양이가(0)</th>
        <th style="padding:9px 8px; font-weight:900;">나는(1)</th>
        <th style="padding:9px 8px; font-weight:900;">마셨다(2)</th>
        <th style="padding:9px 8px; font-weight:900;">먹었다(3)</th>
        <th style="padding:9px 8px; font-weight:900;">밥을(4)</th>
        <th style="padding:9px 8px; font-weight:900; border-radius:0 8px 0 0;">물을(5)</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background:#f8fafc;">
        <td style="padding:9px 12px; font-weight:900; color:#1681c4; text-align:left; font-size:12px;">문서1 "나는 밥을 먹었다"</td>
        <td style="padding:9px 8px; color:#94a3b8;">0</td>
        <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">1</td>
        <td style="padding:9px 8px; color:#94a3b8;">0</td>
        <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">1</td>
        <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">1</td>
        <td style="padding:9px 8px; color:#94a3b8;">0</td>
      </tr>
      <tr style="background:#eef7ff;">
        <td style="padding:9px 12px; font-weight:900; color:#1681c4; text-align:left; font-size:12px;">문서2 "나는 물을 마셨다"</td>
        <td style="padding:9px 8px; color:#94a3b8;">0</td>
        <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">1</td>
        <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">1</td>
        <td style="padding:9px 8px; color:#94a3b8;">0</td>
        <td style="padding:9px 8px; color:#94a3b8;">0</td>
        <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">1</td>
      </tr>
      <tr style="background:#f8fafc;">
        <td style="padding:9px 12px; font-weight:900; color:#1681c4; text-align:left; font-size:12px;">문서3 "고양이가 밥을 먹었다"</td>
        <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">1</td>
        <td style="padding:9px 8px; color:#94a3b8;">0</td>
        <td style="padding:9px 8px; color:#94a3b8;">0</td>
        <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">1</td>
        <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">1</td>
        <td style="padding:9px 8px; color:#94a3b8;">0</td>
      </tr>
    </tbody>
  </table>
  </div>
</div>

<!-- STEP 3 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 3</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">각 문서를 벡터로 표현</div>
  </div>
  <div style="display: grid; gap: 8px;">
    <div style="display:grid; grid-template-columns:80px 1fr; gap:10px; align-items:center;">
      <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:7px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center;">문서 1</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 16px; font-family:Consolas, monospace; font-size:13px;">
        <span style="color:#6c7086;">[0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, 0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, 0]</span>
      </div>
    </div>
    <div style="display:grid; grid-template-columns:80px 1fr; gap:10px; align-items:center;">
      <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:7px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center;">문서 2</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 16px; font-family:Consolas, monospace; font-size:13px;">
        <span style="color:#6c7086;">[0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, 0, 0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">]</span>
      </div>
    </div>
    <div style="display:grid; grid-template-columns:80px 1fr; gap:10px; align-items:center;">
      <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:7px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center;">문서 3</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 16px; font-family:Consolas, monospace; font-size:13px;">
        <span style="color:#6c7086;">[</span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, 0, 0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#6c7086;">, 0]</span>
      </div>
    </div>
  </div>
  <div style="margin-top:12px; background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    이제 세 문서가 각각 <b style="color:#FF6B00;">숫자 벡터로 표현</b>됐습니다!
  </div>
</div>

</div>
</div>

<br>

<!-- 유사도 비교 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔍 BoW로 문서 유사도 비교하기
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BoW 벡터로 만들면 두 문서가 얼마나 비슷한지 <b style="color:#1681c4;">수학적으로 계산</b>할 수 있습니다.
</p>

<div style="display: grid; gap: 12px; margin-top: 16px;">

  <!-- 유사한 경우 -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">✅ 문서 1 vs 문서 3 — 유사한 문서</div>
    <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; margin-bottom:10px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">문서 1 → </span><span style="color:#89dceb;">[0, 1, 0, </span><span style="color:#a6e3a1; font-weight:900;">1, 1</span><span style="color:#89dceb;">, 0]</span>   <span style="color:#6c7086;">(나는 밥을 먹었다)</span>
<span style="color:#6c7086;">문서 3 → </span><span style="color:#89dceb;">[1, 0, 0, </span><span style="color:#a6e3a1; font-weight:900;">1, 1</span><span style="color:#89dceb;">, 0]</span>   <span style="color:#6c7086;">(고양이가 밥을 먹었다)</span></div>
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
      <b style="color:#1681c4;">"먹었다"(3번)</b>, <b style="color:#1681c4;">"밥을"(4번)</b> 위치에서 동일 → <b>유사한 문서</b>
    </div>
  </div>

  <!-- 덜 유사한 경우 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:10px;">🔺 문서 1 vs 문서 2 — 덜 유사한 문서</div>
    <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; margin-bottom:10px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">문서 1 → </span><span style="color:#89dceb;">[0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#89dceb;">, 0, 1, 1, 0]</span>   <span style="color:#6c7086;">(나는 밥을 먹었다)</span>
<span style="color:#6c7086;">문서 2 → </span><span style="color:#89dceb;">[0, </span><span style="color:#a6e3a1; font-weight:900;">1</span><span style="color:#89dceb;">, 1, 0, 0, 1]</span>   <span style="color:#6c7086;">(나는 물을 마셨다)</span></div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
      <b style="color:#FF6B00;">"나는"(1번)</b> 위치만 동일 → <b>덜 유사한 문서</b>
    </div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 BoW의 강력한 점</span><br>
텍스트를 벡터로 바꾸면 <b>수학적 비교가 가능</b>해집니다.
</div>

</div>

</div>