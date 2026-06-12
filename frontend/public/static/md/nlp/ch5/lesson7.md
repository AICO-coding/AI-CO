<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Encoder — Self-Attention
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
같은 문장 안의 단어들이 서로를 바라보는
<b style="color:#1681c4;">Self-Attention</b>의 원리와 Q, K, V 계산 과정을 알아봅니다.
</p>

</div>

<br>

<!-- Attention 복습 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔁 챕터 4에서 배운 Attention을 다시 불러옵시다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
챕터 4에서 배운 Attention의 핵심 아이디어는 이것이었습니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; font-weight: 900; line-height: 1.8; margin: 14px 0;">
<span style="color: #1681c4;">"문장을 번역할 때, 지금 번역하는 단어와 <b>가장 관련 있는 입력 단어</b>에 집중한다."</span>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡 예시:</span> "나는 밥을 먹었다"를 번역할 때,<br>
"ate"를 생성하는 순간에는 <b style="color:#FF6B00;">"먹었다"</b>에 가장 높은 집중도(Attention 가중치)를 줍니다.
</div>

</div>

<br>

<!-- Self-Attention 개념 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🆕 Self-Attention: 같은 문장 안에서 서로를 바라본다
</h2>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px;">
    <div style="font-size:12px; font-weight:900; color:#94a3b8; margin-bottom:8px;">챕터 4의 Attention</div>
    <div style="font-size:13px; color:#475569; line-height:1.8;"><b>서로 다른 두 문장</b> 사이의 관계를 계산했습니다.<br><span style="color:#94a3b8;">(입력 문장 → 출력 문장)</span></div>
  </div>
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px;">
    <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:8px;">Self-Attention</div>
    <div style="font-size:13px; color:#334155; line-height:1.8;"><b style="color:#1681c4;">같은 문장 안</b>의 단어들이 서로서로를 바라봅니다.</div>
  </div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> <code style="background:#0f172a; color:#89dceb; padding:2px 6px; border-radius:4px; font-size:12px;">Self</code>(자기 자신)라는 말이 붙은 이유가 여기 있습니다.<br>
입력 문장 하나만 가지고, 그 안의 <b style="color:#1681c4;">단어들끼리 관계를 계산</b>합니다.
</div>

</div>

<br>

<!-- "배" 예시 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🌰 Self-Attention 예시: "배"라는 단어의 의미
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
한국어에서 "배"는 여러 뜻이 있습니다.
</p>

<div style="display: grid; gap: 8px; margin-bottom: 16px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:14px; align-items:center;">
    <div style="font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; background:#0f172a; padding:6px 12px; border-radius:8px; white-space:nowrap;">문장 1</div>
    <div style="font-size:14px; color:#334155;">"나는 <b style="color:#FF6B00;">배</b>가 고프다" &nbsp;→&nbsp; 배 = <b>신체 기관 (복부)</b></div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:14px; align-items:center;">
    <div style="font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; background:#0f172a; padding:6px 12px; border-radius:8px; white-space:nowrap;">문장 2</div>
    <div style="font-size:14px; color:#334155;">"<b style="color:#FF6B00;">배</b>를 타고 떠났다" &nbsp;→&nbsp; 배 = <b>선박</b></div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; display:flex; gap:14px; align-items:center;">
    <div style="font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; background:#0f172a; padding:6px 12px; border-radius:8px; white-space:nowrap;">문장 3</div>
    <div style="font-size:14px; color:#334155;">"<b style="color:#FF6B00;">배</b>가 맛있게 익었다" &nbsp;→&nbsp; 배 = <b>과일</b></div>
  </div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; margin-bottom: 16px;">
<span style="color: #FF6B00; font-weight: 900;">⚠️ 문제:</span> 단어 임베딩(챕터 3)에서는 "배"라는 단어가 항상 <b style="color:#FF6B00;">같은 벡터</b>를 가졌습니다.<br>
어느 문장이든 "배" → <code style="background:#0f172a; color:#89dceb; padding:2px 6px; border-radius:4px; font-size:12px;">[0.5, 0.3, 0.8, ...]</code>으로 고정되어 있었죠.
</div>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18);">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Self-Attention 적용 후</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#cba6f7;">"나는 배가 고프다"</span> 에서 <span style="color:#f38ba8;">"배"</span>:
  → <span style="color:#6c7086;">"나는"(0.1) + </span><span style="color:#a6e3a1;">"배가"(1.0)</span><span style="color:#6c7086;"> + </span><span style="color:#a6e3a1;">"고프다"(0.8)</span><span style="color:#6c7086;"> 참고</span>
  → <span style="color:#89dceb;">"신체 기관" 의미 반영</span>

<span style="color:#cba6f7;">"배를 타고 떠났다"</span> 에서 <span style="color:#f38ba8;">"배"</span>:
  → <span style="color:#a6e3a1;">"배를"(1.0)</span><span style="color:#6c7086;"> + </span><span style="color:#a6e3a1;">"타고"(0.9)</span><span style="color:#6c7086;"> + </span><span style="color:#a6e3a1;">"떠났다"(0.7)</span><span style="color:#6c7086;"> 참고</span>
  → <span style="color:#89dceb;">"선박" 의미 반영</span></div>
</div>

<div style="margin-top:14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> 같은 단어 "배"라도, <b style="color:#1681c4;">주변 단어들과의 관계에 따라 다른 벡터</b>가 만들어집니다.<br>
이것이 Self-Attention의 핵심 능력입니다.
</div>

</div>

<br>

<!-- Q, K, V -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
⚙️ Self-Attention 계산 과정: Q, K, V
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 16px;">
Self-Attention은 <b>Q(Query), K(Key), V(Value)</b> 세 가지 벡터를 사용합니다.<br>
도서관 검색 시스템으로 비유하면 쉽습니다.
</p>

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 16px;">
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:22px; margin-bottom:6px;">🔍</div>
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:4px;">Q (Query)</div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">"내가 지금<br>찾는 것"</div>
  </div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:22px; margin-bottom:6px;">🏷️</div>
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:4px;">K (Key)</div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">"각 책에 붙어있는<br>분류 태그"</div>
  </div>
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:22px; margin-bottom:6px;">📖</div>
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:4px;">V (Value)</div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">"책의<br>실제 내용"</div>
  </div>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
이제 실제 단어에 적용해봅시다. <b>"나는 배가 고프다"</b>에서 <b style="color:#FF6B00;">"고프다"</b>의 계산 과정입니다.
</p>

<div style="display: grid; gap: 10px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 1</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">각 단어에서 Q, K, V 벡터를 만든다</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"나는"</span>   → <span style="color:#89dceb;">Q_나는,  K_나는,  V_나는</span>
<span style="color:#a6e3a1;">"배가"</span>   → <span style="color:#89dceb;">Q_배가,  K_배가,  V_배가</span>
<span style="color:#a6e3a1;">"고프다"</span> → <span style="color:#89dceb;">Q_고프다, K_고프다, V_고프다</span></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 2</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">"고프다"의 Q로 모든 단어의 K와 비교 → 유사도 점수 계산</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#cba6f7;">Q_고프다</span> vs <span style="color:#a6e3a1;">K_나는</span>   → 점수: <span style="color:#6c7086;">0.2  (별로 관련 없음)</span>
<span style="color:#cba6f7;">Q_고프다</span> vs <span style="color:#a6e3a1;">K_배가</span>   → 점수: <span style="color:#f9e2af;">0.9  (매우 관련 있음! "배"는 신체)</span>
<span style="color:#cba6f7;">Q_고프다</span> vs <span style="color:#a6e3a1;">K_고프다</span> → 점수: <span style="color:#89dceb;">0.6  (자기 자신)</span></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 3</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:8px;">점수를 비율로 변환 <span style="color:#94a3b8; font-size:12px; font-weight:400;">(Softmax, 합이 1이 되도록)</span></div>
      <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:8px;">
        <div style="background:#0f172a; border-radius:8px; padding:10px; text-align:center;">
          <div style="font-family:Consolas,monospace; font-size:12px; color:#a6e3a1; margin-bottom:4px;">나는</div>
          <div style="font-size:18px; font-weight:900; color:#6c7086;">14%</div>
        </div>
        <div style="background:#0f172a; border-radius:8px; padding:10px; text-align:center; border:2px solid #f9e2af;">
          <div style="font-family:Consolas,monospace; font-size:12px; color:#a6e3a1; margin-bottom:4px;">배가</div>
          <div style="font-size:18px; font-weight:900; color:#f9e2af;">64%</div>
        </div>
        <div style="background:#0f172a; border-radius:8px; padding:10px; text-align:center;">
          <div style="font-family:Consolas,monospace; font-size:12px; color:#a6e3a1; margin-bottom:4px;">고프다</div>
          <div style="font-size:18px; font-weight:900; color:#89dceb;">22%</div>
        </div>
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 4</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">비율만큼 각 단어의 V를 가중 합산</div>
      <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">최종 "고프다" 벡터 =</span>
  <span style="color:#89dceb;">V_나는</span>   × <span style="color:#6c7086;">0.14</span>  <span style="color:#6c7086;">+</span>
  <span style="color:#89dceb;">V_배가</span>   × <span style="color:#f9e2af;">0.64</span>  <span style="color:#6c7086;">+  ← "배"의 정보가 64% 반영됨</span>
  <span style="color:#89dceb;">V_고프다</span> × <span style="color:#6c7086;">0.22</span></div>
    </div>
  </div>

</div>

<div style="margin-top:14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡 결과:</span> "고프다"의 새 벡터에는 <b style="color:#FF6B00;">"배가"의 정보가 64% 녹아들어 있습니다.</b><br>
그래서 "배"가 신체 기관이라는 맥락이 자동으로 반영됩니다.
</div>

</div>

<br>

<!-- 모든 단어 동시에 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 모든 단어가 동시에 이 과정을 수행합니다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Self-Attention의 강력함은 여기 있습니다.<br>
"나는", "배가", "고프다" <b style="color:#1681c4;">모두가 동시에</b> 위의 과정을 수행합니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">동시 처리</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#a6e3a1;">"나는"</span>  <span style="color:#cba6f7;">←→</span>  <span style="color:#a6e3a1;">"배가"</span>   <span style="color:#cba6f7;">←→</span>  <span style="color:#a6e3a1;">"고프다"</span>
  <span style="color:#cba6f7;">↕</span>            <span style="color:#cba6f7;">↕</span>            <span style="color:#cba6f7;">↕</span>
<span style="color:#6c7086;">모든 단어가 서로의 관계를 동시에 계산</span></div>
</div>

<div style="display: grid; gap: 8px; margin-top: 4px;">
  <div style="background:#eef7ff; border-left:4px solid #1681c4; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    각 단어가 문장 안의 다른 모든 단어를 참고해서 자신의 벡터를 <b style="color:#1681c4;">문맥에 맞게 업데이트</b>합니다.
  </div>
  <div style="background:#eef7ff; border-left:4px solid #1681c4; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    RNN처럼 순서대로 처리하지 않고, <b style="color:#1681c4;">전체를 한꺼번에</b> 처리하기 때문에 빠릅니다.
  </div>
</div>

</div>

<br>

<!-- Self-Attention이 배우는 관계 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 Self-Attention이 배워내는 관계들
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
Encoder를 학습시키면, Self-Attention이 문법적·의미적으로 중요한 관계를 <b>자동으로 발견</b>합니다.
</p>

<div style="overflow-x: auto;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; font-weight:900;">예시 문장</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">단어 쌍</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">Self-Attention이 배우는 것</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; color:#475569; font-size:13px;">"그 동물은 너무 지쳐서... <b style="color:#FF6B00;">그것</b>은..."</td>
      <td style="padding:10px 14px; color:#FF6B00; font-weight:900;">그것 ↔ 동물</td>
      <td style="padding:10px 14px; color:#334155;">대명사와 지칭 대상 연결</td>
    </tr>
    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; color:#475569; font-size:13px;">"나는 <b style="color:#FF6B00;">빨간</b> 사과를 먹었다"</td>
      <td style="padding:10px 14px; color:#FF6B00; font-weight:900;">빨간 ↔ 사과</td>
      <td style="padding:10px 14px; color:#334155;">형용사와 명사 연결</td>
    </tr>
    <tr style="background:#fff;">
      <td style="padding:10px 14px; color:#475569; font-size:13px;">"<b style="color:#FF6B00;">은행</b>에 돈을 맡겼다" vs "강가를 거닐었다"</td>
      <td style="padding:10px 14px; color:#FF6B00; font-weight:900;">은행 ↔ 문맥</td>
      <td style="padding:10px 14px; color:#334155;">동음이의어 의미 구분</td>
    </tr>
  </tbody>
</table>
</div>

<div style="margin-top:14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> 이 모든 관계를 <b style="color:#1681c4;">사람이 직접 가르치지 않아도</b> 데이터에서 스스로 학습합니다.
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
    <b style="color:#FF6B00;">Self-Attention</b>은 같은 문장 안의 단어들이 <b style="color:#FF6B00;">서로의 관계를 계산</b>하는 메커니즘입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">Q(질문), K(태그), V(내용)</b> 세 벡터를 사용해서 각 단어가 다른 단어들을 얼마나 참고할지 계산합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    덕분에 "배"처럼 여러 뜻을 가진 단어도 <b style="color:#FF6B00;">문맥에 맞는 올바른 의미</b>로 표현할 수 있습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    모든 단어가 <b style="color:#FF6B00;">동시에</b> 처리되므로 병렬 처리가 가능하고 빠릅니다.
  </div>
</div>

<div style="margin-top:12px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> 다음 페이지에서는 이 Self-Attention을 <b style="color:#1681c4;">여러 개 동시에 실행</b>하는 Multi-Head Attention을 배웁니다.
</div>

</div>

</div>