<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Add &amp; Norm — Layer Normalization
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
벡터 값이 폭발하거나 사라지는 문제를
<b style="color:#1681c4;">Layer Normalization</b>이 어떻게 안정화하는지 알아봅니다.
</p>

</div>

<br>

<!-- 정규화가 필요한 이유 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
⚠️ 학습 중에 벡터 값이 폭발하거나 사라지는 문제
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Transformer는 수백만 번의 계산을 거치며 학습합니다. 이 과정에서 벡터 안의 숫자들이 <b style="color:#FF6B00;">너무 크거나 너무 작아지는</b> 문제가 생깁니다.
</p>

<div style="display: grid; gap: 10px; margin: 16px 0;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#a6e3a1; color:#0f172a; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">정상</div>
    <div style="font-family:Consolas,monospace; font-size:13px; color:#a6e3a1; background:#0f172a; padding:8px 12px; border-radius:8px; flex:1; overflow-x:auto; white-space:nowrap;">
      "나는" → <span style="color:#89dceb;">[0.3, -0.5, 0.8, 0.1, -0.2, ...]</span>
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">폭발</div>
    <div style="font-family:Consolas,monospace; font-size:13px; color:#f38ba8; background:#0f172a; padding:8px 12px; border-radius:8px; flex:1; overflow-x:auto; white-space:nowrap;">
      "나는" → <span style="color:#f38ba8;">[3000, -5000, 8000, 1000, -2000, ...]</span>
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">소실</div>
    <div style="font-family:Consolas,monospace; font-size:13px; color:#6c7086; background:#0f172a; padding:8px 12px; border-radius:8px; flex:1; overflow-x:auto; white-space:nowrap;">
      "나는" → <span style="color:#6c7086;">[0.0003, -0.0005, 0.0008, 0.0001, ...]</span>
    </div>
  </div>

</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
  <div style="background:#fff3eb; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
    값이 <b style="color:#FF6B00;">너무 크면</b> → 계산이 불안정해지고, 학습이 이상한 방향으로 튑니다.
  </div>
  <div style="background:#fff3eb; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
    값이 <b style="color:#FF6B00;">너무 작으면</b> → 기울기가 소실되어 학습이 멈춥니다.
  </div>
</div>

</div>

<br>

<!-- 체온 비유 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🌡️ 비유: 체온 정규화
</h2>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 16px 18px; border-radius: 14px; margin-bottom: 16px;">
  <p style="font-size:14px; color:#334155; line-height:1.8; margin:0;">
    사람의 정상 체온은 36~37°C입니다.
  </p>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 12px;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.7;">
      체온이 <b style="color:#FF6B00;">40°C 넘으면</b><br>→ 몸이 제대로 작동하지 않습니다.
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.7;">
      체온이 <b style="color:#FF6B00;">34°C 아래면</b><br>→ 저체온증으로 위험합니다.
    </div>
  </div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> Layer Normalization은 벡터 값을 <b style="color:#1681c4;">항상 적절한 범위로 조정</b>하는 체온 조절 장치 같은 역할을 합니다.
</div>

</div>

<br>

<!-- Layer Norm이 하는 일 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔧 Layer Normalization이 하는 일
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Layer Normalization은 벡터 안의 숫자들을 <b style="color:#1681c4;">평균 0, 분산 1이 되도록</b> 조정합니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; margin: 14px 0;">
<span style="color: #1681c4; font-weight: 900;">📚 비유: 성적 표준화</span><br>
학교마다 시험 난이도가 달라 A학교 90점과 B학교 90점을 직접 비교하기 어렵습니다.<br>
이를 해결하기 위해 <b style="color:#1681c4;">표준 점수(Z-score)</b>로 변환하는 것과 같습니다.
</div>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 1</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:6px;">벡터 안의 모든 값을 모읍니다</div>
      <div style="font-family:Consolas,monospace; font-size:13px; color:#a6e3a1; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8;">
        "나는" 벡터 = <span style="color:#89dceb;">[2.0, 4.0, 6.0, 8.0]</span>
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 2</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:6px;">평균을 계산합니다</div>
      <div style="font-family:Consolas,monospace; font-size:13px; color:#cba6f7; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8;">
        평균 = (2.0 + 4.0 + 6.0 + 8.0) / 4 = <span style="color:#f9e2af;">5.0</span>
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 3</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:6px;">각 값에서 평균을 뺍니다 <span style="color:#94a3b8; font-size:12px; font-weight:400;">(평균을 0으로 이동)</span></div>
      <div style="font-family:Consolas,monospace; font-size:13px; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">[2.0-5.0, 4.0-5.0, 6.0-5.0, 8.0-5.0]</span>
= <span style="color:#89dceb;">[-3.0,    -1.0,     1.0,     3.0]</span></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 4</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:6px;">표준편차로 나눕니다 <span style="color:#94a3b8; font-size:12px; font-weight:400;">(퍼진 정도를 1로 통일)</span></div>
      <div style="font-family:Consolas,monospace; font-size:13px; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">표준편차 ≈ 2.24</span>
= <span style="color:#a6e3a1;">[-1.34,   -0.45,   0.45,    1.34]</span></div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">결과</div>
    <div style="font-size:14px; font-weight:900; color:#1681c4;">
      평균 ≈ 0, 표준편차 ≈ 1인 <b>안정적인 벡터</b> 완성!
    </div>
  </div>

</div>

</div>

<br>

<!-- Batch Norm vs Layer Norm -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🆚 Batch Normalization vs Layer Normalization
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
Transformer는 <b style="color:#1681c4;">Layer Normalization</b>을 사용합니다. 왜일까요?
</p>

<div style="overflow-x: auto; margin-bottom: 14px;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; font-weight:900;">구분</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">Batch Normalization</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">Layer Normalization</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#475569;">정규화 범위</td>
      <td style="padding:10px 14px; color:#334155;">여러 문장(배치) 전체</td>
      <td style="padding:10px 14px; color:#1681c4; font-weight:900;">하나의 벡터 안에서</td>
    </tr>
    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#475569;">문장 길이가 달라도 OK?</td>
      <td style="padding:10px 14px; color:#FF6B00; font-weight:900;">❌ 길이가 같아야 함</td>
      <td style="padding:10px 14px; color:#1681c4; font-weight:900;">✅ 각 벡터 독립적</td>
    </tr>
    <tr style="background:#fff;">
      <td style="padding:10px 14px; font-weight:900; color:#475569;">텍스트 처리 적합성</td>
      <td style="padding:10px 14px; color:#FF6B00;">낮음</td>
      <td style="padding:10px 14px; color:#1681c4; font-weight:900;">높음</td>
    </tr>
  </tbody>
</table>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 자연어 문장은 <b style="color:#FF6B00;">길이가 제각각</b>입니다.<br>
"안녕" (1단어)과 "나는 오늘 정말 맛있는 점심을 먹었다" (8단어)처럼 동시에 처리할 때,<br>
Layer Normalization은 <b style="color:#FF6B00;">각 단어 벡터를 독립적으로</b> 정규화하기 때문에 문장 길이에 상관없이 잘 작동합니다.
</div>

</div>

<br>

<!-- Add와 Norm이 함께 쓰이는 이유 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔗 Add와 Norm은 왜 항상 함께 쓰일까?
</h2>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Add & Norm 흐름</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">입력 X</span>
  <span style="color:#6c7086;">├── [Multi-Head Attention 또는 FFN]</span> ──┐
  <span style="color:#6c7086;">│</span>                                       <span style="color:#6c7086;">↓</span>
  <span style="color:#6c7086;">└──────────────── </span><span style="color:#f9e2af;">ADD</span><span style="color:#6c7086;"> ──────────────→ </span><span style="color:#a6e3a1;">X + Layer(X)</span>
                                           <span style="color:#6c7086;">↓</span>
                                         <span style="color:#cba6f7;">NORM</span>
                                           <span style="color:#6c7086;">↓</span>
                                   <span style="color:#89dceb;">출력 (안정된 벡터)</span></div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌 순서가 중요한 이유 — Add 먼저, Norm 나중</span><br>
Add(잔차 연결)로 원본 정보를 살리고, 그 합산된 값을 Norm으로 <b style="color:#1681c4;">한 번에 안정화</b>합니다.<br>
만약 순서가 바뀌면(Norm → Add), 정규화된 값에 원본을 더할 때 크기가 달라 불균형이 생깁니다.
</div>

</div>

<br>

<!-- 전체 효과 요약 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 Add &amp; Norm 전체 효과 요약
</h2>

<div style="overflow-x: auto; margin: 14px 0;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; font-weight:900;">구성 요소</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">역할</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">해결하는 문제</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff3eb; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Add (잔차 연결)</td>
      <td style="padding:10px 14px; color:#334155;">원래 입력을 그대로 더함</td>
      <td style="padding:10px 14px; color:#334155;">기울기 소실, 정보 손실</td>
    </tr>
    <tr style="background:#eef7ff;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">Norm (레이어 정규화)</td>
      <td style="padding:10px 14px; color:#334155;">값을 평균 0, 분산 1로 조정</td>
      <td style="padding:10px 14px; color:#334155;">값 폭발/소실, 학습 불안정</td>
    </tr>
  </tbody>
</table>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">⚠️ Add &amp; Norm 없이는?</span><br>
레이어가 4~5개만 넘어도 <b style="color:#FF6B00;">학습이 수렴하지 않습니다.</b> 학습 손실(Loss)이 줄어들지 않거나 오히려 커지고, 번역 품질이 크게 떨어집니다.
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
    <b style="color:#FF6B00;">Layer Normalization(Norm)</b>: 벡터 안의 값들을 <b style="color:#FF6B00;">평균 0, 분산 1</b>로 조정해 학습을 안정화합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    자연어의 <b style="color:#FF6B00;">가변 길이 문장</b> 처리에 적합해 Transformer는 Batch Norm 대신 Layer Norm을 씁니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">Add(잔차 연결) → Norm</b> 순서로 항상 세트로 적용됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Add는 <b style="color:#FF6B00;">정보 보존</b>, Norm은 <b style="color:#FF6B00;">값 안정화</b> 역할을 담당합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    둘 다 없으면 깊은 Transformer는 <b style="color:#FF6B00;">제대로 학습되지 않습니다.</b>
  </div>
</div>

</div>

</div>