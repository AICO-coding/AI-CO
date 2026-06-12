<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
BERT와 Transformer Encoder
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
BERT를 이해하려면 먼저 <b style="color:#1681c4;">트랜스포머(Transformer)</b>를 알아야 합니다.<br>
인코더와 디코더 구조, 그리고 BERT가 왜 인코더만 사용하는지 알아봅니다.
</p>

</div>

<br>

<!-- 트랜스포머란 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🏛️ 트랜스포머(Transformer)란?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
트랜스포머는 2017년 구글이 발표한 논문 <b>"Attention Is All You Need"</b>에서 소개된 모델 구조입니다.<br>
현재 BERT, GPT, ChatGPT 등 거의 모든 최신 언어 모델의 기반이 됩니다.
</p>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; margin-top: 14px;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 트랜스포머 이전에는 RNN/LSTM이 주류였습니다.<br>
트랜스포머는 RNN 없이 <b style="color:#FF6B00;">Attention만으로</b> 언어를 처리하는 구조를 제안했습니다.
</div>

</div>

<br>

<!-- 두 가지 블록 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🏗️ 트랜스포머의 두 가지 블록
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
원래 트랜스포머는 <b>인코더</b>와 <b>디코더</b> 두 부분으로 나뉩니다.
</p>

<!-- 다이어그램 -->
<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Transformer 구조</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">입력 문장: </span><span style="color:#a6e3a1;">"나는 밥을 먹었다"</span>
       <span style="color:#6c7086;">↓</span>
<span style="color:#89dceb;">┌─────────────────┐</span>
<span style="color:#89dceb;">│    인코더         │</span>  <span style="color:#6c7086;">← 입력 문장을 이해하는 역할</span>
<span style="color:#89dceb;">│  (Encoder)      │</span>     <span style="color:#6c7086;">"의미를 읽어서 벡터로 압축"</span>
<span style="color:#89dceb;">└────────┬────────┘</span>
         <span style="color:#6c7086;">↓ (문맥이 담긴 벡터)</span>
<span style="color:#cba6f7;">┌─────────────────┐</span>
<span style="color:#cba6f7;">│    디코더         │</span>  <span style="color:#6c7086;">← 결과 문장을 생성하는 역할</span>
<span style="color:#cba6f7;">│  (Decoder)      │</span>     <span style="color:#6c7086;">"벡터를 보고 번역/답변 생성"</span>
<span style="color:#cba6f7;">└─────────────────┘</span>
       <span style="color:#6c7086;">↓</span>
<span style="color:#6c7086;">출력 문장: </span><span style="color:#a6e3a1;">"I ate rice"</span></div>
</div>

<!-- 비교 테이블 -->
<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">인코더</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:4px;">입력 문장 이해 → 벡터로 표현</div>
      <div style="font-size:14px; color:#475569; line-height:1.7;">주요 사용 모델: <b style="color:#1681c4;">BERT</b></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#64748b; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">디코더</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#64748b; margin-bottom:4px;">벡터 → 새로운 문장 생성</div>
      <div style="font-size:14px; color:#475569; line-height:1.7;">주요 사용 모델: GPT</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#64748b; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">인코더+디코더</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#64748b; margin-bottom:4px;">이해 + 생성 (번역 등)</div>
      <div style="font-size:14px; color:#475569; line-height:1.7;">주요 사용 모델: T5, 원래 Transformer</div>
    </div>
  </div>

</div>

</div>

<br>

<!-- BERT는 인코더만 사용 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔍 BERT는 인코더만 사용합니다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BERT는 트랜스포머 전체 구조 중 <b>인코더(Encoder) 부분만</b> 가져와서 사용합니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; line-height: 1.9; text-align: center; margin: 14px 0;">
BERT의 목표는 <b>문장을 생성</b>하는 것이 아니라,<br>
문장을 <b>깊이 이해</b>하는 것이기 때문입니다.
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:18px 20px; text-align:center;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:8px;">문장 이해</div>
    <div style="font-size:13px; color:#334155; line-height:1.7; margin-bottom:12px;">분류, 감정 분석, 질의응답</div>
    <div style="background:#1681c4; color:#fff; padding:6px 14px; border-radius:8px; font-size:13px; font-weight:900; display:inline-block;">인코더 ← BERT</div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px; text-align:center;">
    <div style="font-size:13px; font-weight:900; color:#64748b; margin-bottom:8px;">문장 생성</div>
    <div style="font-size:13px; color:#334155; line-height:1.7; margin-bottom:12px;">번역, 요약, 대화</div>
    <div style="background:#64748b; color:#fff; padding:6px 14px; border-radius:8px; font-size:13px; font-weight:900; display:inline-block;">디코더 또는 인코더+디코더</div>
  </div>

</div>

</div>

<br>

<!-- BERT 전체 층 구조 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧱 BERT의 전체 층 구조
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BERT는 인코더 블록을 <b>여러 겹 쌓은 구조</b>입니다. 층이 쌓일수록 더 복잡하고 추상적인 언어 패턴을 학습합니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">BERT 층 구조 (BERT-Base 기준)</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">입력 토큰들</span>
<span style="color:#a6e3a1;">[CLS] 나는 오늘 [MASK] 에서 커피를 마셨다 [SEP]</span>
       <span style="color:#6c7086;">↓ 임베딩</span>
<span style="color:#89dceb;">┌─────────────────────────────┐</span>
<span style="color:#89dceb;">│  Transformer Encoder 1층    │</span>
<span style="color:#89dceb;">└──────────────┬──────────────┘</span>
               <span style="color:#6c7086;">↓</span>
<span style="color:#89dceb;">┌─────────────────────────────┐</span>
<span style="color:#89dceb;">│  Transformer Encoder 2층    │</span>
<span style="color:#89dceb;">└──────────────┬──────────────┘</span>
               <span style="color:#6c7086;">↓  (계속...)</span>
               <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1;">┌─────────────────────────────┐</span>
<span style="color:#a6e3a1;">│  Transformer Encoder 12층   │</span>
<span style="color:#a6e3a1;">└──────────────┬──────────────┘</span>
               <span style="color:#6c7086;">↓</span>
<span style="color:#cdd6f4;">각 토큰별 문맥 벡터 출력 (768차원 × 토큰 수)</span></div>
</div>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#e2e8f0; color:#64748b; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap;">1~3층</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">단어의 형태, 품사 같은 <b>표면적인 특징</b>을 학습합니다.</div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#c2e4ff; color:#1681c4; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap;">4~8층</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">문법 구조, <b style="color:#1681c4;">단어 간 관계</b>를 학습합니다.</div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap;">9~12층</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">문장의 <b style="color:#1681c4;">의미, 추론, 문맥</b> 수준의 이해를 학습합니다.</div>
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
    트랜스포머는 <b style="color:#FF6B00;">인코더(이해)</b>와 <b style="color:#FF6B00;">디코더(생성)</b> 두 블록으로 구성됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    BERT는 그 중 <b style="color:#FF6B00;">인코더만</b> 가져와 쌓은 구조입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    인코더를 12층(또는 24층) 쌓으면서 <b style="color:#FF6B00;">점점 더 깊은 수준의 언어 이해</b>가 가능해집니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    각 층에서 핵심적으로 일어나는 작업이 <b style="color:#FF6B00;">Self-Attention</b>이고, 다음 화면에서 자세히 살펴봅니다.
  </div>
</div>

</div>

</div>