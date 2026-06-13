<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">이진 분류기 전체 코드</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    이진 분류기는 출력이 <b>확률 1개</b>입니다. 마지막 Linear 층의 출력 뉴런을 1개로 설정하고, Sigmoid를 붙여서 0~1 사이 확률로 만듭니다.<br><br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-family: monospace; font-weight: 700;">nn.Sequential</span>
    을 쓰면 층을 순서대로 쌓는 것을 한 번에 정의할 수 있습니다. 데이터가 위에서 아래로 순서대로 통과합니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      class BinaryClassifier(nn.Module):<br>
      &nbsp;&nbsp;&nbsp;&nbsp;def __init__(self):<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;super().__init__()<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.net = nn.Sequential(<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nn.Linear(8, 16),&nbsp;&nbsp;&nbsp;# 입력 8 → 은닉 16<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nn.ReLU(),&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 은닉층 활성화<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nn.Linear(16, 1),&nbsp;&nbsp;&nbsp;# 은닉 16 → 출력 1<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nn.Sigmoid()&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 출력층 활성화 → 확률<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)<br><br>
      &nbsp;&nbsp;&nbsp;&nbsp;def forward(self, x):<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return self.net(x)
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      📐 <b>Linear(8, 16) 의미</b> — 입력 뉴런 8개 → 출력 뉴런 16개인 선형 층. 가중치 행렬 shape = (16, 8)
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎯 <b>마지막 층</b> — nn.Linear(16, 1) → nn.Sigmoid() → 확률 1개 출력. 이진 분류이므로 뉴런 1개
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">이진 분류 출력층 = Linear(n, 1) + Sigmoid(). Sequential로 층을 순서대로 쌓습니다.</div>
</div>
