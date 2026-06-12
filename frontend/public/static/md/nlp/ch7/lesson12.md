<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 07 · GPT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
컨텍스트 윈도우
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
GPT가 한 번에 처리할 수 있는
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">최대 토큰 수의 한계</span>
와 그로 인해 생기는 현상들을 알아봅니다.
</p>

</div>

<br>

<!-- GPT에는 시야의 한계가 있다 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🪟 GPT에는 "시야의 한계"가 있다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT는 무한히 긴 텍스트를 한 번에 처리할 수 없습니다.<br>
한 번에 처리할 수 있는 <b style="color:#1681c4;">최대 토큰 수</b>가 정해져 있는데, 이것을 <b style="color:#1681c4;">컨텍스트 윈도우(Context Window)</b>라고 합니다.
</p>

</div>

<br>

<!-- 비유로 이해하기 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔭 비유로 이해하기: 이동하는 창문
</h2>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8; margin: 14px 0;">
<span style="color: #FF6B00; font-weight: 900;">🪟 창문 비유</span><br>
책의 내용을 읽는데, 딱 <b>N개 단어만 보이는 창문</b>이 있다고 상상해보세요.
</div>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">창문 크기 = 10단어</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#cdd6f4;">나는 오늘 학교에 가서 친구를 만났다 우리는 함께 점심을</span>
<span style="color:#a6e3a1;"> ↑━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━↑</span>
<span style="color:#6c7086;"> 창문 안에 보이는 10개 단어</span>

<span style="color:#6c7086;">창문을 오른쪽으로 밀면:</span>
<span style="color:#cdd6f4;">              가서 친구를 만났다 우리는 함께 점심을 먹고 공원에</span>
<span style="color:#89dceb;">               ↑━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━↑</span>

<span style="color:#ff5f57;">창문 밖으로 밀려난 "나는 오늘 학교에"는 더 이상 보이지 않음!</span></div>
</div>

<div style="margin-top: 14px; background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align: center; font-weight: 900;">
GPT에서 이 창문이 <span style="color:#FF6B00;">컨텍스트 윈도우</span>입니다. 창문 밖의 내용은 GPT가 기억할 수 없습니다.
</div>

</div>

<br>

<!-- GPT 버전별 컨텍스트 윈도우 크기 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📏 GPT 버전별 컨텍스트 윈도우 크기
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
컨텍스트 윈도우가 클수록 더 긴 대화, 더 긴 문서를 처리할 수 있습니다.
</p>

<div style="overflow-x:auto; margin-top: 14px;">
<table style="width:100%; border-collapse:collapse; font-size:13px; text-align:left;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; font-weight:900; border-radius:8px 0 0 0;">모델</th>
      <th style="padding:10px 14px; font-weight:900; text-align:center;">컨텍스트 윈도우</th>
      <th style="padding:10px 14px; font-weight:900; border-radius:0 8px 0 0;">대략적인 분량</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">GPT-1</td>
      <td style="padding:10px 14px; text-align:center; font-family:Consolas, monospace; color:#334155;">512 토큰</td>
      <td style="padding:10px 14px; color:#334155;">A4 반 페이지 정도</td>
    </tr>
    <tr style="background:#eef7ff;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">GPT-2</td>
      <td style="padding:10px 14px; text-align:center; font-family:Consolas, monospace; color:#334155;">1,024 토큰</td>
      <td style="padding:10px 14px; color:#334155;">A4 1페이지 정도</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">GPT-3</td>
      <td style="padding:10px 14px; text-align:center; font-family:Consolas, monospace; color:#334155;">4,096 토큰</td>
      <td style="padding:10px 14px; color:#334155;">A4 5~6페이지 정도</td>
    </tr>
    <tr style="background:#eef7ff;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">GPT-4</td>
      <td style="padding:10px 14px; text-align:center; font-family:Consolas, monospace; color:#334155;">최대 128,000 토큰</td>
      <td style="padding:10px 14px; color:#334155;">책 한 권 분량</td>
    </tr>
    <tr style="background:#fff3eb;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Claude 3</td>
      <td style="padding:10px 14px; text-align:center; font-family:Consolas, monospace; color:#FF6B00; font-weight:900;">최대 200,000 토큰</td>
      <td style="padding:10px 14px; color:#334155;">책 2~3권 분량</td>
    </tr>
  </tbody>
</table>
</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 토큰과 글자의 관계</span><br>
영어: 단어 1개 ≈ <b>1~2 토큰</b> &nbsp;|&nbsp; 한국어: 어절 1개 ≈ <b>2~4 토큰</b><br>
한국어는 영어보다 토큰을 더 소비하는 경향이 있습니다.
</div>

</div>

<br>

<!-- 컨텍스트 윈도우의 한계 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
⚠️ 컨텍스트 윈도우의 한계: "앞 대화를 잊어버린다"
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
ChatGPT와 오래 대화하다 보면 초반에 나눴던 내용을 <b style="color:#1681c4;">"잊는"</b> 현상이 생깁니다.<br>
이것이 바로 컨텍스트 윈도우 한계 때문입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">대화가 길어질수록</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">┌───────────────────────────────────────────────┐</span>
<span style="color:#6c7086;">│</span>  <span style="color:#cdd6f4;">컨텍스트 윈도우 (최대 4,096 토큰)</span>                  <span style="color:#6c7086;">│</span>
<span style="color:#6c7086;">│</span>                                               <span style="color:#6c7086;">│</span>
<span style="color:#6c7086;">│</span>  <span style="color:#ff5f57;">[앞 대화 ← 창문 밖으로 밀려남]</span>    <span style="color:#a6e3a1;">[최근 대화]</span> <span style="color:#6c7086;">       │</span>
<span style="color:#6c7086;">│</span>   <span style="color:#ff5f57;">(GPT가 더 이상 볼 수 없음)</span>      <span style="color:#a6e3a1;">(GPT가 봄)</span> <span style="color:#6c7086;">      │</span>
<span style="color:#6c7086;">└───────────────────────────────────────────────┘</span>

<span style="color:#89dceb;">사용자: "아까 내가 말한 내 이름 기억해?"</span>
<span style="color:#cdd6f4;">GPT: "죄송합니다, 이전 대화 내용을 찾을 수 없습니다."</span>
<span style="color:#6c7086;">← 이름을 말한 시점이 창문 밖으로 밀려났기 때문</span></div>
</div>

</div>

<br>

<!-- 입력 토큰 + 출력 토큰 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧮 입력 토큰 + 출력 토큰 = 컨텍스트 사용량
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
중요한 점은 <b style="color:#1681c4;">입력과 출력이 모두 컨텍스트 윈도우를 공유</b>한다는 것입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">컨텍스트 윈도우: 4,096 토큰</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#89dceb;">[사용자 질문]</span>         <span style="color:#6c7086;">→</span> <span style="color:#a6e3a1;">500 토큰 사용</span>
<span style="color:#cdd6f4;">[GPT 답변 생성 공간]</span>  <span style="color:#6c7086;">→</span> <span style="color:#ff5f57;">3,596 토큰 남음</span>

<span style="color:#6c7086;">GPT가 생성할 수 있는 최대 답변 길이 = </span><span style="color:#ff5f57;">3,596 토큰</span></div>
</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 긴 질문 = 짧은 답변</span><br>
긴 질문을 할수록 답변에 사용할 수 있는 공간이 줄어듭니다.<br>
API를 쓸 때 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px; font-weight:900;">max_tokens</code> 파라미터로 출력 길이를 제한하는 이유도 이 때문입니다.
</div>

</div>

<br>

<!-- 실제 ChatGPT 입력 구조 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📦 실제 ChatGPT 입력 구조: 프롬프트 형식
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
ChatGPT처럼 대화 형식으로 파인튜닝된 GPT는 대화 내용을 <b style="color:#1681c4;">특정 구조로 포장</b>해서 입력받습니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">GPT에게 실제로 전달되는 입력 구조</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#cba6f7;">&lt;|im_start|&gt;</span><span style="color:#89dceb;">system</span>
<span style="color:#cdd6f4;">당신은 친절한 AI 어시스턴트입니다.</span>
<span style="color:#cba6f7;">&lt;|im_end|&gt;</span>
<span style="color:#cba6f7;">&lt;|im_start|&gt;</span><span style="color:#89dceb;">user</span>
<span style="color:#cdd6f4;">파이썬으로 피보나치 수열 만드는 법 알려줘</span>
<span style="color:#cba6f7;">&lt;|im_end|&gt;</span>
<span style="color:#cba6f7;">&lt;|im_start|&gt;</span><span style="color:#89dceb;">assistant</span></div>
</div>

<div style="margin-top: 14px; background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align: center; font-weight: 900;">
사용자는 <span style="color:#FF6B00;">"파이썬으로 피보나치..."</span>만 썼지만, 내부적으로는 시스템 프롬프트와 대화 이력이 함께 전달됩니다.
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
    <b style="color:#FF6B00;">컨텍스트 윈도우</b>: GPT가 한 번에 처리할 수 있는 최대 토큰 수입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    창문 밖으로 밀려난 내용은 GPT가 <b style="color:#FF6B00;">기억하지 못함</b> → "망각" 현상의 원인입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">입력 + 출력 모두</b> 컨텍스트 윈도우를 사용 → 긴 질문은 답변 공간을 줄입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    ChatGPT는 <b style="color:#FF6B00;">system / user / assistant</b> 역할로 구조화된 형식으로 입력받습니다.
  </div>
</div>

</div>

</div>