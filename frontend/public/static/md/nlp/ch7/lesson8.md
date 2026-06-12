<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">Chapter 07 · GPT</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">다음 단어 예측 방식</h1>
<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
GPT는 단어 하나를 바로 찍지 않습니다.<br>
<b style="color:#1681c4;">로짓(점수) → 소프트맥스 → 확률</b>로 변환되는 과정을 알아봅니다.
</p>
</div>

<br>

<!-- 어떻게 고르는가 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🎲 GPT는 단어를 어떻게 "고르는가"?</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
7-2에서 GPT가 "다음 단어를 예측한다"고 배웠습니다. 그런데 실제로는 어떤 과정으로 단어를 고를까요?
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center;">
"모든 단어에 점수를 매긴 뒤, 그 점수를 확률로 변환해서 선택"
</div>

</div>

<br>

<!-- STEP 1 로짓 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#FF6B00; color:#fff; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">STEP 1</span>
모든 단어에 점수(로짓)를 매긴다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT의 마지막 층을 통과하면, 단어 사전에 있는 <b>모든 단어에 대한 점수(로짓, Logit)</b>가 만들어집니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">단어 사전 전체에 대한 점수</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#6c7086;">입력: "오늘 날씨가"</span>

<span style="color:#cdd6f4;">"좋아서"   → 점수: </span><span style="color:#a6e3a1; font-weight:900;">8.3</span>   <span style="color:#6c7086;">← 높음</span>
<span style="color:#cdd6f4;">"나빠서"   → 점수: </span><span style="color:#89dceb;">5.1</span>
<span style="color:#cdd6f4;">"먹었다"   → 점수: </span><span style="color:#89dceb;">2.4</span>
<span style="color:#cdd6f4;">"사과"     → 점수: </span><span style="color:#89dceb;">1.2</span>
<span style="color:#cdd6f4;">"이었다"   → 점수: </span><span style="color:#89dceb;">0.7</span>
<span style="color:#cdd6f4;">"의자"     → 점수: </span><span style="color:#f38ba8; font-weight:900;">-3.1</span>  <span style="color:#6c7086;">← 낮음</span>
<span style="color:#6c7086;">...        (단어 사전의 모든 단어, 수만 개)</span></div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 점수가 높을수록 그 자리에 어울리는 단어입니다. 하지만 이 숫자들은 아직 <b style="color:#FF6B00;">"확률"이 아닙니다.</b>
</div>

</div>

<br>

<!-- STEP 2 소프트맥스 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#1681c4; color:#fff; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">STEP 2</span>
소프트맥스(Softmax)로 확률로 바꾼다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
점수들을 그대로 쓸 수는 없습니다. <b style="color:#1681c4;">모든 단어의 확률을 합했을 때 반드시 100%가 되어야</b> 하기 때문입니다.
이 변환을 해주는 것이 <b style="color:#1681c4;">소프트맥스(Softmax) 함수</b>입니다.
</p>

<!-- 비유: 선거 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px; margin: 14px 0;">
<div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:12px;">🗳️ 비유: 점수를 득표율로 바꾸기</div>
<p style="font-size:14px; color:#334155; line-height:1.8; margin:0 0 12px 0;">학급 반장 선거에서 각 후보가 얻은 표가 있습니다.</p>

<table style="width:100%; border-collapse: separate; border-spacing: 0 6px;">
<tr>
<td style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 12px; font-size:13px; font-weight:900; color:#334155; text-align:center; width:90px;">A후보</td>
<td style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 12px; font-size:13px; color:#334155; text-align:center;">15표</td>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:8px 12px; font-size:13px; font-weight:900; color:#1681c4; text-align:center;">50%</td>
</tr>
<tr><td style="height:2px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 12px; font-size:13px; font-weight:900; color:#334155; text-align:center;">B후보</td>
<td style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 12px; font-size:13px; color:#334155; text-align:center;">9표</td>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:8px 12px; font-size:13px; font-weight:900; color:#1681c4; text-align:center;">30%</td>
</tr>
<tr><td style="height:2px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 12px; font-size:13px; font-weight:900; color:#334155; text-align:center;">C후보</td>
<td style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 12px; font-size:13px; color:#334155; text-align:center;">6표</td>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:8px 12px; font-size:13px; font-weight:900; color:#1681c4; text-align:center;">20%</td>
</tr>
</table>

<div style="margin-top:10px; font-size:13px; color:#475569; line-height:1.7;">
소프트맥스는 GPT의 점수를 이 <b style="color:#1681c4;">득표율</b>처럼 "모두 더하면 100%가 되는 확률"로 변환합니다.
</div>
</div>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">소프트맥스 적용 후</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#cdd6f4;">"좋아서"   → 확률: </span><span style="color:#a6e3a1; font-weight:900;">43.2%</span>   <span style="color:#6c7086;">← 가장 유력</span>
<span style="color:#cdd6f4;">"나빠서"   → 확률: </span><span style="color:#89dceb;">21.8%</span>
<span style="color:#cdd6f4;">"맑아서"   → 확률: </span><span style="color:#89dceb;">15.1%</span>
<span style="color:#cdd6f4;">"흐려서"   → 확률: </span><span style="color:#89dceb;"> 9.4%</span>
<span style="color:#cdd6f4;">"춥고"     → 확률: </span><span style="color:#89dceb;"> 6.3%</span>
<span style="color:#cdd6f4;">나머지 전부 → 확률: </span><span style="color:#6c7086;"> 4.2%</span>  <span style="color:#6c7086;">(수만 개가 나눠 가짐)</span>
<span style="color:#6c7086;">────────────────────────</span>
<span style="color:#f9e2af; font-weight:900;">합계       → 100.0%</span></div>
</div>

</div>

<br>

<!-- 소프트맥스 특성 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🔑 소프트맥스의 중요한 특성</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
소프트맥스는 단순히 퍼센트로 바꾸는 것 이상의 특성이 있습니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center; margin: 14px 0;">
점수 차이를 "증폭"시킵니다.
</div>

<div style="background-color: #1e1e2e; border-radius: 14px; padding: 16px 20px; font-family:'JetBrains Mono','Consolas',monospace; font-size: 13px; line-height: 2.4; overflow-x:auto; white-space:pre; text-align:center;"><span style="color:#cdd6f4;">점수가 </span><span style="color:#f9e2af;">8.3</span><span style="color:#cdd6f4;">이면 </span><span style="color:#a6e3a1;">43%</span><span style="color:#cdd6f4;">,  점수가 </span><span style="color:#f9e2af;">5.1</span><span style="color:#cdd6f4;">이면 </span><span style="color:#89dceb;">22%</span>
<span style="color:#6c7086;">→ 점수 차이 3.2배  →  확률 차이 약 2배로 증폭</span>

<span style="color:#a6e3a1; font-weight:900;">즉, 높은 점수를 받은 단어가 확률적으로 훨씬 더 유리해집니다.</span></div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 이 특성 덕분에 GPT는 문맥에 어울리는 단어를 훨씬 <b style="color:#FF6B00;">높은 확률로 선택</b>하게 됩니다.
</div>

</div>

<br>

<!-- STEP 3 선택 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
<span style="background:#0f172a; color:#c3e88d; padding:3px 11px; border-radius:999px; font-size:13px; font-weight:900; margin-right:8px;">STEP 3</span>
확률 분포에서 단어를 선택한다
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
확률 분포가 완성되면 드디어 단어를 선택합니다. 선택 방법은 여러 가지가 있고, 이 내용은 다음 페이지에서 자세히 다룹니다.
</p>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 18px 20px; margin-top: 14px;">
<div style="font-size:13px; font-weight:900; color:#0f172a; margin-bottom:14px;">"오늘 날씨가" 다음에 올 단어 확률 분포</div>

<div style="display: grid; gap: 8px;">
<div style="display:grid; grid-template-columns:70px 1fr 60px; gap:10px; align-items:center;">
<div style="font-size:13px; color:#334155; font-weight:900;">좋아서</div>
<div style="background:#e2e8f0; border-radius:6px; height:14px; overflow:hidden;"><div style="background:#1681c4; width:43.2%; height:100%;"></div></div>
<div style="font-size:12px; color:#1681c4; font-weight:900; text-align:right;">43.2%</div>
</div>
<div style="display:grid; grid-template-columns:70px 1fr 60px; gap:10px; align-items:center;">
<div style="font-size:13px; color:#334155;">나빠서</div>
<div style="background:#e2e8f0; border-radius:6px; height:14px; overflow:hidden;"><div style="background:#94a3b8; width:21.8%; height:100%;"></div></div>
<div style="font-size:12px; color:#64748b; text-align:right;">21.8%</div>
</div>
<div style="display:grid; grid-template-columns:70px 1fr 60px; gap:10px; align-items:center;">
<div style="font-size:13px; color:#334155;">맑아서</div>
<div style="background:#e2e8f0; border-radius:6px; height:14px; overflow:hidden;"><div style="background:#94a3b8; width:15.1%; height:100%;"></div></div>
<div style="font-size:12px; color:#64748b; text-align:right;">15.1%</div>
</div>
<div style="display:grid; grid-template-columns:70px 1fr 60px; gap:10px; align-items:center;">
<div style="font-size:13px; color:#334155;">흐려서</div>
<div style="background:#e2e8f0; border-radius:6px; height:14px; overflow:hidden;"><div style="background:#94a3b8; width:9.4%; height:100%;"></div></div>
<div style="font-size:12px; color:#64748b; text-align:right;">9.4%</div>
</div>
<div style="display:grid; grid-template-columns:70px 1fr 60px; gap:10px; align-items:center;">
<div style="font-size:13px; color:#334155;">춥고</div>
<div style="background:#e2e8f0; border-radius:6px; height:14px; overflow:hidden;"><div style="background:#94a3b8; width:6.3%; height:100%;"></div></div>
<div style="font-size:12px; color:#64748b; text-align:right;">6.3%</div>
</div>
<div style="display:grid; grid-template-columns:70px 1fr 60px; gap:10px; align-items:center;">
<div style="font-size:13px; color:#334155;">기타</div>
<div style="background:#e2e8f0; border-radius:6px; height:14px; overflow:hidden;"><div style="background:#94a3b8; width:4.2%; height:100%;"></div></div>
<div style="font-size:12px; color:#64748b; text-align:right;">4.2%</div>
</div>
</div>

<div style="margin-top: 12px; font-size: 13px; color: #1681c4; font-weight: 900; text-align: center;">→ 이 분포에서 단어 하나를 선택</div>
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;"><span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리</div>
<div style="display: grid; gap: 8px;">
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">GPT의 예측은 단어 하나를 찍는 게 아니라 <b style="color:#FF6B00;">전체 단어에 확률 분포</b>를 만드는 것입니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;"><b style="color:#FF6B00;">로짓(점수)</b> → <b style="color:#FF6B00;">소프트맥스</b> → <b style="color:#FF6B00;">확률(합계 100%)</b> 순서로 변환됩니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">소프트맥스는 점수 차이를 <b style="color:#FF6B00;">증폭</b>시켜 적합한 단어가 더 높은 확률을 갖게 합니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">이 확률 분포에서 최종 단어를 선택하는 방법이 <b style="color:#FF6B00;">여러 가지 존재</b>합니다 (다음 페이지에서 계속).</div>
</div>
</div>

</div>