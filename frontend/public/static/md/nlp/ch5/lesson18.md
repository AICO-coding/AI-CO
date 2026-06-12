<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Masked Self-Attention - 마스킹은 어떻게 동작하는가?
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Decoder가 미래 단어를 보지 못하도록 막는
<b style="color:#1681c4;">마스크 행렬</b>과
<b style="color:#FF6B00;">−∞ 처리</b>가 실제 계산에서 어떻게 쓰이는지 살펴봅니다.
</p>

</div>

<br>

<!-- 마스킹 구현 방법 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔧 마스킹의 실제 구현 방법
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
앞 페이지에서 <b>"미래 단어를 가린다"</b>는 개념을 배웠습니다.<br>
이번 페이지에서는 이것이 <b style="color:#1681c4;">실제 계산에서 어떻게 구현되는지</b> 살펴봅니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 16px 18px; border-radius: 14px; margin: 16px 0; text-align:center;">
  <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">💡 핵심 아이디어</div>
  <div style="font-size:16px; color:#0f172a; line-height:1.8; font-weight:900;">
    가려야 하는 위치의 Attention 점수를<br>
    <span style="color:#FF6B00; background:#fff3eb; border:1px solid #ffd0b0; padding:3px 8px; border-radius:8px;">마이너스 무한대(−∞)</span> 로 만든다.
  </div>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 0;">
즉, 미래 단어를 물리적으로 삭제하는 것이 아니라, <b>점수를 거의 불가능한 값으로 낮춰서</b> Softmax 이후 선택되지 않게 만드는 방식입니다.
</p>

</div>

<br>

<!-- Attention 점수 행렬 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 Attention 점수 행렬 이해하기
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Self-Attention을 계산하면 <b>Attention 점수 행렬</b>이 만들어집니다.<br>
이 행렬의 각 칸은 <b style="color:#FF6B00;">"이 단어가 저 단어를 얼마나 참고하는가"</b>를 나타냅니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">attention_scores_before_mask.txt</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 900; font-family: 'Nunito', sans-serif;">
      마스킹 전
    </div>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.2; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">         참고하는 단어</span>
<span style="color:#6c7086;">         I      ate    rice</span>
<span style="color:#f38ba8;">보는  I</span>  [ <span style="color:#a6e3a1;">0.9</span>,  <span style="color:#a6e3a1;">0.3</span>,  <span style="color:#a6e3a1;">0.5</span> ]   <span style="color:#6c7086;">← "I"가 각 단어를 얼마나 참고?</span>
<span style="color:#f38ba8;">단어 ate</span> [ <span style="color:#a6e3a1;">0.4</span>,  <span style="color:#a6e3a1;">0.8</span>,  <span style="color:#a6e3a1;">0.6</span> ]   <span style="color:#6c7086;">← "ate"가 각 단어를 얼마나 참고?</span>
<span style="color:#f38ba8;">    rice</span> [ <span style="color:#a6e3a1;">0.2</span>,  <span style="color:#a6e3a1;">0.7</span>,  <span style="color:#a6e3a1;">0.9</span> ]   <span style="color:#6c7086;">← "rice"가 각 단어를 얼마나 참고?</span></div>
</div>

<div style="display:grid; gap:8px; margin-top:14px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">첫 번째 행 "I"</b> : 자신(0.9)을 가장 많이 참고하고, 뒤 단어인 "ate", "rice"도 참고할 수 있는 상태입니다.
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">두 번째 행 "ate"</b> : 자신(0.8), "I"(0.4), 그리고 미래 단어인 "rice"(0.6)까지 참고하고 있습니다.
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">세 번째 행 "rice"</b> : 이미 앞에 있는 단어들을 모두 참고해도 되는 위치입니다.
  </div>
</div>

</div>

<br>

<!-- 마스크 행렬 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎭 마스크 행렬 적용하기
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
마스킹을 적용하기 위해 <b style="color:#1681c4;">삼각형 모양의 마스크 행렬</b>을 사용합니다.<br>
아래 행렬에서 <b>1은 볼 수 있음</b>, <b style="color:#FF6B00;">0은 가려야 함</b>을 의미합니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">causal_mask_matrix.txt</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.2; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">         I    ate   rice</span>
   <span style="color:#f38ba8;">I</span>  [  <span style="color:#a6e3a1;">1</span>,    <span style="color:#ff5f57;">0</span>,    <span style="color:#ff5f57;">0</span>  ]  <span style="color:#6c7086;">← "I"는 자기 자신만 볼 수 있음</span>
  <span style="color:#f38ba8;">ate</span> [  <span style="color:#a6e3a1;">1</span>,    <span style="color:#a6e3a1;">1</span>,    <span style="color:#ff5f57;">0</span>  ]  <span style="color:#6c7086;">← "ate"는 "I"와 자신만 볼 수 있음</span>
 <span style="color:#f38ba8;">rice</span> [  <span style="color:#a6e3a1;">1</span>,    <span style="color:#a6e3a1;">1</span>,    <span style="color:#a6e3a1;">1</span>  ]  <span style="color:#6c7086;">← "rice"는 모든 앞 단어를 볼 수 있음</span></div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color:#1681c4; font-weight:900;">📌</span> 이 삼각형 패턴이 <b style="color:#1681c4;">"앞 단어만 볼 수 있다"</b>는 규칙을 구현합니다.
</div>

</div>

<br>

<!-- -inf 처리 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
➕ 마스크 적용: 0인 위치를 −∞로 바꾼다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
마스크에서 0인 위치, 즉 <b style="color:#FF6B00;">가려야 할 곳</b>은 매우 큰 음수로 교체합니다.<br>
수학적으로는 <b>−∞</b>라고 표현하고, 실제 코드에서는 보통 <b style="color:#FF6B00;">−1억 정도의 큰 음수</b>를 사용합니다.
</p>

<div style="display:grid; grid-template-columns: 1fr 1fr; gap: 14px; margin: 16px 0;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#475569; margin-bottom:10px;">마스킹 전 점수 행렬</div>
    <div style="background:#0f172a; border-radius:8px; padding:12px 14px; font-family:Consolas, monospace; font-size:12px; color:#cdd6f4; line-height:2.1; overflow-x:auto; white-space:pre;">
       I     ate   rice
 I   [0.9,  0.3,  0.5]
ate  [0.4,  0.8,  0.6]
rice [0.2,  0.7,  0.9]</div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:10px;">마스킹 후 점수 행렬</div>
    <div style="background:#0f172a; border-radius:8px; padding:12px 14px; font-family:Consolas, monospace; font-size:12px; color:#cdd6f4; line-height:2.1; overflow-x:auto; white-space:pre;">
       I     ate   rice
 I   [<span style="color:#a6e3a1;">0.9</span>, <span style="color:#ff5f57;">-∞</span>,  <span style="color:#ff5f57;">-∞</span>]
ate  [<span style="color:#a6e3a1;">0.4</span>,  <span style="color:#a6e3a1;">0.8</span>, <span style="color:#ff5f57;">-∞</span>]
rice [<span style="color:#a6e3a1;">0.2</span>,  <span style="color:#a6e3a1;">0.7</span>,  <span style="color:#a6e3a1;">0.9</span>]</div>
  </div>

</div>

<div style="display:grid; gap:8px;">
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">"I" 행</b>에서는 뒤 단어인 "ate", "rice"가 −∞ 처리됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">"ate" 행</b>에서는 미래 단어인 "rice"만 −∞ 처리됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">"rice" 행</b>은 마지막 위치이므로 모든 앞 단어를 볼 수 있습니다.
  </div>
</div>

</div>

<br>

<!-- Softmax -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 Softmax가 −∞를 0으로 만든다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Attention 점수는 Softmax를 거쳐 <b>확률</b>로 변환됩니다.<br>
Softmax의 핵심 성질은 <b style="color:#1681c4;">−∞가 사실상 0의 확률이 된다</b>는 점입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">softmax_after_mask.txt</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.3; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">"ate"의 마스킹 후 점수</span>: [ <span style="color:#a6e3a1;">0.4</span>,  <span style="color:#a6e3a1;">0.8</span>,  <span style="color:#ff5f57;">−∞</span> ]
                             <span style="color:#89dceb;">↓ Softmax 적용</span>
<span style="color:#6c7086;">확률로 변환</span>:              [ <span style="color:#a6e3a1;">0.31</span>, <span style="color:#a6e3a1;">0.69</span>,  <span style="color:#ff5f57; font-weight:900;">0</span> ]
                                        <span style="color:#f9e2af;">↑</span>
                                  <span style="color:#f9e2af;">정확히 0이 됨!</span>
                                  <span style="color:#6c7086;">→ "rice"를 전혀 참고하지 않음</span></div>
</div>

<div style="display:grid; grid-template-columns: 1fr 1fr; gap: 14px;">
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">수식 느낌으로 보면</div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 12px; font-family:Consolas,monospace; font-size:13px; color:#cdd6f4; line-height:1.9;">
      e<sup>−∞</sup> = <span style="color:#ff5f57; font-weight:900;">0</span>
    </div>
  </div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:8px;">직관으로 보면</div>
    <div style="font-size:13px; color:#334155; line-height:1.8;">
      −∞ 점수를 받은 단어는 Softmax 후 <b style="color:#FF6B00;">참고 비율이 0%</b>가 됩니다.
    </div>
  </div>
</div>

</div>

<br>

<!-- 전체 계산에서 위치 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📐 전체 Attention 계산에서 마스킹 위치 확인
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
마스크는 Attention 계산 전체 과정에서 <b style="color:#FF6B00;">Softmax 직전</b>에 한 번 적용됩니다.
</p>

<div style="display:grid; gap:12px; margin-top:16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#475569; margin-bottom:10px;">일반 Self-Attention</div>
    <div style="display:grid; grid-template-columns: repeat(5, auto); gap:8px; align-items:center; overflow-x:auto;">
      <div style="background:#0f172a; color:#c3e88d; padding:8px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">Q, K 유사도</div>
      <div style="color:#94a3b8; font-weight:900; text-align:center;">→</div>
      <div style="background:#0f172a; color:#c3e88d; padding:8px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">점수 행렬</div>
      <div style="color:#94a3b8; font-weight:900; text-align:center;">→</div>
      <div style="background:#0f172a; color:#c3e88d; padding:8px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">Softmax → V 가중 합산</div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">Masked Self-Attention</div>
    <div style="display:grid; grid-template-columns: repeat(7, auto); gap:8px; align-items:center; overflow-x:auto;">
      <div style="background:#0f172a; color:#c3e88d; padding:8px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">Q, K 유사도</div>
      <div style="color:#94a3b8; font-weight:900; text-align:center;">→</div>
      <div style="background:#0f172a; color:#c3e88d; padding:8px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">점수 행렬</div>
      <div style="color:#94a3b8; font-weight:900; text-align:center;">→</div>
      <div style="background:#fff3eb; border:2px solid #ffd0b0; color:#FF6B00; padding:8px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">★ 마스크 적용</div>
      <div style="color:#94a3b8; font-weight:900; text-align:center;">→</div>
      <div style="background:#0f172a; color:#c3e88d; padding:8px 12px; border-radius:10px; font-size:12px; font-weight:900; text-align:center; white-space:nowrap;">Softmax → V 가중 합산</div>
    </div>
  </div>

</div>

<div style="margin-top:14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color:#FF6B00; font-weight:900;">💡</span> 이 단 한 번의 추가 연산으로 <b style="color:#FF6B00;">미래 차단</b>이 완벽하게 구현됩니다.
</div>

</div>

<br>

<!-- 단어별 결과 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔢 단어별 Attention 결과 확인
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
마스킹 적용 후 각 단어가 참고할 수 있는 범위는 다음처럼 달라집니다.<br>
생성 위치가 뒤로 갈수록 <b style="color:#1681c4;">볼 수 있는 범위가 점점 넓어집니다.</b>
</p>

<div style="display:grid; gap:10px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">1번째</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:5px;">"I" 생성 시</div>
      <div style="font-size:13px; color:#475569; line-height:1.8;">
        참고 가능: <b style="color:#1681c4;">&lt;시작&gt;</b><br>
        참고 불가: <span style="color:#94a3b8;">아직 아무것도 없음</span><br>
        → 오직 시작 토큰과 현재 위치 정보만 참고합니다.
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">2번째</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:5px;">"ate" 생성 시</div>
      <div style="font-size:13px; color:#475569; line-height:1.8;">
        참고 가능: <b style="color:#1681c4;">&lt;시작&gt;, I</b><br>
        참고 불가: <b style="color:#FF6B00;">rice</b> <span style="color:#94a3b8;">(마스킹됨)</span><br>
        → "I"를 보고 그 다음에 올 동사를 결정합니다.
      </div>
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">3번째</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:5px;">"rice" 생성 시</div>
      <div style="font-size:13px; color:#475569; line-height:1.8;">
        참고 가능: <b style="color:#FF6B00;">&lt;시작&gt;, I, ate</b><br>
        참고 불가: <span style="color:#94a3b8;">없음</span><br>
        → "I ate"를 보고 목적어를 결정합니다.
      </div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 병렬 처리 -->
< style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🌟 학습 중 병렬 처리가 가능해진다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
마스킹의 또 다른 중요한 효과가 있습니다.<br>
RNN은 단어를 하나씩 순서대로 처리해야 했지만, Masked Self-Attention은 학습 중 <b style="color:#FF6B00;">모든 위치를 동시에 처리</b>할 수 있습니다.
</p>

<div style="display:grid; grid-template-columns: 1fr 1fr; gap: 14px; margin: 16px 0;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#475569; margin-bottom:10px;">🐢 RNN 방식</div>
    <div style="background:#0f172a; border-radius:8px; padding:12px 14px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"I" 처리 완료</span>
      <span style="color:#89dceb;">↓</span>
<span style="color:#a6e3a1;">"ate" 처리 시작</span>
      <span style="color:#89dceb;">↓</span>
<span style="color:#a6e3a1;">"rice" 처리 시작</span>

<span style="color:#6c7086;">순서대로 처리 → 느림</span></div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:10px;">⚡ Masked Self-Attention 방식</div>
    <div style="background:#0f172a; border-radius:8px; padding:12px 14px; font-family:Consolas, monospace; font-size:13px; color:#cdd6f4; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"I" 처리</span>    <span style="color:#6c7086;">← &lt;시작&gt;만 참고</span>
<span style="color:#a6e3a1;">"ate" 처리</span>  <span style="color:#6c7086;">← &lt;시작&gt;, "I" 참고</span>
<span style="color:#a6e3a1;">"rice" 처리</span> <span style="color:#6c7086;">← &lt;시작&gt;, "I", "ate" 참고</span>

<span style="color:#f9e2af;">세 위치 모두 동시에 처리!</span></div>
  </div>

</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; margin-bottom: 12px;">
<span style="color:#1681c4; font-weight:900;">💡</span> 마스킹은 미래 차단 규칙을 강제하면서도 <b style="color:#1681c4;">학습 중 병렬 처리</b>를 가능하게 해주는 장치입니다.
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color:#FF6B00; font-weight:900;">⚠️ 주의</span><br>
실제 사용, 즉 번역이나 문장 생성 <b>추론 시</b>에는 아직 뒤 단어가 없기 때문에 단어를 <b style="color:#FF6B00;">하나씩 순서대로</b> 생성합니다.<br>
병렬 처리는 주로 <b>학습 중</b>에 가능한 장점입니다.
</div>

</div>

<br>

<!-- 전체 흐름 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 Masked Self-Attention 전체 흐름 정리
</h2>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">masked_self_attention_flow.txt</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.35; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">Decoder 입력 단어들 (이전에 생성된 것들)</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#a6e3a1;">임베딩 + Positional Encoding</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#a6e3a1;">Q, K, V 생성</span> <span style="color:#6c7086;">(입력에서 각각 선형 변환)</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#a6e3a1;">Q × Kᵀ</span> → <span style="color:#f9e2af;">Attention 점수 행렬</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#ff5f57; font-weight:900;">★ 마스크 행렬 적용</span> <span style="color:#6c7086;">(미래 위치 → −∞)</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#a6e3a1;">Softmax</span> <span style="color:#6c7086;">(−∞ → 0, 확률 분포로 변환)</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#a6e3a1;">Attention 가중치 × V</span> → <span style="color:#f9e2af;">출력</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#cba6f7;">Multi-Head로 확장</span> <span style="color:#6c7086;">(여러 Head 병렬)</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#cba6f7;">결과 이어 붙이기 + 선형 변환</span>
         <span style="color:#89dceb;">↓</span>
<span style="color:#f9e2af; font-weight:900;">Masked Self-Attention 최종 출력</span></div>
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;">
<span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리
</div>

<div style="display: grid; gap: 8px;">
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    마스킹은 <b style="color:#FF6B00;">삼각형 모양의 마스크 행렬</b>로 구현됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    가려야 할 위치의 Attention 점수를 <b style="color:#FF6B00;">−∞</b>로 바꿉니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Softmax를 거치면 −∞ 위치의 가중치가 <b style="color:#FF6B00;">0</b>이 되어 완전히 차단됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    마스크는 Softmax <b style="color:#FF6B00;">직전</b>에 단 한 번 적용됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    미래 차단과 동시에 <b style="color:#FF6B00;">학습 중 병렬 처리</b>도 가능하게 해줍니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    실제 번역 시에는 여전히 단어를 <b style="color:#FF6B00;">하나씩 순서대로</b> 생성합니다.
  </div>
</div>

</div>

<br>

<!-- Decoder 마무리 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔗 전체 마무리: Decoder의 모든 것
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
이제 Decoder를 구성하는 모든 요소를 배웠습니다.<br>
각 요소가 Decoder 안에서 어떤 역할을 맡는지 한 번에 정리해봅시다.
</p>

<div style="overflow-x: auto; margin-top: 14px;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; font-weight:900;">구성 요소</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">역할</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">특징</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">Masked Self-Attention</td>
      <td style="padding:10px 14px; color:#334155;">이전 단어들 사이 관계 파악</td>
      <td style="padding:10px 14px; color:#475569;">미래 단어 차단</td>
    </tr>
    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">Encoder-Decoder Attention</td>
      <td style="padding:10px 14px; color:#334155;">원문 정보 참고</td>
      <td style="padding:10px 14px; color:#475569;">Q=Decoder, K·V=Encoder</td>
    </tr>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">FFN</td>
      <td style="padding:10px 14px; color:#334155;">단어 표현 심화</td>
      <td style="padding:10px 14px; color:#475569;">각 단어 독립 처리</td>
    </tr>
    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Add &amp; Norm × 3</td>
      <td style="padding:10px 14px; color:#334155;">정보 보존 + 안정화</td>
      <td style="padding:10px 14px; color:#475569;">Encoder보다 1번 더</td>
    </tr>
    <tr style="background:#fff;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Linear + Softmax</td>
      <td style="padding:10px 14px; color:#334155;">다음 단어 확률 계산</td>
      <td style="padding:10px 14px; color:#475569;">단어 사전 크기로 변환</td>
    </tr>
  </tbody>
</table>
</div>

<div style="margin-top:14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color:#1681c4; font-weight:900;">📌</span> 다음 페이지에서는 Encoder와 Decoder를 합쳐<br>
<b style="color:#1681c4;">Transformer 전체 처리 과정</b>을 처음부터 끝까지 정리합니다.
</div>

</div>

</div>