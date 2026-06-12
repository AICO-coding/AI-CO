<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
단어 빈도 기반 표현
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
단어 빈도 기반 표현은
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">어떤 단어가 얼마나 자주 나오는지</span>
를 숫자로 표현하는 방법입니다.
</p>

</div>

<br>

<!-- 원-핫 한계에서 출발 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🤔 원-핫 인코딩의 한계에서 출발하기
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
앞서 배운 원-핫 인코딩은 단어를 0과 1만으로 표현했습니다.<br>
그런데 이 방법에는 큰 문제가 하나 있었습니다.
</p>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 15px 17px; border-radius: 12px; font-size: 14px; line-height: 1.8; color: #334155; margin: 14px 0;">
  <div style="margin-bottom: 8px;">
    <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:3px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px;">"나는 오늘 행복하다"</span>
    와
    <span style="display:inline-block; background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:3px 9px; border-radius:7px; font-family:Consolas, monospace; font-size:13px;">"나는 오늘 슬프다"</span>
  </div>
  두 문장에서 <b style="color:#1681c4;">"나는"</b>, <b style="color:#1681c4;">"오늘"</b>은 같고, <b style="color:#FF6B00;">"행복하다"</b>와 <b style="color:#FF6B00;">"슬프다"</b>만 다릅니다.<br>
  하지만 원-핫 인코딩으로는 두 문장이 얼마나 비슷한지 <b style="color:#FF6B00;">전혀 알 수 없습니다.</b>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 0;">
그래서 등장한 것이 <b>단어 빈도 기반 표현</b>입니다.
</p>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡 핵심 아이디어</span><br>
<b>"어떤 단어가 얼마나 자주 나오는지"를 숫자로 표현하자!</b>
</div>

</div>

<br>

<!-- 뉴스 기사 비유 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📰 비유로 이해하기: 뉴스 기사 분류
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
어떤 뉴스 기사가 <b style="color:#1681c4;">스포츠</b> 기사인지, <b style="color:#FF6B00;">경제</b> 기사인지 구분하려면 어떻게 할까요?
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">🏆 스포츠 기사</div>
    <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-size:13px; color:#cdd6f4; line-height:1.8; margin-bottom:12px; font-family:Consolas, monospace;">
      "오늘 경기에서 선수가 골을 넣었다.<br>
      팀이 승리했다. 다음 경기는..."
    </div>
    <div style="display:flex; gap:6px; flex-wrap:wrap;">
      <span style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:3px 8px; border-radius:6px; font-size:12px; font-weight:900;">경기</span>
      <span style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:3px 8px; border-radius:6px; font-size:12px; font-weight:900;">선수</span>
      <span style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:3px 8px; border-radius:6px; font-size:12px; font-weight:900;">골</span>
      <span style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:3px 8px; border-radius:6px; font-size:12px; font-weight:900;">팀</span>
      <span style="background:#fff; border:1px solid #c2e4ff; color:#1681c4; padding:3px 8px; border-radius:6px; font-size:12px; font-weight:900;">승리</span>
      <span style="font-size:12px; color:#94a3b8; align-self:center;">자주 등장 ↑</span>
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:10px;">📈 경제 기사</div>
    <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-size:13px; color:#cdd6f4; line-height:1.8; margin-bottom:12px; font-family:Consolas, monospace;">
      "주가가 급등했다. 금리 인상으로<br>
      시장이 흔들렸다. 투자자들이..."
    </div>
    <div style="display:flex; gap:6px; flex-wrap:wrap;">
      <span style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:3px 8px; border-radius:6px; font-size:12px; font-weight:900;">주가</span>
      <span style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:3px 8px; border-radius:6px; font-size:12px; font-weight:900;">금리</span>
      <span style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:3px 8px; border-radius:6px; font-size:12px; font-weight:900;">시장</span>
      <span style="background:#fff; border:1px solid #ffd0b0; color:#FF6B00; padding:3px 8px; border-radius:6px; font-size:12px; font-weight:900;">투자</span>
      <span style="font-size:12px; color:#94a3b8; align-self:center;">자주 등장 ↑</span>
    </div>
  </div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡 핵심</span><br>
<b>자주 등장하는 단어</b>를 보면 그 문서의 주제를 파악할 수 있습니다.<br>
이것이 단어 빈도 기반 표현의 핵심입니다.
</div>

</div>

</div>