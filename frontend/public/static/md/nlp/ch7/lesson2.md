<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">Chapter 07 · GPT</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">"사전 학습"이라는 혁명적 아이디어</h1>
<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
2018년 OpenAI가 던진 질문 하나가 NLP의 판도를 바꿨습니다.<br>
<b style="color:#1681c4;">사전 학습(Pre-training)</b> 패러다임과 GPT라는 이름의 의미를 알아봅니다.
</p>
</div>

<br>

<!-- 2018년 아이디어 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">📚 2018년, NLP의 판도를 바꾼 아이디어</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
2018년 OpenAI는 GPT-1을 발표하면서 중요한 질문을 던졌습니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center; line-height: 1.9; margin: 14px 0;">
"매번 새 과제마다 처음부터 학습시킬 필요가 있을까?<br>
미리 언어 자체를 충분히 학습해두면 안 될까?"
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 이 아이디어가 바로 <b style="color:#FF6B00;">사전 학습(Pre-training)</b> 패러다임입니다.
</div>

</div>

<br>

<!-- 시험 준비 전략 비유 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🏫 비유로 이해하기: 시험 준비 전략</h2>

<div style="display: grid; gap: 14px; margin-top: 14px;">

<!-- 전통적 방식 -->
<div style="background:#fff1f2; border:2px solid #fca5a5; border-radius:14px; overflow:hidden;">
<div style="background:#dc2626; padding:10px 16px;"><div style="font-size:13px; font-weight:900; color:#fff;">❌ 전통적인 방식 (기존 NLP 모델)</div></div>
<div style="padding:14px 16px;">
<div style="background:#1e1e2e; border-radius:10px; padding:12px 16px; font-family:'JetBrains Mono','Consolas',monospace; font-size:13px; line-height:2.2; overflow-x:auto; white-space:pre; margin-bottom:10px;"><span style="color:#a6e3a1;">감성 분석 시험</span> <span style="color:#6c7086;">→</span> <span style="color:#a6e3a1;">감성 분석만 공부</span>
<span style="color:#89dceb;">번역 시험</span>     <span style="color:#6c7086;">→</span> <span style="color:#89dceb;">번역만 공부</span>
<span style="color:#f9e2af;">요약 시험</span>     <span style="color:#6c7086;">→</span> <span style="color:#f9e2af;">요약만 공부</span></div>
<div style="font-size:13px; color:#dc2626; font-weight:900;">매번 처음부터 공부해야 함. 비효율적!</div>
</div>
</div>

<!-- GPT 방식 -->
<div style="background:#f0fdf4; border:2px solid #86efac; border-radius:14px; overflow:hidden;">
<div style="background:#16a34a; padding:10px 16px;"><div style="font-size:13px; font-weight:900; color:#fff;">✅ GPT의 방식 (사전 학습 + 미세 조정)</div></div>
<div style="padding:14px 16px;">

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px;">
<tr>
<td style="background:#FF6B00; color:#fff; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:top; width:70px; text-align:center;">Step 1</td>
<td style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:9px 14px; font-size:13px; color:#334155; line-height:1.7;">먼저 <b>엄청나게 많은 책과 글을 읽어 언어 자체를 익힘</b></td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#1681c4; color:#fff; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:top; width:70px; text-align:center;">Step 2</td>
<td style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:9px 14px; font-size:13px; color:#334155; line-height:1.7;">특정 시험에 맞게 <b>짧게 추가 공부(미세 조정)</b></td>
</tr>
</table>

<div style="margin-top:4px; font-size:13px; color:#16a34a; font-weight:900;">기초가 탄탄하니 어떤 시험도 쉽게 적응!</div>
</div>
</div>

</div>

</div>

<br>

<!-- GPT 등장이 가져온 변화 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">📊 GPT 등장이 가져온 변화</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT-1이 등장한 이후, AI 모델 개발의 흐름이 완전히 바뀌었습니다.
</p>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px; margin-top: 14px;">
<tr>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#64748b; white-space:nowrap; width:140px;">GPT 이전</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">과제별 개별 학습</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">매번 처음부터 학습, 비용↑</td>
</tr>
<tr><td style="height:2px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#FF6B00; white-space:nowrap;">GPT-1 (2018)</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">사전 학습 도입</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">범용 언어 이해 + 미세 조정</td>
</tr>
<tr><td style="height:2px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#1681c4; white-space:nowrap;">GPT-2 (2019)</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">규모 확장</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">훨씬 더 많은 데이터, 더 큰 모델</td>
</tr>
<tr><td style="height:2px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#1681c4; white-space:nowrap;">GPT-3 (2020)</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">초대규모</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">1,750억 개 파라미터, 거의 학습 불필요</td>
</tr>
<tr><td style="height:2px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#0f172a; color:#c3e88d; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; white-space:nowrap;">ChatGPT (2022)</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">대화 특화</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">대화 방식 학습 추가 (RLHF)</td>
</tr>
</table>

</div>

<br>

<!-- GPT 이름의 의미 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🔑 GPT의 이름 속에 담긴 의미</h2>

<div style="display: grid; gap: 10px; margin-top: 14px;">

<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:14px 18px; display:flex; gap:16px; align-items:center;">
<div style="flex-shrink:0; background:#FF6B00; color:#fff; width:40px; height:40px; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:900;">G</div>
<div>
<div style="font-size:15px; font-weight:900; color:#FF6B00;">Generative</div>
<div style="font-size:13px; color:#475569; line-height:1.6;">생성하는 — 언어를 직접 만들어낼 수 있음</div>
</div>
</div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px; display:flex; gap:16px; align-items:center;">
<div style="flex-shrink:0; background:#1681c4; color:#fff; width:40px; height:40px; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:900;">P</div>
<div>
<div style="font-size:15px; font-weight:900; color:#1681c4;">Pre-trained</div>
<div style="font-size:13px; color:#475569; line-height:1.6;">사전 학습된 — 미리 대규모 데이터로 언어를 학습해둠</div>
</div>
</div>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px; display:flex; gap:16px; align-items:center;">
<div style="flex-shrink:0; background:#0f172a; color:#c3e88d; width:40px; height:40px; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:900;">T</div>
<div>
<div style="font-size:15px; font-weight:900; color:#0f172a;">Transformer</div>
<div style="font-size:13px; color:#475569; line-height:1.6;">트랜스포머 구조 기반 — Self-Attention을 사용</div>
</div>
</div>

</div>

<div style="margin-top: 14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align:center;">
이 세 단어만 알면 GPT가 무엇인지 절반은 이해한 셈입니다.
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;"><span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리</div>
<div style="display: grid; gap: 8px;">
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">GPT는 <b style="color:#FF6B00;">"생성(Generative)"</b>에 특화된 사전 학습 모델입니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">한 번 크게 학습해두고, 다양한 과제에 재사용하는 <b style="color:#FF6B00;">사전 학습 패러다임</b>을 도입했습니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">이 방식이 이후 <b style="color:#FF6B00;">ChatGPT, Claude 등 현대 AI</b>의 기반이 됩니다.</div>
</div>
</div>

</div>