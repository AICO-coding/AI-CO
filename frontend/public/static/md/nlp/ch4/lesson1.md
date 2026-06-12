<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
  Chapter 04 · Attention
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Attention이 필요한 이유
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Attention 이전의 모델은 문장을 
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">끝에서 끝까지 순서대로</span>
읽어야 했습니다.<br>
긴 문장에서는 앞에서 읽은 내용을 잊어버리는 문제가 생겼고, 이를 해결하기 위해 Attention이 등장했습니다.
</p>

</div>

<br>

<!-- 기존 모델의 한계 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📬 편지를 한 글자씩 읽는 비서 — RNN의 한계
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Attention이 등장하기 전, NLP에서는 주로 <b style="color:#1681c4;">RNN(순환 신경망)</b>을 사용했습니다.<br>
RNN은 문장을 왼쪽부터 오른쪽으로 <b>한 단어씩</b> 읽으면서 이전 내용을 기억하는 구조입니다.
</p>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 15px 17px; border-radius: 12px; font-size: 14px; line-height: 1.8; color: #334155; margin: 14px 0;">
  마치 편지를 한 글자씩 읽으면서 메모지에 내용을 적는 비서와 같습니다.<br>
  메모지가 한 장이라 앞에서 읽은 내용을 계속 덮어쓰다 보면, <b style="color:#FF6B00;">처음 내용은 흐릿하게 기억</b>될 수밖에 없습니다.
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 18px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:8px;">RNN의 작동 방식</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      단어를 <b>순서대로</b> 하나씩 읽습니다.<br>
      이전 단어의 정보를 <b>hidden state</b>에 담아 다음 단어로 전달합니다.
    </div>
  </div>

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:8px;">RNN의 한계</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      문장이 길어질수록 <b>앞부분의 정보가 희미</b>해집니다.<br>
      이를 <b>장기 의존성(Long-term Dependency)</b> 문제라고 부릅니다.
    </div>
  </div>

</div>

</div>

<br>

<!-- 장기 의존성 문제 시각화 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
멀리 떨어진 단어를 기억하지 못한다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
아래 문장을 번역할 때, <b style="color:#FF6B00;">"그"</b>가 누구를 가리키는지 이해하려면 문장 맨 앞의 <b style="color:#1681c4;">"철수"</b>를 기억해야 합니다.
</p>

<!-- 문장 예시 -->
<div style="background:#0f172a; color:#c3e88d; border-radius:14px; padding:16px 20px; font-size:14px; font-family: 'JetBrains Mono', Consolas, monospace; line-height:2; margin: 16px 0;">
  <span style="color:#89dceb; font-weight:900;">철수</span>는 오늘 아침 일찍 일어나서 밥을 먹고, 학교에 가는 버스를 탔는데,
  버스 안에서 친구를 만나 한참 이야기를 나눴고, 학교에 도착한 뒤에도
  <span style="color:#f38ba8; font-weight:900;">그</span>는 계속 그 친구와 이야기를 이어갔다.
</div>

<div style="display: grid; gap: 12px; margin-top: 16px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:14px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:6px;">❌ RNN의 상황</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      <b style="color:#89dceb;">"철수"</b>가 문장 앞에 있고, <b style="color:#f38ba8;">"그"</b>는 훨씬 뒤에 있습니다.<br>
      RNN은 단어를 순서대로 처리하면서 hidden state를 계속 덮어쓰기 때문에,<br>
      <b style="color:#FF6B00;">"그"를 처리할 시점에는 "철수"의 정보가 거의 사라져 있습니다.</b>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:6px;">✅ Attention의 해결 방법</div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      Attention은 <b>"그"를 처리할 때 문장 전체를 다시 훑어보면서</b><br>
      <b style="color:#1681c4;">"철수"와 가장 관련 있는 단어에 집중</b>합니다.<br>
      순서에 제약 없이, 필요한 단어를 언제든 직접 참조할 수 있습니다.
    </div>
  </div>

</div>
</div>

<br>

<!-- 핵심 비교 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
RNN vs Attention — 무엇이 다를까?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
두 방식의 핵심 차이는 <b style="color:#FF6B00;">"언제, 어떤 단어를 참조하느냐"</b>에 있습니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 18px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
      <span style="background:#e2e8f0; color:#475569; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">RNN</span>
      <span style="font-size:15px; font-weight:900; color:#0f172a;">순서대로 읽기, 앞은 잊혀짐</span>
    </div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      단어 A → B → C → D 순서로 처리하고, 각 단계에서 이전 정보를 압축해 전달합니다.<br>
      문장이 길어질수록 초반 단어의 정보는 점점 희석됩니다.
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
      <span style="background:#c2e4ff; color:#1681c4; padding:3px 10px; border-radius:999px; font-size:12px; font-weight:900;">Attention</span>
      <span style="font-size:15px; font-weight:900; color:#0f172a;">전체를 보고 관련 단어에 집중</span>
    </div>
    <div style="font-size:14px; color:#334155; line-height:1.7;">
      어떤 단어를 처리할 때, 문장 전체의 모든 단어를 동시에 참조합니다.<br>
      관련성이 높은 단어에는 <b style="color:#1681c4;">높은 가중치</b>를, 관련 없는 단어에는 낮은 가중치를 부여합니다.
    </div>
  </div>

</div>

<!-- 핵심 정리 표 -->
<div style="margin-top: 18px; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0; border: 2px solid #e2e8f0; border-radius: 14px; overflow: hidden;">
  <div style="background:#0f172a; color:#c3e88d; padding:12px 14px; font-size:13px; font-weight:900; text-align:center;">구분</div>
  <div style="background:#0f172a; color:#c3e88d; padding:12px 14px; font-size:13px; font-weight:900; text-align:center; border-left:1px solid #1a1a2e;">RNN</div>
  <div style="background:#0f172a; color:#c3e88d; padding:12px 14px; font-size:13px; font-weight:900; text-align:center; border-left:1px solid #1a1a2e;">Attention</div>

  <div style="background:#f8fafc; padding:12px 14px; font-size:13px; font-weight:700; color:#475569; border-top:1px solid #e2e8f0;">정보 참조 방식</div>
  <div style="background:#f8fafc; padding:12px 14px; font-size:13px; color:#334155; border-top:1px solid #e2e8f0; border-left:1px solid #e2e8f0;">순차적 (앞→뒤)</div>
  <div style="background:#f8fafc; padding:12px 14px; font-size:13px; color:#1681c4; font-weight:700; border-top:1px solid #e2e8f0; border-left:1px solid #e2e8f0;">전체 동시 참조</div>

  <div style="background:#fff; padding:12px 14px; font-size:13px; font-weight:700; color:#475569; border-top:1px solid #e2e8f0;">긴 문장 처리</div>
  <div style="background:#fff; padding:12px 14px; font-size:13px; color:#FF6B00; font-weight:700; border-top:1px solid #e2e8f0; border-left:1px solid #e2e8f0;">성능 저하</div>
  <div style="background:#fff; padding:12px 14px; font-size:13px; color:#1681c4; font-weight:700; border-top:1px solid #e2e8f0; border-left:1px solid #e2e8f0;">안정적</div>

  <div style="background:#f8fafc; padding:12px 14px; font-size:13px; font-weight:700; color:#475569; border-top:1px solid #e2e8f0;">병렬 처리</div>
  <div style="background:#f8fafc; padding:12px 14px; font-size:13px; color:#FF6B00; font-weight:700; border-top:1px solid #e2e8f0; border-left:1px solid #e2e8f0;">불가능</div>
  <div style="background:#f8fafc; padding:12px 14px; font-size:13px; color:#1681c4; font-weight:700; border-top:1px solid #e2e8f0; border-left:1px solid #e2e8f0;">가능</div>
</div>

</div>

<br>

<!-- Attention이 해결한 것 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
Attention이 해결한 3가지 문제
</h2>

<div style="display: grid; gap: 14px; margin-top: 16px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:10px; min-width:40px; height:40px; display:flex; align-items:center; justify-content:center; font-size:18px; font-weight:900; color:#1681c4;">1</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#0f172a; margin-bottom:4px;">장기 의존성 문제</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">
        문장이 아무리 길어도, 처음 단어와 끝 단어가 직접 연결될 수 있습니다.<br>
        거리에 상관없이 관련 있는 단어끼리 연결됩니다.
      </div>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:10px; min-width:40px; height:40px; display:flex; align-items:center; justify-content:center; font-size:18px; font-weight:900; color:#FF6B00;">2</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#0f172a; margin-bottom:4px;">정보 병목 문제</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">
        RNN은 긴 문장의 모든 정보를 하나의 hidden state에 압축해야 했습니다.<br>
        Attention은 문장 전체를 직접 참조하므로 정보 손실이 없습니다.
      </div>
    </div>
  </div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px; display:flex; gap:14px; align-items:flex-start;">
    <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:10px; min-width:40px; height:40px; display:flex; align-items:center; justify-content:center; font-size:18px; font-weight:900; color:#1681c4;">3</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#0f172a; margin-bottom:4px;">해석 가능성 문제</div>
      <div style="font-size:14px; color:#334155; line-height:1.7;">
        Attention은 각 단어가 어떤 단어에 얼마나 집중했는지 <b style="color:#1681c4;">가중치 수치로 확인</b>할 수 있습니다.<br>
        모델이 왜 그런 결과를 냈는지 설명할 수 있게 됩니다.
      </div>
    </div>
  </div>

</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; font-weight: 900; font-size: 15px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<span style="color: #FF6B00; font-size: 18px;">⚡</span>
Attention은 "지금 이 단어를 이해하려면 문장의 어느 부분을 봐야 할까?"를 스스로 판단합니다.<br>
<span style="font-weight:400; font-size:14px; color:#475569;">RNN처럼 순서에 묶이지 않고, 필요한 단어를 언제든 직접 참조하는 것이 Attention의 핵심입니다.</span>
</div>

</div>