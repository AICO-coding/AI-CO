<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->

<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Transformer 처리 과정 정리
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
지금까지 배운 Transformer의 핵심 개념들이
<b style="color:#1681c4;">어디에 배치되고, 어떤 순서로 연결되는지</b>
전체 흐름으로 정리합니다.
</p>

</div>

<br>

<!-- 챕터 개념 되짚기 -->

<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🗺️ 챕터 5에서 배운 핵심 개념
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
챕터 5에서는 Transformer를 구성하는 여러 개념을 배웠습니다.<br>
전체 흐름을 정리하기 전에, 각 개념이 어떤 역할을 했는지 먼저 되짚어봅시다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 14px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; margin-top: 14px;">
<span style="color: #1681c4; font-weight: 900;">💡 정리 포인트</span><br>
Transformer는 하나의 큰 덩어리가 아니라,
<b style="color:#1681c4;">여러 블록이 정해진 위치에 배치되어 함께 동작하는 구조</b>입니다.
</div>

</div>

<br>

<!-- 개념별 한 줄 요약 -->

<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📋 개념별 한 줄 요약
</h2>

<div style="display: grid; gap: 14px; margin-top: 16px;">

  <!-- 5-1 -->

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:17px 19px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
      <span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">5-1</span>
      <span style="font-size:15px; font-weight:900; color:#FF6B00;">Transformer가 등장한 이유</span>
    </div>
    <p style="margin:0 0 12px 0; line-height:1.8; color:#334155; font-size:14px;">
      RNN은 문장을 순서대로만 처리해서 느렸고, 긴 문장에서 앞 내용을 잊는 문제가 있었습니다.<br>
      Transformer는 문장 전체를 <b style="color:#FF6B00;">동시에, 병렬로</b> 처리해서 이 문제를 해결했습니다.
    </p>
    <div style="background:#0f172a; border-radius:10px; padding:12px 15px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#f38ba8;">RNN</span>:          나는 → 밥을 → 먹었다  <span style="color:#6c7086;">(순서대로, 느림)</span>
<span style="color:#89dceb;">Transformer</span>:  나는 · 밥을 · 먹었다  <span style="color:#6c7086;">(동시에, 빠름)</span></div>
  </div>

  <!-- 5-2 -->

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:17px 19px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
      <span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">5-2</span>
      <span style="font-size:15px; font-weight:900; color:#1681c4;">Transformer의 전체 구조</span>
    </div>
    <p style="margin:0 0 12px 0; line-height:1.8; color:#334155; font-size:14px;">
      입력 문장을 이해하는 <b>Encoder</b>와 출력 문장을 생성하는 <b>Decoder</b>로 구성됩니다.<br>
      각각 6개 레이어가 쌓이고, 레이어마다 동일한 블록 구조가 반복됩니다.
    </p>
    <div style="background:#0f172a; border-radius:10px; padding:12px 15px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre; text-align:center;">
<span style="color:#a6e3a1;">[입력]</span> → <span style="color:#89dceb;">Encoder × 6</span> → <span style="color:#cba6f7;">Decoder × 6</span> → <span style="color:#f9e2af;">[출력]</span></div>
  </div>

  <!-- 5-3 -->

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:17px 19px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
      <span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">5-3</span>
      <span style="font-size:15px; font-weight:900; color:#FF6B00;">Positional Encoding</span>
    </div>
    <p style="margin:0 0 12px 0; line-height:1.8; color:#334155; font-size:14px;">
      Transformer는 단어를 동시에 처리하기 때문에 단어 순서를 스스로 알 수 없습니다.<br>
      그래서 sin/cos 파동 패턴으로 만든 위치 벡터를 단어 벡터에 <b style="color:#FF6B00;">더해서</b> 순서 정보를 추가합니다.
    </p>
    <div style="background:#0f172a; border-radius:10px; padding:12px 15px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"나는" 벡터</span> + <span style="color:#f9e2af;">위치 1 인코딩</span> = <span style="color:#89dceb;">순서 정보가 담긴 "나는" 벡터</span></div>
  </div>

  <!-- 5-4 -->

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:17px 19px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
      <span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">5-4</span>
      <span style="font-size:15px; font-weight:900; color:#1681c4;">Encoder — Self-Attention & Multi-Head Attention</span>
    </div>
    <p style="margin:0 0 12px 0; line-height:1.8; color:#334155; font-size:14px;">
      같은 문장 안에서 단어들이 서로의 관계를 계산합니다.<br>
      Q(질문), K(태그), V(내용)으로 각 단어가 다른 단어를 얼마나 참고할지 결정합니다.<br>
      이 과정을 8개 관점으로 동시에 실행하면 <b style="color:#1681c4;">Multi-Head Attention</b>입니다.
    </p>
    <div style="background:#0f172a; border-radius:10px; padding:12px 15px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"고프다"</span>가 <span style="color:#f9e2af;">"배가"</span>를 64% 참고
→ <span style="color:#89dceb;">"배"가 신체 기관이 아니라 음식과 관련된 표현임을 파악</span></div>
  </div>

  <!-- 5-5 -->

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:17px 19px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
      <span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">5-5</span>
      <span style="font-size:15px; font-weight:900; color:#FF6B00;">Add & Norm</span>
    </div>
    <p style="margin:0 0 12px 0; line-height:1.8; color:#334155; font-size:14px;">
      레이어를 깊이 쌓을 때 생기는 기울기 소실과 정보 손실을 막는 장치입니다.<br>
      <b>Add</b>는 원래 입력을 레이어 출력에 더해 정보를 보존하고,<br>
      <b>Norm</b>은 벡터 값을 안정적인 범위로 조정해 학습을 안정화합니다.
    </p>
    <div style="background:#0f172a; border-radius:10px; padding:12px 15px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre; text-align:center;">
<span style="color:#89dceb;">출력</span> = <span style="color:#cba6f7;">Norm</span>( <span style="color:#a6e3a1;">원래 입력 X</span> + <span style="color:#f9e2af;">레이어(X)</span> )</div>
  </div>

  <!-- 5-6 -->

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:17px 19px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
      <span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">5-6</span>
      <span style="font-size:15px; font-weight:900; color:#1681c4;">Feed Forward Network (FFN)</span>
    </div>
    <p style="margin:0 0 12px 0; line-height:1.8; color:#334155; font-size:14px;">
      Self-Attention이 단어 <b>간 관계</b>를 잡았다면, FFN은 각 단어를 <b>독립적으로 심화 변환</b>합니다.<br>
      512 → 2048 → ReLU → 512 구조로 단어 표현을 더 풍부하게 만듭니다.
    </p>
    <div style="background:#0f172a; border-radius:10px; padding:12px 15px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"밥을" 벡터</span> → <span style="color:#cba6f7;">FFN</span> → <span style="color:#89dceb;">"먹을 수 있는 음식, 목적어" 정보가 강화된 벡터</span></div>
  </div>

  <!-- 5-7 -->

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:17px 19px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
      <span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">5-7</span>
      <span style="font-size:15px; font-weight:900; color:#FF6B00;">Decoder — Encoder-Decoder Attention</span>
    </div>
    <p style="margin:0 0 12px 0; line-height:1.8; color:#334155; font-size:14px;">
      Decoder는 매 단어를 생성할 때 Encoder의 결과를 참고합니다.<br>
      Q는 Decoder에서, K와 V는 Encoder 출력에서 가져와 <b style="color:#FF6B00;">원문의 어느 부분을 볼지</b> 결정합니다.
    </p>
    <div style="background:#0f172a; border-radius:10px; padding:12px 15px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"ate"</span> 생성 시:
<span style="color:#cba6f7;">Q_decoder</span> → <span style="color:#f9e2af;">"먹었다" 벡터에 65% Attention</span> → <span style="color:#89dceb;">"ate" 선택</span></div>
  </div>

  <!-- 5-8 -->

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:17px 19px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
      <span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">5-8</span>
      <span style="font-size:15px; font-weight:900; color:#1681c4;">Masked Self-Attention</span>
    </div>
    <p style="margin:0 0 12px 0; line-height:1.8; color:#334155; font-size:14px;">
      Decoder에서 아직 생성하지 않은 미래 단어를 미리 보면 치팅이 됩니다.<br>
      Attention 점수 행렬에서 미래 위치를 <b style="color:#1681c4;">−∞</b>로 만들어 Softmax 후 0이 되게 합니다.
    </p>
    <div style="background:#0f172a; border-radius:10px; padding:12px 15px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"ate"</span> 예측 시:
<span style="color:#f9e2af;">"rice" 위치 점수</span> → <span style="color:#f38ba8;">−∞</span> → <span style="color:#cba6f7;">Softmax</span> → <span style="color:#89dceb;">0</span> <span style="color:#6c7086;">(완전 차단)</span></div>
  </div>

</div>

</div>

<br>

<!-- 개념 위치 -->

<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧩 개념들이 Transformer 안에서 어디에 있는지
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
이제 각 개념이 Transformer 전체 구조 안에서 어디에 배치되는지 확인해봅시다.<br>
아래 흐름을 보면 Encoder와 Decoder의 차이가 한눈에 보입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Transformer 전체 구조 속 개념 위치</span>
  </div>

  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.1; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#a6e3a1;">입력 문장</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#f9e2af;">[임베딩]</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#f38ba8;">[★ Positional Encoding]</span>  <span style="color:#6c7086;">← 5-3</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#cba6f7;">┌──────────────────────────────────────┐</span>
<span style="color:#cba6f7;">│  ENCODER LAYER × 6                  │</span>
<span style="color:#cba6f7;">│  [★ Multi-Head Self-Attention] ← 5-4│</span>
<span style="color:#cba6f7;">│  [★ Add & Norm]                ← 5-5│</span>
<span style="color:#cba6f7;">│  [★ FFN]                       ← 5-6│</span>
<span style="color:#cba6f7;">│  [★ Add & Norm]                ← 5-5│</span>
<span style="color:#cba6f7;">└──────────────────────────────────────┘</span>
    <span style="color:#89dceb;">↓</span> <span style="color:#6c7086;">Encoder 출력: K, V로 Decoder에 전달</span>
<span style="color:#89dceb;">┌──────────────────────────────────────┐</span>
<span style="color:#89dceb;">│  DECODER LAYER × 6                  │</span>
<span style="color:#89dceb;">│  [★ Masked Self-Attention]     ← 5-8│</span>
<span style="color:#89dceb;">│  [★ Add & Norm]                ← 5-5│</span>
<span style="color:#89dceb;">│  [★ Encoder-Decoder Attention] ← 5-7│</span>
<span style="color:#89dceb;">│  [★ Add & Norm]                ← 5-5│</span>
<span style="color:#89dceb;">│  [★ FFN]                       ← 5-6│</span>
<span style="color:#89dceb;">│  [★ Add & Norm]                ← 5-5│</span>
<span style="color:#89dceb;">└──────────────────────────────────────┘</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#f9e2af;">[Linear + Softmax → 단어 선택]</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#a6e3a1;">출력 문장</span></div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 구조 해석</span><br>
Encoder는 입력 문장을 <b>이해</b>하는 쪽이고, Decoder는 Encoder 결과를 참고하면서 출력 문장을 <b>생성</b>하는 쪽입니다.<br>
따라서 Decoder에는 <b style="color:#FF6B00;">Masked Self-Attention</b>과 <b style="color:#FF6B00;">Encoder-Decoder Attention</b>이 추가로 들어갑니다.
</div>

</div>

<br>

<!-- Encoder vs Decoder 요약 -->

<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🆚 Encoder와 Decoder 역할 비교
</h2>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">Encoder</div>
    <div style="display:grid; gap:8px;">
      <div style="background:#fff; border-left:4px solid #FF6B00; padding:9px 12px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
        입력 문장을 전체적으로 이해합니다.
      </div>
      <div style="background:#fff; border-left:4px solid #FF6B00; padding:9px 12px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
        모든 단어가 서로를 자유롭게 참고합니다.
      </div>
      <div style="background:#fff; border-left:4px solid #FF6B00; padding:9px 12px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
        결과는 Decoder가 참고할 <b style="color:#FF6B00;">K, V 정보</b>로 전달됩니다.
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:18px 20px;">
    <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:12px;">Decoder</div>
    <div style="display:grid; gap:8px;">
      <div style="background:#fff; border-left:4px solid #1681c4; padding:9px 12px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
        출력 문장을 앞에서부터 생성합니다.
      </div>
      <div style="background:#fff; border-left:4px solid #1681c4; padding:9px 12px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
        미래 단어는 볼 수 없도록 마스킹합니다.
      </div>
      <div style="background:#fff; border-left:4px solid #1681c4; padding:9px 12px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
        Encoder 결과를 참고해 <b style="color:#1681c4;">다음 단어</b>를 선택합니다.
      </div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 전체 흐름 핵심 -->

<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 Transformer 처리 흐름을 한 문장으로 정리하면
</h2>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 1</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:4px;">입력 문장에 순서 정보를 더한다</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">임베딩 벡터에 Positional Encoding을 더해 단어 위치를 알려줍니다.</div>
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 2</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:4px;">Encoder가 입력 문장을 이해한다</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">Self-Attention, Add & Norm, FFN을 반복해 단어들의 관계를 풍부하게 반영합니다.</div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 3</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:4px;">Decoder가 앞 단어만 보고 다음 단어를 만든다</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">Masked Self-Attention으로 미래 단어를 차단하고, Encoder 결과를 참고합니다.</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 4</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:4px;">Linear + Softmax로 단어를 선택한다</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">Decoder 출력은 단어 사전 크기의 확률로 변환되고, 가장 적절한 다음 단어가 선택됩니다.</div>
    </div>
  </div>

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
    Transformer는 <b style="color:#FF6B00;">여러 핵심 블록</b>이 조화롭게 연결된 구조입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    각 블록은 독립적인 역할을 가지며, 어느 하나도 빠지면 전체 성능이 떨어질 수 있습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Encoder는 입력 문장을 <b style="color:#FF6B00;">이해</b>하고, Decoder는 출력 문장을 <b style="color:#FF6B00;">생성</b>합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Decoder는 미래 단어를 볼 수 없도록 <b style="color:#FF6B00;">Masked Self-Attention</b>을 사용합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    블록들이 Encoder와 Decoder에 배치되는 방식에는 <b style="color:#FF6B00;">명확한 설계 의도</b>가 담겨 있습니다.
  </div>
</div>

<div style="margin-top:12px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> 다음 페이지에서는 <b style="color:#1681c4;">"나는 밥을 먹었다" → "I ate rice"</b><br>
한 문장이 Transformer를 통과하는 완전한 여정을 처음부터 끝까지 따라갑니다.
</div>

</div>

</div>
