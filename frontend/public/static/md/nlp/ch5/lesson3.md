<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Transformer의 전체 구조 — Encoder와 Decoder
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Transformer가 어떤 두 파트로 나뉘는지,
<b style="color:#1681c4;">Encoder와 Decoder</b>의 역할을 함께 알아봅니다.
</p>

</div>

<br>

<!-- 번역 공장 비유 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🏭 Transformer를 "번역 공장"으로 상상해보세요
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Transformer를 처음 이해할 때 가장 좋은 비유는 <b>번역 공장</b>입니다.<br>
이 공장은 크게 <b style="color:#1681c4;">두 개의 작업실</b>로 나뉩니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 15px; font-weight: 900; line-height: 1.8; text-align: center; margin: 14px 0;">
<span style="color: #1681c4;">"한국어 문장을 입력하면 → 영어 문장이 출력된다"</span>
</div>

<div style="display: grid; gap: 0; margin-top: 18px;">

  <div style="text-align: center; font-size: 13px; color: #475569; font-weight: 900; margin-bottom: 6px;">
    [입력] 한국어 문장
  </div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin-bottom: 6px;">↓</div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px; margin-bottom:6px;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:6px;">📥 Encoder (인코더)</div>
    <div style="font-size:14px; color:#475569; line-height:1.7;">"이해하는 방" — 입력 문장을 완전히 파악하고 <b style="color:#FF6B00;">의미를 압축</b>합니다.</div>
  </div>

  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin-bottom: 2px;">↓</div>
  <div style="text-align: center; font-size: 12px; color: #94a3b8; margin-bottom: 2px; font-family: 'JetBrains Mono', Consolas, monospace;">문장의 의미 정보 전달</div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin-bottom: 6px;">↓</div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:18px 20px; margin-bottom:6px;">
    <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:6px;">📤 Decoder (디코더)</div>
    <div style="font-size:14px; color:#475569; line-height:1.7;">"생성하는 방" — 이해한 내용을 바탕으로 <b style="color:#1681c4;">번역 결과를 생성</b>합니다.</div>
  </div>

  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin-top: 6px; margin-bottom: 6px;">↓</div>
  <div style="text-align: center; font-size: 13px; color: #475569; font-weight: 900;">
    [출력] 영어 문장
  </div>

</div>

</div>

<br>

<!-- Encoder -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📥 Encoder: "이해하는 방"
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Encoder의 역할은 <b>입력 문장을 완전히 이해하는 것</b>입니다.<br>
입력 문장의 각 단어가 서로 어떤 관계인지 파악해서, <b style="color:#FF6B00;">"이 문장이 담고 있는 의미"를 하나의 정보 묶음으로 압축</b>합니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 18px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Encoder가 파악하는 것</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">예시: "나는 어제 맛있는 밥을 먹었다"</span>

<span style="color:#a6e3a1;">"나는"</span>    <span style="color:#89dceb;">→</span>  <span style="color:#cdd6f4;">행위의 주체</span>
<span style="color:#a6e3a1;">"먹었다"</span>  <span style="color:#89dceb;">→</span>  <span style="color:#cdd6f4;">행동 (과거)</span>
<span style="color:#a6e3a1;">"밥을"</span>    <span style="color:#89dceb;">→</span>  <span style="color:#cdd6f4;">먹은 대상</span>
<span style="color:#a6e3a1;">"맛있는"</span>  <span style="color:#89dceb;">→</span>  <span style="color:#cdd6f4;">밥의 상태</span>
<span style="color:#a6e3a1;">"어제"</span>    <span style="color:#89dceb;">→</span>  <span style="color:#cdd6f4;">시간 정보</span></div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; margin-bottom: 16px;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 이 모든 관계를 파악해서 <b style="color:#FF6B00;">"맥락이 담긴 벡터 묶음"</b>으로 변환합니다.<br>
이것을 <b style="color:#FF6B00;">Context(문맥 정보)</b>라고 부릅니다.
</div>

<div style="display: grid; gap: 8px;">
  <div style="background:#fff3eb; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    입력 문장의 <b style="color:#FF6B00;">모든 단어를 동시에</b> 봅니다.
  </div>
  <div style="background:#fff3eb; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    각 단어가 <b style="color:#FF6B00;">다른 모든 단어와 어떤 관계</b>인지 계산합니다. (Self-Attention)
  </div>
  <div style="background:#fff3eb; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">원본 언어(한국어)</b>만 처리합니다.
  </div>
</div>

</div>

<br>

<!-- Decoder -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📤 Decoder: "생성하는 방"
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Decoder의 역할은 Encoder가 이해한 내용을 바탕으로 <b>출력 문장을 한 단어씩 생성</b>하는 것입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 18px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Decoder 생성 과정</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#cba6f7;">Encoder의 문맥 정보</span> <span style="color:#89dceb;">→</span>  <span style="color:#6c7086;">Decoder</span>
                              <span style="color:#89dceb;">↓</span>
                         <span style="color:#a6e3a1;">[I]</span> <span style="color:#6c7086;">생성</span>
                              <span style="color:#89dceb;">↓</span>
                         <span style="color:#a6e3a1;">[ate]</span> <span style="color:#6c7086;">생성</span>
                              <span style="color:#89dceb;">↓</span>
                         <span style="color:#a6e3a1;">[delicious]</span> <span style="color:#6c7086;">생성</span>
                              <span style="color:#89dceb;">↓</span>
                         <span style="color:#a6e3a1;">[rice]</span> <span style="color:#6c7086;">생성</span>
                              <span style="color:#89dceb;">↓</span>
                         <span style="color:#a6e3a1;">[yesterday]</span> <span style="color:#6c7086;">생성</span></div>
</div>

<div style="display: grid; gap: 8px; margin-top: 4px;">
  <div style="background:#eef7ff; border-left:4px solid #1681c4; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Encoder로부터 받은 <b style="color:#1681c4;">문맥 정보를 참고</b>합니다.
  </div>
  <div style="background:#eef7ff; border-left:4px solid #1681c4; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이미 생성한 <b style="color:#1681c4;">앞 단어들도 참고</b>합니다.
  </div>
  <div style="background:#eef7ff; border-left:4px solid #1681c4; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    출력 언어(영어)를 <b style="color:#1681c4;">순서대로</b> 한 단어씩 생성합니다.
  </div>
</div>

</div>

<br>

<!-- 레이어 쌓기 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔢 레이어가 여러 개 쌓인다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
원래 Transformer 논문에서는 Encoder와 Decoder를 각각 <b>6개씩 쌓았습니다.</b>
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 18px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Encoder 6층 쌓기</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#cba6f7;">[Encoder Layer 6]</span>  <span style="color:#6c7086;">← 가장 위</span>
<span style="color:#cba6f7;">[Encoder Layer 5]</span>
<span style="color:#cba6f7;">[Encoder Layer 4]</span>
<span style="color:#cba6f7;">[Encoder Layer 3]</span>
<span style="color:#cba6f7;">[Encoder Layer 2]</span>
<span style="color:#cba6f7;">[Encoder Layer 1]</span>  <span style="color:#6c7086;">← 입력이 처음 들어오는 곳</span></div>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 12px;">왜 여러 번 쌓을까요?</p>

<div style="display: grid; gap: 8px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">1독</div>
    <div style="font-size:14px; color:#475569;">단어와 문법 파악</div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">2독</div>
    <div style="font-size:14px; color:#475569;">각 문장의 의미 파악</div>
  </div>
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:center;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">3독+</div>
    <div style="font-size:14px; color:#334155;">전체 맥락과 복선 파악 — <b style="color:#1681c4;">레이어가 쌓일수록 더 깊고 추상적인 의미</b>를 이해합니다.</div>
  </div>
</div>

</div>

<br>

<!-- 전체 구조 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🗺️ 전체 구조 한눈에
</h2>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 18px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Transformer 전체 구조</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">Input (입력 문장)</span>
      <span style="color:#89dceb;">↓</span>
<span style="color:#cba6f7;">[Positional Encoding 추가]</span>  <span style="color:#6c7086;">← 단어 순서 정보 부여 (5-3에서 배울 내용!)</span>
      <span style="color:#89dceb;">↓</span>
<span style="color:#f38ba8;">┌─────────────────────────────┐</span>
<span style="color:#f38ba8;">│         ENCODER             │</span>
<span style="color:#f38ba8;">│  ┌───────────────────────┐  │</span>
<span style="color:#f38ba8;">│  │</span>  <span style="color:#cdd6f4;">Encoder Layer × 6</span>   <span style="color:#f38ba8;">│  │</span>
<span style="color:#f38ba8;">│  │</span>  <span style="color:#a6e3a1;">① Self-Attention</span>    <span style="color:#f38ba8;">│  │</span>
<span style="color:#f38ba8;">│  │</span>  <span style="color:#89dceb;">② Add & Norm</span>        <span style="color:#f38ba8;">│  │</span>
<span style="color:#f38ba8;">│  │</span>  <span style="color:#a6e3a1;">③ Feed Forward Net</span>  <span style="color:#f38ba8;">│  │</span>
<span style="color:#f38ba8;">│  │</span>  <span style="color:#89dceb;">④ Add & Norm</span>        <span style="color:#f38ba8;">│  │</span>
<span style="color:#f38ba8;">│  └───────────────────────┘  │</span>
<span style="color:#f38ba8;">└──────────────┬──────────────┘</span>
               <span style="color:#89dceb;">│</span> <span style="color:#6c7086;">문맥 정보(Context)</span>
               <span style="color:#89dceb;">↓</span>
<span style="color:#89dceb;">┌─────────────────────────────┐</span>
<span style="color:#89dceb;">│         DECODER             │</span>
<span style="color:#89dceb;">│  ┌───────────────────────┐  │</span>
<span style="color:#89dceb;">│  │</span>  <span style="color:#cdd6f4;">Decoder Layer × 6</span>   <span style="color:#89dceb;">│  │</span>
<span style="color:#89dceb;">│  │</span>  <span style="color:#a6e3a1;">① Masked Self-Attn</span>  <span style="color:#89dceb;">│  │</span>
<span style="color:#89dceb;">│  │</span>  <span style="color:#cba6f7;">② Add & Norm</span>        <span style="color:#89dceb;">│  │</span>
<span style="color:#89dceb;">│  │</span>  <span style="color:#a6e3a1;">③ Encoder-Decoder</span>   <span style="color:#89dceb;">│  │</span>
<span style="color:#89dceb;">│  │</span>     <span style="color:#a6e3a1;">Attention</span>        <span style="color:#89dceb;">│  │</span>
<span style="color:#89dceb;">│  │</span>  <span style="color:#cba6f7;">④ Add & Norm</span>        <span style="color:#89dceb;">│  │</span>
<span style="color:#89dceb;">│  │</span>  <span style="color:#a6e3a1;">⑤ Feed Forward Net</span>  <span style="color:#89dceb;">│  │</span>
<span style="color:#89dceb;">│  │</span>  <span style="color:#cba6f7;">⑥ Add & Norm</span>        <span style="color:#89dceb;">│  │</span>
<span style="color:#89dceb;">│  └───────────────────────┘  │</span>
<span style="color:#89dceb;">└─────────────────────────────┘</span>
      <span style="color:#89dceb;">↓</span>
<span style="color:#6c7086;">Output (출력 문장)</span></div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 처음 보면 복잡해 보이지만, 걱정하지 마세요!<br>
앞으로 <b style="color:#FF6B00;">5-3부터 5-8까지</b> 각 구성 요소를 하나씩 차근차근 배울 것입니다.
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
      <th style="padding:10px 14px; text-align:left; font-weight:900;">구분</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">Encoder</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">Decoder</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">역할</td>
      <td style="padding:10px 14px; color:#334155;">입력 문장 이해</td>
      <td style="padding:10px 14px; color:#334155;">출력 문장 생성</td>
    </tr>
    <tr style="background:#fff8f4; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">처리 방향</td>
      <td style="padding:10px 14px; color:#334155;">전체 동시 처리</td>
      <td style="padding:10px 14px; color:#334155;">한 단어씩 순서대로 생성</td>
    </tr>
    <tr style="background:#fff;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">참고 정보</td>
      <td style="padding:10px 14px; color:#334155;">입력 문장 전체</td>
      <td style="padding:10px 14px; color:#334155;">Encoder 결과 + 이미 생성한 단어들</td>
    </tr>
  </tbody>
</table>
</div>

<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
Encoder는 <b style="color:#FF6B00;">"읽고 이해하는 사람"</b>,<br>
Decoder는 <b style="color:#FF6B00;">"이해한 내용을 바탕으로 번역해 쓰는 사람"</b>이라고 생각하세요.
</div>

</div>

</div>