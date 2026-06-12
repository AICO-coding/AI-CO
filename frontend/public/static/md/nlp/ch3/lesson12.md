<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
TF-IDF
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
TF-IDF는
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">이 문서에서 자주 나오면서, 다른 문서에서는 드문 단어</span>
에 높은 점수를 부여하는 방법입니다.
</p>

</div>

<br>

<!-- BoW의 문제 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🤔 BoW의 문제: 자주 나오면 항상 중요한가?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BoW는 단어의 등장 횟수를 셌습니다. 그런데 다음 상황을 생각해봅시다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; padding: 14px 20px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; line-height: 2.2; margin: 14px 0; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">[문서 1]</span> <span style="color:#a6e3a1;">"오늘 날씨가 맑다. 날씨가 좋아서 기분이 좋다."</span>
<span style="color:#6c7086;">[문서 2]</span> <span style="color:#a6e3a1;">"오늘 경기에서 선수가 골을 넣었다. 좋은 경기였다."</span>
<span style="color:#6c7086;">[문서 3]</span> <span style="color:#a6e3a1;">"오늘 주가가 올랐다. 금리가 떨어져서 시장이 좋다."</span></div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 14px;">
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:14px 16px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:8px;">😐 범용 단어 — 별로 특별하지 않음</div>
    <div style="display:flex; gap:6px; flex-wrap:wrap;">
      <span style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:3px 9px; border-radius:6px; font-family:Consolas, monospace; font-size:13px;">오늘</span>
      <span style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:3px 9px; border-radius:6px; font-family:Consolas, monospace; font-size:13px;">좋다</span>
    </div>
    <div style="margin-top:8px; font-size:13px; color:#475569; line-height:1.6;">세 문서 모두에 자주 등장하지만<br>각 문서의 주제를 나타내지 않습니다.</div>
  </div>
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 16px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:8px;">⭐ 핵심 단어 — 문서를 잘 설명함</div>
    <div style="display:flex; gap:6px; flex-wrap:wrap;">
      <span style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:3px 9px; border-radius:6px; font-family:Consolas, monospace; font-size:13px;">날씨</span>
      <span style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:3px 9px; border-radius:6px; font-family:Consolas, monospace; font-size:13px;">경기</span>
      <span style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:3px 9px; border-radius:6px; font-family:Consolas, monospace; font-size:13px;">주가</span>
    </div>
    <div style="margin-top:8px; font-size:13px; color:#475569; line-height:1.6;">각 문서에만 등장하여<br>주제를 훨씬 잘 설명합니다.</div>
  </div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
BoW는 이런 범용 단어와 핵심 단어를 구별하지 못합니다.<br>
이 문제를 해결하는 것이 <b style="color:#FF6B00;">TF-IDF</b>입니다.
</div>

</div>

<br>

<!-- TF-IDF 핵심 아이디어 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💡 TF-IDF의 핵심 아이디어
</h2>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.9; margin-bottom: 18px;">
<span style="color: #FF6B00; font-weight: 900;">💡 핵심</span><br>
<b>이 문서에서 자주 나오면서(TF),<br>
다른 문서에서는 잘 안 나오는 단어(IDF)가 중요하다!</b>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 16px;">
TF-IDF는 두 가지 점수를 곱해서 단어의 중요도를 계산합니다.
</p>

<div style="background-color: #0f172a; border-radius: 14px; padding: 14px 20px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 14px; color: #c3e88d; text-align: center; margin-bottom: 18px; font-weight: 900; letter-spacing: 0.5px;">
TF-IDF 점수 = TF(단어 빈도) × IDF(역문서 빈도)
</div>

<div style="display: grid; gap: 10px;">

  <div style="display:grid; grid-template-columns:80px 120px 1fr; gap:10px; align-items:center;">
    <div style="background:#FF6B00; color:#fff; padding:9px 12px; border-radius:10px; font-size:14px; font-weight:900; text-align:center;">TF</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:12px; color:#475569; text-align:center;">Term Frequency</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 14px; border-radius:10px; font-size:14px; color:#334155;">이 단어가 <b style="color:#FF6B00;">이 문서</b>에서 얼마나 자주 나오나?</div>
  </div>

  <div style="display:grid; grid-template-columns:80px 120px 1fr; gap:10px; align-items:center;">
    <div style="background:#1681c4; color:#fff; padding:9px 12px; border-radius:10px; font-size:14px; font-weight:900; text-align:center;">IDF</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:12px; color:#475569; text-align:center;">Inverse Document Frequency</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 14px; border-radius:10px; font-size:14px; color:#334155;">이 단어가 <b style="color:#1681c4;">전체 문서</b> 중 얼마나 희귀한가?</div>
  </div>

  <div style="display:grid; grid-template-columns:80px 120px 1fr; gap:10px; align-items:center;">
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; text-align:center;">TF-IDF</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:12px; color:#475569; text-align:center;">TF × IDF</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 14px; border-radius:10px; font-size:14px; color:#334155;">이 문서에서 자주, 다른 문서에선 드물게 나오는 단어</div>
  </div>

</div>
</div>

<br>

<!-- 기자 비유 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📰 비유로 이해하기: 기자의 특종 기사
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
어떤 기자가 100개의 기사를 썼습니다. "경제" 기사 하나를 분석해봅시다.
</p>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="display:grid; grid-template-columns:80px 1fr auto; gap:12px; align-items:center; background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px;">
    <div style="background:#1681c4; color:#fff; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px; font-weight:900; text-align:center;">"주가"</div>
    <div style="font-size:13px; color:#334155; line-height:1.7;">이 기사에 <b>10번</b> 등장, 전체 100개 기사 중 <b>3개</b>에만 등장</div>
    <div style="background:#1681c4; color:#fff; padding:5px 12px; border-radius:999px; font-size:12px; font-weight:900; white-space:nowrap;">핵심 단어 ⭐</div>
  </div>

  <div style="display:grid; grid-template-columns:80px 1fr auto; gap:12px; align-items:center; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px;">
    <div style="background:#94a3b8; color:#fff; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px; font-weight:900; text-align:center;">"오늘"</div>
    <div style="font-size:13px; color:#334155; line-height:1.7;">이 기사에 <b>5번</b> 등장, 전체 100개 기사 중 <b>90개</b>에 등장</div>
    <div style="background:#94a3b8; color:#fff; padding:5px 12px; border-radius:999px; font-size:12px; font-weight:900; white-space:nowrap;">별로 특별 않음 😐</div>
  </div>

  <div style="display:grid; grid-template-columns:80px 1fr auto; gap:12px; align-items:center; background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 16px;">
    <div style="background:#FF6B00; color:#fff; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px; font-weight:900; text-align:center;">"이다"</div>
    <div style="font-size:13px; color:#334155; line-height:1.7;">이 기사에 <b>20번</b> 등장, 전체 100개 기사 <b>모두</b>에 등장</div>
    <div style="background:#FF6B00; color:#fff; padding:5px 12px; border-radius:999px; font-size:12px; font-weight:900; white-space:nowrap;">완전 범용 단어 ❌</div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
TF-IDF는 이런 판단을 <b style="color:#FF6B00;">수학적으로</b> 계산하는 방법입니다.
</div>

</div>

<br>

<!-- 계산 공식 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔢 TF-IDF 계산 공식
</h2>

<div style="display: grid; gap: 14px; margin-top: 4px;">

<!-- TF -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 14px; border-radius:999px; font-size:13px; font-weight:900;">TF</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">단어 빈도 (Term Frequency)</div>
  </div>
  <p style="margin:0 0 12px 0; font-size:14px; color:#475569; line-height:1.7;">해당 문서에서 특정 단어가 등장하는 비율입니다.</p>
  <div style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">TF(t, d) =</span>  <span style="color:#89dceb;">문서 d에서 단어 t의 등장 횟수</span>
           <span style="color:#6c7086;">─────────────────────────────</span>
           <span style="color:#89dceb;">문서 d의 전체 단어 수</span></div>
  <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; background:#1e1e2e; line-height:1.9; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">예시: </span><span style="color:#a6e3a1;">"나는 밥을 먹었다 밥을"</span><span style="color:#6c7086;">  (전체 4개 단어)</span>
<span style="color:#cdd6f4;">TF(</span><span style="color:#a6e3a1;">"밥을"</span><span style="color:#cdd6f4;">, 문서1) = 2 / 4 = </span><span style="color:#ff5f57; font-weight:900;">0.5</span></div>
</div>

<!-- IDF -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 14px; border-radius:999px; font-size:13px; font-weight:900;">IDF</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">역문서 빈도 (Inverse Document Frequency)</div>
  </div>
  <p style="margin:0 0 12px 0; font-size:14px; color:#475569; line-height:1.7;">전체 문서 중에서 해당 단어가 얼마나 희귀한지를 나타냅니다.<br>
  <b style="color:#1681c4;">많은 문서에 등장할수록 IDF 값이 낮아집니다.</b></p>
  <div style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">IDF(t) = log(</span> <span style="color:#89dceb;">전체 문서 수</span> <span style="color:#6c7086;">/</span> <span style="color:#89dceb;">단어 t가 등장한 문서 수</span> <span style="color:#6c7086;">)</span></div>
  <div style="background:#1e1e2e; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; line-height:2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">예시: 전체 문서 4개일 때</span>
<span style="color:#cdd6f4;">"밥을"이 </span><span style="color:#a6e3a1;">2개</span><span style="color:#cdd6f4;"> 문서에 등장 → IDF = log(4/2) = log(2) ≈ </span><span style="color:#ff5f57; font-weight:900;">0.693</span>
<span style="color:#cdd6f4;">"나는"이 </span><span style="color:#a6e3a1;">4개</span><span style="color:#cdd6f4;"> 문서에 등장 → IDF = log(4/4) = log(1) = </span><span style="color:#ff5f57; font-weight:900;">0.0</span></div>
  <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    <span style="color:#1681c4; font-weight:900;">💡</span> "나는"은 모든 문서에 등장하므로 IDF = 0 → TF-IDF도 0이 됩니다.<br>
    즉, 어디서나 나오는 단어는 <b style="color:#1681c4;">자동으로 중요도가 0</b>으로 처리됩니다!
  </div>
</div>

<!-- TF-IDF 최종 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#0f172a; color:#c3e88d; padding:3px 14px; border-radius:999px; font-size:13px; font-weight:900;">TF-IDF</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">최종 점수</div>
  </div>
  <div style="background:#1e1e2e; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#cdd6f4;">TF-IDF(</span><span style="color:#a6e3a1;">"밥을"</span><span style="color:#cdd6f4;">, 문서1) = 0.5 × 0.693 = </span><span style="color:#ff5f57; font-weight:900;">0.347</span>
<span style="color:#cdd6f4;">TF-IDF(</span><span style="color:#a6e3a1;">"나는"</span><span style="color:#cdd6f4;">, 문서1) = 0.25 × 0.0  = </span><span style="color:#89dceb; font-weight:900;">0.0</span></div>
  <div style="margin-top:10px; background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    "나는"보다 <b style="color:#FF6B00;">"밥을"</b>이 문서 1에서 훨씬 중요한 단어로 계산됩니다.
  </div>
</div>

</div>
</div>

<br>

<!-- 손계산 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📋 손으로 계산해보기
</h2>

<div style="background-color: #0f172a; border-radius: 14px; padding: 14px 20px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; line-height: 2.2; margin-bottom: 16px;">
  <span style="color:#6c7086;">문서 1: </span><span style="color:#a6e3a1;">"나는 밥을 먹었다"</span><br>
  <span style="color:#6c7086;">문서 2: </span><span style="color:#a6e3a1;">"나는 물을 마셨다"</span><br>
  <span style="color:#6c7086;">문서 3: </span><span style="color:#a6e3a1;">"고양이가 밥을 먹었다"</span><br>
  <span style="color:#6c7086;">문서 4: </span><span style="color:#a6e3a1;">"고양이가 물을 마셨다"</span>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">

  <!-- 밥을 계산 -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:12px;">"밥을"의 TF-IDF (문서 1 기준)</div>
    <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:12px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">① TF = 1 / 3 ≈ </span><span style="color:#89dceb;">0.333</span>
<span style="color:#6c7086;">   (문서1에서 1번, 전체 단어 3개)</span>

<span style="color:#6c7086;">② IDF = log(4/2) ≈ </span><span style="color:#89dceb;">0.693</span>
<span style="color:#6c7086;">   (4개 문서 중 문서1,3에 등장)</span>

<span style="color:#6c7086;">③ TF-IDF = </span><span style="color:#ff5f57; font-weight:900;">0.333 × 0.693 ≈ 0.231</span></div>
  </div>

  <!-- 나는 계산 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:12px;">"나는"의 TF-IDF (문서 1 기준)</div>
    <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:12px; line-height:2.2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">① TF = 1 / 3 ≈ </span><span style="color:#89dceb;">0.333</span>

<span style="color:#6c7086;">② IDF = log(4/2) ≈ </span><span style="color:#89dceb;">0.693</span>
<span style="color:#6c7086;">   (4개 문서 중 문서1,2에 등장)</span>

<span style="color:#6c7086;">③ TF-IDF = </span><span style="color:#ff5f57; font-weight:900;">0.333 × 0.693 ≈ 0.231</span></div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌</span> 이 예시는 문서가 적고 단어도 단순해서 점수가 비슷하게 나옵니다.<br>
실제로 수백~수천 개 문서를 다루면 TF-IDF의 효과가 훨씬 뚜렷하게 나타납니다.
</div>

</div>

</div>