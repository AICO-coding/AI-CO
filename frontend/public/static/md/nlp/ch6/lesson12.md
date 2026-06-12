<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
MLM이 BERT에게 가르치는 것
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
단순해 보이는 "빈칸 채우기"를 수십억 번 반복하면 무엇을 배울 수 있을까요?<br>
MLM이 BERT에게 가르치는 <b style="color:#1681c4;">네 가지 언어 지식</b>을 알아봅니다.
</p>

</div>

<br>

<!-- 4가지 학습 내용 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧠 MLM을 수십억 번 반복하면 무엇을 배울까요?
</h2>

<div style="display: grid; gap: 16px; margin-top: 16px;">

  <!-- ① 단어의 의미 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">① 단어의 의미</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">의미적으로 가까운 단어들을 파악</div>
    </div>
    <div style="background:#1e1e2e; border-radius:10px; padding:14px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.3; overflow-x:auto; white-space:pre; margin-bottom:10px;">
<span style="color:#a6e3a1;">"그는 ____을 피아노로 연주했다"</span>
<span style="color:#6c7086;">→ [MASK] = </span><span style="color:#f9e2af;">"곡", "음악", "소나타"</span> <span style="color:#6c7086;">...</span>

<span style="color:#a6e3a1;">"그는 ____을 주방에서 요리했다"</span>
<span style="color:#6c7086;">→ [MASK] = </span><span style="color:#f9e2af;">"음식", "요리", "파스타"</span> <span style="color:#6c7086;">...</span></div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:8px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.7;">
      <span style="color:#FF6B00; font-weight:900;">💡</span> 비슷한 문맥에 어울리는 단어들을 반복 학습하면서 <b style="color:#FF6B00;">"피아노 ↔ 연주 ↔ 음악"</b>이 의미적으로 가깝다는 것을 파악합니다.
    </div>
  </div>

  <!-- ② 문법 구조 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">② 문법 구조</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">문법적으로 올바른 품사 선택</div>
    </div>
    <div style="background:#1e1e2e; border-radius:10px; padding:14px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.3; overflow-x:auto; white-space:pre; margin-bottom:10px;">
<span style="color:#a6e3a1;">"그 ____가 빠르게 달렸다"</span>
<span style="color:#6c7086;">→ [MASK] = </span><span style="color:#89dceb;">"강아지", "자동차", "말"</span> <span style="color:#6c7086;">... (명사만 가능)</span>

<span style="color:#a6e3a1;">"그 강아지가 ____게 달렸다"</span>
<span style="color:#6c7086;">→ [MASK] = </span><span style="color:#89dceb;">"빠르", "느리", "힘차"</span> <span style="color:#6c7086;">... (부사 어근만 가능)</span></div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.7;">
      <span style="color:#1681c4; font-weight:900;">💡</span> 빈칸을 채우려면 <b style="color:#1681c4;">문법적으로 올바른 품사</b>의 단어를 골라야 합니다. BERT는 이 과정에서 문법 규칙을 자연스럽게 내재화합니다.
    </div>
  </div>

  <!-- ③ 동음이의어 구별 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">③ 동음이의어 구별</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">문맥에 따른 단어 의미 변화</div>
    </div>
    <div style="background:#1e1e2e; border-radius:10px; padding:14px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.3; overflow-x:auto; white-space:pre; margin-bottom:10px;">
<span style="color:#a6e3a1;">"그는 은행에서 ____을 찾았다"</span>
<span style="color:#6c7086;">→ [MASK] = </span><span style="color:#f9e2af;">"돈", "통장", "현금"</span>  <span style="color:#6c7086;">(금융 맥락)</span>

<span style="color:#a6e3a1;">"그는 강가의 ____에서 낚시를 했다"</span>
<span style="color:#6c7086;">→ [MASK] = </span><span style="color:#f9e2af;">"바위", "자리", "모래"</span>  <span style="color:#6c7086;">(자연 맥락)</span></div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:8px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.7;">
      <span style="color:#FF6B00; font-weight:900;">💡</span> "은행"이 금융 기관인지, 강가의 언덕인지는 앞뒤 문맥이 결정합니다. BERT는 <b style="color:#FF6B00;">동음이의어를 문맥으로 구별하는 능력</b>을 키웁니다.
    </div>
  </div>

  <!-- ④ 세상 지식 -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">④ 세상에 대한 사실적 지식</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">역사, 과학, 문화까지 흡수</div>
    </div>
    <div style="background:#1e1e2e; border-radius:10px; padding:14px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.3; overflow-x:auto; white-space:pre; margin-bottom:10px;">
<span style="color:#a6e3a1;">"대한민국의 수도는 ____이다"</span>
<span style="color:#6c7086;">→ [MASK] = </span><span style="color:#89dceb; font-weight:900;">"서울"</span>

<span style="color:#a6e3a1;">"물은 100도에서 ____한다"</span>
<span style="color:#6c7086;">→ [MASK] = </span><span style="color:#89dceb; font-weight:900;">"끓"</span>

<span style="color:#a6e3a1;">"셰익스피어는 ____를 쓴 작가이다"</span>
<span style="color:#6c7086;">→ [MASK] = </span><span style="color:#89dceb; font-weight:900;">"햄릿"</span></div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.7;">
      <span style="color:#1681c4; font-weight:900;">💡</span> 위키피디아와 책으로 학습하면서 단순한 언어 규칙을 넘어 <b style="color:#1681c4;">역사, 과학, 문화 등의 사실적 지식</b>까지 흡수합니다.
    </div>
  </div>

</div>

</div>

<br>

<!-- MLM + NSP 동시 진행 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔗 MLM + NSP: 두 학습이 함께 일어납니다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BERT의 사전학습은 <b>MLM과 NSP(Next Sentence Prediction)가 동시에</b> 진행됩니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">사전학습 입력 예시</span>
  </div>
  <div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;">
<span style="color:#a6e3a1;">[CLS] 강아지는 공원에서 [MASK]했다 [SEP] 지치고 배가 [MASK]는지 밥을 먹었다 [SEP]</span>

<span style="color:#6c7086;">두 가지 학습이 동시 진행:</span>
<span style="color:#89dceb;">① MLM:</span>  <span style="color:#cdd6f4;">[MASK] 자리 단어 맞히기 →</span> <span style="color:#a6e3a1; font-weight:900;">"뛰어놀", "고프"</span>
<span style="color:#cba6f7;">② NSP:</span>  <span style="color:#cdd6f4;">두 문장이 이어지는가?   →</span> <span style="color:#a6e3a1; font-weight:900;">IsNext ✅</span>

<span style="color:#6c7086;">→ 하나의 입력으로 두 가지 언어 능력을 동시에 학습</span></div>
</div>

</div>

<br>

<!-- MLM의 한계와 발전 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🎓 MLM의 한계와 이후 발전
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
MLM이 강력하지만 완벽하지는 않습니다. 이 한계를 개선하기 위해 다양한 후속 모델들이 등장했습니다.
</p>

<div style="display: grid; gap: 10px; margin-top: 16px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:14px 18px; display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; align-items:start;">
    <div>
      <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">[MASK] 불일치</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">사전학습엔 [MASK] 있지만 실제 사용엔 없음</div>
    </div>
    <div style="border-left:2px solid #ffd0b0; padding-left:12px;">
      <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">결과</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">사전학습·미세조정 간 환경 차이 발생</div>
    </div>
    <div style="border-left:2px solid #ffd0b0; padding-left:12px;">
      <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:4px;">후속 해결</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">80/10/10 규칙 완화, <b>ELECTRA</b>는 다른 방식으로 해결</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; align-items:start;">
    <div>
      <div style="font-size:12px; font-weight:900; color:#64748b; margin-bottom:4px;">독립 예측 가정</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">여러 [MASK]를 각각 독립적으로 예측</div>
    </div>
    <div style="border-left:2px solid #e2e8f0; padding-left:12px;">
      <div style="font-size:12px; font-weight:900; color:#64748b; margin-bottom:4px;">결과</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">예측 간 상호작용 부재</div>
    </div>
    <div style="border-left:2px solid #e2e8f0; padding-left:12px;">
      <div style="font-size:12px; font-weight:900; color:#64748b; margin-bottom:4px;">후속 해결</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;"><b>XLNet</b>은 순서 정보 활용해 개선</div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; align-items:start;">
    <div>
      <div style="font-size:12px; font-weight:900; color:#64748b; margin-bottom:4px;">느린 수렴</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">전체의 15%만 학습에 활용</div>
    </div>
    <div style="border-left:2px solid #e2e8f0; padding-left:12px;">
      <div style="font-size:12px; font-weight:900; color:#64748b; margin-bottom:4px;">결과</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;">학습 효율이 낮음</div>
    </div>
    <div style="border-left:2px solid #e2e8f0; padding-left:12px;">
      <div style="font-size:12px; font-weight:900; color:#64748b; margin-bottom:4px;">후속 해결</div>
      <div style="font-size:13px; color:#334155; line-height:1.6;"><b>ELECTRA</b>는 100% 토큰 활용</div>
    </div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡</span> 이런 한계를 개선하기 위해 <b style="color:#1681c4;">RoBERTa, ALBERT, ELECTRA</b> 등 다양한 BERT 후속 모델들이 등장했습니다.
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
    MLM의 빈칸 채우기를 반복하면서 BERT는 <b style="color:#FF6B00;">단어 의미, 문법, 동음이의어 구별, 세상 지식</b>까지 자연스럽게 학습합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이 모든 지식은 <b style="color:#FF6B00;">별도의 레이블 없이</b> 텍스트 자체에서 학습됩니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    사전학습은 <b style="color:#FF6B00;">MLM과 NSP를 동시에</b> 진행하며, 하나의 입력으로 두 가지 능력을 함께 키웁니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    MLM의 한계를 개선하려는 시도에서 <b style="color:#FF6B00;">RoBERTa, ELECTRA 등 다양한 후속 모델들</b>이 탄생했습니다.
  </div>
</div>

</div>

</div>