<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #ffffff; border: 1px solid #ffd0b0; color: #ff6b00; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; margin-bottom: 12px;">
NLP 전처리
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
2-3. 토큰화
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
토큰화는 문장을 AI가 이해하기 좋은 
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">작은 조각</span>
으로 나누는 과정입니다.<br>
이때 나눠진 각각의 조각을 <b style="color:#1681c4;">토큰(Token)</b>이라고 부릅니다.
</p>

</div>

<br>

<!-- 개념 설명 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
레고 블록처럼 — 문장을 최소 단위로 분해
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
컴퓨터는 문장을 사람처럼 자연스럽게 이해하지 못합니다.<br>
예를 들어 
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">"나는 오늘 학교에 갔다"</code>
라는 문장도 의미 있는 단위로 잘라서 다뤄야 합니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 18px 0;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:8px;">토큰 Token</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      문장을 쪼갰을 때 나오는 각각의 조각입니다.
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:8px;">토큰화 Tokenization</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      문장을 토큰 단위로 나누는 과정입니다.
    </div>
  </div>

</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡 레고 비유</span><br>
완성된 레고 집을 낱개 블록으로 분해해야 다시 조립할 수 있듯이, 문장도 토큰으로 분해해야 AI가 학습할 수 있습니다.
</div>

</div>

<br>

<!-- 토큰화 결과 비교 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
같은 문장, 다른 토큰화 결과 비교
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
같은 문장이라도 어떤 방식으로 자르느냐에 따라 결과가 달라집니다.
</p>

<div style="background:#0f172a; color:#c3e88d; border-radius:14px; padding:14px 18px; font-weight:900; text-align:center; margin: 16px 0;">
원본: "나는 오늘 학교에 갔다"
</div>

<div style="display: grid; gap: 14px; margin-top: 18px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:10px;">방법 1. 단어 토큰화</div>
    <div style="margin-bottom:10px;">
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"나는"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"오늘"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"학교에"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"갔다"</span>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px; font-size:14px; color:#334155; line-height:1.7;">
      ❌ <b style="color:#FF6B00;">"학교에"</b>와 <b style="color:#FF6B00;">"학교를"</b>을 다른 단어처럼 인식할 수 있습니다.
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:10px;">방법 2. 형태소 토큰화</div>
    <div style="margin-bottom:10px;">
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"나"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"는"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"오늘"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"학교"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"에"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"갔다"</span>
    </div>
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px; font-size:14px; color:#334155; line-height:1.7;">
      ✅ <b style="color:#1681c4;">"학교에"</b>에서 <b style="color:#1681c4;">"학교"</b>를 분리해 같은 단어로 인식할 수 있습니다.
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:10px;">방법 3. 서브워드 토큰화</div>
    <div style="margin-bottom:10px;">
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"나"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"##는"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"오늘"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"학교"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"##에"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"갔"</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">"##다"</span>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px; font-size:14px; color:#334155; line-height:1.7;">
      ✅ 처음 보는 단어도 더 작은 조각으로 나눠 처리할 수 있습니다.
    </div>
  </div>

</div>

</div>

<br>

<!-- 코드 예시 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
방법별 코드 예시
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
단어 토큰화, 형태소 토큰화, 서브워드 토큰화를 코드로 비교해봅니다.
</p>

<!-- 코드 1 -->
<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 18px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 word_tokenization.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      단어 토큰화
    </div>
  </div>
<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
# pip install nltk
import nltk
nltk.download('punkt', quiet=True)
from nltk.tokenize import word_tokenize

sentence = "I'm going to school today."
tokens = word_tokenize(sentence)
print(tokens)
# ["I", "'m", "going", "to", "school", "today", "."]
# ← 축약형("I'm")도 자동으로 분리해줍니다
```

</div>
</div>

<!-- 코드 2 -->
<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 18px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 korean_morph_tokenization.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      형태소 토큰화
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
# pip install konlpy  (Java 8 이상 필요)
from konlpy.tag import Okt

okt = Okt()
sentence = "나는 오늘 학교에 갔다"

# 형태소 분리 — 의미를 가진 최소 단위로 쪼갭니다
print(okt.morphs(sentence))
# ['나', '는', '오늘', '학교', '에', '갔다']

# 품사(POS) 태깅 — 각 토큰의 품사도 함께 출력
print(okt.pos(sentence))
# [('나','Noun'), ('는','Josa'), ('오늘','Noun'),
#  ('학교','Noun'), ('에','Josa'), ('갔다','Verb')]
# Noun=명사, Josa=조사, Verb=동사

# 명사만 추출 — 텍스트 분류에서 가장 많이 사용
print(okt.nouns(sentence))
# ['나', '오늘', '학교']
```
</div>

</div>

<!-- 코드 3 -->
<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 18px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 subword_tokenization.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      서브워드 토큰화
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
# pip install transformers
from transformers import AutoTokenizer

# BERT 계열 토크나이저 불러오기
tok = AutoTokenizer.from_pretrained("bert-base-uncased")

# 처음 보는 단어도 조각으로 나눠서 처리
result = tok.tokenize("unbelievable happiness")
print(result)
# ['un', '##believable', 'happiness']
# ## = 앞 토큰에 이어붙는 조각이라는 표시

# 한국어 BERT
tok_ko = AutoTokenizer.from_pretrained("klue/bert-base")
print(tok_ko.tokenize("나는 학교에 갔다"))
# ['나', '##는', '학교', '##에', '갔', '##다']
```
</div>

</div>

</div>

<br>

<!-- 방식 선택 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
어떤 방식을 써야 할까?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
분석하려는 언어와 사용하는 모델에 따라 적절한 토큰화 방식이 달라집니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 18px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:8px;">한국어 텍스트 분류</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">추천 방식</div>
        <div style="font-size:14px; color:#334155;">형태소 토큰화</div>
      </div>
      <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">라이브러리</div>
        <div style="font-size:14px; color:#334155;">KoNLPy(Okt), kiwipiepy</div>
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:8px;">영어 간단 분석</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">추천 방식</div>
        <div style="font-size:14px; color:#334155;">단어 토큰화</div>
      </div>
      <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">라이브러리</div>
        <div style="font-size:14px; color:#334155;">NLTK</div>
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:8px;">BERT·GPT 계열 모델 사용</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">추천 방식</div>
        <div style="font-size:14px; color:#334155;">서브워드 토큰화</div>
      </div>
      <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">라이브러리</div>
        <div style="font-size:14px; color:#334155;">transformers AutoTokenizer</div>
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:8px;">오타가 많은 데이터</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">추천 방식</div>
        <div style="font-size:14px; color:#334155;">문자 토큰화</div>
      </div>
      <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">라이브러리</div>
        <div style="font-size:14px; color:#334155;">직접 구현</div>
      </div>
    </div>
  </div>

</div>

<div style="margin-top: 18px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 OOV 문제</span><br>
OOV는 <b>Out-Of-Vocabulary</b>의 줄임말로, 학습 때 보지 못한 단어를 처리하지 못하는 문제입니다.<br>
서브워드 방식은 단어를 더 작은 조각으로 쪼개기 때문에 처음 보는 단어도 조각 단위로 다룰 수 있어 OOV 문제를 크게 줄일 수 있습니다.
</div>

</div>

<br>

<!-- 마무리 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; font-weight: 900; font-size: 15px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<span style="color: #FF6B00; font-size: 18px;">⚡</span>
토큰화는 문장을 AI가 처리할 수 있는 작은 단위로 나누는 NLP의 핵심 전처리 단계입니다.
</div>

</div>