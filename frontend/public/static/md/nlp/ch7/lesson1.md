<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">Chapter 07 · GPT</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">GPT가 등장한 이유</h1>
<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
BERT는 문장을 <b style="color:#1681c4;">이해</b>하는 데는 강력했지만, <b style="color:#FF6B00;">생성</b>은 잘하지 못했습니다.<br>
이 한계가 어떻게 GPT의 탄생으로 이어졌는지 알아봅니다.
</p>
</div>

<br>

<!-- GPT 이전엔 어떻게 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🤔 GPT 이전에는 어떻게 했을까?</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT가 등장하기 전, NLP 분야에는 이미 강력한 모델이 있었습니다. 바로 앞 챕터에서 배운 <b style="color:#1681c4;">BERT</b>입니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">✅</span> BERT는 문장을 <b style="color:#1681c4;">양방향</b>으로 읽으며 문맥을 이해하는 데 뛰어났습니다. 하지만 한 가지 큰 약점이 있었습니다.
</div>

</div>

<br>

<!-- BERT의 약점 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">❌ BERT의 약점: "생성"을 잘 못 한다</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
BERT는 주어진 문장을 <b>이해하고 분류</b>하는 데는 강했지만, <b style="color:#FF6B00;">새로운 문장을 스스로 만들어내는 것</b>은 잘 하지 못했습니다.
</p>

<!-- 비유 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px; margin: 14px 0;">
<div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:10px;">📖 비유로 이해하기</div>
<div style="font-size:14px; color:#334155; line-height:1.8;">
BERT는 마치 <b style="color:#1681c4;">독해 전문 학생</b>과 같습니다.<br>
시험 문제를 읽고 답을 찾는 건 잘 하지만, <b style="color:#FF6B00;">"자유롭게 글을 써봐"</b>라고 하면 막막해집니다.
</div>
</div>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px; margin-top: 14px;">
<tr>
<td style="background:#f8fafc; font-size:12px; font-weight:900; color:#94a3b8; padding:0 8px;"></td>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#1681c4; text-align:center;">✅ 할 수 있는 것 (BERT)</td>
<td style="background:#fff1f2; border:1px solid #fca5a5; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#dc2626; text-align:center;">❌ 못 하는 것 (BERT)</td>
</tr>
<tr><td style="height:4px;"></td><td></td><td></td></tr>
<tr>
<td style="width:0;"></td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155;">문장 분류 (스팸 메일 감지)</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155;">새로운 문장 생성</td>
</tr>
<tr><td style="height:4px;"></td><td></td><td></td></tr>
<tr>
<td style="width:0;"></td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155;">감성 분석 (긍정/부정 판단)</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155;">이야기 이어쓰기</td>
</tr>
<tr><td style="height:4px;"></td><td></td><td></td></tr>
<tr>
<td style="width:0;"></td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155;">질문에 대한 답 위치 찾기</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155;">자연스러운 대화 응답</td>
</tr>
</table>

</div>

<br>

<!-- 대화에 필요한 것 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">💬 AI가 '대화'를 하려면 무엇이 필요할까?</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
챗봇이나 AI 어시스턴트처럼 <b>대화를 주고받는 AI</b>를 만들려면, 단순히 이해하는 것을 넘어 <b style="color:#FF6B00;">자연스럽게 문장을 생성</b>할 수 있어야 합니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">대화 예시</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#89dceb;">사용자:</span> <span style="color:#cdd6f4;">"오늘 날씨가 좋네요."</span>
<span style="color:#f9e2af;">AI:</span>     <span style="color:#6c7086;">(적절한 응답을 직접 생성해야 함)</span></div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> BERT는 이 응답을 <b style="color:#FF6B00;">스스로 만들어낼 수 없었습니다</b>. 정해진 선택지 중에 고르거나, 기존 텍스트에서 구간을 찾아오는 방식이었습니다.
</div>

</div>

<br>

<!-- 정리: 왜 필요했나 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🔍 정리: 왜 새로운 모델이 필요했나?</h2>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 16px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">GPT 탄생 배경</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#a6e3a1;">BERT 등 기존 모델</span>
         <span style="color:#6c7086;">↓</span>
<span style="color:#f9e2af;">"이해"에는 강하지만 "생성"에는 약함</span>
         <span style="color:#6c7086;">↓</span>
<span style="color:#f38ba8;">자연스러운 대화, 글 생성, 창작 → 불가능</span>
         <span style="color:#6c7086;">↓</span>
<span style="color:#89dceb; font-weight:900;">새로운 접근 방식이 필요!</span></div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center;">
바로 이 필요성에서 <b>GPT(Generative Pre-trained Transformer)</b>가 탄생했습니다.<br>
이름 그대로 <b>"생성(Generative)"</b>이 핵심입니다.
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;"><span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리</div>
<div style="display: grid; gap: 8px;">
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">기존 모델(BERT)은 <b style="color:#FF6B00;">이해</b>에 특화 → <b style="color:#FF6B00;">생성</b>에는 약점이 있었습니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">AI가 자연스러운 대화를 하려면 <b style="color:#FF6B00;">문장을 직접 만드는 능력</b>이 필요합니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">GPT는 이 <b style="color:#FF6B00;">"생성" 문제를 해결</b>하기 위해 등장한 모델입니다.</div>
</div>
</div>

</div>