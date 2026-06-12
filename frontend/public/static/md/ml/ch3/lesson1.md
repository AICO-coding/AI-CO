<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">활성화 함수가 없으면 어떤 문제가 생길까?</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    신경망은 층과 층 사이에서 선형 변환
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 8px; border-radius: 6px; font-family: monospace;">(w·X + b)</span>
    을 반복합니다. 그런데 선형 변환을 아무리 많이 쌓아도 결과는 여전히 선형입니다. 층을 10개 쌓든 100개 쌓든 수식으로 정리하면 결국
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 6px; font-family: monospace;">w·X + b</span>
    하나와 같습니다.<br><br>
    즉 층을 깊게 쌓는 의미가 사라집니다. 직선 하나로 표현할 수 없는 복잡한 패턴은 아무리 층을 늘려도 학습할 수 없습니다.<br><br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-weight: 700;">활성화 함수</span>
    는 각 층의 선형 변환 결과에 <b>비선형성</b>을 추가합니다. 이 덕분에 신경망이 층을 쌓을수록 더 복잡한 패턴을 학습할 수 있게 됩니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #fee2e2; border-radius: 12px; padding: 12px 15px; color: #991b1b;">
      ❌ <b>선형 변환만 쌓으면</b> — 층 3개: w3·(w2·(w1·X + b1) + b2) + b3 → 정리하면 결국 w·X + b 하나와 같음
    </div>
    <div style="background: #dcfce7; border-radius: 12px; padding: 12px 15px; color: #166534;">
      ✅ <b>활성화 함수를 추가하면</b> — 선형 변환 → 활성화 함수 → 선형 변환 → 활성화 함수 → ... → 비선형 패턴 학습 가능
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🧩 <b>비유</b> — 활성화 함수 없는 신경망 = 아무리 구부려도 직선인 막대 / 있는 신경망 = 자유롭게 구부러지는 곡선
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">활성화 함수 없이는 층을 아무리 쌓아도 선형 변환 하나와 같습니다. 비선형성이 있어야 복잡한 패턴을 학습할 수 있습니다.</div>
</div>
