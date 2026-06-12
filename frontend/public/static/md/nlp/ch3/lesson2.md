<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
텍스트 표현이란?
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
텍스트 표현 방법은 어떻게 발전해왔을까요?<br>
그리고 <b style="color:#1681c4;">벡터(Vector)</b>란 무엇인지 함께 알아봅니다.
</p>

</div>

<br>

<!-- 발전 과정 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
📚 텍스트 표현 방법의 발전
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
텍스트 표현 방법은 시간이 지나면서 점점 더 똑똑해졌습니다.<br>
이 챕터에서 이 발전 과정을 하나씩 따라가며 배웁니다.
</p>

<div style="display: grid; gap: 10px; margin-top: 18px;">

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">1세대</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:4px;">원-핫 인코딩 (One-Hot Encoding)</div>
      <div style="font-size:14px; color:#475569; line-height:1.7;">단어를 0과 1만으로 표현합니다. 단순하지만 <b style="color:#FF6B00;">의미를 담지 못합니다.</b></div>
    </div>
  </div>

  <div style="text-align:center; color:#94a3b8; font-size:18px; font-weight:900;">↓</div>

  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#0f172a; color:#c3e88d; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">2세대</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:4px;">단어 빈도 기반 (BoW, TF-IDF)</div>
      <div style="font-size:14px; color:#475569; line-height:1.7;">단어가 얼마나 자주 나오는지를 반영합니다. 그래도 <b style="color:#FF6B00;">의미는 여전히 부족합니다.</b></div>
    </div>
  </div>

  <div style="text-align:center; color:#94a3b8; font-size:18px; font-weight:900;">↓</div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">3세대</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:4px;">단어 임베딩 (Word2Vec, GloVe)</div>
      <div style="font-size:14px; color:#475569; line-height:1.7;">단어의 의미를 밀집된 벡터로 표현합니다. <b style="color:#1681c4;">유사한 단어는 비슷한 벡터값</b>을 가집니다.</div>
    </div>
  </div>

  <div style="text-align:center; color:#94a3b8; font-size:18px; font-weight:900;">↓</div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 20px; display:flex; gap:16px; align-items:flex-start;">
    <div style="flex-shrink:0; background:#1681c4; color:#fff; padding:5px 11px; border-radius:10px; font-size:12px; font-weight:900; white-space:nowrap;">4세대</div>
    <div>
      <div style="font-size:15px; font-weight:900; color:#1681c4; margin-bottom:4px;">문장 임베딩 (BERT, GPT 등)</div>
      <div style="font-size:14px; color:#475569; line-height:1.7;">단어뿐 아니라 <b style="color:#1681c4;">문맥까지 반영</b>한 표현입니다. 현재 가장 강력한 방법입니다.</div>
    </div>
  </div>

</div>

<div style="margin-top: 16px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 이 챕터에서 이 발전 과정을 하나씩 따라가며 배웁니다.
</div>

</div>

<br>

<!-- 벡터란 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔢 벡터(Vector)란?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
텍스트 표현에서 자주 등장하는 단어가 <b style="color:#1681c4;">벡터</b>입니다.<br>
벡터는 쉽게 말하면 <b>숫자들의 목록</b>입니다.
</p>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 18px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">벡터 예시</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.2; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">예시:</span>
<span style="color:#a6e3a1;">"사과"</span>  → <span style="color:#89dceb;">[1, 0, 0, 0, 0]</span>  <span style="color:#6c7086;">← 5개 숫자로 이루어진 벡터</span>
<span style="color:#a6e3a1;">"바나나"</span> → <span style="color:#89dceb;">[0, 1, 0, 0, 0]</span>
<span style="color:#a6e3a1;">"포도"</span>   → <span style="color:#89dceb;">[0, 0, 1, 0, 0]</span></div>
</div>

<p style="line-height: 1.8; color: #334155; font-size: 15px; margin: 0;">
숫자가 많아질수록(차원이 높아질수록) 더 많은 정보를 담을 수 있습니다.<br>
하지만 그만큼 <b style="color:#FF6B00;">계산도 복잡해집니다.</b>
</p>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;">
<span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리
</div>

<div style="display: grid; gap: 8px;">
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    컴퓨터는 숫자만 이해하므로, 텍스트를 <b style="color:#FF6B00;">숫자(벡터)로 변환</b>해야 합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    이 변환 방법을 <b style="color:#FF6B00;">텍스트 표현(Text Representation)</b>이라고 합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    좋은 표현은 단어의 <b style="color:#FF6B00;">의미와 유사성</b>을 숫자에 담아야 합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    표현 방법은 <b style="color:#FF6B00;">원-핫 인코딩 → BoW/TF-IDF → 단어 임베딩 → 문장 임베딩</b> 순으로 발전했습니다.
  </div>
</div>

</div>

</div>