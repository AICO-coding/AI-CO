<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
    <div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
      Chapter 02 · NLP 텍스트 전처리
    </div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
2-1. 전처리란 무엇인가?
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
전처리는 모델이 텍스트를 더 잘 이해할 수 있도록 
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">데이터를 미리 다듬는 과정</span>
입니다.<br>
쉽게 말하면, 데이터를 다루는 요리사가 재료를 손질하는 단계라고 볼 수 있습니다.
</p>

</div>

<br>

<!-- 개념 설명 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
왜 텍스트를 미리 다듬어야 할까?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
인터넷에서 긁어온 글, 카카오톡 대화, 쇼핑몰 리뷰처럼 현실의 텍스트는 대부분 깔끔하지 않습니다.
</p>

<div style="display: flex; gap: 10px; flex-wrap: wrap; margin: 14px 0 18px 0;">
  <span style="background: #fff3eb; border: 1px solid #ffd0b0; color: #FF6B00; padding: 6px 11px; border-radius: 999px; font-weight: 800; font-size: 13px;">HTML 태그</span>
  <span style="background: #fff3eb; border: 1px solid #ffd0b0; color: #FF6B00; padding: 6px 11px; border-radius: 999px; font-weight: 800; font-size: 13px;">이모지</span>
  <span style="background: #fff3eb; border: 1px solid #ffd0b0; color: #FF6B00; padding: 6px 11px; border-radius: 999px; font-weight: 800; font-size: 13px;">오타</span>
  <span style="background: #fff3eb; border: 1px solid #ffd0b0; color: #FF6B00; padding: 6px 11px; border-radius: 999px; font-weight: 800; font-size: 13px;">광고 문구</span>
  <span style="background: #fff3eb; border: 1px solid #ffd0b0; color: #FF6B00; padding: 6px 11px; border-radius: 999px; font-weight: 800; font-size: 13px;">불필요한 공백</span>
</div>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 15px 17px; border-radius: 12px; font-size: 14px; line-height: 1.8; color: #334155;">
AI 모델은 이런 요소들을 스스로 “쓸모없는 정보”라고 판단하지 못하고, 
<b style="color:#FF6B00;">모두 의미 있는 정보처럼 학습</b>할 수 있습니다.<br>
즉, 쓰레기와 음식 재료를 함께 넣고 요리하는 것과 비슷합니다.
</div>

<div style="margin-top: 16px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡 요리 비유</span><br>
라면을 끓이기 전에 봉지를 뜯고, 면과 스프를 준비하듯이 모델 학습 전에도 텍스트를 깨끗하게 손질해야 합니다.<br>
이 과정이 바로 <b>전처리</b>입니다.
</div>

</div>

<br>

<!-- 문제 상황 표 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
전처리를 안 하면 어떻게 될까?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 16px;">
사람이 보기에는 같은 의미처럼 보여도, 컴퓨터는 다르게 받아들일 수 있습니다.
</p>

<tbody>
<div style="display: grid; gap: 14px; margin-top: 18px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="margin-bottom:10px;">
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"안녕"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"안녕!"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"안녕~"</span>
    </div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">컴퓨터가 보는 방식</div>
        <div style="font-size:14px; color:#334155; line-height:1.6;">3개의 완전히 다른 단어</div>
      </div>
      <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">실제 의미</div>
        <div style="font-size:14px; color:#334155; line-height:1.6;">모두 같은 인사말</div>
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="margin-bottom:10px;">
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">&lt;p&gt;맛있다&lt;/p&gt;</span>
    </div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">컴퓨터가 보는 방식</div>
        <div style="font-size:14px; color:#334155; line-height:1.6;">
          <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px; font-family:Consolas, monospace; font-size:13px;">&lt;p&gt;</span>
          <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px; font-family:Consolas, monospace; font-size:13px;">맛있다</span>
          <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px; font-family:Consolas, monospace; font-size:13px;">&lt;/p&gt;</span>
          세 토큰
        </div>
      </div>
      <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">실제 의미</div>
        <div style="font-size:14px; color:#334155; line-height:1.6;">맛있다</div>
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="margin-bottom:10px;">
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"최고예요~~~~"</span>
    </div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">컴퓨터가 보는 방식</div>
        <div style="font-size:14px; color:#334155; line-height:1.6;">느낌표와 물결표도 학습</div>
      </div>
      <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">실제 의미</div>
        <div style="font-size:14px; color:#334155; line-height:1.6;">최고예요</div>
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="margin-bottom:10px;">
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"  나  는   학교"</span>
    </div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">컴퓨터가 보는 방식</div>
        <div style="font-size:14px; color:#334155; line-height:1.6;">공백 개수까지 다른 단어</div>
      </div>
      <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">실제 의미</div>
        <div style="font-size:14px; color:#334155; line-height:1.6;">나는 학교</div>
      </div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 전처리 전후 비교 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
전처리 전후 비교
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
아래는 실제 리뷰 문장이 전처리를 거치면서 어떻게 깔끔해지는지 보여주는 예시입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      전처리 예시
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.8; overflow-x: auto;">

<pre style="margin:0; white-space:pre-wrap;"><code>원본:
"&lt;b&gt;대박!!&lt;/b&gt;  이 폰   👍👍 진짜  최고예요~~~  https://t.co/abc  #광고아님 &lt;br/&gt;"

① HTML 태그 제거:
"대박!!  이 폰   👍👍 진짜  최고예요~~~  https://t.co/abc  #광고아님"

② URL 제거:
"대박!!  이 폰   👍👍 진짜  최고예요~~~  #광고아님"

③ 이모지 + 특수기호 제거:
"대박  이 폰  진짜  최고예요"

④ 공백 정리:
"대박 이 폰 진짜 최고예요"   ← 깨끗한 텍스트 완성</code></pre>

</div>
</div>

</div>

<br>

<!-- 파이프라인 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
전처리 5단계 파이프라인
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
전처리는 보통 아래와 같은 흐름으로 진행됩니다.
</p>

<div style="margin-top: 18px; display: grid; gap: 12px;">

  <div style="background: #0f172a; color: #c3e88d; border-radius: 14px; padding: 14px 18px; font-weight: 900; text-align: center; box-shadow: 0 6px 14px rgba(15,23,42,.12);">
    원본 텍스트
  </div>

  <div style="text-align:center; color:#1681c4; font-weight:900;">▼</div>

  <div style="background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 16px 18px;">
    <div style="font-size: 15px; font-weight: 900; color: #FF6B00; margin-bottom: 6px;">1단계. 노이즈 제거</div>
    <div style="font-size: 14px; color: #475569; line-height: 1.7;">HTML, URL, 이모지, 특수문자처럼 불필요한 요소를 삭제합니다.</div>
  </div>

  <div style="text-align:center; color:#1681c4; font-weight:900;">▼</div>

  <div style="background: #eef7ff; border: 2px solid #c2e4ff; border-radius: 14px; padding: 16px 18px;">
    <div style="font-size: 15px; font-weight: 900; color: #1681c4; margin-bottom: 6px;">2단계. 토큰화</div>
    <div style="font-size: 14px; color: #475569; line-height: 1.7;">문장을 단어, 형태소, 문장 단위로 나눕니다.</div>
  </div>

  <div style="text-align:center; color:#1681c4; font-weight:900;">▼</div>

  <div style="background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 16px 18px;">
    <div style="font-size: 15px; font-weight: 900; color: #FF6B00; margin-bottom: 6px;">3단계. 불용어 제거</div>
    <div style="font-size: 14px; color: #475569; line-height: 1.7;">은, 는, 이, 가처럼 분석에 큰 의미가 없는 단어를 제거합니다.</div>
  </div>

  <div style="text-align:center; color:#1681c4; font-weight:900;">▼</div>

  <div style="background: #eef7ff; border: 2px solid #c2e4ff; border-radius: 14px; padding: 16px 18px;">
    <div style="font-size: 15px; font-weight: 900; color: #1681c4; margin-bottom: 6px;">4단계. 정규화</div>
    <div style="font-size: 14px; color: #475569; line-height: 1.7;">대소문자 통일, 숫자 처리, 맞춤법 교정 등을 수행합니다.</div>
  </div>

  <div style="text-align:center; color:#1681c4; font-weight:900;">▼</div>

  <div style="background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 16px 18px;">
    <div style="font-size: 15px; font-weight: 900; color: #FF6B00; margin-bottom: 6px;">5단계. 어간 추출</div>
    <div style="font-size: 14px; color: #475569; line-height: 1.7;">
      단어를 원형에 가깝게 변환합니다. 
      <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">run</code>,
      <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">ran</code>,
      <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">running</code>
      → 
      <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">run</code>
    </div>
  </div>

  <div style="text-align:center; color:#1681c4; font-weight:900;">▼</div>

  <div style="background: #0f172a; color: #c3e88d; border-radius: 14px; padding: 14px 18px; font-weight: 900; text-align: center; box-shadow: 0 6px 14px rgba(15,23,42,.12);">
    모델 입력용 텍스트
  </div>

</div>

</div>

<br>

<!-- 핵심 정리 카드 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 20px 22px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="font-size: 15px; font-weight: 900; margin-bottom: 8px;">
<span style="color: #FF6B00; font-size: 18px;">⚠️</span>
Garbage in, Garbage out
</div>

<p style="margin: 0; line-height: 1.8; font-size: 14px; color: #334155;">
전처리 품질은 모델 성능을 직접 결정합니다.<br>
지저분한 데이터를 넣으면 모델도 지저분한 패턴을 학습하게 됩니다.
</p>

</div>

</div>