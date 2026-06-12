<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Encoder 전체 흐름
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
지금까지 배운 모든 블록이 Encoder 안에서
<b style="color:#1681c4;">어떻게 연결되어 흐르는지</b> 처음부터 끝까지 따라가 봅니다.
</p>

</div>

<br>

<!-- 지금까지 배운 것 정리 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🗺️ 지금까지 배운 것을 조합해봅시다
</h2>

<div style="display: grid; gap: 8px; margin-top: 14px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">5-3</div>
    <div style="font-size:14px; color:#334155;"><b style="color:#1681c4;">Positional Encoding</b> — 각 단어에 "나는 몇 번째 단어" 위치 정보를 추가</div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">5-4</div>
    <div style="font-size:14px; color:#334155;"><b style="color:#1681c4;">Self-Attention</b> — 같은 문장 안 단어들이 서로의 관계를 계산</div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">5-5</div>
    <div style="font-size:14px; color:#334155;"><b style="color:#1681c4;">Multi-Head Attention</b> — Self-Attention을 8개 시각으로 동시에 실행</div>
  </div>
</div>

<div style="margin-top:14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> 이 조각들이 Encoder 안에서 어떻게 연결되는지, 지금부터 처음부터 끝까지 따라가 봅시다.
</div>

</div>

<br>

<!-- STEP 1~7 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
"나는 밥을 먹었다" — 입력부터 출력까지
</h2>

<div style="display: grid; gap: 12px; margin-top: 4px;">

  <!-- STEP 1 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 1</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">입력 준비: 토큰화 + 임베딩</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">입력 문장: "나는 밥을 먹었다"</span>  →  <span style="color:#a6e3a1;">["나는", "밥을", "먹었다"]</span>

<span style="color:#6c7086;">임베딩 변환 (각 단어 → 512차원 벡터):</span>
<span style="color:#a6e3a1;">나는</span>   → <span style="color:#89dceb;">[0.21, 0.53, 0.08, ..., 0.32]</span>  <span style="color:#6c7086;">(512개 숫자)</span>
<span style="color:#a6e3a1;">밥을</span>   → <span style="color:#89dceb;">[0.65, 0.12, 0.91, ..., 0.59]</span>  <span style="color:#6c7086;">(512개 숫자)</span>
<span style="color:#a6e3a1;">먹었다</span> → <span style="color:#89dceb;">[0.38, 0.80, 0.27, ..., 0.11]</span>  <span style="color:#6c7086;">(512개 숫자)</span></div>
      <div style="margin-top:8px; background:#fff3eb; border:1px solid #ffd0b0; border-radius:8px; padding:8px 12px; font-size:13px; color:#334155; line-height:1.7;">
        <span style="color:#FF6B00; font-weight:900;">⚠️</span> 아직 <b style="color:#FF6B00;">순서 정보가 없습니다.</b>
      </div>
    </div>
  </div>

  <!-- STEP 2 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 2</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">Positional Encoding 추가</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">나는</span>   벡터  <span style="color:#f9e2af;">+</span>  위치 1 인코딩  <span style="color:#89dceb;">=</span>  <span style="color:#cba6f7;">나는_위치포함</span>
<span style="color:#a6e3a1;">밥을</span>   벡터  <span style="color:#f9e2af;">+</span>  위치 2 인코딩  <span style="color:#89dceb;">=</span>  <span style="color:#cba6f7;">밥을_위치포함</span>
<span style="color:#a6e3a1;">먹었다</span> 벡터  <span style="color:#f9e2af;">+</span>  위치 3 인코딩  <span style="color:#89dceb;">=</span>  <span style="color:#cba6f7;">먹었다_위치포함</span></div>
      <div style="margin-top:8px; background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:8px 12px; font-size:13px; color:#334155; line-height:1.7;">
        sin/cos 패턴의 위치 정보가 <b style="color:#1681c4;">더해짐으로써</b> 각 단어 벡터에 순서 정보가 녹아듭니다.
      </div>
    </div>
  </div>

  <!-- STEP 3 -->
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 3</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:8px;">Multi-Head Self-Attention</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#cba6f7;">[나는_위치포함]  </span>──┐
<span style="color:#cba6f7;">[밥을_위치포함]  </span>──┼──→ <span style="color:#f9e2af;">Multi-Head Attention (8 Heads)</span>
<span style="color:#cba6f7;">[먹었다_위치포함]</span>──┘
                         <span style="color:#6c7086;">↓ 각 Head가 서로 다른 관계 탐색</span>
                         <span style="color:#6c7086;">↓ 결과를 이어 붙이고 선형 변환</span>

<span style="color:#a6e3a1;">[나는_문맥반영]</span>   <span style="color:#6c7086;">← "먹었다"의 주어라는 정보가 녹아있음</span>
<span style="color:#a6e3a1;">[밥을_문맥반영]</span>   <span style="color:#6c7086;">← "먹었다"의 목적어라는 정보가 녹아있음</span>
<span style="color:#a6e3a1;">[먹었다_문맥반영]</span> <span style="color:#6c7086;">← "나는"이 주어, "밥을"이 목적어 정보가 녹아있음</span></div>
    </div>
  </div>

  <!-- STEP 4 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 4</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">Add &amp; Norm <span style="color:#94a3b8; font-size:12px; font-weight:400;">(잔차 연결 + 레이어 정규화)</span></div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">입력 X  +  Attention(X)</span>
               <span style="color:#f9e2af;">↓ ADD</span>  <span style="color:#6c7086;">← 원래 값 + 새로운 값</span>
         <span style="color:#a6e3a1;">X + Attention(X)</span>
               <span style="color:#cba6f7;">↓ NORM</span> <span style="color:#6c7086;">← 값의 크기를 안정적으로 조정</span>
         <span style="color:#89dceb;">정규화된 벡터들</span></div>
      <div style="margin-top:8px; background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:8px 12px; font-size:13px; color:#334155; line-height:1.7;">
        원본을 완전히 지우지 않고 <b style="color:#1681c4;">보완하는 방식</b>이라 중요한 정보가 사라지지 않습니다.
      </div>
    </div>
  </div>

  <!-- STEP 5 -->
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 5</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:8px;">Feed Forward Network (FFN)</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">[나는_문맥반영_정규화]</span>   → <span style="color:#f9e2af;">FFN</span> → <span style="color:#89dceb;">[나는_더욱풍부]</span>
<span style="color:#a6e3a1;">[밥을_문맥반영_정규화]</span>   → <span style="color:#f9e2af;">FFN</span> → <span style="color:#89dceb;">[밥을_더욱풍부]</span>
<span style="color:#a6e3a1;">[먹었다_문맥반영_정규화]</span> → <span style="color:#f9e2af;">FFN</span> → <span style="color:#89dceb;">[먹었다_더욱풍부]</span>

<span style="color:#6c7086;">FFN 내부: 512 → 2048 → ReLU → 512</span></div>
    </div>
  </div>

  <!-- STEP 6 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 6</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">또 한 번 Add &amp; Norm</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">FFN 입력 + FFN 출력</span> → <span style="color:#f9e2af;">ADD</span> → <span style="color:#cba6f7;">NORM</span> → <span style="color:#a6e3a1;">이 레이어의 최종 출력</span></div>
    </div>
  </div>

  <!-- STEP 7 -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 7</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">레이어 6번 반복</div>
      <div style="display:grid; gap:6px;">
        <div style="background:#0f172a; border-radius:6px; padding:8px 14px; font-family:Consolas,monospace; font-size:13px; display:flex; align-items:center; gap:10px;">
          <span style="color:#6c7086; white-space:nowrap;">Layer 1~2:</span>
          <span style="color:#a6e3a1;">단어와 바로 이웃한 관계 파악</span>
        </div>
        <div style="background:#0f172a; border-radius:6px; padding:8px 14px; font-family:Consolas,monospace; font-size:13px; display:flex; align-items:center; gap:10px;">
          <span style="color:#6c7086; white-space:nowrap;">Layer 3~4:</span>
          <span style="color:#cba6f7;">좀 더 넓은 문맥 파악</span>
        </div>
        <div style="background:#0f172a; border-radius:6px; padding:8px 14px; font-family:Consolas,monospace; font-size:13px; display:flex; align-items:center; gap:10px;">
          <span style="color:#6c7086; white-space:nowrap;">Layer 5~6:</span>
          <span style="color:#f9e2af;">문장 전체의 고차원적 의미 파악</span>
        </div>
      </div>
    </div>
  </div>

</div>

</div>

<br>

<!-- Encoder 최종 출력 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📤 Encoder의 최종 출력
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
Encoder를 모두 통과하면, 입력한 각 단어마다 <b>512차원 벡터</b> 하나씩 출력됩니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-bottom: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Encoder 입력 → 출력</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">입력:  </span>[<span style="color:#a6e3a1;">"나는"</span>,     <span style="color:#a6e3a1;">"밥을"</span>,     <span style="color:#a6e3a1;">"먹었다"</span>]
<span style="color:#6c7086;">출력:  </span>[<span style="color:#f9e2af;">벡터_나는</span>, <span style="color:#f9e2af;">벡터_밥을</span>, <span style="color:#f9e2af;">벡터_먹었다</span>]
        <span style="color:#6c7086;">(512차원)   (512차원)    (512차원)</span></div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> 이 벡터들은 단순한 단어 의미가 아니라,<br>
<b style="color:#1681c4;">문장 전체 맥락이 반영된 풍부한 표현</b>입니다.<br>
이 출력이 Decoder로 전달되어 번역 생성에 사용됩니다.
</div>

</div>

<br>

<!-- 전체 구조 다이어그램 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 Encoder 전체 구조 한눈에
</h2>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Encoder 전체 구조</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">입력 문장</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#6c7086;">임베딩 변환 (단어 → 512차원 벡터)</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#cba6f7;">Positional Encoding 추가 (위치 정보 +)</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#f38ba8;">┌────────────────────────────────────────┐</span>
<span style="color:#f38ba8;">│           Encoder Layer × 6            │</span>
<span style="color:#f38ba8;">│                                        │</span>
<span style="color:#f38ba8;">│  </span><span style="color:#f9e2af;">┌──────────────────────────────────┐</span>  <span style="color:#f38ba8;">│</span>
<span style="color:#f38ba8;">│  </span><span style="color:#f9e2af;">│  Multi-Head Self-Attention (×8)  │</span>  <span style="color:#f38ba8;">│</span>
<span style="color:#f38ba8;">│  </span><span style="color:#f9e2af;">└──────────────┬───────────────────┘</span>  <span style="color:#f38ba8;">│</span>
<span style="color:#f38ba8;">│               </span><span style="color:#89dceb;">↓</span>                      <span style="color:#f38ba8;">  │</span>
<span style="color:#f38ba8;">│  </span><span style="color:#6c7086;">┌──────────────────────────────────┐</span>  <span style="color:#f38ba8;">│</span>
<span style="color:#f38ba8;">│  </span><span style="color:#6c7086;">│      Add & Norm (잔차 + 정규화)   │</span>  <span style="color:#f38ba8;">  │</span>
<span style="color:#f38ba8;">│  </span><span style="color:#6c7086;">└──────────────┬───────────────────┘</span>  <span style="color:#f38ba8;">│</span>
<span style="color:#f38ba8;">│               </span><span style="color:#89dceb;">↓</span>                      <span style="color:#f38ba8;">  │</span>
<span style="color:#f38ba8;">│  </span><span style="color:#f9e2af;">┌──────────────────────────────────┐</span>  <span style="color:#f38ba8;">│</span>
<span style="color:#f38ba8;">│  </span><span style="color:#f9e2af;">│    Feed Forward Network (FFN)    │</span>  <span style="color:#f38ba8;">│</span>
<span style="color:#f38ba8;">│  </span><span style="color:#f9e2af;">└──────────────┬───────────────────┘</span>  <span style="color:#f38ba8;">│</span>
<span style="color:#f38ba8;">│               </span><span style="color:#89dceb;">↓</span>                      <span style="color:#f38ba8;">  │</span>
<span style="color:#f38ba8;">│  </span><span style="color:#6c7086;">┌──────────────────────────────────┐</span>  <span style="color:#f38ba8;">│</span>
<span style="color:#f38ba8;">│  </span><span style="color:#6c7086;">│      Add & Norm (잔차 + 정규화)   │</span>  <span style="color:#f38ba8;">  │</span>
<span style="color:#f38ba8;">│  </span><span style="color:#6c7086;">└──────────────────────────────────┘</span>  <span style="color:#f38ba8;">│</span>
<span style="color:#f38ba8;">└────────────────────────────────────────┘</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#a6e3a1;">Encoder 최종 출력 (각 단어별 512차원 벡터)</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#89dceb;">→ Decoder로 전달</span></div>
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
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">임베딩</td>
      <td style="padding:10px 14px; color:#334155;">단어 → 512차원 숫자 벡터</td>
    </tr>
    <tr style="background:#fff8f4; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Positional Encoding</td>
      <td style="padding:10px 14px; color:#334155;">위치 정보(몇 번째 단어) 추가</td>
    </tr>
    <tr style="background:#fff; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Multi-Head Attention</td>
      <td style="padding:10px 14px; color:#334155;">8가지 관점으로 단어 간 관계 동시 탐색</td>
    </tr>
    <tr style="background:#fff8f4; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Add &amp; Norm</td>
      <td style="padding:10px 14px; color:#334155;">정보 손실 방지 + 학습 안정화</td>
    </tr>
    <tr style="background:#fff; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">FFN</td>
      <td style="padding:10px 14px; color:#334155;">각 단어 표현을 비선형으로 풍부하게 변환</td>
    </tr>
    <tr style="background:#fff8f4;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">× 6 반복</td>
      <td style="padding:10px 14px; color:#334155;">점점 더 깊고 추상적인 문맥 이해</td>
    </tr>
  </tbody>
</table>
</div>

<div style="background:#fff; border-left:4px solid #FF6B00; padding:12px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#FF6B00; font-weight:900;">🎯 Encoder의 목표는 단 하나입니다:</span><br>
<b style="color:#FF6B00;">"이 문장이 무슨 뜻인지 완전히 이해한 벡터를 만들어서 Decoder에게 넘겨주기"</b>
</div>

</div>

</div>