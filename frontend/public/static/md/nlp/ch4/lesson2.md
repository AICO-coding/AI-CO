<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
  Chapter 04 · Attention
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Attention의 기본 아이디어
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Attention의 핵심은 단순합니다 —
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">어떤 단어가 지금 단어와 얼마나 관련 있는지 점수를 매기고, 그 점수에 비례해서 참조한다.</span><br>
이 섹션에서는 그 아이디어를 수식 없이, 코드로 직접 구현해봅니다.
</p>

</div>

<br>

<!-- 핵심 아이디어 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔦 손전등 비유 — 집중해서 봐야 할 곳에 불빛을 비춘다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
어두운 방에서 책을 읽을 때 손전등을 들고 있다고 상상해보세요.<br>
중요한 문장에는 불빛을 강하게, 덜 중요한 곳에는 약하게 비춥니다.
</p>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8; margin: 14px 0;">
<span style="color: #FF6B00; font-weight: 900;">💡 Attention의 손전등</span><br>
"나는 <b>사과</b>를 먹었다"를 처리할 때, 모델은<br>
→ <b style="color:#1681c4;">"먹었다"</b>에 강한 불빛 (관련성 높음)<br>
→ <b style="color:#94a3b8;">"나는"</b>에 약한 불빛 (관련성 낮음)<br>
이렇게 단어마다 다른 밝기(가중치)로 빛을 비춥니다.
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-top: 18px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; text-align:center;">
    <div style="font-size:24px; margin-bottom:8px;">1️⃣</div>
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:6px;">점수 계산</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">현재 단어와 다른 모든 단어의 관련성 점수를 계산합니다.</div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px; text-align:center;">
    <div style="font-size:24px; margin-bottom:8px;">2️⃣</div>
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:6px;">가중치 변환</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">점수를 softmax로 0~1 사이의 확률 값(가중치)으로 바꿉니다.</div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; text-align:center;">
    <div style="font-size:24px; margin-bottom:8px;">3️⃣</div>
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:6px;">가중 합산</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">가중치에 따라 각 단어의 정보를 합산해 최종 표현을 만듭니다.</div>
  </div>

</div>

</div>

<br>

<!-- STEP 카드들 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
3단계로 이해하는 Attention
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
"먹었다"라는 단어를 처리할 때 Attention이 어떻게 작동하는지 단계별로 살펴봅니다.
</p>

<div style="display: grid; gap: 16px; margin-top: 18px;">

  <!-- STEP 1 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
      <div style="background:#0f172a; color:#c3e88d; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900;">STEP 1</div>
      <div style="font-size:15px; font-weight:900; color:#0f172a;">관련성 점수 계산 (Attention Score)</div>
    </div>
    <p style="margin:0 0 12px; font-size:14px; color:#334155; line-height:1.7;">
      "먹었다"와 문장의 각 단어가 얼마나 관련 있는지 점수를 매깁니다.<br>
      가장 간단한 방법은 <b style="color:#FF6B00;">내적(dot product)</b>으로 두 벡터의 유사도를 계산하는 것입니다.
    </p>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px; font-size:14px; color:#334155; line-height:1.8;">
      예시:<br>
      "먹었다" ↔ "나는"      → 점수: <b style="color:#94a3b8;">0.1</b> (관련 낮음)<br>
      "먹었다" ↔ "사과를"    → 점수: <b style="color:#FF6B00;">2.3</b> (관련 높음)<br>
      "먹었다" ↔ "먹었다"    → 점수: <b style="color:#FF6B00;">3.1</b> (자기 자신, 가장 높음)
    </div>
  </div>

  <!-- STEP 2 -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:18px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
      <div style="background:#0f172a; color:#c3e88d; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900;">STEP 2</div>
      <div style="font-size:15px; font-weight:900; color:#0f172a;">Softmax로 가중치 변환 (Attention Weight)</div>
    </div>
    <p style="margin:0 0 12px; font-size:14px; color:#334155; line-height:1.7;">
      점수들을 <b style="color:#1681c4;">softmax 함수</b>에 통과시켜 모두 더하면 1이 되는 확률 값으로 바꿉니다.<br>
      이 값들이 바로 각 단어에 얼마나 집중할지를 결정하는 <b>가중치(weight)</b>입니다.
    </p>
    <div style="background:#ffffff; border:1px solid #c2e4ff; border-radius:10px; padding:12px; font-size:14px; color:#334155; line-height:1.8;">
      softmax 후:<br>
      "나는"    → <b style="color:#94a3b8;">0.05</b> (5%만 참조)<br>
      "사과를"  → <b style="color:#FF6B00;">0.30</b> (30% 참조)<br>
      "먹었다"  → <b style="color:#1681c4;">0.65</b> (65% 참조)<br>
      합계: <b>1.00</b>
    </div>
  </div>

  <!-- STEP 3 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
      <div style="background:#0f172a; color:#c3e88d; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:900;">STEP 3</div>
      <div style="font-size:15px; font-weight:900; color:#0f172a;">가중 합산으로 Context Vector 생성</div>
    </div>
    <p style="margin:0 0 12px; font-size:14px; color:#334155; line-height:1.7;">
      각 단어의 벡터에 해당 가중치를 곱하고 모두 더하면,<br>
      "먹었다"가 문장 전체를 바라보며 만든 <b style="color:#FF6B00;">문맥이 담긴 표현(Context Vector)</b>이 완성됩니다.
    </p>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px; font-size:14px; color:#334155; line-height:1.8;">
      Context Vector = 0.05 × v("나는") + 0.30 × v("사과를") + 0.65 × v("먹었다")<br>
      → <b style="color:#FF6B00;">"사과를 먹는 행위"라는 문맥 정보가 담긴 벡터</b>
    </div>
  </div>

</div>

</div>

<br>

<!-- 완전체 코드 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
코드로 구현하기 — Attention 3단계
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
아래 코드는 Attention의 핵심 계산 과정을 NumPy로 단계별로 구현한 완전한 예시입니다.<br>
오른쪽 빈칸 연습 파일에서는 핵심 부분만 직접 채워봅니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-top: 18px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">📄 attention_basic.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      Attention 완전체 코드
    </div>
  </div>

<div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 1.9; overflow-x: auto;">

```python
import numpy as np

# ── 입력 준비 ───────────────────────────────────────────────
# 단어 3개, 각각 4차원 벡터로 표현 (실제로는 임베딩 벡터)
# 행(row): 단어 수, 열(col): 임베딩 차원
vectors = np.array([
    [1.0, 0.2, 0.1, 0.5],   # "나는"
    [0.8, 1.0, 0.3, 0.2],   # "사과를"
    [0.2, 0.9, 1.0, 0.7],   # "먹었다"  ← 현재 처리 중인 단어
])

query = vectors[2]   # "먹었다"를 기준으로 Attention 계산

# ── STEP 1: Attention Score ─────────────────────────────────
# query와 모든 단어 벡터의 내적으로 관련성 점수를 계산합니다
# vectors @ query : 행렬 × 벡터 = 각 단어와의 내적값 배열
scores = vectors @ query
# scores = [내적("나는","먹었다"), 내적("사과를","먹었다"), 내적("먹었다","먹었다")]
print("Attention Scores:", scores)

# ── STEP 2: Softmax → Attention Weight ─────────────────────
# 점수를 0~1 사이 확률로 변환합니다 (합 = 1.0)
# exp: 지수함수로 음수 점수도 양수로 만들고 차이를 강조
exp_scores = np.exp(scores)
weights = exp_scores / exp_scores.sum()
print("Attention Weights:", np.round(weights, 3))
# 합이 1인지 확인: weights.sum() == 1.0

# ── STEP 3: 가중 합산 → Context Vector ──────────────────────
# 각 단어 벡터에 해당 가중치를 곱하고 모두 더합니다
# weights[:, None] : (3,) → (3, 1) 로 변환해서 브로드캐스팅
context = (weights[:, None] * vectors).sum(axis=0)
print("Context Vector:", np.round(context, 3))
# → "먹었다"가 문장 전체를 참조해 만든 문맥 벡터
```

</div>
</div>

<!-- 코드 줄별 핵심 설명 -->
<div style="display: grid; gap: 12px; margin-top: 18px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:15px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:6px;">vectors @ query — 내적으로 관련성 측정</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      두 벡터가 비슷한 방향을 가리킬수록 내적 값이 커집니다.<br>
      Attention에서는 이 내적값이 곧 "얼마나 관련 있는가"의 점수가 됩니다.
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:15px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:6px;">np.exp(scores) / sum — Softmax 직접 구현</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">np.exp()</code>로 모든 점수를 양수로 만들고,<br>
      전체 합으로 나눠 0~1 사이의 확률로 변환합니다. 합은 항상 1.0이 됩니다.
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:15px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:6px;">weights[:, None] * vectors — 가중치 적용</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      <code style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:2px 6px; border-radius:5px;">[:, None]</code>은 shape (3,)을 (3, 1)로 바꿔 행렬 곱이 되도록 합니다.<br>
      각 단어 벡터에 해당 가중치를 곱한 뒤 모두 더하면 Context Vector가 완성됩니다.
    </div>
  </div>

</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; font-weight: 900; font-size: 15px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<span style="color: #FF6B00; font-size: 18px;">⚡</span>
Attention = 점수 계산 → Softmax → 가중 합산, 이 세 단계가 전부입니다.<br>
<span style="font-weight:400; font-size:14px; color:#475569;">뒤에서 배울 Query·Key·Value는 이 구조를 더 정교하게 만든 확장 버전입니다.</span>
</div>

</div>