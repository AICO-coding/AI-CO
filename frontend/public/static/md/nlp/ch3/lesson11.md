<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Bag of Words (BoW)
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
BoW의
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">세 가지 한계</span>
와 실전에서 자주 쓰는 <b style="color:#1681c4;">CountVectorizer 파라미터</b>를 정리합니다.
</p>

</div>

<br>

<!-- 한계 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
⚠️ BoW의 한계
</h2>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<!-- 한계 1 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 1. 단어 순서를 무시한다</div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:12px;">
    <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; text-align:center; line-height:1.8;">
      "나는 고양이를 좋아한다"
    </div>
    <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; text-align:center; line-height:1.8;">
      "고양이는 나를 좋아한다"
    </div>
  </div>
  <div style="background:#1e1e2e; border-radius:10px; padding:11px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">문장 1 → </span><span style="color:#89dceb;">[나는:1, 고양이를:1, 좋아한다:1]</span>
<span style="color:#6c7086;">문장 2 → </span><span style="color:#89dceb;">[나는:1, 고양이를:1, 좋아한다:1]</span>  <span style="color:#ff5f57;">← 벡터 동일!</span></div>
  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    두 문장의 주체와 객체가 다르지만, BoW로는 <b style="color:#FF6B00;">완전히 같은 벡터</b>가 나옵니다.
  </div>
</div>

<!-- 한계 2 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 2. 흔한 단어가 중요한 단어처럼 보인다</div>
  <div style="background:#1e1e2e; border-radius:10px; padding:11px 16px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:1.9; margin-bottom:12px;">
    <span style="color:#ff5f57;">"은", "는", "이", "가", "을"</span> 같은 조사(불용어)가<br>
    전처리에서 제거되지 않으면 빈도가 매우 높게 나옵니다.
  </div>
  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    <span style="color:#FF6B00; font-weight:900;">💡</span> 불용어를 충분히 제거해야 BoW가 제대로 작동합니다.<br>
    <span style="color:#94a3b8; font-size:13px;">(챕터 2. 텍스트 전처리 — 불용어 제거 참고)</span>
  </div>
</div>

<!-- 한계 3 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 3. "자주 나온다 = 중요하다"가 항상 옳지 않다</div>
  <div style="background:#1e1e2e; border-radius:10px; padding:11px 16px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:1.9; margin-bottom:12px;">
    <span style="color:#ff5f57;">"이다", "있다", "하다"</span> 같은 단어는 모든 문서에서 자주 나오지만,<br>
    특정 문서를 특징짓는 중요한 단어가 아닙니다.
  </div>
  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    <span style="color:#FF6B00; font-weight:900;">💡</span> 이 문제를 해결하는 것이 다음에 배울 <b style="color:#FF6B00;">TF-IDF</b>입니다!
  </div>
</div>

</div>
</div>

<br>

<!-- CountVectorizer 파라미터 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 CountVectorizer 주요 파라미터
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
실제 사용 시 자주 쓰는 옵션들입니다.
</p>

<!-- 파라미터 코드 -->
<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">CountVectorizer 파라미터 예시</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#cdd6f4;">vectorizer = CountVectorizer(</span>
<span style="color:#cdd6f4;">    max_features=</span><span style="color:#89dceb;">1000</span><span style="color:#cdd6f4;">,      </span><span style="color:#6c7086;"># 자주 등장하는 상위 1000개 단어만 사용</span>
<span style="color:#cdd6f4;">    min_df=</span><span style="color:#89dceb;">2</span><span style="color:#cdd6f4;">,               </span><span style="color:#6c7086;"># 최소 2개 문서에 등장한 단어만 포함</span>
<span style="color:#cdd6f4;">    max_df=</span><span style="color:#89dceb;">0.9</span><span style="color:#cdd6f4;">,             </span><span style="color:#6c7086;"># 전체 90% 이상 문서에 등장하는 단어 제외</span>
<span style="color:#cdd6f4;">    stop_words=[</span><span style="color:#a6e3a1;">'나는'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'을'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'를'</span><span style="color:#cdd6f4;">],  </span><span style="color:#6c7086;"># 제거할 불용어 지정</span>
<span style="color:#cdd6f4;">    ngram_range=(</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">, </span><span style="color:#89dceb;">2</span><span style="color:#cdd6f4;">),     </span><span style="color:#6c7086;"># 단어 1개 + 2개 연속 단어쌍도 포함</span>
<span style="color:#cdd6f4;">)</span></div>
</div>

<!-- 파라미터 설명 카드 -->
<div style="display: grid; gap: 10px;">

  <div style="display:grid; grid-template-columns:140px 1fr 1fr; gap:10px; align-items:center;">
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">파라미터</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">역할</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">활용 예</div>
  </div>

  <div style="display:grid; grid-template-columns:140px 1fr 1fr; gap:10px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-family:Consolas, monospace; font-size:12px; font-weight:900; color:#1681c4; text-align:center;">max_features</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155;">사용할 단어 수 제한</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155;">너무 많은 단어 → 상위 N개만</div>
  </div>

  <div style="display:grid; grid-template-columns:140px 1fr 1fr; gap:10px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-family:Consolas, monospace; font-size:12px; font-weight:900; color:#1681c4; text-align:center;">min_df</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155;">희귀 단어 제거</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155;">오타, 신조어 등 제거</div>
  </div>

  <div style="display:grid; grid-template-columns:140px 1fr 1fr; gap:10px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-family:Consolas, monospace; font-size:12px; font-weight:900; color:#1681c4; text-align:center;">max_df</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155;">너무 흔한 단어 제거</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155;">자동 불용어 처리</div>
  </div>

  <div style="display:grid; grid-template-columns:140px 1fr 1fr; gap:10px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-family:Consolas, monospace; font-size:12px; font-weight:900; color:#1681c4; text-align:center;">ngram_range</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155;">연속 단어 묶음 포함</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155;">"인공 지능"을 하나의 단위로</div>
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
    BoW는 <b style="color:#FF6B00;">단어의 등장 횟수를 세어 문서를 벡터로 표현</b>하는 방법입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    단어의 순서는 무시하고, <b style="color:#FF6B00;">어떤 단어가 몇 번 나왔는지</b>만 기록합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">CountVectorizer</b>를 이용해 쉽게 구현할 수 있습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    벡터로 변환된 문서는 <b style="color:#FF6B00;">코사인 유사도</b> 등으로 수학적 비교가 가능합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    단어 순서 무시, 흔한 단어 문제가 있어 <b style="color:#FF6B00;">TF-IDF로 개선</b>할 수 있습니다.
  </div>
</div>

</div>

</div>