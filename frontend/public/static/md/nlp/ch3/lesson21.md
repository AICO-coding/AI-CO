<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
텍스트 표현 방식 비교
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
지금까지 배운
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">5가지 표현 방법</span>
을 같은 예시 문장으로 직접 비교하며 정리합니다.
</p>

</div>

<br>

<!-- 챕터 되돌아보기 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🗺️ 챕터 3 전체 되돌아보기
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
우리는 지금까지 텍스트를 숫자로 바꾸는 방법을 4단계로 배웠습니다.
</p>

<div style="display: grid; gap: 8px; margin-top: 16px;">

  <div style="display:grid; grid-template-columns:60px 1fr auto; gap:12px; align-items:center; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px;">
    <div style="background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">1단계</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:4px;">원-핫 인코딩 (One-Hot Encoding)</div>
      <div style="font-size:13px; color:#475569; line-height:1.6;">해당 단어 위치만 1, 나머지는 0</div>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:60px 1fr auto; gap:12px; align-items:center; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px;">
    <div style="background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">2단계</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:4px;">단어 빈도 기반 표현 (BoW / TF-IDF)</div>
      <div style="font-size:13px; color:#475569; line-height:1.6;">단어가 얼마나 자주 나왔는지 기록 · TF-IDF는 중요도 가중치까지 추가</div>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:60px 1fr auto; gap:12px; align-items:center; background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px;">
    <div style="background:#1681c4; color:#fff; padding:6px 10px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">3단계</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:4px;">단어 임베딩 (Word2Vec 등)</div>
      <div style="font-size:13px; color:#475569; line-height:1.6;">단어의 의미를 담은 밀집 벡터로 표현 · 비슷한 단어는 비슷한 벡터</div>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:60px 1fr auto; gap:12px; align-items:center; background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px;">
    <div style="background:#1681c4; color:#fff; padding:6px 10px; border-radius:10px; font-size:12px; font-weight:900; text-align:center;">4단계</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:4px;">문장 임베딩 (BERT 등)</div>
      <div style="font-size:13px; color:#475569; line-height:1.6;">문장 전체를 하나의 벡터로 · 문맥까지 반영한 가장 강력한 표현</div>
    </div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌</span> 이 섹션에서는 네 가지 방법을 <b>같은 예시 문장으로 직접 비교</b>하며 정리합니다.
</div>

</div>

<br>

<!-- 비교 기준 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📋 비교 기준 정리
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
같은 문장 4개로 모든 방법을 비교합니다.
</p>

<div style="background-color: #0f172a; border-radius: 14px; padding: 14px 20px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; line-height: 2.2; margin-top: 14px;">
  <span style="color:#6c7086;">문서 1: </span><span style="color:#a6e3a1;">"나는 밥을 먹었다"</span><br>
  <span style="color:#6c7086;">문서 2: </span><span style="color:#a6e3a1;">"나는 물을 마셨다"</span><br>
  <span style="color:#6c7086;">문서 3: </span><span style="color:#a6e3a1;">"고양이가 밥을 먹었다"</span><br>
  <span style="color:#6c7086;">문서 4: </span><span style="color:#a6e3a1;">"고양이가 물을 마셨다"</span>
</div>

</div>

<br>

<!-- 방법별 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
방법별 표현 결과 비교
</h2>

<div style="display: grid; gap: 14px; margin-top: 4px;">

<!-- 1️⃣ 원-핫 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#0f172a; color:#c3e88d; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900;">1️⃣ 원-핫 인코딩</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:12px; line-height:2.2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">단어 사전: [고양이가(0), 나는(1), 마셨다(2), 먹었다(3), 밥을(4), 물을(5)]</span>

<span style="color:#a6e3a1;">"밥을"</span>   → <span style="color:#89dceb;">[0, 0, 0, 0, </span><span style="color:#ff5f57; font-weight:900;">1</span><span style="color:#89dceb;">, 0]</span>  <span style="color:#6c7086;">← 밥을 위치(4번)만 1</span>
<span style="color:#a6e3a1;">"먹었다"</span> → <span style="color:#89dceb;">[0, 0, 0, </span><span style="color:#ff5f57; font-weight:900;">1</span><span style="color:#89dceb;">, 0, 0]</span> <span style="color:#6c7086;">← 먹었다 위치(3번)만 1</span></div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:9px 12px; font-size:13px; color:#334155; line-height:1.6;">✅ 구현 단순, 이해 쉬움</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:8px; padding:9px 12px; font-size:13px; color:#334155; line-height:1.6;">❌ 단어 의미 없음 · 벡터가 무한정 커짐 · 관계 파악 불가</div>
  </div>
</div>

<!-- 2️⃣ BoW -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900;">2️⃣ Bag of Words</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:12px; line-height:2.2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">단어 사전: [고양이가, 나는, 마셨다, 먹었다, 밥을, 물을]</span>

<span style="color:#a6e3a1;">문서1 "나는 밥을 먹었다"    </span>→ <span style="color:#89dceb;">[0, </span><span style="color:#ff5f57;">1</span><span style="color:#89dceb;">, 0, </span><span style="color:#ff5f57;">1</span><span style="color:#89dceb;">, </span><span style="color:#ff5f57;">1</span><span style="color:#89dceb;">, 0]</span>
<span style="color:#a6e3a1;">문서2 "나는 물을 마셨다"    </span>→ <span style="color:#89dceb;">[0, </span><span style="color:#ff5f57;">1</span><span style="color:#89dceb;">, </span><span style="color:#ff5f57;">1</span><span style="color:#89dceb;">, 0, 0, </span><span style="color:#ff5f57;">1</span><span style="color:#89dceb;">]</span>
<span style="color:#a6e3a1;">문서3 "고양이가 밥을 먹었다"</span>→ <span style="color:#89dceb;">[</span><span style="color:#ff5f57;">1</span><span style="color:#89dceb;">, 0, 0, </span><span style="color:#ff5f57;">1</span><span style="color:#89dceb;">, </span><span style="color:#ff5f57;">1</span><span style="color:#89dceb;">, 0]</span></div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:9px 12px; font-size:13px; color:#334155; line-height:1.6;">✅ 문서 단위 표현 가능 · 문서 간 비교 가능</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:8px; padding:9px 12px; font-size:13px; color:#334155; line-height:1.6;">❌ 단어 순서 무시 · 핵심/범용 단어 구별 못 함</div>
  </div>
</div>

<!-- 3️⃣ TF-IDF -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900;">3️⃣ TF-IDF</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:12px; line-height:2.2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">단어 사전: [고양이가, 나는, 마셨다, 먹었다, 밥을, 물을]</span>

<span style="color:#a6e3a1;">문서1 "나는 밥을 먹었다"    </span>→ <span style="color:#89dceb;">[0.000, 0.579, 0.000, 0.579, 0.579, 0.000]</span>
<span style="color:#a6e3a1;">문서2 "나는 물을 마셨다"    </span>→ <span style="color:#89dceb;">[0.000, 0.579, 0.579, 0.000, 0.000, 0.579]</span>
<span style="color:#a6e3a1;">문서3 "고양이가 밥을 먹었다"</span>→ <span style="color:#89dceb;">[0.579, 0.000, 0.000, 0.579, 0.579, 0.000]</span></div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:9px 12px; font-size:13px; color:#334155; line-height:1.6;">✅ BoW보다 의미 있는 단어에 높은 가중치 · 실무에서 여전히 많이 사용</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:8px; padding:9px 12px; font-size:13px; color:#334155; line-height:1.6;">❌ 단어 순서 무시 · 의미 유사성 표현 불가</div>
  </div>
</div>

<!-- 4️⃣ 단어 임베딩 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900;">4️⃣ 단어 임베딩 (Word2Vec)</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:12px; line-height:2.2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"밥을"</span>   → <span style="color:#89dceb;">[ 0.24, -0.13,  0.87,  0.45, ...]</span>  <span style="color:#6c7086;">← 음식 관련 방향</span>
<span style="color:#a6e3a1;">"먹었다"</span> → <span style="color:#89dceb;">[ 0.31, -0.09,  0.79,  0.38, ...]</span>  <span style="color:#6c7086;">← 행동 관련 방향</span>
<span style="color:#a6e3a1;">"마셨다"</span> → <span style="color:#89dceb;">[ 0.28, -0.11,  0.81,  0.41, ...]</span>  <span style="color:#ff5f57;">← "먹었다"와 유사한 벡터!</span>
<span style="color:#a6e3a1;">"자동차"</span> → <span style="color:#89dceb;">[-0.72,  0.65, -0.33, -0.21, ...]</span> <span style="color:#6c7086;">← 완전히 다른 방향</span></div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:8px; padding:9px 12px; font-size:13px; color:#334155; line-height:1.6;">✅ 유사한 단어끼리 비슷한 벡터 · 의미 관계 담김 · 희소 벡터 문제 해결</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:8px; padding:9px 12px; font-size:13px; color:#334155; line-height:1.6;">❌ 단어 순서·문맥 무시 · 동음이의어 구분 불가</div>
  </div>
</div>

<!-- 5️⃣ 문장 임베딩 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#0f172a; color:#c3e88d; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900;">5️⃣ 문장 임베딩 (BERT)</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:12px; line-height:2.2; margin-bottom:12px; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"나는 배가 고프다"</span>  → <span style="color:#89dceb;">[ 0.12, -0.34,  0.78,  0.23, ...]</span>  <span style="color:#ff5f57;">← "배"=신체 기관 반영</span>
<span style="color:#a6e3a1;">"배를 타고 떠났다"</span>  → <span style="color:#89dceb;">[-0.45,  0.67, -0.12,  0.89, ...]</span>  <span style="color:#ff5f57;">← "배"=선박 반영</span></div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:8px; padding:9px 12px; font-size:13px; color:#334155; line-height:1.6;">✅ 문장 전체 의미를 하나의 벡터로 · 문맥에 따라 동음이의어 구분 · 가장 강력한 표현</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:8px; padding:9px 12px; font-size:13px; color:#334155; line-height:1.6;">❌ 계산 비용 높음 · 모델 크기 큼 · 설명 어려움 (블랙박스)</div>
  </div>
</div>

</div>
</div>

<br>

<!-- 전체 비교표 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 전체 비교표
</h2>

<div style="overflow-x: auto; margin-top: 16px;">
<table style="width:100%; border-collapse:collapse; font-size:13px; text-align:center; min-width:640px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 12px; text-align:left; border-radius:10px 0 0 0; font-weight:900;">항목</th>
      <th style="padding:10px 8px; font-weight:900;">원-핫</th>
      <th style="padding:10px 8px; font-weight:900;">BoW</th>
      <th style="padding:10px 8px; font-weight:900;">TF-IDF</th>
      <th style="padding:10px 8px; font-weight:900;">단어 임베딩</th>
      <th style="padding:10px 8px; border-radius:0 10px 0 0; font-weight:900;">문장 임베딩</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f8fafc;">
      <td style="padding:9px 12px; font-weight:900; color:#0f172a; text-align:left;">표현 단위</td>
      <td style="padding:9px 8px; color:#475569;">단어</td>
      <td style="padding:9px 8px; color:#475569;">문서</td>
      <td style="padding:9px 8px; color:#475569;">문서</td>
      <td style="padding:9px 8px; color:#475569;">단어</td>
      <td style="padding:9px 8px; color:#1681c4; font-weight:900;">문장</td>
    </tr>
    <tr style="background:#ffffff;">
      <td style="padding:9px 12px; font-weight:900; color:#0f172a; text-align:left;">벡터 크기</td>
      <td style="padding:9px 8px; color:#FF6B00; font-size:12px;">단어 사전 수</td>
      <td style="padding:9px 8px; color:#FF6B00; font-size:12px;">단어 사전 수</td>
      <td style="padding:9px 8px; color:#FF6B00; font-size:12px;">단어 사전 수</td>
      <td style="padding:9px 8px; color:#1681c4; font-weight:900;">50~300</td>
      <td style="padding:9px 8px; color:#1681c4; font-weight:900;">768~1024</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:9px 12px; font-weight:900; color:#0f172a; text-align:left;">벡터 유형</td>
      <td style="padding:9px 8px; color:#FF6B00;">희소</td>
      <td style="padding:9px 8px; color:#FF6B00;">희소</td>
      <td style="padding:9px 8px; color:#FF6B00;">희소</td>
      <td style="padding:9px 8px; color:#1681c4; font-weight:900;">밀집</td>
      <td style="padding:9px 8px; color:#1681c4; font-weight:900;">밀집</td>
    </tr>
    <tr style="background:#ffffff;">
      <td style="padding:9px 12px; font-weight:900; color:#0f172a; text-align:left;">의미 반영</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#1681c4; font-weight:900;">🔺</td>
      <td style="padding:9px 8px; color:#1681c4; font-weight:900;">✅</td>
      <td style="padding:9px 8px; color:#1681c4; font-weight:900;">✅</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:9px 12px; font-weight:900; color:#0f172a; text-align:left;">문맥 반영</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#1681c4; font-weight:900;">✅</td>
    </tr>
    <tr style="background:#ffffff;">
      <td style="padding:9px 12px; font-weight:900; color:#0f172a; text-align:left;">단어 순서</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#1681c4; font-weight:900;">✅</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:9px 12px; font-weight:900; color:#0f172a; text-align:left;">동음이의어</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#FF6B00; font-weight:900;">❌</td>
      <td style="padding:9px 8px; color:#1681c4; font-weight:900;">✅</td>
    </tr>
    <tr style="background:#ffffff;">
      <td style="padding:9px 12px; font-weight:900; color:#0f172a; text-align:left;">계산 비용</td>
      <td style="padding:9px 8px; color:#1681c4; font-size:12px;">매우 낮음</td>
      <td style="padding:9px 8px; color:#1681c4; font-size:12px;">낮음</td>
      <td style="padding:9px 8px; color:#1681c4; font-size:12px;">낮음</td>
      <td style="padding:9px 8px; color:#475569; font-size:12px;">중간</td>
      <td style="padding:9px 8px; color:#FF6B00; font-size:12px;">높음</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:9px 12px; font-weight:900; color:#0f172a; text-align:left;">구현 난이도</td>
      <td style="padding:9px 8px; color:#1681c4;">⭐</td>
      <td style="padding:9px 8px; color:#1681c4;">⭐⭐</td>
      <td style="padding:9px 8px; color:#1681c4;">⭐⭐</td>
      <td style="padding:9px 8px; color:#475569;">⭐⭐⭐</td>
      <td style="padding:9px 8px; color:#FF6B00;">⭐⭐⭐⭐</td>
    </tr>
    <tr style="background:#eef7ff;">
      <td style="padding:9px 12px; font-weight:900; color:#0f172a; text-align:left; border-radius:0 0 0 10px;">대표 활용</td>
      <td style="padding:9px 8px; color:#475569; font-size:12px;">범주형 인코딩</td>
      <td style="padding:9px 8px; color:#475569; font-size:12px;">문서 분류</td>
      <td style="padding:9px 8px; color:#475569; font-size:12px;">검색·키워드</td>
      <td style="padding:9px 8px; color:#475569; font-size:12px;">유사 단어 검색</td>
      <td style="padding:9px 8px; color:#1681c4; font-size:12px; font-weight:900; border-radius:0 0 10px 0;">질의응답·번역</td>
    </tr>
  </tbody>
</table>
</div>

</div>

<br>

<!-- 상황별 선택 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔍 상황별 어떤 방법을 써야 할까?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
방법이 발전했다고 해서 무조건 최신 방법이 항상 정답은 아닙니다.<br>
<b>목적, 데이터 크기, 계산 환경</b>에 따라 알맞은 방법을 선택해야 합니다.
</p>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:13px 16px;">
    <div style="font-size:13px; color:#475569; line-height:1.7; white-space:nowrap;">📌 빠른 프로토타이핑, 소규모 데이터</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:5px 12px; border-radius:999px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">BoW / TF-IDF</div>
  </div>

  <div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:13px 16px;">
    <div style="font-size:13px; color:#475569; line-height:1.7; white-space:nowrap;">📌 검색 엔진, 키워드 기반 문서 분류</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:5px 12px; border-radius:999px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">TF-IDF</div>
  </div>

  <div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#eef7ff; border:1px solid #c2e4ff; border-radius:12px; padding:13px 16px;">
    <div style="font-size:13px; color:#475569; line-height:1.7; white-space:nowrap;">📌 단어 간 유사성 비교, 추천 시스템</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; color:#1681c4; padding:5px 12px; border-radius:999px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">단어 임베딩 (Word2Vec, FastText)</div>
  </div>

  <div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#eef7ff; border:1px solid #c2e4ff; border-radius:12px; padding:13px 16px;">
    <div style="font-size:13px; color:#475569; line-height:1.7; white-space:nowrap;">📌 감성 분석, 질의응답, 기계 번역, 챗봇</div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; color:#1681c4; padding:5px 12px; border-radius:999px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">문장 임베딩 (BERT, KoELECTRA 등)</div>
  </div>

  <div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#0f172a; border-radius:12px; padding:13px 16px;">
    <div style="font-size:13px; color:#a6e3a1; line-height:1.7; white-space:nowrap;">📌 GPT·Claude 같은 생성형 AI</div>
    <div style="background:#0d0d1a; color:#c3e88d; padding:5px 12px; border-radius:999px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">문장 임베딩 + 대규모 트랜스포머 모델</div>
  </div>

</div>

</div>

</div>