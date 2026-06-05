<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #ffffff; border: 1px solid #ffd0b0; color: #ff6b00; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; margin-bottom: 12px;">
NLP 전처리
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
2-2. 노이즈 제거
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
노이즈 제거는 텍스트 안에 섞인 
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">쓸모없는 문자</span>
를 정리하는 과정입니다.<br>
이번에는 정규표현식으로 HTML 태그, URL, 반복 문자, 특수문자, 공백을 정리해봅니다.
</p>

</div>

<br>

<!-- 핵심 함수 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
핵심 함수: <span style="color:#1681c4;">re.sub()</span>
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Python의 <b style="color:#FF6B00;">re</b> 모듈은 정규표현식을 다루는 내장 라이브러리입니다.<br>
그중 <b>re.sub()</b> 함수는 패턴에 해당하는 부분을 찾아 원하는 문자로 바꿔줍니다.
</p>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 16px 18px; border-radius: 12px; margin-top: 14px;">
  <div style="font-size: 13px; font-weight: 900; color: #1681c4; margin-bottom: 8px;">기본 구조</div>
  <code style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:5px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:14px;">re.sub(패턴, 교체, 텍스트)</code>
</div>

<div style="margin-top: 16px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡 핵심 포인트</span><br>
패턴에 해당하는 부분을 찾아 교체 문자로 바꿉니다.<br>
교체 문자를 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">''</code> 빈 문자열로 쓰면 해당 부분이 <b>삭제</b>됩니다.
</div>

</div>

<br>

<!-- 코드 줄별 설명 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
코드 줄별 상세 설명
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
아래 코드는 전처리에서 자주 사용하는 정규표현식 패턴입니다.
</p>

<div style="display: grid; gap: 16px; margin-top: 18px;">

<!-- import re -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="margin-bottom: 10px;">
    <span style="display:inline-block; background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px;">import re</span>
  </div>
  <p style="margin:0; font-size:14px; color:#475569; line-height:1.7;">
    <b style="color:#FF6B00;">re</b> 모듈은 파이썬 내장 라이브러리라서 별도 설치 없이 바로 사용할 수 있습니다.
  </p>
</div>

<!-- HTML 제거 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:10px;">1. HTML 태그 제거</div>
  <div style="margin-bottom: 12px;">
    <span style="display:inline-block; background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px;">re.sub(r'&lt;[^&gt;]+&gt;', '', text)</span>
  </div>
  <p style="margin:0 0 12px 0; font-size:14px; color:#475569; line-height:1.7;">
    <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">&lt;</code> 로 시작하고 
    <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">&gt;</code> 로 끝나는 모든 문자열을 삭제합니다.
  </p>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">패턴 설명</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">
        <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">[^&gt;]</code>
        는 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">&gt;</code> 를 제외한 문자입니다.<br>
        <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">+</code>
        는 1개 이상 반복을 뜻합니다.
      </div>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">예시</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">
        <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">&lt;b&gt;대박&lt;/b&gt;</code>
        → 대박<br>
        <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">&lt;p class="a"&gt;글&lt;/p&gt;</code>
        → 글
      </div>
    </div>
  </div>
</div>

<!-- URL 제거 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:10px;">2. URL 제거</div>
  <div style="margin-bottom: 12px;">
    <span style="display:inline-block; background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px;">re.sub(r'https?://\S+', '', text)</span>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">https?</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">http 또는 https</div>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">://</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">그대로 매칭</div>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">\S+</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">공백 전까지 URL 끝까지</div>
    </div>
  </div>
</div>

<!-- 반복 문자 축약 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:10px;">3. 반복 문자 축약</div>
  <div style="margin-bottom: 12px;">
    <span style="display:inline-block; background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px;">re.sub(r'(.)\1{2,}', r'\1', text)</span>
  </div>
  <p style="margin:0 0 12px 0; font-size:14px; color:#475569; line-height:1.7;">
    같은 문자가 3번 이상 반복되면 1개만 남깁니다.
    예를 들어 <b style="color:#FF6B00;">~~~ → ~</b>, <b style="color:#FF6B00;">!!! → !</b> 로 줄어듭니다.
  </p>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">패턴 설명</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">
        <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">(.)</code>
        는 문자 1개를 기억합니다.<br>
        <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">\1</code>
        은 방금 기억한 같은 문자입니다.<br>
        <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">{2,}</code>
        는 2번 이상 반복입니다.
      </div>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">교체 결과</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">
        <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">r'\1'</code>
        로 바꾸면 기억한 문자 1개만 남습니다.
      </div>
    </div>
  </div>
</div>

<!-- 특수문자 제거 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:10px;">4. 특수문자 제거</div>
  <div style="margin-bottom: 12px;">
    <span style="display:inline-block; background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px;">re.sub(r'[^\w\s가-힣]', '', text)</span>
  </div>
  <p style="margin:0 0 12px 0; font-size:14px; color:#475569; line-height:1.7;">
    한글, 영문, 숫자, 공백만 남기고 나머지 특수문자를 제거합니다.
  </p>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">[^...]</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">목록 이외의 문자</div>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">\w, \s</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">영문·숫자·공백</div>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">가-힣</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">한글 전체 범위</div>
    </div>
  </div>
</div>

<!-- 공백 정리 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:10px;">5. 공백 정리</div>
  <div style="margin-bottom: 12px;">
    <span style="display:inline-block; background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px;">re.sub(r'\s+', ' ', text).strip()</span>
  </div>
  <p style="margin:0; font-size:14px; color:#475569; line-height:1.7;">
    여러 개의 공백, 탭, 줄바꿈을 공백 1개로 바꾸고, 맨 앞과 뒤의 공백을 제거합니다.
  </p>
</div>

</div>
</div>

<br>

<!-- 정규표현식 패턴 모음 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
자주 쓰는 정규표현식 패턴 모음
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
표 대신 깨지지 않는 카드형 목록으로 정리했습니다.
</p>

<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; margin-top: 18px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:15px 16px;">
    <code style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 8px; border-radius:7px; font-weight:900;">\S+</code>
    <div style="margin-top:9px; font-size:14px; color:#334155; line-height:1.7;">
      공백 아닌 문자 1개 이상<br>
      <b style="color:#1681c4;">활용:</b> URL, 이메일 제거
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:15px 16px;">
    <code style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 8px; border-radius:7px; font-weight:900;">\s+</code>
    <div style="margin-top:9px; font-size:14px; color:#334155; line-height:1.7;">
      공백 문자 1개 이상<br>
      <b style="color:#1681c4;">활용:</b> 공백 정리
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:15px 16px;">
    <code style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 8px; border-radius:7px; font-weight:900;">\d+</code>
    <div style="margin-top:9px; font-size:14px; color:#334155; line-height:1.7;">
      숫자 1개 이상<br>
      <b style="color:#1681c4;">활용:</b> 숫자 제거 또는 [NUM] 대체
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:15px 16px;">
    <code style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 8px; border-radius:7px; font-weight:900;">[^가-힣]</code>
    <div style="margin-top:9px; font-size:14px; color:#334155; line-height:1.7;">
      한글이 아닌 모든 문자<br>
      <b style="color:#1681c4;">활용:</b> 한글만 남기기
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:15px 16px;">
    <code style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 8px; border-radius:7px; font-weight:900;">(.)\1{2,}</code>
    <div style="margin-top:9px; font-size:14px; color:#334155; line-height:1.7;">
      같은 문자 3회 이상 반복<br>
      <b style="color:#1681c4;">활용:</b> 반복 문자 축약
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:15px 16px;">
    <code style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 8px; border-radius:7px; font-weight:900;">&lt;[^&gt;]+&gt;</code>
    <div style="margin-top:9px; font-size:14px; color:#334155; line-height:1.7;">
      HTML 태그<br>
      <b style="color:#1681c4;">활용:</b> 태그 제거
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:15px 16px; grid-column: 1 / -1;">
    <code style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 8px; border-radius:7px; font-weight:900;">https?://\S+</code>
    <div style="margin-top:9px; font-size:14px; color:#334155; line-height:1.7;">
      http 또는 https로 시작하는 URL<br>
      <b style="color:#1681c4;">활용:</b> URL 제거
    </div>
  </div>

</div>

</div>

<br>

<!-- 마무리 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; font-weight: 900; font-size: 15px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<span style="color: #FF6B00; font-size: 18px;">⚡</span>
노이즈 제거는 모델이 불필요한 문자에 속지 않도록 텍스트를 깨끗하게 정리하는 단계입니다.
</div>

</div>