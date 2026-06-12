<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">Chapter 07 · GPT</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">GPT와 Transformer Decoder</h1>
<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
Transformer는 <b>인코더 + 디코더</b>로 구성됩니다.<br>
BERT가 인코더를, GPT가 <b style="color:#1681c4;">디코더</b>를 가져간 이유를 알아봅니다.
</p>
</div>

<br>

<!-- GPT는 어떤 구조 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">🏗️ GPT는 어떤 구조 위에 만들어졌나?</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
앞서 GPT의 이름 속에 <b style="color:#1681c4;">Transformer</b>가 들어있다고 했습니다. GPT를 제대로 이해하려면 Transformer가 무엇인지 먼저 알아야 합니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📄</span> Transformer는 2017년 구글이 발표한 논문 <b>"Attention is All You Need"</b>에서 처음 소개된 구조입니다.<br>
현재 거의 모든 최신 AI 언어 모델(<b style="color:#1681c4;">GPT, BERT, Claude</b> 등)의 기반이 됩니다.
</div>

</div>

<br>

<!-- 비유: 번역 회사 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">📬 비유로 이해하기: 번역 회사</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Transformer의 원래 목적은 <b>번역</b>이었습니다. "한국어 → 영어"처럼 한 언어를 다른 언어로 바꾸는 작업이죠.
</p>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; padding: 13px 17px; border-radius: 12px; font-size: 14px; color: #334155; text-align: center; margin: 14px 0;">
<b>번역 의뢰:</b> "나는 오늘 밥을 먹었다" → (영어로 번역해줘)
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">번역 회사에는 두 팀이 있습니다.</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">번역 회사 구조</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace;"><span style="color:#89dceb;">┌──────────────┐</span>       <span style="color:#f9e2af;">┌──────────────────────┐</span>
<span style="color:#89dceb;">│   인코더팀   │</span> <span style="color:#6c7086;">───▶</span> <span style="color:#f9e2af;">│      디코더팀        │</span>
<span style="color:#89dceb;">│  (Encoder)   │</span>       <span style="color:#f9e2af;">│     (Decoder)        │</span>
<span style="color:#89dceb;">│              │</span>       <span style="color:#f9e2af;">│                      │</span>
<span style="color:#89dceb;">│ 원문을 완전히 │</span>       <span style="color:#f9e2af;">│ 인코더의 이해를 바탕  │</span>
<span style="color:#89dceb;">│ 이해하는 팀  │</span>       <span style="color:#f9e2af;">│ 으로 번역문을 쓰는 팀 │</span>
<span style="color:#89dceb;">└──────────────┘</span>       <span style="color:#f9e2af;">└──────────────────────┘</span></div>
</div>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px;">
<tr>
<td style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#1681c4; white-space:nowrap; width:130px;">인코더 (Encoder)</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">입력 문장 전체를 읽고 의미를 파악</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">원문을 꼼꼼히 읽는 독해 전문가</td>
</tr>
<tr><td style="height:2px;"></td><td></td><td></td></tr>
<tr>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#FF6B00; white-space:nowrap;">디코더 (Decoder)</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">파악된 의미를 바탕으로 출력 문장 생성</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:12px; color:#475569;">독해한 내용을 토대로 글 쓰는 작가</td>
</tr>
</table>

</div>

<br>

<!-- 절반씩 가져갔다 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">✂️ BERT와 GPT는 이 구조에서 절반만 가져왔다</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
흥미로운 점은 BERT와 GPT 모두 Transformer 전체를 쓰지 않고 <b>절반씩 가져갔다</b>는 것입니다.
</p>

<div style="background-color: #1e1e2e; border-radius: 14px; overflow: hidden; margin: 14px 0;">
<div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
<div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
<div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
<span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">Transformer 분할</span>
</div>
<div style="padding: 18px; font-size: 13px; line-height: 2.4; overflow-x: auto; white-space: pre; font-family: 'JetBrains Mono', 'Consolas', monospace; text-align:center;"><span style="color:#cdd6f4;">Transformer 전체</span>
<span style="color:#89dceb;">┌─────────────┬─────────────────┐</span>
<span style="color:#89dceb;">│   인코더    │</span><span style="color:#f9e2af;">     디코더      │</span>
<span style="color:#89dceb;">└─────────────┴─────────────────┘</span>
      <span style="color:#6c7086;">↓                ↓</span>
   <span style="color:#89dceb;">BERT이 사용</span>     <span style="color:#f9e2af;">GPT가 사용</span>
  <span style="color:#89dceb;">(이해에 특화)</span>    <span style="color:#f9e2af;">(생성에 특화)</span></div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 14px;">

<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
<div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:8px;">BERT = 인코더만 사용</div>
<div style="font-size:13px; color:#334155; line-height:1.7;">문장 전체를 양방향으로 읽고 <b style="color:#1681c4;">"이해"</b>하는 데 최적화</div>
</div>

<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
<div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:8px;">GPT = 디코더만 사용</div>
<div style="font-size:13px; color:#334155; line-height:1.7;">앞 내용을 바탕으로 다음 내용을 <b style="color:#FF6B00;">"생성"</b>하는 데 최적화</div>
</div>

</div>

</div>

<br>

<!-- 왜 디코더를 선택했나 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">💡 왜 GPT는 디코더를 선택했나?</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
디코더의 특성을 생각해보면 자연스러운 선택이었습니다.
</p>

<table style="width:100%; border-collapse: separate; border-spacing: 0 8px; margin: 14px 0;">
<tr>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#64748b; white-space:nowrap; width:130px;">번역 디코더</td>
<td style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">"지금까지 번역한 내용을 보고, 다음에 올 단어를 써라"</td>
</tr>
<tr><td style="height:2px;"></td><td></td></tr>
<tr>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 16px; font-size:13px; font-weight:900; color:#FF6B00; white-space:nowrap;">GPT</td>
<td style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:12px 16px; font-size:13px; color:#334155;">"지금까지 나온 문장을 보고, 다음에 올 단어를 예측하라"</td>
</tr>
</table>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; color: #1681c4; font-weight: 900; text-align: center;">
두 역할이 구조적으로 완전히 같습니다.<br>
그래서 GPT는 Transformer Decoder 구조를 그대로 가져와 언어 생성에 활용했습니다.
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;"><span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리</div>
<div style="display: grid; gap: 8px;">
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">Transformer는 <b style="color:#FF6B00;">인코더 + 디코더</b> 두 부분으로 구성된 구조입니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;"><b style="color:#FF6B00;">인코더</b>: 입력을 읽고 이해 / <b style="color:#FF6B00;">디코더</b>: 이해를 바탕으로 출력 생성</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">BERT는 인코더만, <b style="color:#FF6B00;">GPT는 디코더만</b> 사용합니다.</div>
<div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">"다음 단어 예측"과 디코더의 역할이 <b style="color:#FF6B00;">딱 맞아 떨어집니다.</b></div>
</div>
</div>

</div>