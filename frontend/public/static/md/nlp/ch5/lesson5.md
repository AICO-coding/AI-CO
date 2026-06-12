<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Positional Encoding — 순서를 모르면 뭐가 문제일까?
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Transformer가 단어 순서를 알 수 없는 이유와,
<b style="color:#1681c4;">Positional Encoding</b>이 왜 필요한지 알아봅니다.
</p>

</div>

<br>

<!-- 치명적인 약점 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🤔 Transformer에는 치명적인 약점이 하나 있습니다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
5-2에서 Transformer의 큰 장점을 배웠습니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 15px; font-weight: 900; line-height: 1.8; text-align: center; margin: 14px 0;">
<span style="color: #1681c4;">"문장의 모든 단어를 <b>동시에</b> 처리한다!"</span>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">⚠️ 그런데 문제가 생깁니다.</span><br>
<b style="color:#FF6B00;">"동시에 처리한다"는 말은, 단어의 순서를 무시한다는 뜻이기도 합니다.</b>
</div>

</div>

<br>

<!-- 단어 순서가 사라지면 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔀 단어 순서가 사라지면 어떤 일이 벌어질까요?
</h2>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:12px; font-weight:900; color:#94a3b8; margin-bottom:8px;">문장 A</div>
    <div style="font-family:Consolas, monospace; font-size:14px; color:#a6e3a1; background:#0f172a; padding:8px 12px; border-radius:8px;">"나는 밥을 먹었다"</div>
  </div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:14px 16px; text-align:center;">
    <div style="font-size:12px; font-weight:900; color:#94a3b8; margin-bottom:8px;">문장 B</div>
    <div style="font-family:Consolas, monospace; font-size:14px; color:#a6e3a1; background:#0f172a; padding:8px 12px; border-radius:8px;">"밥을 나는 먹었다"</div>
  </div>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
한국어에서는 뜻이 비슷하게 통하지만, <b>영어에서는 이야기가 완전히 달라집니다.</b>
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 14px;">
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px;">
    <div style="font-size:12px; font-weight:900; color:#1681c4; margin-bottom:8px;">문장 C</div>
    <div style="font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; background:#0f172a; padding:8px 12px; border-radius:8px; margin-bottom:6px;">"The dog bit the man"</div>
    <div style="font-size:13px; color:#475569; text-align:center;">개가 사람을 물었다</div>
  </div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 16px;">
    <div style="font-size:12px; font-weight:900; color:#FF6B00; margin-bottom:8px;">문장 D</div>
    <div style="font-family:Consolas, monospace; font-size:13px; color:#f38ba8; background:#0f172a; padding:8px 12px; border-radius:8px; margin-bottom:6px;">"The man bit the dog"</div>
    <div style="font-size:13px; color:#475569; text-align:center;">사람이 개를 물었다</div>
  </div>
</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 단어는 동일합니다: <code style="background:#0f172a; color:#89dceb; padding:2px 6px; border-radius:4px; font-size:12px;">The, dog, bit, the, man</code><br>
<b style="color:#FF6B00;">오직 순서만 달라졌는데, 뜻이 정반대가 됩니다.</b>
</div>

</div>

<br>

<!-- 왜 순서를 모를까 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📦 Transformer는 왜 순서를 모를까요?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Transformer의 Self-Attention은 모든 단어를 <b>한꺼번에</b> 받아서 처리합니다.<br>
이때 단어들은 <b style="color:#FF6B00;">번호 없이</b> 동시에 들어옵니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 16px 0;">
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:8px;">✅ 순서가 있는 경우</div>
    <div style="font-size:13px; color:#334155; line-height:1.8; background:#f8fafc; padding:10px 12px; border-radius:8px;">
      "1번 철수, 2번 영희, 3번 민수..."<br>
      <span style="color:#1681c4; font-weight:900;">→ 자리를 알 수 있음</span>
    </div>
  </div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 16px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:8px;">❌ 순서가 없는 경우</div>
    <div style="font-size:13px; color:#334155; line-height:1.8; background:#f8fafc; padding:10px 12px; border-radius:8px;">
      "철수, 영희, 민수가 동시에 손을 들어요"<br>
      <span style="color:#FF6B00; font-weight:900;">→ 누가 몇 번인지 알 수 없음</span>
    </div>
  </div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> Transformer의 Self-Attention은 단어들이 <b style="color:#FF6B00;">동시에 손을 드는 상황</b>입니다.<br>
이 상태로는 "나는"이 첫 번째 단어인지 세 번째 단어인지 알 수 없습니다.
</div>

</div>

<br>

<!-- 실제로 순서 정보가 없으면 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🧪 실제로 순서 정보가 없으면 무슨 일이 생기나요?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Transformer에 순서 정보를 아예 주지 않으면, 아래 두 문장을 <b style="color:#FF6B00;">완전히 동일하게</b> 처리합니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">순서 정보 없을 때</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#a6e3a1;">"나는 밥을 먹었다"</span>
<span style="color:#f38ba8;">"먹었다 밥을 나는"</span>

<span style="color:#6c7086;">→ Transformer 입장에서 두 문장은 완전히 같습니다.</span>
<span style="color:#6c7086;">  단어 집합이 동일하니까요.</span></div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">⚠️</span> 번역기가 이 두 문장을 같은 문장으로 본다면?<br>
<b style="color:#FF6B00;">엉터리 번역이 나올 수밖에 없습니다.</b>
</div>

</div>

<br>

<!-- 해결책 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📮 해결책: 각 단어에 "위치 번호표"를 붙여준다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Transformer 연구팀이 생각한 해결책은 단순하고 명쾌했습니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; color: #0f172a; font-size: 14px; font-weight: 900; line-height: 1.8; margin: 14px 0;">
<span style="color: #1681c4;">💡</span> "Self-Attention을 실행하기 <b style="color:#1681c4;">전</b>에,<br>
각 단어 벡터에 <b style="color:#1681c4;">'나는 몇 번째 단어입니다'라는 정보</b>를 추가해주자!"
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
이것이 바로 <b style="color:#1681c4;">Positional Encoding(위치 인코딩)</b>입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Positional Encoding 적용 전 / 후</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#f38ba8;">[Positional Encoding 없이]</span>
<span style="color:#a6e3a1;">"나는"</span>   → <span style="color:#89dceb;">[0.2, 0.5, 0.1, ...]</span>  <span style="color:#6c7086;">← 순수 의미 벡터</span>
<span style="color:#a6e3a1;">"밥을"</span>   → <span style="color:#89dceb;">[0.7, 0.1, 0.9, ...]</span>  <span style="color:#6c7086;">← 순수 의미 벡터</span>
<span style="color:#a6e3a1;">"먹었다"</span> → <span style="color:#89dceb;">[0.3, 0.8, 0.4, ...]</span>  <span style="color:#6c7086;">← 순수 의미 벡터</span>

<span style="color:#a6e3a1;">[Positional Encoding 추가 후]</span>
<span style="color:#a6e3a1;">"나는"</span>   → <span style="color:#cba6f7;">[0.2+위치1, 0.5+위치1, ...]</span>  <span style="color:#6c7086;">← "나는 1번째!"</span>
<span style="color:#a6e3a1;">"밥을"</span>   → <span style="color:#cba6f7;">[0.7+위치2, 0.1+위치2, ...]</span>  <span style="color:#6c7086;">← "나는 2번째!"</span>
<span style="color:#a6e3a1;">"먹었다"</span> → <span style="color:#cba6f7;">[0.3+위치3, 0.8+위치3, ...]</span>  <span style="color:#6c7086;">← "나는 3번째!"</span></div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> 단어의 의미 정보(임베딩 벡터)에 위치 정보를 <b style="color:#1681c4;">더해주는 방식</b>입니다.
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="font-size: 15px; font-weight: 900; margin-bottom: 14px;">
<span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리
</div>

<div style="overflow-x: auto; margin-bottom: 14px;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; font-weight:900;">문제</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">Positional Encoding으로 해결</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; color:#334155;">단어 순서를 모름</td>
      <td style="padding:10px 14px; color:#334155;">각 단어 벡터에 위치 정보 추가</td>
    </tr>
    <tr style="background:#fff8f4; border-bottom:1px solid #ffd0b0;">
      <td style="padding:10px 14px; color:#334155;">같은 단어도 위치에 따라 역할이 다름</td>
      <td style="padding:10px 14px; color:#334155;">위치가 다르면 벡터 값도 달라짐</td>
    </tr>
    <tr style="background:#fff;">
      <td style="padding:10px 14px; color:#334155;">"The man bit the dog"과 "The dog bit the man" 구분 불가</td>
      <td style="padding:10px 14px; color:#334155;">위치가 다르니 벡터가 달라져 구분 가능</td>
    </tr>
  </tbody>
</table>
</div>

<div style="display: grid; gap: 8px;">
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Transformer는 단어를 <b style="color:#FF6B00;">동시에</b> 처리하기 때문에, 본래 <b style="color:#FF6B00;">순서 정보가 없습니다.</b>
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    Positional Encoding은 단어 벡터에 <b style="color:#FF6B00;">"몇 번째 단어인지"를 숫자로 추가</b>하는 방법입니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이 과정은 Self-Attention <b style="color:#FF6B00;">이전, 입력 단계</b>에서 수행됩니다.
  </div>
</div>

<div style="margin-top: 12px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> 다음 페이지에서는 "그럼 위치 정보를 구체적으로 어떤 숫자로 표현하는가?"를 알아봅니다.
</div>

</div>

</div>