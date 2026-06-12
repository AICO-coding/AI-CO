<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
텍스트 표현이란?
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
텍스트 표현은 사람이 쓰는 언어를
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">컴퓨터가 처리할 수 있는 숫자 형태로 변환하는 방법</span>
입니다.
</p>

</div>

<br>

<!-- 컴퓨터는 글자를 모른다 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🤔 컴퓨터는 글자를 모른다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
우리는 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">"나는 오늘 행복하다"</code>라는 문장을 읽는 순간 그 의미를 바로 이해합니다.<br>
하지만 컴퓨터는 <b style="color:#FF6B00;">오직 숫자(0과 1)만 이해</b>합니다.
</p>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 15px 17px; border-radius: 12px; font-size: 14px; line-height: 1.8; color: #334155; margin: 14px 0;">
"나는 오늘 행복하다" → 컴퓨터 입장에서는 <b style="color:#FF6B00;">의미를 모르는 문자의 나열</b>일 뿐
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin: 0;">
그렇다면 컴퓨터가 텍스트를 이해하게 하려면 어떻게 해야 할까요?<br>
정답은 <b style="color:#1681c4;">텍스트를 숫자로 바꾸는 것</b>입니다.<br>
이것이 바로 <b>텍스트 표현(Text Representation)</b>입니다.
</p>

</div>

<br>

<!-- 텍스트 표현이란 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📖 텍스트 표현이란?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
<b>텍스트 표현</b>이란 자연어(사람이 쓰는 언어)를 컴퓨터가 처리할 수 있는 <b style="color:#1681c4;">숫자 형태로 변환하는 방법</b>입니다.<br>
앞 챕터에서 텍스트를 깨끗하게 전처리했다면, 이제는 그 텍스트를 컴퓨터가 계산할 수 있는 <b style="color:#FF6B00;">숫자(벡터)로 바꿔야</b> 합니다.
</p>

<div style="margin-top: 18px; display: grid; gap: 10px;">

  <div style="background: #0f172a; color: #c3e88d; border-radius: 14px; padding: 14px 18px; font-weight: 900; text-align: center; box-shadow: 0 6px 14px rgba(15,23,42,.12);">
    전처리된 텍스트
  </div>

  <div style="text-align:center; color:#1681c4; font-weight:900; font-size:20px;">↓</div>

  <div style="background: #eef7ff; border: 2px solid #c2e4ff; border-radius: 14px; padding: 14px 18px; text-align: center;">
    <div style="font-size:15px; font-weight:900; color:#1681c4;">텍스트 표현</div>
  </div>

  <div style="text-align:center; color:#1681c4; font-weight:900; font-size:20px;">↓</div>

  <div style="background: #fff3eb; border: 2px solid #ffd0b0; border-radius: 14px; padding: 14px 18px; text-align: center;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00;">숫자 벡터 (Numbers / Vectors)</div>
  </div>

  <div style="text-align:center; color:#1681c4; font-weight:900; font-size:20px;">↓</div>

  <div style="background: #0f172a; color: #c3e88d; border-radius: 14px; padding: 14px 18px; font-weight: 900; text-align: center; box-shadow: 0 6px 14px rgba(15,23,42,.12);">
    AI 모델 학습
  </div>

</div>

</div>

<br>

<!-- 지도 비유 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🗺️ 비유로 이해하기: 단어를 지도 위에 올리기
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
텍스트를 숫자로 바꾼다는 것을 지도로 비유해봅시다.
</p>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8; margin: 14px 0;">
<span style="color: #FF6B00; font-weight: 900;">💡 도시 좌표 비유</span><br>
서울, 부산, 대구라는 도시를 지도에 표시하면 각각 좌표(위도, 경도)로 나타낼 수 있습니다.<br><br>
<div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:6px;">
  <span style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 10px; border-radius:8px; font-weight:900; font-size:13px;">서울 (37.5, 126.9)</span>
  <span style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 10px; border-radius:8px; font-weight:900; font-size:13px;">부산 (35.1, 129.0)</span>
  <span style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 10px; border-radius:8px; font-weight:900; font-size:13px;">대구 (35.8, 128.6)</span>
</div>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
단어도 마찬가지입니다.<br>
"왕", "여왕", "남자", "여자"라는 단어를 숫자 좌표로 표현하면,<br>
<b style="color:#1681c4;">비슷한 의미를 가진 단어는 가까운 곳에, 다른 의미는 먼 곳에</b> 위치하게 됩니다.
</p>

</div>

<br>

<!-- 좋은 표현의 조건 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
✅ 좋은 텍스트 표현의 조건
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
모든 텍스트 표현 방법이 동일한 것은 아닙니다.<br>
좋은 텍스트 표현이 갖춰야 할 조건이 있습니다.
</p>

<div style="display: grid; gap: 12px; margin-top: 16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:grid; grid-template-columns:auto 1fr 1fr; gap:14px; align-items:start;">
    <div style="font-size:22px;">🎯</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:4px;">의미 보존</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">단어의 의미가 숫자에 반영되어야 합니다.</div>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.7;">
      <b style="color:#FF6B00;">나쁜 예:</b> "행복"과 "기쁨"이 전혀 다른 숫자로 표현됨
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:grid; grid-template-columns:auto 1fr 1fr; gap:14px; align-items:start;">
    <div style="font-size:22px;">📏</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:4px;">유사성 반영</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">비슷한 단어는 비슷한 숫자여야 합니다.</div>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.7;">
      <b style="color:#FF6B00;">나쁜 예:</b> "개"와 "강아지"가 완전히 다르게 표현됨
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:grid; grid-template-columns:auto 1fr 1fr; gap:14px; align-items:start;">
    <div style="font-size:22px;">⚡</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:4px;">효율성</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">너무 많은 메모리를 차지하지 않아야 합니다.</div>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.7;">
      <b style="color:#FF6B00;">나쁜 예:</b> 단어 10만 개를 10만 차원 벡터로 표현
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:grid; grid-template-columns:auto 1fr 1fr; gap:14px; align-items:start;">
    <div style="font-size:22px;">🌍</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:4px;">일반화</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">새로운 문장에도 잘 적용될 수 있어야 합니다.</div>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.7;">
      <b style="color:#FF6B00;">나쁜 예:</b> 학습 데이터에만 있는 단어만 표현 가능
    </div>
  </div>

</div>

</div>

</div>