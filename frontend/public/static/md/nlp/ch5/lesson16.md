<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Decoder 전체 흐름
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
지금까지 배운 모든 블록이 Decoder 안에서
<b style="color:#1681c4;">어떤 순서로 실행되는지</b> 한 번에 따라가 봅니다.
</p>

</div>

<br>

<!-- 조각 모음 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🗺️ 이제 모든 조각이 모였습니다
</h2>

<div style="display: grid; gap: 8px; margin: 14px 0;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:12px; align-items:center;">
    <div style="font-size:14px; color:#334155;">Decoder는 출력 단어를 <b style="color:#1681c4;">한 번에 하나씩</b> 생성한다</div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:12px; align-items:center;">
    <div style="font-size:14px; color:#334155;"><b style="color:#1681c4;">Masked Self-Attention</b> — 이미 생성한 단어들 사이의 관계 파악</div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:12px; align-items:center;">
    <div style="font-size:14px; color:#334155;"><b style="color:#1681c4;">Encoder-Decoder Attention</b> — 원문(Encoder 결과)에서 필요한 정보 가져오기</div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:12px; align-items:center;">
    <div style="font-size:14px; color:#334155;"><b style="color:#1681c4;">FFN</b> — 각 단어 표현 심화</div>
  </div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">🎯 예시 설정:</span>
입력(한국어): <b>"나는 쌀을 먹었다"</b> → 출력(영어): <b>"I ate rice"</b><br>
Encoder 출력: <code style="background:#0f172a; color:#cba6f7; padding:2px 6px; border-radius:4px; font-size:12px;">[벡터_나는, 벡터_밥을, 벡터_먹었다]</code> 이미 준비됨
</div>

</div>

<br>

<!-- "ate" 생성 한 사이클 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔁 "ate"를 생성하는 한 사이클 — 단계별로 따라가기
</h2>

<div style="display: grid; gap: 10px; margin-top: 4px;">

  <!-- STEP 1 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 1</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">입력 준비: 지금까지 생성한 단어 + 위치 정보</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">지금까지 생성한 출력: ["&lt;시작&gt;", "I"]</span>
                      <span style="color:#89dceb;">↓ 임베딩 변환 + Positional Encoding</span>
  <span style="color:#cba6f7;">&lt;시작&gt;_벡터</span> <span style="color:#6c7086;">(위치 1)</span>
  <span style="color:#cba6f7;">I_벡터</span>      <span style="color:#6c7086;">(위치 2)</span></div>
    </div>
  </div>

  <!-- STEP 2 -->
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 2</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:8px;">Masked Self-Attention</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"I"</span>는 <span style="color:#a6e3a1;">"&lt;시작&gt;"</span>을 참고할 수 있습니다.     <span style="color:#a6e3a1;">✅</span>
<span style="color:#f38ba8;">"ate"</span>, <span style="color:#f38ba8;">"rice"</span>는 아직 생성 안 됨 → 볼 수 없습니다. <span style="color:#f38ba8;">❌</span></div>
      <div style="margin-top:8px; background:#fff3eb; border:1px solid #ffd0b0; border-radius:8px; padding:8px 12px; font-size:13px; color:#334155; line-height:1.7;">
        <b style="color:#FF6B00;">"Masked"</b>가 핵심 — 아직 생성되지 않은 미래 단어는 볼 수 없습니다.
      </div>
    </div>
  </div>

  <!-- STEP 3 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 3</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">Add &amp; Norm</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">Masked Attention 입력 + 출력 → </span><span style="color:#f9e2af;">ADD</span> → <span style="color:#cba6f7;">NORM</span> → <span style="color:#a6e3a1;">안정화된 Decoder 상태 벡터</span></div>
    </div>
  </div>

  <!-- STEP 4 -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 4</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">Encoder-Decoder Attention</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#f9e2af;">Q</span> = Decoder 현재 상태 <span style="color:#6c7086;">("ate"를 만들기 위한 질문)</span>
<span style="color:#cba6f7;">K</span> = [K_나는, K_밥을, K_먹었다]   <span style="color:#6c7086;">← Encoder 출력</span>
<span style="color:#cba6f7;">V</span> = [V_나는, V_밥을, V_먹었다]   <span style="color:#6c7086;">← Encoder 출력</span>

<span style="color:#6c7086;">나는   → </span><span style="color:#6c7086;">15%</span>
<span style="color:#6c7086;">밥을   → </span><span style="color:#6c7086;">20%</span>
<span style="color:#f9e2af;">먹었다 → 65%</span>  <span style="color:#6c7086;">← "ate"와 가장 관련 있는 원문 단어</span></div>
    </div>
  </div>

  <!-- STEP 5 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 5</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">Add &amp; Norm</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">Encoder-Decoder Attention 입력 + 출력 → </span><span style="color:#f9e2af;">ADD</span> → <span style="color:#cba6f7;">NORM</span></div>
    </div>
  </div>

  <!-- STEP 6 -->
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 6</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:8px;">Feed Forward Network</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#cba6f7;">[Decoder 상태 벡터]</span> → <span style="color:#f9e2af;">FFN (512 → 2048 → ReLU → 512)</span> → <span style="color:#a6e3a1;">[더욱 풍부해진 벡터]</span></div>
    </div>
  </div>

  <!-- STEP 7 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 7</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">Add &amp; Norm → Decoder Layer 최종 출력</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">FFN 입력 + FFN 출력 → </span><span style="color:#f9e2af;">ADD</span> → <span style="color:#cba6f7;">NORM</span> → <span style="color:#a6e3a1;">Decoder Layer 최종 출력</span></div>
    </div>
  </div>

  <!-- STEP 8 -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 8</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">Decoder Layer × 6 반복</div>
      <div style="display:grid; gap:5px;">
        <div style="background:#0f172a; border-radius:6px; padding:7px 12px; font-family:Consolas,monospace; font-size:12px; color:#6c7086;">[Decoder Layer 1] → [Layer 2] → [Layer 3] → [Layer 4] → [Layer 5] → [Layer 6]</div>
        <div style="background:#0f172a; border-radius:6px; padding:7px 12px; font-family:Consolas,monospace; font-size:12px; color:#a6e3a1; text-align:center;">Decoder 최종 출력 벡터 (512차원)</div>
      </div>
    </div>
  </div>

  <!-- STEP 9 -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 9</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">Linear + Softmax → 단어 확률 계산</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#cba6f7;">Decoder 출력 (512차원)</span> → <span style="color:#6c7086;">Linear (512 → 30,000)</span> → <span style="color:#6c7086;">Softmax</span>
  <span style="color:#6c7086;">a      → 0.001</span>
  <span style="color:#f9e2af;">ate    → 0.731</span>  <span style="color:#f9e2af;">← 가장 높음!</span>
  <span style="color:#6c7086;">eat    → 0.043</span>
  <span style="color:#6c7086;">rice   → 0.008</span>
  <span style="color:#a6e3a1;">→ "ate" 선택!</span></div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 전체 번역 완성 흐름 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 전체 번역이 완성되기까지
</h2>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">"I ate rice" 번역 전체 과정</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.6; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">[1번째 생성]</span>
  입력: <span style="color:#cba6f7;">&lt;시작&gt;</span>
  Attention: <span style="color:#f9e2af;">"나는"에 집중</span>  →  <span style="color:#a6e3a1;">"I"</span> 생성

<span style="color:#6c7086;">[2번째 생성]</span>
  입력: <span style="color:#cba6f7;">&lt;시작&gt;</span>, <span style="color:#a6e3a1;">I</span>
  Attention: <span style="color:#f9e2af;">"먹었다"에 집중</span>  →  <span style="color:#a6e3a1;">"ate"</span> 생성

<span style="color:#6c7086;">[3번째 생성]</span>
  입력: <span style="color:#cba6f7;">&lt;시작&gt;</span>, <span style="color:#a6e3a1;">I</span>, <span style="color:#a6e3a1;">ate</span>
  Attention: <span style="color:#f9e2af;">"밥을"에 집중</span>  →  <span style="color:#a6e3a1;">"rice"</span> 생성

<span style="color:#6c7086;">[4번째 생성]</span>
  입력: <span style="color:#cba6f7;">&lt;시작&gt;</span>, <span style="color:#a6e3a1;">I</span>, <span style="color:#a6e3a1;">ate</span>, <span style="color:#a6e3a1;">rice</span>
  →  <span style="color:#cba6f7;">&lt;종료&gt;</span> 생성  →  <span style="color:#f9e2af;">번역 완료!</span>

<span style="color:#a6e3a1;">최종 출력: "I ate rice"</span></div>
</div>

</div>

<br>

<!-- 전체 구조 다이어그램 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 Decoder 전체 구조 한눈에
</h2>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Decoder 전체 구조</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">지금까지 생성한 출력 단어들</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#cba6f7;">임베딩 + Positional Encoding</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#89dceb;">┌──────────────────────────────────────────────┐</span>
<span style="color:#89dceb;">│             Decoder Layer × 6                │</span>
<span style="color:#89dceb;">│                                              │</span>
<span style="color:#89dceb;">│  </span><span style="color:#f38ba8;">┌────────────────────────────────────────┐</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#f38ba8;">│  ① Masked Multi-Head Self-Attention    │</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#f38ba8;">└──────────────────┬─────────────────────┘</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│                   </span><span style="color:#89dceb;">↓</span>                        <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#6c7086;">┌────────────────────────────────────────┐</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#6c7086;">│  ② Add & Norm                          │</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#6c7086;">└──────────────────┬─────────────────────┘</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│                   </span><span style="color:#89dceb;">↓</span>      <span style="color:#cba6f7;">↑ Encoder 출력</span>    <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#f9e2af;">┌────────────────────────────────────────┐</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#f9e2af;">│  ③ Encoder-Decoder Attention           │</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#f9e2af;">└──────────────────┬─────────────────────┘</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│                   </span><span style="color:#89dceb;">↓</span>                        <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#6c7086;">┌────────────────────────────────────────┐</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#6c7086;">│  ④ Add & Norm                          │</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#6c7086;">└──────────────────┬─────────────────────┘</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│                   </span><span style="color:#89dceb;">↓</span>                        <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#f38ba8;">┌────────────────────────────────────────┐</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#f38ba8;">│  ⑤ Feed Forward Network               │</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#f38ba8;">└──────────────────┬─────────────────────┘</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│                   </span><span style="color:#89dceb;">↓</span>                        <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#6c7086;">┌────────────────────────────────────────┐</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#6c7086;">│  ⑥ Add & Norm                          │</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│  </span><span style="color:#6c7086;">└────────────────────────────────────────┘</span>  <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">└──────────────────────────────────────────────┘</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#cba6f7;">Linear + Softmax</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#a6e3a1;">다음 단어 확률 분포 → 단어 선택</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#f9e2af;">[종료 신호 나올 때까지 반복]</span></div>
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="font-size: 15px; font-weight: 900; margin-bottom: 14px;">
<span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리
</div>

<div style="overflow-x: auto; margin-bottom: 14px;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; font-weight:900;">단계</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">역할</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">임베딩 + PE</td>
      <td style="padding:10px 14px; color:#334155;">이전 생성 단어 → 위치 포함 벡터</td>
    </tr>
    <tr style="background:#fff8f4; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Masked Self-Attention</td>
      <td style="padding:10px 14px; color:#334155;">이전 단어들 사이 관계 (미래 단어 차단)</td>
    </tr>
    <tr style="background:#fff; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Encoder-Decoder Attention</td>
      <td style="padding:10px 14px; color:#334155;">원문 어느 부분을 참고할지 결정</td>
    </tr>
    <tr style="background:#fff8f4; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">FFN</td>
      <td style="padding:10px 14px; color:#334155;">단어 표현 심화</td>
    </tr>
    <tr style="background:#fff; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Add &amp; Norm × 3</td>
      <td style="padding:10px 14px; color:#334155;">정보 보존 + 안정화</td>
    </tr>
    <tr style="background:#fff8f4;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Linear + Softmax</td>
      <td style="padding:10px 14px; color:#334155;">다음 단어 확률 계산</td>
    </tr>
  </tbody>
</table>
</div>

<div style="background:#fff; border-left:4px solid #FF6B00; padding:12px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#FF6B00; font-weight:900;">🎯 Decoder의 목표는 단 하나입니다:</span><br>
<b style="color:#FF6B00;">"Encoder가 이해한 원문 내용을 바탕으로, 한 번에 한 단어씩 자연스러운 번역을 만들어내기"</b>
</div>

</div>

</div>