<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">
<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 03 · 텍스트 표현
</div>
<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
단어 임베딩 (Word Embedding)
</h1>
<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
단어 임베딩은 단어를
<span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 7px; border-radius: 6px; font-weight: 900;">의미가 담긴 숫자 공간에 배치</span>
하는 방법입니다. 비슷한 단어는 가까이, 다른 단어는 멀리 위치합니다.
</p>
</div>
<br>
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🚧 지금까지 방법들의 공통 한계
</h2>
<p style="line-height: 1.8; color: #334155; font-size: 15px;">
원-핫 인코딩, BoW, TF-IDF 모두 같은 근본적인 문제를 가지고 있습니다.
</p>
<div style="background-color: #1e1e2e; border-radius: 14px; padding: 14px 20px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; line-height: 2.2; margin: 14px 0; overflow-x: auto; white-space: pre;">
<span style="color:#a6e3a1;">"강아지"</span> <span style="color:#6c7086;">= [0, 0, </span><span style="color:#ff5f57;">1</span><span style="color:#6c7086;">, 0, 0, 0, 0 ...]</span>
<span style="color:#a6e3a1;">"개"</span>     <span style="color:#6c7086;">= [0, 0, 0, </span><span style="color:#ff5f57;">1</span><span style="color:#6c7086;">, 0, 0, 0 ...]</span>
<span style="color:#a6e3a1;">"고양이"</span> <span style="color:#6c7086;">= [0, 0, 0, 0, </span><span style="color:#ff5f57;">1</span><span style="color:#6c7086;">, 0, 0 ...]</span>
<span style="color:#a6e3a1;">"자동차"</span> <span style="color:#6c7086;">= [0, 0, 0, 0, 0, </span><span style="color:#ff5f57;">1</span><span style="color:#6c7086;">, 0 ...]</span></div>
<p style="line-height: 1.8; color: #334155; font-size: 15px; margin-bottom: 14px;">
이 표현으로는 이런 사실을 전혀 알 수 없습니다.
</p>
<div style="display: grid; gap: 8px; margin-bottom: 14px;">
<div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:11px 14px;">
<div style="font-size:20px;">🐶</div>
<div style="font-size:14px; color:#334155; line-height:1.7;"><b style="color:#1681c4;">"강아지"</b>와 <b style="color:#1681c4;">"개"</b>는 거의 같은 의미 → 유사도 높음</div>
</div>
<div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:11px 14px;">
<div style="font-size:20px;">🐾</div>
<div style="font-size:14px; color:#334155; line-height:1.7;"><b style="color:#475569;">"강아지"</b>와 <b style="color:#475569;">"고양이"</b>는 비슷한 종류의 동물 → 어느 정도 유사</div>
</div>
<div style="display:grid; grid-template-columns:auto 1fr; gap:12px; align-items:center; background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:11px 14px;">
<div style="font-size:20px;">🚗</div>
<div style="font-size:14px; color:#334155; line-height:1.7;"><b style="color:#FF6B00;">"강아지"</b>와 <b style="color:#FF6B00;">"자동차"</b>는 완전히 다른 종류 → 유사도 낮음</div>
</div>
</div>
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 모든 단어 쌍의 거리가 똑같이 측정되어, <b style="color:#FF6B00;">의미 관계를 전혀 담지 못합니다.</b>
</div>
</div>
<br>
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🗺️ 임베딩의 핵심 아이디어: 의미를 공간에 담자
</h2>
<p style="line-height: 1.8; color: #334155; font-size: 15px;">
<b>임베딩(Embedding)</b>은 단어를 <b style="color:#1681c4;">의미가 담긴 좌표 공간에 배치</b>하는 방법입니다.<br>
비슷한 의미의 단어는 공간에서 가까이, 다른 의미의 단어는 멀리 배치됩니다.
</p>

<div style="background-color: #0f172a; border-radius: 14px; padding: 22px 24px; margin: 16px 0; overflow-x: auto;">
<div style="font-size: 11px; color: #94a3b8; margin-bottom: 14px; font-family: Consolas, monospace;">
[2차원으로 단순화한 예시]
</div>

<div style="position: relative; min-width: 620px; height: 360px; background:
  linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
  linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px);
  background-size: 40px 40px;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;">

  <div style="position:absolute; left:70px; top:42px; padding:6px 10px; border-radius:999px; background:rgba(166,227,161,0.16); color:#a6e3a1; font-family:Consolas, monospace; font-size:13px; font-weight:900;">행복 ★</div>
  <div style="position:absolute; left:165px; top:50px; padding:6px 10px; border-radius:999px; background:rgba(166,227,161,0.16); color:#a6e3a1; font-family:Consolas, monospace; font-size:13px; font-weight:900;">기쁨 ★</div>
  <div style="position:absolute; left:105px; top:105px; padding:6px 10px; border-radius:999px; background:rgba(166,227,161,0.16); color:#a6e3a1; font-family:Consolas, monospace; font-size:13px; font-weight:900;">웃음 ★</div>

  <div style="position:absolute; left:72px; top:218px; padding:6px 10px; border-radius:999px; background:rgba(137,220,235,0.14); color:#89dceb; font-family:Consolas, monospace; font-size:13px; font-weight:900;">슬픔 ★</div>
  <div style="position:absolute; left:45px; top:265px; padding:6px 10px; border-radius:999px; background:rgba(137,220,235,0.14); color:#89dceb; font-family:Consolas, monospace; font-size:13px; font-weight:900;">우울 ★</div>

  <div style="position:absolute; left:288px; top:220px; padding:6px 10px; border-radius:999px; background:rgba(255,107,0,0.18); color:#ffd0b0; font-family:Consolas, monospace; font-size:13px; font-weight:900;">강아지 ★</div>
  <div style="position:absolute; left:322px; top:265px; padding:6px 10px; border-radius:999px; background:rgba(255,107,0,0.18); color:#ffd0b0; font-family:Consolas, monospace; font-size:13px; font-weight:900;">개 ★</div>
  <div style="position:absolute; left:292px; top:308px; padding:6px 10px; border-radius:999px; background:rgba(255,107,0,0.18); color:#ffd0b0; font-family:Consolas, monospace; font-size:13px; font-weight:900;">고양이 ★</div>

  <div style="position:absolute; left:470px; top:135px; padding:6px 10px; border-radius:999px; background:rgba(148,163,184,0.16); color:#cbd5e1; font-family:Consolas, monospace; font-size:13px; font-weight:900;">자동차 ★</div>

  <div style="position:absolute; left:52px; top:24px; width:190px; height:120px; border:1px dashed rgba(166,227,161,0.35); border-radius:20px;"></div>
  <div style="position:absolute; left:32px; top:204px; width:135px; height:110px; border:1px dashed rgba(137,220,235,0.35); border-radius:20px;"></div>
  <div style="position:absolute; left:270px; top:204px; width:135px; height:140px; border:1px dashed rgba(255,107,0,0.35); border-radius:20px;"></div>

</div>
</div>

<div style="display: grid; gap: 8px; margin-top: 4px;">
<div style="background:#eef7ff; border:1px solid #c2e4ff; border-radius:10px; padding:10px 14px; font-size:14px; color:#334155; line-height:1.7;">
<b style="color:#1681c4;">★ "행복", "기쁨", "웃음"</b>은 서로 가까이 위치 → 유사한 의미
</div>
<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 14px; font-size:14px; color:#334155; line-height:1.7;">
<b style="color:#475569;">★ "슬픔", "우울"</b>은 서로 가까이, "행복"과는 멀리 → 반대 의미
</div>
<div style="background:#fff3eb; border:1px solid #ffd0b0; border-radius:10px; padding:10px 14px; font-size:14px; color:#334155; line-height:1.7;">
<b style="color:#FF6B00;">★ "강아지", "개", "고양이"</b>는 서로 가까이 → 동물이라는 공통점
</div>
</div>
<div style="margin-top: 14px; background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #FF6B00; font-weight: 900;">💡</span> 임베딩은 단어를 <b style="color:#FF6B00;">의미의 지도 위에 올려놓는 것</b>입니다.
</div>
</div>
<br>
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">
<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔢 벡터로 표현한다는 것
</h2>
<p style="line-height: 1.8; color: #334155; font-size: 15px;">
임베딩에서 각 단어는 <b style="color:#1681c4;">여러 개의 숫자(벡터)</b>로 표현됩니다.
</p>
<div style="background-color: #1e1e2e; border-radius: 14px; padding: 16px 20px; font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: 13px; line-height: 2.2; margin: 14px 0; overflow-x: auto; white-space: pre;">
<span style="color:#a6e3a1;">"강아지"</span> <span style="color:#6c7086;">=</span> <span style="color:#89dceb;">[ 0.2,   0.8,  -0.1,   0.5,   0.3, ...]</span>  <span style="color:#6c7086;">← 수백 개의 숫자</span>
<span style="color:#a6e3a1;">"개"</span>     <span style="color:#6c7086;">=</span> <span style="color:#89dceb;">[ 0.21,  0.79, -0.09,  0.51,  0.29, ...]</span> <span style="color:#6c7086;">← 거의 비슷한 숫자</span>
<span style="color:#a6e3a1;">"자동차"</span> <span style="color:#6c7086;">=</span> <span style="color:#ff5f57;">[-0.8,   0.1,   0.9,  -0.3,   0.6, ...]</span>  <span style="color:#6c7086;">← 완전히 다른 숫자</span></div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 4px;">
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:14px 16px;">
<div style="font-size:13px; font-weight:900; color:#FF6B00; margin-bottom:6px;">❌ 사람이 직접 정하지 않는다</div>
<div style="font-size:13px; color:#475569; line-height:1.7;">각 숫자 하나하나가 어떤 의미를 나타내는지 사람이 직접 정하지 않습니다.</div>
</div>
<div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:14px 16px;">
<div style="font-size:13px; font-weight:900; color:#1681c4; margin-bottom:6px;">✅ 모델이 스스로 학습한다</div>
<div style="font-size:13px; color:#475569; line-height:1.7;">대량의 텍스트를 학습하면서 <b>모델이 스스로 숫자를 정합니다.</b></div>
</div>
</div>
</div>
</div>