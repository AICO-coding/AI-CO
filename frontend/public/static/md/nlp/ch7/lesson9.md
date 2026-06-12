<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">Chapter 07 · GPT</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">확률 분포에서 단어를 어떻게 고를까?</h1>
<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
확률 분포가 만들어졌다고 선택이 자동으로 정해지는 건 아닙니다.<br>
<b style="color:#1681c4;">디코딩 전략(Decoding Strategy)</b> 네 가지를 알아봅니다.
</p>
</div>

<br>

<!-- 어떻게 고르나 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🗺️ 확률이 나왔다면, 이제 어떻게 고르나?</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
앞 페이지에서 GPT가 모든 단어에 확률을 매긴다는 것을 배웠습니다. 그런데 <b>확률 분포가 있다고 해서 선택이 자동으로 정해지는 건 아닙니다.</b>
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> "가장 높은 것만 고를까? 아니면 확률에 따라 랜덤으로 뽑을까?" 이 선택 방법을 <b style="color:#1681c4;">디코딩 전략(Decoding Strategy)</b>이라고 합니다.<br>
전략에 따라 같은 GPT라도 <b style="color:#1681c4;">완전히 다른 문장</b>이 나올 수 있습니다.
</div>

</div>

<br>

<!-- 전략 ① Greedy -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">전략 ①</span>
Greedy Decoding — 매번 1등만 고른다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
가장 단순한 방법입니다. 매 단계마다 확률이 <b>가장 높은 단어 하나만</b> 선택합니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Greedy Decoding 흐름</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#6c7086;">"오늘 날씨가" 다음 단어 예측:</span>
  <span style="color:#a6e3a1; font-weight:900;">좋아서 43.2% ← ✅ 선택 (1등)</span>
  <span style="color:#6c7086;">나빠서 21.8%</span>
  <span style="color:#6c7086;">맑아서 15.1%</span>
  <span style="color:#6c7086;">...</span>

<span style="color:#6c7086;">"오늘 날씨가 좋아서" 다음:</span>
  <span style="color:#a6e3a1; font-weight:900;">기분이 55.7% ← ✅ 선택 (1등)</span>
  <span style="color:#6c7086;">...</span>

<span style="color:#6c7086;">"오늘 날씨가 좋아서 기분이" 다음:</span>
  <span style="color:#a6e3a1; font-weight:900;">좋다 68.3% ← ✅ 선택 (1등)</span>
  <span style="color:#6c7086;">...</span></div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
<div style="background:#f0fdf4; border:2px solid #86efac; border-radius:14px; padding:14px 18px;">
<div style="font-size:13px; font-weight:900; color:#16a34a; margin-bottom:6px;">✅ 장점</div>
<div style="font-size:13px; color:#334155; line-height:1.6;">빠르고, 결과가 항상 일정함</div>
</div>
<div style="background:#fff1f2; border:2px solid #fca5a5; border-radius:14px; padding:14px 18px;">
<div style="font-size:13px; font-weight:900; color:#dc2626; margin-bottom:6px;">❌ 단점</div>
<div style="font-size:13px; color:#334155; line-height:1.6;">창의성이 없고, 뻔한 문장만 나옴. 같은 문장이 반복될 수 있음</div>
</div>
</div>

<div style="margin-top: 14px; background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px;">
<div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:6px;">🍽️ 비유</div>
<div style="font-size:13px; color:#334155; line-height:1.7;">음식점 메뉴에서 항상 베스트셀러만 시키는 사람. 안전하지만, 새로운 맛을 경험할 기회가 없습니다.</div>
</div>

</div>

<br>

<!-- 전략 ② Temperature -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">전략 ②</span>
Temperature 조절 — 확률 분포의 날카로움을 바꾼다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
7-2에서 잠깐 다뤘던 <b style="color:#1681c4;">온도(Temperature)</b>입니다. 이 값으로 확률 분포 자체의 모양을 변형합니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">온도에 따른 분포 변화</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.2; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#6c7086;">원본 분포 (Temperature = 1.0):</span>
  <span style="color:#cdd6f4;">좋아서 43%  나빠서 22%  맑아서 15%  흐려서 9%  ...</span>

<span style="color:#89dceb;">Temperature 낮음 (0.3):</span>
  <span style="color:#89dceb;">좋아서 81%  나빠서  9%  맑아서  6%  흐려서 2%  ...</span>
  <span style="color:#6c7086;">→ 1등이 더욱 압도적 / 항상 비슷한 대답</span>

<span style="color:#f9e2af;">Temperature 높음 (1.5):</span>
  <span style="color:#f9e2af;">좋아서 28%  나빠서 22%  맑아서 19%  흐려서 16%  ...</span>
  <span style="color:#6c7086;">→ 차이가 줄어 다양한 단어가 선택될 기회 증가 / 엉뚱한 결과 가능</span></div>
</div>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px;">
<tr>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#1681c4; white-space:nowrap; width:110px;">0.1 ~ 0.5</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">안정적, 반복적, 예측 가능</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">코드 생성, 정확한 답변이 필요할 때</td>
</tr>
<tr><td style="height:2px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#1681c4; white-space:nowrap;">0.7 ~ 1.0</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">균형 잡힌 다양성</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">일반 대화, 요약</td>
</tr>
<tr><td style="height:2px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#FF6B00; white-space:nowrap;">1.2 ~ 2.0</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">창의적, 무작위성 높음</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">시 창작, 아이디어 브레인스토밍</td>
</tr>
</table>

</div>

<br>

<!-- 전략 ③ Top-k -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">전략 ③</span>
Top-k Sampling — 상위 k개 중에서만 고른다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
전체 수만 개의 단어 중 확률 상위 <b style="color:#FF6B00;">k개만 남기고</b> 나머지는 버립니다. 그 k개 안에서 확률에 따라 랜덤 선택합니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">k = 3 으로 설정한 경우</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.2; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#6c7086;">전체 확률 분포에서 상위 3개만 남김:</span>
  <span style="color:#a6e3a1;">좋아서 43.2%</span>
  <span style="color:#a6e3a1;">나빠서 21.8%</span>
  <span style="color:#a6e3a1;">맑아서 15.1%</span>
  <span style="color:#6c7086;">────────────</span>
  <span style="color:#f38ba8;">나머지(흐려서, 춥고, ...) → 0%로 제거</span>

<span style="color:#6c7086;">남은 3개의 확률을 다시 100%로 정규화:</span>
  <span style="color:#89dceb; font-weight:900;">좋아서 53.6%</span>
  <span style="color:#89dceb; font-weight:900;">나빠서 27.1%</span>
  <span style="color:#89dceb; font-weight:900;">맑아서 19.3%</span>
  <span style="color:#6c7086;">────────────</span>
  <span style="color:#f9e2af;">합계: 100%</span>

<span style="color:#cdd6f4;">이 중에서 확률에 따라 랜덤 선택</span></div>
</div>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px;">
<div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:6px;">🍽️ 비유</div>
<div style="font-size:13px; color:#334155; line-height:1.7;">음식점 메뉴 중 인기 상위 3개만 후보로 두고, 그 안에서 랜덤으로 선택. 완전히 이상한 음식(확률 낮은 단어)은 선택지 자체에서 제외됩니다.</div>
</div>

</div>

<br>

<!-- 전략 ④ Top-p -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#0f172a; color:#c3e88d; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">전략 ④</span>
Top-p Sampling (핵 샘플링) — 누적 확률 p%까지만 고른다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Top-k의 개선 버전입니다. 개수를 고정하는 대신, <b style="color:#1681c4;">누적 확률이 p%를 넘을 때까지</b> 높은 순서대로 단어를 모읍니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">p = 0.9 (90%) 로 설정한 경우</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.2; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#a6e3a1;">좋아서  43.2%  →  누적 43.2%</span>
<span style="color:#a6e3a1;">나빠서  21.8%  →  누적 65.0%</span>
<span style="color:#a6e3a1;">맑아서  15.1%  →  누적 80.1%</span>
<span style="color:#a6e3a1;">흐려서   9.4%  →  누적 89.5%</span>
<span style="color:#f9e2af; font-weight:900;">춥고     6.3%  →  누적 95.8%  ← 여기서 90% 초과! 멈춤</span>

<span style="color:#89dceb;">→ 상위 5개 단어 안에서 확률에 따라 선택</span></div>
</div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px;">
<div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:6px;">🔄 Top-k와의 차이</div>
<div style="font-size:13px; color:#334155; line-height:1.7;">
Top-k는 항상 k개 고정. Top-p는 상황에 따라 후보 개수가 달라짐<br>
(한 단어가 99% 확률이면 그것 하나만, 골고루 퍼져있으면 여러 개 포함)
</div>
</div>

</div>

<br>

<!-- 실제 서비스 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🧩 실제 ChatGPT, Claude는 어떤 전략을 쓸까?</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">실제 서비스들은 이 전략들을 <b>조합해서</b> 사용합니다.</p>

<div style="background-color: #1e1e2e; border-radius: 14px; padding: 16px 20px; font-family:'JetBrains Mono','Consolas',monospace; font-size: 13px; line-height: 2.4; margin: 14px 0; text-align:center; overflow-x:auto; white-space:pre;"><span style="color:#89dceb;">Temperature 조절</span>
    <span style="color:#6c7086;">+</span> <span style="color:#f9e2af;">Top-p Sampling</span>
    <span style="color:#6c7086;">+</span> <span style="color:#cba6f7;">(때로는 반복 패널티: 이미 나온 단어에 불이익)</span>
    <span style="color:#6c7086;">=</span> <span style="color:#a6e3a1; font-weight:900;">자연스럽고 다양하면서도 이상하지 않은 문장 생성</span></div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 사용자가 설정을 바꾸면 같은 질문에도 다른 스타일의 답변이 나오는 이유입니다.
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;"><span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리</div>
<div style="display: grid; gap: 8px;">
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;"><b style="color:#FF6B00;">Greedy</b>: 매번 1등만 → 안정적이지만 단조로움</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;"><b style="color:#FF6B00;">Temperature</b>: 확률 분포 날카로움 조절 → 낮으면 보수적, 높으면 창의적</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;"><b style="color:#FF6B00;">Top-k</b>: 상위 k개 후보 안에서 랜덤 → 황당한 단어 차단</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;"><b style="color:#FF6B00;">Top-p</b>: 누적 확률 p%까지 후보 수집 → 상황에 따라 후보 수 자동 조절</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">실제 서비스는 이 전략들을 <b style="color:#FF6B00;">조합해서</b> 사용합니다.</div>
</div>
</div>

</div>