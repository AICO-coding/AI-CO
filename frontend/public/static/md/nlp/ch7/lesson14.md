<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 07 · GPT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
GPT가 문장을 생성하는 과정
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
"파이썬 코드 짜줘"라고 입력했을 때,
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">GPT 내부에서 실제로 벌어지는 일</span>
을 시나리오로 따라가며 이해해봅니다.
</p>

</div>

<br>

<!-- 인트로 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💬 "파이썬 코드 짜줘"라고 입력했을 때 실제로 무슨 일이 생길까?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
ChatGPT에 메시지를 보내는 순간, GPT 내부에서는 <b style="color:#1681c4;">눈에 보이지 않는 수많은 단계</b>가 진행됩니다.<br>
7-5까지는 구조를 배웠다면, 7-6에서는 <b>실제 생성 과정을 시나리오로 따라가며</b> 이해해봅니다.
</p>

</div>

<br>

<!-- GPT가 실제로 받는 입력의 전체 모습 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📨 GPT가 실제로 받는 입력의 전체 모습
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
사용자가 <b>"파이썬으로 1부터 10까지 더하는 코드 짜줘"</b>라고 입력하면, GPT는 그 문장만 보는 것이 아닙니다.<br>
대화형 GPT(ChatGPT 등)는 다음과 같은 <b style="color:#1681c4;">구조화된 전체 텍스트</b>를 입력으로 받습니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">GPT가 실제로 받는 전체 입력</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#cba6f7; font-weight:900;">[SYSTEM]</span>
<span style="color:#cdd6f4;">당신은 도움이 되는 AI 어시스턴트입니다.</span>
<span style="color:#cdd6f4;">사용자의 질문에 정확하고 친절하게 답해주세요.</span>

<span style="color:#89dceb; font-weight:900;">[USER]</span>
<span style="color:#cdd6f4;">파이썬으로 1부터 10까지 더하는 코드 짜줘</span>

<span style="color:#a6e3a1; font-weight:900;">[ASSISTANT]</span>
<span style="color:#6c7086;">← 여기부터 GPT가 생성해야 할 부분</span></div>
</div>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="display:grid; grid-template-columns:120px 1fr; gap:10px; align-items:center; background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:11px 14px;">
    <div style="background:#0f172a; color:#cba6f7; padding:5px 10px; border-radius:8px; font-size:12px; font-weight:900; font-family:Consolas, monospace; text-align:center;">[SYSTEM]</div>
    <div style="font-size:14px; color:#334155; line-height:1.6;">서비스 운영자가 GPT의 <b>역할과 규칙</b>을 설정하는 부분</div>
  </div>

  <div style="display:grid; grid-template-columns:120px 1fr; gap:10px; align-items:center; background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px;">
    <div style="background:#0f172a; color:#89dceb; padding:5px 10px; border-radius:8px; font-size:12px; font-weight:900; font-family:Consolas, monospace; text-align:center;">[USER]</div>
    <div style="font-size:14px; color:#334155; line-height:1.6;"><b>실제 사용자가 입력</b>한 메시지</div>
  </div>

  <div style="display:grid; grid-template-columns:120px 1fr; gap:10px; align-items:center; background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px;">
    <div style="background:#0f172a; color:#a6e3a1; padding:5px 10px; border-radius:8px; font-size:12px; font-weight:900; font-family:Consolas, monospace; text-align:center;">[ASSISTANT]</div>
    <div style="font-size:14px; color:#334155; line-height:1.6;">GPT가 <b style="color:#FF6B00;">채워나가야 하는 빈칸</b></div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align: center; font-weight: 900;">
GPT는 이 전체를 하나의 긴 텍스트로 읽고, <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">[ASSISTANT]</code> 이후에 올 내용을 <span style="color:#FF6B00;">예측</span>하는 방식으로 답변을 생성합니다.
</div>

</div>

<br>

<!-- GPT는 의도를 어떻게 파악할까 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧭 GPT는 질문의 "의도"를 어떻게 파악할까?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT에게는 별도의 "의도 분석 모듈" 같은 것이 없습니다.<br>
그럼에도 불구하고 GPT는 <b style="color:#1681c4;">문맥 전체를 읽고 자연스럽게 의도를 파악</b>합니다.<br>
어떻게 가능할까요? 학습 과정에서 <b>수억 개의 대화, 질문-답변 쌍</b>을 학습했기 때문입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">학습 데이터 속 패턴</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#a6e3a1;">"파이썬으로 ~~~하는 코드 짜줘"</span>
  <span style="color:#6c7086;">→ 항상 </span><span style="color:#89dceb;">코드 블록</span><span style="color:#6c7086;">이 뒤따라 나옴</span>

<span style="color:#a6e3a1;">"~~~을 쉽게 설명해줘"</span>
  <span style="color:#6c7086;">→ 항상 </span><span style="color:#89dceb;">쉬운 설명 텍스트</span><span style="color:#6c7086;">가 뒤따라 나옴</span>

<span style="color:#a6e3a1;">"~~~의 장단점 알려줘"</span>
  <span style="color:#6c7086;">→ 항상 </span><span style="color:#89dceb;">목록 형식의 비교</span><span style="color:#6c7086;">가 뒤따라 나옴</span></div>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-top: 16px;">
GPT는 이 패턴들을 학습해서, <b style="color:#1681c4;">"이런 형태의 질문에는 이런 형태의 답변이 이어진다"</b>는 것을 내면화했습니다.
</p>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8; margin-top: 14px;">
<span style="color: #FF6B00; font-weight: 900;">📚 비유: 수백만 권의 책을 읽은 사람</span><br>
수백만 권의 책을 읽은 사람에게 "파이썬 코드 짜는 방법"을 물어보면, 별도의 분석 없이도 자연스럽게 적절한 형식으로 대답할 수 있습니다.<br>
그 사람이 언제 어디서 비슷한 패턴을 봤는지 기억 못 해도, 이미 그 지식이 머릿속에 녹아있기 때문입니다.<br>
<b>GPT도 마찬가지입니다.</b>
</div>

</div>

<br>

<!-- 어텐션이 이 단계에서 하는 일 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎯 어텐션이 이 단계에서 하는 일
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
입력 전체를 받은 GPT는 <b style="color:#1681c4;">Masked Self-Attention</b>을 통해 <b>어떤 부분에 집중해서 답변을 만들지</b> 판단합니다.
</p>

<div style="background-color: #0f172a; border-radius: 12px; padding: 12px 16px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; color: #c3e88d; margin: 14px 0;">
입력: "파이썬으로 1부터 10까지 더하는 코드 짜줘"
</div>

<p style="line-height: 1.8; color: #334155; font-size: 14px; margin-bottom: 10px;">
각 단어가 받는 어텐션 가중치 (직관적 표현):
</p>

<div style="display: grid; gap: 10px;">

  <div style="display:grid; grid-template-columns:110px 1fr 90px; gap:12px; align-items:center;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:7px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center;">파이썬</div>
    <div style="background:#f1f5f9; border-radius:999px; height:14px; overflow:hidden;">
      <div style="background:#FF6B00; width:100%; height:100%; border-radius:999px;"></div>
    </div>
    <div style="font-size:12px; color:#475569; text-align:right;">매우 중요</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 90px; gap:12px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; color:#1681c4; padding:7px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center;">1부터 10</div>
    <div style="background:#f1f5f9; border-radius:999px; height:14px; overflow:hidden;">
      <div style="background:#1681c4; width:80%; height:100%; border-radius:999px;"></div>
    </div>
    <div style="font-size:12px; color:#475569; text-align:right;">중요</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 90px; gap:12px; align-items:center;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:7px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center;">더하는</div>
    <div style="background:#f1f5f9; border-radius:999px; height:14px; overflow:hidden;">
      <div style="background:#FF6B00; width:100%; height:100%; border-radius:999px;"></div>
    </div>
    <div style="font-size:12px; color:#475569; text-align:right;">매우 중요</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 90px; gap:12px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; color:#1681c4; padding:7px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center;">코드</div>
    <div style="background:#f1f5f9; border-radius:999px; height:14px; overflow:hidden;">
      <div style="background:#1681c4; width:60%; height:100%; border-radius:999px;"></div>
    </div>
    <div style="font-size:12px; color:#475569; text-align:right;">중요</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 90px; gap:12px; align-items:center;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; color:#475569; padding:7px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center;">짜줘</div>
    <div style="background:#f1f5f9; border-radius:999px; height:14px; overflow:hidden;">
      <div style="background:#94a3b8; width:40%; height:100%; border-radius:999px;"></div>
    </div>
    <div style="font-size:12px; color:#475569; text-align:right;">보통</div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
이 가중치들이 합산되어 <b style="color:#FF6B00;">"파이썬으로 범위 내 숫자를 합산하는 코드"</b>라는 <b>응답의 방향성</b>이 벡터 안에 녹아듭니다.
</div>

</div>

<br>

<!-- 응답의 형식도 자동으로 결정된다 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📋 응답의 형식도 자동으로 결정된다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT는 내용뿐만 아니라 <b style="color:#1681c4;">어떤 형식으로 답할지</b>도 자동으로 판단합니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<!-- 코드 짜줘 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">입력</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">"코드 짜줘"</div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:11px 14px; font-size:13px; color:#334155; line-height:1.6;">
      <b style="color:#1681c4;">학습 패턴</b><br>코드 블록(```) 형식이 뒤따름
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:13px; color:#334155; line-height:1.6;">
      <b style="color:#FF6B00;">결과</b><br>코드 블록 형식으로 시작할 확률이 높음
    </div>
  </div>
</div>

<!-- 설명해줘 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">입력</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">"설명해줘"</div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:13px; color:#334155; line-height:1.6;">
      <b style="color:#1681c4;">학습 패턴</b><br>산문 설명 텍스트가 뒤따름
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:13px; color:#334155; line-height:1.6;">
      <b style="color:#FF6B00;">결과</b><br>일반 문장으로 시작할 확률이 높음
    </div>
  </div>
</div>

<!-- 비교해줘 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">입력</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">"비교해줘"</div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:11px 14px; font-size:13px; color:#334155; line-height:1.6;">
      <b style="color:#1681c4;">학습 패턴</b><br>표나 목록이 뒤따름
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:13px; color:#334155; line-height:1.6;">
      <b style="color:#FF6B00;">결과</b><br>마크다운 표나 불릿 포인트로 시작할 확률이 높음
    </div>
  </div>
</div>

</div>

<div style="margin-top: 14px; background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align: center; font-weight: 900;">
형식 판단 역시 별도의 규칙이 아니라, 학습 데이터에서 <span style="color:#FF6B00;">자연스럽게 익힌 패턴</span>입니다.
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
    GPT는 사용자 메시지만이 아니라 <b style="color:#FF6B00;">시스템 프롬프트 + 대화 이력 전체</b>를 입력으로 받습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    별도의 "의도 분석" 없이, <b style="color:#FF6B00;">패턴 학습</b>으로 질문의 의도와 적절한 형식을 자동 파악합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    어텐션이 중요한 단어에 집중해 <b style="color:#FF6B00;">응답 방향성을 벡터에 녹여냅니다.</b>
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    "코드 짜줘", "설명해줘", "비교해줘" 등 <b style="color:#FF6B00;">요청 형식에 따라 출력 형식도 달라집니다.</b>
  </div>
</div>

</div>

</div>