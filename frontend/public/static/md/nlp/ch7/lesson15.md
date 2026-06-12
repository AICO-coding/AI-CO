<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 07 · GPT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
첫 단어부터 마지막 단어까지, 한 토큰씩 따라가보기
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
GPT가 답변을 생성하는 과정을
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">슬로우 모션</span>
으로 한 토큰씩 따라가 봅니다.
</p>

</div>

<br>

<!-- 인트로 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎬 생성 과정을 슬로우 모션으로 보기
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT가 <b>"파이썬으로 1부터 10까지 더하는 코드 짜줘"</b>에 답변을 생성한다고 합시다.<br>
실제 생성은 눈 깜짝할 사이에 일어나지만, 내부적으로는 <b style="color:#1681c4;">수십 번의 단계</b>를 거칩니다.<br>
그 과정을 <b>슬로우 모션으로</b> 하나씩 따라가 봅니다.
</p>

</div>

<br>

<!-- 0단계 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="display:flex; gap:10px; align-items:center; margin-bottom:14px;">
  <div style="background:#0f172a; color:#c3e88d; padding:5px 13px; border-radius:999px; font-size:13px; font-weight:900;">0단계</div>
  <h2 style="margin: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
  🔵 출발 — 응답의 첫 토큰을 결정한다
  </h2>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT가 입력 전체를 처리한 뒤, <b style="color:#1681c4;">첫 번째 토큰</b>을 만들어냅니다.<br>
이것이 답변의 방향을 사실상 결정하는 순간입니다.
</p>

<div style="background-color: #0f172a; border-radius: 12px; padding: 12px 16px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; color: #c3e88d; margin: 14px 0; line-height:1.8;">
입력 전체를 Decoder에 통과시킴 → 마지막 위치의 벡터에서 확률 분포 계산
</div>

<p style="font-size: 14px; color: #334155; margin-bottom: 10px; font-weight: 900;">
첫 번째 토큰 후보들:
</p>

<div style="display: grid; gap: 8px;">

  <div style="display:grid; grid-template-columns:110px 1fr 60px 1fr; gap:12px; align-items:center;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:6px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center; font-family:Consolas, monospace;">"물론"</div>
    <div style="background:#f1f5f9; border-radius:999px; height:12px; overflow:hidden;"><div style="background:#FF6B00; width:14.2%; height:100%;"></div></div>
    <div style="font-size:13px; color:#0f172a; font-weight:900; text-align:right;">14.2%</div>
    <div style="font-size:12px; color:#94a3b8;">동의/수락의 서두</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 60px 1fr; gap:12px; align-items:center;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; color:#475569; padding:6px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center; font-family:Consolas, monospace;">"아래"</div>
    <div style="background:#f1f5f9; border-radius:999px; height:12px; overflow:hidden;"><div style="background:#94a3b8; width:11.8%; height:100%;"></div></div>
    <div style="font-size:13px; color:#0f172a; font-weight:900; text-align:right;">11.8%</div>
    <div style="font-size:12px; color:#94a3b8;">"아래 코드를..." 서두</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 60px 1fr; gap:12px; align-items:center;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; color:#475569; padding:6px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center; font-family:Consolas, monospace;">"파이썬"</div>
    <div style="background:#f1f5f9; border-radius:999px; height:12px; overflow:hidden;"><div style="background:#94a3b8; width:10.3%; height:100%;"></div></div>
    <div style="font-size:13px; color:#0f172a; font-weight:900; text-align:right;">10.3%</div>
    <div style="font-size:12px; color:#94a3b8;">언어 이름으로 시작</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 60px 1fr; gap:12px; align-items:center;">
    <div style="background:#eef7ff; border:2px solid #1681c4; color:#1681c4; padding:6px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center; font-family:Consolas, monospace;">"```"</div>
    <div style="background:#f1f5f9; border-radius:999px; height:12px; overflow:hidden;"><div style="background:#1681c4; width:9.7%; height:100%;"></div></div>
    <div style="font-size:13px; color:#1681c4; font-weight:900; text-align:right;">9.7%</div>
    <div style="font-size:12px; color:#1681c4; font-weight:900;">코드 블록 바로 시작 ✅ 선택</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 60px 1fr; gap:12px; align-items:center;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; color:#475569; padding:6px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center; font-family:Consolas, monospace;">"다음은"</div>
    <div style="background:#f1f5f9; border-radius:999px; height:12px; overflow:hidden;"><div style="background:#94a3b8; width:8.9%; height:100%;"></div></div>
    <div style="font-size:13px; color:#0f172a; font-weight:900; text-align:right;">8.9%</div>
    <div style="font-size:12px; color:#94a3b8;">...</div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 Top-p(0.9) + Temperature(0.8)</span> 적용 후 선택: <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px; font-weight:900;">"```"</code><br>
GPT가 코드 블록 마크(<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">```</code>)를 첫 토큰으로 선택했습니다. 이것은 <b>"이 답변은 코드로 시작하겠다"</b>는 결정입니다.
</div>

</div>

<br>

<!-- 1단계 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="display:flex; gap:10px; align-items:center; margin-bottom:14px;">
  <div style="background:#0f172a; color:#c3e88d; padding:5px 13px; border-radius:999px; font-size:13px; font-weight:900;">1단계</div>
  <h2 style="margin: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
  🔵 코드 블록의 언어 선언
  </h2>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
첫 토큰이 <code style="background:#f8fafc; border:1px solid #e2e8f0; color:#1681c4; padding:2px 6px; border-radius:5px; font-weight:900;">```</code> 로 결정됐으니, 이제 어떤 언어인지 선언해야 합니다.
</p>

<div style="background-color: #0f172a; border-radius: 12px; padding: 12px 16px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; color: #c3e88d; margin: 14px 0; line-height:1.8;">
지금까지 생성된 토큰: ["```"]   →   새 입력 = 원본 입력 + ["```"]
</div>

<p style="font-size: 14px; color: #334155; margin-bottom: 10px; font-weight: 900;">
확률 분포:
</p>

<div style="display: grid; gap: 8px;">

  <div style="display:grid; grid-template-columns:110px 1fr 60px 1fr; gap:12px; align-items:center;">
    <div style="background:#eef7ff; border:2px solid #1681c4; color:#1681c4; padding:6px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center; font-family:Consolas, monospace;">"python"</div>
    <div style="background:#f1f5f9; border-radius:999px; height:12px; overflow:hidden;"><div style="background:#1681c4; width:82.4%; height:100%;"></div></div>
    <div style="font-size:13px; color:#1681c4; font-weight:900; text-align:right;">82.4%</div>
    <div style="font-size:12px; color:#1681c4; font-weight:900;">✅ 선택</div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 60px 1fr; gap:12px; align-items:center;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; color:#475569; padding:6px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center; font-family:Consolas, monospace;">"py"</div>
    <div style="background:#f1f5f9; border-radius:999px; height:12px; overflow:hidden;"><div style="background:#94a3b8; width:10.1%; height:100%;"></div></div>
    <div style="font-size:13px; color:#0f172a; font-weight:900; text-align:right;">10.1%</div>
    <div style="font-size:12px; color:#94a3b8;"></div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 60px 1fr; gap:12px; align-items:center;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; color:#475569; padding:6px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center; font-family:Consolas, monospace;">"Python"</div>
    <div style="background:#f1f5f9; border-radius:999px; height:12px; overflow:hidden;"><div style="background:#94a3b8; width:5.3%; height:100%;"></div></div>
    <div style="font-size:13px; color:#0f172a; font-weight:900; text-align:right;">5.3%</div>
    <div style="font-size:12px; color:#94a3b8;"></div>
  </div>

  <div style="display:grid; grid-template-columns:110px 1fr 60px 1fr; gap:12px; align-items:center;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; color:#475569; padding:6px 10px; border-radius:8px; font-weight:900; font-size:13px; text-align:center; font-family:Consolas, monospace;">"java"</div>
    <div style="background:#f1f5f9; border-radius:999px; height:12px; overflow:hidden;"><div style="background:#94a3b8; width:0.8%; height:100%;"></div></div>
    <div style="font-size:13px; color:#0f172a; font-weight:900; text-align:right;">0.8%</div>
    <div style="font-size:12px; color:#94a3b8;">...</div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align: center; font-weight: 900;">
학습 과정에서 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">```python</code> 이라는 패턴을 수없이 봤기 때문에 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">```</code> 다음에 <span style="color:#FF6B00;">"python"</span>이 올 확률이 압도적으로 높습니다.
</div>

</div>

<br>

<!-- 2~5단계 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="display:flex; gap:10px; align-items:center; margin-bottom:14px;">
  <div style="background:#0f172a; color:#c3e88d; padding:5px 13px; border-radius:999px; font-size:13px; font-weight:900;">2~5단계</div>
  <h2 style="margin: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
  🔵 코드 내용 생성 — GPT가 코드를 "작성"하는 방식
  </h2>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
이제 실제 코드가 나옵니다. GPT는 코드도 자연어와 똑같이 <b style="color:#1681c4;">토큰 하나씩</b> 생성합니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">토큰별 생성 과정 (지금까지: "```python")</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.3; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#a6e3a1;">"\n"</span>     <span style="color:#6c7086;">(줄바꿈)               </span> <span style="color:#89dceb;">확률: 91.2%</span> <span style="color:#ff5f57;">→ 선택</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">"total"</span> <span style="color:#6c7086;">(변수명 시작)         </span> <span style="color:#89dceb;">확률: 34.1%</span> <span style="color:#ff5f57;">→ 선택</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">" ="</span>    <span style="color:#6c7086;">(대입 연산자)          </span> <span style="color:#89dceb;">확률: 78.3%</span> <span style="color:#ff5f57;">→ 선택</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">" 0"</span>    <span style="color:#6c7086;">(초기값)               </span> <span style="color:#89dceb;">확률: 65.7%</span> <span style="color:#ff5f57;">→ 선택</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">"\n"</span>    <span style="color:#6c7086;">(줄바꿈)               </span> <span style="color:#89dceb;">확률: 87.4%</span> <span style="color:#ff5f57;">→ 선택</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">"for"</span>   <span style="color:#6c7086;">(반복문 시작)          </span> <span style="color:#89dceb;">확률: 72.1%</span> <span style="color:#ff5f57;">→ 선택</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">" i"</span>    <span style="color:#6c7086;">(반복 변수)            </span> <span style="color:#89dceb;">확률: 55.8%</span> <span style="color:#ff5f57;">→ 선택</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">" in"</span>   <span style="color:#6c7086;">                       </span> <span style="color:#89dceb;">확률: 94.6%</span> <span style="color:#ff5f57;">→ 선택</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">" range"</span> <span style="color:#6c7086;">(범위 함수)           </span> <span style="color:#89dceb;">확률: 61.3%</span> <span style="color:#ff5f57;">→ 선택</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">"(1"</span>    <span style="color:#6c7086;">                       </span> <span style="color:#89dceb;">확률: 48.7%</span> <span style="color:#ff5f57;">→ 선택</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">","</span>     <span style="color:#6c7086;">                       </span> <span style="color:#89dceb;">확률: 88.2%</span> <span style="color:#ff5f57;">→ 선택</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">" 11"</span>   <span style="color:#6c7086;">(10까지 = 11 미포함)   </span> <span style="color:#89dceb;">확률: 43.9%</span> <span style="color:#ff5f57;">→ 선택</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">"):"</span>    <span style="color:#6c7086;">                       </span> <span style="color:#89dceb;">확률: 96.1%</span> <span style="color:#ff5f57;">→ 선택</span>
<span style="color:#6c7086;">...</span></div>
</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡 GPT가 range(1, 11)을 쓴 이유</span><br>
<b>"1부터 10까지"</b>라는 사람의 말을 GPT는 파이썬에서 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px; font-weight:900;">range(1, 11)</code>로 표현해야 한다는 것을 별도의 "번역 규칙" 없이 학습 데이터의 패턴으로 알고 있습니다.<br>
수백만 개의 파이썬 코드를 학습하면서 <b>"1부터 10까지" → range(1, 11)</b> 이라는 패턴이 반복됐기 때문입니다.
</div>

</div>

<br>

<!-- 최종 단계 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="display:flex; gap:10px; align-items:center; margin-bottom:14px;">
  <div style="background:#0f172a; color:#c3e88d; padding:5px 13px; border-radius:999px; font-size:13px; font-weight:900;">최종 단계</div>
  <h2 style="margin: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
  🔵 생성 완료 신호
  </h2>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
코드가 완성된 뒤, GPT는 <b style="color:#1681c4;">언제 멈출지</b>도 스스로 판단합니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">마무리 토큰 생성</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">...</span>
<span style="color:#cdd6f4;">"print"("total")</span>
<span style="color:#cdd6f4;">"\n"</span>
<span style="color:#89dceb;">"```"</span>         <span style="color:#6c7086;">← 코드 블록 닫기</span>
<span style="color:#cdd6f4;">"\n"</span>
<span style="color:#cdd6f4;">"\n"</span>
<span style="color:#a6e3a1;">"이 코드는"</span>   <span style="color:#6c7086;">← 설명 시작</span>
<span style="color:#a6e3a1;">" 1부터"</span>
<span style="color:#a6e3a1;">" 10까지"</span>
<span style="color:#a6e3a1;">"의 합을"</span>
<span style="color:#a6e3a1;">" 계산합니다"</span>
<span style="color:#a6e3a1;">"."</span>
<span style="color:#ff5f57;">&lt;|endoftext|&gt;</span>  <span style="color:#6c7086;">← 종료 토큰 → 생성 멈춤</span></div>
</div>

<div style="margin-top: 14px; background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align: center; font-weight: 900;">
종료 토큰의 확률이 충분히 높아지는 시점에 생성이 멈춥니다. <span style="color:#FF6B00;">언제 멈출지</span>도 "이런 답변 뒤에는 여기서 끝났다"는 패턴으로 학습된 것입니다.
</div>

</div>

<br>

<!-- 최종 생성된 답변 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📝 최종 생성된 답변
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
위 과정을 거쳐 만들어진 전체 답변:
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 최종 답변</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 1.9; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#89dceb;">```python</span>
<span style="color:#cdd6f4;">total = 0</span>
<span style="color:#cba6f7;">for</span> <span style="color:#cdd6f4;">i </span><span style="color:#cba6f7;">in</span> <span style="color:#cdd6f4;">range(1, 11):</span>
<span style="color:#cdd6f4;">    total += i</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(total)</span>
<span style="color:#89dceb;">```</span>

<span style="color:#a6e3a1;">이 코드는 1부터 10까지의 합을 계산합니다.</span></div>
</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align: center; font-weight: 900;">
총 <span style="color:#FF6B00;">약 40~50개의 토큰</span>이 순서대로 선택되어 이 답변이 만들어졌습니다.<br>
각 토큰이 선택될 때마다 <span style="color:#FF6B00;">Decoder 전체를 한 번씩 통과</span>했습니다.
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
    첫 토큰 선택이 <b style="color:#FF6B00;">답변의 방향</b>을 결정합니다 (코드 블록으로 시작 vs 문장으로 시작).
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    코드도 자연어와 동일하게 <b style="color:#FF6B00;">토큰 하나씩</b> 생성됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    GPT는 <code style="background:#f8fafc; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">range(1, 11)</code> 같은 프로그래밍 관용 표현을 <b style="color:#FF6B00;">패턴 학습</b>으로 알고 있습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    종료 토큰(<code style="background:#f8fafc; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">&lt;|endoftext|&gt;</code>)의 확률이 높아지는 시점에 <b style="color:#FF6B00;">스스로 멈춥니다.</b>
  </div>
</div>

</div>

</div>