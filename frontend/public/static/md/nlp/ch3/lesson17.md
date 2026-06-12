<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
단어 임베딩 (Word Embedding)
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
단어 임베딩의
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">두 가지 한계</span>
와 지금까지 배운 모든 표현 방법을 총정리합니다.
</p>

</div>

<br>

<!-- 한계 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
⚠️ 단어 임베딩의 한계
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
단어 임베딩도 완벽하지 않습니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<!-- 한계 1 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 1. 같은 단어, 다른 의미를 구분 못 한다</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 12px;">
    <div style="background:#0f172a; border-radius:10px; padding:10px 12px; font-family:Consolas, monospace; font-size:12px; color:#a6e3a1; text-align:center; line-height:1.8;">
      "나는 <span style="color:#ff5f57; font-weight:900;">배</span>가 고프다"<br>
      <span style="color:#6c7086;">→ 배 (신체)</span>
    </div>
    <div style="background:#0f172a; border-radius:10px; padding:10px 12px; font-family:Consolas, monospace; font-size:12px; color:#a6e3a1; text-align:center; line-height:1.8;">
      "<span style="color:#ff5f57; font-weight:900;">배</span>를 타고 바다로"<br>
      <span style="color:#6c7086;">→ 배 (선박)</span>
    </div>
    <div style="background:#0f172a; border-radius:10px; padding:10px 12px; font-family:Consolas, monospace; font-size:12px; color:#a6e3a1; text-align:center; line-height:1.8;">
      "<span style="color:#ff5f57; font-weight:900;">배</span>나무 과일이 맛있다"<br>
      <span style="color:#6c7086;">→ 배 (과일)</span>
    </div>
  </div>

  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7; margin-bottom:10px;">
    Word2Vec은 "배"에 대해 <b style="color:#FF6B00;">하나의 벡터</b>만 만듭니다.<br>
    세 가지 의미의 평균쯤 되는 벡터가 됩니다.
  </div>

  <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    <span style="color:#FF6B00; font-weight:900;">💡</span> 이 한계는 다음에 배울 <b style="color:#FF6B00;">문장 임베딩(BERT 등)</b>에서 해결됩니다.<br>
    문장 전체 맥락을 보고 단어의 의미를 결정하기 때문입니다.
  </div>
</div>

<!-- 한계 2 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">한계 2. 모르는 단어(OOV)를 처리 못 한다</div>

  <div style="background:#1e1e2e; border-radius:10px; padding:11px 16px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:1.9; margin-bottom:12px;">
    <span style="color:#ff5f57;">"치킨런닝", "갓생"</span> 같은 신조어 → Word2Vec 모델에 없을 수 있음
  </div>

  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    <span style="color:#FF6B00; font-weight:900;">💡</span> <b>FastText</b>는 단어를 글자 단위로 쪼개서 이 문제를 일부 해결합니다.
  </div>
</div>

</div>
</div>

<br>

<!-- 총정리 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 지금까지 배운 표현 방법 총정리
</h2>

<div style="display: grid; gap: 8px; margin-top: 16px;">

  <!-- 헤더 -->
  <div style="display:grid; grid-template-columns:140px 1fr 80px 80px 80px; gap:8px;">
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">방법</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">벡터 크기</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 10px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">의미 반영</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 10px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">문맥 반영</div>
    <div style="background:#0f172a; color:#c3e88d; padding:9px 10px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">계산 비용</div>
  </div>

  <!-- 원-핫 -->
  <div style="display:grid; grid-template-columns:140px 1fr 80px 80px 80px; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; display:flex; align-items:center; justify-content:center; text-align:center;">원-핫 인코딩</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:12px; color:#334155; display:flex; align-items:center;">단어 사전 크기</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 10px; border-radius:10px; font-size:13px; color:#FF6B00; font-weight:900; display:flex; align-items:center; justify-content:center;">❌</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 10px; border-radius:10px; font-size:13px; color:#FF6B00; font-weight:900; display:flex; align-items:center; justify-content:center;">❌</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 10px; border-radius:10px; font-size:11px; color:#334155; display:flex; align-items:center; justify-content:center; text-align:center;">매우 낮음</div>
  </div>

  <!-- BoW -->
  <div style="display:grid; grid-template-columns:140px 1fr 80px 80px 80px; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; display:flex; align-items:center; justify-content:center;">BoW</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:12px; color:#334155; display:flex; align-items:center;">단어 사전 크기</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 10px; border-radius:10px; font-size:13px; color:#FF6B00; font-weight:900; display:flex; align-items:center; justify-content:center;">❌</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 10px; border-radius:10px; font-size:13px; color:#FF6B00; font-weight:900; display:flex; align-items:center; justify-content:center;">❌</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 10px; border-radius:10px; font-size:11px; color:#334155; display:flex; align-items:center; justify-content:center; text-align:center;">낮음</div>
  </div>

  <!-- TF-IDF -->
  <div style="display:grid; grid-template-columns:140px 1fr 80px 80px 80px; gap:8px; align-items:stretch;">
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#0f172a; display:flex; align-items:center; justify-content:center;">TF-IDF</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 12px; border-radius:10px; font-size:12px; color:#334155; display:flex; align-items:center;">단어 사전 크기</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 10px; border-radius:10px; font-size:12px; color:#1681c4; font-weight:900; display:flex; align-items:center; justify-content:center;">🔺 일부</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 10px; border-radius:10px; font-size:13px; color:#FF6B00; font-weight:900; display:flex; align-items:center; justify-content:center;">❌</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 10px; border-radius:10px; font-size:11px; color:#334155; display:flex; align-items:center; justify-content:center; text-align:center;">낮음</div>
  </div>

  <!-- 단어 임베딩 -->
  <div style="display:grid; grid-template-columns:140px 1fr 80px 80px 80px; gap:8px; align-items:stretch;">
    <div style="background:#eef7ff; border:2px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#1681c4; display:flex; align-items:center; justify-content:center; text-align:center;">단어 임베딩</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 12px; border-radius:10px; font-size:12px; color:#334155; display:flex; align-items:center;">고정 (50~300)</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; padding:9px 10px; border-radius:10px; font-size:13px; color:#1681c4; font-weight:900; display:flex; align-items:center; justify-content:center;">✅</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; padding:9px 10px; border-radius:10px; font-size:13px; color:#FF6B00; font-weight:900; display:flex; align-items:center; justify-content:center;">❌</div>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:9px 10px; border-radius:10px; font-size:11px; color:#334155; display:flex; align-items:center; justify-content:center; text-align:center;">중간</div>
  </div>

  <!-- 문장 임베딩 -->
  <div style="display:grid; grid-template-columns:140px 1fr 80px 80px 80px; gap:8px; align-items:stretch;">
    <div style="background:#0f172a; border:2px solid #0f172a; padding:9px 12px; border-radius:10px; font-size:13px; font-weight:900; color:#c3e88d; display:flex; align-items:center; justify-content:center; text-align:center;">문장 임베딩</div>
    <div style="background:#0f172a; border:1px solid #0f172a; padding:9px 12px; border-radius:10px; font-size:12px; color:#c3e88d; display:flex; align-items:center;">고정 (768~)</div>
    <div style="background:#0f172a; border:1px solid #0f172a; padding:9px 10px; border-radius:10px; font-size:13px; color:#a6e3a1; font-weight:900; display:flex; align-items:center; justify-content:center;">✅</div>
    <div style="background:#0f172a; border:1px solid #0f172a; padding:9px 10px; border-radius:10px; font-size:13px; color:#a6e3a1; font-weight:900; display:flex; align-items:center; justify-content:center;">✅</div>
    <div style="background:#0f172a; border:1px solid #0f172a; padding:9px 10px; border-radius:10px; font-size:11px; color:#c3e88d; display:flex; align-items:center; justify-content:center; text-align:center;">높음</div>
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
    <b style="color:#FF6B00;">단어 임베딩</b>은 단어의 <b style="color:#FF6B00;">의미를 숫자 공간에 담는</b> 방법입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    비슷한 의미의 단어는 공간에서 <b style="color:#FF6B00;">가까이, 다른 의미는 멀리</b> 배치됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    대표 방법인 <b style="color:#FF6B00;">Word2Vec</b>은 "주변에 같이 등장하는 단어끼리 비슷한 벡터를 갖는다"는 원리로 학습합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">"왕 - 남자 + 여자 = 여왕"</b> 같은 의미 계산이 가능해집니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    같은 단어의 다른 의미를 구분하지 못하는 한계는 <b style="color:#FF6B00;">문장 임베딩(BERT 등)</b>으로 해결합니다.
  </div>
</div>

</div>

</div>