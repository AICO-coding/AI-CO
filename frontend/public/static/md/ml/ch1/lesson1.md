<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 18px; padding: 24px 26px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">회귀 vs 분류의 차이</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    머신러닝 문제는 크게 두 가지로 나뉩니다.<br><br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 6px; font-weight: 700;">회귀 (Regression)</span>
    — <b>'얼마나?'</b> 라는 질문에 답합니다. 정답이 연속적인 숫자입니다.<br>
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 6px; font-weight: 700;">분류 (Classification)</span>
    — <b>'어느 그룹인가?'</b> 라는 질문에 답합니다. 정답이 정해진 카테고리 중 하나입니다.<br><br>
    둘을 구분하는 가장 빠른 방법은 <b>정답의 형태</b>를 보는 것입니다.<br>
    정답이 숫자이면 → 회귀 / 정답이 카테고리이면 → 분류
  </div>

  <table style="width: 100%; border-collapse: collapse; margin-top: 16px; font-size: 13px;">
    <thead>
      <tr style="background-color: #dbeafe;">
        <th style="padding: 8px 12px; text-align: left; color: #0f172a;"> </th>
        <th style="padding: 8px 12px; text-align: left; color: #0f172a;">회귀</th>
        <th style="padding: 8px 12px; text-align: left; color: #0f172a;">분류</th>
      </tr>
    </thead>
    <tbody>
      <tr style="border-top: 1px solid #e2e8f0;">
        <td style="padding: 8px 12px; color: #64748b;">질문</td>
        <td style="padding: 8px 12px; color: #334155;">얼마나?</td>
        <td style="padding: 8px 12px; color: #334155;">어느 그룹?</td>
      </tr>
      <tr style="border-top: 1px solid #e2e8f0; background: #f8fafc;">
        <td style="padding: 8px 12px; color: #64748b;">출력 형태</td>
        <td style="padding: 8px 12px; color: #334155;">연속값 (숫자)</td>
        <td style="padding: 8px 12px; color: #334155;">이산값 (카테고리)</td>
      </tr>
      <tr style="border-top: 1px solid #e2e8f0;">
        <td style="padding: 8px 12px; color: #64748b;">정답 수</td>
        <td style="padding: 8px 12px; color: #334155;">무한히 많음</td>
        <td style="padding: 8px 12px; color: #334155;">유한하게 정해짐</td>
      </tr>
      <tr style="border-top: 1px solid #e2e8f0; background: #f8fafc;">
        <td style="padding: 8px 12px; color: #64748b;">예시</td>
        <td style="padding: 8px 12px; color: #334155;">집값, 기온, 혈당</td>
        <td style="padding: 8px 12px; color: #334155;">스팸/정상, 양성/악성</td>
      </tr>
    </tbody>
  </table>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🔢 <b>회귀 예시</b> — 내일 기온이 몇 도인가? → <span style="color: #FF6B00; font-weight: 700;">27.3도</span> (연속값)
    </div>
    <div style="background: #f1f5f9; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🔢 <b>회귀 예시</b> — 이 집의 가격은 얼마인가? → <span style="color: #FF6B00; font-weight: 700;">3억 2천만원</span> (연속값)
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🏷️ <b>분류 예시</b> — 이 이메일은 스팸인가? → <span style="color: #1681c4; font-weight: 700;">스팸 / 정상</span> (카테고리)
    </div>
    <div style="background: #eef7ff; border-radius: 12px; padding: 12px 15px; color: #334155;">
      🏷️ <b>분류 예시</b> — 이 종양은 악성인가? → <span style="color: #1681c4; font-weight: 700;">양성 / 악성</span> (카테고리)
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 14px 16px; font-family: 'Nunito', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">정답이 숫자이면 회귀, 이름 있는 카테고리이면 분류입니다.</div>
</div>
