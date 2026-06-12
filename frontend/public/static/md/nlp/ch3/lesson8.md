<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
단어 빈도 기반 표현
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
단어 빈도 기반 표현의
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">세 가지 한계</span>
와 지금까지 배운 표현 방법을 비교합니다.
</p>

</div>

<br>

<!-- 한계 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
⚠️ 단어 빈도 기반 표현의 한계
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
단어 빈도 기반 표현은 원-핫 인코딩보다 훨씬 유용하지만, 여전히 한계가 있습니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<!-- 한계 1 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 1. 순서 정보를 잃어버린다</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 12px;">
    <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; line-height:1.8; text-align:center;">
      "나는 고양이를 좋아한다"
    </div>
    <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; line-height:1.8; text-align:center;">
      "고양이는 나를 좋아한다"
    </div>
  </div>

  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.7;">
    등장하는 단어는 같지만, <b style="color:#FF6B00;">의미는 완전히 다릅니다.</b><br>
    하지만 BoW/TF-IDF로 표현하면 두 문장이 <b>똑같이</b> 나옵니다!
  </div>
</div>

<!-- 한계 2 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 2. 단어 의미를 여전히 모른다</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 12px;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.7;">
      <b style="color:#FF6B00;">"기쁘다"</b>와 <b style="color:#FF6B00;">"행복하다"</b><br>
      → 비슷한 의미지만, <b>다른 단어로 취급</b>됩니다.
    </div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.7;">
      <b style="color:#FF6B00;">"배"(과일)</b>와 <b style="color:#FF6B00;">"배"(신체)</b><br>
      → 같은 단어지만, 의미가 다릅니다. <b>구분 불가.</b>
    </div>
  </div>
</div>

<!-- 한계 3 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 3. 여전히 희소 벡터 문제가 있다</div>

  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.7; margin-bottom: 12px;">
    단어 사전이 수만 개 이상이면, <b style="color:#FF6B00;">대부분의 값이 0인 매우 긴 벡터</b>가 생깁니다.
  </div>

  <div style="background-color: #fff3eb; border: 1px solid #ffd0b0; padding: 13px 16px; border-radius: 10px; font-size: 14px; color: #334155; line-height: 1.8;">
    <span style="color: #FF6B00; font-weight: 900;">💡</span> 이런 한계들을 해결하기 위해 나중에 <b style="color:#FF6B00;">단어 임베딩(Word Embedding)</b>이 등장합니다.
  </div>
</div>

</div>
</div>

<br>

<!-- 비교 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 지금까지 배운 표현 방법 비교
</h2>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <!-- 헤더 -->
  <div style="display:grid; grid-template-columns:140px 1fr 100px 100px 120px; gap:8px; align-items:center;">
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">방법</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">원리</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">의미 반영</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">순서 반영</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">벡터 크기</div>
  </div>

  <!-- 원-핫 -->
  <div style="display:grid; grid-template-columns:140px 1fr 100px 100px 120px; gap:8px; align-items:center;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; text-align:center;">원-핫 인코딩</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155;">해당 위치만 1</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; font-weight:900; text-align:center;">❌</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; font-weight:900; text-align:center;">❌</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:12px; color:#334155; text-align:center;">단어 사전 크기</div>
  </div>

  <!-- BoW -->
  <div style="display:grid; grid-template-columns:140px 1fr 100px 100px 120px; gap:8px; align-items:center;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; text-align:center;">BoW</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155;">등장 횟수 기록</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; font-weight:900; text-align:center;">❌</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; font-weight:900; text-align:center;">❌</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:12px; color:#334155; text-align:center;">단어 사전 크기</div>
  </div>

  <!-- TF-IDF -->
  <div style="display:grid; grid-template-columns:140px 1fr 100px 100px 120px; gap:8px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#1681c4; text-align:center;">TF-IDF</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; color:#334155;">빈도 + 중요도 가중치</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; color:#1681c4; font-weight:900; text-align:center;">🔺 일부</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 12px; border-radius:10px; font-size:13px; color:#FF6B00; font-weight:900; text-align:center;">❌</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:12px; color:#334155; text-align:center;">단어 사전 크기</div>
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
    단어 빈도 기반 표현은 <b style="color:#FF6B00;">"단어가 얼마나 자주 나오는지"를 숫자로</b> 표현하는 방법입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    대표적인 방법으로 <b style="color:#FF6B00;">BoW(단순 빈도)</b>와 <b style="color:#FF6B00;">TF-IDF(빈도 + 중요도)</b>가 있습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    결과는 <b style="color:#FF6B00;">문서-단어 행렬(DTM)</b> 형태로 나타납니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    단어의 순서나 의미를 담지 못하는 한계가 있지만, <b style="color:#FF6B00;">문서 분류·검색</b> 등 실용적인 분야에 여전히 많이 쓰입니다.
  </div>
</div>

</div>

</div>