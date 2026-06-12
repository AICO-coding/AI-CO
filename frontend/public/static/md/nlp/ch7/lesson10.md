<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">Chapter 07 · GPT</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">학습할 때와 실제로 쓸 때, 무엇이 다를까?</h1>
<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
GPT는 <b style="color:#1681c4;">손실(Loss)</b>을 계산해 스스로를 수정하며 학습합니다.<br>
학습 과정과 실제 추론(생성) 과정의 차이를 알아봅니다.
</p>
</div>

<br>

<!-- 어떻게 정확해지나 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🎓 GPT는 어떻게 "틀린 걸 고쳐나가며" 학습할까?</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
지금까지는 GPT가 다음 단어를 예측한다고 배웠습니다. 그런데 처음에는 당연히 예측이 엉망일 텐데, 어떻게 점점 정확해질까요?
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center;">
"정답과 비교해서, 틀린 만큼 스스로를 수정한다"
</div>

</div>

<br>

<!-- 손실(Loss) -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">📐 손실(Loss) — 얼마나 틀렸는지를 숫자로 나타낸 것</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT는 예측이 정답과 얼마나 다른지를 숫자로 계산합니다. 이 숫자를 <b style="color:#1681c4;">손실(Loss)</b>이라고 합니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 12px 16px; border-radius: 12px; font-size: 14px; color: #1681c4; font-weight: 900; text-align: center; margin: 14px 0;">
학습 예시: "나는 오늘 학교에 갔다"
</div>

<table style="width:100%; border-collapse: separate; border-spacing: 0 10px;">
<tr>
<td style="background:#f0fdf4; border:2px solid #86efac; border-radius:14px; padding:14px 18px;">
<div style="font-size:13px; font-weight:900; color:#16a34a; margin-bottom:8px;">"나는" 다음에 올 단어를 예측</div>
<div style="font-size:13px; color:#334155; line-height:1.8;">
정답: <b>"오늘"</b><br>
GPT 예측 확률: "오늘" <b style="color:#16a34a;">72%</b><br>
손실: <b style="color:#16a34a;">낮음</b> → 거의 맞혔으니 조금만 수정
</div>
</td>
</tr>
<tr><td style="height:2px;"></td></tr>
<tr>
<td style="background:#fff1f2; border:2px solid #fca5a5; border-radius:14px; padding:14px 18px;">
<div style="font-size:13px; font-weight:900; color:#dc2626; margin-bottom:8px;">"나는 오늘 학교에" 다음에 올 단어를 예측</div>
<div style="font-size:13px; color:#334155; line-height:1.8;">
정답: <b>"갔다"</b><br>
GPT 예측 확률: "갔다" <b style="color:#dc2626;">18%</b><br>
손실: <b style="color:#dc2626;">높음</b> → 많이 틀렸으니 크게 수정
</div>
</td>
</tr>
</table>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">🔁</span> 손실이 클수록 더 크게 수정하고, 손실이 작을수록 조금만 수정합니다. 이 과정이 <b style="color:#FF6B00;">수억 번 반복</b>되면서 GPT가 점점 정확해집니다.
</div>

</div>

<br>

<!-- 비유: 받아쓰기 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🏋️ 비유로 이해하기: 받아쓰기 연습</h2>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px;">

<div style="font-size:14px; color:#334155; line-height:1.8; margin-bottom:12px;">
학생이 받아쓰기 시험을 봅니다.
</div>

<table style="width:100%; border-collapse: separate; border-spacing: 0 6px;">
<tr>
<td style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 12px; font-size:13px; font-weight:900; color:#64748b; white-space:nowrap; width:90px;">문제</td>
<td style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 12px; font-size:13px; color:#334155;">"나는 오늘 학교에 ___"</td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#fff1f2; border:1px solid #fca5a5; border-radius:8px; padding:8px 12px; font-size:13px; font-weight:900; color:#dc2626; white-space:nowrap;">학생 답</td>
<td style="background:#fff1f2; border:1px solid #fca5a5; border-radius:8px; padding:8px 12px; font-size:13px; color:#334155;">"집에" (틀림)</td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#f0fdf4; border:1px solid #86efac; border-radius:8px; padding:8px 12px; font-size:13px; font-weight:900; color:#16a34a; white-space:nowrap;">정답</td>
<td style="background:#f0fdf4; border:1px solid #86efac; border-radius:8px; padding:8px 12px; font-size:13px; color:#334155;">"갔다"</td>
</tr>
</table>

<div style="margin-top:12px; font-size:14px; color:#334155; line-height:1.8;">
선생님이 틀린 부분에 빨간 펜으로 표시하고 점수를 줍니다. 학생은 틀린 부분을 확인하고 다음에는 더 잘 씁니다.
</div>

</div>

<div style="margin-top: 14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align:center;">
<b style="color:#1681c4;">GPT의 학습이 정확히 이 구조입니다.</b><br>
예측 → 정답 확인 → 수정 → 다시 예측 → 반복
</div>

</div>

<br>

<!-- 학습 vs 사용 차이 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🔄 학습할 때 vs 실제로 쓸 때: 결정적인 차이</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
학습이 끝난 GPT를 실제로 사용할 때는 방식이 달라집니다.
</p>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px; margin-top: 14px;">
<tr>
<td style="background:#f8fafc; font-size:12px; font-weight:900; color:#94a3b8; padding:0 8px; width:90px;"></td>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#1681c4; text-align:center;">학습할 때</td>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#FF6B00; text-align:center;">실제로 사용할 때</td>
</tr>
<tr><td style="height:4px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#64748b;">처리 방식</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; text-align:center;">문장 전체를 한 번에 처리</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; text-align:center;">단어를 하나씩 순서대로 생성</td>
</tr>
<tr><td style="height:4px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#64748b;">정답 여부</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; text-align:center;">정답이 있어서 비교 가능</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; text-align:center;">정답 없음, 스스로 생성</td>
</tr>
<tr><td style="height:4px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#64748b;">목적</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; text-align:center;">틀린 예측을 수정해 더 좋아지기</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; text-align:center;">지금까지 배운 것으로 최선의 답 생성</td>
</tr>
<tr><td style="height:4px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#64748b;">속도</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; text-align:center;">병렬 처리라 빠름</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; text-align:center;">한 단어씩이라 상대적으로 느림</td>
</tr>
</table>

<!-- 운전 비유 -->
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px;">
<div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:6px;">🚗 연습장 (학습)</div>
<div style="font-size:13px; color:#334155; line-height:1.7;">교관이 옆에 앉아 틀릴 때마다 바로 교정해줍니다. → 빠르게 실력이 늘어남</div>
</div>
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:14px 18px;">
<div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:6px;">🛣️ 실제 운전 (사용)</div>
<div style="font-size:13px; color:#334155; line-height:1.7;">면허를 따고 나면 혼자 핸들을 잡습니다. → 지금까지 배운 것으로 스스로 판단</div>
</div>
</div>

</div>

<br>

<!-- 학습 전체 흐름 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🌊 학습 전체 흐름 한눈에 보기</h2>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin-top: 14px;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">GPT 사전학습 흐름</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.2; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#a6e3a1;">① 대량의 텍스트 준비</span>
   <span style="color:#6c7086;">(인터넷 글, 책, 위키피디아 등 수백 GB)</span>
        <span style="color:#6c7086;">↓</span>
<span style="color:#89dceb;">② 문장을 토큰 단위로 자르기</span>
   <span style="color:#6c7086;">"나는 오늘 밥을 먹었다" → [나는, 오늘, 밥을, 먹었다]</span>
        <span style="color:#6c7086;">↓</span>
<span style="color:#f9e2af;">③ 각 위치에서 "다음 단어" 예측 문제 생성</span>
   <span style="color:#6c7086;">[나는] → "오늘"?,  [나는, 오늘] → "밥을"?  ...</span>
        <span style="color:#6c7086;">↓</span>
<span style="color:#cba6f7;">④ 소프트맥스로 확률 분포 계산</span>
        <span style="color:#6c7086;">↓</span>
<span style="color:#f38ba8;">⑤ 정답과 비교해 손실(Loss) 계산</span>
        <span style="color:#6c7086;">↓</span>
<span style="color:#89dceb;">⑥ 손실을 바탕으로 파라미터 수정</span>
        <span style="color:#6c7086;">↓</span>
<span style="color:#6c7086;">⑦ ③~⑥을 수억~수천억 번 반복</span>
        <span style="color:#6c7086;">↓</span>
<span style="color:#a6e3a1; font-weight:900;">⑧ 완성된 GPT 모델</span></div>
</div>

</div>

<br>

<!-- 추론 흐름 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">⚡ 실제 사용할 때(추론) 흐름</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
학습이 끝난 GPT가 실제로 문장을 생성하는 흐름입니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">추론(생성) 흐름</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.2; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#6c7086;">사용자 입력: "오늘 날씨가"</span>

<span style="color:#a6e3a1;">1. 입력 토큰화 → [오늘, 날씨가]</span>
<span style="color:#89dceb;">2. 임베딩 + 위치 인코딩</span>
<span style="color:#f9e2af;">3. Decoder 블록 12개 통과 (GPT-1 기준)</span>
<span style="color:#cba6f7;">4. 최종 층에서 전체 단어 점수(로짓) 계산</span>
<span style="color:#f38ba8;">5. 소프트맥스 → 확률 분포</span>
<span style="color:#a6e3a1;">6. 디코딩 전략으로 "좋아서" 선택</span>
<span style="color:#89dceb;">7. "좋아서"를 다시 입력에 추가</span>

<span style="color:#6c7086;">→ [오늘, 날씨가, 좋아서] 로 2~6 반복</span>
<span style="color:#6c7086;">→ [오늘, 날씨가, 좋아서, 기분이] 로 반복</span>
<span style="color:#6c7086;">→ [오늘, 날씨가, 좋아서, 기분이, 좋다] 로 반복</span>
<span style="color:#6c7086;">→ [종료 토큰] 감지 → 생성 완료</span>

<span style="color:#f9e2af; font-weight:900;">최종 출력: "오늘 날씨가 좋아서 기분이 좋다"</span></div>
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;"><span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리</div>
<div style="display: grid; gap: 8px;">
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">학습: 예측 → 정답과 비교 → <b style="color:#FF6B00;">손실(Loss) 계산</b> → 파라미터 수정 → 반복</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">손실이 클수록 크게 수정, 작을수록 조금 수정 → <b style="color:#FF6B00;">수억 번 반복</b>하면 점점 정확해집니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">학습 중엔 문장 전체를 <b style="color:#FF6B00;">한 번에</b> 처리 / 실제 사용 시엔 단어를 <b style="color:#FF6B00;">하나씩</b> 생성합니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">추론 흐름: 입력 → 임베딩 → Decoder → 소프트맥스 → 단어 선택 → 반복</div>
</div>
</div>

</div>