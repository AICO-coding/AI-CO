<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #ffffff; border: 1px solid #ffd0b0; color: #ff6b00; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; margin-bottom: 12px;">NLP 기초 개념</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
NLP는 구체적으로 어떤 일을 할까?
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
NLP는 하나의 기술이 아니라, 여러 
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">태스크</span>
의 모음입니다.<br>
각 태스크는 언어에서 다른 종류의 정보를 뽑아냅니다.
</p>

<div style="margin-top: 18px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; color: #0f172a; font-weight: 800; font-size: 14px;">
<span style="color: #FF6B00;">💡</span>
NLP 태스크는 “문장에서 무엇을 알아낼 것인가?”에 따라 나뉩니다.
</div>

</div>

<br>

<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
주요 NLP 태스크 한눈에 보기
</h2>

<table style="width: 100%; border-collapse: collapse; overflow: hidden; border-radius: 12px; font-size: 14px;">
  <thead>
    <tr style="background-color: #0f172a; color: #c3e88d;">
      <th style="padding: 13px 14px; text-align: left; border: 1px solid #1e293b;">태스크</th>
      <th style="padding: 13px 14px; text-align: left; border: 1px solid #1e293b;">무엇을 하나요?</th>
      <th style="padding: 13px 14px; text-align: left; border: 1px solid #1e293b;">대표 활용</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 13px 14px; border: 1px solid #e2e8f0; color: #FF6B00; font-weight: 900;">감정 분석</td>
      <td style="padding: 13px 14px; border: 1px solid #e2e8f0; color:#475569;">텍스트가 긍정인지 부정인지 판별</td>
      <td style="padding: 13px 14px; border: 1px solid #e2e8f0; color:#475569;">리뷰 분류, 여론 분석</td>
    </tr>
    <tr style="background-color: #eef7ff;">
      <td style="padding: 13px 14px; border: 1px solid #e2e8f0; color: #FF6B00; font-weight: 900;">개체명 인식</td>
      <td style="padding: 13px 14px; border: 1px solid #e2e8f0; color:#475569;">사람, 장소, 회사명 등을 추출</td>
      <td style="padding: 13px 14px; border: 1px solid #e2e8f0; color:#475569;">뉴스/계약서 분석</td>
    </tr>
    <tr style="background-color: #f8fafc;">
      <td style="padding: 13px 14px; border: 1px solid #e2e8f0; color: #FF6B00; font-weight: 900;">기계 번역</td>
      <td style="padding: 13px 14px; border: 1px solid #e2e8f0; color:#475569;">한 언어를 다른 언어로 번역</td>
      <td style="padding: 13px 14px; border: 1px solid #e2e8f0; color:#475569;">파파고, 구글 번역</td>
    </tr>
    <tr style="background-color: #eef7ff;">
      <td style="padding: 13px 14px; border: 1px solid #e2e8f0; color: #FF6B00; font-weight: 900;">질의응답</td>
      <td style="padding: 13px 14px; border: 1px solid #e2e8f0; color:#475569;">문서에서 질문의 답을 찾음</td>
      <td style="padding: 13px 14px; border: 1px solid #e2e8f0; color:#475569;">검색, 챗봇, 문서 QA</td>
    </tr>
  </tbody>
</table>

</div>

<br>

<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
① 감정 분석 <span style="color: #1681c4;">(Sentiment Analysis)</span>
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
텍스트가 <b style="color:#1681c4;">긍정</b>인지 <b style="color:#FF6B00;">부정</b>인지 자동으로 판별합니다.
</p>

<div style="display: flex; gap: 10px; flex-wrap: wrap; margin: 14px 0;">
  <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 5px 10px; border-radius: 999px; font-weight: 800; font-size: 13px;">쇼핑몰 리뷰 자동 분류</span>
  <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 5px 10px; border-radius: 999px; font-weight: 800; font-size: 13px;">SNS 여론 분석</span>
  <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 5px 10px; border-radius: 999px; font-weight: 800; font-size: 13px;">고객 불만 탐지</span>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; line-height: 1.8; margin-top: 14px;">
<span style="color: #FF6B00; font-weight: 900;">예시</span><br>
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">"이 영화 최고예요!"</code>
→ <b>POSITIVE (긍정)</b><br>
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">"환불하고 싶어요"</code>
→ <b>NEGATIVE (부정)</b>
</div>

</div>

<br>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18);">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 sentiment_analysis.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      감정 분석 코드
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
from transformers import pipeline

# pipeline()으로 원하는 태스크를 한 줄에 로드
analyzer = pipeline("sentiment-analysis")

texts = [
    "이 영화 정말 재미있었어요!",
    "너무 별로였어요. 돈 아까워요."
]
for t in texts:
    r = analyzer(t)[0]
    print(r['label'], r['score'])
# POSITIVE  0.998
# NEGATIVE  0.991
```

</div>
</div>

<br>

<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
② 개체명 인식 <span style="color: #1681c4;">(NER, Named Entity Recognition)</span>
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
문장에서 <b>사람 이름, 장소, 날짜, 회사명</b> 등을 자동으로 찾아냅니다.
</p>

<div style="display: flex; gap: 10px; flex-wrap: wrap; margin: 14px 0;">
  <span style="background: #eef7ff; border: 1px solid #c2e4ff; color: #1681c4; padding: 5px 10px; border-radius: 999px; font-weight: 800; font-size: 13px;">뉴스 기사 정보 추출</span>
  <span style="background: #eef7ff; border: 1px solid #c2e4ff; color: #1681c4; padding: 5px 10px; border-radius: 999px; font-weight: 800; font-size: 13px;">기관/인물 자동 추출</span>
  <span style="background: #eef7ff; border: 1px solid #c2e4ff; color: #1681c4; padding: 5px 10px; border-radius: 999px; font-weight: 800; font-size: 13px;">계약서 분석</span>
</div>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 16px; border-radius: 12px; font-size: 14px; line-height: 1.8; margin-top: 14px;">
<span style="color: #FF6B00; font-weight: 900;">예시</span><br>
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">"삼성전자가 서울에서 발표했다"</code><br>
→ <b>삼성전자(회사)</b>, <b>서울(장소)</b>
</div>

</div>

<br>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18);">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 ner.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      개체명 인식 코드
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
from transformers import pipeline

# aggregation_strategy: 분리된 토큰을 하나의 개체로 합치는 방식
ner = pipeline("ner", aggregation_strategy="simple")

result = ner("삼성전자가 서울에서 발표했다")
for e in result:
    print(e['word'], "→", e['entity_group'])
# 삼성전자 → ORG  (조직, Organization)
# 서울     → LOC  (장소, Location)
```

</div>
</div>

<br>

<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
③ 기계 번역 <span style="color: #1681c4;">(Machine Translation)</span>
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
한 언어를 다른 언어로 <b style="color:#FF6B00;">자동 번역</b>합니다.<br>
파파고, 구글 번역이 대표적입니다.
</p>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; color: #0f172a; font-weight: 800; font-size: 14px;">
<span style="color: #FF6B00;">🌐</span>
기계 번역은 문장의 단어만 바꾸는 것이 아니라, 문맥과 표현까지 고려합니다.
</div>

</div>

<br>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18);">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 translation.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      기계 번역 코드
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
from transformers import pipeline

# Helsinki-NLP: 공개 번역 모델 (ko → en)
translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-ko-en"
)
result = translator("안녕하세요, 반갑습니다.")
print(result[0]['translation_text'])
# Hello, nice to meet you.
```

</div>
</div>

<br>

<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
④ 질의응답 <span style="color: #1681c4;">(Question Answering)</span>
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
주어진 <b style="color:#1681c4;">문서(context)</b>를 읽고, 질문에 대한 정확한 답을 찾아냅니다.
</p>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 16px; border-radius: 12px; font-size: 14px; line-height: 1.8; margin-top: 14px;">
<span style="color: #FF6B00; font-weight: 900;">핵심 구조</span><br>
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">question</code>
→ 질문<br>
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">context</code>
→ 답을 찾을 문서
</div>

</div>

<br>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18);">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 question_answering.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      질의응답 코드
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
from transformers import pipeline

# question: 질문 / context: 답을 찾을 문서
qa = pipeline("question-answering")
answer = qa(
    question="수도는 어디인가요?",
    context="대한민국의 수도는 서울이다. 인구는 약 5천만 명이다."
)
print(answer['answer'])
# 출력: 서울
print(answer['score'])   # 확신도 점수
# 출력: 0.987
```

</div>
</div>

<br>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; font-weight: 900; font-size: 15px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<span style="color: #FF6B00; font-size: 18px;">⚡</span>
NLP 태스크는 텍스트에서 감정, 개체명, 번역 결과, 질문의 답처럼 필요한 정보를 뽑아내는 작업입니다.
</div>

</div>
