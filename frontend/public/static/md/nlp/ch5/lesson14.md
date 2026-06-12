<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Decoder
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Encoder가 이해한 내용을 받아
<b style="color:#1681c4;">출력 문장을 한 단어씩 생성하는 Decoder</b>의 구조와 세 가지 핵심 특징을 알아봅니다.
</p>

</div>

<br>

<!-- Encoder → Decoder 전달 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📬 Encoder가 끝났습니다. 이제 Decoder 차례입니다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Encoder는 입력 문장을 <b>완전히 이해한 벡터 묶음</b>으로 압축해서 Decoder에게 넘겨줍니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Encoder → Decoder 전달</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#a6e3a1;">"나는 밥을 먹었다"</span>
        <span style="color:#89dceb;">↓</span>
  <span style="color:#f38ba8;">[ Encoder × 6 ]</span>
        <span style="color:#89dceb;">↓</span>
  <span style="color:#cba6f7;">[벡터_나는, 벡터_밥을, 벡터_먹었다]</span>   <span style="color:#6c7086;">← 문맥이 녹아있는 3개의 벡터</span>
        <span style="color:#89dceb;">↓</span>
     <span style="color:#f9e2af;">Decoder 로 전달</span></div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 14px; text-align:center; font-size:13px; color:#334155; line-height:1.7;">
    <b style="color:#1681c4;">Encoder 직원</b><br>한국어 문장을 읽고<br>완전히 이해해서 메모(벡터)를 건네줌
  </div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:12px 14px; text-align:center; font-size:13px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">Decoder 직원</b><br>메모를 보면서<br>영어 단어를 하나씩 받아 씀
  </div>
</div>

</div>

<br>

<!-- 세 가지 핵심 특징 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔑 Decoder의 세 가지 핵심 특징
</h2>

<div style="display: grid; gap: 14px; margin-top: 4px;">

  <!-- 특징 1 -->
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">특징 1. 단어를 하나씩 순서대로 생성한다</div>
    <div style="display: grid; grid-template-columns: auto 1fr; gap:2px 0; margin-bottom:12px;">
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2.2; overflow-x:auto; grid-column: 1 / -1; white-space:pre;">
<span style="color:#6c7086;">1단계:</span> [시작]                          → <span style="color:#a6e3a1;">"I"</span> 생성
<span style="color:#6c7086;">2단계:</span> [시작, <span style="color:#a6e3a1;">"I"</span>]                    → <span style="color:#a6e3a1;">"ate"</span> 생성
<span style="color:#6c7086;">3단계:</span> [시작, <span style="color:#a6e3a1;">"I"</span>, <span style="color:#a6e3a1;">"ate"</span>]           → <span style="color:#a6e3a1;">"rice"</span> 생성
<span style="color:#6c7086;">4단계:</span> [시작, <span style="color:#a6e3a1;">"I"</span>, <span style="color:#a6e3a1;">"ate"</span>, <span style="color:#a6e3a1;">"rice"</span>]  → <span style="color:#f9e2af;">[종료]</span> 생성</div>
    </div>
    <div style="background:#fff; border-left:4px solid #ffd0b0; padding:9px 13px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
      다음 단어를 생성할 때마다 <b style="color:#FF6B00;">이전에 생성한 단어들을 모두 참고</b>합니다.
    </div>
  </div>

  <!-- 특징 2 -->
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">특징 2. Encoder의 결과를 참고한다</div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2.2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">"ate" 생성 시:</span>
  → 이전 단어 <span style="color:#a6e3a1;">"I"</span> 참고
  → Encoder 벡터 참고, 특히 <span style="color:#f9e2af;">"먹었다"</span> 벡터에 높은 Attention

<span style="color:#6c7086;">"rice" 생성 시:</span>
  → 이전 단어 <span style="color:#a6e3a1;">"I", "ate"</span> 참고
  → Encoder 벡터 참고, 특히 <span style="color:#f9e2af;">"밥을"</span> 벡터에 높은 Attention</div>
    <div style="background:#fff; border-left:4px solid #ffd0b0; padding:9px 13px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
      이 과정을 <b style="color:#FF6B00;">Encoder-Decoder Attention</b>이라고 합니다. 다음 페이지에서 자세히 배웁니다.
    </div>
  </div>

  <!-- 특징 3 -->
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">특징 3. 아직 안 나온 단어는 볼 수 없다</div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2.2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">"ate" 생성 시점에서 볼 수 있는 것:</span>
  <span style="color:#a6e3a1;">✅ "I"</span>          <span style="color:#6c7086;">(이미 생성됨)</span>
  <span style="color:#a6e3a1;">✅ Encoder 벡터</span>  <span style="color:#6c7086;">(입력 문장 이해 결과)</span>
  <span style="color:#f38ba8;">❌ "rice"</span>        <span style="color:#6c7086;">(아직 생성 안 됨)</span>
  <span style="color:#f38ba8;">❌ "yesterday"</span>  <span style="color:#6c7086;">(아직 생성 안 됨)</span></div>
    <div style="background:#fff; border-left:4px solid #ffd0b0; padding:9px 13px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
      이것을 구현하기 위한 장치가 <b style="color:#FF6B00;">Masked Self-Attention</b>입니다. 5-8에서 자세히 배웁니다.
    </div>
  </div>

</div>

</div>

<br>

<!-- Encoder vs Decoder 비교 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🆚 Encoder vs Decoder 구조 비교
</h2>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 16px 0;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:12px; text-align:center;">ENCODER</div>
    <div style="font-size:12px; color:#94a3b8; text-align:center; margin-bottom:10px;">입력 전체를 동시에 처리</div>
    <div style="display:grid; gap:5px;">
      <div style="background:#0f172a; border-radius:7px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#a6e3a1;">① Multi-Head Self-Attention</div>
      <div style="background:#0f172a; border-radius:7px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#89dceb;">② Add &amp; Norm</div>
      <div style="background:#0f172a; border-radius:7px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#a6e3a1;">③ FFN</div>
      <div style="background:#0f172a; border-radius:7px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#89dceb;">④ Add &amp; Norm</div>
      <div style="background:#0f172a; border-radius:7px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#6c7086; text-align:center;">× 6 반복</div>
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:12px; text-align:center;">DECODER</div>
    <div style="font-size:12px; color:#94a3b8; text-align:center; margin-bottom:10px;">출력을 한 단어씩 순서대로 생성</div>
    <div style="display:grid; gap:5px;">
      <div style="background:#0f172a; border-radius:7px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#f38ba8;">① Masked Self-Attention</div>
      <div style="background:#0f172a; border-radius:7px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#89dceb;">② Add &amp; Norm</div>
      <div style="background:#0f172a; border-radius:7px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#f9e2af;">③ Encoder-Decoder Attention</div>
      <div style="background:#0f172a; border-radius:7px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#89dceb;">④ Add &amp; Norm</div>
      <div style="background:#0f172a; border-radius:7px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#a6e3a1;">⑤ FFN</div>
      <div style="background:#0f172a; border-radius:7px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#89dceb;">⑥ Add &amp; Norm</div>
      <div style="background:#0f172a; border-radius:7px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#6c7086; text-align:center;">× 6 반복</div>
    </div>
  </div>

</div>

<div style="overflow-x: auto;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; font-weight:900;">구성 요소</th>
      <th style="padding:10px 14px; text-align:center; font-weight:900;">Encoder</th>
      <th style="padding:10px 14px; text-align:center; font-weight:900;">Decoder</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; color:#334155;">Multi-Head Self-Attention</td>
      <td style="padding:10px 14px; text-align:center; color:#1681c4; font-weight:900;">✅</td>
      <td style="padding:10px 14px; text-align:center; color:#94a3b8;">❌ (Masked 버전)</td>
    </tr>
    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; color:#334155;">Masked Self-Attention</td>
      <td style="padding:10px 14px; text-align:center; color:#94a3b8;">❌</td>
      <td style="padding:10px 14px; text-align:center; color:#FF6B00; font-weight:900;">✅</td>
    </tr>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; color:#334155;">Encoder-Decoder Attention</td>
      <td style="padding:10px 14px; text-align:center; color:#94a3b8;">❌</td>
      <td style="padding:10px 14px; text-align:center; color:#FF6B00; font-weight:900;">✅</td>
    </tr>
    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; color:#334155;">FFN</td>
      <td style="padding:10px 14px; text-align:center; color:#1681c4; font-weight:900;">✅</td>
      <td style="padding:10px 14px; text-align:center; color:#1681c4; font-weight:900;">✅</td>
    </tr>
    <tr style="background:#fff;">
      <td style="padding:10px 14px; color:#334155;">Add &amp; Norm</td>
      <td style="padding:10px 14px; text-align:center; color:#475569;">✅ (×2)</td>
      <td style="padding:10px 14px; text-align:center; color:#475569;">✅ (×3)</td>
    </tr>
  </tbody>
</table>
</div>

</div>

<br>

<!-- Decoder 최종 출력 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📤 Decoder의 최종 출력
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
Decoder의 마지막 레이어를 통과한 벡터는 <b>Linear + Softmax</b>를 거쳐 "다음에 올 단어의 확률"로 변환됩니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-bottom: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">단어 확률 계산</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#cba6f7;">Decoder 출력 벡터 (512차원)</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#6c7086;">Linear 변환 (512 → 30,000)</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#6c7086;">Softmax (확률 분포로 변환)</span>
         <span style="color:#89dceb;">↓</span>
  <span style="color:#6c7086;">I:         0.01</span>
  <span style="color:#f9e2af;">ate:       0.72  ← 가장 높음!</span>
  <span style="color:#6c7086;">rice:      0.15</span>
  <span style="color:#6c7086;">yesterday: 0.03</span>
  <span style="color:#6c7086;">...</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#a6e3a1;">가장 높은 확률의 단어 선택 → "ate" 출력</span></div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> 이 과정을 <b style="color:#1681c4;">[종료] 신호가 나올 때까지 반복</b>하면 완전한 번역 문장이 완성됩니다.
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
    Decoder는 Encoder가 이해한 내용을 바탕으로 <b style="color:#FF6B00;">출력 단어를 한 번에 하나씩 생성</b>합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    매 단계마다 <b style="color:#FF6B00;">이미 생성한 단어</b>와 <b style="color:#FF6B00;">Encoder의 벡터</b> 두 가지를 모두 참고합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Encoder보다 블록이 하나 더 많습니다. <b style="color:#FF6B00;">Masked Self-Attention + Encoder-Decoder Attention + FFN</b>.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    최종적으로 <b style="color:#FF6B00;">Softmax</b>로 다음 단어 확률을 계산하고, 가장 높은 확률의 단어를 선택합니다.
  </div>
</div>

<div style="margin-top:12px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> 다음 페이지에서는 "Encoder 결과를 어떻게 참고하는가"인 <b style="color:#1681c4;">Encoder-Decoder Attention</b>을 자세히 살펴봅니다.
</div>

</div>

</div>