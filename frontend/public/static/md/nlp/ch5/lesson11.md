<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Feed Forward Network
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Self-Attention 이후 각 단어를 독립적으로 변환하는
<b style="color:#1681c4;">FFN의 역할</b>과 비선형 변환이 왜 필요한지 알아봅니다.
</p>

</div>

<br>

<!-- FFN 위치 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🗺️ Encoder 레이어에서 FFN의 위치
</h2>

<div style="display: grid; gap: 0; margin: 16px 0;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; text-align:center; font-size:14px; font-weight:900; color:#475569;">Multi-Head Self-Attention</div>
  <div style="text-align:center; color:#94a3b8; font-size:18px; font-weight:900; margin:3px 0;">↓</div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; text-align:center; font-size:14px; font-weight:900; color:#475569;">Add &amp; Norm</div>
  <div style="text-align:center; color:#94a3b8; font-size:18px; font-weight:900; margin:3px 0;">↓</div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:12px 16px; text-align:center; font-size:14px; font-weight:900; color:#FF6B00;">★ Feed Forward Network (FFN) &nbsp;<span style="color:#94a3b8; font-size:12px; font-weight:400;">← 지금 배우는 단계</span></div>
  <div style="text-align:center; color:#94a3b8; font-size:18px; font-weight:900; margin:3px 0;">↓</div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; text-align:center; font-size:14px; font-weight:900; color:#475569;">Add &amp; Norm</div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">🤔 의문:</span> "Self-Attention으로 이미 단어 간 관계를 다 파악했는데, FFN은 왜 또 필요한 걸까요?"
</div>

</div>

<br>

<!-- Self-Attention vs FFN -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔍 Self-Attention과 FFN의 역할 차이
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
Self-Attention과 FFN은 <b>서로 다른 종류의 일</b>을 합니다.
</p>

<div style="overflow-x: auto; margin-bottom: 16px;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; font-weight:900;">구분</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">Self-Attention</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">Feed Forward Network</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#475569;">처리 대상</td>
      <td style="padding:10px 14px; color:#1681c4; font-weight:900;">단어들 사이의 관계</td>
      <td style="padding:10px 14px; color:#FF6B00; font-weight:900;">단어 하나씩 독립적으로</td>
    </tr>
    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#475569;">하는 일</td>
      <td style="padding:10px 14px; color:#334155;">"이 단어와 저 단어가 어떤 관계인가?"</td>
      <td style="padding:10px 14px; color:#334155;">"이 단어의 표현을 더 풍부하게 변환"</td>
    </tr>
    <tr style="background:#fff;">
      <td style="padding:10px 14px; font-weight:900; color:#475569;">단어 간 소통</td>
      <td style="padding:10px 14px; color:#1681c4; font-weight:900;">✅ 있음</td>
      <td style="padding:10px 14px; color:#94a3b8;">❌ 없음 (각 단어 독립 처리)</td>
    </tr>
  </tbody>
</table>
</div>

<!-- 팀 회의 비유 -->
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">🤝 Self-Attention = 팀 회의</div>
    <div style="font-size:13px; color:#475569; line-height:1.8;">팀 전체가 모여 서로 정보를 공유합니다.<br>"나는"이 "먹었다"의 주어, "밥을"이 목적어라는 것을 서로 공유합니다.</div>
  </div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:8px;">📖 FFN = 개인 심화 학습</div>
    <div style="font-size:13px; color:#475569; line-height:1.8;">회의가 끝난 후 각자 자리에서 개인 공부를 합니다.<br>얻은 정보를 바탕으로 <b>각 단어가 자신의 표현을 혼자서 심화</b>합니다.</div>
  </div>
</div>

<div style="margin-top:12px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> 팀 회의(Self-Attention)가 아무리 잘 돼도, 개인 공부(FFN)도 필요합니다.<br>
<b style="color:#1681c4;">두 가지가 합쳐져야 완전한 학습</b>이 됩니다.
</div>

</div>

<br>

<!-- FFN = 패턴 기억 창고 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧠 FFN이 하는 일: "패턴 기억 창고"
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
연구자들은 FFN이 <b>특정 언어 패턴과 지식을 저장하는 역할</b>을 한다고 분석합니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Self-Attention vs FFN 담당 영역</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#89dceb;">Self-Attention이 파악하는 것</span> <span style="color:#6c7086;">(이 문장 안에서):</span>
  → <span style="color:#a6e3a1;">"먹었다"의 주어가 "나는"이다</span>

<span style="color:#cba6f7;">FFN이 저장한 것</span> <span style="color:#6c7086;">(수많은 학습 데이터에서):</span>
  → <span style="color:#a6e3a1;">"먹었다"는 동사다</span>
  → <span style="color:#a6e3a1;">동사 앞에는 주어와 목적어가 온다</span>
  → <span style="color:#a6e3a1;">"밥"은 먹을 수 있는 음식이다</span>
  → <span style="color:#a6e3a1;">"어제"는 과거 시제를 나타낸다</span></div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:12px 14px; text-align:center; font-size:13px; color:#334155; line-height:1.7;">
    <b style="color:#1681c4;">Self-Attention</b><br>"지금 읽는 책의 문맥"
  </div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:12px 14px; text-align:center; font-size:13px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">FFN</b><br>"평생 공부해서 쌓은 배경 지식"
  </div>
</div>

</div>

<br>

<!-- 비선형 변환 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📦 FFN의 또 다른 역할: 비선형 변환
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
Self-Attention의 계산은 기본적으로 <b>선형 변환(행렬 곱셈)</b>입니다.<br>
선형 변환만 계속 쌓으면, 아무리 많이 쌓아도 결국 <b style="color:#FF6B00;">하나의 선형 변환과 수학적으로 동일</b>합니다.
</p>

<div style="display: grid; gap: 10px; margin-bottom: 16px;">
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 16px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:6px;">❌ 선형 변환만 있을 때</div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">직선으로만 데이터를 나눌 수 있음 → <b style="color:#FF6B00;">복잡한 패턴은 표현 불가능</b></div>
  </div>
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:6px;">✅ 비선형 변환(ReLU)이 추가되면</div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">곡선, 꺾인 선 등 복잡한 경계도 표현 가능 → <b style="color:#1681c4;">언어의 복잡한 의미 관계를 학습할 수 있음</b></div>
  </div>
</div>

<!-- ReLU -->
<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 16px 18px; border-radius: 14px;">
  <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">ReLU(Rectified Linear Unit)란?</div>
  <p style="font-size:13px; color:#334155; line-height:1.7; margin: 0 0 10px 0;">
  아주 단순한 규칙입니다. 입력 값이 0보다 크면 그대로 통과, 0 이하면 0으로 만들어 버립니다.
  </p>
  <div style="background-color: #1e1e2e; border-radius: 12px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace;">
    <div style="padding: 14px 18px; font-size: 13px; line-height: 2.2; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">입력:  </span><span style="color:#f38ba8;">[-2.0</span><span style="color:#6c7086;">,  </span><span style="color:#a6e3a1;">0.5</span><span style="color:#6c7086;">,  </span><span style="color:#a6e3a1;">3.0</span><span style="color:#6c7086;">, </span><span style="color:#f38ba8;">-0.3</span><span style="color:#6c7086;">,  </span><span style="color:#a6e3a1;">1.2</span><span style="color:#6c7086;">]</span>
<span style="color:#6c7086;">출력:  </span><span style="color:#6c7086;">[</span><span style="color:#89dceb;"> 0.0</span><span style="color:#6c7086;">,  </span><span style="color:#a6e3a1;">0.5</span><span style="color:#6c7086;">,  </span><span style="color:#a6e3a1;">3.0</span><span style="color:#6c7086;">,  </span><span style="color:#89dceb;">0.0</span><span style="color:#6c7086;">,  </span><span style="color:#a6e3a1;">1.2</span><span style="color:#6c7086;">]</span>
        <span style="color:#89dceb;">↑ 0으로</span>               <span style="color:#89dceb;">↑ 0으로</span></div>
  </div>
  <div style="margin-top:10px; font-size:13px; color:#334155; line-height:1.7; text-align:center;">
    단순하지만, 이 <b style="color:#1681c4;">"0 이하는 잘라내는"</b> 동작이 비선형성을 만들어냅니다.
  </div>
</div>

</div>

<br>

<!-- 동일한 FFN 적용 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 FFN은 모든 단어에 동일하게 적용됩니다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
FFN의 중요한 특성 중 하나는 <b>각 단어 위치에 동일한 FFN이 적용</b>된다는 점입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-bottom: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">동일한 FFN 가중치 적용</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">"나는 밥을 먹었다"</span>

<span style="color:#a6e3a1;">"나는"</span>   → <span style="color:#cba6f7;">[같은 FFN 가중치]</span> → <span style="color:#89dceb;">"나는" 새 벡터</span>
<span style="color:#a6e3a1;">"밥을"</span>   → <span style="color:#cba6f7;">[같은 FFN 가중치]</span> → <span style="color:#89dceb;">"밥을" 새 벡터</span>
<span style="color:#a6e3a1;">"먹었다"</span> → <span style="color:#cba6f7;">[같은 FFN 가중치]</span> → <span style="color:#89dceb;">"먹었다" 새 벡터</span></div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> <b style="color:#1681c4;">같은 FFN</b>이 각 단어 벡터에 <b style="color:#1681c4;">독립적으로</b> 적용됩니다.<br>
Self-Attention처럼 단어들이 서로 참고하지 않습니다.
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
    <b style="color:#FF6B00;">FFN</b>은 Self-Attention 이후, 각 단어 벡터를 <b style="color:#FF6B00;">독립적으로</b> 변환합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Self-Attention이 <b style="color:#FF6B00;">단어 간 관계</b>를 파악한다면, FFN은 각 단어의 <b style="color:#FF6B00;">표현을 심화</b>합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    FFN은 학습 데이터에서 반복 등장하는 <b style="color:#FF6B00;">언어 패턴과 사실 지식</b>을 내부에 저장합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">비선형 함수(ReLU)</b>를 포함해 모델이 복잡한 언어 패턴을 학습할 수 있게 합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    모든 단어 위치에 <b style="color:#FF6B00;">동일한 FFN</b>이 적용됩니다.
  </div>
</div>

<div style="margin-top:12px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> 다음 페이지에서는 FFN의 <b style="color:#1681c4;">내부 구조</b>를 들여다보고, 숫자가 어떻게 변하는지 따라가 봅니다.
</div>

</div>

</div>