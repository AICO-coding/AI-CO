<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">Chapter 07 · GPT</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">Decoder의 셀프 어텐션(Self-Attention)</h1>
<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Decoder의 핵심 메커니즘인 <b style="color:#1681c4;">Self-Attention</b>과,<br>
GPT만의 특별한 규칙인 <b style="color:#FF6B00;">Masked Self-Attention</b>을 알아봅니다.
</p>
</div>

<br>

<!-- Decoder 안에서 가장 중요한 것 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🧠 Decoder 안에서 가장 중요한 것</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Transformer Decoder 안에는 여러 장치가 있지만, 가장 핵심적인 개념은 단연 <b style="color:#1681c4;">셀프 어텐션(Self-Attention)</b>입니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center; margin: 14px 0;">
"문장 안에서 각 단어가 다른 단어들과 얼마나 관련 있는지를 스스로 계산하는 것"
</div>

</div>

<br>

<!-- 비유: 강의실 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">👀 비유로 이해하기: 강의실에서 집중하는 방향</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
강의실에 학생들이 앉아 있습니다. 선생님이 "이 문장에서 가장 중요한 단어에 집중해봐"라고 했을 때, 각 학생(단어)은 <b>다른 학생들을 얼마나 쳐다보는지</b>를 결정합니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">"먹었다" 입장에서의 Attention</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#6c7086;">문장: "그 고양이는 배가 고파서 밥을 먹었다"</span>

<span style="color:#cdd6f4;">"먹었다" 입장에서 어떤 단어를 가장 주목할까?</span>
  <span style="color:#6c7086;">→</span> <span style="color:#a6e3a1; font-weight:900;">"고양이"</span> <span style="color:#6c7086;">(행동의 주체)</span>    <span style="color:#f9e2af;">★★★★★ 매우 중요</span>
  <span style="color:#6c7086;">→</span> <span style="color:#89dceb; font-weight:900;">"밥을"</span>   <span style="color:#6c7086;">(먹은 대상)</span>      <span style="color:#f9e2af;">★★★★☆ 중요</span>
  <span style="color:#6c7086;">→</span> <span style="color:#cdd6f4;">"고파서"</span> <span style="color:#6c7086;">(먹은 이유)</span>      <span style="color:#6c7086;">★★★☆☆ 보통</span>
  <span style="color:#6c7086;">→</span> <span style="color:#6c7086;">"그"</span>     <span style="color:#6c7086;">(관사)         </span>  <span style="color:#6c7086;">★☆☆☆☆ 별로 안 중요</span></div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 각 단어는 자신과 관련 깊은 단어에 <b style="color:#FF6B00;">높은 점수(Attention Weight)</b>를 줍니다. 이 점수들을 모아 그 단어의 의미를 더 정확히 표현합니다.
</div>

</div>

<br>

<!-- 계산 과정 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🔍 셀프 어텐션 계산 과정 (쉽게)</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
실제로는 수학적 계산이지만, 개념적으로는 이렇게 이해할 수 있습니다.
</p>

<table style="width:100%; border-collapse: separate; border-spacing: 0 10px; margin-top: 14px;">
<tr>
<td style="background:#FF6B00; color:#fff; padding:5px 12px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:top; width:90px; text-align:center;">STEP 1</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; line-height:1.9;">
<b>각 단어에 세 가지 역할을 부여한다</b><br>
<span style="color:#1681c4; font-weight:900;">Query (Q):</span> "나는 어떤 정보가 필요한가?"<br>
<span style="color:#1681c4; font-weight:900;">Key (K):</span> "나는 어떤 정보를 가지고 있는가?"<br>
<span style="color:#FF6B00; font-weight:900;">Value (V):</span> "실제로 전달할 내용"
</td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#1681c4; color:#fff; padding:5px 12px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:top; width:90px; text-align:center;">STEP 2</td>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; line-height:1.9;">
<b>Query와 Key를 비교해 관련성(점수)을 계산한다</b><br>
<span style="font-family:Consolas,monospace; font-size:12px;">"먹었다"의 Q ↔ "고양이"의 K → 높은 점수</span><br>
<span style="font-family:Consolas,monospace; font-size:12px;">"먹었다"의 Q ↔ "그"의 K → 낮은 점수</span>
</td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#FF6B00; color:#fff; padding:5px 12px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:top; width:90px; text-align:center;">STEP 3</td>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; line-height:1.9;">
<b>점수에 따라 Value를 가중 합산한다</b><br>
관련 깊은 단어의 정보를 더 많이 반영
</td>
</tr>
</table>

<!-- 도서관 비유 -->
<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px; margin-top: 16px;">
<div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:12px;">📚 도서관 비유</div>
<table style="width:100%; border-collapse: separate; border-spacing: 0 6px;">
<tr>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:8px 12px; font-size:13px; font-weight:900; color:#1681c4; white-space:nowrap; width:90px;">Query</td>
<td style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 12px; font-size:13px; color:#334155;">내가 찾고 싶은 주제 (검색어)</td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:8px; padding:8px 12px; font-size:13px; font-weight:900; color:#1681c4; white-space:nowrap;">Key</td>
<td style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 12px; font-size:13px; color:#334155;">책의 제목, 목차 (검색 대상)</td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:8px; padding:8px 12px; font-size:13px; font-weight:900; color:#FF6B00; white-space:nowrap;">Value</td>
<td style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:8px 12px; font-size:13px; color:#334155;">책 안에 담긴 실제 내용</td>
</tr>
</table>
<div style="margin-top:10px; font-size:13px; color:#475569; line-height:1.7;">검색어와 제목이 잘 맞는 책의 내용을 더 많이 가져오는 것과 같습니다.</div>
</div>

</div>

<br>

<!-- Masked Self-Attention -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🚫 GPT Decoder의 특별한 규칙: Masked Self-Attention</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
일반 셀프 어텐션은 문장 전체를 볼 수 있습니다. 하지만 GPT는 한 가지 중요한 제한을 둡니다.
</p>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #FF6B00; font-weight: 900; text-align: center; margin: 14px 0;">
"미래 단어는 볼 수 없다"
</div>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Masked Self-Attention 예시</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#6c7086;">문장: "오늘  날씨가  좋아서  기분이  좋다"</span>
<span style="color:#6c7086;">       (1)    (2)     (3)     (4)    (5)</span>

<span style="color:#cdd6f4;">"날씨가(2)"가 볼 수 있는 단어:</span>
  <span style="color:#a6e3a1;">✅ "오늘(1)"</span>    <span style="color:#6c7086;">← 이미 나온 단어, 볼 수 있음</span>
  <span style="color:#f38ba8;">🚫 "좋아서(3)"</span> <span style="color:#6c7086;">← 아직 안 나온 단어, 볼 수 없음</span>
  <span style="color:#f38ba8;">🚫 "기분이(4)"</span> <span style="color:#6c7086;">← 아직 안 나온 단어, 볼 수 없음</span>
  <span style="color:#f38ba8;">🚫 "좋다(5)"</span>   <span style="color:#6c7086;">← 아직 안 나온 단어, 볼 수 없음</span></div>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 10px;">왜 이런 제한을 걸까요?</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
GPT는 <b style="color:#1681c4;">"아직 생성하지 않은 미래의 단어를 보고 현재 단어를 결정하면 안 되기 때문"</b>입니다.<br>
실제 문장 생성 때는 미래 단어가 존재하지 않으니까요. 학습할 때도 실제 사용 조건과 동일하게 유지해야 합니다.
</div>

</div>

<br>

<!-- Masked vs 일반 비교 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🎭 Masked vs 일반 Self-Attention 비교</h2>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px; margin-top: 14px;">
<tr>
<td style="background:#f8fafc; font-size:12px; font-weight:900; color:#94a3b8; padding:0 8px; width:120px;"></td>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#1681c4; text-align:center;">BERT (일반 Self-Attention)</td>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#FF6B00; text-align:center;">GPT (Masked Self-Attention)</td>
</tr>
<tr><td style="height:4px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#64748b;">볼 수 있는 범위</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; text-align:center;">문장 전체 (앞뒤 모두)</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; text-align:center;">현재까지 나온 단어만 (왼쪽만)</td>
</tr>
<tr><td style="height:4px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#64748b;">목적</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; text-align:center;">전체 문맥 파악 → 이해</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; text-align:center;">과거 내용으로 다음 단어 예측 → 생성</td>
</tr>
<tr><td style="height:4px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#64748b;">비유</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:12px; color:#334155; text-align:center;">완성된 글을 처음부터 끝까지 읽는 독자</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:12px; color:#334155; text-align:center;">소설을 한 줄씩 써 내려가는 작가</td>
</tr>
</table>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;"><span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리</div>
<div style="display: grid; gap: 8px;">
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;"><b style="color:#FF6B00;">셀프 어텐션</b>: 문장 안에서 각 단어가 다른 단어들과의 관련성을 계산하는 메커니즘입니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;"><b style="color:#FF6B00;">Q</b>(무엇이 필요?), <b style="color:#FF6B00;">K</b>(무엇을 갖고 있나?), <b style="color:#FF6B00;">V</b>(실제 내용)의 세 요소로 작동합니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">GPT는 <b style="color:#FF6B00;">Masked Self-Attention</b> 사용 → 미래 단어는 절대 볼 수 없습니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">이 마스킹 덕분에 GPT는 <b style="color:#FF6B00;">자연스러운 순서대로</b> 문장을 생성할 수 있습니다.</div>
</div>
</div>

</div>