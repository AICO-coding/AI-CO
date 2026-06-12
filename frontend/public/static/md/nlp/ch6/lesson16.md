<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
[CLS] 토큰
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
BERT는 문장을 처리하고 나면 각 토큰 위치마다 벡터를 출력합니다.<br>
그 중 <b style="color:#1681c4;">[CLS] 토큰</b>이 어떻게 문장 전체의 의미를 담게 되는지 알아봅니다.
</p>

</div>

<br>

<!-- 왜 [CLS]가 필요한가 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧐 특수 토큰이 왜 필요할까요?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BERT는 문장을 처리하고 나면 <b>각 토큰 위치마다 벡터를 하나씩 출력</b>합니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">BERT 입출력 구조</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">입력:  </span><span style="color:#f38ba8;">[CLS]</span>  <span style="color:#a6e3a1;">나는  오늘  카페  에서  커피를  마셨다</span>  <span style="color:#f38ba8;">[SEP]</span>
       <span style="color:#6c7086;">↓      ↓    ↓    ↓    ↓     ↓      ↓        ↓</span>
<span style="color:#6c7086;">출력:  </span><span style="color:#f9e2af; font-weight:900;">h₀</span>     <span style="color:#89dceb;">h₁   h₂   h₃   h₄    h₅     h₆       h₇</span></div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> "이 리뷰가 긍정적인가, 부정적인가?" 같은 분류 문제에서는 단어 하나하나가 아닌<br>
<b style="color:#FF6B00;">문장 전체를 대표하는 벡터 하나</b>가 필요합니다. 그 역할을 하는 것이 바로 <b style="color:#FF6B00;">[CLS] 토큰</b>입니다.
</div>

</div>

<br>

<!-- [CLS] 토큰이란 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🏆 [CLS] 토큰이란?
</h2>

<div style="display: grid; grid-template-columns: auto 1fr; gap: 20px; align-items: center; margin-bottom: 18px;">
  <div style="background:#1681c4; color:#fff; padding:10px 16px; border-radius:12px; font-family:Consolas,monospace; font-size:20px; font-weight:900; white-space:nowrap;">[CLS]</div>
  <div>
    <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:4px;">Classification의 약자</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">BERT 입력 문장의 <b>맨 앞에 항상 붙는</b> 특수 토큰. 항상 0번 위치에 위치합니다.</div>
  </div>
</div>

<div style="background-color: #1e1e2e; border-radius: 12px; padding: 14px 18px; font-family:'JetBrains Mono','Consolas',monospace; font-size: 13px; color: #cdd6f4; line-height: 2.2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">모든 BERT 입력:</span>
<span style="color:#f38ba8;">[CLS]</span> <span style="color:#6c7086;">+</span> <span style="color:#a6e3a1;">실제 문장 토큰들</span> <span style="color:#6c7086;">+</span> <span style="color:#f38ba8;">[SEP]</span>
 <span style="color:#f9e2af;">↑
 항상 0번 위치</span></div>

</div>

<br>

<!-- 어떻게 문장 의미를 담나 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🌊 [CLS]는 어떻게 문장 전체 의미를 담게 될까요?
</h2>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 18px;">

  <div style="background:#fff1f2; border:2px solid #fca5a5; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#dc2626; margin-bottom:8px;">처음 입력될 때</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      <code style="background:#fff; border:1px solid #fca5a5; color:#dc2626; padding:1px 5px; border-radius:4px; font-weight:900;">[CLS]</code>는 사실 <b style="color:#dc2626;">아무 의미도 없는 빈 슬롯</b>입니다.
    </div>
  </div>

  <div style="background:#f0fdf4; border:2px solid #86efac; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#16a34a; margin-bottom:8px;">12층 통과 후</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      Self-Attention으로 <b style="color:#16a34a;">문장 전체의 의미가 집약</b>된 벡터가 됩니다.
    </div>
  </div>

</div>

<!-- 비유: 반장 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:14px;">🏫 비유: 반장이 반 전체를 대표하는 과정</div>
  <div style="display: grid; gap: 8px;">

    <div style="display:flex; gap:12px; align-items:center;">
      <div style="flex-shrink:0; background:#e2e8f0; color:#64748b; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap;">1층</div>
      <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:10px 14px; font-size:13px; color:#334155; line-height:1.6; flex:1;">
        반장([CLS])이 반 학생 전체의 의견을 한 번 듣습니다.
      </div>
    </div>

    <div style="display:flex; gap:12px; align-items:center;">
      <div style="flex-shrink:0; background:#c2e4ff; color:#1681c4; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap;">6층</div>
      <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:10px 14px; font-size:13px; color:#334155; line-height:1.6; flex:1;">
        반장이 의견을 바탕으로 다시 소통하며 점점 종합합니다.
      </div>
    </div>

    <div style="display:flex; gap:12px; align-items:center;">
      <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap;">12층</div>
      <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:10px 14px; font-size:13px; color:#334155; line-height:1.6; flex:1;">
        반장은 이제 반 전체의 분위기, 주요 의견, 핵심 정보를 모두 반영한 <b style="color:#1681c4;">"대표 의견"</b>을 갖게 됩니다.
      </div>
    </div>

  </div>
  <div style="margin-top: 12px; background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; line-height:1.7; text-align:center;">
    이 최종 반장의 의견 = <b style="color:#1681c4;">[CLS] 출력 벡터 (h₀)</b>
  </div>
</div>

</div>

<br>

<!-- 실제 활용 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎯 [CLS] 벡터의 실제 활용
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 16px;">
사전학습이 끝난 BERT를 문장 분류 과제에 미세조정(Fine-tuning)할 때, <code style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:2px 7px; border-radius:6px; font-weight:900;">[CLS]</code> 출력 벡터 하나만 꺼내서 <b>분류기</b>에 연결합니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">감정 분류 Fine-tuning 흐름</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#6c7086;">입력:  </span><span style="color:#f38ba8;">[CLS]</span> <span style="color:#a6e3a1;">이 영화 정말 최고였어요</span> <span style="color:#f38ba8;">[SEP]</span>
         <span style="color:#6c7086;">↓</span>
   <span style="color:#cba6f7;">BERT 12층 통과</span>
         <span style="color:#6c7086;">↓</span>
<span style="color:#6c7086;">출력:  </span><span style="color:#f9e2af; font-weight:900;">h₀</span>     <span style="color:#89dceb;">h₁    h₂   ...</span>
      <span style="color:#f9e2af;">[CLS]</span>  <span style="color:#89dceb;">이   영화</span>
       <span style="color:#6c7086;">768차원 벡터</span>

         <span style="color:#6c7086;">↓ h₀만 사용</span>
   <span style="color:#cba6f7;">분류기 (Linear Layer)</span>
         <span style="color:#6c7086;">↓</span>
   <span style="color:#a6e3a1;">긍정(0.95) / 부정(0.05)  → 긍정 ✅</span></div>
</div>

</div>

<br>

<!-- 시각화 증거 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧪 [CLS] 벡터가 실제로 의미 있다는 증거
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 16px;">
연구자들은 학습된 BERT의 [CLS] 벡터를 2차원으로 줄여서 시각화해봤습니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-top: 16px;">

  <div style="background:#f0fdf4; border:2px solid #86efac; border-radius:14px; padding:16px 18px; text-align:center;">
    <div style="font-size:22px; margin-bottom:8px;">● ● ●</div>
    <div style="font-size:13px; font-weight:900; color:#16a34a; margin-bottom:6px;">긍정적인 문장</div>
    <div style="font-size:12px; color:#475569; line-height:1.5;">[CLS] 벡터들이<br>공간에서 <b>서로 가까이</b> 모임</div>
  </div>

  <div style="background:#fff1f2; border:2px solid #fca5a5; border-radius:14px; padding:16px 18px; text-align:center;">
    <div style="font-size:22px; margin-bottom:8px;">■ ■ ■</div>
    <div style="font-size:13px; font-weight:900; color:#dc2626; margin-bottom:6px;">부정적인 문장</div>
    <div style="font-size:12px; color:#475569; line-height:1.5;">[CLS] 벡터들이<br><b>다른 공간</b>에 모임</div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px; text-align:center;">
    <div style="font-size:22px; margin-bottom:8px;">▲ ▲ ▲</div>
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:6px;">중립적인 문장</div>
    <div style="font-size:12px; color:#475569; line-height:1.5;">[CLS] 벡터들이<br><b>또 다른 공간</b>에 모임</div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">✅</span> <b style="color:#1681c4;">의미가 비슷한 문장끼리 [CLS] 벡터도 비슷</b>해지는 것이 확인됐습니다.<br>
[CLS] 벡터가 문장 전체의 의미를 잘 요약하고 있다는 증거입니다.
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
    <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 6px; border-radius:4px;">[CLS]</code>는 BERT 입력의 <b style="color:#FF6B00;">맨 앞에 항상 붙는</b> 특수 토큰입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    처음엔 빈 슬롯이지만 12층의 Self-Attention을 거치며 <b style="color:#FF6B00;">문장 전체 의미를 흡수</b>합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    최종 출력인 <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 6px; border-radius:4px;">h₀</code> (768차원)는 <b style="color:#FF6B00;">문장 전체를 대표하는 벡터</b>로, 문장 분류 과제에 직접 사용됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    <code style="background:#fff3eb; border:1px solid #ffd0b0; color:#FF6B00; padding:1px 6px; border-radius:4px;">[CLS]</code> 덕분에 "문장 전체를 하나의 벡터로" 만드는 문제가 자연스럽게 해결됩니다.
  </div>
</div>

</div>

</div>