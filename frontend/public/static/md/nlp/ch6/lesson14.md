<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
BERT의 입력 구조 — 3가지 임베딩이 합쳐지는 방법
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
각 토큰은 세 가지 임베딩의 합으로 변환됩니다.<br>
<b style="color:#1681c4;">토큰 · 세그먼트 · 포지셔널 임베딩</b>이 왜 필요하고 어떻게 만들어지는지 알아봅니다.
</p>

</div>

<br>

<!-- 3가지 재료 개요 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧩 BERT 입력 벡터의 3가지 재료
</h2>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center; margin: 14px 0;">
BERT 입력 벡터 = ① 토큰 임베딩 + ② 세그먼트 임베딩 + ③ 포지셔널 임베딩
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-top: 16px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:6px;">① 토큰 임베딩</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">"이 단어가<br>어떤 단어인가?"</div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:6px;">② 세그먼트 임베딩</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">"몇 번째<br>문장에 속하나?"</div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:13px; font-weight:900; color:#64748b; margin-bottom:6px;">③ 포지셔널 임베딩</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">"문장에서<br>몇 번째 위치인가?"</div>
  </div>

</div>

</div>

<br>

<!-- ① 토큰 임베딩 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔤 ① 토큰 임베딩 (Token Embedding)
</h2>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 17px; border-radius: 12px; font-size: 14px; font-weight: 900; color: #FF6B00; text-align: center; margin-bottom: 16px;">
"이 단어가 어떤 단어인가?" — 각 토큰 ID를 768차원 실수 벡터로 변환
</div>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">토큰 ID → 임베딩 테이블 조회 → 768차원 벡터</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#f38ba8;">[CLS]</span>  <span style="color:#6c7086;">→</span>  <span style="color:#89dceb;">[0.1, -0.3,  0.8,  0.2, ...]</span>  <span style="color:#6c7086;">(768개 숫자)</span>
<span style="color:#a6e3a1;">나는</span>   <span style="color:#6c7086;">→</span>  <span style="color:#89dceb;">[0.5,  0.2, -0.1,  0.9, ...]</span>  <span style="color:#6c7086;">(768개 숫자)</span>
<span style="color:#a6e3a1;">카페</span>   <span style="color:#6c7086;">→</span>  <span style="color:#89dceb;">[0.3,  0.7,  0.4, -0.5, ...]</span>  <span style="color:#6c7086;">(768개 숫자)</span></div>
</div>

<div style="background:#fff3eb; border:2px solid #ffd0b0; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#FF6B00; font-weight:900;">💡</span> 처음에는 랜덤한 값이지만, 수십억 문장을 학습하면서 <b style="color:#FF6B00;">비슷한 의미의 단어들은 비슷한 벡터</b>를 갖게 됩니다.
</div>

</div>

<br>

<!-- ② 세그먼트 임베딩 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🏷️ ② 세그먼트 임베딩 (Segment Embedding)
</h2>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 17px; border-radius: 12px; font-size: 14px; font-weight: 900; color: #1681c4; text-align: center; margin-bottom: 16px;">
"이 토큰은 몇 번째 문장에 속하는가?" — 문장 A인지 B인지 구분
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
BERT는 두 문장을 동시에 입력받는 경우가 많습니다. (NSP 학습, 질의응답 등)
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">질의응답 입력 예시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">질문: "카페는 어디에 있나요?"</span>
<span style="color:#6c7086;">지문: "카페는 역 앞에 있습니다."</span>

<span style="color:#cdd6f4;">[CLS] 카페는 어디에 있나요? [SEP] 카페는 역 앞에 있습니다. [SEP]</span>
<span style="color:#89dceb;">  A    A    A    A    A     A     B    B   B   B  B    B      B</span></div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 14px;">
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:13px 16px; text-align:center;">
    <div style="font-size:22px; font-weight:900; color:#FF6B00; margin-bottom:6px;">A</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">문장 A 토큰<br>→ <b>세그먼트 A 벡터</b></div>
  </div>
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:13px 16px; text-align:center;">
    <div style="font-size:22px; font-weight:900; color:#1681c4; margin-bottom:6px;">B</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">문장 B 토큰<br>→ <b>세그먼트 B 벡터</b></div>
  </div>
</div>

</div>

<br>

<!-- ③ 포지셔널 임베딩 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📍 ③ 포지셔널 임베딩 (Positional Embedding)
</h2>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 17px; border-radius: 12px; font-size: 14px; font-weight: 900; color: #64748b; text-align: center; margin-bottom: 16px;">
"이 토큰은 문장에서 몇 번째 위치인가?" — 단어 순서 정보 부여
</div>

<div style="background:#fff1f2; border:2px solid #fca5a5; border-radius:12px; padding:14px 16px; margin-bottom:14px;">
  <div style="font-size:13px; font-weight:900; color:#dc2626; margin-bottom:8px;">⚠️ 위치 정보 없을 때의 문제</div>
  <div style="background:#1e1e2e; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; color:#f38ba8; line-height:2.0; overflow-x:auto; white-space:pre;">
<span style="color:#cdd6f4;">"나는 철수를 이겼다"</span>  <span style="color:#f38ba8;">=?</span>  <span style="color:#cdd6f4;">"철수를 나는 이겼다"</span>
<span style="color:#6c7086;">→ 의미가 달라지지만, 위치 정보 없이는 구분 불가!</span></div>
</div>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">각 위치별 고유 벡터 부여</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">위치 0 </span><span style="color:#f38ba8;">([CLS])</span>  <span style="color:#6c7086;">→</span> <span style="color:#89dceb;">[ 0.0,  1.0,  0.0,  1.0, ...]</span>
<span style="color:#6c7086;">위치 1 </span><span style="color:#a6e3a1;">(나는)</span>   <span style="color:#6c7086;">→</span> <span style="color:#89dceb;">[ 0.84, 0.54, 0.91, ...]</span>
<span style="color:#6c7086;">위치 2 </span><span style="color:#a6e3a1;">(카페)</span>   <span style="color:#6c7086;">→</span> <span style="color:#89dceb;">[ 0.91,-0.41, 0.14, ...]</span>
<span style="color:#6c7086;">위치 3 </span><span style="color:#a6e3a1;">(에서)</span>   <span style="color:#6c7086;">→</span> <span style="color:#89dceb;">[ 0.14,-0.99, ...]</span></div>
</div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#1681c4; font-weight:900;">💡</span> BERT는 원래 트랜스포머처럼 수식으로 계산하는 방식이 아니라 <b style="color:#1681c4;">학습을 통해 위치 벡터를 자동으로 만들어냅니다.</b>
</div>

</div>

<br>

<!-- 3가지 더하기 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
➕ 3가지가 더해지는 방법
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
세 벡터를 <b>원소별로 더하면</b> 하나의 768차원 벡터가 완성됩니다. 예시: 위치 2의 토큰 "카페"
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">"카페" 토큰 최종 입력 벡터 계산</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#f9e2af;">토큰 임베딩      </span><span style="color:#89dceb;">[ 0.3,  0.7,  0.4, -0.5, ...]</span>
<span style="color:#cba6f7;">세그먼트 임베딩  </span><span style="color:#89dceb;">[ 0.1, -0.1,  0.1, -0.1, ...]</span>  <span style="color:#6c7086;">(문장 A)</span>
<span style="color:#a6e3a1;">포지셔널 임베딩  </span><span style="color:#89dceb;">[ 0.91,-0.41, 0.14, 0.99, ...]</span>  <span style="color:#6c7086;">(위치 2)</span>
<span style="color:#6c7086;">──────────────────────────────────────────</span>
<span style="color:#cdd6f4; font-weight:900;">최종 입력 벡터   </span><span style="color:#a6e3a1; font-weight:900;">[ 1.31, 0.19,  0.64, 0.39, ...]</span>  <span style="color:#6c7086;">(768차원)</span></div>
</div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#1681c4; font-weight:900;">💡</span> <b style="color:#1681c4;">"카페라는 단어가 / 첫 번째 문장에서 / 2번째 위치에"</b> 있다는 정보가 한 벡터에 담깁니다.
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
    <b style="color:#FF6B00;">토큰 임베딩:</b> 단어 자체의 의미 → "카페란 무엇인가"
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">세그먼트 임베딩:</b> 어느 문장 소속인지 → "첫 번째 문장의 단어인가, 두 번째인가"
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">포지셔널 임베딩:</b> 문장 내 위치 → "몇 번째 단어인가"
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    세 벡터를 <b style="color:#FF6B00;">원소별로 더해</b> 하나의 768차원 입력 벡터를 만들고, 이것이 인코더의 입력이 됩니다.
  </div>
</div>

</div>

</div>