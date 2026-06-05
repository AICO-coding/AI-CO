<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #ffffff; border: 1px solid #ffd0b0; color: #ff6b00; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; margin-bottom: 12px;">
NLP 전처리
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
2-5. 정규화 & 어간 추출
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
정규화와 어간 추출은 표현은 다르지만 의미가 비슷한 단어들을 
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">같은 형태로 맞추는 과정</span>
입니다.<br>
쉽게 말해, 같은 말은 같게 보이도록 정리하는 단계입니다.
</p>

</div>

<br>

<!-- 개념 설명 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
"달리다"와 "달렸다"는 같은 동사다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
사람은 
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">run</code>,
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">running</code>,
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">ran</code>
이 같은 동사라는 것을 압니다.<br>
하지만 컴퓨터는 이 세 단어를 완전히 다른 단어로 볼 수 있습니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 18px 0;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:8px;">정규화 Normalization</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      대소문자, 숫자, 축약형처럼 표현 방식을 통일합니다.
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:8px;">어간/표제어 추출</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      활용된 단어를 기본형이나 원형에 가깝게 바꿉니다.
    </div>
  </div>

</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡 사전 비유</span><br>
사전에서 단어를 찾을 때 <b>"달렸다"</b>를 찾으면 나오지 않고, <b>"달리다"</b>를 찾아야 합니다.<br>
어간 추출과 표제어 추출은 여러 활용형을 사전에 나오는 형태로 바꾸는 작업입니다.
</div>

</div>

<br>

<!-- 정규화 코드 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
정규화 Normalization
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
정규화는 단어의 표현 방식을 통일하는 과정입니다.<br>
대소문자 통일, 숫자 대체, 영어 축약형 확장 등이 대표적입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 normalization.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      정규화 코드
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
import re

# ① 대소문자 통일 (영어)
texts = ["Apple", "APPLE", "apple"]
unified = [t.lower() for t in texts]
print(unified)  # ['apple', 'apple', 'apple']

# ② 숫자를 [NUM] 태그로 대체
# 숫자 자체보다 "숫자가 있다"는 사실이 중요할 때
text = "2024년에 5억 원을 투자했습니다."
text = re.sub(r'\d+', '[NUM]', text)
print(text)  # "[NUM]년에 [NUM]억 원을 투자했습니다."

# ③ 영어 축약형 확장
contractions = {
    "isn't": "is not",  "can't": "cannot",
    "won't": "will not", "I'm": "I am",
}
text = "I'm happy that it isn't raining"
for short, full in contractions.items():
    text = text.replace(short, full)
print(text)  # "I am happy that it is not raining"
```
</div>

</div>

</div>

<br>

<!-- 어간 vs 표제어 비교 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
어간 추출 vs 표제어 추출 비교
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
둘 다 단어를 기본형에 가깝게 만드는 방법이지만, 정확도와 처리 방식이 다릅니다.
</p>

<div style="background:#0f172a; color:#c3e88d; border-radius:14px; padding:14px 18px; font-weight:900; text-align:center; margin: 16px 0;">
같은 동사 run의 다양한 형태: run · running · ran · runs · runner
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 18px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:10px;">어간 추출 후</div>
    <div style="margin-bottom:10px;">
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">run</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">run</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">ran</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">run</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">runner</span>
    </div>
    <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px; font-size:14px; color:#334155; line-height:1.7;">
      빠르지만 불완전합니다.<br>
      <b style="color:#FF6B00;">ran</b>이 <b>run</b>으로 바뀌지 않을 수 있습니다.
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:10px;">표제어 추출 후</div>
    <div style="margin-bottom:10px;">
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">run</span>
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">run</span>
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">run</span>
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">run</span>
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">run</span>
    </div>
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px; font-size:14px; color:#334155; line-height:1.7;">
      느리지만 더 정확합니다.<br>
      문맥과 품사를 고려해 단어를 원형으로 통일합니다.
    </div>
  </div>

</div>

</div>

<br>

<!-- 어간 추출 코드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
어간 추출 Stemming
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
어간 추출은 단어의 끝부분을 규칙에 따라 잘라내는 방식입니다.<br>
처리 속도는 빠르지만, 결과가 실제 단어가 아닐 수도 있습니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 stemming.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      어간 추출
    </div>
  </div>
<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["running", "happily", "studies", "connection"]
for w in words:
    print(f"{w:15} → {ps.stem(w)}")

# running         → run       (정확)
# happily         → happili   (부정확! 실제 단어 아님)
# studies         → studi     (부정확! 실제 단어 아님)
# connection      → connect   (정확)
```

</div>
</div>

</div>

<br>

<!-- 표제어 추출 코드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
표제어 추출 Lemmatization
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
표제어 추출은 단어의 품사와 문맥을 고려해 사전에 등재된 원형으로 바꾸는 방식입니다.<br>
어간 추출보다 느리지만, 결과가 더 정확합니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 lemmatization.py</span>
    </div>
    <div style="background-color: rgba(22,129,196,.2); color: #1681c4; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      표제어 추출
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
# pip install spacy
# python -m spacy download en_core_web_sm
import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("The cats were running and they ran away better")
for token in doc:
    print(f"{token.text:10} → {token.lemma_:10} ({token.pos_})")

# cats       → cat        (NOUN)   ← 복수 → 단수
# were       → be         (AUX)    ← 과거 → 원형
# running    → run        (VERB)   ← 진행형 → 원형
# ran        → run        (VERB)   ← 과거형 → 원형
# better     → well       (ADV)    ← 비교급 → 원형
```
</div>
</div>

</div>

<br>

<!-- 한국어 원형 복원 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
한국어 원형 복원
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
한국어에서는 KoNLPy의 Okt를 사용해 동사와 형용사를 원형에 가깝게 복원할 수 있습니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 korean_stemming.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      한국어 원형 복원
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
from konlpy.tag import Okt

okt = Okt()

# stem=True: 동사·형용사를 원형으로 복원
# norm=True: 반복 문자 정규화 ("ㅋㅋㅋ" 처리 등)
sentence = "나는 밥을 먹었어요. 정말 맛있었습니다"
result = okt.pos(sentence, norm=True, stem=True)

for word, pos in result:
    print(f"{word:10} ({pos})")

# 나          (Noun)
# 밥          (Noun)
# 먹다        (Verb)      ← "먹었어요" → "먹다"
# 정말        (Adverb)
# 맛있다      (Adjective) ← "맛있었습니다" → "맛있다"
```

</div>
</div>

</div>

<br>

<!-- 언제 뭘 쓸까 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
어간 추출 vs 표제어 추출 — 언제 뭘 쓸까?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
목적이 속도인지, 정확도인지에 따라 선택이 달라집니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 18px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:8px;">속도</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">어간 추출</div>
        <div style="font-size:14px; color:#334155;">빠름</div>
      </div>
      <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">표제어 추출</div>
        <div style="font-size:14px; color:#334155;">느림</div>
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:8px;">정확도</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">어간 추출</div>
        <div style="font-size:14px; color:#334155;">낮음</div>
      </div>
      <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">표제어 추출</div>
        <div style="font-size:14px; color:#334155;">높음</div>
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:8px;">결과 형태</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">어간 추출</div>
        <div style="font-size:14px; color:#334155;">실제 단어가 아닐 수 있음</div>
      </div>
      <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">표제어 추출</div>
        <div style="font-size:14px; color:#334155;">항상 실제 단어에 가까움</div>
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:8px;">추천 상황</div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
      <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">어간 추출</div>
        <div style="font-size:14px; color:#334155;">대량 데이터 빠른 처리</div>
      </div>
      <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px;">
        <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">표제어 추출</div>
        <div style="font-size:14px; color:#334155;">정확성이 중요한 분석</div>
      </div>
    </div>
  </div>

</div>

<div style="margin-top: 18px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 실무 권장</span><br>
정확도가 중요한 감정 분석, 질의응답 태스크에서는 <b>표제어 추출</b>을 사용하는 것이 좋습니다.<br>
수백만 건의 데이터를 빠르게 처리해야 한다면 <b>어간 추출</b>도 실용적인 선택입니다.
</div>

</div>

<br>

<!-- 마무리 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; font-weight: 900; font-size: 15px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<span style="color: #FF6B00; font-size: 18px;">⚡</span>
정규화와 어간·표제어 추출은 서로 다르게 생긴 단어들을 같은 의미 단위로 맞춰 모델이 더 안정적으로 학습하도록 돕습니다.
</div>

</div>