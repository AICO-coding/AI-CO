<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">Chapter 06 · BERT</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">BERT가 등장한 이유</h1>
<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">기존 NLP 모델들이 가졌던 한계를 살펴보고, 왜 <b style="color:#1681c4;">양방향으로 문맥을 이해하는 BERT</b>가 필요했는지 알아봅니다.</p>
</div>

<br>

<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🤔 BERT가 뭔가요?</h2>
<p style="line-height: 1.8; color: #334155; font-size: 15px;">BERT(버트)는 2018년 구글이 발표한 자연어 처리 모델입니다.<br>발표 직후 번역, 질의응답, 문장 분류 등 거의 모든 NLP 과제에서 당시 최고 성능을 갱신했고, 현재까지도 수많은 AI 서비스의 뼈대가 되고 있습니다.</p>
<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 16px 18px; border-radius: 14px; font-size: 14px; color: #334155; line-height: 1.8; margin: 16px 0;">
<div style="color:#1681c4; font-weight:900; margin-bottom:8px;">💡 BERT 이름의 의미</div>
<div style="background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 14px;">
<b style="color:#1681c4;">B</b>idirectional <b style="color:#1681c4;">E</b>ncoder <b style="color:#1681c4;">R</b>epresentations from <b style="color:#1681c4;">T</b>ransformers<br>
<span style="color:#64748b;">→ 트랜스포머를 이용한 양방향 인코더 표현</span>
</div>
</div>
<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 0;">그런데 왜 BERT가 필요했을까요?<br>기존에 있던 모델들이 무엇을 잘 못했는지부터 살펴봐야 합니다.</p>
</div>

<br>

<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">📖 비유: 책 읽기 방식의 차이</h2>
<p style="line-height: 1.8; color: #334155; font-size: 15px;">어떤 독자가 책을 읽는다고 상상해 봅시다.<br>문장을 이해하는 방식은 크게 세 가지로 나눌 수 있습니다.</p>
<div style="overflow-x:auto; margin-top: 16px;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
<thead>
<tr style="background:#0f172a; color:#c3e88d;">
<th style="padding:10px 14px; text-align:left; font-weight:900;">방식</th>
<th style="padding:10px 14px; text-align:left; font-weight:900;">설명</th>
<th style="padding:10px 14px; text-align:left; font-weight:900;">문제</th>
</tr>
</thead>
<tbody>
<tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
<td style="padding:10px 14px; font-weight:900; color:#FF6B00;">왼쪽 → 오른쪽만 읽기</td>
<td style="padding:10px 14px; color:#334155;">앞에서부터 순서대로만 읽음</td>
<td style="padding:10px 14px; color:#475569;">뒤에 나오는 내용이 앞 단어 해석에 영향을 못 줌</td>
</tr>
<tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
<td style="padding:10px 14px; font-weight:900; color:#FF6B00;">오른쪽 → 왼쪽만 읽기</td>
<td style="padding:10px 14px; color:#334155;">뒤에서부터 거꾸로만 읽음</td>
<td style="padding:10px 14px; color:#475569;">반대 방향으로 같은 문제 발생</td>
</tr>
<tr style="background:#eef7ff;">
<td style="padding:10px 14px; font-weight:900; color:#1681c4;">양방향으로 읽기</td>
<td style="padding:10px 14px; color:#334155;">앞뒤 문맥을 동시에 보면서 읽음</td>
<td style="padding:10px 14px; color:#1681c4; font-weight:900;">문맥 이해에 유리함 ✅</td>
</tr>
</tbody>
</table>
</div>
<div style="margin-top: 16px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">📌 핵심</span><br>
기존 NLP 모델들은 대부분 <b>한 방향으로만</b> 문장을 읽었습니다.<br>BERT는 문장 전체를 <b style="color:#FF6B00;">양방향으로 한 번에 이해</b>하도록 설계되었습니다.
</div>
</div>

<br>

<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🔍 기존 모델들의 한계</h2>
<p style="line-height: 1.8; color: #334155; font-size: 15px;">BERT가 등장하기 전에도 여러 NLP 모델이 있었지만, 각각 중요한 한계를 가지고 있었습니다.</p>
<div style="display: grid; gap: 14px; margin-top: 16px;">

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">①</span>
<span style="font-size:15px; font-weight:900; color:#FF6B00;">RNN / LSTM — 긴 문장을 잘 기억하지 못해요</span>
</div>
<p style="margin:0 0 12px 0; line-height:1.8; color:#334155; font-size:14px;">RNN 계열 모델은 문장을 <b>왼쪽에서 오른쪽으로 순서대로</b> 처리합니다.<br>문장이 길어질수록 앞부분의 정보가 희미해지는 <b style="color:#FF6B00;">장기 의존성(Long-term Dependency) 문제</b>가 있습니다.</p>
<pre style="background:#0f172a; color:#cdd6f4; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre-wrap; margin:0;">예시 문장:
&quot;어제 공원에서 강아지를 데리고 산책을 하다가 갑자기 비가 내려서 근처 카페로 피했는데, 그것이 정말 좋았다.&quot;</pre>
<div style="margin-top:12px; background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
이 문장에서 <b style="color:#FF6B00;">&quot;그것&quot;</b>이 무엇을 가리키는지 이해하려면 훨씬 앞의 정보가 필요합니다.<br>RNN은 이런 먼 거리의 관계를 파악하는 데 취약합니다.
</div>
</div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#1681c4; color:#fff; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">②</span>
<span style="font-size:15px; font-weight:900; color:#1681c4;">Word2Vec / GloVe — 문맥이 달라도 같은 벡터를 줘요</span>
</div>
<p style="margin:0 0 12px 0; line-height:1.8; color:#334155; font-size:14px;">챕터 3에서 배운 단어 임베딩인 Word2Vec, GloVe는 단어마다 <b>하나의 고정된 벡터</b>를 가집니다.</p>
<div style="background:#fff; border:1px solid #c2e4ff; border-radius:12px; padding:13px 16px; font-size:14px; color:#334155; line-height:1.9;">
<div style="font-weight:900; color:#1681c4; margin-bottom:8px;">🍎 &quot;배&quot;라는 단어가 들어간 두 문장</div>
<div style="display:grid; gap:8px;">
<div style="background:#f8fafc; border-left:4px solid #1681c4; padding:9px 12px; border-radius:0 8px 8px 0;">나는 <b style="color:#1681c4;">배</b>가 고프다. <span style="color:#64748b;">→ 복부, 배고픔</span></div>
<div style="background:#f8fafc; border-left:4px solid #1681c4; padding:9px 12px; border-radius:0 8px 8px 0;">항구에 큰 <b style="color:#1681c4;">배</b>가 들어왔다. <span style="color:#64748b;">→ 선박</span></div>
</div>
</div>
<div style="margin-top:12px; background:#fff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
두 문장에서 <b>&quot;배&quot;</b>의 의미는 완전히 다릅니다.<br>그런데 Word2Vec은 항상 동일한 벡터를 <b>&quot;배&quot;</b>에 배정합니다.<br>즉, <b style="color:#1681c4;">문맥에 따라 의미가 달라지는 현상</b>을 제대로 반영하지 못합니다.
</div>
</div>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:17px 19px;">
<div style="display:flex; align-items:center; gap:10px; margin-bottom:10px; flex-wrap:wrap;">
<span style="background:#0f172a; color:#c3e88d; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:900;">③</span>
<span style="font-size:15px; font-weight:900; color:#FF6B00;">GPT-1 — 한쪽 방향만 봐요</span>
</div>
<p style="margin:0 0 12px 0; line-height:1.8; color:#334155; font-size:14px;">GPT는 트랜스포머 구조를 사용했고, 언어 생성에서 뛰어난 성능을 보였습니다.<br>하지만 GPT는 <b style="color:#FF6B00;">왼쪽 → 오른쪽</b> 방향으로만 문장을 읽도록 설계됐습니다.</p>
<pre style="background:#0f172a; color:#cdd6f4; border-radius:10px; padding:13px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2.1; overflow-x:auto; white-space:pre-wrap; margin:0;">나는 오늘 [MASK]를 먹었다.</pre>
<div style="margin-top:12px; background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
이 문장의 빈칸을 채우려면 <b>앞뒤 문맥을 동시에</b> 봐야 합니다.<br>하지만 단방향 모델은 빈칸 앞의 내용만 보고 추측하기 때문에 정확도가 떨어질 수 있습니다.
</div>
</div>

</div>
</div>

<br>

<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">📊 기존 모델 한계 요약</h2>
<div style="overflow-x:auto; margin-top: 14px;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
<thead>
<tr style="background:#0f172a; color:#c3e88d;">
<th style="padding:10px 14px; text-align:left; font-weight:900;">모델</th>
<th style="padding:10px 14px; text-align:left; font-weight:900;">구조</th>
<th style="padding:10px 14px; text-align:left; font-weight:900;">핵심 한계</th>
</tr>
</thead>
<tbody>
<tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
<td style="padding:10px 14px; font-weight:900; color:#FF6B00;">RNN / LSTM</td>
<td style="padding:10px 14px; color:#334155;">순차 처리 (→)</td>
<td style="padding:10px 14px; color:#475569;">긴 문장에서 앞 정보 소실</td>
</tr>
<tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
<td style="padding:10px 14px; font-weight:900; color:#FF6B00;">Word2Vec / GloVe</td>
<td style="padding:10px 14px; color:#334155;">고정 벡터</td>
<td style="padding:10px 14px; color:#475569;">동음이의어 구분 불가</td>
</tr>
<tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
<td style="padding:10px 14px; font-weight:900; color:#FF6B00;">GPT-1</td>
<td style="padding:10px 14px; color:#334155;">단방향 트랜스포머 (→)</td>
<td style="padding:10px 14px; color:#475569;">오른쪽 문맥 활용 불가</td>
</tr>
<tr style="background:#eef7ff;">
<td style="padding:10px 14px; font-weight:900; color:#1681c4;">BERT</td>
<td style="padding:10px 14px; color:#1681c4; font-weight:900;">양방향 트랜스포머</td>
<td style="padding:10px 14px; color:#1681c4; font-weight:900;">앞뒤 문맥을 함께 이해 ✅</td>
</tr>
</tbody>
</table>
</div>
<div style="margin-top: 16px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡 BERT의 핵심 차이</span><br>
BERT는 문장을 왼쪽에서 오른쪽으로만 보지 않고, <b style="color:#1681c4;">앞 문맥과 뒤 문맥을 동시에 참고</b>합니다.
</div>
</div>

<br>

<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;"><span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리</div>
<div style="display: grid; gap: 8px;">
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">기존 모델들은 문장을 <b style="color:#FF6B00;">한 방향으로만 읽거나</b>, 문맥을 무시한 <b style="color:#FF6B00;">고정 벡터</b>를 사용했습니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">특히 동음이의어처럼 <b style="color:#FF6B00;">앞뒤 문맥에 따라 의미가 달라지는 단어</b>를 제대로 표현하지 못했습니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">BERT는 이 한계를 <b style="color:#FF6B00;">양방향 학습</b>으로 해결하기 위해 등장했습니다.</div>
</div>
<div style="margin-top:12px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> 다음 페이지에서는 BERT가 말하는 <b style="color:#1681c4;">양방향 문맥 이해</b>가 정확히 무엇인지 더 자세히 살펴봅니다.
</div>
</div>

</div>

