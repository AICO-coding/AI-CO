<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 14px; padding: 20px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <h3 style="margin-top: 0; margin-bottom: 14px; color: #0f172a; font-weight: 900; font-size: 17px;">같은 모델인데 왜 동작이 달라질까?</h3>

  <div style="line-height: 1.85; color: #334155; font-size: 14px; margin-bottom: 18px;">
    학습할 때와 검증할 때, 모델은 <b style="color: #1681c4;">다르게 동작</b>해야 해요.<br>
    대표적인 이유가 바로 <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 1px 6px; border-radius: 4px; font-family: 'JetBrains Mono', monospace; font-size: 12.5px;">Dropout</span> 이에요.
  </div>

  <div style="display: flex; gap: 12px; margin-bottom: 18px;">
    <div style="flex: 1; background: #fff3eb; border: 2px solid #ffd0b0; border-radius: 10px; padding: 14px;">
      <div style="font-size: 13px; font-weight: 900; color: #FF6B00; margin-bottom: 8px;">model.train() 모드</div>
      <div style="font-size: 13px; color: #334155; line-height: 1.7;">
        Dropout <b>켜짐</b><br>
        일부 뉴런을 랜덤하게 끄면서<br>
        과적합을 방지해요
      </div>
      <pre style="background: #0f172a; color: #fab387; padding: 8px 10px; border-radius: 6px; font-size: 12px; margin-top: 8px; margin-bottom: 0;">○ ● ○ ● ● ○ ● ○
일부 뉴런 비활성화</pre>
    </div>
    <div style="flex: 1; background: #e1f5ee; border: 2px solid #9fe1cb; border-radius: 10px; padding: 14px;">
      <div style="font-size: 13px; font-weight: 900; color: #0f6e56; margin-bottom: 8px;">model.eval() 모드</div>
      <div style="font-size: 13px; color: #334155; line-height: 1.7;">
        Dropout <b>꺼짐</b><br>
        모든 뉴런을 사용해서<br>
        안정적인 예측을 해요
      </div>
      <pre style="background: #0f172a; color: #a6e3a1; padding: 8px 10px; border-radius: 6px; font-size: 12px; margin-top: 8px; margin-bottom: 0;">● ● ● ● ● ● ● ●
모든 뉴런 활성화</pre>
    </div>
  </div>

  <div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 12px 14px; border-radius: 10px; color: #0f172a; font-weight: bold; font-size: 13px; display: flex; align-items: flex-start; gap: 10px;">
    <div style="color: #FF6B00; font-size: 16px; margin-top: -2px;">⚡</div>
    <div style="line-height: 1.6;">
      eval() 없이 검증하면 Dropout이 꺼지지 않아<br>
      매 실행마다 다른 결과가 나와요!
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <div style="color: #94a3b8; font-size: 12px; font-weight: 800; margin-bottom: 6px; display: flex; align-items: center; gap: 5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.6;">
    미션 검증 루프에서 model.eval()을 반드시 호출해야<br>
    R² 점수가 안정적으로 나와요.
  </div>
</div>