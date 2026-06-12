<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 06 · BERT
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
양방향 문맥 이해
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
양방향이 실제로 어떻게 작동하고, 없으면 무엇이 달라지는지 구체적으로 살펴봅니다.<br>
<b style="color:#1681c4;">단방향 모델의 한계</b>와 <b style="color:#1681c4;">BERT가 이를 극복하는 방법</b>을 비교합니다.
</p>

</div>

<br>

<!-- 왜 양방향이 중요한가 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧭 "양방향"이 왜 그렇게 중요할까요?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
다음 문장에서 <b>"부상"</b>의 의미를 파악해봅시다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 20px; border-radius: 12px; font-size: 15px; color: #0f172a; font-weight: 700; line-height: 1.9; text-align: center; margin: 14px 0;">
"그 선수는 경기 중 <span style="color:#1681c4; background:#fff; border:1px solid #c2e4ff; padding:2px 8px; border-radius:6px;">부상</span>을 입었지만, 끝까지 포기하지 않았다."
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 14px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px;">
    <div style="font-size:13px; font-weight:900; color:#64748b; margin-bottom:6px;">⬅️ 왼쪽 문맥</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">"그 선수는 경기 중"<br>→ <b>스포츠 상황</b></div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px;">
    <div style="font-size:13px; font-weight:900; color:#64748b; margin-bottom:6px;">➡️ 오른쪽 문맥</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">"입었지만, 끝까지 포기하지 않았다"<br>→ <b>부정적 사건 + 극복</b></div>
  </div>

</div>

<div style="margin-top:12px; background:#fff3eb; border:2px solid #ffd0b0; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#FF6B00; font-weight:900;">💡</span> 앞뒤를 <b style="color:#FF6B00;">모두</b> 봐야 <b style="color:#FF6B00;">"부상 = 신체 상해"</b>임을 확실히 알 수 있습니다.
</div>

</div>

<br>

<!-- 단방향 vs 양방향 비교 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
➡️ 단방향 vs. ⬅️➡️ 양방향 비교
</h2>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 14px;">

  <!-- 단방향 -->
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; overflow:hidden;">
    <div style="background:#FF6B00; padding:10px 16px;">
      <div style="font-size:13px; font-weight:900; color:#fff;">➡️ GPT — 단방향 (왼쪽→오른쪽)</div>
    </div>
    <div style="background:#1e1e2e; padding:16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.3; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">입력: 나는  오늘  ___  에서  커피를  마셨다</span>

<span style="color:#f38ba8;">"나는" 다음 단어 예측</span>
<span style="color:#f38ba8;">"나는 오늘" 다음 단어 예측</span>
<span style="color:#f38ba8;">"나는 오늘 ___" 예측할 때</span>
<span style="color:#6c7086;">→ "에서 커피를 마셨다"는 아직 모름!</span></div>
    <div style="padding:12px 14px; font-size:13px; color:#475569; line-height:1.7; background:#fff8f3;">
      텍스트 <b>생성</b>에는 자연스럽지만, <b style="color:#FF6B00;">문장 이해</b> 과제에서는 한계가 있습니다.
    </div>
  </div>

  <!-- 양방향 -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; overflow:hidden;">
    <div style="background:#1681c4; padding:10px 16px;">
      <div style="font-size:13px; font-weight:900; color:#fff;">⬅️➡️ BERT — 양방향 (전체 동시)</div>
    </div>
    <div style="background:#1e1e2e; padding:16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.3; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">문장: 나는  오늘  카페  에서  커피를  마셨다</span>

<span style="color:#a6e3a1;">"카페"가 보는 것:</span>
<span style="color:#89dceb;">← 왼쪽: "나는", "오늘"</span>
<span style="color:#89dceb;">→ 오른쪽: "에서", "커피를", "마셨다"</span>
<span style="color:#a6e3a1;">→ 전체 참조 → 의미 확신 ✅</span></div>
    <div style="padding:12px 14px; font-size:13px; color:#475569; line-height:1.7; background:#f0f7ff;">
      Self-Attention으로 <b style="color:#1681c4;">전체 문장을 동시에</b> 보기 때문에 진정한 양방향 이해가 가능합니다.
    </div>
  </div>

</div>

</div>

<br>

<!-- 단방향이면 놓치는 것들 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🚫 단방향이면 놓치는 것들
</h2>

<div style="display: grid; gap: 16px; margin-top: 16px;">

  <!-- ① 동음이의어 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:14px;">
      <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">① 동음이의어</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">같은 발음, 다른 의미</div>
    </div>
    <div style="display:grid; gap:8px;">
      <div style="display:grid; grid-template-columns:1fr 100px 100px; gap:8px; align-items:center;">
        <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.6;">
          <b style="color:#FF6B00;">"배"</b>가 고프다 → <b>복부</b>
        </div>
        <div style="background:#fff1f2; border:1px solid #fca5a5; border-radius:8px; padding:8px; text-align:center; font-size:12px; color:#dc2626; font-weight:900;">앞만 봐서<br>애매 ❌</div>
        <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:8px; padding:8px; text-align:center; font-size:12px; color:#16a34a; font-weight:900;">뒤의 "고프다"<br>보고 확신 ✅</div>
      </div>
      <div style="display:grid; grid-template-columns:1fr 100px 100px; gap:8px; align-items:center;">
        <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.6;">
          항구에 <b style="color:#FF6B00;">"배"</b>가 들어왔다 → <b>선박</b>
        </div>
        <div style="background:#fff1f2; border:1px solid #fca5a5; border-radius:8px; padding:8px; text-align:center; font-size:12px; color:#dc2626; font-weight:900;">앞만 봐서<br>애매 ❌</div>
        <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:8px; padding:8px; text-align:center; font-size:12px; color:#16a34a; font-weight:900;">뒤의 "들어왔다"<br>보고 확신 ✅</div>
      </div>
      <div style="display:grid; grid-template-columns:1fr 100px 100px; gap:8px; align-items:center;">
        <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.6;">
          <b style="color:#FF6B00;">"배"</b>나무에 배가 열렸다 → <b>과일</b>
        </div>
        <div style="background:#fff1f2; border:1px solid #fca5a5; border-radius:8px; padding:8px; text-align:center; font-size:12px; color:#dc2626; font-weight:900;">앞만 봐서<br>애매 ❌</div>
        <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:8px; padding:8px; text-align:center; font-size:12px; color:#16a34a; font-weight:900;">앞의 "배나무"<br>보고 확신 ✅</div>
      </div>
    </div>
  </div>

  <!-- ② 대명사 지칭 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">② 대명사 지칭</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">앞 문장을 참조해야 하는 경우</div>
    </div>
    <div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.9; margin-bottom:10px;">
      "철수는 민수를 도와줬다. <b style="color:#1681c4; background:#fff; border:1px solid #c2e4ff; padding:1px 6px; border-radius:5px;">그는</b> 정말 착한 사람이다."
    </div>
    <div style="font-size:13px; color:#475569; line-height:1.7;">
      <b>"그"</b>가 철수인지 민수인지 알려면 <b style="color:#1681c4;">앞 문장 전체</b>가 필요합니다.<br>
      단방향 모델은 문장이 길어질수록 이 관계를 잘 파악하지 못합니다.
    </div>
  </div>

  <!-- ③ 뒤에 오는 부정어 -->
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
      <div style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:12px; font-weight:900;">③ 뒤에 오는 부정어</div>
      <div style="font-size:14px; font-weight:900; color:#0f172a;">문장 끝에서 의미가 뒤집히는 경우</div>
    </div>
    <div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 14px; font-size:14px; color:#334155; line-height:1.9; margin-bottom:10px;">
      "나는 오늘 밥을 먹지 <b style="color:#FF6B00; background:#fff; border:1px solid #ffd0b0; padding:1px 6px; border-radius:5px;">않았다</b>."
    </div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:8px;">
      <div style="background:#fff1f2; border:1px solid #fca5a5; border-radius:10px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.7;">
        <b style="color:#dc2626;">단방향:</b> "않았다"를 보기 전까지 "밥을 먹었다"로 해석하고 나중에 수정
      </div>
      <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:10px; padding:10px 12px; font-size:13px; color:#334155; line-height:1.7;">
        <b style="color:#16a34a;">BERT:</b> 처음부터 "않았다"를 보고 전체를 동시에 해석 ✅
      </div>
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
    단방향 모델(GPT 등)은 왼쪽에서 오른쪽으로만 읽어, <b style="color:#FF6B00;">오른쪽 문맥을 활용할 수 없습니다.</b>
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    BERT는 <b style="color:#FF6B00;">Self-Attention으로 전체 문장을 동시에</b> 보기 때문에 진정한 양방향 이해가 가능합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    동음이의어, 대명사 지칭, 문장 끝의 부정어처럼 <b style="color:#FF6B00;">앞뒤 맥락이 함께 필요한 경우</b>에 특히 강력합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이 양방향성이 BERT가 문장 <b style="color:#FF6B00;">이해</b> 과제에서 탁월한 성능을 내는 핵심 이유입니다.
  </div>
</div>

</div>

</div>