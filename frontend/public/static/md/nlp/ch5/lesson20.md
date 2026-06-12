<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Transformer 처리 과정 예시
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
<b style="color:#1681c4;">"그는 축구를 좋아한다" → "He likes soccer"</b><br>
한 문장이 Transformer 안에서 어떻게 숫자로 바뀌고, 이해되고, 다시 영어 문장으로 생성되는지 처음부터 끝까지 따라갑니다.
</p>

</div>

<br>

<!-- 예시 소개 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🚀 번역 예시: "그는 축구를 좋아한다" → "He likes soccer"
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
지금부터 이 번역이 완성되기까지 Transformer 안에서 일어나는 일을 <b>처음부터 끝까지</b> 따라가 봅니다.<br>
단계마다 데이터가 어떤 형태로 바뀌는지 구체적으로 확인합니다.
</p>

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; text-align:center; font-size:16px; font-weight:900; color:#0f172a; line-height:1.8;">
<span style="color:#1681c4;">그는 축구를 좋아한다</span>
<span style="color:#94a3b8; padding:0 10px;">→</span>
<span style="color:#FF6B00;">He likes soccer</span>
</div>

</div>

<br>

<!-- PHASE 1 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📥 PHASE 1. 입력 준비
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
먼저 한국어 문장을 Transformer가 계산할 수 있는 <b style="color:#1681c4;">숫자 벡터 형태</b>로 바꿉니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">1-1</span>
<span style="font-size:15px; font-weight:900; color:#FF6B00;">토크나이저: 문장 → 토큰 목록</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0;"><span style="color:#6c7086;">입력 문장:</span> <span style="color:#a6e3a1;">"그는 축구를 좋아한다"</span>
             <span style="color:#89dceb;">↓</span>
<span style="color:#6c7086;">토크나이저</span> <span style="color:#cdd6f4;">(단어 단위)</span>
             <span style="color:#89dceb;">↓</span>
<span style="color:#6c7086;">토큰 목록:</span> <span style="color:#f9e2af;">["그는", "축구를", "좋아한다"]</span>
<span style="color:#6c7086;">단어 ID:</span>   <span style="color:#89dceb;">[  215,    1064,      3921   ]</span>   <span style="color:#6c7086;">← 각 단어의 사전 번호</span></pre>
</div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">1-2</span>
<span style="font-size:15px; font-weight:900; color:#1681c4;">임베딩: 단어 ID → 512차원 벡터</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0;"><span style="color:#a6e3a1;">"그는"</span>     <span style="color:#6c7086;">(ID: 215)</span>  → <span style="color:#89dceb;">[0.31, -0.42,  0.18,  0.67, ..., 0.25]</span>  <span style="color:#6c7086;">(512개 숫자)</span>
<span style="color:#a6e3a1;">"축구를"</span>   <span style="color:#6c7086;">(ID: 1064)</span> → <span style="color:#89dceb;">[0.58,  0.22,  0.83, -0.37, ..., 0.49]</span>  <span style="color:#6c7086;">(512개 숫자)</span>
<span style="color:#a6e3a1;">"좋아한다"</span> <span style="color:#6c7086;">(ID: 3921)</span> → <span style="color:#89dceb;">[0.44,  0.71, -0.19,  0.52, ..., 0.13]</span>  <span style="color:#6c7086;">(512개 숫자)</span></pre>

<div style="margin-top:12px; background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
이 시점에서 단어들은 숫자 벡터가 됐지만, <b style="color:#1681c4;">아직 순서 정보가 없습니다.</b>
</div>
</div>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">1-3</span>
<span style="font-size:15px; font-weight:900; color:#FF6B00;">Positional Encoding: 위치 정보 추가</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0;"><span style="color:#a6e3a1;">"그는"</span>     벡터 + <span style="color:#f9e2af;">위치 1 인코딩</span> = <span style="color:#89dceb;">그는_완성벡터</span>
<span style="color:#a6e3a1;">"축구를"</span>   벡터 + <span style="color:#f9e2af;">위치 2 인코딩</span> = <span style="color:#89dceb;">축구를_완성벡터</span>
<span style="color:#a6e3a1;">"좋아한다"</span> 벡터 + <span style="color:#f9e2af;">위치 3 인코딩</span> = <span style="color:#89dceb;">좋아한다_완성벡터</span>

<span style="color:#6c7086;">결과:</span> <span style="color:#cba6f7;">3개 × 512차원 벡터 행렬</span>
      <span style="color:#6c7086;">각 벡터에 "몇 번째 단어인지"가 녹아 있음</span></pre>

<div style="margin-top:12px; background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
이 행렬이 <b style="color:#FF6B00;">Encoder의 첫 레이어</b>로 들어갑니다.
</div>
</div>

</div>
</div>

<br>

<!-- PHASE 2 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 PHASE 2. Encoder 처리
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Encoder에서는 입력 문장의 각 단어가 문장 안의 다른 단어들과 어떤 관계를 가지는지 파악합니다.<br>
아래 과정이 여러 Encoder Layer에서 반복됩니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#FF6B00; color:#fff; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">2-1</span>
<span style="font-size:15px; font-weight:900; color:#FF6B00;">Multi-Head Self-Attention</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0;"><span style="color:#6c7086;">입력:</span> <span style="color:#a6e3a1;">[그는_완성벡터, 축구를_완성벡터, 좋아한다_완성벡터]</span>

<span style="color:#cba6f7;">Head 1</span> <span style="color:#6c7086;">(주어-동사 관계 탐색)</span>:
  <span style="color:#f9e2af;">"그는"</span>     ← <span style="color:#a6e3a1;">"좋아한다"</span>에서 <span style="color:#89dceb;">0.7</span> 참고  <span style="color:#6c7086;">(누가 좋아하는지 파악)</span>
  <span style="color:#f9e2af;">"좋아한다"</span> ← <span style="color:#a6e3a1;">"그는"</span>에서     <span style="color:#89dceb;">0.6</span> 참고  <span style="color:#6c7086;">(행위자 정보 습득)</span>

<span style="color:#cba6f7;">Head 2</span> <span style="color:#6c7086;">(목적어-동사 관계 탐색)</span>:
  <span style="color:#f9e2af;">"축구를"</span>   ← <span style="color:#a6e3a1;">"좋아한다"</span>에서 <span style="color:#89dceb;">0.8</span> 참고  <span style="color:#6c7086;">(좋아하는 대상 역할 강화)</span>
  <span style="color:#f9e2af;">"좋아한다"</span> ← <span style="color:#a6e3a1;">"축구를"</span>에서   <span style="color:#89dceb;">0.7</span> 참고  <span style="color:#6c7086;">(무엇을 좋아하는지 파악)</span>

<span style="color:#6c7086;">... Head 3~8도 각자 다른 관계 탐색</span>

<span style="color:#89dceb;">8개 Head 결과 이어 붙이기 + 선형 변환</span>
<span style="color:#89dceb;">↓</span>
<span style="color:#a6e3a1;">[그는_관계반영, 축구를_관계반영, 좋아한다_관계반영]</span></pre>

<div style="margin-top:12px; background:#fff; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
Self-Attention을 거치면 각 단어는 자기 자신만의 의미가 아니라,
<b style="color:#FF6B00;">문장 전체 안에서의 역할</b>을 반영한 벡터가 됩니다.
</div>
</div>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">2-2</span>
<span style="font-size:15px; font-weight:900; color:#475569;">Add & Norm</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0; text-align:center;"><span style="color:#a6e3a1;">입력 벡터 X</span> + <span style="color:#f9e2af;">Self-Attention 출력</span>
              <span style="color:#89dceb;">↓</span>
           <span style="color:#cba6f7;">LayerNorm</span>
              <span style="color:#89dceb;">↓</span>
<span style="color:#89dceb;">안정화된 벡터</span> <span style="color:#6c7086;">(여전히 512차원 × 3개)</span></pre>

<p style="margin:12px 0 0 0; line-height:1.8; color:#334155; font-size:14px;">
Add & Norm은 원래 입력 정보를 잃지 않도록 더해주고, 값이 너무 커지거나 불안정해지지 않도록 정리해주는 단계입니다.
</p>
</div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#1681c4; color:#fff; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">2-3</span>
<span style="font-size:15px; font-weight:900; color:#1681c4;">FFN</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0;"><span style="color:#6c7086;">각 단어 벡터를 독립적으로 처리:</span>

<span style="color:#a6e3a1;">그는_관계반영</span>     → <span style="color:#cba6f7;">FFN(512→2048→ReLU→512)</span> → <span style="color:#89dceb;">그는_심화</span>
<span style="color:#a6e3a1;">축구를_관계반영</span>   → <span style="color:#cba6f7;">FFN(512→2048→ReLU→512)</span> → <span style="color:#89dceb;">축구를_심화</span>
<span style="color:#a6e3a1;">좋아한다_관계반영</span> → <span style="color:#cba6f7;">FFN(512→2048→ReLU→512)</span> → <span style="color:#89dceb;">좋아한다_심화</span>

<span style="color:#6c7086;">각 단어에 언어 지식이 더해짐</span></pre>

<p style="margin:12px 0 0 0; line-height:1.8; color:#334155; font-size:14px;">
FFN은 각 단어 벡터를 한 번 더 가공해서 더 풍부한 의미 표현으로 만들어줍니다.
</p>
</div>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">2-4</span>
<span style="font-size:15px; font-weight:900; color:#475569;">Add & Norm</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0; text-align:center;"><span style="color:#a6e3a1;">FFN 입력</span> + <span style="color:#f9e2af;">FFN 출력</span>
        <span style="color:#89dceb;">↓</span>
     <span style="color:#cba6f7;">LayerNorm</span>
        <span style="color:#89dceb;">↓</span>
<span style="color:#89dceb;">Encoder Layer 1 최종 출력</span> <span style="color:#6c7086;">(512차원 × 3개)</span></pre>
</div>

<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#FF6B00; color:#fff; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">2-5</span>
<span style="font-size:15px; font-weight:900; color:#FF6B00;">Layer 2~6 반복</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0;"><span style="color:#a6e3a1;">Layer 1 출력</span>
    <span style="color:#89dceb;">↓</span> <span style="color:#6c7086;">Layer 2: 더 깊은 관계 파악</span>
    <span style="color:#89dceb;">↓</span> <span style="color:#6c7086;">Layer 3: 더욱 추상적인 의미</span>
    <span style="color:#89dceb;">↓</span> <span style="color:#6c7086;">Layer 4</span>
    <span style="color:#89dceb;">↓</span> <span style="color:#6c7086;">Layer 5</span>
    <span style="color:#89dceb;">↓</span> <span style="color:#6c7086;">Layer 6: 가장 고차원적인 문맥 표현</span>
    <span style="color:#89dceb;">↓</span>

<span style="color:#f9e2af;">Encoder 최종 출력:</span>
  <span style="color:#a6e3a1;">[벡터_그는, 벡터_축구를, 벡터_좋아한다]</span>
  <span style="color:#6c7086;">각 벡터 = 512차원, 문장 전체 맥락이 담긴 표현</span></pre>

<div style="margin-top:12px; background:#fff; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
Encoder의 최종 출력은 단순한 단어 벡터가 아닙니다.<br>
각 단어가 문장 안에서 어떤 역할을 하는지, 다른 단어들과 어떤 관계를 가지는지까지 담긴 <b style="color:#FF6B00;">문맥 벡터</b>입니다.
</div>
</div>

</div>
</div>

<br>

<!-- PHASE 3 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
✍️ PHASE 3. Decoder 처리 — "He" 생성
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Decoder는 번역 결과를 한 번에 모두 만드는 것이 아니라, <b style="color:#1681c4;">단어를 하나씩 순서대로 생성</b>합니다.<br>
첫 번째로 만들 단어는 <b>"He"</b>입니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#1681c4; color:#fff; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">3-1</span>
<span style="font-size:15px; font-weight:900; color:#1681c4;">시작 신호 입력</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0;"><span style="color:#6c7086;">Decoder 입력:</span> <span style="color:#a6e3a1;">["&lt;시작&gt;"]</span>
<span style="color:#f9e2af;">임베딩 + Positional Encoding</span> → <span style="color:#89dceb;">&lt;시작&gt;_벡터</span> <span style="color:#6c7086;">(위치 1)</span></pre>

<p style="margin:12px 0 0 0; line-height:1.8; color:#334155; font-size:14px;">
Decoder는 아직 아무 단어도 만들지 않았기 때문에 처음에는 <b>&lt;시작&gt;</b> 토큰만 가지고 출발합니다.
</p>
</div>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">3-2</span>
<span style="font-size:15px; font-weight:900; color:#475569;">Masked Self-Attention</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0; text-align:center;"><span style="color:#6c7086;">현재 입력이</span> <span style="color:#a6e3a1;">"&lt;시작&gt;"</span> <span style="color:#6c7086;">하나뿐</span>
<span style="color:#89dceb;">↓</span>
<span style="color:#f9e2af;">자기 자신만 참고</span> <span style="color:#6c7086;">(마스크로 미래 차단)</span>
<span style="color:#89dceb;">↓</span>
<span style="color:#a6e3a1;">&lt;시작&gt;_벡터 그대로 전달</span></pre>

<p style="margin:12px 0 0 0; line-height:1.8; color:#334155; font-size:14px;">
Masked Self-Attention은 Decoder가 아직 생성하지 않은 미래 단어를 미리 보지 못하게 막습니다.
</p>
</div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#1681c4; color:#fff; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">3-3</span>
<span style="font-size:15px; font-weight:900; color:#1681c4;">Encoder-Decoder Attention</span>
</div>

<p style="margin:0 0 12px 0; line-height:1.8; color:#334155; font-size:14px;">
이제 Decoder는 Encoder가 이해한 한국어 문장을 참고합니다.
</p>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0;"><span style="color:#cba6f7;">Q</span> = <span style="color:#a6e3a1;">Decoder의 &lt;시작&gt;_벡터</span>  <span style="color:#6c7086;">("첫 단어를 찾고 있어")</span>
<span style="color:#cba6f7;">K</span> = <span style="color:#f9e2af;">[K_그는, K_축구를, K_좋아한다]</span>
<span style="color:#cba6f7;">V</span> = <span style="color:#f9e2af;">[V_그는, V_축구를, V_좋아한다]</span>

<span style="color:#6c7086;">Attention 계산:</span>
  <span style="color:#a6e3a1;">"그는"</span>     → <span style="color:#89dceb;">0.78</span>  <span style="color:#6c7086;">← 첫 단어(주어)와 가장 관련 있음!</span>
  <span style="color:#a6e3a1;">"축구를"</span>   → <span style="color:#89dceb;">0.12</span>
  <span style="color:#a6e3a1;">"좋아한다"</span> → <span style="color:#89dceb;">0.10</span>

<span style="color:#6c7086;">가중 합산:</span>
<span style="color:#f9e2af;">V_그는 × 0.78 + V_축구를 × 0.12 + V_좋아한다 × 0.10</span>

→ <span style="color:#89dceb;">"주어인 그는"의 정보가 많이 담긴 벡터</span></pre>

<div style="margin-top:12px; background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
첫 영어 단어를 만들 때는 주어 정보가 중요하기 때문에 Decoder는 <b style="color:#1681c4;">"그는"</b>에 가장 높은 Attention을 둡니다.
</div>
</div>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">3-4</span>
<span style="font-size:15px; font-weight:900; color:#475569;">FFN + Add & Norm</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0; text-align:center;"><span style="color:#a6e3a1;">Encoder-Decoder Attention 결과</span>
    <span style="color:#89dceb;">↓</span> <span style="color:#cba6f7;">Add & Norm</span>
    <span style="color:#89dceb;">↓</span> <span style="color:#f9e2af;">FFN (512→2048→ReLU→512)</span>
    <span style="color:#89dceb;">↓</span> <span style="color:#cba6f7;">Add & Norm</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#89dceb;">Decoder 최종 출력 벡터</span> <span style="color:#6c7086;">(512차원)</span></pre>
</div>

<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#FF6B00; color:#fff; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">3-5</span>
<span style="font-size:15px; font-weight:900; color:#FF6B00;">Linear + Softmax → 단어 선택</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0;"><span style="color:#a6e3a1;">Decoder 출력 벡터</span> <span style="color:#6c7086;">(512차원)</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#f9e2af;">Linear 변환</span> <span style="color:#6c7086;">(512 → 30,000차원, 단어 사전 크기)</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#cba6f7;">Softmax</span> <span style="color:#6c7086;">(확률 분포로 변환)</span>
    <span style="color:#89dceb;">↓</span>

<span style="color:#6c7086;">상위 5개 확률:</span>
  <span style="color:#a6e3a1;">"He"</span>   → <span style="color:#89dceb;">0.814</span>  <span style="color:#6c7086;">← 가장 높음!</span>
  <span style="color:#a6e3a1;">"She"</span>  → <span style="color:#89dceb;">0.062</span>
  <span style="color:#a6e3a1;">"They"</span> → <span style="color:#89dceb;">0.041</span>
  <span style="color:#a6e3a1;">"I"</span>    → <span style="color:#89dceb;">0.027</span>
  <span style="color:#6c7086;">...</span>

→ <span style="color:#f38ba8;">"He" 선택 및 출력</span></pre>

<div style="margin-top:12px; background:#fff; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
결과적으로 Decoder는 첫 번째 단어로 <b style="color:#FF6B00;">"He"</b>를 선택합니다.
</div>
</div>

</div>
</div>

<br>

<!-- PHASE 4 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
✍️ PHASE 4. Decoder 처리 — "likes", "soccer" 순차 생성
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
첫 단어 <b>"He"</b>가 만들어졌으므로, 이제 Decoder는 이전에 만든 단어를 참고하면서 다음 단어를 생성합니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#1681c4; color:#fff; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">4-1</span>
<span style="font-size:15px; font-weight:900; color:#1681c4;">"likes" 생성</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0;"><span style="color:#6c7086;">Decoder 입력:</span> <span style="color:#a6e3a1;">["&lt;시작&gt;", "He"]</span>

<span style="color:#cba6f7;">Masked Self-Attention:</span>
  <span style="color:#a6e3a1;">"He"</span>가 <span style="color:#f9e2af;">"&lt;시작&gt;"</span>을 참고
  <span style="color:#6c7086;">아직 미래 단어는 보지 못함</span>

<span style="color:#cba6f7;">Encoder-Decoder Attention:</span>
  <span style="color:#a6e3a1;">"좋아한다"</span> → <span style="color:#89dceb;">0.69</span>  <span style="color:#6c7086;">← 동사와 가장 관련 있음!</span>
  <span style="color:#a6e3a1;">"그는"</span>     → <span style="color:#89dceb;">0.19</span>
  <span style="color:#a6e3a1;">"축구를"</span>   → <span style="color:#89dceb;">0.12</span>

<span style="color:#cba6f7;">Linear + Softmax 상위 결과:</span>
  <span style="color:#a6e3a1;">"likes"</span> → <span style="color:#89dceb;">0.756</span>  <span style="color:#6c7086;">← 선택!</span>
  <span style="color:#a6e3a1;">"like"</span>  → <span style="color:#89dceb;">0.081</span>
  <span style="color:#a6e3a1;">"plays"</span> → <span style="color:#89dceb;">0.046</span></pre>

<div style="margin-top:12px; background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
Transformer는 단순히 <b>"좋아한다" = like</b>만 고르는 것이 아닙니다.<br>
앞에서 이미 <b>"He"</b>가 나왔기 때문에 영어 문법에 맞게 <b style="color:#1681c4;">"likes"</b>를 선택합니다.
</div>

<div style="margin-top:12px; display:grid; grid-template-columns:1fr 1fr; gap:10px;">
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#FF6B00; font-weight:900; text-align:center;">
He like soccer ❌
</div>
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:14px; color:#1681c4; font-weight:900; text-align:center;">
He likes soccer ✅
</div>
</div>
</div>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">4-2</span>
<span style="font-size:15px; font-weight:900; color:#475569;">"soccer" 생성</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0;"><span style="color:#6c7086;">Decoder 입력:</span> <span style="color:#a6e3a1;">["&lt;시작&gt;", "He", "likes"]</span>

<span style="color:#cba6f7;">Masked Self-Attention:</span>
  <span style="color:#a6e3a1;">"likes"</span>가 <span style="color:#f9e2af;">"&lt;시작&gt;", "He"</span>를 모두 참고

<span style="color:#cba6f7;">Encoder-Decoder Attention:</span>
  <span style="color:#a6e3a1;">"축구를"</span>   → <span style="color:#89dceb;">0.81</span>  <span style="color:#6c7086;">← 목적어와 가장 관련 있음!</span>
  <span style="color:#a6e3a1;">"좋아한다"</span> → <span style="color:#89dceb;">0.11</span>
  <span style="color:#a6e3a1;">"그는"</span>     → <span style="color:#89dceb;">0.08</span>

<span style="color:#cba6f7;">Linear + Softmax 상위 결과:</span>
  <span style="color:#a6e3a1;">"soccer"</span>   → <span style="color:#89dceb;">0.724</span>  <span style="color:#6c7086;">← 선택!</span>
  <span style="color:#a6e3a1;">"football"</span> → <span style="color:#89dceb;">0.139</span>
  <span style="color:#a6e3a1;">"sports"</span>   → <span style="color:#89dceb;">0.064</span></pre>

<p style="margin:12px 0 0 0; line-height:1.8; color:#334155; font-size:14px;">
이번에는 영어 문장에서 목적어가 올 차례이므로 Decoder는 Encoder 출력 중 <b style="color:#1681c4;">"축구를"</b>에 가장 크게 집중합니다.
</p>
</div>

<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#FF6B00; color:#fff; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">4-3</span>
<span style="font-size:15px; font-weight:900; color:#FF6B00;">종료 신호 생성</span>
</div>

<pre style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre; margin:0; text-align:center;"><span style="color:#6c7086;">Decoder 입력:</span> <span style="color:#a6e3a1;">["&lt;시작&gt;", "He", "likes", "soccer"]</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#f9e2af;">"&lt;종료&gt;" 토큰의 확률이 가장 높아짐</span>
    <span style="color:#89dceb;">↓</span>
<span style="color:#f38ba8;">번역 완료!</span></pre>

<p style="margin:12px 0 0 0; line-height:1.8; color:#334155; font-size:14px;">
Decoder는 더 이상 생성할 단어가 없다고 판단하면 <b>&lt;종료&gt;</b> 토큰을 출력하고 번역을 마칩니다.
</p>
</div>

</div>
</div>

<br>

<!-- 최종 결과 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🏁 최종 결과
</h2>

<pre style="background:#0f172a; border-radius:14px; padding:16px 18px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre; margin:14px 0 0 0;"><span style="color:#6c7086;">입력  (한국어):</span> <span style="color:#a6e3a1;">"그는    축구를    좋아한다"</span>
                  <span style="color:#89dceb;">↓        ↓         ↓</span>
<span style="color:#6c7086;">Encoder Attn:</span>  <span style="color:#f9e2af;">"그는"</span>     → <span style="color:#89dceb;">"He"</span>      <span style="color:#6c7086;">(주어)</span>
               <span style="color:#f9e2af;">"좋아한다"</span> → <span style="color:#89dceb;">"likes"</span>   <span style="color:#6c7086;">(동사)</span>
               <span style="color:#f9e2af;">"축구를"</span>   → <span style="color:#89dceb;">"soccer"</span>  <span style="color:#6c7086;">(목적어)</span>
                  <span style="color:#89dceb;">↓        ↓         ↓</span>
<span style="color:#6c7086;">출력  (영어):</span>  <span style="color:#f38ba8;">"He      likes     soccer"</span></pre>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:16px;">

<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
<div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:10px;">한국어 어순</div>
<div style="background:#fff; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#334155; line-height:2;">
그는 / 축구를 / 좋아한다<br>
<span style="color:#FF6B00; font-weight:900;">주어 / 목적어 / 동사</span>
</div>
</div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
<div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">영어 어순</div>
<div style="background:#fff; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#334155; line-height:2;">
He / likes / soccer<br>
<span style="color:#1681c4; font-weight:900;">주어 / 동사 / 목적어</span>
</div>
</div>

</div>

<div style="margin-top:14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡 핵심</span><br>
Transformer는 Encoder-Decoder Attention을 통해 입력 문장의 단어들을 참고하면서, 영어 어순에 맞게 단어를 <b style="color:#1681c4;">자동으로 재정렬</b>합니다.
</div>

</div>

<br>

<!-- 핵심 정리 표 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="font-size: 15px; font-weight: 900; margin-bottom: 12px;">
<span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리
</div>

<div style="overflow-x:auto;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
<thead>
<tr style="background:#0f172a; color:#c3e88d;">
<th style="padding:10px 14px; text-align:left; font-weight:900;">단계</th>
<th style="padding:10px 14px; text-align:left; font-weight:900;">처리 내용</th>
<th style="padding:10px 14px; text-align:left; font-weight:900;">데이터 형태</th>
</tr>
</thead>
<tbody>
<tr style="background:#fff; border-bottom:1px solid #ffd0b0;">
<td style="padding:10px 14px; font-weight:900; color:#FF6B00;">토크나이저</td>
<td style="padding:10px 14px; color:#334155;">문장 → 단어 ID</td>
<td style="padding:10px 14px; color:#475569;">정수 리스트</td>
</tr>
<tr style="background:#fff8f3; border-bottom:1px solid #ffd0b0;">
<td style="padding:10px 14px; font-weight:900; color:#FF6B00;">임베딩</td>
<td style="padding:10px 14px; color:#334155;">단어 ID → 벡터</td>
<td style="padding:10px 14px; color:#475569;">N × 512 행렬</td>
</tr>
<tr style="background:#fff; border-bottom:1px solid #ffd0b0;">
<td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Positional Encoding</td>
<td style="padding:10px 14px; color:#334155;">위치 정보 추가</td>
<td style="padding:10px 14px; color:#475569;">N × 512 행렬</td>
</tr>
<tr style="background:#fff8f3; border-bottom:1px solid #ffd0b0;">
<td style="padding:10px 14px; font-weight:900; color:#1681c4;">Encoder</td>
<td style="padding:10px 14px; color:#334155;">문장 전체 이해</td>
<td style="padding:10px 14px; color:#475569;">N × 512 행렬</td>
</tr>
<tr style="background:#fff; border-bottom:1px solid #ffd0b0;">
<td style="padding:10px 14px; font-weight:900; color:#1681c4;">Decoder</td>
<td style="padding:10px 14px; color:#334155;">단어 하나씩 생성</td>
<td style="padding:10px 14px; color:#475569;">1 × 512 벡터</td>
</tr>
<tr style="background:#fff8f3;">
<td style="padding:10px 14px; font-weight:900; color:#1681c4;">Linear + Softmax</td>
<td style="padding:10px 14px; color:#334155;">단어 확률 계산</td>
<td style="padding:10px 14px; color:#475569;">30,000차원 확률 분포</td>
</tr>
</tbody>
</table>
</div>

<div style="margin-top:12px; background-color: #ffffff; border-left:4px solid #FF6B00; padding: 11px 14px; border-radius: 0 10px 10px 0; font-size: 14px; color: #334155; line-height: 1.8;">
Transformer는 <b style="color:#FF6B00;">입력 문장을 문맥 벡터로 이해</b>하고,
Decoder가 그 정보를 참고해 <b style="color:#FF6B00;">출력 문장을 한 단어씩 생성</b>합니다.
</div>

</div>

</div>