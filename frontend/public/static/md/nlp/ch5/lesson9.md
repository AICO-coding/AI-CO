<div style="max-width: 920px; margin: 0 auto; font-family: 'Nunito', 'Pretendard', 'Malgun Gothic', sans-serif; color: #0f172a;">

<!-- 제목 영역 -->
<div style="background: linear-gradient(135deg, #eef7ff 0%, #f8fbff 100%); border: 2px solid #c2e4ff; border-radius: 18px; padding: 28px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.06);">

<div style="display: inline-block; background: #0f172a; color: #c3e88d; padding: 5px 12px; border-radius: 999px; font-size: 12px; font-weight: 900; letter-spacing: .2px; margin-bottom: 12px;">
Chapter 05 · Transformer
</div>

<h1 style="margin: 0 0 12px 0; font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #0f172a;">
Add &amp; Norm — 잔차 연결
</h1>

<p style="margin: 0; line-height: 1.8; font-size: 15px; color: #334155;">
깊은 네트워크에서 발생하는 기울기 소실 문제를
<b style="color:#1681c4;">잔차 연결(Residual Connection)</b>이 어떻게 해결하는지 알아봅니다.
</p>

</div>

<br>

<!-- Encoder 구조 다시 보기 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔍 Encoder 레이어 구조 다시 보기
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
5-4에서 Encoder 레이어는 이 순서로 구성된다고 배웠습니다.
</p>

<div style="display: grid; gap: 0; margin: 16px 0;">
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; text-align:center; font-size:14px; font-weight:900; color:#475569;">Multi-Head Attention</div>
  <div style="text-align:center; color:#94a3b8; font-size:18px; font-weight:900; margin:3px 0;">↓</div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:12px 16px; text-align:center; font-size:14px; font-weight:900; color:#FF6B00;">★ Add &amp; Norm &nbsp;<span style="color:#94a3b8; font-size:12px; font-weight:400;">← 지금 배우는 단계</span></div>
  <div style="text-align:center; color:#94a3b8; font-size:18px; font-weight:900; margin:3px 0;">↓</div>
  <div style="background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; padding:12px 16px; text-align:center; font-size:14px; font-weight:900; color:#475569;">Feed Forward Network</div>
  <div style="text-align:center; color:#94a3b8; font-size:18px; font-weight:900; margin:3px 0;">↓</div>
  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:12px; padding:12px 16px; text-align:center; font-size:14px; font-weight:900; color:#FF6B00;">★ Add &amp; Norm &nbsp;<span style="color:#94a3b8; font-size:12px; font-weight:400;">← 여기도 등장</span></div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 4px;">
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:12px 14px; text-align:center;">
    <div style="font-size:15px; font-weight:900; color:#1681c4;">Add</div>
    <div style="font-size:13px; color:#475569; margin-top:4px;">더한다</div>
  </div>
  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:12px; padding:12px 14px; text-align:center;">
    <div style="font-size:15px; font-weight:900; color:#1681c4;">Norm</div>
    <div style="font-size:13px; color:#475569; margin-top:4px;">정규화한다</div>
  </div>
</div>

</div>

<br>

<!-- 깊은 레이어의 문제 -->
<div style="background-color: #ffffff; border: 2px solid #ffd0b0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
😰 레이어가 깊어질수록 생기는 문제
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
Transformer는 Encoder 레이어가 <b>6번 쌓입니다.</b> BERT 같은 모델은 12층, 24층까지 쌓기도 합니다.<br>
레이어를 많이 쌓을수록 학습할 때 심각한 문제가 생깁니다.
</p>

<!-- 문제 1 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px; margin-bottom:12px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">문제 1. 기울기 소실 (Vanishing Gradient)</div>
  <p style="font-size:14px; color:#334155; line-height:1.7; margin: 0 0 12px 0;">
  딥러닝은 "예측이 틀렸을 때 얼마나 틀렸는지"를 역방향으로 전달하며 학습합니다.<br>
  이 신호를 <b>기울기(Gradient)</b>라고 하는데, 레이어가 깊어질수록 <b style="color:#FF6B00;">점점 약해집니다.</b>
  </p>
  <div style="background-color: #1e1e2e; border-radius: 12px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace;">
    <div style="padding: 14px 18px; font-size: 13px; line-height: 2.2; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">레이어 6  →  레이어 5  →  레이어 4  →  레이어 3  →  레이어 2  →  레이어 1</span>
<span style="color:#a6e3a1;">신호 1.0</span>     <span style="color:#a6e3a1;">신호 0.5</span>     <span style="color:#f9e2af;">신호 0.25</span>    <span style="color:#f38ba8;">신호 0.12</span>    <span style="color:#f38ba8;">신호 0.06</span>    <span style="color:#f38ba8;">신호 0.03</span>
                                                               <span style="color:#f38ba8;">↑</span>
                                                     <span style="color:#f38ba8;">거의 0에 가까워짐 → 학습이 안 됨!</span></div>
  </div>
</div>

<!-- 문제 2 -->
<div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:18px 20px;">
  <div style="font-size:15px; font-weight:900; color:#FF6B00; margin-bottom:12px;">문제 2. 정보 손실</div>
  <p style="font-size:14px; color:#334155; line-height:1.7; margin: 0 0 12px 0;">
  레이어를 통과할 때마다 벡터가 변환됩니다. 변환을 거듭하다 보면 <b style="color:#FF6B00;">원래 입력이 가진 중요한 정보</b>가 사라질 수 있습니다.
  </p>
  <div style="background-color: #1e1e2e; border-radius: 12px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace;">
    <div style="padding: 14px 18px; font-size: 13px; line-height: 2.2; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">입력: "나는" 벡터</span>  <span style="color:#a6e3a1;">[0.2, 0.5, 0.8, ...]</span>
    <span style="color:#89dceb;">↓ Layer 1 변환</span>
                   <span style="color:#cba6f7;">[0.3, 0.7, 0.1, ...]</span>
    <span style="color:#89dceb;">↓ Layer 2 변환</span>
                   <span style="color:#cba6f7;">[0.9, 0.2, 0.5, ...]</span>
    <span style="color:#89dceb;">↓ Layer 3 변환</span>
                   <span style="color:#f38ba8;">[0.1, 0.1, 0.9, ...]</span>  <span style="color:#6c7086;">← 원래 정보가 얼마나 남아있을까?</span></div>
  </div>
</div>

</div>

<br>

<!-- 잔차 연결 해결책 -->
<div style="background-color: #ffffff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
💡 해결책: 잔차 연결 (Residual Connection)
</h2>

<p style="line-height: 1.8; color: #334155; font-size: 15px;">
아이디어는 매우 단순합니다.
</p>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 15px 17px; border-radius: 12px; font-size: 15px; font-weight: 900; line-height: 1.8; text-align: center; margin: 14px 0;">
<span style="color: #1681c4;">"변환 결과"에 "원래 입력"을 그냥 더한다.</span>
</div>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 16px; overflow: hidden; font-family: 'JetBrains Mono', 'Consolas', monospace; box-shadow: 0 8px 20px rgba(15,23,42,.18); margin: 16px 0;">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 11px 15px; display: flex; align-items: center; gap: 6px;">
    <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
    <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
    <span style="color: #8b8bc7; margin-left: 8px; font-size: 12px;">잔차 연결 수식</span>
  </div>
  <div style="padding: 18px; color: #cdd6f4; font-size: 13px; line-height: 2.4; font-family: 'JetBrains Mono', 'Consolas', monospace; overflow-x: auto; white-space: pre;">
<span style="color:#6c7086;">출력 = 원래 입력 + 레이어(원래 입력)</span>
     <span style="color:#6c7086;">=</span> <span style="color:#a6e3a1;">X</span>         <span style="color:#6c7086;">+</span> <span style="color:#cba6f7;">Layer(X)</span></div>
</div>

<!-- 두 가지 비유 -->
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 14px;">

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">✏️ 비유: 선생님의 첨삭</div>
    <div style="display:grid; gap:6px; font-size:13px; color:#334155; line-height:1.7;">
      <div style="background:#fff; border:1px solid #c2e4ff; border-radius:8px; padding:8px 10px;">
        학생 원본 글 = <b style="color:#a6e3a1;">X</b>
      </div>
      <div style="background:#fff; border:1px solid #c2e4ff; border-radius:8px; padding:8px 10px;">
        선생님 수정 사항 = <b style="color:#cba6f7;">Layer(X)</b>
      </div>
      <div style="background:#fff; border:2px solid #c2e4ff; border-radius:8px; padding:8px 10px; font-weight:900; color:#1681c4;">
        최종 = <b style="color:#a6e3a1;">X</b> + <b style="color:#cba6f7;">Layer(X)</b>
      </div>
    </div>
    <div style="margin-top:8px; font-size:12px; color:#475569; line-height:1.7;">
      원본을 완전히 새로 쓰는 대신,<br><b>원본은 그대로 두고 수정 사항만 얹습니다.</b>
    </div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">🛣️ 비유: 지름길(고속도로)</div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 12px; font-family:Consolas,monospace; font-size:12px; line-height:2; color:#cdd6f4; overflow-x:auto; white-space:pre; margin-bottom:8px;">
<span style="color:#a6e3a1;">X</span> ──────────────────────→ <span style="color:#a6e3a1;">X</span>
<span style="color:#6c7086;">↓</span>                           <span style="color:#6c7086;">↓</span>
<span style="color:#cba6f7;">[Layer]</span> → <span style="color:#cba6f7;">Layer(X)</span>       <span style="color:#89dceb;">+</span>
                             <span style="color:#6c7086;">↓</span>
                     <span style="color:#f9e2af;">X + Layer(X)</span></div>
    <div style="font-size:12px; color:#475569; line-height:1.7;">
      <b>일반 경로</b>와 <b>지름길</b> 두 갈래로 흐릅니다.
    </div>
  </div>

</div>

<div style="margin-top:14px; display:grid; gap:8px;">
  <div style="background:#eef7ff; border-left:4px solid #1681c4; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    중요한 원본 정보가 <b style="color:#1681c4;">사라지지 않습니다.</b>
  </div>
  <div style="background:#eef7ff; border-left:4px solid #1681c4; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    지름길 덕분에 기울기 신호가 깊은 레이어까지 <b style="color:#1681c4;">약해지지 않고 전달</b>됩니다.
  </div>
</div>

</div>

<br>

<!-- 잔차 연결 유무 비교 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
🔍 잔차 연결이 없을 때 vs 있을 때
</h2>

<div style="display: grid; gap: 12px; margin-top: 14px;">

  <div style="background:#fff3eb; border:2px solid #ffd0b0; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#FF6B00; margin-bottom:10px;">❌ 잔차 연결 없을 때</div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">L6    ← L5    ← L4    ← L3    ← L2    ← L1</span>
<span style="color:#f38ba8;">0.001   0.01    0.05    0.15    0.4     1.0</span>
<span style="color:#f38ba8;">↑ 거의 0 → 학습 실패</span></div>
  </div>

  <div style="background:#eef7ff; border:2px solid #c2e4ff; border-radius:14px; padding:16px 18px;">
    <div style="font-size:14px; font-weight:900; color:#1681c4; margin-bottom:10px;">✅ 잔차 연결 있을 때</div>
    <div style="background:#0f172a; border-radius:8px; padding:10px 14px; font-family:Consolas,monospace; font-size:13px; line-height:2; overflow-x:auto; white-space:pre;">
<span style="color:#6c7086;">각 레이어에 지름길이 있어 기울기가 직접 전달됨</span>
<span style="color:#a6e3a1;">0.9     0.9     0.9     0.9     0.9     1.0</span>
<span style="color:#a6e3a1;">↑ 충분히 큰 값 → 모든 레이어가 잘 학습됨</span></div>
  </div>

</div>

</div>

<br>

<!-- 효과 정리 -->
<div style="background-color: #ffffff; border: 2px solid #e2e8f0; border-radius: 18px; padding: 26px 30px; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<h2 style="margin-top: 0; color: #0f172a; font-weight: 900; letter-spacing: -0.4px;">
✅ 잔차 연결의 효과 정리
</h2>

<div style="overflow-x: auto; margin: 14px 0;">
<table style="width:100%; border-collapse:collapse; font-size:14px;">
  <thead>
    <tr style="background:#0f172a; color:#c3e88d;">
      <th style="padding:10px 14px; text-align:left; font-weight:900;">문제</th>
      <th style="padding:10px 14px; text-align:left; font-weight:900;">잔차 연결로 해결되는 방식</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">기울기 소실</td>
      <td style="padding:10px 14px; color:#334155;">지름길로 기울기가 직접 전달됨</td>
    </tr>
    <tr style="background:#f8fafc; border-bottom:1px solid #e2e8f0;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">정보 손실</td>
      <td style="padding:10px 14px; color:#334155;">원본 입력이 항상 출력에 포함됨</td>
    </tr>
    <tr style="background:#fff;">
      <td style="padding:10px 14px; font-weight:900; color:#FF6B00;">학습 불안정</td>
      <td style="padding:10px 14px; color:#334155;">레이어가 "원본+수정"만 학습하면 돼 안정적</td>
    </tr>
  </tbody>
</table>
</div>

<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">💡 핵심 직관:</span><br>
레이어는 "처음부터 새로운 표현을 만든다"가 아니라<br>
<b style="color:#1681c4;">"원래 표현에서 무엇을 보완할지만 학습한다"</b>고 봐도 됩니다.<br>
이게 훨씬 쉬운 학습 문제입니다.
</div>

</div>

<br>

<!-- 핵심 정리 -->
<div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 18px 20px; border-radius: 16px; color: #0f172a; box-shadow: 0 8px 20px rgba(15,23,42,.05);">

<div style="font-size: 15px; font-weight: 900; margin-bottom: 10px;">
<span style="color: #FF6B00; font-size: 18px;">⚡</span> 핵심 정리
</div>

<div style="display: grid; gap: 8px;">
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    레이어를 여러 겹 쌓으면 <b style="color:#FF6B00;">기울기 소실</b>과 <b style="color:#FF6B00;">정보 손실</b> 문제가 생깁니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    잔차 연결은 <b style="color:#FF6B00;">"원래 입력 + 레이어 출력"</b>을 더해서 이 문제를 해결합니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    정보가 <b style="color:#FF6B00;">일반 경로</b>와 <b style="color:#FF6B00;">지름길</b> 두 갈래로 동시에 흐릅니다.
  </div>
  <div style="background:#fff; border-left:4px solid #FF6B00; padding:10px 14px; border-radius:0 8px 8px 0; font-size:14px; color:#334155; line-height:1.7;">
    덕분에 Transformer처럼 <b style="color:#FF6B00;">깊은 네트워크</b>도 안정적으로 학습할 수 있습니다.
  </div>
</div>

<div style="margin-top:12px; background-color: #eef7ff; border: 2px solid #c2e4ff; padding: 13px 16px; border-radius: 12px; font-size: 14px; color: #334155; line-height: 1.8;">
<span style="color: #1681c4; font-weight: 900;">📌</span> 다음 페이지에서는 Add 다음에 오는 <b style="color:#1681c4;">Norm(Layer Normalization)</b>을 배웁니다.
</div>

</div>

</div>