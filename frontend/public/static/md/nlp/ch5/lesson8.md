<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Encoder — Multi-Head Attention
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Self-Attention을 여러 개 동시에 실행해
<b style="color:#1681c4;">다양한 언어 관계를 한 번에 포착</b>하는 Multi-Head Attention을 알아봅니다.
</p>

</div>

<br>

<!-- Self-Attention 하나의 한계 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🤔 Self-Attention 하나로는 부족한 이유
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
하나의 Self-Attention에는 <b style="color:#FF6B00;">한 가지 관점</b>밖에 없다는 한계가 있습니다.<br>
아래 문장을 봅시다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; font-weight: 900; line-height: 1.8; text-align: center; margin: 14px 0;">
<span style="color: #1681c4;">"나는 어제 친구와 함께 맛있는 밥을 먹었다"</span>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 12px;">
이 문장 안에는 <b>여러 종류의 관계</b>가 섞여 있습니다.
</p>

<div style="display: grid; gap: 8px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">문법</div>
    <div style="font-size:14px; color:#334155;">"먹었다"의 주어는 "나는" <span style="color:#94a3b8;">(동사-주어 관계)</span></div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">의미</div>
    <div style="font-size:14px; color:#334155;">"맛있는"은 "밥을"을 꾸밈 <span style="color:#94a3b8;">(형용사-명사 관계)</span></div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">시간</div>
    <div style="font-size:14px; color:#334155;">"어제"는 행위가 일어난 시점 <span style="color:#94a3b8;">(시간 부사 관계)</span></div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">동반</div>
    <div style="font-size:14px; color:#334155;">"친구와 함께"는 누구와 행동했는지 <span style="color:#94a3b8;">(동반자 관계)</span></div>
  </div>
</div>

<div style="margin-top:14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">⚠️</span> Self-Attention 하나는 이 여러 관계 중 <b style="color:#FF6B00;">하나의 패턴에 집중</b>하는 경향이 있습니다.
</div>

</div>

<br>

<!-- Multi-Head Attention 개념 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
👀 Multi-Head Attention: 여러 전문가가 동시에 분석한다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
<b>Multi-Head Attention</b>은 Self-Attention을 <b style="color:#1681c4;">여러 개(h개) 동시에 실행</b>하는 방법입니다.
</p>

<!-- 영화 평론가 비유 -->
<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 16px 18px; border-radius: 14px; margin: 16px 0;">
  <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:12px;">🎬 한 편의 영화를 여러 전문 평론가가 동시에 보는 것</div>
  <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; margin-bottom:12px;">
    <div style="background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 12px; font-size:13px; color:#475569; line-height:1.7;">
      <b style="color:#1681c4;">평론가 1:</b> 스토리 구조에 집중
    </div>
    <div style="background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 12px; font-size:13px; color:#475569; line-height:1.7;">
      <b style="color:#1681c4;">평론가 2:</b> 배우의 연기에 집중
    </div>
    <div style="background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 12px; font-size:13px; color:#475569; line-height:1.7;">
      <b style="color:#1681c4;">평론가 3:</b> 촬영 기법에 집중
    </div>
    <div style="background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 12px; font-size:13px; color:#475569; line-height:1.7;">
      <b style="color:#1681c4;">평론가 4:</b> 음악에 집중
    </div>
  </div>
  <div style="font-size:13px; color:#334155; text-align:center; font-weight:900;">
    → 마지막에 <b style="color:#1681c4;">모든 평론가의 의견을 종합</b>해서 최종 리뷰를 만든다.
  </div>
</div>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-bottom: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">각 Head가 집중하는 관계</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#cba6f7;">[Head 1]</span>: <span style="color:#a6e3a1;">"먹었다"</span> → <span style="color:#f9e2af;">"나는"</span>에 높은 주목  <span style="color:#6c7086;">(주어-동사 관계)</span>
<span style="color:#cba6f7;">[Head 2]</span>: <span style="color:#a6e3a1;">"맛있는"</span> → <span style="color:#f9e2af;">"밥을"</span>에 높은 주목  <span style="color:#6c7086;">(형용사-명사 관계)</span>
<span style="color:#cba6f7;">[Head 3]</span>: <span style="color:#a6e3a1;">"어제"</span> → <span style="color:#f9e2af;">"먹었다"</span>에 높은 주목  <span style="color:#6c7086;">(시간-동사 관계)</span>
<span style="color:#cba6f7;">[Head 4]</span>: <span style="color:#a6e3a1;">"함께"</span> → <span style="color:#f9e2af;">"친구와"</span>에 높은 주목  <span style="color:#6c7086;">(동반 관계)</span>
<span style="color:#6c7086;">...
[Head 8]</span>: 또 다른 관계 파악</div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌</span> 원래 논문에서는 <b style="color:#FF6B00;">8개의 Head</b>를 사용했습니다.
</div>

</div>

<br>

<!-- 작동 방식 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔧 Multi-Head Attention 작동 방식
</h2>

<div style="display: grid; gap: 10px;">

  <!-- STEP 1 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 1</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">입력 벡터를 각 Head에 맞게 변환</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">입력: "나는 배가 고프다" (각 단어가 512차원 벡터)</span>
        <span style="color:#89dceb;">↓</span>
<span style="color:#cba6f7;">Head 1</span>의 변환 → <span style="color:#a6e3a1;">Q1, K1, V1</span>  <span style="color:#89dceb;">(64차원)</span>  <span style="color:#6c7086;">← Head 1만의 시각</span>
<span style="color:#cba6f7;">Head 2</span>의 변환 → <span style="color:#a6e3a1;">Q2, K2, V2</span>  <span style="color:#89dceb;">(64차원)</span>  <span style="color:#6c7086;">← Head 2만의 시각</span>
<span style="color:#6c7086;">...</span>
<span style="color:#cba6f7;">Head 8</span>의 변환 → <span style="color:#a6e3a1;">Q8, K8, V8</span>  <span style="color:#89dceb;">(64차원)</span>  <span style="color:#6c7086;">← Head 8만의 시각</span></div>
      <div style="margin-top:10px; background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:10px 14px; font-size:13px; color:#334155; line-height:1.7;">
        <b style="color:#1681c4;">왜 64차원인가?</b> 512차원을 8개로 나누면 64차원입니다. <span style="color:#94a3b8;">(512 ÷ 8 = 64)</span><br>
        각 Head가 전체 정보를 나눠서 담당하는 셈입니다.
      </div>
    </div>
  </div>

  <!-- STEP 2 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 2</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">각 Head가 독립적으로 Self-Attention 수행</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#cba6f7;">Head 1</span>: 64차원 Q1, K1, V1 → Self-Attention → <span style="color:#a6e3a1;">결과값 64차원</span>
<span style="color:#cba6f7;">Head 2</span>: 64차원 Q2, K2, V2 → Self-Attention → <span style="color:#a6e3a1;">결과값 64차원</span>
<span style="color:#6c7086;">...</span>
<span style="color:#cba6f7;">Head 8</span>: 64차원 Q8, K8, V8 → Self-Attention → <span style="color:#a6e3a1;">결과값 64차원</span></div>
      <div style="margin-top:10px; background-color: #fff3eb; border: 1px solid #ffd0b0; padding: 9px 13px; border-radius: 8px; font-size: 13px; color: #334155; line-height: 1.7;">
        <span style="color: #FF6B00; font-weight: 900;">💡</span> 8개의 Head가 <b style="color:#FF6B00;">병렬로(동시에)</b> Self-Attention을 실행합니다.
      </div>
    </div>
  </div>

  <!-- STEP 3 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 3</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">모든 Head의 결과를 이어 붙인다 <span style="color:#94a3b8; font-size:12px; font-weight:400;">(Concatenate)</span></div>
      <div style="display: grid; gap: 6px; margin-bottom:8px;">
        <div style="background:#0f172a; border-radius:6px; padding:8px 14px; font-family:Consolas,monospace; font-size:13px; display:flex; justify-content:space-between; align-items:center;">
          <span style="color:#cba6f7;">Head 1 결과</span>
          <span style="color:#89dceb;">64차원</span>
        </div>
        <div style="background:#0f172a; border-radius:6px; padding:8px 14px; font-family:Consolas,monospace; font-size:13px; display:flex; justify-content:space-between; align-items:center;">
          <span style="color:#cba6f7;">Head 2 결과</span>
          <span style="color:#89dceb;">64차원</span>
        </div>
        <div style="background:#0f172a; border-radius:6px; padding:8px 14px; font-family:Consolas,monospace; font-size:13px; display:flex; justify-content:space-between; align-items:center;">
          <span style="color:#6c7086;">...</span>
          <span style="color:#6c7086;">...</span>
        </div>
        <div style="background:#0f172a; border-radius:6px; padding:8px 14px; font-family:Consolas,monospace; font-size:13px; display:flex; justify-content:space-between; align-items:center;">
          <span style="color:#cba6f7;">Head 8 결과</span>
          <span style="color:#89dceb;">64차원</span>
        </div>
      </div>
      <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:8px; padding:10px 14px; text-align:center; font-family:Consolas,monospace; font-size:13px; color:#1681c4; font-weight:900;">
        전부 이어 붙임 → <span style="color:#f9e2af;">512차원</span> <span style="color:#6c7086; font-weight:400;">(= 64 × 8)</span>
      </div>
    </div>
  </div>

  <!-- STEP 4 -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 4</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">최종 선형 변환으로 합치기</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#89dceb;">[512차원]</span> → <span style="color:#cba6f7;">선형 변환(W_O 행렬)</span> → <span style="color:#a6e3a1;">[512차원]</span></div>
      <div style="margin-top:8px; font-size:13px; color:#475569; line-height:1.7;">
        각 Head의 정보가 적절히 혼합된 <b style="color:#1681c4;">최종 Multi-Head Attention 결과</b>가 완성됩니다.
      </div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 전체 흐름 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 Multi-Head Attention 전체 흐름 한눈에
</h2>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Multi-Head Attention 전체 구조</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">입력 단어 벡터 (512차원)</span>
         <span style="color:#89dceb;">│</span>
   <span style="color:#f38ba8;">┌─────┴─────┐</span>
   <span style="color:#f38ba8;">│  8개로 분할 │</span>
   <span style="color:#f38ba8;">└─────┬─────┘</span>
         <span style="color:#89dceb;">│</span>
 <span style="color:#cba6f7;">┌───┬───┼───┬───┐</span>
 <span style="color:#cba6f7;">H1  H2  H3 ... H8</span>     <span style="color:#6c7086;">← 각 Head가 독립적으로 Self-Attention</span>
 <span style="color:#cba6f7;">│   │   │       │</span>
 <span style="color:#cba6f7;">└───┴───┼───┴───┘</span>
         <span style="color:#89dceb;">│</span>
   <span style="color:#a6e3a1;">┌─────┴──────┐</span>
   <span style="color:#a6e3a1;">│  이어 붙이기 │</span>   <span style="color:#6c7086;">(64×8 = 512차원)</span>
   <span style="color:#a6e3a1;">└─────┬──────┘</span>
         <span style="color:#89dceb;">│</span>
   <span style="color:#89dceb;">┌─────┴─────┐</span>
   <span style="color:#89dceb;">│  선형 변환  │</span>
   <span style="color:#89dceb;">└─────┬─────┘</span>
         <span style="color:#89dceb;">│</span>
<span style="color:#f9e2af;">출력 단어 벡터 (512차원)</span>  <span style="color:#6c7086;">← 여러 관점이 통합된 풍부한 표현</span></div>
</div>

</div>

<br>

<!-- 왜 강력한가 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🌟 Multi-Head Attention이 왜 강력한가요?
</h2>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:10px;">❌ 하나의 Self-Attention</div>
    <div style="display:grid; gap:6px;">
      <div style="background:#fff; border-left:3px solid #ffd0b0; padding:7px 10px; border-radius:0 6px 6px 0; font-size:13px; color:#475569; line-height:1.6;">학습 중 하나의 패턴에만 지나치게 집중할 수 있습니다.</div>
      <div style="background:#fff; border-left:3px solid #ffd0b0; padding:7px 10px; border-radius:0 6px 6px 0; font-size:13px; color:#475569; line-height:1.6;">문장의 다양한 측면을 동시에 포착하기 어렵습니다.</div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">✅ Multi-Head Attention</div>
    <div style="display:grid; gap:6px;">
      <div style="background:#fff; border-left:3px solid #c2e4ff; padding:7px 10px; border-radius:0 6px 6px 0; font-size:13px; color:#334155; line-height:1.6;">각 Head가 <b style="color:#1681c4;">서로 다른 관계 패턴</b>을 담당합니다.</div>
      <div style="background:#fff; border-left:3px solid #c2e4ff; padding:7px 10px; border-radius:0 6px 6px 0; font-size:13px; color:#334155; line-height:1.6;">문법·의미·시간 관계 등을 <b style="color:#1681c4;">동시에 모두 포착</b>합니다.</div>
      <div style="background:#fff; border-left:3px solid #c2e4ff; padding:7px 10px; border-radius:0 6px 6px 0; font-size:13px; color:#334155; line-height:1.6;">여러 Head의 결과를 합쳐 <b style="color:#1681c4;">훨씬 풍부한 표현</b>이 만들어집니다.</div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 실제 연구 결과 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💡 실제로 각 Head가 무엇을 학습하는지 연구된 결과
</h2>

<div style="overflow-x: auto; margin: 14px 0;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; font-weight:900;">Head</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">주로 학습한 패턴</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">일부 Head</td>
      <td style="padding:10px 14px; color:#334155;">다음 단어와의 관계 (인접 단어)</td>
    </tr>
    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">일부 Head</td>
      <td style="padding:10px 14px; color:#334155;">대명사와 그 지칭 대상 연결</td>
    </tr>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">일부 Head</td>
      <td style="padding:10px 14px; color:#334155;">동사와 주어/목적어 관계</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">일부 Head</td>
      <td style="padding:10px 14px; color:#334155;">문장 전체의 전반적 관계</td>
    </tr>
  </tbody>
</table>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> 이 패턴들을 사람이 직접 설계하지 않아도, 데이터에서 <b style="color:#1681c4;">자동으로 발견</b>합니다.
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
    <b style="color:#FF6B00;">Multi-Head Attention</b> = Self-Attention을 <b style="color:#FF6B00;">여러 개 동시에</b> 실행하는 방법입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    각 Head는 문장 안의 <b style="color:#FF6B00;">서로 다른 관계 패턴</b>에 집중하도록 학습됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    원래 논문에서는 <b style="color:#FF6B00;">8개의 Head</b>를 사용했습니다. <span style="color:#94a3b8;">(512차원 ÷ 8 = 64차원/Head)</span>
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    모든 Head의 결과를 <b style="color:#FF6B00;">이어 붙이고 선형 변환</b>하여 최종 출력을 만듭니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    하나의 Self-Attention보다 훨씬 <b style="color:#FF6B00;">다양한 언어적 관계</b>를 동시에 포착할 수 있습니다.
  </div>
</div>

<div style="margin-top:12px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> 다음 페이지에서는 지금까지 배운 것들이 Encoder 안에서 어떻게 조합되어 흐르는지,<br>
<b style="color:#1681c4;">Encoder 전체 흐름</b>을 처음부터 끝까지 따라가 봅니다.
</div>

</div>

</div>