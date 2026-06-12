<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Transformer의 전체 구조 — 내부 블록 구성
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Encoder와 Decoder 각각의
<b style="color:#1681c4;">내부 블록</b>을 살펴보고, 데이터가 흐르는 전체 경로를 따라가 봅니다.
</p>

</div>

<br>

<!-- Encoder 내부 구조 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧩 Encoder 레이어 하나의 내부 구조
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Encoder 레이어 하나는 <b>4개의 구성 블록</b>으로 이루어져 있습니다.<br>
각 블록이 무엇을 하는지 간단히 파악해봅시다. <span style="color:#94a3b8;">(각각 뒤에서 자세히 배웁니다!)</span>
</p>

<div style="display: grid; gap: 0; margin: 18px 0;">

  <div style="text-align: center; font-size: 13px; color: #475569; font-weight: 900; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:10px 14px;">
    입력 (단어 벡터들)
  </div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin: 4px 0;">↓</div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center; gap:12px;">
    <div>
      <div style="font-size:14px; font-weight:900; color:#FF6B00;">① Self-Attention</div>
      <div style="font-size:13px; color:#475569; margin-top:4px;">"이 단어가 다른 어떤 단어와 관련 있나?"</div>
    </div>
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">챕터 4 복습</div>
  </div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin: 4px 0;">↓</div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center; gap:12px;">
    <div>
      <div style="font-size:14px; font-weight:900; color:#475569;">② Add & Norm</div>
      <div style="font-size:13px; color:#475569; margin-top:4px;">"원래 값 + 새 값, 안정적으로 합치기"</div>
    </div>
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">5-5</div>
  </div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin: 4px 0;">↓</div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center; gap:12px;">
    <div>
      <div style="font-size:14px; font-weight:900; color:#FF6B00;">③ Feed Forward Network</div>
      <div style="font-size:13px; color:#475569; margin-top:4px;">"각 단어 벡터를 더 풍부하게 변환"</div>
    </div>
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">5-6</div>
  </div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin: 4px 0;">↓</div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center; gap:12px;">
    <div>
      <div style="font-size:14px; font-weight:900; color:#475569;">④ Add & Norm</div>
      <div style="font-size:13px; color:#475569; margin-top:4px;">"또 한 번 안정적으로 합치기"</div>
    </div>
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">5-5</div>
  </div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin: 4px 0;">↓</div>

  <div style="text-align: center; font-size: 13px; color: #1681c4; font-weight: 900; background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:10px 14px;">
    출력 (더 풍부해진 단어 벡터들)
  </div>

</div>

</div>

<br>

<!-- Decoder 내부 구조 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧩 Decoder 레이어 하나의 내부 구조
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Decoder 레이어는 Encoder보다 <b>블록이 하나 더</b> 있습니다. 총 <b style="color:#1681c4;">6개의 구성 블록</b>으로 이루어집니다.
</p>

<div style="display: grid; gap: 0; margin: 18px 0;">

  <div style="text-align: center; font-size: 13px; color: #475569; font-weight: 900; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:10px 14px;">
    입력 (지금까지 생성한 단어들)
  </div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin: 4px 0;">↓</div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center; gap:12px;">
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4;">① Masked Self-Attention</div>
      <div style="font-size:13px; color:#475569; margin-top:4px;">"앞에 나온 단어들만 참고" <span style="color:#94a3b8;">(미래 단어는 가림)</span></div>
    </div>
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">5-8</div>
  </div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin: 4px 0;">↓</div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center; gap:12px;">
    <div>
      <div style="font-size:14px; font-weight:900; color:#475569;">② Add & Norm</div>
    </div>
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">5-5</div>
  </div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin: 4px 0;">↓</div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center; gap:12px;">
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4;">③ Encoder-Decoder Attention</div>
      <div style="font-size:13px; color:#475569; margin-top:4px;">"Encoder가 이해한 내용을 참고해서 어떤 단어를 쓸까?"</div>
      <div style="margin-top:6px; font-size:12px; color:#94a3b8;">← Encoder의 출력도 함께 들어옴</div>
    </div>
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">5-7</div>
  </div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin: 4px 0;">↓</div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center; gap:12px;">
    <div>
      <div style="font-size:14px; font-weight:900; color:#475569;">④ Add & Norm</div>
    </div>
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">5-5</div>
  </div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin: 4px 0;">↓</div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center; gap:12px;">
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4;">⑤ Feed Forward Network</div>
    </div>
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">5-6</div>
  </div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin: 4px 0;">↓</div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center; gap:12px;">
    <div>
      <div style="font-size:14px; font-weight:900; color:#475569;">⑥ Add & Norm</div>
    </div>
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:900; white-space:nowrap;">5-5</div>
  </div>
  <div style="text-align: center; color: #94a3b8; font-size: 18px; font-weight: 900; margin: 4px 0;">↓</div>

  <div style="text-align: center; font-size: 13px; color: #1681c4; font-weight: 900; background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:10px 14px;">
    출력 (다음에 올 단어 예측)
  </div>

</div>

</div>

<br>

<!-- 각 블록 정리 표 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📋 각 블록 한눈에 정리
</h2>

<div style="overflow-x: auto; margin-top: 14px;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; font-weight:900;">블록 이름</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">등장 위치</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">하는 일</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">배우는 섹션</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Self-Attention</td>
      <td style="padding:10px 14px; color:#475569;">Encoder</td>
      <td style="padding:10px 14px; color:#475569;">입력 단어들끼리 서로의 관계 파악</td>
      <td style="padding:10px 14px; color:#94a3b8;">챕터 4 복습</td>
    </tr>
    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Masked Self-Attention</td>
      <td style="padding:10px 14px; color:#475569;">Decoder</td>
      <td style="padding:10px 14px; color:#475569;">생성된 단어끼리 관계 파악 (미래 차단)</td>
      <td style="padding:10px 14px; color:#94a3b8;">5-8</td>
    </tr>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Encoder-Decoder Attention</td>
      <td style="padding:10px 14px; color:#475569;">Decoder</td>
      <td style="padding:10px 14px; color:#475569;">Encoder 결과 참고</td>
      <td style="padding:10px 14px; color:#94a3b8;">5-7</td>
    </tr>
    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">Add & Norm</td>
      <td style="padding:10px 14px; color:#475569;">Encoder · Decoder</td>
      <td style="padding:10px 14px; color:#475569;">잔차 연결 + 정규화로 학습 안정화</td>
      <td style="padding:10px 14px; color:#94a3b8;">5-5</td>
    </tr>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">Feed Forward Network</td>
      <td style="padding:10px 14px; color:#475569;">Encoder · Decoder</td>
      <td style="padding:10px 14px; color:#475569;">각 단어 표현을 비선형 변환</td>
      <td style="padding:10px 14px; color:#94a3b8;">5-6</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:10px 14px; font-weight:900; color:#1681c4;">Positional Encoding</td>
      <td style="padding:10px 14px; color:#475569;">입력 단계</td>
      <td style="padding:10px 14px; color:#475569;">단어의 순서 정보 추가</td>
      <td style="padding:10px 14px; color:#94a3b8;">5-3</td>
    </tr>
  </tbody>
</table>
</div>

</div>

<br>

<!-- 데이터 흐름 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔄 데이터가 흐르는 전체 경로
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
실제로 번역을 할 때 데이터가 어떻게 흐르는지 한 번에 따라가 봅시다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; font-weight: 900; text-align: center; margin-bottom: 16px;">
<span style="color: #1681c4;">"나는 밥을 먹었다" → "I ate rice"</span>
</div>

<div style="display: grid; gap: 10px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 1</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:4px;">입력 토큰화</div>
      <div style="font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8;">
        "나는 밥을 먹었다" → <span style="color:#89dceb;">["나는", "밥을", "먹었다"]</span>
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 2</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:4px;">임베딩 + Positional Encoding</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">각 단어를 벡터로 변환 + <b>순서 정보 추가</b></div>
      <div style="font-family:Consolas, monospace; font-size:13px; color:#cba6f7; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8; margin-top:6px;">
        [나는_벡터, 밥을_벡터, 먹었다_벡터] <span style="color:#6c7086;">(위치 정보 포함)</span>
      </div>
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 3</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:4px;">Encoder 6번 통과</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">Self-Attention + FFN 반복 × 6</div>
      <div style="font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8; margin-top:6px;">
        [<span style="color:#f38ba8;">풍부해진_나는</span>, <span style="color:#f38ba8;">풍부해진_밥을</span>, <span style="color:#f38ba8;">풍부해진_먹었다</span>]
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 4</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:4px;">Decoder에서 생성 시작</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">[시작 신호] + Encoder 출력 참고</div>
      <div style="font-family:Consolas, monospace; font-size:13px; color:#89dceb; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8; margin-top:6px;">
        → <span style="color:#a6e3a1;">"I"</span> 생성
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 5</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:4px;">"I"를 보면서 다음 단어 생성</div>
      <div style="font-family:Consolas, monospace; font-size:13px; color:#89dceb; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8; margin-top:6px;">
        <span style="color:#6c7086;">["I"]</span> + Encoder 출력 참고 → <span style="color:#a6e3a1;">"ate"</span> 생성
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">STEP 6</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:4px;">반복...</div>
      <div style="font-family:Consolas, monospace; font-size:13px; color:#89dceb; background:#0f172a; padding:8px 12px; border-radius:8px; line-height:1.8; margin-top:6px;">
        <span style="color:#6c7086;">["I", "ate"]</span> → <span style="color:#a6e3a1;">"rice"</span> 생성<br>
        <span style="color:#6c7086;">["I", "ate", "rice"]</span> → <span style="color:#cba6f7;">[종료 신호]</span> 생성
      </div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 왜 복잡한가 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💡 "이걸 왜 이렇게 복잡하게 만들었나요?"
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
처음 보면 복잡해 보이지만, 각 블록은 <b>명확한 이유</b>가 있어 추가되었습니다.
</p>

<div style="display: grid; gap: 8px; margin-top: 14px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; font-size:18px;">🔗</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:2px;">Self-Attention</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">단어 간 관계 파악 → <b>문맥 이해</b></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; font-size:18px;">⚖️</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:2px;">Add & Norm</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">학습이 불안정해지는 것 방지 → <b>안정적인 학습</b></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; font-size:18px;">🔧</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:2px;">Feed Forward</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">Attention이 잡지 못한 정보 보완 → <b>표현력 향상</b></div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="flex-shrink:0; font-size:18px;">🚫</div>
    <div>
      <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:2px;">Masked Attention</div>
      <div style="font-size:13px; color:#475569; line-height:1.7;">아직 생성 안 된 단어를 미리 보는 "치팅" 방지</div>
    </div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 각 블록 하나하나가 없으면 성능이 눈에 띄게 떨어집니다.<br>
<b style="color:#FF6B00;">수십 차례의 실험을 통해 검증된 구조</b>입니다.
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
    Transformer는 <b style="color:#FF6B00;">Encoder + Decoder</b> 두 파트로 구성됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Encoder 레이어 = <b style="color:#FF6B00;">Self-Attention → Add&Norm → FFN → Add&Norm</b> (4블록)
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Decoder 레이어 = <b style="color:#FF6B00;">Masked Self-Attention → Add&Norm → Enc-Dec Attention → Add&Norm → FFN → Add&Norm</b> (6블록)
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이 레이어가 <b style="color:#FF6B00;">각각 6번씩 쌓여서</b> 깊고 풍부한 표현을 학습합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    다음 섹션부터 각 구성 요소를 <b style="color:#FF6B00;">하나씩 자세히</b> 배웁니다.
  </div>
</div>

</div>

</div>