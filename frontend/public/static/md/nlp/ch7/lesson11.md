<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 07 · GPT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
GPT의 입력과 출력 구조
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
GPT가 텍스트를
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">토큰 → ID → 벡터</span>
순서로 변환해 처리하는 과정을 알아봅니다.
</p>

</div>

<br>

<!-- GPT는 텍스트를 그대로 받지 않는다 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📥 GPT는 텍스트를 그대로 받지 않는다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
우리가 ChatGPT에 <b>"안녕하세요, 오늘 날씨 알려줘"</b>라고 입력하면, GPT는 이 문장을 <b style="color:#1681c4;">그대로</b> 처리하지 않습니다.<br>
텍스트는 컴퓨터가 처리할 수 있는 <b>숫자</b>로 변환되어야 합니다. 이 과정은 크게 두 단계로 이루어집니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">GPT 입력 처리 흐름</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#a6e3a1;">"안녕하세요, 오늘 날씨 알려줘"</span>
         <span style="color:#6c7086;">↓ STEP 1. 토큰화</span>
<span style="color:#89dceb;">[안녕하세요, ,, 오늘, 날씨, 알려줘]</span>
         <span style="color:#6c7086;">↓ STEP 2. 임베딩</span>
<span style="color:#cdd6f4;">[[0.2, -0.5, ...], [0.8, 0.1, ...], ...]</span>
<span style="color:#6c7086;">(각 토큰이 수백 차원의 벡터로 변환됨)</span>
         <span style="color:#6c7086;">↓ STEP 3. 위치 인코딩 추가 (7-3에서 배움)</span>
<span style="color:#ff5f57;">Decoder 블록으로 전달</span></div>
</div>

</div>

<br>

<!-- STEP 1. 토큰화 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
✂️ STEP 1. 토큰화 (Tokenization) — 텍스트를 조각으로 자른다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT는 단어 단위가 아니라 <b style="color:#1681c4;">토큰(Token)</b> 단위로 텍스트를 처리합니다.<br>
토큰은 단어보다 작을 수도, 여러 단어가 하나의 토큰이 될 수도 있습니다.
</p>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8; margin: 14px 0;">
<span style="color: #FF6B00; font-weight: 900;">💡 BPE(Byte Pair Encoding)란?</span><br>
GPT가 사용하는 토크나이저 방식으로, <b>자주 같이 등장하는 글자 조합을 하나의 토큰으로 묶는 방법</b>입니다.
</div>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">BPE 토큰화 예시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">영어 예시:</span>
<span style="color:#a6e3a1;">"unhappiness"</span>  <span style="color:#6c7086;">→</span>  <span style="color:#89dceb;">["un", "happiness"]</span>
<span style="color:#a6e3a1;">"playing"</span>      <span style="color:#6c7086;">→</span>  <span style="color:#89dceb;">["play", "ing"]</span>
<span style="color:#a6e3a1;">"ChatGPT"</span>      <span style="color:#6c7086;">→</span>  <span style="color:#89dceb;">["Chat", "G", "PT"]</span>

<span style="color:#6c7086;">한국어 예시:</span>
<span style="color:#a6e3a1;">"안녕하세요"</span>   <span style="color:#6c7086;">→</span>  <span style="color:#89dceb;">["안녕", "하세요"]</span>
<span style="color:#a6e3a1;">"자연어처리"</span>   <span style="color:#6c7086;">→</span>  <span style="color:#89dceb;">["자연어", "처리"]</span>
<span style="color:#a6e3a1;">"먹었습니다"</span>   <span style="color:#6c7086;">→</span>  <span style="color:#89dceb;">["먹었", "습니다"]</span></div>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-top: 18px; margin-bottom: 10px;">
왜 단어 단위가 아닌 토큰 단위를 쓸까요?
</p>

<div style="display: grid; gap: 14px;">

<!-- 문제 1 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">문제 1</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">새로운 단어를 만나면?</div>
  </div>
  <p style="margin:0 0 10px 0; font-size:14px; color:#475569; line-height:1.7;">
    <b>"코로나바이러스"</b> 같은 신조어는 단어 사전에 없을 수 있습니다.
  </p>
  <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    → BPE는 <b style="color:#FF6B00;">"코로나" + "바이러스"</b> 처럼 아는 조각들로 분해할 수 있습니다.
  </div>
</div>

<!-- 문제 2 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">문제 2</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">언어마다 단어 경계가 다름</div>
  </div>
  <p style="margin:0 0 10px 0; font-size:14px; color:#475569; line-height:1.7;">
    한국어는 <b>"먹었습니다"</b>를 어디서 잘라야 할까요?
  </p>
  <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    → BPE는 데이터를 보고 <b style="color:#1681c4;">가장 효율적인 조각</b>을 자동으로 학습합니다.
  </div>
</div>

</div>

</div>

<br>

<!-- 토큰 ID -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔢 토큰 ID — 각 토큰에 고유 번호를 붙인다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
토큰화 후, 각 토큰은 단어 사전에서의 <b style="color:#1681c4;">고유 번호(ID)</b>로 변환됩니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">GPT 토큰 사전 (GPT-2 기준 약 5만 개)</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">토큰 </span><span style="color:#a6e3a1;">"Hello"</span>  <span style="color:#6c7086;">→ ID:</span> <span style="color:#89dceb;">15496</span>
<span style="color:#6c7086;">토큰 </span><span style="color:#a6e3a1;">"world"</span>  <span style="color:#6c7086;">→ ID:</span> <span style="color:#89dceb;">995</span>
<span style="color:#6c7086;">토큰 </span><span style="color:#a6e3a1;">" the"</span>   <span style="color:#6c7086;">→ ID:</span> <span style="color:#89dceb;">262</span>
<span style="color:#6c7086;">토큰 </span><span style="color:#a6e3a1;">"안녕"</span>   <span style="color:#6c7086;">→ ID:</span> <span style="color:#89dceb;">31495</span>
<span style="color:#6c7086;">...</span>

<span style="color:#a6e3a1;">"Hello world"</span> <span style="color:#6c7086;">입력 시:</span>
<span style="color:#89dceb;">["Hello", " world"]</span>  <span style="color:#6c7086;">→</span>  <span style="color:#ff5f57;">[15496, 995]</span></div>
</div>

<div style="margin-top: 14px; background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align: center; font-weight: 900;">
이제 텍스트가 <span style="color:#FF6B00;">숫자 배열</span>이 되었습니다. 컴퓨터가 처리할 수 있는 형태가 된 것입니다.
</div>

</div>

<br>

<!-- STEP 2. 토큰 임베딩 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🗺️ STEP 2. 토큰 임베딩 — 번호를 의미 있는 벡터로 변환
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
토큰 ID는 그냥 번호일 뿐입니다. <b>15496번</b>과 <b>995번</b>이 얼마나 비슷한지는 알 수 없습니다.<br>
그래서 GPT는 각 토큰 ID를 <b style="color:#1681c4;">고차원 벡터</b>로 변환합니다. 이 변환표를 <b style="color:#1681c4;">임베딩 행렬(Embedding Matrix)</b>이라고 합니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">임베딩 행렬 (GPT-3 기준, 12,288 차원)</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">토큰 ID </span><span style="color:#89dceb;">15496</span> <span style="color:#6c7086;">(</span><span style="color:#a6e3a1;">"Hello"</span><span style="color:#6c7086;">)</span>
  <span style="color:#6c7086;">→</span> <span style="color:#cdd6f4;">[0.23, -0.51, 0.87, 0.12, -0.34, 0.65, ...]</span>  <span style="color:#6c7086;">(12,288개 숫자)</span>

<span style="color:#6c7086;">토큰 ID </span><span style="color:#89dceb;">995</span> <span style="color:#6c7086;">(</span><span style="color:#a6e3a1;">"world"</span><span style="color:#6c7086;">)</span>
  <span style="color:#6c7086;">→</span> <span style="color:#cdd6f4;">[0.41, 0.18, 0.73, -0.28, 0.52, -0.11, ...]</span>  <span style="color:#6c7086;">(12,288개 숫자)</span></div>
</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 처음엔 랜덤, 점점 정교해짐</span><br>
이 벡터들은 처음엔 랜덤 값이지만, 학습이 진행되면서 <b>의미가 담긴 벡터</b>로 점점 정교해집니다.
</div>

</div>

<br>

<!-- 특수 토큰들 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📏 특수 토큰들 — GPT가 구조를 이해하는 신호
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT는 일반 단어 외에 <b style="color:#1681c4;">특수한 역할을 하는 토큰</b>들도 사용합니다.
</p>

<div style="overflow-x:auto; margin-top: 14px;">
<table style="width:100%; border-collapse:collapse; font-size:13px; text-align:left;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; font-weight:900; border-radius:8px 0 0 0;">특수 토큰</th>
      <th style="padding:10px 14px; font-weight:900; border-radius:0 8px 0 0;">역할</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 14px; font-family:Consolas, monospace; color:#1681c4; font-weight:900;">&lt;|endoftext|&gt;</td>
      <td style="padding:10px 14px; color:#334155;">문서의 시작 또는 끝을 알리는 신호</td>
    </tr>
    <tr style="background:#eef7ff;">
      <td style="padding:10px 14px; font-family:Consolas, monospace; color:#1681c4; font-weight:900;">&lt;|padding|&gt;</td>
      <td style="padding:10px 14px; color:#334155;">길이를 맞추기 위해 채우는 빈 토큰</td>
    </tr>
  </tbody>
</table>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-top: 18px; margin-bottom: 10px;">
ChatGPT처럼 <b>대화 형식으로 파인튜닝</b>된 모델은 추가로 다음 토큰들을 사용합니다.
</p>

<div style="overflow-x:auto;">
<table style="width:100%; border-collapse:collapse; font-size:13px; text-align:left;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; font-weight:900; border-radius:8px 0 0 0;">특수 토큰</th>
      <th style="padding:10px 14px; font-weight:900; border-radius:0 8px 0 0;">역할</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 14px; font-family:Consolas, monospace; color:#FF6B00; font-weight:900;">&lt;|im_start|&gt;</td>
      <td style="padding:10px 14px; color:#334155;">메시지 시작 신호</td>
    </tr>
    <tr style="background:#eef7ff;">
      <td style="padding:10px 14px; font-family:Consolas, monospace; color:#FF6B00; font-weight:900;">&lt;|im_end|&gt;</td>
      <td style="padding:10px 14px; color:#334155;">메시지 끝 신호</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 14px; font-family:Consolas, monospace; color:#FF6B00; font-weight:900;">system / user / assistant</td>
      <td style="padding:10px 14px; color:#334155;">누가 말하는지 역할 구분</td>
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
    GPT는 텍스트를 <b style="color:#FF6B00;">토큰 → ID → 벡터</b> 순서로 변환한 뒤 처리합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    토큰은 단어보다 작거나 큰 단위이며, <b style="color:#FF6B00;">BPE 방식</b>으로 자동 분할됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    각 토큰 ID는 <b style="color:#FF6B00;">수백~수천 차원의 벡터</b>로 변환됩니다 (임베딩).
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <code style="background:#f8fafc; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">&lt;|endoftext|&gt;</code> 같은 <b style="color:#FF6B00;">특수 토큰</b>으로 문서 구조를 알려줍니다.
  </div>
</div>

</div>

</div>