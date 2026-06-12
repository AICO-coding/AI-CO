<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
  Chapter 04 · Attention
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
왜 √d 로 나눌까? — Scaling
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
내적만으로 점수를 계산하면 한 가지 문제가 생깁니다.<br>
실제 Attention에서는 내적 결과를
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">√d (차원의 제곱근)</span>
으로 나눠서 점수를 안정시킵니다. 왜 그럴까요?
</p>

</div>

<br>

<!-- 문제: 차원이 커지면 내적도 커진다 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📈 문제 — 차원이 커질수록 점수가 폭발한다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
내적은 각 차원의 곱을 모두 더합니다.<br>
차원 수(d)가 커질수록 더하는 항이 많아지고, 점수 값이 <b style="color:#FF6B00;">커지는 건 당연한 일</b>입니다.
</p>

<div style="background:#0f172a; border-radius:14px; padding:18px 20px; font-family:'JetBrains Mono', Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:2.2; margin:16px 0; overflow-x:auto;">
<span style="color:#6c7086;">-- 차원(d)이 4일 때 --</span><br>
내적 = 곱셈 4번 더하기  → 점수: <span style="color:#a6e3a1;">1.50</span>  (비교적 작음)<br><br>
<span style="color:#6c7086;">-- 차원(d)이 512일 때 (실제 Transformer) --</span><br>
내적 = 곱셈 512번 더하기 → 점수: <span style="color:#f38ba8;">~150 이상</span>  (매우 커짐)
</div>

<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:14px 18px; font-size:14px; color:#334155; line-height:1.8;">
  <span style="color:#FF6B00; font-weight:900;">⚠️ 점수가 너무 크면 어떤 문제가 생길까?</span><br>
  다음 단계에서 Softmax를 적용할 때, 큰 값에는 확률이 <b>거의 1</b>로, 작은 값에는 <b>거의 0</b>으로 쏠립니다.<br>
  → 한 단어에만 집중하고 나머지는 완전히 무시하는 현상이 생깁니다.<br>
  → 이를 <b style="color:#FF6B00;">"Softmax 포화(saturation)"</b> 문제라고 합니다.
</div>

</div>

<br>

<!-- Softmax 포화 시각화 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
Softmax 포화 — 점수 크기에 따른 차이
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
같은 비율의 점수라도 절댓값이 크면 Softmax 결과가 극단적으로 달라집니다.
</p>

<div style="display:grid; gap:14px; margin-top:16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:10px;">✅ 점수가 작을 때 (스케일링 후) — 고른 집중</div>
    <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:2;">
      scores  = [<span style="color:#89dceb;">1.0</span>, <span style="color:#89dceb;">2.0</span>, <span style="color:#89dceb;">1.5</span>]<br>
      weights = [<span style="color:#a6e3a1;">0.21</span>, <span style="color:#a6e3a1;">0.58</span>, <span style="color:#a6e3a1;">0.32</span>]  <span style="color:#6c7086;">← 골고루 분산</span>
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:10px;">❌ 점수가 클 때 (스케일링 전) — 한 곳에 쏠림</div>
    <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:2;">
      scores  = [<span style="color:#f38ba8;">100</span>, <span style="color:#f38ba8;">200</span>, <span style="color:#f38ba8;">150</span>]<br>
      weights = [<span style="color:#f38ba8;">0.00</span>, <span style="color:#f38ba8;">1.00</span>, <span style="color:#f38ba8;">0.00</span>]  <span style="color:#6c7086;">← 하나에 집중, 나머지 무시</span>
    </div>
  </div>

</div>

<div style="margin-top:14px; background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px; font-size:14px; color:#334155; line-height:1.8;">
  <span style="color:#1681c4; font-weight:900;">💡 학습에도 문제가 생깁니다</span><br>
  Softmax가 한 곳에 쏠리면 기울기(gradient)가 거의 0에 가까워집니다.<br>
  → 모델이 학습을 거의 못 하는 <b style="color:#1681c4;">기울기 소실(vanishing gradient)</b> 문제로 이어집니다.
</div>

</div>

<br>

<!-- 해결책: √d로 나누기 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
✅ 해결책 — √d 로 나눠서 안정시키기
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
내적 결과를 벡터 차원 수 d의 제곱근(√d)으로 나눠주면, 차원이 커져도 점수 크기가 안정됩니다.<br>
이것이 바로 <b style="color:#FF6B00;">Scaled Dot-Product Attention</b>의 핵심입니다.
</p>

<!-- 공식 카드 -->
<div style="background:#0f172a; border-radius:14px; padding:22px; text-align:center; margin:18px 0;">
  <div style="color:#6c7086; font-size:13px; margin-bottom:12px; font-family:Consolas, monospace;">Scaled Dot-Product Attention Score</div>
  <div style="font-size:22px; font-weight:900; color:#c3e88d; font-family:'JetBrains Mono', Consolas, monospace; letter-spacing:1px;">
    score(Q, K) = (Q · K) / √d
  </div>
  <div style="margin-top:14px; display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; text-align:left;">
    <div style="background:rgba(255,255,255,0.06); border-radius:10px; padding:10px 12px;">
      <div style="color:#f38ba8; font-size:12px; font-weight:900; margin-bottom:4px;">Q (Query)</div>
      <div style="color:#94a3b8; font-size:13px;">지금 처리 중인 단어의 벡터</div>
    </div>
    <div style="background:rgba(255,255,255,0.06); border-radius:10px; padding:10px 12px;">
      <div style="color:#89dceb; font-size:12px; font-weight:900; margin-bottom:4px;">K (Key)</div>
      <div style="color:#94a3b8; font-size:13px;">참조할 단어의 벡터</div>
    </div>
    <div style="background:rgba(255,255,255,0.06); border-radius:10px; padding:10px 12px;">
      <div style="color:#a6e3a1; font-size:12px; font-weight:900; margin-bottom:4px;">√d</div>
      <div style="color:#94a3b8; font-size:13px;">벡터 차원 수의 제곱근</div>
    </div>
  </div>
</div>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; font-size:14px; color:#334155; line-height:1.8;">
  <b style="color:#FF6B00;">왜 √d인가?</b><br>
  내적값의 분산이 d에 비례해서 커지는 수학적 성질 때문입니다.<br>
  √d로 나누면 차원에 상관없이 분산을 <b>1 근처로 유지</b>할 수 있습니다.<br>
  → Softmax 입력이 항상 적당한 범위에 머물러, 학습이 안정적으로 진행됩니다.
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size:15px; font-weight:900; margin-bottom:10px;"><span style="color:#FF6B00; font-size:18px;">⚡</span> 핵심 정리</div>
<div style="display:grid; gap:8px;">
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    차원(d)이 클수록 내적 값이 커져 Softmax가 한 단어에만 <b style="color:#FF6B00;">쏠리는 포화 문제</b>가 생깁니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    내적값을 <b style="color:#FF6B00;">√d로 나눠</b> 점수 크기를 일정하게 유지합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이 공식이 <b style="color:#FF6B00;">Scaled Dot-Product Attention Score</b>이며, 실제 Transformer의 공식입니다.
  </div>
</div>
</div>

</div>