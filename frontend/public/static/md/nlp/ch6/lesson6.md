<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
인코더 블록 내부
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
인코더 블록 하나가 내부에서 어떻게 작동하는지 살펴봅니다.<br>
<b style="color:#1681c4;">Multi-Head Self-Attention</b>과 <b style="color:#1681c4;">Feed Forward Network</b>, 두 단계로 이루어집니다.
</p>

</div>

<br>

<!-- 인코더 블록 전체 흐름 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔬 인코더 블록 구조 한눈에 보기
</h2>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Encoder Block 내부 구조</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">입력 벡터들 (각 토큰의 임베딩)</span>
         <span style="color:#6c7086;">↓</span>
<span style="color:#89dceb;">┌──────────────────────────────┐</span>
<span style="color:#89dceb;">│  ① Multi-Head Self-Attention │</span>  <span style="color:#6c7086;">← "각 단어가 다른 단어들과 얼마나 관련 있나?"</span>
<span style="color:#89dceb;">└──────────────┬───────────────┘</span>
               <span style="color:#6c7086;">↓ (+ 잔차 연결 &amp; 정규화)</span>
<span style="color:#a6e3a1;">┌──────────────────────────────┐</span>
<span style="color:#a6e3a1;">│  ② Feed Forward Network      │</span>  <span style="color:#6c7086;">← "각 단어 벡터를 더 풍부하게 변환"</span>
<span style="color:#a6e3a1;">└──────────────┬───────────────┘</span>
               <span style="color:#6c7086;">↓ (+ 잔차 연결 &amp; 정규화)</span>
<span style="color:#cdd6f4;">출력 벡터들 (문맥이 반영된 각 토큰의 벡터)</span></div>
</div>

</div>

<br>

<!-- Multi-Head Self-Attention -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎯 ① Multi-Head Self-Attention
</h2>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center; margin-bottom: 18px;">
"여러 시각으로 동시에 관계를 바라본다"
</div>

<!-- 비유: 편집회의 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px; margin-bottom:18px;">
  <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:12px;">📋 비유: 신문 기사 편집회의</div>
  <p style="font-size:14px; color:#334155; line-height:1.8; margin:0 0 14px 0;">
  편집장 한 명이 기사를 검토하면 한 가지 시각만 반영됩니다. 하지만 <b>편집자 8명이 각자 다른 관점</b>으로 같은 기사를 검토한다면?
  </p>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; line-height:1.7;">
      <b style="color:#1681c4;">편집자 A:</b> 문법 오류 관점
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; line-height:1.7;">
      <b style="color:#1681c4;">편집자 B:</b> 사실 관계 관점
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; line-height:1.7;">
      <b style="color:#1681c4;">편집자 C:</b> 문체 관점
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; line-height:1.7;">
      <b style="color:#1681c4;">편집자 D:</b> 독자 흥미 관점
    </div>
  </div>
  <div style="margin-top:10px; background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; line-height:1.7;">
    <span style="color:#FF6B00; font-weight:900;">💡</span> 각자의 검토를 <b style="color:#FF6B00;">종합</b>하면 훨씬 풍부하고 정확한 결과가 나옵니다. Multi-Head Self-Attention도 같은 방식입니다.
  </div>
</div>

<!-- 멀티헤드 다이어그램 -->
<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin-bottom: 18px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Multi-Head 구조</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.2; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#cdd6f4;">입력 벡터</span>
    <span style="color:#6c7086;">↓ (동시에 여러 헤드로 분리)</span>
<span style="color:#89dceb;">Head 1:</span>  <span style="color:#6c7086;">"주어-서술어 관계에 집중"</span>
<span style="color:#89dceb;">Head 2:</span>  <span style="color:#6c7086;">"수식어-명사 관계에 집중"</span>
<span style="color:#89dceb;">Head 3:</span>  <span style="color:#6c7086;">"대명사가 가리키는 것에 집중"</span>
<span style="color:#89dceb;">Head 4:</span>  <span style="color:#6c7086;">"시제 관련 단어들 관계에 집중"</span>
<span style="color:#6c7086;">...  (BERT-Base는 12개 헤드)</span>
    <span style="color:#6c7086;">↓ (모든 헤드 결과를 합침)</span>
<span style="color:#a6e3a1;">종합된 풍부한 문맥 벡터</span></div>
</div>

<!-- Attention 계산 흐름 -->
<div style="display: grid; gap: 14px;">

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 1</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">세 가지 벡터 생성 (Q · K · V)</div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px;">
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:11px; text-align:center;">
      <div style="font-size:22px; font-weight:900; color:#1681c4;">Q</div>
      <div style="font-size:12px; color:#334155; margin-top:4px; line-height:1.5;">"카페"가 다른 단어에게 묻는 질문 벡터</div>
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:11px; text-align:center;">
      <div style="font-size:22px; font-weight:900; color:#1681c4;">K</div>
      <div style="font-size:12px; color:#334155; margin-top:4px; line-height:1.5;">"카페"가 갖고 있는 정보 벡터</div>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px; text-align:center;">
      <div style="font-size:22px; font-weight:900; color:#FF6B00;">V</div>
      <div style="font-size:12px; color:#334155; margin-top:4px; line-height:1.5;">"카페"의 실제 내용 벡터</div>
    </div>
  </div>
</div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 2</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">Attention Score 계산</div>
  </div>
  <div style="background:#1e1e2e; border-radius:10px; padding:14px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.3; overflow-x:auto; white-space:pre;">
<span style="color:#cdd6f4;">Q(카페) · K(나는)   = </span><span style="color:#f38ba8;">0.2</span>  <span style="color:#6c7086;">← 관련도 낮음</span>
<span style="color:#cdd6f4;">Q(카페) · K(오늘)   = </span><span style="color:#f38ba8;">0.3</span>
<span style="color:#cdd6f4;">Q(카페) · K(에서)   = </span><span style="color:#f9e2af; font-weight:900;">0.8</span>  <span style="color:#6c7086;">← 관련도 높음 (장소 조사)</span>
<span style="color:#cdd6f4;">Q(카페) · K(커피를) = </span><span style="color:#a6e3a1; font-weight:900;">0.9</span>  <span style="color:#6c7086;">← 관련도 매우 높음 (카페=커피)</span>
<span style="color:#cdd6f4;">Q(카페) · K(마셨다) = </span><span style="color:#f9e2af;">0.6</span></div>
</div>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 3</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">Value 가중합산 → 최종 벡터</div>
  </div>
  <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.8;">
    관련도(점수)에 따라 Value를 가중합산하면<br>
    <b style="color:#FF6B00;">"카페"의 최종 벡터 = 문맥이 충분히 반영된 표현</b>이 완성됩니다.
  </div>
</div>

</div>

</div>

<br>

<!-- Feed Forward Network -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
⚙️ ② Feed Forward Network (FFN)
</h2>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #FF6B00; font-weight: 900; text-align: center; margin-bottom: 18px;">
"Self-Attention 결과를 한 번 더 깊이 처리"
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Self-Attention이 <b>단어들 사이의 관계</b>를 계산했다면, FFN은 그 결과를 받아서 <b>각 단어 벡터를 더 풍부하게 변환</b>합니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">FFN 변환 과정</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#cdd6f4;">Self-Attention 출력 벡터 </span><span style="color:#89dceb;">(768차원)</span>
         <span style="color:#6c7086;">↓</span>
<span style="color:#6c7086;">    선형 변환 </span><span style="color:#f9e2af;">(768 → 3072차원으로 확장)</span>  <span style="color:#6c7086;">← 넓게 펼치기</span>
         <span style="color:#6c7086;">↓</span>
<span style="color:#6c7086;">    활성화 함수 (GELU) </span><span style="color:#6c7086;">— 비선형성 추가</span>
         <span style="color:#6c7086;">↓</span>
<span style="color:#6c7086;">    선형 변환 </span><span style="color:#a6e3a1;">(3072 → 768차원으로 압축)</span>  <span style="color:#6c7086;">← 핵심만 선별</span>
         <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">풍부해진 벡터 </span><span style="color:#89dceb;">(768차원)</span></div>
</div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#1681c4; font-weight:900;">💡 왜 크게 늘렸다가 다시 줄일까요?</span><br>
<b style="color:#1681c4;">크게 펼치면서</b> 다양한 언어 패턴을 찾아내고, <b style="color:#1681c4;">다시 압축하면서</b> 가장 중요한 정보만 남깁니다.<br>
마치 넓게 수집하고 선별하는 과정입니다.
</div>

</div>

<br>

<!-- 잔차 연결 & 정규화 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 잔차 연결과 레이어 정규화
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
인코더 블록에는 두 가지 안정화 기법이 함께 쓰입니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:18px 20px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">🔗 잔차 연결 (Add)</div>
    <div style="background:#1e1e2e; border-radius:10px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; color:#a6e3a1; text-align:center; margin-bottom:10px;">
      출력 = 입력 + Self-Attention(입력)
    </div>
    <div style="font-size:13px; color:#334155; line-height:1.7;">
      층이 깊어질수록 학습이 불안정해지는 문제를 막습니다.<br>
      원래 입력을 <b style="color:#1681c4;">그대로 더해줘서</b> 정보가 소실되지 않도록 합니다.
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:10px;">📐 레이어 정규화 (Layer Norm)</div>
    <div style="background:#1e1e2e; border-radius:10px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; color:#f9e2af; text-align:center; margin-bottom:10px;">
      값의 범위를 일정하게 조정
    </div>
    <div style="font-size:13px; color:#334155; line-height:1.7;">
      값의 범위를 일정하게 맞춰 학습을 <b style="color:#FF6B00;">안정적으로</b> 만들어 줍니다.
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
    인코더 블록은 <b style="color:#FF6B00;">① Multi-Head Self-Attention</b> → <b style="color:#FF6B00;">② Feed Forward Network</b> 순으로 처리됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Multi-Head는 <b style="color:#FF6B00;">여러 시각(헤드)으로 동시에</b> 단어 간 관계를 바라보는 방식입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    FFN은 Self-Attention 결과를 <b style="color:#FF6B00;">한 번 더 변환해 표현을 풍부하게</b> 만듭니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">잔차 연결</b>과 <b style="color:#FF6B00;">레이어 정규화</b>가 함께 작동해 깊은 층에서도 학습이 안정됩니다.
  </div>
</div>

</div>

</div>