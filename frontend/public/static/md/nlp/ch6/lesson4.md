<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
BERT의 핵심 아이디어 — MLM & NSP
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
BERT가 언어를 배우는 독특한 두 가지 방법,<br>
<b style="color:#1681c4;">Masked Language Model(MLM)</b>과 <b style="color:#1681c4;">Next Sentence Prediction(NSP)</b>을 이해합니다.
</p>

</div>

<br>

<!-- MLM -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎭 핵심 아이디어 ② : Masked Language Model (MLM)
</h2>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 15px; font-weight: 900; line-height: 1.8; text-align: center; margin: 0 0 18px 0;">
<span style="color: #FF6B00;">단어를 가리고 맞히게 한다</span>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
학습 과정에서 입력 문장의 일부 단어를 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 7px; border-radius:6px; font-weight:900;">[MASK]</code> 토큰으로 가리고,
모델에게 <b>"원래 단어가 뭐였을까?"</b>를 맞히게 합니다.
</p>

<!-- 비유 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px; margin:14px 0;">
  <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:10px;">📝 비유: 빈칸 채우기 문제</div>
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:10px; padding:14px 16px; font-size:15px; color:#1681c4; font-weight:900; text-align:center; margin-bottom:10px;">
    "나는 오늘 ____에서 커피를 마셨다."
  </div>
  <div style="font-size:14px; color:#334155; line-height:1.8;">
  이 문제를 풀려면 앞("나는 오늘")과 뒤("에서 커피를 마셨다")를 <b>모두</b> 봐야 합니다.<br>
  BERT는 이런 빈칸 채우기를 <b style="color:#FF6B00;">수십억 번 반복</b>하면서 언어의 문법과 의미 관계를 스스로 익힙니다.
  </div>
</div>

<!-- MLM 과정 -->
<div style="display: grid; gap: 10px; margin-top: 14px;">

  <div style="background:#1e1e2e; border-radius:14px; overflow:hidden; font-family:'JetBrains Mono','Consolas',monospace;">
    <div style="background:#0d0d1a; border-bottom:1px solid #1a1a2e; padding:11px 15px; display:flex; align-items:center; gap:6px;">
      <div style="width:10px; height:10px; background:#ff5f57; border-radius:50%;"></div>
      <div style="width:10px; height:10px; background:#ffbd2e; border-radius:50%;"></div>
      <div style="width:10px; height:10px; background:#28ca41; border-radius:50%;"></div>
      <span style="color:#8b8bc7; margin-left:8px; font-size:12px;">MLM 학습 과정</span>
    </div>
    <div style="padding:18px; font-size:13px; line-height:2.4; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">원문:   </span><span style="color:#a6e3a1;">"나는  오늘  카페  에서  커피를  마셨다"</span>
<span style="color:#6c7086;">        ↓ 15% 확률로 단어를 [MASK]로 교체</span>
<span style="color:#6c7086;">입력:   </span><span style="color:#cdd6f4;">"나는  오늘  </span><span style="color:#f38ba8; font-weight:900;">[MASK]</span><span style="color:#cdd6f4;">  에서  커피를  마셨다"</span>
<span style="color:#6c7086;">        ↓ BERT가 [MASK] 자리 예측</span>
<span style="color:#6c7086;">출력:   </span><span style="color:#a6e3a1; font-weight:900;">"카페"</span>  <span style="color:#6c7086;">← 맞으면 학습 성공!</span></div>
  </div>

</div>

<div style="margin-top:14px; background:#eef7ff; border:2px solid #c2e4ff; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#1681c4; font-weight:900;">🔑 핵심:</span> 정답 레이블을 <b style="color:#1681c4;">사람이 달아줄 필요가 없습니다.</b><br>
원문이 곧 정답이기 때문입니다. (자기지도학습, Self-supervised Learning)
</div>

</div>

<br>

<!-- NSP -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔗 핵심 아이디어 ③ : Next Sentence Prediction (NSP)
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BERT는 MLM 외에도 <b>두 문장 간의 관계</b>를 이해하는 훈련도 받습니다.<br>
"이 두 문장은 이어지는 내용일까?"
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">

  <div style="background:#f0fdf4; border:2px solid #86efac; border-radius:14px; overflow:hidden;">
    <div style="background:#16a34a; padding:10px 16px;">
      <div style="font-size:13px; font-weight:900; color:#fff;">✅ IsNext — 이어지는 문장</div>
    </div>
    <div style="padding:14px 16px;">
      <div style="font-size:13px; color:#334155; line-height:1.8; margin-bottom:8px;">
        <b style="color:#64748b;">문장 A:</b> "강아지는 공원에서 뛰어놀았다."<br>
        <b style="color:#64748b;">문장 B:</b> "지치고 배가 고팠는지 집에 오자마자 밥을 먹었다."
      </div>
      <div style="background:#16a34a; color:#fff; padding:6px 12px; border-radius:8px; font-size:13px; font-weight:900; display:inline-block;">IsNext ✅</div>
    </div>
  </div>

  <div style="background:#fff1f2; border:2px solid #fca5a5; border-radius:14px; overflow:hidden;">
    <div style="background:#dc2626; padding:10px 16px;">
      <div style="font-size:13px; font-weight:900; color:#fff;">❌ NotNext — 관계없는 문장</div>
    </div>
    <div style="padding:14px 16px;">
      <div style="font-size:13px; color:#334155; line-height:1.8; margin-bottom:8px;">
        <b style="color:#64748b;">문장 A:</b> "강아지는 공원에서 뛰어놀았다."<br>
        <b style="color:#64748b;">문장 B:</b> "오늘 주식 시장이 크게 하락했다."
      </div>
      <div style="background:#dc2626; color:#fff; padding:6px 12px; border-radius:8px; font-size:13px; font-weight:900; display:inline-block;">NotNext ❌</div>
    </div>
  </div>

</div>

<div style="margin-top:14px; background:#fff3eb; border:2px solid #ffd0b0; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#FF6B00; font-weight:900;">💡</span> 이 훈련을 통해 BERT는 <b style="color:#FF6B00;">문장 간의 논리적 흐름과 관계</b>를 파악합니다.<br>
질의응답(Q&A), 문장 관계 분류 등의 과제에 활용됩니다.
</div>

</div>

<br>

<!-- BERT 전체 구조 조감도 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🗺️ BERT 전체 구조 조감도
</h2>

<div style="background:#1e1e2e; border-radius:14px; overflow:hidden; margin:14px 0;">
  <div style="background:#0d0d1a; border-bottom:1px solid #1a1a2e; padding:11px 15px; display:flex; align-items:center; gap:6px;">
    <div style="width:10px; height:10px; background:#ff5f57; border-radius:50%;"></div>
    <div style="width:10px; height:10px; background:#ffbd2e; border-radius:50%;"></div>
    <div style="width:10px; height:10px; background:#28ca41; border-radius:50%;"></div>
    <span style="color:#8b8bc7; margin-left:8px; font-size:12px;">BERT Architecture</span>
  </div>
  <div style="padding:18px; font-size:12px; line-height:2.2; overflow-x:auto; white-space:pre; font-family:'JetBrains Mono','Consolas',monospace;">
<span style="color:#89dceb;">┌─────────────────────────────────────────────────┐</span>
<span style="color:#89dceb;">│</span>             <span style="color:#f9e2af; font-weight:900;">사전학습 (Pre-training)</span>               <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│</span>                                                 <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│</span>  입력: <span style="color:#a6e3a1;">"나는 [MASK] 카페에서 커피를 마셨다"</span>        <span style="color:#89dceb;">     │</span>
<span style="color:#89dceb;">│</span>         + <span style="color:#a6e3a1;">"[CLS] 문장A [SEP] 문장B [SEP]"</span>       <span style="color:#89dceb;">  │</span>
<span style="color:#89dceb;">│</span>                                                 <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│</span>  <span style="color:#89dceb;">┌──────────────────────────────────┐</span>           <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│</span>  <span style="color:#89dceb;">│</span>  <span style="color:#cba6f7;">트랜스포머 인코더 × 12 레이어</span>         <span style="color:#89dceb;">│</span>           <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│</span>  <span style="color:#89dceb;">│</span>  <span style="color:#6c7086;">(Self-Attention + Feed Forward)</span> <span style="color:#89dceb;">│</span>           <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│</span>  <span style="color:#89dceb;">└──────────────────────────────────┘</span>           <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│</span>                                                 <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│</span>  학습 목표 ①: <span style="color:#f38ba8;">[MASK] 자리 단어 맞히기 (MLM)</span>           <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">│</span>  학습 목표 ②: <span style="color:#f38ba8;">두 문장이 이어지는지 판단 (NSP)</span>           <span style="color:#89dceb;">│</span>
<span style="color:#89dceb;">└──────────────────────────┬──────────────────────┘</span>
                           <span style="color:#6c7086;">↓ 사전학습 완료된 BERT</span>
<span style="color:#a6e3a1;">┌─────────────────────────────────────────────────┐</span>
<span style="color:#a6e3a1;">│</span>            <span style="color:#a6e3a1; font-weight:900;">미세조정 (Fine-tuning)</span>                 <span style="color:#a6e3a1;">│</span>
<span style="color:#a6e3a1;">│</span>                                                 <span style="color:#a6e3a1;">│</span>
<span style="color:#a6e3a1;">│</span>  <span style="color:#cdd6f4;">감정 분류 / 질의응답 / 번역 / 요약 / ...</span>              <span style="color:#a6e3a1;">│</span>
<span style="color:#a6e3a1;">│</span>  <span style="color:#6c7086;">(소량의 레이블 데이터로 짧게 추가 학습)</span>                 <span style="color:#a6e3a1;">│</span>
<span style="color:#a6e3a1;">└─────────────────────────────────────────────────┘</span></div>
</div>

</div>

<br>

<!-- BERT 모델 종류 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📦 BERT 모델 종류
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
구글은 두 가지 크기의 BERT를 공개했습니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:20px 22px; text-align:center;">
    <div style="font-size:13px; font-weight:900; color:#64748b; margin-bottom:8px;">BERT-Base</div>
    <div style="font-size:30px; font-weight:900; color:#0f172a; margin-bottom:8px;">12층</div>
    <div style="font-size:14px; color:#475569; line-height:1.7; margin-bottom:10px;">파라미터 <b>1.1억 개</b></div>
    <div style="background:#e2e8f0; color:#475569; padding:6px 14px; border-radius:8px; font-size:13px; font-weight:900; display:inline-block;">일반적인 사용</div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:20px 22px; text-align:center;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:8px;">BERT-Large</div>
    <div style="font-size:30px; font-weight:900; color:#1681c4; margin-bottom:8px;">24층</div>
    <div style="font-size:14px; color:#475569; line-height:1.7; margin-bottom:10px;">파라미터 <b>3.4억 개</b></div>
    <div style="background:#1681c4; color:#fff; padding:6px 14px; border-radius:8px; font-size:13px; font-weight:900; display:inline-block;">높은 성능 필요 시</div>
  </div>

</div>

<div style="margin-top:14px; background:#fff3eb; border:2px solid #ffd0b0; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#FF6B00; font-weight:900;">💡</span> 레이어(층)가 많을수록 더 복잡한 언어 패턴을 학습할 수 있지만, <b style="color:#FF6B00;">계산 비용도 커집니다.</b>
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
    BERT의 핵심 아이디어는 <b style="color:#FF6B00;">① 양방향 학습</b>, <b style="color:#FF6B00;">② MLM(빈칸 채우기)</b>, <b style="color:#FF6B00;">③ NSP(다음 문장 예측)</b>입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">MLM</b>은 문장의 일부 단어를 가리고 맞히는 훈련으로, 사람이 정답을 달아줄 필요 없이 대규모 학습이 가능합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">NSP</b>는 두 문장의 관계를 이해하는 훈련으로, 질의응답 같은 과제에 도움을 줍니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    사전학습 후 <b style="color:#FF6B00;">미세조정만으로</b> 다양한 과제에 강력한 성능을 발휘합니다.
  </div>
</div>

</div>

</div>