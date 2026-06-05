<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a; line-height: 1.75;">

  <div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 22px rgba(15, 23, 42, 0.06); margin-bottom: 22px;">
    <div style="display: inline-block; background: #ffffff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 5px 11px; border-radius: 999px; font-size: 12px; font-weight: 900; margin-bottom: 12px;">NLP 흐름</div>
    <h1 style="margin: 0 0 14px; font-size: 30px; font-weight: 900; letter-spacing: -0.7px; color: #0f172a;">NLP의 기본 처리 흐름</h1>
    <p style="margin: 0; font-size: 15px; color: #334155;">
      NLP는 보통 <b style="color: #1681c4;">텍스트를 입력받고</b>, 문장을 정리한 뒤,
      작은 단위로 나누고, 숫자로 바꿔서 모델이 처리하는 순서로 진행됩니다.
    </p>
  </div>

  <div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 18px; padding: 24px 26px; box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04); margin-bottom: 22px;">
    <h2 style="margin: 0 0 18px; font-size: 24px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">전체 흐름 한눈에 보기</h2>
    <div style="display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 10px;">
      <div style="background: #ffffff; border: 1px solid #dbeafe; border-radius: 14px; padding: 14px 10px; text-align: center;">
        <div style="color: #FF6B00; font-weight: 900; font-size: 12px; margin-bottom: 5px;">STEP 1</div>
        <div style="font-weight: 900; font-size: 14px;">텍스트 입력</div>
      </div>
      <div style="background: #ffffff; border: 1px solid #dbeafe; border-radius: 14px; padding: 14px 10px; text-align: center;">
        <div style="color: #FF6B00; font-weight: 900; font-size: 12px; margin-bottom: 5px;">STEP 2</div>
        <div style="font-weight: 900; font-size: 14px;">전처리</div>
      </div>
      <div style="background: #ffffff; border: 1px solid #dbeafe; border-radius: 14px; padding: 14px 10px; text-align: center;">
        <div style="color: #FF6B00; font-weight: 900; font-size: 12px; margin-bottom: 5px;">STEP 3</div>
        <div style="font-weight: 900; font-size: 14px;">토큰화</div>
      </div>
      <div style="background: #ffffff; border: 1px solid #dbeafe; border-radius: 14px; padding: 14px 10px; text-align: center;">
        <div style="color: #FF6B00; font-weight: 900; font-size: 12px; margin-bottom: 5px;">STEP 4</div>
        <div style="font-weight: 900; font-size: 14px;">숫자 표현</div>
      </div>
      <div style="background: #ffffff; border: 1px solid #dbeafe; border-radius: 14px; padding: 14px 10px; text-align: center;">
        <div style="color: #FF6B00; font-weight: 900; font-size: 12px; margin-bottom: 5px;">STEP 5</div>
        <div style="font-weight: 900; font-size: 14px;">모델 처리</div>
      </div>
      <div style="background: #ffffff; border: 1px solid #dbeafe; border-radius: 14px; padding: 14px 10px; text-align: center;">
        <div style="color: #FF6B00; font-weight: 900; font-size: 12px; margin-bottom: 5px;">STEP 6</div>
        <div style="font-weight: 900; font-size: 14px;">결과 출력</div>
      </div>
    </div>
  </div>

  <div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'D2Coding', monospace; box-shadow: 0 8px 20px rgba(15,23,42,0.12); margin-bottom: 26px;">
    <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 10px 15px; display: flex; align-items: center; justify-content: space-between;">
      <div style="display: flex; align-items: center; gap: 6px;">
        <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
        <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
        <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
        <span style="color: #94a3b8; margin-left: 8px; font-size: 12px;">📄 nlp_pipeline.txt</span>
      </div>
      <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; font-family: 'Nunito', sans-serif;">처리 순서</div>
    </div>
    <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.75; overflow-x: auto;">

```text
1. 텍스트 입력
2. 전처리
3. 토큰화
4. 숫자 표현
5. 모델 처리
6. 결과 출력
```

  </div>
</div>

<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 28px; box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04); margin-bottom: 22px;">
  <div style="display: inline-block; background: #fff3eb; border: 1px solid #ffd0b0; color: #FF6B00; padding: 4px 10px; border-radius: 8px; font-weight: 900; font-size: 13px; margin-bottom: 10px;">1단계</div>
  <h2 style="margin: 0 0 12px; font-size: 24px; font-weight: 900; color: #0f172a;">텍스트 입력</h2>
  <p style="margin: 0; color: #334155; font-size: 14px;">먼저 사용자가 문장을 입력합니다. 이 문장은 감성 분석기에 넣을 문장이라고 해봅시다.</p>
</div>

```text
I LOVE this movie!!!
```

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 28px; box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04); margin-bottom: 22px;">
  <div style="display: inline-block; background: #ffffff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 4px 10px; border-radius: 8px; font-weight: 900; font-size: 13px; margin-bottom: 10px;">2단계</div>
  <h2 style="margin: 0 0 12px; font-size: 24px; font-weight: 900; color: #0f172a;">전처리</h2>
  <p style="margin: 0; color: #334155; font-size: 14px;">
    전처리는 문장을 깔끔하게 정리하는 과정입니다.<br>
    예를 들어 대문자를 소문자로 바꾸고, 느낌표 같은 특수문자를 제거할 수 있습니다.
  </p>
</div>

<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin-bottom: 22px;">
  <div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 16px; padding: 18px;">
    <div style="color: #64748b; font-size: 12px; font-weight: 900; margin-bottom: 8px;">전처리 전</div>

```text
I LOVE this movie!!!
```

  </div>
  <div style="background: #ffffff; border: 2px solid #c2e4ff; border-radius: 16px; padding: 18px;">
    <div style="color: #1681c4; font-size: 12px; font-weight: 900; margin-bottom: 8px;">전처리 후</div>

```text
i love this movie
```

  </div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; border-radius: 16px; padding: 16px 18px; margin-bottom: 22px; color: #0f172a; font-size: 14px;">
  <b style="color: #FF6B00;">왜 필요할까?</b><br>
  같은 단어라도 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">LOVE</code>,
  <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">love</code>,
  <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">love!!!</code> 는 컴퓨터에게 다르게 보일 수 있습니다.
  그래서 전처리가 필요합니다.
</div>

<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 28px; box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04); margin-bottom: 22px;">
  <div style="display: inline-block; background: #fff3eb; border: 1px solid #ffd0b0; color: #FF6B00; padding: 4px 10px; border-radius: 8px; font-weight: 900; font-size: 13px; margin-bottom: 10px;">3단계</div>
  <h2 style="margin: 0 0 12px; font-size: 24px; font-weight: 900; color: #0f172a;">토큰화</h2>
  <p style="margin: 0; color: #334155; font-size: 14px;">토큰화는 문장을 작은 단위로 나누는 과정입니다. 이렇게 나누면 컴퓨터가 단어 하나하나를 따로 처리할 수 있습니다.</p>
</div>

```text
i love this movie
```

```text
["i", "love", "this", "movie"]
```

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 28px; box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04); margin-bottom: 22px;">
  <div style="display: inline-block; background: #ffffff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 4px 10px; border-radius: 8px; font-weight: 900; font-size: 13px; margin-bottom: 10px;">4단계</div>
  <h2 style="margin: 0 0 12px; font-size: 24px; font-weight: 900; color: #0f172a;">숫자 표현</h2>
  <p style="margin: 0; color: #334155; font-size: 14px;">
    컴퓨터는 문장을 바로 이해하지 못하기 때문에, 단어를 숫자로 바꿉니다.<br>
    예를 들어 단어에 번호를 붙이면 이렇게 됩니다.
  </p>
</div>

```text
i = 1
love = 2
this = 3
movie = 4
```

```text
[1, 2, 3, 4]
```

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 16px; padding: 18px 20px; margin-bottom: 22px;">
  <div style="color: #64748b; font-size: 12px; font-weight: 900; margin-bottom: 8px;">나중에 배우는 더 좋은 표현 방식</div>
  <span style="background:#ffffff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 8px; border-radius:7px; font-weight:900; font-size:13px;">BoW</span>
  <span style="background:#ffffff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 8px; border-radius:7px; font-weight:900; font-size:13px; margin-left:6px;">TF-IDF</span>
  <span style="background:#ffffff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 8px; border-radius:7px; font-weight:900; font-size:13px; margin-left:6px;">임베딩</span>
</div>

<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 28px; box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04); margin-bottom: 22px;">
  <div style="display: inline-block; background: #fff3eb; border: 1px solid #ffd0b0; color: #FF6B00; padding: 4px 10px; border-radius: 8px; font-weight: 900; font-size: 13px; margin-bottom: 10px;">5단계</div>
  <h2 style="margin: 0 0 12px; font-size: 24px; font-weight: 900; color: #0f172a;">모델 처리</h2>
  <p style="margin: 0; color: #334155; font-size: 14px;">
    숫자로 바뀐 문장을 모델에 넣습니다.<br>
    모델은 숫자를 보고 결과를 예측합니다. 감성 분석의 경우, 모델은 문장이 긍정인지 부정인지 판단합니다.
  </p>
</div>

```text
모델 판단: 긍정
```

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 28px; box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04); margin-bottom: 22px;">
  <div style="display: inline-block; background: #ffffff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 4px 10px; border-radius: 8px; font-weight: 900; font-size: 13px; margin-bottom: 10px;">6단계</div>
  <h2 style="margin: 0 0 12px; font-size: 24px; font-weight: 900; color: #0f172a;">결과 출력</h2>
  <p style="margin: 0; color: #334155; font-size: 14px;">마지막으로 사용자에게 결과를 보여줍니다.</p>
</div>

```text
긍정 리뷰입니다.
```

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'D2Coding', monospace; box-shadow: 0 8px 20px rgba(15,23,42,0.12); margin-bottom: 26px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 10px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #94a3b8; margin-left: 8px; font-size: 12px;">📄 full_example.txt</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; font-family: 'Nunito', sans-serif;">전체 예시</div>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.75; overflow-x: auto;">

```text
I LOVE this movie!!!
→ i love this movie
→ ["i", "love", "this", "movie"]
→ [1, 2, 3, 4]
→ 모델 판단
→ 긍정 리뷰입니다.
```

  </div>
</div>

<div style="background: linear-gradient(135deg, #fff7ed 0%, #fffaf5 100%); border: 2px solid #ffd0b0; border-radius: 18px; padding: 20px 22px; margin-bottom: 10px;">
  <div style="display: flex; align-items: flex-start; gap: 12px;">
    <div style="font-size: 22px; line-height: 1;">💡</div>
    <div style="font-size: 14px; color: #0f172a;">
      핵심은 <b style="color: #FF6B00;">문자 → 정리된 단어 → 숫자 → 모델 예측</b> 순서입니다.<br>
      NLP 모델은 결국 숫자로 바뀐 언어 정보를 보고 판단합니다.
    </div>
  </div>
</div>

</div>
