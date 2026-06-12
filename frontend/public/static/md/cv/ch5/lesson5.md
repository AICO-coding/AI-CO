<div style="background:#f0fdf4;border:2px solid #86efac;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🧩</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        왜 VGG는 3×3 Convolution을 반복할까?
      </div>
      <div style="font-size:14px;color:#64748b;">
        작은 Kernel을 여러 번 사용하는 것이 더 효율적입니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #bbf7d0;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      CNN 초창기에는 5×5, 7×7처럼 큰 Kernel을 많이 사용했습니다.
    </div>
    <div>
      하지만 VGG 연구진은
      <strong style="color:#16a34a;">3×3 Kernel을 여러 번 쌓는 방법</strong>이
      더 좋은 성능을 낸다는 것을 발견했습니다.
    </div>
    <div>
      예를 들어,
      3×3 Conv를 두 번 연속 수행하면
      실제로는 5×5 영역을 보는 효과가 생깁니다.
    </div>
    <div>
      세 번 반복하면
      거의 7×7 Kernel과 비슷한 Receptive Field를 갖게 됩니다.
    </div>
    <div>
      그런데 큰 Kernel 하나보다
      작은 Kernel 여러 개가 더 좋은 이유가 있습니다.
    </div>
    <div style="margin-left:12px;">
      • 파라미터 수 감소<br>
      • 계산량 감소<br>
      • ReLU를 여러 번 사용 가능<br>
      • 더 복잡한 특징 학습 가능
    </div>
    <div>
      즉,
      같은 범위를 보면서도
      더 적은 비용으로 더 강력한 모델을 만들 수 있습니다.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;color:#cbd5e1;font-family:monospace;line-height:1.8;white-space:pre;">
5×5 Kernel
      ↓

한 번 계산


3×3 Conv
      ↓
3×3 Conv

두 번 계산

≈ 비슷한 Receptive Field
  </div>

  <div style="margin-top:18px;background:#dcfce7;border:2px solid #86efac;border-radius:14px;padding:14px;">
    <b>파라미터 수 비교</b><br><br>
    5×5 Conv<br>
    → 25개 가중치<br><br>
    3×3 Conv 두 번<br>
    → 18개 가중치<br><br>

    더 적은 파라미터로
    비슷한 범위를 볼 수 있습니다.

  </div>

  <div style="margin-top:18px;background:#bbf7d0;border:2px solid #4ade80;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    VGG는 큰 Kernel 대신 3×3 Conv를 반복하여
    계산량은 줄이고 표현력은 높였습니다.
  </div>

</div>