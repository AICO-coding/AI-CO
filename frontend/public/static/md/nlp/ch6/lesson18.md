<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">Chapter 06 · BERT</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">BERT를 활용한 문장 분류 — 미세조정(Fine-tuning)이란?</h1>
<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
사전학습된 BERT 위에 <b style="color:#1681c4;">분류기 하나만 얹으면</b> 강력한 문장 분류 모델이 됩니다.<br>
미세조정의 구조와 학습 원리를 알아봅니다.
</p>
</div>

<br>

<!-- 문장 분류란 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">📂 문장 분류(Sentence Classification)란?</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
주어진 문장을 정해진 카테고리 중 하나로 분류하는 과제로, NLP에서 가장 많이 활용됩니다.
</p>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px; margin-top: 14px;">
<tr>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#FF6B00; white-space:nowrap; width:130px;">감정 분석</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155;">"이 영화 정말 최고였어요!"</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; white-space:nowrap; width:100px; text-align:center;">긍정 😊</td>
</tr>
<tr><td style="height:4px;"></td></tr>
<tr>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#1681c4; white-space:nowrap;">스팸 탐지</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155;">"지금 바로 클릭하면 100만원!"</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; white-space:nowrap; text-align:center;">스팸 🚨</td>
</tr>
<tr><td style="height:4px;"></td></tr>
<tr>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#FF6B00; white-space:nowrap;">주제 분류</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155;">"코스피가 오늘 2% 상승했다"</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; white-space:nowrap; text-align:center;">경제 📈</td>
</tr>
<tr><td style="height:4px;"></td></tr>
<tr>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#1681c4; white-space:nowrap;">혐오 표현 탐지</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155;">"..."</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; white-space:nowrap; text-align:center;">혐오/정상</td>
</tr>
<tr><td style="height:4px;"></td></tr>
<tr>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 14px; font-size:13px; font-weight:900; color:#FF6B00; white-space:nowrap;">언어 감지</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155;">"Hello, how are you?"</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:13px; color:#334155; white-space:nowrap; text-align:center;">영어 🇺🇸</td>
</tr>
</table>

</div>

<br>

<!-- 미세조정 패러다임 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🎓 BERT로 문장을 분류하는 방법: 미세조정</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">6-1에서 배운 <b>사전학습 + 미세조정</b> 패러다임을 기억하시나요?</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 16px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">미세조정 전체 흐름</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#a6e3a1;">사전학습된 BERT</span>
<span style="color:#6c7086;">(수십억 문장으로 언어를 이미 이해하는 상태)</span>
         <span style="color:#6c7086;">↓</span>
<span style="color:#89dceb;">미세조정 (Fine-tuning)</span>
<span style="color:#6c7086;">(내가 풀고 싶은 과제의 데이터로 짧게 추가 학습)</span>
         <span style="color:#6c7086;">↓</span>
<span style="color:#f9e2af; font-weight:900;">문장 분류 모델 완성</span></div>
</div>

<div style="background:#eef7ff; border:2px solid #c2e4ff; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#1681c4; font-weight:900;">🔑</span> 미세조정의 핵심은 <b style="color:#1681c4;">BERT 위에 분류기(Classifier) 하나만 얹는 것</b>입니다.
</div>

</div>

<br>

<!-- 모델 구조 5단계 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🏗️ 문장 분류 모델 구조</h2>

<div style="background:#eef7ff; border:2px solid #c2e4ff; padding:12px 16px; border-radius:12px; font-size:14px; color:#1681c4; font-weight:900; text-align:center; margin-bottom:14px;">
입력 문장: "이 영화 정말 최고였어요!"
</div>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px;">

<tr>
<td style="background:#FF6B00; color:#fff; padding:6px 12px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:top; width:80px; text-align:center;">STEP 1</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; line-height:1.8;">
<b>토크나이징 + 특수 토큰 추가</b><br>
<span style="font-family:Consolas,monospace; color:#1681c4;">[CLS] 이 영화 정말 최고였어요 ! [SEP]</span>
</td>
</tr>
<tr><td style="height:4px;"></td><td></td></tr>

<tr>
<td style="background:#1681c4; color:#fff; padding:6px 12px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:top; width:80px; text-align:center;">STEP 2</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; line-height:1.8;">
<b>BERT 12층 통과 (Self-Attention × 12)</b><br>
<span style="font-family:Consolas,monospace; font-size:12px; color:#64748b;">[CLS] 이 영화 정말 최고였어요 ! [SEP] → h₀ h₁ h₂ h₃ h₄ h₅ h₆ (각 768차원)</span>
</td>
</tr>
<tr><td style="height:4px;"></td><td></td></tr>

<tr>
<td style="background:#FF6B00; color:#fff; padding:6px 12px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:top; width:80px; text-align:center;">STEP 3</td>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; line-height:1.8;">
<b>CLS 벡터(h₀)만 꺼내기</b><br>
<span style="font-family:Consolas,monospace; font-size:12px; color:#FF6B00;">h₀ = [0.3, -0.1, 0.8, 0.5, ...] (768차원)</span>
</td>
</tr>
<tr><td style="height:4px;"></td><td></td></tr>

<tr>
<td style="background:#1681c4; color:#fff; padding:6px 12px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:top; width:80px; text-align:center;">STEP 4</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; line-height:1.8;">
<b>분류기(Linear Layer) 통과</b><br>
<span style="font-family:Consolas,monospace; font-size:12px; color:#64748b;">h₀ (768차원) → Linear → [긍정 점수, 부정 점수] → [2.8, 0.3]</span>
</td>
</tr>
<tr><td style="height:4px;"></td><td></td></tr>

<tr>
<td style="background:#0f172a; color:#c3e88d; padding:6px 12px; border-radius:8px; font-size:12px; font-weight:900; white-space:nowrap; vertical-align:top; width:80px; text-align:center;">STEP 5</td>
<td style="background:#f0fdf4; border:1px solid #86efac; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155; line-height:1.8;">
<b>Softmax로 확률 변환</b><br>
<span style="font-family:Consolas,monospace; font-size:12px; color:#16a34a;">[2.8, 0.3] → [0.93, 0.07] → 긍정 93% / 부정 7% → 긍정 ✅</span>
</td>
</tr>

</table>

</div>

<br>

<!-- 왜 CLS만 쓰나 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🤔 왜 CLS 벡터만 쓰나요? 다른 토큰은요?</h2>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">각 출력 벡터가 담는 정보</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#f9e2af; font-weight:900;">h₀ (CLS)</span>  <span style="color:#6c7086;">= 문장 전체 Self-Attention을 통해</span>
            <span style="color:#6c7086;">모든 단어 정보를 집약한 벡터</span>
            <span style="color:#a6e3a1;">→ 문장 전체의 의미를 대표</span>

<span style="color:#89dceb;">h₁ (이)</span>    <span style="color:#6c7086;">= "이"라는 단어 + 주변 문맥</span>
<span style="color:#89dceb;">h₂ (영화)</span>  <span style="color:#6c7086;">= "영화"라는 단어 + 주변 문맥</span>
<span style="color:#89dceb;">h₃ (정말)</span>  <span style="color:#6c7086;">= "정말"이라는 단어 + 주변 문맥</span>
<span style="color:#6c7086;">...</span></div>
</div>

<div style="background:#fff3eb; border:2px solid #ffd0b0; padding:13px 16px; border-radius:12px; font-size:14px; color:#334155; line-height:1.8;">
<span style="color:#FF6B00; font-weight:900;">💡</span> 문장 분류는 <b style="color:#FF6B00;">문장 전체</b>가 긍정인지 부정인지 판단하는 과제입니다.
개별 단어 벡터가 아니라 <b style="color:#FF6B00;">문장을 대표하는 CLS 벡터</b>를 쓰는 것이 자연스럽습니다.
</div>

</div>

<br>

<!-- 무엇이 학습되나 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">✏️ 미세조정에서 무엇이 학습되나요?</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">미세조정 시 업데이트되는 파라미터는 두 그룹입니다.</p>

<table style="width:100%; border-collapse: separate; border-spacing: 0 10px;">
<tr>
<td style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px; vertical-align:top;">
<div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">① BERT 전체 가중치 (12층 모든 파라미터)</div>
<div style="font-size:13px; color:#334155; line-height:1.7;">
이미 언어를 잘 알지만, 분류 과제에 맞게 <b style="color:#1681c4;">미세하게 조정</b>됩니다.<br>
학습률(learning rate)을 매우 작게 설정합니다. <span style="font-family:Consolas,monospace; background:#fff; border:1px solid #c2e4ff; padding:1px 6px; border-radius:4px;">2e-5 ~ 5e-5</span>
</div>
</td>
</tr>
<tr><td style="height:2px;"></td></tr>
<tr>
<td style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px; vertical-align:top;">
<div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:8px;">② 분류기 Linear Layer 가중치</div>
<div style="font-size:13px; color:#334155; line-height:1.7;">
새로 추가된 레이어이므로 <b style="color:#FF6B00;">처음부터 학습</b>됩니다.<br>
shape: <span style="font-family:Consolas,monospace; background:#fff; border:1px solid #ffd0b0; padding:1px 6px; border-radius:4px;">(768, 분류 클래스 수)</span> — 예: 긍정/부정이면 (768, 2)
</div>
</td>
</tr>
</table>

<div style="margin-top: 14px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align:center;">
사전학습된 언어 지식을 <b style="color:#1681c4;">최대한 보존하면서</b> 분류 과제를 위해 살짝 방향을 틉니다.
</div>

</div>

<br>

<!-- 미세조정 효과 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">📊 왜 미세조정이 강력한가요?</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">영화 리뷰 감정 분류 과제로 실험한 결과입니다.</p>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 16px;">

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; overflow:hidden;">
<div style="background:#64748b; padding:10px 16px;"><div style="font-size:13px; font-weight:900; color:#fff;">학습 데이터 1,000개</div></div>
<table style="width:100%; border-collapse: collapse;">
<tr>
<td style="padding:12px 16px; font-size:13px; color:#475569;">처음부터 학습</td>
<td style="padding:12px 16px; font-size:18px; font-weight:900; color:#dc2626; text-align:right;">72%</td>
</tr>
<tr>
<td style="padding:12px 16px; font-size:13px; color:#1681c4; font-weight:900;">BERT 미세조정</td>
<td style="padding:12px 16px; font-size:18px; font-weight:900; color:#16a34a; text-align:right;">92%</td>
</tr>
</table>
</div>

<div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; overflow:hidden;">
<div style="background:#64748b; padding:10px 16px;"><div style="font-size:13px; font-weight:900; color:#fff;">학습 데이터 100개</div></div>
<table style="width:100%; border-collapse: collapse;">
<tr>
<td style="padding:12px 16px; font-size:13px; color:#475569;">처음부터 학습</td>
<td style="padding:12px 16px; font-size:18px; font-weight:900; color:#dc2626; text-align:right;">55%</td>
</tr>
<tr>
<td style="padding:12px 16px; font-size:13px; color:#1681c4; font-weight:900;">BERT 미세조정</td>
<td style="padding:12px 16px; font-size:18px; font-weight:900; color:#16a34a; text-align:right;">85%</td>
</tr>
</table>
</div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8; text-align:center;">
<span style="color:#FF6B00; font-weight:900;">💡</span> BERT가 이미 언어를 깊이 이해하고 있기 때문에, <b style="color:#FF6B00;">소량의 데이터만으로도 강력한 성능</b>을 냅니다.
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;"><span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리</div>
<div style="display: grid; gap: 8px;">
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;"><b style="color:#FF6B00;">문장 분류</b>는 문장을 정해진 카테고리 중 하나로 분류하는 과제입니다 (감정, 스팸, 주제 등).</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">BERT는 CLS 출력 벡터(768차원) 위에 <b style="color:#FF6B00;">분류기 하나만 얹어</b> 미세조정합니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">미세조정 시 BERT 전체 가중치와 분류기 가중치 <b style="color:#FF6B00;">모두 함께</b> 업데이트됩니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">사전학습 덕분에 <b style="color:#FF6B00;">소량의 레이블 데이터만으로도</b> 높은 성능을 달성할 수 있습니다.</div>
</div>
</div>

</div>