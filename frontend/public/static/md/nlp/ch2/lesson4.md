<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #ffffff; border: 1px solid #ffd0b0; color: #ff6b00; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; margin-bottom: 12px;">
NLP 전처리
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
2-4. 불용어 제거
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
불용어 제거는 문장에서 의미 분석에 크게 도움이 되지 않는 단어를 빼고, 
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">핵심 단어만 남기는 과정</span>
입니다.<br>
예를 들어 조사, 접속사, 자주 등장하지만 의미가 약한 단어들을 걸러냅니다.
</p>

</div>

<br>

<!-- 핵심 패턴 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
불용어 제거의 핵심 패턴
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
불용어 제거는 크게 두 가지 방식으로 할 수 있습니다.<br>
직접 불용어 사전을 만들거나, NLTK처럼 이미 준비된 불용어 목록을 사용할 수 있습니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 18px 0;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:8px;">방법 1</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a; margin-bottom:6px;">직접 사전 만들기</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      한국어 조사나 프로젝트에 맞는 단어를 직접 불용어로 지정합니다.
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:8px;">방법 2</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a; margin-bottom:6px;">내장 목록 사용하기</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      NLTK처럼 라이브러리에서 제공하는 영어 불용어 목록을 불러옵니다.
    </div>
  </div>

</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡 핵심 표현</span><br>
<code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:3px 7px; border-radius:6px;">[t for t in tokens if 조건]</code><br>
토큰 목록을 하나씩 확인하면서, 조건을 만족하는 토큰만 새 리스트에 담는 파이썬 표현입니다.
</div>

</div>

<br>

<!-- 코드 줄별 상세 설명 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
코드 줄별 상세 설명
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
불용어 제거 코드를 한 줄씩 나눠서 살펴봅니다.
</p>

<div style="display: grid; gap: 16px; margin-top: 18px;">

<!-- 불용어 사전 정의 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:10px;">1. 불용어 사전 정의</div>
  <div style="margin-bottom: 12px;">
    <span style="display:inline-block; background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px;">STOPWORDS_KO = {'은', '는', '이', '가', '을', '를', '에', ...}</span>
  </div>
  <p style="margin:0 0 12px 0; font-size:14px; color:#475569; line-height:1.7;">
    불용어로 처리할 단어들을 미리 모아둔 사전입니다.<br>
    파이썬에서는 <b style="color:#FF6B00;">set, 즉 집합</b>으로 만들면 검색 속도가 빠릅니다.
  </p>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">list에서 in 검색</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">처음부터 하나씩 비교합니다.<br>시간복잡도: O(n)</div>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">set에서 in 검색</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">해시로 바로 찾습니다.<br>시간복잡도: O(1)</div>
    </div>
  </div>
</div>

<!-- 형태소 분리 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:10px;">2. 형태소 분리</div>
  <div style="margin-bottom: 12px;">
    <span style="display:inline-block; background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px;">tokens = okt.morphs(sentence)</span>
  </div>
  <p style="margin:0 0 12px 0; font-size:14px; color:#475569; line-height:1.7;">
    문장을 의미를 가진 최소 단위로 쪼갭니다.<br>
    불용어 제거를 하려면 먼저 문장이 토큰으로 나뉘어 있어야 합니다.
  </p>
  <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px; font-size:14px; color:#334155; line-height:1.7;">
    <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">"이 영화는 정말"</code>
    →
    <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">['이', '영화', '는', '정말']</code><br>
    이렇게 나뉘어야 <b style="color:#1681c4;">'는'</b>이나 <b style="color:#1681c4;">'정말'</b>을 불용어 사전과 비교할 수 있습니다.
  </div>
</div>

<!-- 리스트 컴프리헨션 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:10px;">3. 불용어 필터링</div>
  <div style="margin-bottom: 12px;">
    <span style="display:inline-block; background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px;">filtered = [t for t in tokens if t not in STOPWORDS_KO]</span>
  </div>
  <p style="margin:0 0 12px 0; font-size:14px; color:#475569; line-height:1.7;">
    토큰을 하나씩 꺼내서 불용어 사전에 없는 것만 남기는 코드입니다.
  </p>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px;">
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">for t in tokens</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">토큰을 하나씩 꺼냅니다.</div>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:4px;">if t not in STOPWORDS_KO</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">불용어가 아닐 때만 통과합니다.</div>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
      <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">filtered</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">통과한 토큰만 모은 새 리스트입니다.</div>
    </div>
  </div>
</div>

<!-- 필터링 예시 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:10px;">4. 필터링 결과 예시</div>
  <div style="display:grid; gap:10px;">
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:3px 8px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin-right:6px;">'이'</span>
      <span style="color:#475569; font-size:14px;">STOPWORDS_KO에 있음 → 제거</span>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:3px 8px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin-right:6px;">'영화'</span>
      <span style="color:#475569; font-size:14px;">STOPWORDS_KO에 없음 → 유지</span>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:3px 8px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin-right:6px;">'는'</span>
      <span style="color:#475569; font-size:14px;">STOPWORDS_KO에 있음 → 제거</span>
    </div>
    <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px;">
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:3px 8px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin-right:6px;">'정말'</span>
      <span style="color:#475569; font-size:14px;">STOPWORDS_KO에 있음 → 제거</span>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px;">
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:3px 8px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin-right:6px;">'재미있었어요'</span>
      <span style="color:#475569; font-size:14px;">STOPWORDS_KO에 없음 → 유지</span>
    </div>
  </div>
</div>

<!-- 명사 추출 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:10px;">5. 명사만 추출하는 단축 메서드</div>
  <div style="margin-bottom: 12px;">
    <span style="display:inline-block; background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px;">nouns = okt.nouns(sentence)</span>
  </div>
  <p style="margin:0; font-size:14px; color:#475569; line-height:1.7;">
    형태소 분리 후 품사 태깅을 하고, 그중 명사만 골라주는 과정을 한 줄로 처리합니다.<br>
    텍스트 분류나 키워드 추출에서 자주 사용됩니다.
  </p>
</div>

<!-- 영어 불용어 -->
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
  <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:10px;">6. NLTK 영어 불용어 목록 로드</div>
  <div style="margin-bottom: 12px;">
    <span style="display:inline-block; background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px;">stop_en = set(stopwords.words('english'))</span>
  </div>
  <p style="margin:0; font-size:14px; color:#475569; line-height:1.7;">
    <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">stopwords.words('english')</code>
    는 영어 불용어 목록을 반환합니다.<br>
    검색 속도를 높이기 위해 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">set()</code>으로 감싸는 것이 좋습니다.
  </p>
</div>

<!-- 부정어 보존 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:10px;">7. 부정어는 반드시 보존하기</div>
  <div style="margin-bottom: 12px;">
    <span style="display:inline-block; background:#0f172a; color:#c3e88d; padding:6px 10px; border-radius:8px; font-family:Consolas, monospace; font-size:13px;">stop_en.discard('not')</span>
  </div>
  <p style="margin:0; font-size:14px; color:#475569; line-height:1.7;">
    <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">discard()</code>
    는 해당 단어가 없어도 오류 없이 넘어갑니다.<br>
    반면 <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">remove()</code>
    는 단어가 없으면 오류가 납니다.
  </p>
  <div style="margin-top:12px; background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">not, no, never, nor</b> 같은 부정어는 감정 분석에서 의미를 뒤집는 핵심 단어이므로 제거하면 안 됩니다.
  </div>
</div>

</div>
</div>

<br>

<!-- 코드 예시 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
불용어 제거 코드 예시
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
한국어 불용어 사전을 만들고, 토큰화된 결과에서 불용어를 제거하는 예시입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 stopword_filtering.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      불용어 제거
    </div>
  </div>

  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.8; overflow-x: auto; white-space: nowrap;">
    <code style="font-family: 'JetBrains Mono', 'Consolas', monospace;">
      <span style="color:#8b8bc7;"># 한국어 불용어 사전</span><br>
      <span style="color:#cdd6f4;">STOPWORDS_KO = {</span><span style="color:#a6e3a1;">'은'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'는'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'이'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'가'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'을'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'를'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'에'</span><span style="color:#cdd6f4;">}</span><br>
      <br>
      <span style="color:#cdd6f4;">sentence = </span><span style="color:#a6e3a1;">"이 영화는 정말 재미있었어요"</span><br>
      <span style="color:#cdd6f4;">tokens = [</span><span style="color:#a6e3a1;">'이'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'영화'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'는'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'정말'</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">'재미있었어요'</span><span style="color:#cdd6f4;">]</span><br>
      <br>
      <span style="color:#8b8bc7;"># 불용어가 아닌 토큰만 남기기</span><br>
      <span style="color:#cdd6f4;">filtered = [t for t in tokens if t not in STOPWORDS_KO]</span><br>
      <br>
      <span style="color:#cdd6f4;">print(filtered)</span><br>
      <span style="color:#8b8bc7;"># ['영화', '정말', '재미있었어요']</span>
    </code>
  </div>
</div>

</div>

<br>

<!-- 제거 금지 단어 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
절대 불용어로 처리하면 안 되는 단어
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
모든 짧고 자주 나오는 단어를 무조건 지우면 안 됩니다.<br>
특히 부정어는 문장의 의미를 완전히 뒤집을 수 있습니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 18px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:10px;">한국어</div>
    <div style="margin-bottom:10px;">
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">않다</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">없다</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">못</span>
      <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">안</span>
    </div>
    <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:12px; font-size:14px; color:#334155; line-height:1.7;">
      예를 들어 <b style="color:#FF6B00;">"재미없다"</b>에서 <b>없다</b>를 제거하면 <b>"재미"</b>만 남아 긍정으로 오분류될 수 있습니다.
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:10px;">영어</div>
    <div style="margin-bottom:10px;">
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">not</span>
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">no</span>
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">never</span>
      <span style="display:inline-block; background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:4px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px; margin:2px;">nor</span>
    </div>
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px; font-size:14px; color:#334155; line-height:1.7;">
      예를 들어 <b style="color:#1681c4;">"not good"</b>에서 <b>not</b>을 제거하면 <b>"good"</b>만 남아 긍정으로 오분류될 수 있습니다.
    </div>
  </div>

</div>

</div>

<br>

<!-- 마무리 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; font-weight: 900; font-size: 15px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<span style="color: #FF6B00; font-size: 18px;">⚡</span>
불용어 제거는 불필요한 단어를 줄여 모델이 핵심 의미에 집중하도록 돕는 전처리 단계입니다.
</div>

</div>