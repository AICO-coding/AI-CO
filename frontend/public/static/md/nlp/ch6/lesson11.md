<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
MLM의 정확한 작동 규칙
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
MLM은 단어를 무작위로 가리지만, 정해진 규칙이 있습니다.<br>
<b style="color:#1681c4;">15% 선택</b>과 <b style="color:#1681c4;">80/10/10 전략</b>이 왜 필요한지 이해합니다.
</p>

</div>

<br>

<!-- 15% 선택 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎲 MLM은 어떻게 단어를 고를까요?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
MLM 학습 시 입력 문장의 <b>전체 토큰 중 15%</b>를 무작위로 선택합니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">15% 선택 예시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">예시 문장 (10개 토큰):</span>
<span style="color:#cdd6f4;">나는 / 오늘 / 카페 / 에서 / 친구 / 와 / 커피 / 를 / 마셨 / 다</span>

<span style="color:#6c7086;">15% = 약 1~2개 선택</span>
<span style="color:#6c7086;">→ </span><span style="color:#f9e2af; font-weight:900;">"카페"</span><span style="color:#6c7086;">와 </span><span style="color:#f9e2af; font-weight:900;">"커피"</span><span style="color:#6c7086;"> 선택됨</span></div>
</div>

<!-- 왜 15%인가 -->
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-top: 16px;">

  <div style="background:#fff1f2; border:2px solid #fca5a5; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:22px; font-weight:900; color:#dc2626; margin-bottom:6px;">50%+</div>
    <div style="font-size:13px; font-weight:900; color:#dc2626; margin-bottom:6px;">너무 많이 가리면</div>
    <div style="font-size:12px; color:#475569; line-height:1.6;">문맥 정보가 부족해서 맞히기 어려움 ❌</div>
  </div>

  <div style="background:#f0fdf4; border:2px solid #86efac; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:22px; font-weight:900; color:#16a34a; margin-bottom:6px;">15%</div>
    <div style="font-size:13px; font-weight:900; color:#16a34a; margin-bottom:6px;">균형점 ✅</div>
    <div style="font-size:12px; color:#475569; line-height:1.6;">충분한 문맥 유지 + 의미 있는 학습</div>
  </div>

  <div style="background:#fff1f2; border:2px solid #fca5a5; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:22px; font-weight:900; color:#dc2626; margin-bottom:6px;">1~2%</div>
    <div style="font-size:13px; font-weight:900; color:#dc2626; margin-bottom:6px;">너무 적게 가리면</div>
    <div style="font-size:12px; color:#475569; line-height:1.6;">학습이 너무 느림 ❌</div>
  </div>

</div>

</div>

<br>

<!-- 80/10/10 전략 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎯 선택된 15% 중에서도 세 가지로 나뉩니다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
선택된 토큰을 <b>전부 [MASK]로 바꾸지 않습니다.</b> BERT 논문의 <b>80/10/10 전략</b>을 사용합니다.
</p>

<!-- 비율 시각화: 중첩 div 대신 table로 구성 -->
<div style="margin:16px 0; overflow-x:auto;">
<table style="width:100%; border-collapse:separate; border-spacing:0; background:#0f172a; border-radius:14px; overflow:hidden; font-size:13px;">
  <thead>
    <tr>
      <th colspan="3" style="padding:14px 16px; text-align:left; color:#c3e88d; font-weight:900; border-bottom:1px solid #1e293b;">
        선택된 15% 토큰 처리 방식
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="width:70px; padding:12px 14px; border-bottom:1px solid #1e293b;">
        <span style="display:inline-block; background:#FF6B00; color:#fff; padding:5px 10px; border-radius:8px; font-weight:900;">80%</span>
      </td>
      <td style="padding:12px 14px; color:#f9e2af; font-family:Consolas, monospace; border-bottom:1px solid #1e293b;">
        [MASK]로 교체
      </td>
      <td style="padding:12px 14px; color:#94a3b8; border-bottom:1px solid #1e293b;">
        가장 흔한 경우
      </td>
    </tr>
    <tr>
      <td style="width:70px; padding:12px 14px; border-bottom:1px solid #1e293b;">
        <span style="display:inline-block; background:#1681c4; color:#fff; padding:5px 10px; border-radius:8px; font-weight:900;">10%</span>
      </td>
      <td style="padding:12px 14px; color:#89dceb; font-family:Consolas, monospace; border-bottom:1px solid #1e293b;">
        엉뚱한 다른 단어로 교체
      </td>
      <td style="padding:12px 14px; color:#94a3b8; border-bottom:1px solid #1e293b;">
        노이즈 주입
      </td>
    </tr>
    <tr>
      <td style="width:70px; padding:12px 14px;">
        <span style="display:inline-block; background:#64748b; color:#fff; padding:5px 10px; border-radius:8px; font-weight:900;">10%</span>
      </td>
      <td style="padding:12px 14px; color:#a6e3a1; font-family:Consolas, monospace;">
        원래 단어 그대로 유지
      </td>
      <td style="padding:12px 14px; color:#94a3b8;">
        변화 없음
      </td>
    </tr>
  </tbody>
</table>
</div>

<!-- 세 가지 경우 -->
<div style="display: grid; gap: 14px; margin-top: 18px;">

  <!-- ① 80% MASK -->
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">경우 ① 80%</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">[MASK]로 교체</div>
    </div>
    <div style="background:#1e1e2e; border-radius:10px; padding:12px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.2; overflow-x:auto; margin-bottom:10px;">
  <div><span style="color:#6c7086;">입력: </span><span style="color:#cdd6f4;">나는  오늘  </span><span style="color:#f38ba8; font-weight:900;">[MASK]</span><span style="color:#cdd6f4;">  에서  커피를  마셨다</span></div>
  <div><span style="color:#6c7086;">정답: </span><span style="color:#a6e3a1;">카페</span></div>
</div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">모델은 빈칸을 앞뒤 문맥으로 채워야 합니다. 가장 일반적인 MLM 학습 방식입니다.</div>
  </div>

  <!-- ② 10% 랜덤 -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">경우 ② 10%</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">엉뚱한 단어로 교체</div>
    </div>
    <div style="background:#1e1e2e; border-radius:10px; padding:12px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.2; overflow-x:auto; margin-bottom:10px;">
  <div><span style="color:#6c7086;">입력: </span><span style="color:#cdd6f4;">나는  오늘  </span><span style="color:#f38ba8; font-weight:900;">버스</span><span style="color:#cdd6f4;">  에서  커피를  마셨다</span></div>
  <div><span style="color:#6c7086;">정답: </span><span style="color:#a6e3a1;">카페  (원래 단어)</span></div>
</div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">이상한 단어가 들어있는 걸 눈치채고 수정해야 합니다. <b style="color:#1681c4;">모든 토큰을 항상 의심하는 능력</b>을 키웁니다.</div>
  </div>

  <!-- ③ 10% 그대로 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#64748b; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">경우 ③ 10%</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">원래 단어 그대로</div>
    </div>
    <div style="background:#1e1e2e; border-radius:10px; padding:12px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.2; overflow-x:auto; margin-bottom:10px;">
  <div><span style="color:#6c7086;">입력: </span><span style="color:#cdd6f4;">나는  오늘  </span><span style="color:#a6e3a1; font-weight:900;">카페</span><span style="color:#cdd6f4;">  에서  커피를  마셨다</span></div>
  <div><span style="color:#6c7086;">정답: </span><span style="color:#a6e3a1;">카페  (원래 단어)</span></div>
</div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">외형상 변화 없이도 해당 위치를 예측합니다. 모델이 <b>"바뀐 것만 처리하면 된다"는 편법</b>을 쓰지 못하게 합니다.</div>
  </div>

</div>

</div>

<br>

<!-- 왜 세 가지로 나누나 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🤔 왜 굳이 세 가지로 나눌까요?
</h2>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 14px;">

  <div style="background:#fff1f2; border:2px solid #fca5a5; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#dc2626; margin-bottom:10px;">❌ 만약 [MASK]만 쓴다면?</div>
    <div style="background:#1e1e2e; border-radius:10px; padding:12px 14px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.0; overflow-x:auto; white-space:pre; margin-bottom:10px;">
<span style="color:#6c7086;">사전학습: [MASK] 있을 때만 예측
미세조정: 실제 문장엔 [MASK] 없음
결과:     불일치(mismatch) 발생!</span></div>
    <div style="font-size:13px; color:#475569; line-height:1.6;">사전학습과 실제 사용 환경의 차이가 생겨 성능이 저하됩니다.</div>
  </div>

  <div style="background:#f0fdf4; border:2px solid #86efac; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#16a34a; margin-bottom:10px;">✅ 80/10/10 섞으면?</div>
    <div style="background:#1e1e2e; border-radius:10px; padding:12px 14px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.0; overflow-x:auto; white-space:pre; margin-bottom:10px;">
<span style="color:#a6e3a1;">"어떤 토큰이든 틀릴 수 있으니
 모든 위치를 문맥과 대조해야 해!"</span></div>
    <div style="font-size:13px; color:#475569; line-height:1.6;">모든 토큰을 능동적으로 파악해, 미세조정 단계에서도 자연스럽게 작동합니다.</div>
  </div>

</div>

</div>

<br>

<!-- MLM 전체 흐름 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📊 MLM 학습 흐름 전체 정리
</h2>

<div style="display: grid; gap: 8px; margin-top: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">STEP 1</div>
    <div>
      <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:4px;">대규모 텍스트에서 문장 가져오기</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#a6e3a1; margin-top:6px;">"철수는 공원에서 강아지와 함께 산책을 했다"</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">STEP 2</div>
    <div>
      <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:4px;">토큰화 (총 10개 토큰)</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; color:#cdd6f4; margin-top:6px;">철수 / 는 / 공원 / 에서 / 강아지 / 와 / 함께 / 산책 / 을 / 했다</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#FF6B00; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">STEP 3</div>
    <div>
      <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:4px;">15% 무작위 선택 → 80/10/10 규칙 적용</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; line-height:2.0; color:#cdd6f4; margin-top:6px; overflow-x:auto; white-space:pre;"><span style="color:#6c7086;">"공원" → </span><span style="color:#f38ba8;">[MASK]</span><span style="color:#6c7086;">  (80%)</span>
<span style="color:#6c7086;">"산책" → </span><span style="color:#f38ba8;">"버스"</span><span style="color:#6c7086;">  (10%, 랜덤 교체)</span></div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:13px 16px; display:flex; gap:12px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">STEP 4</div>
    <div>
      <div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:4px;">BERT 예측 → 정답과 비교 → 가중치 업데이트</div>
      <div style="background:#1e1e2e; border-radius:8px; padding:8px 12px; font-family:Consolas,monospace; font-size:12px; line-height:2.0; color:#cdd6f4; margin-top:6px; overflow-x:auto; white-space:pre;"><span style="color:#6c7086;">예측: </span><span style="color:#a6e3a1;">"공원" ✅</span><span style="color:#6c7086;">,  </span><span style="color:#a6e3a1;">"산책" ✅</span><span style="color:#6c7086;">  → 학습 완료</span></div>
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
    MLM은 전체 토큰의 <b style="color:#FF6B00;">15%</b>를 선택해서 처리합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    선택된 토큰은 <b style="color:#FF6B00;">80%는 [MASK], 10%는 랜덤 단어, 10%는 원래 단어</b>로 처리합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    세 가지를 섞는 이유는 <b style="color:#FF6B00;">사전학습과 미세조정의 불일치를 줄이고</b>, 모든 위치를 능동적으로 파악하게 하기 위해서입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이 과정 전체에서 <b style="color:#FF6B00;">사람이 정답을 만들 필요가 없습니다.</b> 원문이 곧 정답입니다.
  </div>
</div>

</div>

</div>