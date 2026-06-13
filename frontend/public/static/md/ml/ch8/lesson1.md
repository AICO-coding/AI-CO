<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">이진 분류에서 다중 분류로</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    이진 분류는 클래스가 2개입니다.
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-weight: 700;">다중 분류 (Multi-class Classification)</span>
    는 클래스가 3개 이상입니다. 손글씨 숫자 인식(0~9, 클래스 10개), 이미지가 고양이/강아지/새 중 무엇인지 맞추는 것이 다중 분류입니다.<br><br>
    이진 분류와 다른 점은 두 가지입니다.<br>
    첫째, <b>출력층 뉴런 수</b>가 클래스 수만큼 늘어납니다. 클래스 10개면 출력 뉴런 10개입니다.<br>
    둘째, <b>출력층 활성화 함수</b>가 Sigmoid 대신
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Softmax</span>
    로 바뀝니다.<br><br>
    Loss 함수도 BCELoss 대신
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 4px; font-weight: 700;">CrossEntropyLoss</span>
    를 씁니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      🔢 <b>다중 분류 예시</b> — 손글씨 숫자(0~9) → 클래스 10개 → 출력 뉴런 10개 → Softmax
    </div>
    <div style="background: #f1f5f9; border-radius: 8px; padding: 10px 14px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      # 이진 분류<br>
      nn.Linear(16, 1) + Sigmoid<br><br>
      # 다중 분류 (N = 클래스 수)<br>
      nn.Linear(16, N) + Softmax
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; color: #334155;">
      ⚖️ <b>Loss 함수</b> — 이진 분류: nn.BCELoss() &nbsp;/&nbsp; 다중 분류: nn.CrossEntropyLoss()
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">다중 분류 = 출력 뉴런 N개 + Softmax + CrossEntropyLoss. 클래스 수만큼 출력 뉴런이 필요합니다.</div>
</div>
