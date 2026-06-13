<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Sigmoid vs ReLU — 어디에 쓰는가?</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    두 함수는 <b>쓰이는 위치가 다릅니다.</b><br><br>
    <b>은닉층</b>에는
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-weight: 700;">ReLU</span>
    를 씁니다. 기울기 소실 문제가 적고 계산이 빠르기 때문입니다. 층을 깊게 쌓을수록 ReLU가 유리합니다.<br><br>
    <b>이진 분류의 출력층</b>에는
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 6px; font-weight: 700;">Sigmoid</span>
    를 씁니다. 출력이 0~1 사이의 확률로 나와야 하기 때문입니다. ReLU는 음수를 0으로 만들고 양수는 그대로 통과시키기 때문에 확률로 쓸 수 없습니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🧠 <b>은닉층</b> → ReLU 사용. 기울기 소실 없음, 계산 빠름
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🎯 <b>이진 분류 출력층</b> → Sigmoid 사용. 출력이 0~1 → 클래스 1일 확률로 해석 가능
    </div>
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      nn.ReLU()     # 은닉층<br>
      nn.Sigmoid()  # 이진 분류 출력층
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">은닉층 → ReLU (기울기 소실 없음) / 이진 분류 출력층 → Sigmoid (0~1 확률 출력). 위치에 따라 함수가 다릅니다.</div>
</div>
