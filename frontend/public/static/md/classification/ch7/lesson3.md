<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">Bias-Variance 트레이드오프</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    Bias와 Variance는 <b>반대 방향으로 움직입니다.</b> 모델을 복잡하게 만들면 Bias는 낮아지지만 Variance가 올라갑니다. 단순하게 만들면 Variance는 낮아지지만 Bias가 올라갑니다.<br><br>
    목표는 <b>둘 다 낮은 지점</b>을 찾는 것입니다. 진단 방법은 간단합니다.<br>
    먼저 train 정확도를 봅니다. 낮으면
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-weight: 700;">High Bias</span>
    (underfitting)입니다. train은 높은데 test가 낮으면
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-weight: 700;">High Variance</span>
    (overfitting)입니다. 둘 다 높으면 이상적인 모델입니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #fee2e2; border-radius: 8px; padding: 10px 14px; color: #991b1b;">
      ❌ train 낮음 + test 낮음 → <b>High Bias (underfitting)</b> — 모델 복잡도 높여야 함
    </div>
    <div style="background: #fef9c3; border-radius: 8px; padding: 10px 14px; color: #713f12;">
      ⚠️ train 높음 + test 낮음 → <b>High Variance (overfitting)</b> — 규제 강화해야 함
    </div>
    <div style="background: #dcfce7; border-radius: 8px; padding: 10px 14px; color: #166534;">
      ✅ train 높음 + test 높음 → <b>이상적인 모델</b>
    </div>
    <div style="background: #eef7ff; border-radius: 8px; padding: 10px 14px; color: #334155;">
      ⚖️ <b>복잡도와의 관계</b> — 모델 복잡도↑ → Bias↓, Variance↑ / 모델 복잡도↓ → Bias↑, Variance↓
    </div>
    <div style="background: #fff3eb; border: 1px solid #ffd0b0; border-radius: 8px; padding: 10px 14px; color: #334155;">
      💡 <b>가장 근본적인 해결책</b> — 데이터를 더 많이 모으는 것. 데이터가 많으면 Bias/Variance 모두 낮아짐
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">train/test 모두 낮음 → underfitting / train 높고 test 낮음 → overfitting / 둘 다 높음 → 이상적.</div>
</div>
