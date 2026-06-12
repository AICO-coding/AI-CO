<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
FFN 내부 구조와 전체 흐름 정리
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
FFN이 <b style="color:#1681c4;">어떻게 넓혔다가 좁히는지</b>, 실제 숫자가 어떻게 변하는지 따라가 봅니다.
</p>

</div>

<br>

<!-- FFN 내부 구조 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔧 FFN 내부 구조: 3단계
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
FFN의 핵심은 <b style="color:#FF6B00;">"넓혔다가 좁힌다"</b>는 것입니다.
</p>

<div style="display: grid; gap: 0; margin: 18px 0;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; text-align:center; font-size:14px; font-weight:900; color:#475569;">
    입력 벡터 <span style="color:#89dceb;">(512차원)</span>
  </div>
  <div style="text-align:center; color:#94a3b8; font-size:18px; font-weight:900; margin:3px 0;">↓</div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center;">
    <div>
      <div style="font-size:14px; font-weight:900; color:#FF6B00;">선형 변환 1</div>
      <div style="font-size:13px; color:#475569; margin-top:3px;">W1 행렬 곱 (512 × 2048)</div>
    </div>
    <div style="font-family:Consolas,monospace; font-size:13px; color:#f9e2af; background:#0f172a; padding:6px 14px; border-radius:8px; font-weight:900;">→ 2048차원으로 확장 (×4)</div>
  </div>
  <div style="text-align:center; color:#94a3b8; font-size:18px; font-weight:900; margin:3px 0;">↓</div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center;">
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4;">ReLU</div>
      <div style="font-size:13px; color:#475569; margin-top:3px;">0 이하 값 제거</div>
    </div>
    <div style="font-family:Consolas,monospace; font-size:13px; color:#89dceb; background:#0f172a; padding:6px 14px; border-radius:8px;">→ 중요 패턴만 남김</div>
  </div>
  <div style="text-align:center; color:#94a3b8; font-size:18px; font-weight:900; margin:3px 0;">↓</div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center;">
    <div>
      <div style="font-size:14px; font-weight:900; color:#FF6B00;">선형 변환 2</div>
      <div style="font-size:13px; color:#475569; margin-top:3px;">W2 행렬 곱 (2048 × 512)</div>
    </div>
    <div style="font-family:Consolas,monospace; font-size:13px; color:#a6e3a1; background:#0f172a; padding:6px 14px; border-radius:8px; font-weight:900;">→ 512차원으로 다시 축소</div>
  </div>
  <div style="text-align:center; color:#94a3b8; font-size:18px; font-weight:900; margin:3px 0;">↓</div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:12px 16px; text-align:center; font-size:14px; font-weight:900; color:#1681c4;">
    출력 벡터 <span style="color:#89dceb;">(512차원)</span>
  </div>

</div>

</div>

<br>

<!-- 왜 넓혔다 줄이나 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📐 왜 2048차원으로 넓혔다가 줄일까요?
</h2>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 16px 18px; border-radius: 14px; margin-bottom: 16px;">
  <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">🗂️ 비유: 공간을 넓혀서 분류하기</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 10px;">
    <div style="background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 12px; font-size:13px; color:#475569; line-height:1.7; text-align:center;">
      <b style="color:#FF6B00;">2D 공간</b>에서는<br>직선 하나로 분리 불가 ❌
    </div>
    <div style="background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 12px; font-size:13px; color:#475569; line-height:1.7; text-align:center;">
      <b style="color:#1681c4;">3D 공간</b>으로 올리면<br>평면으로 깔끔하게 분리 ✅
    </div>
  </div>
  <div style="font-size:13px; color:#334155; line-height:1.8; text-align:center;">
    512차원에서 표현하기 어려운 패턴이 2048차원으로 넓히면 <b style="color:#1681c4;">더 쉽게 분리하고 표현</b>할 수 있게 됩니다.
  </div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 넓힌 공간에서 ReLU로 중요한 패턴을 선택한 뒤,<br>
다시 512차원으로 <b style="color:#FF6B00;">압축해서 핵심 정보만 남깁니다.</b>
</div>

</div>

<br>

<!-- 실제 숫자 계산 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔢 실제 숫자가 어떻게 변하는지 따라가 보기
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
단순화된 예시로 FFN 계산 과정을 따라가 봅시다. <span style="color:#94a3b8;">(이해를 위해 512→2048 대신 4→8→4 크기로 줄였습니다.)</span>
</p>

<div style="display: grid; gap: 10px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 1</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:6px;">입력 벡터 <span style="color:#94a3b8; font-size:12px; font-weight:400;">(Add &amp; Norm을 거친 "밥을" 벡터)</span></div>
      <div style="font-family:Consolas,monospace; font-size:13px; color:#a6e3a1; background:#0f172a; padding:8px 12px; border-radius:8px;">
        입력 = <span style="color:#89dceb;">[0.3, -0.5, 0.8, 0.2]</span>
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 2</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:6px;">선형 변환 1 <span style="color:#94a3b8; font-size:12px; font-weight:400;">(4차원 → 8차원으로 확장)</span></div>
      <div style="font-family:Consolas,monospace; font-size:13px; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8;">
        <span style="color:#6c7086;">W1 행렬 곱셈 후:</span><br>
        = <span style="color:#f9e2af;">[1.2, -0.3, 0.7, 2.1, -1.5, 0.4, -0.8, 1.0]</span>
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 3</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:6px;">ReLU 적용 <span style="color:#94a3b8; font-size:12px; font-weight:400;">(0 이하 → 0으로)</span></div>
      <div style="font-family:Consolas,monospace; font-size:13px; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:2; overflow-x:auto; white-space:pre;">
= [<span style="color:#a6e3a1;">1.2</span>, <span style="color:#89dceb;"> 0.0</span>, <span style="color:#a6e3a1;">0.7</span>, <span style="color:#a6e3a1;">2.1</span>, <span style="color:#89dceb;"> 0.0</span>, <span style="color:#a6e3a1;">0.4</span>, <span style="color:#89dceb;"> 0.0</span>, <span style="color:#a6e3a1;">1.0</span>]
  <span style="color:#a6e3a1;">↑살아남음</span>  <span style="color:#89dceb;">↑음수제거</span>            <span style="color:#89dceb;">↑음수제거</span>      <span style="color:#89dceb;">↑음수제거</span></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 4</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:6px;">선형 변환 2 <span style="color:#94a3b8; font-size:12px; font-weight:400;">(8차원 → 4차원으로 축소)</span></div>
      <div style="font-family:Consolas,monospace; font-size:13px; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8;">
        <span style="color:#6c7086;">W2 행렬 곱셈 후:</span><br>
        = <span style="color:#a6e3a1;">[0.6, 0.9, -0.2, 0.7]</span>
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">결과</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">"밥을"의 새로운 벡터</div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
        <div style="background:#0f172a; border-radius:8px; padding:10px 12px; font-family:Consolas,monospace; font-size:13px; text-align:center;">
          <div style="color:#6c7086; font-size:11px; margin-bottom:4px;">입력</div>
          <div style="color:#6c7086;">[0.3, -0.5, 0.8, 0.2]</div>
        </div>
        <div style="background:#0f172a; border:2px solid #c2e4ff; border-radius:8px; padding:10px 12px; font-family:Consolas,monospace; font-size:13px; text-align:center;">
          <div style="color:#1681c4; font-size:11px; margin-bottom:4px;">출력</div>
          <div style="color:#a6e3a1;">[0.6, 0.9, -0.2, 0.7]</div>
        </div>
      </div>
    </div>
  </div>

</div>

</div>

<br>

<!-- W1, W2 설명 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔢 W1, W2는 무엇인가요?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
W1과 W2는 <b>학습을 통해 결정되는 가중치 행렬</b>입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-bottom: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">학습 전 vs 학습 후</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#f38ba8;">학습 전 W1:</span>  <span style="color:#6c7086;">[ 0.12, -0.34, 0.56, ... ]  ← 의미 없는 랜덤 값</span>
<span style="color:#a6e3a1;">학습 후 W1:</span>  <span style="color:#89dceb;">[ 0.87, -0.02, 0.43, ... ]  ← "동사 표현 강화" 패턴을 담은 값</span></div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> Transformer를 학습시킨다는 것은 곧<br>
<b style="color:#1681c4;">W1, W2(그리고 Q, K, V 등 모든 행렬)의 값을 최적화하는 과정</b>입니다.
</div>

</div>

<br>

<!-- 파라미터 수 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 FFN의 파라미터 수
</h2>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">파라미터 계산</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">W1 크기:</span>  512 × 2048 = <span style="color:#a6e3a1;">1,048,576</span>개
<span style="color:#6c7086;">b1 (편향):</span>             <span style="color:#a6e3a1;">2,048</span>개
<span style="color:#6c7086;">W2 크기:</span> 2048 × 512  = <span style="color:#a6e3a1;">1,048,576</span>개
<span style="color:#6c7086;">b2 (편향):</span>               <span style="color:#a6e3a1;">512</span>개

<span style="color:#cba6f7;">FFN 하나의 파라미터 수 ≈ 210만 개</span>
<span style="color:#cba6f7;">Encoder 레이어 6개 × FFN 1개 = ≈ 1,260만 개</span>

<span style="color:#f9e2af;">(전체 Transformer의 파라미터는 ≈ 6,500만 개)</span></div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 전체 파라미터의 상당 부분을 FFN이 차지합니다.<br>
이 많은 파라미터 덕분에 <b style="color:#FF6B00;">수많은 언어 패턴을 기억</b>할 수 있습니다.
</div>

</div>

<br>

<!-- Self-Attention과 FFN의 분업 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 Self-Attention과 FFN의 완벽한 분업
</h2>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">처리 전 vs 후 비교</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#89dceb;">[Self-Attention 처리 후]</span>  <span style="color:#6c7086;">"나는" 벡터 안에:</span>
  → <span style="color:#a6e3a1;">"먹었다"의 주어라는 관계 정보 포함</span>  ✅
  → <span style="color:#f38ba8;">"한국어에서 나는 = 1인칭 주어" 지식</span>  ❌

<span style="color:#cba6f7;">[FFN 처리 후]</span>  <span style="color:#6c7086;">"나는" 벡터 안에:</span>
  → <span style="color:#a6e3a1;">"먹었다"의 주어라는 관계 정보</span>       ✅ <span style="color:#6c7086;">(Self-Attention에서)</span>
  → <span style="color:#a6e3a1;">"1인칭 주어, 문장 앞에 위치"</span>         ✅ <span style="color:#6c7086;">(FFN이 추가)</span>
  → <span style="color:#a6e3a1;">"나는 = 행위자" 언어 패턴</span>            ✅ <span style="color:#6c7086;">(FFN이 추가)</span></div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:12px 14px; text-align:center; font-size:13px; color:#334155; line-height:1.7;">
    <b style="color:#1681c4;">Self-Attention</b><br>"이 문장에서의 관계"
  </div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:12px 14px; text-align:center; font-size:13px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">FFN</b><br>"언어 전반에서 학습한 지식"
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
    <b style="color:#FF6B00;">FFN 구조</b>: 입력(512) → <b style="color:#FF6B00;">확장</b>(2048) → <b style="color:#FF6B00;">ReLU</b> → <b style="color:#FF6B00;">축소</b>(512) → 출력
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    차원을 <b style="color:#FF6B00;">4배 넓혔다 줄이는</b> 이유: 고차원 공간에서 복잡한 패턴을 더 잘 분리할 수 있기 때문
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">ReLU</b>: 0 이하 값을 제거해 비선형성을 추가하고 중요 패턴만 남김
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">W1, W2</b>: 학습을 통해 수억 개의 언어 패턴을 기억하는 가중치
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Self-Attention(관계 파악) + FFN(지식 적용) = <b style="color:#FF6B00;">Encoder 레이어 한 층의 완전한 처리</b>
  </div>
</div>

<div style="margin-top:12px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> 이제 Encoder를 구성하는 모든 핵심 블록을 배웠습니다. 다음은 <b style="color:#1681c4;">Decoder</b>로 넘어갑니다!
</div>

</div>

</div>