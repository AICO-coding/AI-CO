<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: sans-serif;">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">ReLU — 0보다 크면 그대로, 0 이하면 0</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-weight: 700;">ReLU (Rectified Linear Unit)</span>
    는 입력이 0보다 크면 그대로 통과시키고, 0 이하면 0으로 만드는 함수입니다.<br>
    공식:
    <span style="background: #fff; border: 1px solid #c2e4ff; color: #1681c4; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-weight: 700;">ReLU(z) = max(0, z)</span><br><br>
    시그모이드보다 계산이 훨씬 단순합니다. 양수 구간에서 기울기가 항상 <b>1</b>이기 때문에 기울기 소실 문제가 거의 없습니다. 이 덕분에 층을 깊게 쌓아도 학습이 잘 됩니다. 현재 딥러닝 은닉층의 <b>기본 활성화 함수</b>로 자리잡았습니다.<br><br>
    단점은 z가 음수인 뉴런은 출력이 항상 0이 되어 학습에 전혀 기여하지 못하는
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 8px; border-radius: 4px; font-weight: 700;">Dead ReLU</span>
    문제가 있다는 것입니다.
  </div>

  <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
    <div style="background: #f1f5f9; border-radius: 8px; padding: 10px 14px; color: #334155; font-family: monospace; font-size: 12px; line-height: 2.0;">
      z =  3  → ReLU(z) = 3<br>
      z =  0  → ReLU(z) = 0<br>
      z = -5  → ReLU(z) = 0
    </div>
    <div style="background: #dcfce7; border-radius: 8px; padding: 10px 14px; color: #166534;">
      ✅ <b>Sigmoid 대비 장점</b> — 계산 단순 / 양수 구간 기울기 = 1 → 기울기 소실 없음 → 깊은 신경망에 적합
    </div>
    <div style="background: #fee2e2; border-radius: 8px; padding: 10px 14px; color: #991b1b;">
      ⚠️ <b>Dead ReLU</b> — z가 음수인 뉴런 → 출력 = 0 → 기울기 = 0 → 가중치 업데이트 안 됨
    </div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 12px 15px; font-family: sans-serif;">
  <div style="color: #94a3b8; font-size: 11px; font-weight: 800; margin-bottom: 4px;">💡 핵심 기억</div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.5;">ReLU = max(0, z). 양수는 그대로, 음수는 0. 기울기 소실 없어 은닉층 기본 함수. Dead ReLU 단점 있음.</div>
</div>
