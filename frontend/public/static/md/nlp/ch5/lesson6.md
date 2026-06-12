<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Positional Encoding — 위치를 어떻게 숫자로 표현할까?
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
단순한 번호 방식이 왜 실패하는지,
<b style="color:#1681c4;">sin/cos 파동 패턴</b>이 어떻게 위치를 표현하는지 알아봅니다.
</p>

</div>

<br>

<!-- 방법 1: 1, 2, 3 번호 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
위치 정보를 숫자로 만드는 방법, 뭐가 있을까요?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 18px;">
"몇 번째 단어인지"를 벡터에 담으려면 어떤 숫자를 사용하면 좋을까요?<br>
가장 먼저 떠오르는 방법부터 차례로 살펴봅시다.
</p>

<!-- 방법 1 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px; margin-bottom: 12px;">
  <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:900;">❌ 방법 1</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">그냥 1, 2, 3... 번호를 붙인다</div>
  </div>

  <div style="background-color: #1e1e2e; border-radius: 12px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; margin-bottom: 12px;">
    <div style="padding: 14px 18px; color: #cdd6f4; font-size: 13px; line-height: 2.0; overflow-x: auto; white-space: pre;">
<span style="color:#a6e3a1;">1번째</span> 단어 → 위치값 <span style="color:#89dceb;">1</span>
<span style="color:#a6e3a1;">2번째</span> 단어 → 위치값 <span style="color:#89dceb;">2</span>
<span style="color:#a6e3a1;">3번째</span> 단어 → 위치값 <span style="color:#89dceb;">3</span>
<span style="color:#6c7086;">...</span>
<span style="color:#f38ba8;">1000번째</span> 단어 → 위치값 <span style="color:#f38ba8;">1000</span></div>
  </div>

  <div style="display: grid; gap: 8px;">
    <div style="background:#fff; border-left:4px solid #FF6B00; padding:9px 13px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
      문장이 길어질수록 숫자가 <b style="color:#FF6B00;">너무 커집니다.</b>
    </div>
    <div style="background:#fff; border-left:4px solid #FF6B00; padding:9px 13px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
      위치값이 너무 커지면 <b style="color:#FF6B00;">원래 단어 의미가 묻혀버립니다.</b>
    </div>
    <div style="background:#fff; border-left:4px solid #FF6B00; padding:9px 13px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
      학습할 때 본 적 없는 길이의 문장이 들어오면 <b style="color:#FF6B00;">대응할 수 없습니다.</b>
    </div>
  </div>
</div>

<!-- 방법 2 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
    <div style="background:#FF6B00; color:#fff; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:900;">❌ 방법 2</div>
    <div style="font-size:15px; font-weight:900; color:#0f172a;">0~1 사이로 정규화한다</div>
  </div>

  <div style="background-color: #1e1e2e; border-radius: 12px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; margin-bottom: 12px;">
    <div style="padding: 14px 18px; color: #cdd6f4; font-size: 13px; line-height: 2.0; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">문장 길이 10짜리라면:</span>
<span style="color:#a6e3a1;">1번</span> 단어 → <span style="color:#89dceb;">0.1</span>
<span style="color:#a6e3a1;">2번</span> 단어 → <span style="color:#89dceb;">0.2</span>
<span style="color:#6c7086;">...</span>
<span style="color:#a6e3a1;">10번</span> 단어 → <span style="color:#89dceb;">1.0</span></div>
  </div>

  <div style="display: grid; gap: 8px;">
    <div style="background:#fff; border-left:4px solid #FF6B00; padding:9px 13px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
      같은 단어인데 문장 길이가 달라지면 <b style="color:#FF6B00;">위치값이 달라집니다.</b>
    </div>
    <div style="background:#fff; border-left:4px solid #FF6B00; padding:9px 13px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
      "나는"이 10개짜리 문장 1번째 → <b>0.1</b> / 100개짜리 문장 1번째 → <b>0.01</b>
    </div>
    <div style="background:#fff; border-left:4px solid #FF6B00; padding:9px 13px; border-radius:0 8px 8px 0; font-size:13px; color:#334155; line-height:1.7;">
      위치의 <b style="color:#FF6B00;">절대적인 의미</b>를 표현할 수 없습니다.
    </div>
  </div>
</div>

</div>

<br>

<!-- sin/cos 방법 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
✅ 실제 방법: sin/cos을 이용한다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Transformer 논문 연구팀이 선택한 방법은 훨씬 영리합니다.<br>
<b style="color:#1681c4;">삼각함수(sin, cos)의 파동 패턴</b>을 사용합니다.
</p>

<!-- 음악 비유 -->
<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 16px 18px; border-radius: 14px; margin: 16px 0;">
  <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">🎹 음악으로 비유하기</div>
  <p style="font-size:14px; color:#334155; line-height:1.8; margin: 0 0 10px 0;">
  피아노 건반에서 낮은 도는 <b>천천히 진동</b>하고, 높은 도는 <b>빠르게 진동</b>합니다.<br>
  Positional Encoding도 마찬가지입니다.
  </p>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <div style="background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 14px; text-align:center;">
      <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:4px;">벡터 앞부분 (낮은 차원)</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">천천히 변하는 파동<br>→ <b>큰 단위 위치 구분</b></div>
    </div>
    <div style="background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 14px; text-align:center;">
      <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:4px;">벡터 뒷부분 (높은 차원)</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">빠르게 변하는 파동<br>→ <b>세밀한 위치 구분</b></div>
    </div>
  </div>
  <div style="margin-top:10px; font-size:13px; color:#334155; line-height:1.8; text-align:center;">
  파동들이 합쳐지면 <b style="color:#1681c4;">각 위치마다 고유한 패턴</b>이 만들어집니다.<br>마치 <b>지문</b>처럼, 어떤 두 위치도 똑같은 패턴을 갖지 않습니다.
  </div>
</div>

<!-- 구체적인 값 -->
<h3 style="font-size:15px; font-weight:900; color:#0f172a; margin: 18px 0 12px 0;">구체적으로 어떻게 생겼나요?</h3>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin-bottom: 16px;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">sin/cos 위치 인코딩 값</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#cba6f7;">위치 1번 단어의 Positional Encoding:</span>
  차원 0번 자리 → <span style="color:#a6e3a1;">sin(1 / 파동1)</span>  = <span style="color:#89dceb;">0.841</span>
  차원 1번 자리 → <span style="color:#a6e3a1;">cos(1 / 파동1)</span>  = <span style="color:#89dceb;">0.540</span>
  차원 2번 자리 → <span style="color:#a6e3a1;">sin(1 / 파동2)</span>  = <span style="color:#89dceb;">0.100</span>
  차원 3번 자리 → <span style="color:#a6e3a1;">cos(1 / 파동2)</span>  = <span style="color:#89dceb;">0.995</span>
  <span style="color:#6c7086;">...</span>

<span style="color:#f38ba8;">위치 2번 단어의 Positional Encoding:</span>
  차원 0번 자리 → <span style="color:#a6e3a1;">sin(2 / 파동1)</span>  = <span style="color:#89dceb;">0.909</span>
  차원 1번 자리 → <span style="color:#a6e3a1;">cos(2 / 파동1)</span>  = <span style="color:#89dceb;">-0.416</span>
  차원 2번 자리 → <span style="color:#a6e3a1;">sin(2 / 파동2)</span>  = <span style="color:#89dceb;">0.200</span>
  차원 3번 자리 → <span style="color:#a6e3a1;">cos(2 / 파동2)</span>  = <span style="color:#89dceb;">0.980</span>
  <span style="color:#6c7086;">...</span></div>
</div>

<!-- 장점 표 -->
<h3 style="font-size:15px; font-weight:900; color:#0f172a; margin: 18px 0 12px 0;">sin/cos 방법의 장점</h3>

<div style="overflow-x: auto;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; font-weight:900;">장점</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">설명</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">값이 항상 -1~1 사이</td>
      <td style="padding:10px 14px; color:#334155;">의미 벡터와 크기가 비슷해 서로 잘 어울림</td>
    </tr>
    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">모든 위치가 고유한 패턴</td>
      <td style="padding:10px 14px; color:#334155;">어떤 두 위치도 같은 인코딩 값을 가지지 않음</td>
    </tr>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">학습 없이 계산으로 생성</td>
      <td style="padding:10px 14px; color:#334155;">별도 학습 불필요, 어떤 길이 문장도 처리 가능</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">상대적 위치 관계 학습 가능</td>
      <td style="padding:10px 14px; color:#334155;">"2번째와 5번째는 3칸 떨어져 있다"는 것을 추론 가능</td>
    </tr>
  </tbody>
</table>
</div>

</div>

<br>

<!-- 적용 과정 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔧 Positional Encoding이 적용되는 과정
</h2>

<div style="display: grid; gap: 10px; margin-top: 14px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 1</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:6px;">단어를 임베딩 벡터로 변환</div>
      <div style="font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8;">
        <span style="color:#6c7086;">"나는"</span>  →  <span style="color:#89dceb;">[0.2, 0.5, 0.1, 0.8, ...]</span>  <span style="color:#6c7086;">(512차원)</span>
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 2</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:6px;">해당 위치의 Positional Encoding 계산</div>
      <div style="font-family:Consolas, monospace; font-size:13px; color:#cba6f7; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8;">
        <span style="color:#6c7086;">위치 1</span>  →  <span style="color:#cba6f7;">[0.84, 0.54, 0.10, 0.99, ...]</span>  <span style="color:#6c7086;">(sin/cos 패턴)</span>
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 3</div>
    <div style="width:100%;">
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:6px;">두 벡터를 더한다 <span style="color:#94a3b8; font-weight:400; font-size:12px;">(덧셈)</span></div>
      <div style="font-family:Consolas, monospace; font-size:13px; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8;">
        <span style="color:#6c7086;">[0.2+0.84, 0.5+0.54, 0.1+0.10, 0.8+0.99, ...]</span><br>
        <span style="color:#89dceb;">= [1.04,     1.04,     0.20,     1.79,     ...]</span>
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 4</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:4px;">이 최종 벡터가 Encoder에 입력된다</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">이후 Self-Attention은 순서 정보가 담긴 벡터를 받아 올바르게 처리합니다.</div>
    </div>
  </div>

</div>

<div style="margin-top:14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 핵심:</span> Positional Encoding은 단어 의미 벡터에 위치 정보를 <b style="color:#FF6B00;">더하는(+) 방식</b>입니다.<br>
곱하거나 이어 붙이는 것이 아니라, <b style="color:#FF6B00;">숫자를 더합니다.</b>
</div>

</div>

<br>

<!-- 파동 패턴 시각화 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 위치별 파동 패턴 살펴보기
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
차원 번호에 따라 파동이 얼마나 빠르게 변하는지 비교해보세요.
</p>

<div style="display: grid; gap: 10px;">

  <div style="background:#1e1e2e; border:2px solid #a6e3a1; border-radius:12px; padding:14px 18px;">
    <div style="font-size:13px; font-weight:900; color:#a6e3a1; margin-bottom:8px;">차원 0번 — 가장 빠른 파동</div>
    <div style="font-family:Consolas, monospace; font-size:12px; color:#cdd6f4; line-height:2; overflow-x:auto; white-space:pre;">
위치1→<span style="color:#89dceb;">0.84</span>  위치2→<span style="color:#89dceb;">0.91</span>  위치3→<span style="color:#89dceb;">0.14</span>  위치4→<span style="color:#f38ba8;">-0.76</span>  <span style="color:#6c7086;">... (빠르게 왔다 갔다 함)</span></div>
  </div>

  <div style="background:#1e1e2e; border:2px solid #cba6f7; border-radius:12px; padding:14px 18px;">
    <div style="font-size:13px; font-weight:900; color:#cba6f7; margin-bottom:8px;">차원 100번 — 중간 파동</div>
    <div style="font-family:Consolas, monospace; font-size:12px; color:#cdd6f4; line-height:2; overflow-x:auto; white-space:pre;">
위치1→<span style="color:#89dceb;">0.10</span>  위치2→<span style="color:#89dceb;">0.20</span>  위치3→<span style="color:#89dceb;">0.30</span>  위치4→<span style="color:#89dceb;">0.39</span>   <span style="color:#6c7086;">... (천천히 변함)</span></div>
  </div>

  <div style="background:#1e1e2e; border:2px solid #6c7086; border-radius:12px; padding:14px 18px;">
    <div style="font-size:13px; font-weight:900; color:#8b8bc7; margin-bottom:8px;">차원 500번 — 가장 느린 파동</div>
    <div style="font-family:Consolas, monospace; font-size:12px; color:#cdd6f4; line-height:2; overflow-x:auto; white-space:pre;">
위치1→<span style="color:#89dceb;">0.001</span> 위치2→<span style="color:#89dceb;">0.002</span> 위치3→<span style="color:#89dceb;">0.003</span> 위치4→<span style="color:#89dceb;">0.004</span>  <span style="color:#6c7086;">... (거의 안 변함)</span></div>
  </div>

</div>

<div style="margin-top:14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> 빠른 파동은 <b style="color:#1681c4;">가까운 위치 구분</b>에, 느린 파동은 <b style="color:#1681c4;">먼 위치 구분</b>에 기여합니다.<br>
여러 파동이 조합되어 <b style="color:#1681c4;">모든 위치를 유일하게 표현</b>합니다.
</div>

</div>

<br>

<!-- 전체 구조 위치 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔗 Positional Encoding은 전체 구조 어디에 있나?
</h2>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Transformer 입력 흐름</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">[입력 문장]</span> "나는 밥을 먹었다"
      <span style="color:#89dceb;">↓</span>
<span style="color:#6c7086;">[토크나이저]</span>  → <span style="color:#a6e3a1;">["나는", "밥을", "먹었다"]</span>
      <span style="color:#89dceb;">↓</span>
<span style="color:#6c7086;">[임베딩]</span>      → 각 단어를 512차원 벡터로 변환
      <span style="color:#89dceb;">↓</span>
<span style="color:#f9e2af; font-weight:900;">[★ Positional Encoding 추가]</span>  <span style="color:#6c7086;">← 지금 배운 단계</span>
      <span style="color:#89dceb;">↓</span>
<span style="color:#f38ba8;">[Encoder Layer 1~6]</span>
      <span style="color:#89dceb;">↓</span>
<span style="color:#89dceb;">[Decoder ...]</span></div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> Positional Encoding은 <b style="color:#1681c4;">Encoder에 들어가기 직전, 딱 한 번</b> 수행됩니다.<br>
이후 Self-Attention은 순서 정보가 담긴 벡터를 받아 올바르게 처리할 수 있습니다.
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
    <b style="color:#FF6B00;">단순 번호(1, 2, 3...)</b>는 문장이 길면 값이 너무 커져서 부적합합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">sin/cos 파동 패턴</b>을 사용하면 항상 -1~1 사이의 값으로 모든 위치를 고유하게 표현할 수 있습니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    위치 인코딩 벡터는 단어 의미 벡터에 <b style="color:#FF6B00;">더하는(+)</b> 방식으로 합쳐집니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이 과정은 Encoder 입력 직전, <b style="color:#FF6B00;">딱 한 번</b> 수행됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    덕분에 Transformer는 "나는 밥을 먹었다"와 "밥을 나는 먹었다"를 <b style="color:#FF6B00;">다른 문장으로 구분</b>할 수 있습니다.
  </div>
</div>

</div>

</div>