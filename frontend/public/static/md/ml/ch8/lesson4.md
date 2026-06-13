<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">PyTorch로 다중 분류기 만들기</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    PyTorch의
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">nn.CrossEntropyLoss()</span>
    는 Softmax와 Loss 계산을 <b>한 번에 처리</b>합니다. 그래서 출력층에 Softmax를 직접 붙이지 않아도 됩니다. logit을 그대로 넣으면 됩니다.<br><br>
    레이블 y는 <b>클래스 번호(정수)</b>로 넣습니다. 이진 분류의 BCELoss와 달리 원-핫 인코딩 없이 정수 레이블 그대로 사용합니다.<br><br>
    나머지 학습 루프 구조는 이진 분류와 <b>완전히 같습니다.</b>
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 6px; border-radius: 6px; font-family: monospace; font-size: 12px;">zero_grad → 예측 → Loss → backward → step</span>
    순서 그대로입니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      nn.Sequential(<br>
      &nbsp;&nbsp;&nbsp;&nbsp;nn.Linear(8, 16),<br>
      &nbsp;&nbsp;&nbsp;&nbsp;nn.ReLU(),<br>
      &nbsp;&nbsp;&nbsp;&nbsp;nn.Linear(16, 3)&nbsp;&nbsp;&nbsp;# 클래스 3개 → 뉴런 3개<br>
      &nbsp;&nbsp;&nbsp;&nbsp;# Softmax 생략. CrossEntropyLoss가 내부에서 처리<br>
      )
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      criterion = nn.CrossEntropyLoss()<br>
      # logit을 그대로 넣어도 됨
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155; font-family: monospace; font-size: 12px;">
      y = torch.tensor([0, 2, 1, 0])  # 클래스 번호 정수. 원-핫 인코딩 불필요
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">CrossEntropyLoss = Softmax 내장. 출력층에 Softmax 생략. 레이블은 정수 그대로. 학습 루프는 이진 분류와 동일.</div>
</div>
