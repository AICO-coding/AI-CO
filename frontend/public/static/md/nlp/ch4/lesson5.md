<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
  Chapter 04 · Attention
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Attention Score 직접 계산하기
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
앞에서 배운
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">score(Q, K) = (Q · K) / √d</span>
공식을 NumPy 코드로 직접 구현합니다.<br>
오른쪽 빈칸 파일에서 핵심 부분을 채워보세요.
</p>

</div>

<br>

<!-- STEP 정리 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
코드 흐름 — 3단계 요약
</h2>

<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 16px; text-align:center;">
    <div style="background:#0f172a; color:#c3e88d; padding:3px 10px; border-radius:999px; font-size:11px; font-weight:900; display:inline-block; margin-bottom:8px;">STEP 1</div>
    <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:4px;">내적 계산</div>
    <div style="font-size:13px; color:#475569; line-height:1.6;"><code style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:2px 5px; border-radius:4px;">Q @ K.T</code><br>Query와 모든 Key의 유사도</div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:14px 16px; text-align:center;">
    <div style="background:#0f172a; color:#c3e88d; padding:3px 10px; border-radius:999px; font-size:11px; font-weight:900; display:inline-block; margin-bottom:8px;">STEP 2</div>
    <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:4px;">√d 로 나누기</div>
    <div style="font-size:13px; color:#475569; line-height:1.6;"><code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 5px; border-radius:4px;">/ np.sqrt(d)</code><br>점수 크기 안정화</div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 16px; text-align:center;">
    <div style="background:#0f172a; color:#c3e88d; padding:3px 10px; border-radius:999px; font-size:11px; font-weight:900; display:inline-block; margin-bottom:8px;">STEP 3</div>
    <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:4px;">결과 확인</div>
    <div style="font-size:13px; color:#475569; line-height:1.6;">각 단어 쌍의 Score를 행렬로 출력</div>
  </div>

</div>

</div>

<br>

<!-- 완전체 코드 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💻 완전체 코드
</h2>

<!-- 코드 블록 -->
<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 attention_score.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      Attention Score 완전체 코드
    </div>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.9; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#cba6f7;">import</span> <span style="color:#89dceb;">numpy</span> <span style="color:#cba6f7;">as</span> <span style="color:#cdd6f4;">np</span>

<span style="color:#6c7086;"># ── 입력: Query 행렬과 Key 행렬 ──────────────────────────────
# 단어가 3개, 각 단어를 4차원 벡터로 표현
# 실제 Transformer에서는 Q, K가 별도 가중치로 만들어지지만
# 여기서는 단어 벡터를 그대로 Q, K로 씁니다 (개념 이해용)</span>
<span style="color:#cdd6f4;">Q = np.array([</span>
<span style="color:#cdd6f4;">    [</span><span style="color:#89dceb;">1.0, 0.2, 0.1, 0.5</span><span style="color:#cdd6f4;">],  </span><span style="color:#6c7086;"># "나는"</span>
<span style="color:#cdd6f4;">    [</span><span style="color:#89dceb;">0.8, 1.0, 0.3, 0.2</span><span style="color:#cdd6f4;">],  </span><span style="color:#6c7086;"># "사과를"</span>
<span style="color:#cdd6f4;">    [</span><span style="color:#89dceb;">0.2, 0.9, 1.0, 0.7</span><span style="color:#cdd6f4;">],  </span><span style="color:#6c7086;"># "먹었다"</span>
<span style="color:#cdd6f4;">])</span>
<span style="color:#cdd6f4;">K = Q.copy()  </span><span style="color:#6c7086;"># 개념 이해용: Q와 K를 동일하게 설정</span>

<span style="color:#6c7086;"># ── STEP 1: 내적 (Q @ K^T) ───────────────────────────────────
# Q : (3, 4),  K.T : (4, 3)  →  결과: (3, 3) 행렬
# scores[i][j] = i번째 단어가 j번째 단어를 얼마나 주목하는지</span>
<span style="color:#cdd6f4;">scores_raw = Q @ K.T</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"[STEP 1] 내적 결과 (raw scores):"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(np.round(scores_raw,</span><span style="color:#89dceb;">2</span><span style="color:#cdd6f4;">))</span>

<span style="color:#6c7086;"># ── STEP 2: √d 로 나누기 (Scaling) ──────────────────────────
# d = 벡터의 차원 수 (여기서는 4)
# np.sqrt(d) 로 나눠서 점수 크기를 안정화</span>
<span style="color:#cdd6f4;">d = Q.shape[</span><span style="color:#89dceb;">-1</span><span style="color:#cdd6f4;">]          </span><span style="color:#6c7086;"># 마지막 축의 크기 = 차원 수</span>
<span style="color:#cdd6f4;">scores = scores_raw / np.sqrt(d)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"\n[STEP 2] Scaled Attention Scores:"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(np.round(scores,</span><span style="color:#89dceb;">2</span><span style="color:#cdd6f4;">))</span>

<span style="color:#6c7086;"># ── 결과 해석 출력 ───────────────────────────────────────────</span>
<span style="color:#cdd6f4;">words = [</span><span style="color:#a6e3a1;">"나는"</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">"사과를"</span><span style="color:#cdd6f4;">, </span><span style="color:#a6e3a1;">"먹었다"</span><span style="color:#cdd6f4;">]</span>
<span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">"\n[해석] '먹었다'가 각 단어에 매긴 점수:"</span><span style="color:#cdd6f4;">)</span>
<span style="color:#cba6f7;">for</span> <span style="color:#cdd6f4;">word, score </span><span style="color:#cba6f7;">in</span> <span style="color:#cdd6f4;">zip(words, scores[</span><span style="color:#89dceb;">2</span><span style="color:#cdd6f4;">]):</span>
<span style="color:#cdd6f4;">    </span><span style="color:#cba6f7;">print</span><span style="color:#cdd6f4;">(</span><span style="color:#a6e3a1;">f"  '먹었다' → '{word}': {score:.3f}"</span><span style="color:#cdd6f4;">)</span></div>
</div>

<!-- 출력 결과 -->
<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 14px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">출력 결과</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">[STEP 1] 내적 결과 (raw scores):</span>
<span style="color:#cdd6f4;">[[1.3  1.08 0.92]
 [1.08 1.77 1.65]
 [0.92 1.65 1.94]]</span>

<span style="color:#6c7086;">[STEP 2] Scaled Attention Scores:</span>
<span style="color:#a6e3a1;">[[0.65 0.54 0.46]
 [0.54 0.89 0.83]
 [0.46 0.83 0.97]]</span>

<span style="color:#6c7086;">[해석] '먹었다'가 각 단어에 매긴 점수:</span>
<span style="color:#cdd6f4;">  '먹었다' → '나는':   0.460</span>
<span style="color:#cdd6f4;">  '먹었다' → '사과를': 0.825</span>
<span style="color:#a6e3a1;">  '먹었다' → '먹었다': 0.970  ← 자기 자신이 가장 높음</span></div>
</div>

</div>

<br>

<!-- 코드 핵심 해설 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
코드 핵심 포인트
</h2>

<div style="display:grid; gap:12px; margin-top:16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:6px;">Q @ K.T — 전체 단어 쌍의 점수를 한 번에</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      Q는 (단어 수 × 차원), K.T는 (차원 × 단어 수)이므로 결과는 (단어 수 × 단어 수) 행렬입니다.<br>
      <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">scores[i][j]</code> = i번째 단어가 j번째 단어에 매긴 Attention Score
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:6px;">Q.shape[-1] — 마지막 축 크기가 차원 수</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      <code style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:2px 6px; border-radius:5px;">shape[-1]</code>은 배열의 마지막 차원 크기입니다.<br>
      차원 수 d를 하드코딩하지 않고 이렇게 쓰면, 어떤 차원의 벡터에도 공식이 그대로 적용됩니다.
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:6px;">대각선이 가장 높다 — 자기 자신과의 내적</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      결과 행렬의 대각선(scores[0][0], [1][1], [2][2])이 가장 큰 것을 확인할 수 있습니다.<br>
      자기 자신과의 내적이 항상 가장 크기 때문입니다. (Self-Attention의 기본 성질)
    </div>
  </div>

</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size:15px; font-weight:900; margin-bottom:10px;"><span style="color:#FF6B00; font-size:18px;">⚡</span> 핵심 정리</div>
<div style="display:grid; gap:8px;">
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">Q @ K.T</code>로 모든 단어 쌍의 내적을 <b style="color:#FF6B00;">행렬 한 번에</b> 계산합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">/ np.sqrt(d)</code>로 점수를 스케일링해 Softmax 포화를 방지합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    다음 단계(4-4)에서 이 Score에 Softmax를 적용해 <b style="color:#FF6B00;">Attention Weight</b>로 변환합니다.
  </div>
</div>
</div>

</div>