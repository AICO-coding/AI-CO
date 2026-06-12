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
단어 빈도(TF)의 개념과 대표적인 두 가지 방법,
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">BoW와 TF-IDF</span>
를 알아봅니다.
</p>

</div>

<br>

<!-- 단어 빈도란 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔢 단어 빈도(Term Frequency)란?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
<b>단어 빈도(TF, Term Frequency)</b>는 말 그대로 <b style="color:#1681c4;">어떤 단어가 문서 안에 몇 번 등장하는지</b>를 세는 것입니다.
</p>

<div style="background-color: #0f172a; border-radius: 14px; padding: 14px 20px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; color: #a6e3a1; line-height: 2; margin: 14px 0;">
"고양이가 생선을 먹었다. 고양이가 또 생선을 먹었다."
</div>

<div style="display: grid; gap: 8px; margin-top: 14px;">

  <div style="display:grid; grid-template-columns:120px 1fr; gap:10px; align-items:center;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:8px 12px; border-radius:8px; font-weight:900; font-size:14px; text-align:center;">고양이가</div>
    <div style="display:flex; align-items:center; gap:10px;">
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 16px; font-family:Consolas, monospace; font-size:13px; color:#89dceb;">2번</div>
      <div style="display:flex; gap:4px;">
        <span style="background:#FF6B00; width:20px; height:20px; border-radius:4px; display:inline-block;"></span>
        <span style="background:#FF6B00; width:20px; height:20px; border-radius:4px; display:inline-block;"></span>
      </div>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:120px 1fr; gap:10px; align-items:center;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:8px 12px; border-radius:8px; font-weight:900; font-size:14px; text-align:center;">생선을</div>
    <div style="display:flex; align-items:center; gap:10px;">
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 16px; font-family:Consolas, monospace; font-size:13px; color:#89dceb;">2번</div>
      <div style="display:flex; gap:4px;">
        <span style="background:#FF6B00; width:20px; height:20px; border-radius:4px; display:inline-block;"></span>
        <span style="background:#FF6B00; width:20px; height:20px; border-radius:4px; display:inline-block;"></span>
      </div>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:120px 1fr; gap:10px; align-items:center;">
    <div style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:8px 12px; border-radius:8px; font-weight:900; font-size:14px; text-align:center;">먹었다</div>
    <div style="display:flex; align-items:center; gap:10px;">
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 16px; font-family:Consolas, monospace; font-size:13px; color:#89dceb;">2번</div>
      <div style="display:flex; gap:4px;">
        <span style="background:#FF6B00; width:20px; height:20px; border-radius:4px; display:inline-block;"></span>
        <span style="background:#FF6B00; width:20px; height:20px; border-radius:4px; display:inline-block;"></span>
      </div>
    </div>
  </div>

  <div style="display:grid; grid-template-columns:120px 1fr; gap:10px; align-items:center;">
    <div style="background:#eef7ff; border:1px solid #c2e4ff; color:#1681c4; padding:8px 12px; border-radius:8px; font-weight:900; font-size:14px; text-align:center;">또</div>
    <div style="display:flex; align-items:center; gap:10px;">
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 16px; font-family:Consolas, monospace; font-size:13px; color:#89dceb;">1번</div>
      <div style="display:flex; gap:4px;">
        <span style="background:#1681c4; width:20px; height:20px; border-radius:4px; display:inline-block;"></span>
      </div>
    </div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 각 단어가 몇 번 나왔는지 숫자로 기록하는 것이 <b>단어 빈도</b>입니다.
</div>

</div>

<br>

<!-- BoW vs TF-IDF -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 단어 빈도 기반 표현 방법의 종류
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
단어 빈도를 활용한 텍스트 표현 방법은 크게 두 가지입니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px;">
    <div style="font-size:16px; font-weight:900; color:#FF6B00; margin-bottom:8px;">BoW</div>
    <div style="font-size:13px; color:#94a3b8; font-weight:700; margin-bottom:10px;">Bag of Words</div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 13px; font-size:14px; color:#334155; line-height:1.7; margin-bottom:10px;">
      단어가 <b style="color:#FF6B00;">몇 번 나왔는지</b>만 셉니다.
    </div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">
      <span style="color:#FF6B00; font-weight:900;">핵심 질문:</span> 이 단어가 몇 번 나왔나?<br>
      <span style="color:#6c7086;">ex) "경기" 5번 → 5</span>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:18px 20px;">
    <div style="font-size:16px; font-weight:900; color:#1681c4; margin-bottom:8px;">TF-IDF</div>
    <div style="font-size:13px; color:#94a3b8; font-weight:700; margin-bottom:10px;">Term Frequency - Inverse Document Frequency</div>
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 13px; font-size:14px; color:#334155; line-height:1.7; margin-bottom:10px;">
      빈도 + <b style="color:#1681c4;">"이 단어가 다른 문서에도 많이 나오나?"</b>까지 고려합니다.
    </div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">
      <span style="color:#1681c4; font-weight:900;">핵심 질문:</span> 이 단어가 이 문서에서만 특별히 많이 나왔나?<br>
      <span style="color:#6c7086;">ex) "경기"는 모든 문서에 나오니 중요도 낮춤</span>
    </div>
  </div>

</div>

</div>

<br>

<!-- 처리 흐름 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 단어 빈도 기반 표현의 공통 처리 흐름
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BoW든 TF-IDF든 기본 처리 흐름은 동일합니다.
</p>

<div style="display: grid; gap: 10px; margin-top: 18px;">

  <div style="background:#0f172a; color:#c3e88d; border-radius:14px; padding:14px 20px; font-weight:900; text-align:center; box-shadow: 0 6px 14px rgba(15,23,42,.12);">
    ① 여러 문서(문장)를 모은다
  </div>

  <div style="text-align:center; color:#1681c4; font-weight:900; font-size:20px;">↓</div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 20px; text-align:center;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00;">② 전체 문서에서 등장하는 모든 단어를 모아 단어 사전을 만든다</div>
  </div>

  <div style="text-align:center; color:#1681c4; font-weight:900; font-size:20px;">↓</div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 20px; text-align:center;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00;">③ 각 문서에서 각 단어가 몇 번 나왔는지 센다</div>
  </div>

  <div style="text-align:center; color:#1681c4; font-weight:900; font-size:20px;">↓</div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 20px; text-align:center;">
    <div style="font-size:14px; font-weight:900; color:#1681c4;">④ 단어 사전 크기의 벡터를 만들고, 등장 횟수(또는 가중치)를 채워 넣는다</div>
  </div>

  <div style="text-align:center; color:#1681c4; font-weight:900; font-size:20px;">↓</div>

  <div style="background:#0f172a; color:#c3e88d; border-radius:14px; padding:14px 20px; font-weight:900; text-align:center; box-shadow: 0 6px 14px rgba(15,23,42,.12);">
    ⑤ 문서 = 숫자 벡터로 표현 완료
  </div>

</div>

</div>

<br>

<!-- DTM 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📦 문서-단어 행렬 (Document-Term Matrix)
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
단어 빈도 기반 표현의 결과물은 <b style="color:#1681c4;">문서-단어 행렬(DTM)</b>이라는 표 형태로 나타납니다.
</p>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom:12px;">
예시 문서 3개:
</p>

<div style="background-color: #0f172a; border-radius: 14px; padding: 14px 20px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; line-height: 2.2; margin-bottom: 16px;">
  <span style="color:#6c7086;">문서 1: </span><span style="color:#a6e3a1;">"나는 밥을 먹었다"</span><br>
  <span style="color:#6c7086;">문서 2: </span><span style="color:#a6e3a1;">"나는 물을 마셨다"</span><br>
  <span style="color:#6c7086;">문서 3: </span><span style="color:#a6e3a1;">"고양이가 밥을 먹었다"</span>
</div>

<!-- DTM 표 -->
<div style="overflow-x: auto; margin-top: 4px;">
<table style="width:100%; border-collapse:collapse; font-size:14px; text-align:center;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; border-radius:10px 0 0 0; text-align:left; font-weight:900;"></th>
      <th style="padding:10px 10px; font-weight:900;">고양이가</th>
      <th style="padding:10px 10px; font-weight:900;">나는</th>
      <th style="padding:10px 10px; font-weight:900;">마셨다</th>
      <th style="padding:10px 10px; font-weight:900;">먹었다</th>
      <th style="padding:10px 10px; font-weight:900;">밥을</th>
      <th style="padding:10px 10px; border-radius:0 10px 0 0; font-weight:900;">물을</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#eef7ff;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4; text-align:left;">문서 1</td>
      <td style="padding:10px; color:#94a3b8;">0</td>
      <td style="padding:10px; color:#FF6B00; font-weight:900;">1</td>
      <td style="padding:10px; color:#94a3b8;">0</td>
      <td style="padding:10px; color:#FF6B00; font-weight:900;">1</td>
      <td style="padding:10px; color:#FF6B00; font-weight:900;">1</td>
      <td style="padding:10px; color:#94a3b8;">0</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4; text-align:left;">문서 2</td>
      <td style="padding:10px; color:#94a3b8;">0</td>
      <td style="padding:10px; color:#FF6B00; font-weight:900;">1</td>
      <td style="padding:10px; color:#FF6B00; font-weight:900;">1</td>
      <td style="padding:10px; color:#94a3b8;">0</td>
      <td style="padding:10px; color:#94a3b8;">0</td>
      <td style="padding:10px; color:#FF6B00; font-weight:900;">1</td>
    </tr>
    <tr style="background:#eef7ff;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4; text-align:left;">문서 3</td>
      <td style="padding:10px; color:#FF6B00; font-weight:900;">1</td>
      <td style="padding:10px; color:#94a3b8;">0</td>
      <td style="padding:10px; color:#94a3b8;">0</td>
      <td style="padding:10px; color:#FF6B00; font-weight:900;">1</td>
      <td style="padding:10px; color:#FF6B00; font-weight:900;">1</td>
      <td style="padding:10px; color:#94a3b8;">0</td>
    </tr>
  </tbody>
</table>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-top: 14px;">
  <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 14px; font-size:13px; color:#334155; line-height:1.7;">
    <b style="color:#1681c4;">행(row)</b><br>
    하나의 문서를 숫자 벡터로 표현
  </div>
  <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 14px; font-size:13px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">열(column)</b><br>
    단어 사전의 단어
  </div>
  <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 14px; font-size:13px; color:#334155; line-height:1.7;">
    <b style="color:#0f172a;">숫자</b><br>
    해당 문서에서 해당 단어가 등장한 횟수
  </div>
</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌</span> 이 행렬 하나가 바로 <b>"텍스트를 숫자로 바꾼 결과"</b>입니다.<br>
이제 컴퓨터가 수학적으로 계산할 수 있게 됩니다.
</div>

</div>

</div>