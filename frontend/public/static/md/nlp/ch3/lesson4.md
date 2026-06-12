<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
원-핫 인코딩 (One-Hot Encoding)
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 7px; border-radius:6px; font-weight:900;">sklearn</code>을 활용해 원-핫 인코딩을 직접 구현하고, 코드를 단계별로 이해합니다.
</p>

</div>

<br>

<!-- 실습 코드 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💻 실습 코드
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
아래 코드를 보고 각 단계가 어떤 역할을 하는지 확인해보세요!
</p>

<!-- 코드 블록 -->
<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 one_hot_encoding.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      원-핫 인코딩
    </div>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.9; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;"># 필요한 라이브러리 불러오기</span>
<span style="color:#cba6f7;">from</span> <span style="color:#89dceb;">sklearn.preprocessing</span> <span style="color:#cba6f7;">import</span> <span style="color:#cdd6f4;">LabelEncoder, OneHotEncoder</span>
<span style="color:#cba6f7;">import</span> <span style="color:#89dceb;">numpy</span> <span style="color:#cba6f7;">as</span> <span style="color:#cdd6f4;">np</span>

<span style="color:#6c7086;"># ① 예시 문장과 단어 목록 준비</span>
<span style="color:#cdd6f4;">sentences = [</span><span style="color:#a6e3a1;">"나는 밥을 먹었다"</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">"나는 물을 마셨다"</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">"고양이가 밥을 먹었다"</span><span style="color:#cdd6f4;">]</span>

<span style="color:#6c7086;"># 문장을 단어 단위로 분리하고 중복 제거 → 단어 사전 만들기</span>
<span style="color:#cdd6f4;">vocab = list(set(word </span><span style="color:#cba6f7;">for</span><span style="color:#cdd6f4;"> sentence </span><span style="color:#cba6f7;">in</span><span style="color:#cdd6f4;"> sentences </span><span style="color:#cba6f7;">for</span><span style="color:#cdd6f4;"> word </span><span style="color:#cba6f7;">in</span><span style="color:#cdd6f4;"> sentence.split()))</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"단어 사전:"</span><span style="color:#cdd6f4;">, vocab)</span>
<span style="color:#6c7086;"># 예시 출력: ['먹었다', '나는', '밥을', '마셨다', '물을', '고양이가']</span>

<span style="color:#6c7086;"># ② 각 단어에 정수 인덱스 부여 (LabelEncoder)</span>
<span style="color:#cdd6f4;">label_encoder = LabelEncoder()</span>
<span style="color:#cdd6f4;">integer_encoded = label_encoder.fit_transform(vocab)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"정수 인코딩 결과:"</span><span style="color:#cdd6f4;">, integer_encoded)</span>
<span style="color:#6c7086;"># 예시 출력: [0 1 2 3 4 5]  (알파벳/가나다 순으로 자동 정렬)</span>

<span style="color:#6c7086;"># ③ 정수 → 원-핫 벡터로 변환 (OneHotEncoder)</span>
<span style="color:#cdd6f4;">onehot_encoder = OneHotEncoder(sparse_output=</span><span style="color:#89dceb;">False</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cdd6f4;">integer_encoded_reshaped = integer_encoded.reshape(-</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">, </span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">)  </span><span style="color:#6c7086;"># 2D 형태로 변환</span>
<span style="color:#cdd6f4;">onehot_encoded = onehot_encoder.fit_transform(integer_encoded_reshaped)</span>

<span style="color:#6c7086;"># ④ 결과 출력</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"\n[원-핫 인코딩 결과]"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">for</span><span style="color:#cdd6f4;"> word, vector </span><span style="color:#cba6f7;">in</span><span style="color:#cdd6f4;"> zip(vocab, onehot_encoded):</span>
<span style="color:#cdd6f4;">    </span><span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"  '{word}': {vector.astype(int).tolist()}"</span><span style="color:#cdd6f4;">)</span>

<span style="color:#6c7086;"># ⑤ 특정 단어 조회</span>
<span style="color:#cdd6f4;">target_word = </span><span style="color:#a6e3a1;">"밥을"</span>
<span style="color:#cdd6f4;">target_idx = label_encoder.transform([target_word])</span>
<span style="color:#cdd6f4;">target_vector = onehot_encoder.transform(target_idx.reshape(-</span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">, </span><span style="color:#89dceb;">1</span><span style="color:#cdd6f4;">))</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"\n'{target_word}'의 원-핫 벡터: {target_vector.astype(int).tolist()[0]}"</span><span style="color:#cdd6f4;">)</span></div>
</div>

<!-- 출력 결과 -->
<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">출력 결과 예시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">단어 사전: ['먹었다', '나는', '밥을', '마셨다', '물을', '고양이가']</span>
<span style="color:#6c7086;">정수 인코딩 결과: [2 1 4 0 5 3]</span>

<span style="color:#a6e3a1;">[원-핫 인코딩 결과]</span>
<span style="color:#cdd6f4;">  '먹었다': [0, 0, 1, 0, 0, 0]</span>
<span style="color:#cdd6f4;">  '나는':   [0, 1, 0, 0, 0, 0]</span>
<span style="color:#cdd6f4;">  '밥을':   [0, 0, 0, 0, 1, 0]</span>
<span style="color:#cdd6f4;">  '마셨다': [1, 0, 0, 0, 0, 0]</span>
<span style="color:#cdd6f4;">  '물을':   [0, 0, 0, 0, 0, 1]</span>
<span style="color:#cdd6f4;">  '고양이가':[0, 0, 0, 1, 0, 0]</span>

<span style="color:#a6e3a1;">'밥을'의 원-핫 벡터: [0, 0, 0, 0, 1, 0]</span></div>
</div>

</div>

<br>

<!-- 단계별 설명 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔍 코드 단계별 설명
</h2>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<!-- STEP 1 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 1</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">단어 사전 만들기</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#c3e88d; margin-bottom:12px;">
    vocab = list(set(word for sentence in sentences for word in sentence.split()))
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">sentence.split()</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">공백 기준으로 단어를 쪼갭니다.<br><span style="color:#6c7086;">ex) "나는 밥을 먹었다" → ["나는", "밥을", "먹었다"]</span></div>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">set(...)</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">중복 단어를 제거합니다.<br><span style="color:#6c7086;">ex) "나는"이 여러 문장에 나와도 한 번만 등록</span></div>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">list(...)</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">다루기 쉬운 리스트로 변환합니다.</div>
    </div>
  </div>
</div>

<!-- STEP 2 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 2</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">LabelEncoder: 단어 → 정수</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#c3e88d; margin-bottom:12px; line-height:1.9;">
    label_encoder = LabelEncoder()<br>
    integer_encoded = label_encoder.fit_transform(vocab)
  </div>
  <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px; font-size:14px; color:#334155; line-height:1.7; margin-bottom:12px;">
    <b style="color:#1681c4;">LabelEncoder</b>는 문자열을 정수로 변환하는 도구입니다.<br>
    <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">fit_transform()</code>은 단어 목록을 학습하고(fit), 동시에 변환(transform)합니다.<br>
    <b>"가나다" 순으로 자동 정렬</b> 후 0, 1, 2... 번호를 부여합니다.
  </div>
  <div style="display:grid; grid-template-columns:repeat(6,1fr); gap:8px; text-align:center;">
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 4px;">
      <div style="font-size:11px; color:#1681c4; font-weight:900;">고양이가</div>
      <div style="font-size:18px; font-weight:900; color:#FF6B00;">0</div>
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 4px;">
      <div style="font-size:11px; color:#1681c4; font-weight:900;">나는</div>
      <div style="font-size:18px; font-weight:900; color:#FF6B00;">1</div>
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 4px;">
      <div style="font-size:11px; color:#1681c4; font-weight:900;">마셨다</div>
      <div style="font-size:18px; font-weight:900; color:#FF6B00;">2</div>
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 4px;">
      <div style="font-size:11px; color:#1681c4; font-weight:900;">먹었다</div>
      <div style="font-size:18px; font-weight:900; color:#FF6B00;">3</div>
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 4px;">
      <div style="font-size:11px; color:#1681c4; font-weight:900;">밥을</div>
      <div style="font-size:18px; font-weight:900; color:#FF6B00;">4</div>
    </div>
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 4px;">
      <div style="font-size:11px; color:#1681c4; font-weight:900;">물을</div>
      <div style="font-size:18px; font-weight:900; color:#FF6B00;">5</div>
    </div>
  </div>
</div>

<!-- STEP 3 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">STEP 3</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">OneHotEncoder: 정수 → 원-핫 벡터</div>
  </div>
  <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#c3e88d; margin-bottom:12px; line-height:1.9;">
    onehot_encoder = OneHotEncoder(sparse_output=False)<br>
    integer_encoded_reshaped = integer_encoded.reshape(-1, 1)<br>
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded_reshaped)
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">reshape(-1, 1)</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">OneHotEncoder는 2D 입력이 필요해서 형태를 바꿔줍니다.<br>
      <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 4px; border-radius:4px;">[0, 1, 2]</code> → <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 4px; border-radius:4px;">[[0], [1], [2]]</code></div>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">sparse_output=False</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">결과를 일반 배열로 반환합니다.<br>
      정수 4인 단어 → <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 4px; border-radius:4px;">[0, 0, 0, 0, 1, 0]</code></div>
    </div>
  </div>
</div>

</div>
</div>

</div>