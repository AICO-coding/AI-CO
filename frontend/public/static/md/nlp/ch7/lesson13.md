<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 07 · GPT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
GPT에서 답변이 나오기까지의 전체 흐름
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Decoder를 통과한 벡터가
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">텍스트로 출력되기까지의 과정</span>
과 GPT의 자기회귀 생성 방식을 알아봅니다.
</p>

</div>

<br>

<!-- GPT의 출력 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📤 GPT의 출력: 텍스트가 만들어지는 과정
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
지금까지 입력 (텍스트 → 토큰 → 벡터)을 살펴봤습니다.<br>
이번엔 GPT 내부를 통과한 뒤, <b style="color:#1681c4;">어떻게 텍스트가 출력되는지</b> 살펴봅니다.
</p>

</div>

<br>

<!-- 출력 구조: 세 개의 층 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🏗️ 출력 구조: 세 개의 층
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT의 출력 부분은 세 단계로 이루어집니다.
</p>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; padding: 13px 16px; font-size: 14px; color: #334155; text-align: center; font-weight: 900; margin: 14px 0;">
Decoder 블록들 통과 후 나온 <span style="color:#1681c4;">마지막 벡터</span>
</div>

<div style="display: grid; gap: 14px;">

<!-- ① Linear Layer -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">①</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">Linear Layer (선형 변환 층)</div>
  </div>
  <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    벡터를 <b style="color:#FF6B00;">단어 사전 크기의 점수</b>로 변환합니다. (예: 50,257개 토큰 각각에 점수)
  </div>
</div>

<!-- ↓ -->
<div style="text-align:center; color:#6c7086; font-size: 18px; margin: -6px 0;">↓</div>

<!-- ② Softmax -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">②</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">Softmax</div>
  </div>
  <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    점수를 <b style="color:#1681c4;">확률</b>로 변환합니다. (전체 합계 = 100%)
  </div>
</div>

<!-- ↓ -->
<div style="text-align:center; color:#6c7086; font-size: 18px; margin: -6px 0;">↓</div>

<!-- ③ 디코딩 전략 적용 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">③</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">디코딩 전략 적용 (Top-p, Temperature 등)</div>
  </div>
  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    확률 분포에서 <b style="color:#FF6B00;">토큰 하나를 선택</b>합니다.
  </div>
</div>

</div>

<div style="margin-top: 14px; background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; text-align:center;">
<span style="color:#cdd6f4;">선택된 토큰 ID</span>
<span style="color:#6c7086;"> → </span>
<span style="color:#89dceb;">토큰 → 텍스트 복원</span>
<span style="color:#6c7086;"> → </span>
<span style="color:#a6e3a1;">최종 출력 텍스트</span></div>

</div>

<br>

<!-- 자기회귀의 실제 모습 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔁 출력이 다시 입력이 된다: 자기회귀의 실제 모습
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT의 가장 독특한 특징은 <b style="color:#1681c4;">자신이 생성한 출력을 다음 입력으로 사용</b>한다는 것입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">자기회귀 생성 과정</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">[1번째 생성 단계]</span>
  <span style="color:#89dceb;">입력:  [오늘, 날씨가]</span>
  <span style="color:#a6e3a1;">출력:  "좋아서" (토큰 선택)</span>

<span style="color:#6c7086;">[2번째 생성 단계]</span>
  <span style="color:#89dceb;">입력:  [오늘, 날씨가, </span><span style="color:#a6e3a1;">좋아서</span><span style="color:#89dceb;">]</span>  <span style="color:#6c7086;">← 생성된 "좋아서"가 추가됨</span>
  <span style="color:#a6e3a1;">출력:  "기분이"</span>

<span style="color:#6c7086;">[3번째 생성 단계]</span>
  <span style="color:#89dceb;">입력:  [오늘, 날씨가, 좋아서, </span><span style="color:#a6e3a1;">기분이</span><span style="color:#89dceb;">]</span>
  <span style="color:#a6e3a1;">출력:  "좋다"</span>

<span style="color:#6c7086;">[4번째 생성 단계]</span>
  <span style="color:#89dceb;">입력:  [오늘, 날씨가, 좋아서, 기분이, </span><span style="color:#a6e3a1;">좋다</span><span style="color:#89dceb;">]</span>
  <span style="color:#ff5f57;">출력:  &lt;|endoftext|&gt;  ← 종료 토큰 → 생성 멈춤</span>

<span style="color:#6c7086;">최종 결과: </span><span style="color:#a6e3a1;">"오늘 날씨가 좋아서 기분이 좋다"</span></div>
</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 매번 전체 입력을 다시 처리</span><br>
문장이 길어질수록 <b>생성 속도가 느려집니다.</b>
</div>

</div>

<br>

<!-- 스트리밍 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
⏱️ 왜 ChatGPT는 답변을 한 글자씩 출력할까?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
ChatGPT를 사용해보면 답변이 <b style="color:#1681c4;">한 글자씩 타이핑되듯</b> 나오는 걸 본 적 있을 겁니다.<br>
이것은 GPT가 <b>한 번에 하나의 토큰씩 생성</b>하기 때문입니다.<br>
생성된 토큰을 기다리지 않고 바로 화면에 보여주는 방식을 <b style="color:#1681c4;">스트리밍(Streaming)</b>이라고 합니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">스트리밍 출력 예시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">생성 순서:  </span><span style="color:#89dceb;">"안" → "녕" → "하" → "세" → "요" → "!"</span>
<span style="color:#6c7086;">화면 표시:  </span><span style="color:#a6e3a1;">안 → 안녕 → 안녕하 → 안녕하세 → 안녕하세요 → 안녕하세요!</span>

<span style="color:#6c7086;">(실제로는 글자가 아닌 토큰 단위, 화면에는 토큰을 글자로 변환해서 표시)</span></div>
</div>

<div style="margin-top: 14px; background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align: center; font-weight: 900;">
스트리밍을 쓰지 않으면 전체 답변이 완성될 때까지 기다려야 합니다. <span style="color:#FF6B00;">사용자 경험</span> 때문에 대부분의 서비스가 스트리밍을 사용합니다.
</div>

</div>

<br>

<!-- 전체 입출력 흐름 완전 정리 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🗺️ 전체 입출력 흐름 완전 정리
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
지금까지 배운 내용을 하나로 합쳐봅니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<!-- 입력 처리 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:12px; letter-spacing:.3px;">━━━ 입력 처리 ━━━</div>
  <div style="background-color: #1e1e2e; border-radius: 12px; padding: 14px 16px; font-size: 13px; line-height: 2.1; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">사용자 텍스트 "오늘 날씨가 어때?"</span>
  <span style="color:#6c7086;">↓ 토큰화 (BPE)</span>
<span style="color:#89dceb;">["오늘", "날씨가", "어때", "?"]</span>
  <span style="color:#6c7086;">↓ 토큰 ID 변환</span>
<span style="color:#cdd6f4;">[31234, 42891, 18734, 30]</span>
  <span style="color:#6c7086;">↓ 토큰 임베딩 (수백~수천 차원 벡터)</span>
<span style="color:#cdd6f4;">[[0.2, -0.5, ...], [0.8, 0.1, ...], ...]</span>
  <span style="color:#6c7086;">↓ 위치 인코딩 추가 (각 벡터에 위치 정보 합산)</span></div>
</div>

<!-- 내부 처리 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
  <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:12px; letter-spacing:.3px;">━━━ 내부 처리 ━━━</div>
  <div style="background-color: #1e1e2e; border-radius: 12px; padding: 14px 16px; font-size: 13px; line-height: 2.1; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x:auto; white-space:pre;">
<span style="color:#cdd6f4;">Decoder Block × N층 반복</span>
<span style="color:#6c7086;">(Masked Self-Attention + LayerNorm + FFN)</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">최종 벡터 출력</span></div>
</div>

<!-- 출력 처리 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:12px; letter-spacing:.3px;">━━━ 출력 처리 ━━━</div>
  <div style="background-color: #1e1e2e; border-radius: 12px; padding: 14px 16px; font-size: 13px; line-height: 2.1; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x:auto; white-space:pre;">
<span style="color:#cdd6f4;">Linear Layer</span>
  <span style="color:#6c7086;">→ 전체 토큰 사전 크기의 점수 벡터</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#cdd6f4;">Softmax</span>
  <span style="color:#6c7086;">→ 확률 분포 (합계 100%)</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#cdd6f4;">디코딩 전략 (Top-p + Temperature)</span>
  <span style="color:#6c7086;">→ 토큰 하나 선택: </span><span style="color:#a6e3a1;">"오늘은"</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#cdd6f4;">생성된 토큰을 입력에 추가 → 위 과정 반복</span>
  <span style="color:#6c7086;">↓</span>
<span style="color:#ff5f57;">종료 토큰 감지 시 멈춤</span></div>
</div>

<!-- 최종 출력 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:12px; letter-spacing:.3px;">━━━ 최종 출력 ━━━</div>
  <div style="background-color: #1e1e2e; border-radius: 12px; padding: 14px 16px; font-size: 13px; line-height: 2.1; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">토큰 ID → 텍스트 복원</span>
  <span style="color:#a6e3a1;">"오늘은 날씨가 맑고 기온은 22도 정도입니다."</span></div>
</div>

</div>

</div>

<br>

<!-- 한눈에 보는 입출력 요약표 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📌 한눈에 보는 입출력 요약표
</h2>

<div style="overflow-x:auto; margin-top: 14px;">
<table style="width:100%; border-collapse:collapse; font-size:13px; text-align:left;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 12px; font-weight:900; border-radius:8px 0 0 0;">단계</th>
      <th style="padding:10px 12px; font-weight:900;">입력 형태</th>
      <th style="padding:10px 12px; font-weight:900;">출력 형태</th>
      <th style="padding:10px 12px; font-weight:900; border-radius:0 8px 0 0;">핵심 역할</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f8fafc;">
      <td style="padding:9px 12px; font-weight:900; color:#1681c4;">토큰화</td>
      <td style="padding:9px 12px; color:#334155;">텍스트 문자열</td>
      <td style="padding:9px 12px; color:#334155;">토큰 리스트</td>
      <td style="padding:9px 12px; color:#334155;">텍스트를 처리 단위로 분할</td>
    </tr>
    <tr style="background:#eef7ff;">
      <td style="padding:9px 12px; font-weight:900; color:#1681c4;">ID 변환</td>
      <td style="padding:9px 12px; color:#334155;">토큰 리스트</td>
      <td style="padding:9px 12px; color:#334155;">정수 배열</td>
      <td style="padding:9px 12px; color:#334155;">토큰을 숫자 번호로 매핑</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:9px 12px; font-weight:900; color:#1681c4;">임베딩</td>
      <td style="padding:9px 12px; color:#334155;">정수 배열</td>
      <td style="padding:9px 12px; color:#334155;">벡터 행렬</td>
      <td style="padding:9px 12px; color:#334155;">번호를 의미 있는 벡터로 변환</td>
    </tr>
    <tr style="background:#eef7ff;">
      <td style="padding:9px 12px; font-weight:900; color:#1681c4;">Decoder</td>
      <td style="padding:9px 12px; color:#334155;">벡터 행렬</td>
      <td style="padding:9px 12px; color:#334155;">벡터 행렬</td>
      <td style="padding:9px 12px; color:#334155;">문맥을 반영한 표현으로 변환</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:9px 12px; font-weight:900; color:#1681c4;">Linear+Softmax</td>
      <td style="padding:9px 12px; color:#334155;">벡터</td>
      <td style="padding:9px 12px; color:#334155;">확률 분포</td>
      <td style="padding:9px 12px; color:#334155;">다음 토큰의 확률 계산</td>
    </tr>
    <tr style="background:#eef7ff;">
      <td style="padding:9px 12px; font-weight:900; color:#1681c4;">디코딩</td>
      <td style="padding:9px 12px; color:#334155;">확률 분포</td>
      <td style="padding:9px 12px; color:#334155;">토큰 ID 하나</td>
      <td style="padding:9px 12px; color:#334155;">전략에 따라 토큰 선택</td>
    </tr>
    <tr style="background:#fff3eb;">
      <td style="padding:9px 12px; font-weight:900; color:#FF6B00;">역토큰화</td>
      <td style="padding:9px 12px; color:#334155;">토큰 ID</td>
      <td style="padding:9px 12px; color:#334155;">텍스트</td>
      <td style="padding:9px 12px; color:#334155;">숫자를 다시 텍스트로 복원</td>
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
    GPT 출력: <b style="color:#FF6B00;">Linear Layer → Softmax → 디코딩 전략</b> 순으로 토큰 하나를 선택합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    생성된 토큰이 <b style="color:#FF6B00;">다시 입력으로 추가</b>되어 다음 토큰을 생성합니다 (자기회귀).
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    한 글자씩 타이핑되는 것처럼 보이는 건 <b style="color:#FF6B00;">스트리밍</b> 방식 때문입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    전체 흐름: <b style="color:#FF6B00;">텍스트 → 토큰 → ID → 벡터 → Decoder → 확률 → 토큰 → 텍스트</b>
  </div>
</div>

</div>

</div>