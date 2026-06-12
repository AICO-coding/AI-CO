<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Encoder-Decoder Attention
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Decoder가 매 단어를 생성할 때 Encoder의 결과를
<b style="color:#1681c4;">어떻게 참고하는지</b> 알아봅니다.
</p>

</div>

<br>

<!-- Decoder 안의 두 번째 Attention -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔗 Decoder 레이어 안의 두 번째 Attention
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
Decoder 레이어 안에는 Attention이 두 개 있습니다.
</p>

<div style="display: grid; gap: 8px; margin-bottom: 16px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#0f172a; color:#f38ba8; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">①</div>
    <div style="font-size:14px; color:#334155;"><b>Masked Self-Attention</b> — 지금까지 생성한 출력 단어들끼리의 관계</div>
  </div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:12px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">②</div>
    <div style="font-size:14px; color:#334155;"><b style="color:#FF6B00;">Encoder-Decoder Attention</b> — ★ 지금 배우는 부분: Encoder 결과 참고</div>
  </div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> Encoder-Decoder Attention은 <b style="color:#1681c4;">Encoder의 출력</b>과 <b style="color:#1681c4;">Decoder의 현재 상태</b>를 연결하는 다리입니다.
</div>

</div>

<br>

<!-- 왜 이 다리가 필요한가 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🌉 왜 이 다리가 필요한가?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
Decoder가 <b>"ate"</b>를 생성하는 시점을 상상해보세요.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 14px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 14px;">
    <div style="font-size:12px; font-weight:900; color:#94a3b8; margin-bottom:6px;">Decoder가 알고 있는 것 ①</div>
    <div style="font-family:Consolas,monospace; font-size:13px; color:#a6e3a1; background:#0f172a; padding:8px 10px; border-radius:8px; text-align:center;">지금까지 생성한 단어: "I"</div>
  </div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:12px 14px;">
    <div style="font-size:12px; font-weight:900; color:#94a3b8; margin-bottom:6px;">Decoder가 알고 있는 것 ②</div>
    <div style="font-family:Consolas,monospace; font-size:13px; color:#cba6f7; background:#0f172a; padding:8px 10px; border-radius:8px; text-align:center;">[벡터_나는, 벡터_밥을, 벡터_먹었다]</div>
  </div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> "ate"를 생성하려면 원문에서 <b style="color:#FF6B00;">"먹었다"</b>에 해당하는 정보를 가져와야 합니다.<br>
이 <b style="color:#FF6B00;">"정보 가져오기"</b>를 담당하는 것이 Encoder-Decoder Attention입니다.
</div>

</div>

<br>

<!-- Q, K, V 출처 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔑 Q, K, V의 출처가 달라진다
</h2>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#94a3b8; margin-bottom:10px; text-align:center;">Self-Attention</div>
    <div style="display:grid; gap:5px;">
      <div style="background:#0f172a; border-radius:7px; padding:7px 12px; font-family:Consolas,monospace; font-size:12px; color:#a6e3a1;">Q = 이 문장의 단어들로부터</div>
      <div style="background:#0f172a; border-radius:7px; padding:7px 12px; font-family:Consolas,monospace; font-size:12px; color:#a6e3a1;">K = 이 문장의 단어들로부터</div>
      <div style="background:#0f172a; border-radius:7px; padding:7px 12px; font-family:Consolas,monospace; font-size:12px; color:#a6e3a1;">V = 이 문장의 단어들로부터</div>
    </div>
    <div style="margin-top:8px; font-size:12px; color:#94a3b8; text-align:center;">같은 문장 안에서 관계 탐색</div>
  </div>
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:10px; text-align:center;">Encoder-Decoder Attention</div>
    <div style="display:grid; gap:5px;">
      <div style="background:#0f172a; border-radius:7px; padding:7px 12px; font-family:Consolas,monospace; font-size:12px; color:#f9e2af;">Q = Decoder 현재 상태</div>
      <div style="background:#0f172a; border-radius:7px; padding:7px 12px; font-family:Consolas,monospace; font-size:12px; color:#cba6f7;">K = Encoder 출력 벡터</div>
      <div style="background:#0f172a; border-radius:7px; padding:7px 12px; font-family:Consolas,monospace; font-size:12px; color:#cba6f7;">V = Encoder 출력 벡터</div>
    </div>
    <div style="margin-top:8px; font-size:12px; color:#94a3b8; text-align:center;">원문과 번역문 사이 연결</div>
  </div>
</div>

<!-- 도서관 비유 -->
<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 16px 18px; border-radius: 14px;">
  <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">📚 도서관 비유로 이해하기</div>
  <div style="display:grid; gap:8px;">
    <div style="background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 12px; display:flex; gap:10px; align-items:flex-start;">
      <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:3px 8px; border-radius:6px; font-size:11px; font-weight:900;">Q</div>
      <div style="font-size:13px; color:#334155; line-height:1.7;">"나는 지금 <b>영어 동사</b>를 생성해야 해. 원문에서 동사에 해당하는 부분이 어딨지?"</div>
    </div>
    <div style="background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 12px; display:flex; gap:10px; align-items:flex-start;">
      <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:3px 8px; border-radius:6px; font-size:11px; font-weight:900;">K</div>
      <div style="font-size:13px; color:#334155; line-height:1.7;">"나는(주어), 밥을(목적어), <b>먹었다(동사)</b>, ..."</div>
    </div>
    <div style="background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 12px; display:flex; gap:10px; align-items:flex-start;">
      <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:3px 8px; border-radius:6px; font-size:11px; font-weight:900;">V</div>
      <div style="font-size:13px; color:#334155; line-height:1.7;">Q로 K를 검색 → <b>"먹었다"가 가장 관련 있음</b> → V에서 "먹었다"의 내용을 가져옴</div>
    </div>
  </div>
</div>

</div>

<br>

<!-- 실제 계산 과정 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔢 실제 계산 과정: "ate"를 생성하는 시점
</h2>

<div style="display: grid; gap: 10px; margin-top: 14px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 1</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:6px;">Decoder 현재 상태에서 Q 생성</div>
      <div style="font-family:Consolas,monospace; font-size:13px; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8;">
        <span style="color:#6c7086;">지금까지 생성한 단어: ["I"]</span><br>
        → <span style="color:#f9e2af;">Q_decoder</span> = <span style="color:#89dceb;">"ate를 생성하기 위한 질문 벡터"</span>
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 2</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:6px;">Encoder 출력에서 K, V 생성</div>
      <div style="font-family:Consolas,monospace; font-size:13px; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">Encoder 출력: [벡터_나는, 벡터_밥을, 벡터_먹었다]</span>
→ <span style="color:#cba6f7;">K_나는,  V_나는</span>
→ <span style="color:#cba6f7;">K_밥을,  V_밥을</span>
→ <span style="color:#cba6f7;">K_먹었다, V_먹었다</span></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 3</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:6px;">Q와 모든 K를 비교 → 유사도 계산</div>
      <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:8px;">
        <div style="background:#0f172a; border-radius:8px; padding:10px; text-align:center;">
          <div style="font-family:Consolas,monospace; font-size:12px; color:#a6e3a1; margin-bottom:4px;">나는</div>
          <div style="font-size:16px; font-weight:900; color:#6c7086;">15%</div>
        </div>
        <div style="background:#0f172a; border-radius:8px; padding:10px; text-align:center;">
          <div style="font-family:Consolas,monospace; font-size:12px; color:#a6e3a1; margin-bottom:4px;">밥을</div>
          <div style="font-size:16px; font-weight:900; color:#6c7086;">20%</div>
        </div>
        <div style="background:#0f172a; border:2px solid #f9e2af; border-radius:8px; padding:10px; text-align:center;">
          <div style="font-family:Consolas,monospace; font-size:12px; color:#a6e3a1; margin-bottom:4px;">먹었다</div>
          <div style="font-size:16px; font-weight:900; color:#f9e2af;">65%</div>
        </div>
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 4</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:6px;">가중치에 따라 V를 합산 → "ate" 생성</div>
      <div style="font-family:Consolas,monospace; font-size:13px; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">결과 = </span><span style="color:#cba6f7;">V_나는</span>   × <span style="color:#6c7086;">0.15</span>
      <span style="color:#6c7086;">+</span> <span style="color:#cba6f7;">V_밥을</span>   × <span style="color:#6c7086;">0.20</span>
      <span style="color:#6c7086;">+</span> <span style="color:#cba6f7;">V_먹었다</span> × <span style="color:#f9e2af;">0.65</span>  <span style="color:#6c7086;">← "먹었다" 정보가 65% 반영</span>
→ <span style="color:#a6e3a1;">"ate"</span> 생성!</div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 번역 단어마다 달라지는 Attention -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎯 번역 단어마다 Attention 패턴이 달라진다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
각 출력 단어를 생성할 때마다, 어떤 입력 단어에 집중하는지가 달라집니다.
</p>

<div style="display: grid; gap: 10px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px;">
    <div style="font-size:13px; font-weight:900; color:#a6e3a1; background:#0f172a; display:inline-block; padding:3px 10px; border-radius:6px; margin-bottom:8px; font-family:Consolas,monospace;">"I" 생성 시</div>
    <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:6px;">
      <div style="background:#0f172a; border:2px solid #f9e2af; border-radius:8px; padding:8px; text-align:center;">
        <div style="font-family:Consolas,monospace; font-size:11px; color:#a6e3a1; margin-bottom:2px;">나는</div>
        <div style="font-size:15px; font-weight:900; color:#f9e2af;">80%</div>
      </div>
      <div style="background:#0f172a; border-radius:8px; padding:8px; text-align:center;">
        <div style="font-family:Consolas,monospace; font-size:11px; color:#a6e3a1; margin-bottom:2px;">밥을</div>
        <div style="font-size:15px; font-weight:900; color:#6c7086;">10%</div>
      </div>
      <div style="background:#0f172a; border-radius:8px; padding:8px; text-align:center;">
        <div style="font-family:Consolas,monospace; font-size:11px; color:#a6e3a1; margin-bottom:2px;">먹었다</div>
        <div style="font-size:15px; font-weight:900; color:#6c7086;">10%</div>
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px;">
    <div style="font-size:13px; font-weight:900; color:#a6e3a1; background:#0f172a; display:inline-block; padding:3px 10px; border-radius:6px; margin-bottom:8px; font-family:Consolas,monospace;">"ate" 생성 시</div>
    <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:6px;">
      <div style="background:#0f172a; border-radius:8px; padding:8px; text-align:center;">
        <div style="font-family:Consolas,monospace; font-size:11px; color:#a6e3a1; margin-bottom:2px;">나는</div>
        <div style="font-size:15px; font-weight:900; color:#6c7086;">15%</div>
      </div>
      <div style="background:#0f172a; border-radius:8px; padding:8px; text-align:center;">
        <div style="font-family:Consolas,monospace; font-size:11px; color:#a6e3a1; margin-bottom:2px;">밥을</div>
        <div style="font-size:15px; font-weight:900; color:#6c7086;">20%</div>
      </div>
      <div style="background:#0f172a; border:2px solid #f9e2af; border-radius:8px; padding:8px; text-align:center;">
        <div style="font-family:Consolas,monospace; font-size:11px; color:#a6e3a1; margin-bottom:2px;">먹었다</div>
        <div style="font-size:15px; font-weight:900; color:#f9e2af;">65%</div>
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px;">
    <div style="font-size:13px; font-weight:900; color:#a6e3a1; background:#0f172a; display:inline-block; padding:3px 10px; border-radius:6px; margin-bottom:8px; font-family:Consolas,monospace;">"rice" 생성 시</div>
    <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:6px;">
      <div style="background:#0f172a; border-radius:8px; padding:8px; text-align:center;">
        <div style="font-family:Consolas,monospace; font-size:11px; color:#a6e3a1; margin-bottom:2px;">나는</div>
        <div style="font-size:15px; font-weight:900; color:#6c7086;">10%</div>
      </div>
      <div style="background:#0f172a; border:2px solid #f9e2af; border-radius:8px; padding:8px; text-align:center;">
        <div style="font-family:Consolas,monospace; font-size:11px; color:#a6e3a1; margin-bottom:2px;">밥을</div>
        <div style="font-size:15px; font-weight:900; color:#f9e2af;">75%</div>
      </div>
      <div style="background:#0f172a; border-radius:8px; padding:8px; text-align:center;">
        <div style="font-family:Consolas,monospace; font-size:11px; color:#a6e3a1; margin-bottom:2px;">먹었다</div>
        <div style="font-size:15px; font-weight:900; color:#6c7086;">15%</div>
      </div>
    </div>
  </div>

</div>

<div style="margin-top:14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> Decoder가 자동으로 <b style="color:#FF6B00;">"지금 생성하는 단어와 가장 관련 있는 원문 단어"</b>를 찾아냅니다.<br>
이 능력 덕분에 <b style="color:#FF6B00;">긴 문장도 정확하게 번역</b>할 수 있습니다.
</div>

</div>

<br>

<!-- 어순이 달라도 괜찮다 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🌍 언어 구조가 달라도 괜찮다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
한국어와 영어는 어순이 다릅니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-bottom: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">어순 차이</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">한국어:</span> <span style="color:#a6e3a1;">나는</span><span style="color:#6c7086;">(1)</span>  <span style="color:#a6e3a1;">밥을</span><span style="color:#6c7086;">(2)</span>  <span style="color:#a6e3a1;">먹었다</span><span style="color:#6c7086;">(3)</span>
<span style="color:#6c7086;">영어:  </span>  <span style="color:#89dceb;">I</span><span style="color:#6c7086;">(1)</span>    <span style="color:#f9e2af;">ate</span><span style="color:#6c7086;">(2)</span>    <span style="color:#89dceb;">rice</span><span style="color:#6c7086;">(3)</span>

<span style="color:#6c7086;">"나는"  → "I"</span>        <span style="color:#a6e3a1;">(1번째 → 1번째, 같음)</span>
<span style="color:#6c7086;">"먹었다" → "ate"</span>     <span style="color:#f38ba8;">(3번째 → 2번째, 달라짐!)</span>
<span style="color:#6c7086;">"밥을"  → "rice"</span>     <span style="color:#f38ba8;">(2번째 → 3번째, 달라짐!)</span></div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> Encoder-Decoder Attention은 <b style="color:#1681c4;">단어의 순서에 구애받지 않고</b>,<br>
의미적으로 대응하는 단어를 <b style="color:#1681c4;">자동으로 연결</b>합니다.
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
      <th style="padding:10px 14px; text-align:left; font-weight:900;">Self-Attention</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">Encoder-Decoder Attention</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#475569;">사용 위치</td>
      <td style="padding:10px 14px; color:#334155;">Encoder &amp; Decoder</td>
      <td style="padding:10px 14px; color:#FF6B00; font-weight:900;">Decoder만</td>
    </tr>
    <tr style="background:#fff8f4; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#475569;">Q 출처</td>
      <td style="padding:10px 14px; color:#334155;">현재 레이어 입력</td>
      <td style="padding:10px 14px; color:#FF6B00; font-weight:900;">Decoder 현재 상태</td>
    </tr>
    <tr style="background:#fff; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; font-weight:900; color:#475569;">K, V 출처</td>
      <td style="padding:10px 14px; color:#334155;">현재 레이어 입력</td>
      <td style="padding:10px 14px; color:#FF6B00; font-weight:900;">Encoder 최종 출력</td>
    </tr>
    <tr style="background:#fff8f4;">
      <td style="padding:10px 14px; font-weight:900; color:#475569;">역할</td>
      <td style="padding:10px 14px; color:#334155;">같은 문장 안 단어 관계</td>
      <td style="padding:10px 14px; color:#FF6B00; font-weight:900;">원문과 번역문 사이 연결</td>
    </tr>
  </tbody>
</table>
</div>

<div style="display: grid; gap: 8px;">
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Q는 Decoder에서, K와 V는 <b style="color:#FF6B00;">Encoder 출력</b>에서 만들어집니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    출력 단어마다 Attention 패턴이 달라지면서 <b style="color:#FF6B00;">원문의 올바른 부분을 자동으로 참조</b>합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    어순이 다른 언어 쌍도 <b style="color:#FF6B00;">의미적 연결</b>로 정확하게 번역할 수 있습니다.
  </div>
</div>

<div style="margin-top:12px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> 다음 페이지에서는 이 모든 것이 합쳐진 <b style="color:#1681c4;">Decoder 전체 흐름</b>을 처음부터 끝까지 따라가 봅니다.
</div>

</div>

</div>