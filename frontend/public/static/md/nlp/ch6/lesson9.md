<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
문맥이 벡터에 담기는 과정
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
같은 단어라도 문장에 따라 벡터가 달라집니다.<br>
BERT의 <b style="color:#1681c4;">문맥화된 표현(Contextualized Representation)</b>이 어떻게 만들어지는지 알아봅니다.
</p>

</div>

<br>

<!-- 같은 단어 다른 벡터 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 같은 단어인데 벡터가 달라진다?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Word2Vec은 단어마다 <b>하나의 고정된 벡터</b>를 가집니다. "사과"는 항상 같은 벡터였습니다.<br>
BERT는 다릅니다. <b style="color:#1681c4;">같은 단어라도 문장에 따라 다른 벡터</b>를 가집니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; overflow:hidden;">
    <div style="background:#0f172a; padding:10px 16px;">
      <div style="font-size:13px; font-weight:900; color:#c3e88d;">문장 ①</div>
    </div>
    <div style="background:#1e1e2e; padding:14px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.3; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"나는 사과를 먹었다"</span>
<span style="color:#6c7086;">→ BERT의 "사과" 벡터:</span>
<span style="color:#89dceb;">[0.8, -0.3, 0.5, ...]</span>
<span style="color:#f9e2af;">← 과일 의미</span></div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; overflow:hidden;">
    <div style="background:#0f172a; padding:10px 16px;">
      <div style="font-size:13px; font-weight:900; color:#c3e88d;">문장 ②</div>
    </div>
    <div style="background:#1e1e2e; padding:14px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.3; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"그는 진심으로 사과를 했다"</span>
<span style="color:#6c7086;">→ BERT의 "사과" 벡터:</span>
<span style="color:#89dceb;">[0.2, 0.7, -0.4, ...]</span>
<span style="color:#cba6f7;">← 사죄 의미</span></div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">🔑</span> 두 벡터는 완전히 다릅니다. 바로 이것이 BERT의 출력을 <b style="color:#1681c4;">문맥화된 표현(Contextualized Representation)</b>이라고 부르는 이유입니다.
</div>

</div>

<br>

<!-- 층이 깊어질수록 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🏗️ 층(Layer)이 깊어질수록 문맥이 풍부해진다
</h2>

<!-- 비유: 독서 감상문 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px; margin-bottom:18px;">
<div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:14px;">📖 비유: 독서 감상문 쓰기</div>
<table style="width:100%; border-collapse:separate; border-spacing:0 10px; font-size:13px;">
<tbody>
<tr>
<td style="width:90px; vertical-align:top; padding:0;"><div style="background:#e2e8f0; color:#64748b; padding:7px 10px; border-radius:8px; font-weight:900; text-align:center; white-space:nowrap;">1층</div></td>
<td style="vertical-align:top; padding:0 0 0 10px;"><div style="background:#ffffff; border:2px solid #e2e8f0; border-radius:12px; padding:12px 14px;"><div style="font-weight:900; color:#64748b; margin-bottom:8px;">처음 읽을 때 — 단어의 뜻 파악</div><div style="background:#0f172a; color:#a6e3a1; padding:9px 12px; border-radius:8px; font-family:'JetBrains Mono','Consolas',monospace; line-height:1.7;">&quot;카페 = 커피를 파는 곳&quot;</div></div></td>
</tr>
<tr>
<td style="width:90px; vertical-align:top; padding:0;"><div style="background:#c2e4ff; color:#1681c4; padding:7px 10px; border-radius:8px; font-weight:900; text-align:center; white-space:nowrap;">4~6층</div></td>
<td style="vertical-align:top; padding:0 0 0 10px;"><div style="background:#ffffff; border:2px solid #c2e4ff; border-radius:12px; padding:12px 14px;"><div style="font-weight:900; color:#1681c4; margin-bottom:8px;">두 번째 읽을 때 — 문장 구조와 관계 파악</div><div style="background:#0f172a; color:#89dceb; padding:9px 12px; border-radius:8px; font-family:'JetBrains Mono','Consolas',monospace; line-height:1.7;">&quot;카페에서 = 카페가 장소를 나타내는 역할&quot;</div></div></td>
</tr>
<tr>
<td style="width:90px; vertical-align:top; padding:0;"><div style="background:#1681c4; color:#ffffff; padding:7px 10px; border-radius:8px; font-weight:900; text-align:center; white-space:nowrap;">9~12층</div></td>
<td style="vertical-align:top; padding:0 0 0 10px;"><div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:12px 14px;"><div style="font-weight:900; color:#1681c4; margin-bottom:8px;">세 번째 읽을 때 — 전체 문맥의 의미와 의도 파악</div><div style="background:#0f172a; color:#cba6f7; padding:9px 12px; border-radius:8px; font-family:'JetBrains Mono','Consolas',monospace; line-height:1.7;">&quot;나는 오늘 카페에서 커피를 마셨다 = 화자의 일상적 행동 묘사&quot;</div></div></td>
</tr>
</tbody>
</table>
</div>

<!-- 벡터 변화 시각화 -->
<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">"배" 벡터의 층별 변화 (4차원으로 축소한 예시)</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">문장: "나는 배를 탔다"</span>

<span style="color:#6c7086;">[1층 통과 후 — "배" 벡터]</span>
<span style="color:#cdd6f4;">[0.5, 0.5, 0.5, 0.5]</span>
<span style="color:#6c7086;">→ 아직 의미가 불분명 (배? 선박? 과일? 복부?)</span>

<span style="color:#6c7086;">[4층 통과 후 — "배" 벡터]</span>
<span style="color:#89dceb;">[0.3, 0.8, 0.2, 0.4]</span>
<span style="color:#6c7086;">→ "탔다"와의 관계를 반영 중 (탑승 의미 쪽으로 이동)</span>

<span style="color:#6c7086;">[12층 통과 후 — "배" 벡터]</span>
<span style="color:#a6e3a1; font-weight:900;">[0.1, 0.95, 0.05, 0.2]</span>
<span style="color:#6c7086;">→ 선박(ship)의 의미로 완전히 수렴</span>
<span style="color:#6c7086;">   "나는", "를", "탔다" 모두 반영된 최종 표현</span></div>
</div>

</div>

<br>

<!-- 헤드마다 다른 문맥 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎭 헤드마다 다른 문맥을 포착한다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Multi-Head Self-Attention에서 각 헤드는 서로 다른 관계에 집중합니다.
실제 BERT 연구에서 밝혀진 내용입니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#e2e8f0; color:#64748b; padding:4px 9px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap;">Head 1~2</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">인접한 단어 사이의 관계</div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#e2e8f0; color:#64748b; padding:4px 9px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap;">Head 3~4</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">주어-동사 관계</div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#c2e4ff; color:#1681c4; padding:4px 9px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap;">Head 5~6</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">대명사와 지칭 대상</div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#c2e4ff; color:#1681c4; padding:4px 9px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap;">Head 7~8</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">동사와 목적어 관계</div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#ffd0b0; color:#FF6B00; padding:4px 9px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap;">Head 9~10</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">수식어와 피수식어</div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:center;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:4px 9px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap;">Head 11~12</div>
    <div style="font-size:13px; color:#334155; line-height:1.6;">문장 전체 흐름</div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 이 12가지 시각이 모두 합쳐져 하나의 <b style="color:#FF6B00;">풍부한 문맥 벡터</b>가 됩니다.
</div>

</div>

<br>

<!-- 실제 과제 활용 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📌 "문맥화된 표현"이 실제 과제에서 어떻게 쓰이나요?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BERT가 문장을 처리하고 나면, 각 토큰 위치에 <b>768차원 벡터</b>가 남습니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">BERT 출력 구조</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">입력:  </span><span style="color:#a6e3a1;">[CLS]  나는  배를  탔다  [SEP]</span>
       <span style="color:#6c7086;">↓      ↓    ↓    ↓     ↓</span>
<span style="color:#6c7086;">출력:  </span><span style="color:#89dceb;"> h₀     h₁   h₂   h₃    h₄</span>
      <span style="color:#6c7086;">(768) (768) (768) (768) (768)</span></div>
</div>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 10px; border-radius:8px; font-family:Consolas,monospace; font-size:13px; font-weight:900; white-space:nowrap;">h₀ [CLS]</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:4px;">문장 분류 (감정 분석 등)</div>
      <div style="font-size:13px; color:#475569; line-height:1.6;">문장 전체 의미가 담긴 [CLS]로 분류합니다.</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#64748b; color:#fff; padding:5px 10px; border-radius:8px; font-family:Consolas,monospace; font-size:13px; font-weight:900; white-space:nowrap;">h₁, h₂...</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#64748b; margin-bottom:4px;">단어 분류 (개체명 인식)</div>
      <div style="font-size:13px; color:#475569; line-height:1.6;">각 단어 벡터로 품사/개체명을 판별합니다.</div>
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:5px 10px; border-radius:8px; font-family:Consolas,monospace; font-size:13px; font-weight:900; white-space:nowrap;">전체 벡터</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:4px;">질의응답</div>
      <div style="font-size:13px; color:#475569; line-height:1.6;">정답 위치(시작~끝)를 찾습니다.</div>
    </div>
  </div>

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
    BERT의 출력은 <b style="color:#FF6B00;">문맥화된 표현</b>으로, 같은 단어라도 문장에 따라 벡터가 달라집니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    층이 깊어질수록 <b style="color:#FF6B00;">표면적 특징 → 문법 → 의미 수준</b>의 문맥이 반영됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <b style="color:#FF6B00;">Multi-Head</b>는 주어-동사 관계, 대명사 지칭 등 서로 다른 관계를 동시에 포착합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    최종 출력 벡터는 과제에 따라 <b style="color:#FF6B00;">[CLS] 벡터 또는 각 토큰 벡터</b>를 활용해 다양한 문제를 풉니다.
  </div>
</div>

</div>

</div>