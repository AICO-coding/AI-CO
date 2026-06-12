<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">Chapter 07 · GPT</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">Decoder 블록의 전체 구조</h1>
<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
GPT는 Decoder 블록을 <b style="color:#1681c4;">여러 층으로 쌓아</b> 만듭니다.<br>
블록 내부의 세 가지 구성 요소와 <b style="color:#FF6B00;">위치 인코딩</b>까지 알아봅니다.
</p>
</div>

<br>

<!-- 층층이 쌓다 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🏢 Decoder 블록을 층층이 쌓다</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
GPT는 Transformer Decoder 블록 하나를 만든 뒤, 그것을 <b>여러 층(Layer)으로 쌓아 올립니다.</b>
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Decoder 층 구조</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.2; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace; text-align:center;"><span style="color:#6c7086;">↑ 최종 출력 (다음 단어 확률)</span>
<span style="color:#a6e3a1;">┌────────────┐</span>
<span style="color:#a6e3a1;">                 │  Decoder   │</span>  <span style="color:#f9e2af;">12층 (GPT-1 기준)</span>
<span style="color:#a6e3a1;">│   Block    │</span>
<span style="color:#89dceb;">├────────────┤</span>
<span style="color:#89dceb;">│  Decoder   │</span>
<span style="color:#89dceb;">│   Block    │</span>
<span style="color:#89dceb;">├────────────┤</span>
<span style="color:#89dceb;">│  Decoder   │</span>
<span style="color:#89dceb;">│   Block    │</span>
<span style="color:#89dceb;">├────────────┤</span>
<span style="color:#6c7086;">     ...</span>
<span style="color:#89dceb;">├────────────┤</span>
<span style="color:#89dceb;">│  Decoder   │</span>
<span style="color:#89dceb;">    │   Block    │</span>  <span style="color:#f9e2af;">1층</span>
<span style="color:#89dceb;">└────────────┘</span>
<span style="color:#6c7086;">↑ 입력 (단어 + 위치 정보)</span></div>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📈</span> 층이 많을수록 더 복잡한 언어 패턴을 학습할 수 있습니다. <b style="color:#1681c4;">GPT-1은 12층, GPT-3는 무려 96층</b>입니다.
</div>

</div>

<br>

<!-- 내부 구조 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">📦 Decoder 블록 하나의 내부 구조</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">Decoder 블록 안에는 크게 3가지 구성 요소가 있습니다.</p>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px; margin-top: 14px;">
<tr>
<td style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:14px 18px;">
<div style="display:flex; gap:10px; align-items:center;">
<div style="background:#1681c4; color:#fff; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:900;">①</div>
<div>
<div style="font-size:14px; font-weight:900; color:#1681c4;">Masked Self-Attention</div>
<div style="font-size:12px; color:#475569;">앞 단어만 참고해 관련성 계산</div>
</div>
</div>
</td>
</tr>
<tr><td style="height:2px; text-align:center; color:#94a3b8; font-size:14px;">↑</td></tr>
<tr>
<td style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:14px 18px;">
<div style="display:flex; gap:10px; align-items:center;">
<div style="background:#64748b; color:#fff; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:900;">②</div>
<div>
<div style="font-size:14px; font-weight:900; color:#64748b;">Layer Normalization</div>
<div style="font-size:12px; color:#475569;">학습 안정화 장치</div>
</div>
</div>
</td>
</tr>
<tr><td style="height:2px; text-align:center; color:#94a3b8; font-size:14px;">↑</td></tr>
<tr>
<td style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:14px 18px;">
<div style="display:flex; gap:10px; align-items:center;">
<div style="background:#FF6B00; color:#fff; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:900;">③</div>
<div>
<div style="font-size:14px; font-weight:900; color:#FF6B00;">Feed-Forward Network (FFN)</div>
<div style="font-size:12px; color:#475569;">각 단어를 개별적으로 처리</div>
</div>
</div>
</td>
</tr>
</table>

<div style="margin-top: 10px; font-size: 13px; color: #94a3b8; text-align:center;">각 요소를 하나씩 살펴봅시다.</div>

</div>

<br>

<!-- ① Masked Self-Attention -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">① Masked Self-Attention <span style="font-size:13px; font-weight:700; color:#94a3b8;">(이미 앞에서 배움)</span></h2>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
앞 페이지에서 배운 내용입니다. 현재까지 나온 단어들 사이의 관련성을 계산하되, <b style="color:#1681c4;">미래 단어는 볼 수 없게 마스킹</b>합니다.
</div>

</div>

<br>

<!-- ② Layer Normalization -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">② Layer Normalization — 학습을 안정시키는 장치</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
층을 여러 개 쌓으면 학습이 불안정해질 수 있습니다. 숫자가 너무 크거나 너무 작아지면 학습이 망가지기 때문입니다.
</p>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:18px 20px; margin: 14px 0;">
<div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:10px;">🍳 비유: 요리할 때 간 맞추기</div>
<div style="font-size:14px; color:#334155; line-height:1.8;">
여러 요리사가 릴레이로 요리를 할 때, 앞 요리사가 너무 짜게 만들면 뒤 요리사가 힘들어집니다.<br>
Layer Normalization은 각 단계 후 <b style="color:#1681c4;">간을 적당히 맞춰주는</b> 역할입니다.<br>
(숫자의 평균과 분산을 일정하게 유지)
</div>
</div>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> GPT는 이를 약간 변형한 <b style="color:#FF6B00;">Pre-Layer Normalization</b> 방식을 사용합니다.
</div>

</div>

<br>

<!-- ③ FFN -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">③ Feed-Forward Network (FFN) — 각 단어를 개별 처리</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
셀프 어텐션이 단어들 <b>사이의 관계</b>를 처리했다면, FFN은 각 단어를 <b style="color:#FF6B00;">개별적으로</b> 더 깊이 처리합니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; padding: 16px 20px; font-family:'JetBrains Mono','Consolas',monospace; font-size: 13px; line-height: 2.4; margin: 14px 0; text-align:center; overflow-x:auto; white-space:pre;"><span style="color:#a6e3a1;">단어 "먹었다"의 벡터</span>
       <span style="color:#6c7086;">↓</span>
<span style="color:#89dceb;">[선형 변환 → 활성화 함수(ReLU/GELU) → 선형 변환]</span>
       <span style="color:#6c7086;">↓</span>
<span style="color:#f9e2af; font-weight:900;">더 풍부한 표현으로 변환된 "먹었다" 벡터</span></div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:18px 20px;">
<div style="font-size:14px; font-weight:900; color:#0f172a; margin-bottom:10px;">🧑‍💼 비유: 단어 하나하나를 전문가가 심층 분석</div>
<div style="font-size:14px; color:#334155; line-height:1.8;">
어텐션이 <b style="color:#1681c4;">"팀원 간 소통"</b>이라면, FFN은 <b style="color:#1681c4;">"각 팀원이 혼자 깊이 생각하는 시간"</b>입니다.<br>
두 과정이 모두 있어야 좋은 결과가 나옵니다.
</div>
</div>

</div>

<br>

<!-- 위치 인코딩 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">📍 위치 인코딩 (Positional Encoding) — 순서를 기억하는 방법</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
셀프 어텐션에는 한 가지 맹점이 있습니다. <b style="color:#FF6B00;">단어의 순서를 자동으로 알지 못합니다.</b>
</p>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
단어를 한꺼번에 처리하다 보니, 어느 단어가 앞에 있고 뒤에 있는지를 알려줘야 합니다.
</p>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; margin: 14px 0;">
<b style="color:#FF6B00;">예시:</b> "나는 그를 때렸다" 와 "그는 나를 때렸다"<br>
같은 단어가 있지만 순서가 달라 의미가 완전히 다릅니다!
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
그래서 GPT는 각 단어의 입력 벡터에 <b style="color:#1681c4;">위치 정보를 더해</b> 줍니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; padding: 16px 20px; font-family:'JetBrains Mono','Consolas',monospace; font-size: 13px; line-height: 2.4; overflow-x:auto; white-space:pre;"><span style="color:#cdd6f4;">입력 벡터 = </span><span style="color:#89dceb;">단어 임베딩 벡터</span> <span style="color:#6c7086;">+</span> <span style="color:#f9e2af;">위치 인코딩 벡터</span>
              <span style="color:#89dceb;">(의미)</span>            <span style="color:#f9e2af;">(위치 정보)</span>

<span style="color:#6c7086;">예시:</span>
<span style="color:#a6e3a1;">"나는(1번째)"</span> <span style="color:#cdd6f4;">= [0.2, 0.8, ...] + </span><span style="color:#f9e2af;">[위치1의 고유 신호]</span>
<span style="color:#a6e3a1;">"나는(3번째)"</span> <span style="color:#cdd6f4;">= [0.2, 0.8, ...] + </span><span style="color:#f9e2af;">[위치3의 고유 신호]</span></div>

<div style="margin-top: 14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align:center;">
같은 단어라도 <b style="color:#1681c4;">문장 안에서의 위치에 따라 다른 벡터</b>를 갖게 됩니다.
</div>

</div>

<br>

<!-- GPT 버전별 비교 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🔢 GPT 버전별 구조 크기 비교</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
층이 많고 모델이 클수록 더 강력하지만, 그만큼 학습 비용도 커집니다.
</p>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px; margin-top: 14px;">
<tr>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#64748b; white-space:nowrap; width:90px;">GPT-1</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; text-align:center; width:90px;">12층</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; text-align:center; width:110px;">1.17억 개</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">사전학습 패러다임 도입</td>
</tr>
<tr><td style="height:2px;"></td><td></td><td></td><td></td></tr>
<tr>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#1681c4; white-space:nowrap;">GPT-2</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; text-align:center;">48층</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; text-align:center;">15억 개</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">"너무 위험하다"며 공개 지연</td>
</tr>
<tr><td style="height:2px;"></td><td></td><td></td><td></td></tr>
<tr>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#FF6B00; white-space:nowrap;">GPT-3</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; text-align:center;">96층</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; text-align:center;">1,750억 개</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">거의 추가학습 없이 다양한 과제 수행</td>
</tr>
<tr><td style="height:2px;"></td><td></td><td></td><td></td></tr>
<tr>
<td style="background:#0f172a; color:#c3e88d; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; white-space:nowrap;">GPT-4</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; text-align:center;">비공개</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; text-align:center;">비공개</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">멀티모달(텍스트+이미지)</td>
</tr>
</table>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;"><span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리</div>
<div style="display: grid; gap: 8px;">
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">GPT Decoder 블록 = <b style="color:#FF6B00;">Masked Self-Attention + Layer Norm + FFN</b>의 조합입니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">이 블록을 수십 층 <b style="color:#FF6B00;">쌓을수록</b> 더 복잡한 언어 패턴을 학습할 수 있습니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;"><b style="color:#FF6B00;">위치 인코딩</b>으로 단어 순서 정보를 모델에 알려줍니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">층이 많고 파라미터가 많을수록 강력 → <b style="color:#FF6B00;">GPT-1(12층) → GPT-3(96층)</b>으로 발전했습니다.</div>
</div>
</div>

</div>