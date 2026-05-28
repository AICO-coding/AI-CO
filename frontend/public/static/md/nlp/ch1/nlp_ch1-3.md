<div style="max-width: 900px; margin: 0 auto; font-family: Pretendard, 'Malgun Gothic', sans-serif; line-height: 1.75; color: #0f172a;">

<div style="background: linear-gradient(135deg, #eef7ff 0%, #ffffff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; margin: 18px 0 24px;">
  <div style="display: inline-block; background: #ffffff; border: 1px solid #ffd0b0; color: #ff6b00; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; margin-bottom: 12px;">NLP 기초 개념</div>
  <h1 style="margin: 0 0 14px; font-size: 30px; font-weight: 900; letter-spacing: -0.7px;">왜 텍스트를 숫자로 바꿔야 할까?</h1>
  <p style="margin: 0; font-size: 15px; color: #334155;">
    컴퓨터는 오직 <b style="color:#1681c4;">숫자(0과 1)</b> 만 처리할 수 있습니다.<br>
    "사과"라는 단어도, "좋아요"라는 감정도 — 컴퓨터 입장에서는 그냥 문자일 뿐,<br>
    계산하거나 비교할 수 없습니다.
  </p>
</div>

<div style="background: #fff3eb; border: 2px solid #ffd0b0; border-radius: 16px; padding: 16px 18px; margin: 0 0 26px;">
  <span style="font-size:18px;">📌</span>
  <b style="color:#ff6b00;">비유</b><br>
  사람은 "사과 ≈ 과일"이라는 걸 직관적으로 알지만, 컴퓨터는 모릅니다.<br>
  두 단어를 <b style="color:#ff6b00;">좌표(숫자 벡터)</b> 로 표현해야 비로소 "얼마나 가까운지" 계산할 수 있습니다.
</div>

<div style="background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 18px; padding: 24px 26px; margin: 0 0 26px;">
  <h2 style="margin: 0 0 18px; font-size: 25px; font-weight: 900;">텍스트 → 숫자 변환 방법의 발전</h2>
  <table style="width:100%; border-collapse: collapse; font-size: 14px;">
    <tr style="background:#0f172a; color:#ffffff;">
      <th style="padding:12px; border:1px solid #e2e8f0; text-align:left;">단계</th>
      <th style="padding:12px; border:1px solid #e2e8f0; text-align:left;">방법</th>
      <th style="padding:12px; border:1px solid #e2e8f0; text-align:left;">핵심 아이디어</th>
    </tr>
    <tr style="background:#ffffff;">
      <td style="padding:12px; border:1px solid #e2e8f0; color:#ff6b00; font-weight:900;">STEP 1</td>
      <td style="padding:12px; border:1px solid #e2e8f0; font-weight:900; color:#475569;">One-Hot Encoding</td>
      <td style="padding:12px; border:1px solid #e2e8f0; color:#475569;">단어 위치만 1로 표시</td>
    </tr>
    <tr style="background:#eef7ff;">
      <td style="padding:12px; border:1px solid #e2e8f0; color:#ff6b00; font-weight:900;">STEP 2</td>
      <td style="padding:12px; border:1px solid #e2e8f0; font-weight:900; color:#475569;">Bag of Words</td>
      <td style="padding:12px; border:1px solid #e2e8f0; color:#475569;">단어 등장 횟수를 셈</td>
    </tr>
    <tr style="background:#ffffff;">
      <td style="padding:12px; border:1px solid #e2e8f0; color:#ff6b00; font-weight:900;">STEP 3</td>
      <td style="padding:12px; border:1px solid #e2e8f0; font-weight:900; color:#475569;">Word2Vec Embedding</td>
      <td style="padding:12px; border:1px solid #e2e8f0; color:#475569;">의미가 가까우면 벡터도 가깝게</td>
    </tr>
  </table>
</div>

<div style="background:#ffffff; border:2px solid #e2e8f0; border-radius:18px; padding:24px 26px; margin:0 0 18px;">
  <div style="display:inline-block; background:#fff3eb; border:1px solid #ffd0b0; color:#ff6b00; padding:4px 10px; border-radius:8px; font-size:13px; font-weight:900;">방법 1</div>
  <h2 style="margin:12px 0 10px; font-size:24px; font-weight:900;">One-Hot Encoding <span style="font-size:15px; color:#64748b;">초기 방식</span></h2>
  <p style="margin:0; font-size:14px; color:#334155;">
    단어 하나를 0과 1로만 이루어진 긴 배열로 표현합니다.<br>
    단어 수만큼 칸이 생기고, 해당 단어 위치만 1, 나머지는 모두 0입니다.
  </p>
  <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:12px; padding:12px 14px; margin-top:14px; font-size:13px;">
    <b style="color:#ff6b00;">단점</b>: "사과"와 "과일"이 얼마나 비슷한지 알 수 없습니다.
  </div>
</div>

</div>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18);">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 one_hot_encoding.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      원-핫 인코딩 코드
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
from sklearn.preprocessing import LabelBinarizer

# 단어 목록(사전)
vocab = ["사과", "과일", "바나나", "먹다"]

lb = LabelBinarizer()
oh = lb.fit_transform(vocab)

print("사과 →", oh[0])   # [1, 0, 0, 0]
print("과일 →", oh[1])   # [0, 1, 0, 0]
# → 두 배열을 비교해도 '의미의 유사성'을 알 수 없음
```

</div>
</div>

<div style="max-width: 900px; margin: 0 auto; font-family: Pretendard, 'Malgun Gothic', sans-serif; line-height: 1.75; color: #0f172a;">

<div style="background:#ffffff; border:2px solid #c2e4ff; border-radius:18px; padding:24px 26px; margin:28px 0 18px;">
  <div style="display:inline-block; background:#ffffff; border:1px solid #ffd0b0; color:#ff6b00; padding:4px 10px; border-radius:8px; font-size:13px; font-weight:900;">방법 2</div>
  <h2 style="margin:12px 0 10px; font-size:24px; font-weight:900;">Bag of Words <span style="font-size:15px; color:#64748b;">단어 빈도 기반</span></h2>
  <p style="margin:0; font-size:14px; color:#334155;">
    문장에 각 단어가 <b style="color:#1681c4;">몇 번 등장하는지</b> 세어서 벡터로 만듭니다.
  </p>
  <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:12px; padding:12px 14px; margin-top:14px; font-size:13px;">
    <b style="color:#ff6b00;">단점</b>: 단어의 순서나 문맥이 완전히 무시됩니다.<br>
    "나는 너를 좋아해" = "너는 나를 좋아해" 로 인식될 수 있습니다.
  </div>
</div>

</div>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18);">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 bag_of_words.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      Bag of Words 코드
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
from sklearn.feature_extraction.text import CountVectorizer

docs = ["사과를 먹다", "바나나를 먹다", "사과 바나나 과일"]

# fit_transform: 사전 구축 + 각 문서를 벡터로 변환
cv = CountVectorizer()
bow = cv.fit_transform(docs).toarray()

print(cv.get_feature_names_out())
# ['과일', '먹다', '바나나', '사과']

print(bow)
# [[0, 1, 0, 1],   ← 사과를 먹다
#  [0, 1, 1, 0],   ← 바나나를 먹다
#  [1, 0, 1, 1]]   ← 사과 바나나 과일
# → 어순·문맥 정보 없음
```
</div>
</div>

<div style="max-width: 900px; margin: 0 auto; font-family: Pretendard, 'Malgun Gothic', sans-serif; line-height: 1.75; color: #0f172a;">

<div style="background:#ffffff; border:2px solid #e2e8f0; border-radius:18px; padding:24px 26px; margin:28px 0 18px;">
  <div style="display:inline-block; background:#fff3eb; border:1px solid #ffd0b0; color:#ff6b00; padding:4px 10px; border-radius:8px; font-size:13px; font-weight:900;">방법 3</div>
  <h2 style="margin:12px 0 10px; font-size:24px; font-weight:900;">Word2Vec 임베딩 <span style="font-size:15px; color:#64748b;">의미 기반</span></h2>
  <p style="margin:0; font-size:14px; color:#334155;">
    의미가 비슷한 단어끼리 <b style="color:#1681c4;">숫자 공간에서 가깝게</b> 위치하도록 학습합니다.<br>
    벡터끼리 수학 연산이 가능해집니다.
  </p>
</div>

</div>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18);">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 word2vec_embedding.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      Word2Vec 임베딩 코드
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.7; overflow-x: auto;">

```python
# pip install gensim
from gensim.models import Word2Vec

sentences = [
    ["사과", "과일", "맛있다"],
    ["바나나", "과일", "달다"],
    ["왕", "남자", "여왕", "여자"],
]

# vector_size: 각 단어를 몇 차원 벡터로 표현할지
# min_count: 최소 등장 횟수 (1 = 모든 단어 포함)
model = Word2Vec(sentences, vector_size=50, min_count=1)

# 의미적으로 유사한 단어 찾기
sim = model.wv.most_similar("사과", topn=2)
print(sim)
# [('바나나', 0.93), ('과일', 0.89)]
# → 숫자만으로 의미 관계 표현 성공!

# 유명한 벡터 연산 예시
# 왕 - 남자 + 여자 ≈ 여왕
result = model.wv.most_similar(
    positive=["왕", "여자"],
    negative=["남자"]
)
print(result[0])  # ('여왕', 0.91)
```
</div>
</div>

<div style="max-width: 900px; margin: 0 auto; font-family: Pretendard, 'Malgun Gothic', sans-serif; line-height: 1.75; color: #0f172a;">

<div style="background: linear-gradient(135deg, #fff7ed 0%, #fffaf5 100%); border: 2px solid #ffd0b0; border-radius: 18px; padding: 18px 20px; margin: 26px 0 8px;">
  <span style="font-size:20px;">💡</span>
  최신 모델(BERT, GPT)은 <b style="color:#ff6b00;">문맥까지 반영한 동적 임베딩</b>을 사용합니다.<br>
  같은 "배"라는 단어도 "과일 배"인지 "타는 배(船)"인지 문맥으로 구별합니다.
</div>

</div>
