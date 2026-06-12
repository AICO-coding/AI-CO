<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 07 · GPT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
생성 도중 생기는 문제들
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
GPT가
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">환각, 반복, 앞뒤 불일치</span>
같은 문제를 일으키는 원인을 생성 원리에서 이해해봅니다.
</p>

</div>

<br>

<!-- 인트로 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🤔 GPT가 자신 있게 틀린 말을 하는 이유
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT를 사용하다 보면 분명히 틀린 정보를 자신감 있게 말하는 경우가 있습니다.<br>
예를 들어 존재하지 않는 논문을 그럴듯하게 인용하거나, 실제로는 일어나지 않은 역사적 사건을 설명하기도 합니다.<br>
이것을 <b style="color:#1681c4;">환각(Hallucination)</b>이라고 부릅니다. 왜 이런 일이 생기는지, 생성 과정의 원리에서 이해해봅시다.
</p>

</div>

<br>

<!-- 환각 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
👻 환각(Hallucination): 그럴듯하지만 틀린 내용을 생성하는 이유
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT는 <b>"사실을 찾아오는"</b> 모델이 아닙니다. <b style="color:#1681c4;">"다음에 올 확률이 가장 높은 토큰을 생성하는"</b> 모델입니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<!-- 우연히 맞는 경우 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">✅ 질문: "아인슈타인이 노벨 물리학상을 받은 연도는?"</div>
  <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2; color:#cdd6f4; overflow-x:auto; white-space:pre;">
<span style="color:#89dceb;">"아인슈타인" + "노벨" + "물리학상" + "받은" + "연도"</span>
  <span style="color:#6c7086;">→ 이 패턴 다음에 연도 숫자가 오는 것은 당연한 흐름</span>
  <span style="color:#6c7086;">→ 학습 데이터에서 본 비슷한 패턴들에서 연도를 가져옴</span>
  <span style="color:#a6e3a1;">→ "1921년"이라고 생성 (이 경우는 우연히 맞음)</span></div>
</div>

<!-- 틀린 경우 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
  <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:10px;">⚠️ 질문: "김민준 교수의 2023년 논문 제목은?"</div>
  <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2; color:#cdd6f4; overflow-x:auto; white-space:pre;">
<span style="color:#89dceb;">"교수" + "논문" + "제목" + "은" 패턴</span>
  <span style="color:#6c7086;">→ 논문 제목처럼 생긴 텍스트가 다음에 오는 것이 자연스러움</span>
  <span style="color:#ff5f57;">→ 실제로 그런 논문이 있는지와 무관하게</span>
  <span style="color:#ff5f57;">  그럴듯한 제목을 만들어냄</span></div>
</div>

</div>

<div style="margin-top: 14px; background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 핵심</span><br>
GPT는 데이터베이스를 검색하지 않습니다. <b>"이런 패턴 다음에 오기에 가장 그럴듯한 텍스트"</b>를 생성합니다.<br>
그 텍스트가 사실과 일치하는지는 <b style="color:#FF6B00;">보장되지 않습니다.</b>
</div>

</div>

<br>

<!-- 반복 생성 문제 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔁 반복 생성 문제: 같은 말을 계속 하는 이유
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Temperature가 낮거나 Greedy Decoding을 쓸 때, GPT가 같은 문장이나 구절을 반복하는 현상이 나타납니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">낮은 Temperature 설정 시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#cdd6f4;">"좋은 아침입니다. 오늘도 좋은 하루 되세요.</span>
<span style="color:#ff5f57;"> 좋은 하루 되세요. 좋은 하루 되세요. 좋은 하루 되세요..."</span></div>
</div>

<div style="display: grid; gap: 14px; margin-top: 14px;">

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:10px;">왜 이런 일이 생기나?</div>
  <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    → <b style="color:#FF6B00;">"좋은 하루 되세요"</b> 다음에 올 가장 높은 확률의 토큰 = 또 <b style="color:#FF6B00;">"좋은 하루 되세요"</b><br>
    문맥이 쌓일수록 패턴이 강화되어 <b>반복 루프</b>에 빠짐
  </div>
</div>

</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-top: 16px;">
이를 막기 위해 실제 서비스들은 <b style="color:#1681c4;">반복 패널티(Repetition Penalty)</b>를 적용합니다.<br>
이미 생성된 토큰의 확률을 인위적으로 낮춰서 반복을 억제하는 방법입니다.
</p>

<div style="margin-top: 10px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">🛠️ 반복 패널티 적용 시</span><br>
<b>"좋은 하루 되세요"</b> 이후 같은 토큰 재등장 확률 감소 → <b style="color:#1681c4;">다른 토큰(새로운 내용)</b>을 선택하게 됨
</div>

</div>

<br>

<!-- 앞뒤 일관성 문제 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📏 앞뒤 일관성 문제: 긴 답변에서 말이 바뀌는 이유
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT는 긴 답변을 생성할 때 <b style="color:#1681c4;">초반의 내용을 "잊는"</b> 경향이 있습니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">예시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#89dceb;">앞부분: "파이썬은 느린 언어입니다."</span>
<span style="color:#6c7086;">...200 토큰 후...</span>
<span style="color:#ff5f57;">뒷부분: "파이썬은 빠른 실행 속도가 장점입니다."</span></div>
</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 왜 이런 일이 생기나?</span><br>
GPT는 지금 생성하는 토큰의 <b>바로 앞 맥락</b>에 가장 강하게 집중합니다.<br>
긴 거리의 앞 내용은 어텐션 가중치가 상대적으로 작아져 앞에서 한 말과 모순된 내용이 나올 수 있습니다.
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-top: 16px;">
또한 GPT는 자신이 생성한 텍스트를 <b style="color:#1681c4;">수정하거나 되돌아볼 수 없습니다.</b><br>
한 번 생성한 토큰은 확정이고, 뒤에서 발견한 오류를 앞으로 돌아가 고칠 수 없습니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 14px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:10px;">👤 사람이 글을 쓸 때</div>
    <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:12px; color:#cdd6f4; line-height:2;">
      초안 작성 → 검토 → 수정 → 다시 검토 → 최종 완성
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:10px;">🤖 GPT가 글을 생성할 때</div>
    <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:12px; color:#cdd6f4; line-height:2;">
      토큰1 → 토큰2 → 토큰3 → ... → 토큰N (끝)<br>
      <span style="color:#ff5f57;">(뒤로 돌아가서 수정 불가)</span>
    </div>
  </div>

</div>

</div>

<br>

<!-- Temperature와 품질 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🌡️ Temperature와 품질의 관계
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Temperature 설정이 생성 품질에 미치는 영향을 구체적으로 봅니다.
</p>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; padding: 13px 16px; font-size: 14px; color: #334155; text-align: center; font-weight: 900; margin: 14px 0;">
동일한 질문: <span style="color:#1681c4;">"행복이란 무엇인가?"</span>
</div>

<div style="display: grid; gap: 14px;">

<!-- 0.1 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#94a3b8; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">Temp 0.1</div>
    <div style="font-size:14px; font-weight:900; color:#0f172a;">매우 낮음</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:1.9; margin-bottom:10px;">
    "행복이란 긍정적인 감정 상태를 말합니다.<br>
    행복은 긍정적인 감정을 의미합니다.<br>
    이러한 긍정적인 감정은..."
  </div>
  <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155;">
    → <b>안전하지만 반복적이고 단조로움</b>
  </div>
</div>

<!-- 0.7 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">Temp 0.7</div>
    <div style="font-size:14px; font-weight:900; color:#0f172a;">적당</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:1.9; margin-bottom:10px;">
    "행복이란 단순히 좋은 감정이 아니라,<br>
    자신의 삶에 의미를 느끼는 상태입니다.<br>
    이는 인간 관계, 성취, 그리고 내면의 평화가..."
  </div>
  <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155;">
    → <b style="color:#1681c4;">자연스럽고 다양한 표현</b>
  </div>
</div>

<!-- 1.5 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">Temp 1.5</div>
    <div style="font-size:14px; font-weight:900; color:#0f172a;">높음</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:1.9; margin-bottom:10px;">
    "행복이란 사실 우주적 아이러니의 산물이며,<br>
    우리가 채우려 할수록 더 먼 곳에 있는 무엇,<br>
    마치 수평선처럼 가까워질 수 없는..."
  </div>
  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155;">
    → <b style="color:#FF6B00;">창의적이지만 논점을 벗어날 수 있음</b>
  </div>
</div>

</div>

</div>

<br>

<!-- 실제 서비스가 줄이는 방법 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🛡️ 실제 서비스가 이런 문제를 줄이는 방법
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
실제 ChatGPT, Claude 같은 서비스들은 생성 과정의 문제를 줄이기 위해 다양한 기법을 함께 사용합니다.
</p>

<div style="overflow-x:auto; margin-top: 14px;">
<table style="width:100%; border-collapse:collapse; font-size:13px; text-align:left;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; font-weight:900; border-radius:8px 0 0 0;">문제</th>
      <th style="padding:10px 14px; font-weight:900; border-radius:0 8px 0 0;">대응 방법</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">환각 (틀린 정보 생성)</td>
      <td style="padding:10px 14px; color:#334155;">검색 기능 연결 (RAG), 답변 후 출처 확인 요구</td>
    </tr>
    <tr style="background:#eef7ff;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">반복 생성</td>
      <td style="padding:10px 14px; color:#334155;">반복 패널티 적용</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">앞뒤 불일치</td>
      <td style="padding:10px 14px; color:#334155;">더 긴 컨텍스트 윈도우, 요약 기법</td>
    </tr>
    <tr style="background:#eef7ff;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">유해 콘텐츠 생성</td>
      <td style="padding:10px 14px; color:#334155;">RLHF(인간 피드백 강화학습)로 사후 조정</td>
    </tr>
  </tbody>
</table>
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
    <b style="color:#FF6B00;">환각</b>: GPT는 사실 검색이 아닌 "가장 그럴듯한 패턴"을 생성 → 틀린 정보도 자신 있게 말할 수 있습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">반복</b>: 낮은 Temperature에서 같은 패턴이 강화되어 루프에 빠질 수 있음 → 반복 패널티로 대응합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">불일치</b>: 한 번 생성한 토큰은 수정 불가, 긴 거리 맥락에서 앞뒤가 어긋날 수 있습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    실제 서비스는 <b style="color:#FF6B00;">RAG, RLHF, 반복 패널티</b> 등을 조합해 이런 문제를 완화합니다.
  </div>
</div>

</div>

</div>