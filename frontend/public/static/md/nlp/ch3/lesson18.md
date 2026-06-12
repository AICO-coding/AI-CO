<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
문장 임베딩 (Sentence Embedding)
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
문장 임베딩은
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">문장 전체를 하나의 벡터로 표현</span>
하는 방법입니다. 단어가 아닌 문장 전체의 의미와 문맥을 담습니다.
</p>

</div>

<br>

<!-- 남은 문제 카드 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🤔 단어 임베딩의 남은 문제
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
3-6에서 배운 단어 임베딩(Word2Vec)은 단어의 의미를 벡터로 표현할 수 있었습니다.<br>
하지만 여전히 해결되지 않은 문제가 있었습니다.
</p>

<div style="display: grid; gap: 14px; margin-top: 16px;">

<!-- 문제 1 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">문제 1. 같은 단어, 다른 의미</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-bottom: 12px;">
    <div style="background:#0f172a; border-radius:10px; padding:11px 12px; font-family:Consolas, monospace; font-size:12px; text-align:center; line-height:1.9;">
      <span style="color:#a6e3a1;">"나는 <span style="color:#ff5f57; font-weight:900;">배</span>가 고프다"</span><br>
      <span style="color:#6c7086;">→ 배 (신체 기관)</span>
    </div>
    <div style="background:#0f172a; border-radius:10px; padding:11px 12px; font-family:Consolas, monospace; font-size:12px; text-align:center; line-height:1.9;">
      <span style="color:#a6e3a1;">"<span style="color:#ff5f57; font-weight:900;">배</span>를 타고 섬에 갔다"</span><br>
      <span style="color:#6c7086;">→ 배 (선박)</span>
    </div>
    <div style="background:#0f172a; border-radius:10px; padding:11px 12px; font-family:Consolas, monospace; font-size:12px; text-align:center; line-height:1.9;">
      <span style="color:#a6e3a1;">"<span style="color:#ff5f57; font-weight:900;">배</span>가 달콤하게 익었다"</span><br>
      <span style="color:#6c7086;">→ 배 (과일)</span>
    </div>
  </div>

  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    Word2Vec은 "배"에 대해 <b style="color:#FF6B00;">단 하나의 벡터</b>만 만듭니다.<br>
    세 문장에서 "배"의 의미가 완전히 달라도, <b>항상 같은 숫자</b>로 표현됩니다.
  </div>
</div>

<!-- 문제 2 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">문제 2. 문장의 의미를 통째로 표현하지 못함</div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 12px;">
    <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; text-align:center; line-height:1.8;">
      "나는 고양이를 좋아한다"
    </div>
    <div style="background:#0f172a; border-radius:10px; padding:11px 14px; font-family:Consolas, monospace; font-size:13px; color:#a6e3a1; text-align:center; line-height:1.8;">
      "고양이는 나를 좋아한다"
    </div>
  </div>

  <div style="background:#ffffff; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px; font-size:14px; color:#334155; line-height:1.7;">
    단어 임베딩으로는 각 단어는 표현할 수 있지만,<br>
    <b style="color:#FF6B00;">문장 전체의 의미</b>를 하나의 벡터로 표현하기 어렵습니다.
  </div>
</div>

</div>

<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 이 두 가지 문제를 해결하는 것이 <b style="color:#FF6B00;">문장 임베딩(Sentence Embedding)</b>입니다.
</div>

</div>

<br>

<!-- 문장 임베딩이란 카드 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💡 문장 임베딩이란?
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
<b>문장 임베딩(Sentence Embedding)</b>은 <b style="color:#1681c4;">문장 전체를 하나의 벡터로 표현</b>하는 방법입니다.<br>
단어 하나하나가 아닌, <b>문장 전체의 의미와 문맥</b>을 하나의 숫자 묶음에 담습니다.
</p>

<div style="display: grid; gap: 12px; margin-top: 16px;">

  <!-- 단어 임베딩 -->
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:10px;">단어 임베딩 — 단어별로 따로따로 표현</div>
    <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"나는"</span>    → <span style="color:#89dceb;">[...]</span>
<span style="color:#a6e3a1;">"고양이를"</span> → <span style="color:#89dceb;">[...]</span>
<span style="color:#a6e3a1;">"좋아한다"</span> → <span style="color:#89dceb;">[...]</span>
<span style="color:#6c7086;">↓  단어별로 따로따로 표현</span></div>
  </div>

  <div style="text-align:center; font-size:22px; color:#94a3b8;">↓</div>

  <!-- 문장 임베딩 -->
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:10px;">문장 임베딩 — 문장 전체를 하나의 벡터로 표현</div>
    <div style="background:#0f172a; border-radius:10px; padding:12px 16px; font-family:Consolas, monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#a6e3a1;">"나는 고양이를 좋아한다"</span> → <span style="color:#ff5f57; font-weight:900;">[0.12, -0.34, 0.78, ...]</span>
<span style="color:#6c7086;">↓  문장 전체를 하나의 벡터로 표현</span></div>
  </div>

</div>

</div>

</div>