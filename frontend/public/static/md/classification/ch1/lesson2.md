<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">클래스(Class)란?</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-weight: 700;">클래스 (Class)</span>
    — 모델이 예측할 수 있는 <b>범주의 목록</b>입니다. 정답으로 나올 수 있는 선택지들입니다.<br><br>
    코드에서는 클래스를 숫자로 표현합니다.<br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 6px; font-family: monospace; font-size: 13px;">0</span> = <b>음성 (Negative)</b> &nbsp;&nbsp;
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 6px; font-family: monospace; font-size: 13px;">1</span> = <b>양성 (Positive)</b><br><br>
    ⚠️ <b>양성이 꼭 좋은 의미는 아닙니다.</b> 단지 <b>'우리가 탐지하려는 대상'</b>을 양성으로 정의하는 관례입니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      📧 <b>스팸 분류</b> — 클래스 = [0, 1] →
      <span style="background: #f1f5f9; padding: 1px 6px; border-radius: 6px; font-family: monospace;">0</span> = 정상 &nbsp;
      <span style="background: #f1f5f9; padding: 1px 6px; border-radius: 6px; font-family: monospace;">1</span> = 스팸
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🏥 <b>암 진단</b> — 클래스 = [0, 1] →
      <span style="background: #f1f5f9; padding: 1px 6px; border-radius: 6px; font-family: monospace;">0</span> = 양성 종양 &nbsp;
      <span style="background: #f1f5f9; padding: 1px 6px; border-radius: 6px; font-family: monospace;">1</span> = 악성 종양
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 12px; padding: 12px 15px; color: #334155;">
      ❓ 악성 종양이 왜 클래스 1(양성)인가요?<br>
      → <b>양성(Positive)</b>은 '좋다'는 뜻이 아니라 <b>'우리가 탐지하려는 대상'</b>이라는 뜻입니다.<br>
      암 진단 모델의 목적은 악성 종양을 잡아내는 것이므로, 악성 종양이 클래스 1입니다.
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">클래스 1(양성) = 탐지하려는 대상. 좋은 것이 아니라 찾으려는 것입니다.</div>
</div>
