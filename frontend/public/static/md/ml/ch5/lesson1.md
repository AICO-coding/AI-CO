<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">PyTorch 신경망의 기본 구조</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    PyTorch에서 신경망은
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-weight: 700;">nn.Module</span>
    을 상속한 클래스로 만듭니다. 처음 보면 낯설지만 구조는 항상 같습니다.
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-weight: 700;">__init__</span>
    과
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-weight: 700;">forward</span>
    , 두 메서드만 기억하면 됩니다.<br><br>
    <b>__init__</b>에는 모델에서 쓸 층(layer)을 정의합니다. 어떤 층을 쓸지 목록을 만드는 것입니다.<br>
    <b>forward</b>에는 데이터가 층을 통과하는 순서를 정의합니다. 입력 x가 들어와서 어떤 순서로 층을 거쳐 출력되는지 적습니다.<br><br>
    모델을 호출하면 forward가 자동으로 실행됩니다.
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 8px; border-radius: 4px; font-family: monospace;">model(x)</span>
    라고 쓰면 내부적으로
    <span style="background: #fff; border: 1px solid #e2e8f0; color: #334155; padding: 2px 8px; border-radius: 4px; font-family: monospace;">model.forward(x)</span>
    가 호출됩니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 8px; padding: 10px 14px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      class MyModel(nn.Module):<br>
      &nbsp;&nbsp;&nbsp;&nbsp;def __init__(self):<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;super().__init__()<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 층 정의<br><br>
      &nbsp;&nbsp;&nbsp;&nbsp;def forward(self, x):<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 데이터 흐름 정의<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return x
    </div>
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      🏗️ <b>__init__ 역할</b> — 층을 정의하는 곳. 어떤 층을 쓸지 선언만 합니다
    </div>
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      ➡️ <b>forward 역할</b> — 데이터가 흐르는 순서를 정의하는 곳. x가 층을 거쳐 출력까지 가는 경로입니다
    </div>
    <div style="background: #f1f5f9; border-radius: 8px; padding: 10px 14px; color: #334155; font-family: monospace; font-size: 12px;">
      pred = model(x)  # 내부적으로 forward(x)가 실행됨
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">__init__ = 층 목록 정의 / forward = 데이터 흐름 정의. model(x) 호출 시 forward(x)가 자동 실행됩니다.</div>
</div>
