<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
입력을 어떻게 벡터로 만드나요?
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
BERT의 입력 벡터는 세 가지 임베딩의 합입니다.<br>
<b style="color:#1681c4;">토큰 임베딩 + 세그먼트 임베딩 + 포지셔널 임베딩</b>이 어떻게 작동하는지 살펴봅니다.
</p>

</div>

<br>

<!-- 순서 문제 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
❓ 트랜스포머는 "순서"를 어떻게 알까요?
</h2>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 18px;">

  <div style="background:#f0fdf4; border:2px solid #86efac; border-radius:14px; padding:18px 20px;">
    <div style="font-size:14px; font-weight:900; color:#16a34a; margin-bottom:8px;">✅ RNN — 순서를 자연스럽게 반영</div>
    <div style="font-size:13px; color:#334155; line-height:1.8;">
      단어를 <b>왼쪽에서 오른쪽으로 순서대로</b> 처리하기 때문에 위치 정보가 자동 반영됩니다.
    </div>
  </div>

  <div style="background:#fff1f2; border:2px solid #fca5a5; border-radius:14px; padding:18px 20px;">
    <div style="font-size:14px; font-weight:900; color:#dc2626; margin-bottom:8px;">⚠️ Transformer — 순서를 모름</div>
    <div style="font-size:13px; color:#334155; line-height:1.8;">
      <b>모든 단어를 동시에</b> 보기 때문에, 아무 처리 없이 넣으면 단어의 위치를 모릅니다.
    </div>
  </div>

</div>

<div style="background-color: #1e1e2e; border-radius: 14px; padding: 16px 20px; font-family:'JetBrains Mono','Consolas',monospace; font-size: 13px; color: #f38ba8; line-height: 2.2; overflow-x: auto; white-space: pre; margin-bottom: 14px;">
<span style="color:#6c7086;">Self-Attention 입장에서 이 두 문장이 같아 보일 수 있습니다:</span>
<span style="color:#f9e2af;">"나는 밥을 먹었다"</span>  <span style="color:#6c7086;">↔</span>  <span style="color:#f9e2af;">"밥을 나는 먹었다"</span></div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 이 문제를 해결하기 위해 <b style="color:#FF6B00;">포지셔널 인코딩(Positional Encoding)</b>이 필요합니다.
</div>

</div>

<br>

<!-- 포지셔널 인코딩 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📍 포지셔널 인코딩(Positional Encoding)
</h2>

<!-- 비유 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px; margin-bottom:18px;">
  <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:12px;">🎫 비유: 카페 번호표</div>
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-bottom: 12px;">
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:10px; text-align:center;">
      <div style="font-size:20px; font-weight:900; color:#FF6B00;">1번</div>
      <div style="font-size:13px; color:#334155; margin-top:4px;">나는</div>
      <div style="font-size:11px; color:#94a3b8; margin-top:2px;">(1번째 단어)</div>
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:10px; text-align:center;">
      <div style="font-size:20px; font-weight:900; color:#FF6B00;">2번</div>
      <div style="font-size:13px; color:#334155; margin-top:4px;">오늘</div>
      <div style="font-size:11px; color:#94a3b8; margin-top:2px;">(2번째 단어)</div>
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:10px; text-align:center;">
      <div style="font-size:20px; font-weight:900; color:#FF6B00;">3번</div>
      <div style="font-size:13px; color:#334155; margin-top:4px;">카페</div>
      <div style="font-size:11px; color:#94a3b8; margin-top:2px;">(3번째 단어)</div>
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:10px; text-align:center;">
      <div style="font-size:20px; font-weight:900; color:#FF6B00;">4번</div>
      <div style="font-size:13px; color:#334155; margin-top:4px;">에서</div>
      <div style="font-size:11px; color:#94a3b8; margin-top:2px;">(4번째 단어)</div>
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:10px; text-align:center;">
      <div style="font-size:20px; font-weight:900; color:#FF6B00;">5번</div>
      <div style="font-size:13px; color:#334155; margin-top:4px;">커피를</div>
      <div style="font-size:11px; color:#94a3b8; margin-top:2px;">(5번째 단어)</div>
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:10px; padding:10px; text-align:center;">
      <div style="font-size:20px; font-weight:900; color:#FF6B00;">6번</div>
      <div style="font-size:13px; color:#334155; margin-top:4px;">마셨다</div>
      <div style="font-size:11px; color:#94a3b8; margin-top:2px;">(6번째 단어)</div>
    </div>
  </div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center; margin-bottom: 14px;">
최종 입력 벡터 = 단어 임베딩 벡터 + 위치 임베딩 벡터
</div>

<div style="font-size: 14px; color: #334155; line-height: 1.8;">
이렇게 하면 Self-Attention이 단어의 <b style="color:#1681c4;">의미와 위치를 동시에</b> 고려할 수 있습니다.
</div>

</div>

<br>

<!-- 3가지 임베딩 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧩 BERT의 입력 임베딩 = 3가지의 합
</h2>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center; margin-bottom: 18px;">
BERT 입력 벡터 = ① 토큰 임베딩 + ② 세그먼트 임베딩 + ③ 포지셔널 임베딩
</div>

<div style="display: grid; gap: 12px; margin-top: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:900;">①</div>
    <div style="flex:1;">
      <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:6px;">토큰 임베딩</div>
      <div style="font-size:14px; color:#334155; line-height:1.7; margin-bottom:8px;">단어 자체의 의미 벡터</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:9px 14px; font-family:Consolas,monospace; font-size:13px; color:#a6e3a1;">
        "카페" → [0.3, -0.1, 0.9, ...]
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:900;">②</div>
    <div style="flex:1;">
      <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:6px;">세그먼트 임베딩</div>
      <div style="font-size:14px; color:#334155; line-height:1.7; margin-bottom:8px;">이 단어가 문장 A인지 B인지 구분</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:9px 14px; font-family:Consolas,monospace; font-size:13px; color:#89dceb;">
        문장A → 0 &nbsp;&nbsp;&nbsp; 문장B → 1
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:900;">③</div>
    <div style="flex:1;">
      <div style="font-size:15px; font-weight:900; color:#0f172a; margin-bottom:6px;">포지셔널 임베딩</div>
      <div style="font-size:14px; color:#334155; line-height:1.7; margin-bottom:8px;">이 단어가 몇 번째 위치인지</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:9px 14px; font-family:Consolas,monospace; font-size:13px; color:#c3e88d;">
        3번째 단어 → 위치 벡터
      </div>
    </div>
  </div>

</div>

<!-- 세그먼트 임베딩 예시 -->
<div style="margin-top: 18px;">
  <div style="font-size: 14px; font-weight: 900; color: #0f172a; margin-bottom: 10px;">📌 세그먼트 임베딩이 필요한 이유</div>
  <p style="font-size: 14px; color: #334155; line-height: 1.8; margin-bottom: 12px;">
  BERT는 두 문장을 동시에 입력받는 경우가 많습니다. (예: 질의응답에서 질문 + 지문을 함께 입력)
  </p>
  <div style="background-color: #1e1e2e; border-radius: 12px; padding: 16px 18px; font-family:'JetBrains Mono','Consolas',monospace; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">입력:      </span><span style="color:#cdd6f4;">[CLS] 오늘 날씨 어때? [SEP] 맑고 화창합니다. [SEP]</span>
<span style="color:#6c7086;">세그먼트:  </span><span style="color:#89dceb;">  A    A   A    A    A  </span><span style="color:#f9e2af;">  B    B    B       B</span></div>
  <div style="margin-top:10px; background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:13px; color:#334155; line-height:1.7;">
    <span style="color:#FF6B00; font-weight:900;">💡</span> 세그먼트 임베딩 덕분에 BERT는 <b style="color:#FF6B00;">"이 단어는 첫 번째 문장에서 온 것"</b>이라는 걸 알 수 있습니다.
  </div>
</div>

</div>

<br>

<!-- 전체 흐름 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🗺️ 입력부터 출력까지 전체 흐름
</h2>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">BERT 입력 → 출력 흐름</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">입력 문장:</span>
<span style="color:#a6e3a1;">[CLS] 나는 카페 에서 커피를 마셨다 [SEP]</span>

  <span style="color:#6c7086;">↓ (① + ② + ③ 임베딩 합산)</span>

<span style="color:#6c7086;">입력 벡터:</span>
<span style="color:#89dceb;"> v₀    v₁    v₂   v₃    v₄     v₅    v₆</span>
<span style="color:#cdd6f4;">[CLS] [나는] [카페] [에서] [커피를] [마셨다] [SEP]</span>

  <span style="color:#6c7086;">↓ Encoder Layer 1 (Self-Attention + FFN)</span>
  <span style="color:#6c7086;">↓ Encoder Layer 2</span>
  <span style="color:#6c7086;">↓ ...</span>
  <span style="color:#6c7086;">↓ Encoder Layer 12</span>

<span style="color:#6c7086;">출력 벡터:</span>
<span style="color:#a6e3a1;"> h₀    h₁    h₂   h₃    h₄      h₅    h₆</span>
<span style="color:#a6e3a1;">[CLS] [나는] [카페] [에서] [커피를] [마셨다] [SEP]</span>
<span style="color:#6c7086;">→ 각 벡터에 단어 의미 + 문장 전체 문맥이 담겨 있습니다.</span></div>
</div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8; margin-top:14px;">
<span style="color:#1681c4; font-weight:900;">📌</span> 입력 벡터(v)와 출력 벡터(h)는 <b style="color:#1681c4;">같은 위치, 같은 개수</b>이지만,<br>
출력 벡터는 12층의 Self-Attention을 거쳐 <b style="color:#1681c4;">문맥이 풍부하게 반영</b>된 상태입니다.
</div>

</div>

<br>

<!-- BERT-Base 구조 요약 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 BERT-Base 구조 요약
</h2>

<div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-top: 16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:16px 12px; text-align:center;">
    <div style="font-size:11px; font-weight:900; color:#1681c4; margin-bottom:6px;">인코더 레이어</div>
    <div style="font-size:24px; font-weight:900; color:#0f172a;">12</div>
    <div style="font-size:11px; color:#64748b; margin-top:4px;">층</div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:16px 12px; text-align:center;">
    <div style="font-size:11px; font-weight:900; color:#1681c4; margin-bottom:6px;">헤드 수</div>
    <div style="font-size:24px; font-weight:900; color:#0f172a;">12</div>
    <div style="font-size:11px; color:#64748b; margin-top:4px;">Multi-Head</div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:16px 12px; text-align:center;">
    <div style="font-size:11px; font-weight:900; color:#FF6B00; margin-bottom:6px;">벡터 차원</div>
    <div style="font-size:24px; font-weight:900; color:#0f172a;">768</div>
    <div style="font-size:11px; color:#64748b; margin-top:4px;">차원</div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:16px 12px; text-align:center;">
    <div style="font-size:11px; font-weight:900; color:#FF6B00; margin-bottom:6px;">FFN 내부</div>
    <div style="font-size:24px; font-weight:900; color:#0f172a;">3072</div>
    <div style="font-size:11px; color:#64748b; margin-top:4px;">차원</div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:16px 12px; text-align:center;">
    <div style="font-size:11px; font-weight:900; color:#64748b; margin-bottom:6px;">파라미터</div>
    <div style="font-size:20px; font-weight:900; color:#0f172a;">1.1억</div>
    <div style="font-size:11px; color:#64748b; margin-top:4px;">개</div>
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
    Self-Attention은 순서를 모르기 때문에 <b style="color:#FF6B00;">포지셔널 인코딩</b>으로 위치 정보를 추가합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    BERT의 입력 벡터는 <b style="color:#FF6B00;">① 토큰 임베딩 + ② 세그먼트 임베딩 + ③ 포지셔널 임베딩</b>의 합입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이 입력이 12층의 인코더를 통과하면 <b style="color:#FF6B00;">문맥이 담긴 벡터</b>로 변환됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    출력 벡터의 수와 위치는 입력과 같지만, 내용은 <b style="color:#FF6B00;">문장 전체의 문맥을 반영</b>합니다.
  </div>
</div>

</div>

</div>