<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
원-핫 인코딩 (One-Hot Encoding)
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
원-핫 인코딩의
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">치명적인 한계 두 가지</span>
와 전체 요약을 정리합니다.
</p>

</div>

<br>

<!-- 한계 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
⚠️ 원-핫 인코딩의 한계
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
원-핫 인코딩은 단순하지만 <b style="color:#FF6B00;">치명적인 단점 두 가지</b>가 있습니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<!-- 한계 1 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 1. 단어 사전이 커질수록 벡터가 너무 커진다</div>

  <div style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">단어 사전 크기 10개   →</span> <span style="color:#ff5f57;">벡터 길이 10</span>
<span style="color:#6c7086;">단어 사전 크기 1만개  →</span> <span style="color:#ff5f57;">벡터 길이 10,000</span>
<span style="color:#6c7086;">단어 사전 크기 10만개 →</span> <span style="color:#ff5f57;">벡터 길이 100,000</span></div>

  <p style="margin: 0 0 12px 0; font-size:14px; color:#334155; line-height:1.8;">
    실제 한국어 단어 수는 수십만 개이기 때문에, 벡터 하나가 수십만 개의 숫자로 이루어집니다.<br>
    그 대부분이 0이라서 <b style="color:#FF6B00;">메모리 낭비</b>가 심합니다.
  </p>

  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.7;">
    <span style="color:#FF6B00; font-weight:900;">📌 희소 벡터(Sparse Vector)</span><br>
    이렇게 대부분이 0으로 채워진 벡터를 <b>희소 벡터(Sparse Vector)</b>라고 합니다.
  </div>
</div>

<!-- 한계 2 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 2. 단어 간의 의미 관계를 담지 못한다</div>

  <div style="background:#0f172a; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"강아지"</span> = <span style="color:#89dceb;">[1, 0, 0, 0, 0, ...]</span>
<span style="color:#a6e3a1;">"개"</span>     = <span style="color:#89dceb;">[0, 1, 0, 0, 0, ...]</span>
<span style="color:#a6e3a1;">"고양이"</span> = <span style="color:#89dceb;">[0, 0, 1, 0, 0, ...]</span></div>

  <p style="margin: 0 0 12px 0; font-size:14px; color:#334155; line-height:1.8;">
    원-핫 벡터로는 <b style="color:#FF6B00;">"강아지"</b>와 <b style="color:#FF6B00;">"개"</b>가 비슷한 단어인지,<br>
    <b style="color:#FF6B00;">"강아지"</b>와 <b style="color:#FF6B00;">"고양이"</b>가 비슷한 단어인지 <b>전혀 알 수 없습니다.</b><br>
    모든 단어 간의 거리가 똑같이 측정됩니다.
  </p>

  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.7;">
    <span style="color:#FF6B00; font-weight:900;">📐 코사인 유사도로 확인하면</span><br>
    두 벡터의 유사도를 측정하는 코사인 유사도를 사용하면,<br>
    어떤 두 단어를 비교해도 항상 <b>0 (완전히 다름)</b>이 나옵니다.
  </div>
</div>

</div>
</div>

<br>

<!-- 요약 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 원-핫 인코딩 요약
</h2>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="display:grid; grid-template-columns:130px 1fr; gap:12px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:9px 12px; font-size:13px; font-weight:900; color:#1681c4; text-align:center;">원리</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:9px 14px; font-size:14px; color:#334155;">해당 단어 위치만 1, 나머지는 0</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr; gap:12px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:9px 12px; font-size:13px; font-weight:900; color:#1681c4; text-align:center;">벡터 크기</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:9px 14px; font-size:14px; color:#334155;">단어 사전 크기와 동일</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr; gap:12px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:9px 12px; font-size:13px; font-weight:900; color:#1681c4; text-align:center;">의미 반영</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:9px 14px; font-size:14px; color:#FF6B00; font-weight:900;">❌ 불가능</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr; gap:12px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:9px 12px; font-size:13px; font-weight:900; color:#1681c4; text-align:center;">구현 난이도</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:9px 14px; font-size:14px; color:#334155;">⭐ 매우 쉬움</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr; gap:12px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:9px 12px; font-size:13px; font-weight:900; color:#1681c4; text-align:center;">주요 문제</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:9px 14px; font-size:14px; color:#FF6B00;">희소 벡터, 의미 유사성 표현 불가</div>
  </div>

  <div style="display:grid; grid-template-columns:130px 1fr; gap:12px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:9px 12px; font-size:13px; font-weight:900; color:#1681c4; text-align:center;">현재 활용</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:9px 14px; font-size:14px; color:#334155;">분류 모델의 레이블 표현 등 제한적 사용</div>
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
    원-핫 인코딩은 단어 위치만 1, 나머지는 0으로 표현하는 <b style="color:#FF6B00;">가장 단순한 텍스트 표현 방법</b>입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이해하기 쉽고 구현이 간단하지만, <b style="color:#FF6B00;">단어 수가 많아지면 벡터가 지나치게 커지는 문제</b>가 있습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    "강아지"와 "개"처럼 <b style="color:#FF6B00;">비슷한 단어 사이의 관계를 전혀 표현하지 못합니다.</b>
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이 한계를 극복하기 위해 <b style="color:#FF6B00;">BoW, TF-IDF, 단어 임베딩</b> 등이 등장합니다.
  </div>
</div>

</div>

</div>