<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">Chapter 07 · GPT</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">왼쪽에서 오른쪽으로, 한 방향으로만!</h1>
<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
BERT는 양방향, GPT는 단방향으로 문장을 읽습니다.<br>
이 방향의 차이가 어떻게 <b style="color:#1681c4;">자기회귀(Autoregressive) 생성</b>으로 이어지는지 알아봅니다.
</p>
</div>

<br>

<!-- 읽는 방향 차이 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">↔️ BERT vs GPT: 읽는 방향의 차이</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
앞에서 배운 BERT와 GPT는 <b>문장을 읽는 방향</b>이 다릅니다. 이 차이가 두 모델의 성격을 완전히 갈라놓습니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; overflow:hidden;">
<div style="background:#1681c4; padding:10px 16px;"><div style="font-size:13px; font-weight:900; color:#fff;">BERT (양방향)</div></div>
<div style="background:#1e1e2e; padding:16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.3; overflow-x:auto; white-space:pre; text-align:center;"><span style="color:#cdd6f4;">"나는  오늘  [?]  갔다"</span>
<span style="color:#a6e3a1;">←←←←← 양쪽 모두 참고 →→→→→</span></div>
</div>

<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; overflow:hidden;">
<div style="background:#FF6B00; padding:10px 16px;"><div style="font-size:13px; font-weight:900; color:#fff;">GPT (단방향)</div></div>
<div style="background:#1e1e2e; padding:16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:12px; line-height:2.3; overflow-x:auto; white-space:pre; text-align:center;"><span style="color:#cdd6f4;">"나는  오늘  학교에  [?]"</span>
<span style="color:#f9e2af;">→→→→→ 왼쪽만 보고 다음 예측</span></div>
</div>

</div>

</div>

<br>

<!-- 비유: 기차 vs 예언가 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🚂 비유로 이해하기: 독자 vs 작가</h2>

<div style="display: grid; gap: 14px; margin-top: 14px;">

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
<div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">📘 BERT = 완성된 문장을 보는 독자</div>
<div style="font-size:14px; color:#334155; line-height:1.8;">
글 전체를 먼저 읽고, 앞뒤 맥락을 모두 파악합니다.<br>
"이 문장에서 이 단어는 어떤 의미일까?"를 분석합니다.<br>
→ <b style="color:#1681c4;">이해에 강함</b>
</div>
</div>

<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
<div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:8px;">✍️ GPT = 소설을 쓰는 작가</div>
<div style="font-size:14px; color:#334155; line-height:1.8;">
지금까지 쓴 내용만 보고, 다음 문장을 이어 씁니다.<br>
아직 쓰지 않은 뒷부분은 볼 수 없습니다.<br>
→ <b style="color:#FF6B00;">생성에 강함</b>
</div>
</div>

</div>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px; margin-top: 14px;">
<tr>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#1681c4; white-space:nowrap; width:60px;">BERT</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">"이 리뷰가 긍정인가 부정인가?" 같은 <b>분류·이해</b> 과제에 유리</td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#FF6B00; white-space:nowrap;">GPT</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">"이 문장에 이어질 내용을 써봐" 같은 <b>생성·대화</b> 과제에 유리</td>
</tr>
</table>

</div>

<br>

<!-- 생성 기본 원리 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🔄 GPT가 문장을 생성하는 기본 원리</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT는 단어를 <b>한 번에 하나씩</b> 생성합니다. 생성한 단어를 다시 입력으로 넣어서 그 다음 단어를 생성하는 방식입니다.
</p>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px; margin-top: 14px;">
<tr>
<td style="background:#FF6B00; color:#fff; padding:5px 12px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:middle; width:80px; text-align:center;">Step 1</td>
<td style="background:#1e1e2e; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; color:#cdd6f4; vertical-align:middle;"><span style="color:#a6e3a1;">"오늘 날씨가"</span> → <span style="color:#f9e2af;">[GPT]</span> → <span style="color:#89dceb; font-weight:900;">"좋아서"</span></td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#1681c4; color:#fff; padding:5px 12px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:middle; width:80px; text-align:center;">Step 2</td>
<td style="background:#1e1e2e; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; color:#cdd6f4; vertical-align:middle;"><span style="color:#a6e3a1;">"오늘 날씨가 좋아서"</span> → <span style="color:#f9e2af;">[GPT]</span> → <span style="color:#89dceb; font-weight:900;">"기분이"</span></td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#FF6B00; color:#fff; padding:5px 12px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:middle; width:80px; text-align:center;">Step 3</td>
<td style="background:#1e1e2e; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; color:#cdd6f4; vertical-align:middle;"><span style="color:#a6e3a1;">"오늘 날씨가 좋아서 기분이"</span> → <span style="color:#f9e2af;">[GPT]</span> → <span style="color:#89dceb; font-weight:900;">"좋다"</span></td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#0f172a; color:#c3e88d; padding:5px 12px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:middle; width:80px; text-align:center;">Step 4</td>
<td style="background:#1e1e2e; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; color:#cdd6f4; vertical-align:middle;"><span style="color:#a6e3a1;">"오늘 날씨가 좋아서 기분이 좋다"</span> → <span style="color:#f9e2af;">[GPT]</span> → <span style="color:#f38ba8; font-weight:900;">[종료 신호]</span></td>
</tr>
</table>

<div style="margin-top: 14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">🔁</span> 이렇게 <b style="color:#1681c4;">연쇄적으로 단어를 이어붙여</b> 완성된 문장을 만들어냅니다. 이 과정을 <b style="color:#1681c4;">자기회귀(Autoregressive) 생성</b>이라고 합니다.
</div>

</div>

<br>

<!-- 온도 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🌡️ 생성의 다양성: 온도(Temperature)</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT는 다음 단어를 선택할 때 항상 같은 단어만 고르지 않습니다. <b>확률</b>에 따라 선택하며, 이 무작위성의 정도를 <b style="color:#1681c4;">온도(Temperature)</b>로 조절합니다.
</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 18px;">
<div style="font-size:13px; font-weight:900; color:#64748b; margin-bottom:8px;">🧊 온도 낮음 (0에 가까움)</div>
<div style="font-size:13px; color:#334155; line-height:1.7;">가장 확률 높은 단어만 선택<br>→ <b>안전하고 반복적인</b> 문장</div>
</div>

<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
<div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:8px;">🔥 온도 높음 (1 이상)</div>
<div style="font-size:13px; color:#334155; line-height:1.7;">확률 낮은 단어도 선택<br>→ <b style="color:#FF6B00;">창의적이지만 엉뚱할 수 있음</b></div>
</div>

</div>

<div style="background-color: #1e1e2e; border-radius: 14px; padding: 16px 20px; font-family:'JetBrains Mono','Consolas',monospace; font-size: 13px; line-height: 2.2; margin-top: 14px; overflow-x:auto; white-space:pre;"><span style="color:#6c7086;">예시: "오늘 날씨가 ___"</span>

<span style="color:#89dceb;">온도 낮음</span> <span style="color:#6c7086;">→</span> <span style="color:#a6e3a1;">항상 "좋다"</span>
<span style="color:#f9e2af;">온도 높음</span> <span style="color:#6c7086;">→</span> <span style="color:#f38ba8;">"좋다", "흐리다", "묘하다", "춤추는 것 같다" 등 다양하게</span></div>

</div>

<br>

<!-- 핵심 아이디어 정리 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🔑 두 가지 핵심 아이디어 정리</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">GPT의 핵심은 딱 두 가지입니다.</p>

<table style="width:100%; border-collapse: separate; border-spacing: 0 10px; margin-top: 14px;">
<tr>
<td style="background:#FF6B00; color:#fff; width:36px; height:36px; border-radius:50%; font-size:15px; font-weight:900; text-align:center; vertical-align:middle;">①</td>
<td style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:14px 18px; vertical-align:middle;">
<div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:4px;">다음 단어 예측으로 학습</div>
<div style="font-size:13px; color:#475569; line-height:1.6;">별도 정답 없이 텍스트만으로 학습 가능</div>
</td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#1681c4; color:#fff; width:36px; height:36px; border-radius:50%; font-size:15px; font-weight:900; text-align:center; vertical-align:middle;">②</td>
<td style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px; vertical-align:middle;">
<div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:4px;">왼쪽에서 오른쪽으로 단방향 생성</div>
<div style="font-size:13px; color:#475569; line-height:1.6;">이미 만든 내용을 바탕으로 다음 내용을 이어감</div>
</td>
</tr>
</table>

<div style="margin-top: 14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align:center;">
이 두 가지가 GPT를 <b style="color:#1681c4;">"생성형 AI"</b>로 만드는 핵심 원리입니다.
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;"><span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리</div>
<div style="display: grid; gap: 8px;">
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">GPT는 <b style="color:#FF6B00;">단방향(왼→오)</b> 구조: 과거 내용만 보고 다음 단어를 생성합니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">단어를 <b style="color:#FF6B00;">한 번에 하나씩</b> 연쇄적으로 생성하는 자기회귀 방식입니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">BERT(이해 특화) vs GPT(생성 특화): <b style="color:#FF6B00;">읽는 방향의 차이</b>에서 비롯됩니다.</div>
</div>
</div>

</div>