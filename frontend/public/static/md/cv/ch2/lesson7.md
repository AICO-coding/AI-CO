<div style="background:#f5f3ff;border:2px solid #ddd6fe;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">📐</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Output Size 코드 따라해보기
      </div>
      <div style="font-size:14px;color:#64748b;margin-top:4px;">
        Output Size 공식을 코드로 구현해봅시다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #e9d5ff;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">

    <div>
      CNN에서는 Convolution 이후 생성되는 Feature Map의 크기를
      <strong style="color:#7c3aed;">Output Size</strong>
      라고 합니다.
    </div>

    <div>
      Output Size는 Input Size, Kernel Size, Padding, Stride를 이용하여 계산할 수 있습니다.
    </div>

    <div>
      아래 코드를 직접 입력하며 Output Size 공식을 확인해보세요.
    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

<pre style="margin:0;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.9;">
def output_size(W, K, P, S):
    return ((W - K + 2 * P) // S) + 1

print(output_size(28, 3, 0, 1))
</pre>

  </div>

  <div style="margin-top:18px;background:white;border:1.5px solid #e9d5ff;border-radius:14px;padding:18px;">

    <div style="font-size:15px;font-weight:800;color:#0f172a;margin-bottom:12px;">
      코드 설명
    </div>

    <div style="font-size:14px;color:#334155;line-height:2;">

      <strong style="color:#7c3aed;">W</strong><br>
      Input Size (입력 이미지 크기)
      <br><br>

      <strong style="color:#7c3aed;">K</strong><br>
      Kernel Size
      <br><br>

      <strong style="color:#7c3aed;">P</strong><br>
      Padding 크기
      <br><br>

      <strong style="color:#7c3aed;">S</strong><br>
      Stride 크기
      <br><br>

      함수는 Output Size 공식을 그대로 구현한 것입니다.

    </div>

  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;overflow-x:auto;">

    <div style="font-size:14px;font-weight:700;color:white;margin-bottom:10px;">
      실행 결과
    </div>

<pre style="margin:0;color:#cbd5e1;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.9;">
26
</pre>

  </div>

  <div style="margin-top:18px;background:white;border:1.5px solid #e9d5ff;border-radius:14px;padding:18px;">

    <div style="font-size:15px;font-weight:800;color:#0f172a;margin-bottom:12px;">
      계산 과정
    </div>

    <div style="font-size:14px;color:#334155;line-height:2;">

      입력값

<pre style="margin-top:10px;background:#faf5ff;padding:12px;border-radius:10px;color:#4c1d95;font-family:'JetBrains Mono',monospace;">
W = 28
K = 3
P = 0
S = 1
</pre>

      Output Size

<pre style="margin-top:10px;background:#faf5ff;padding:12px;border-radius:10px;color:#4c1d95;font-family:'JetBrains Mono',monospace;">
((28 - 3 + 2×0) / 1) + 1
= 26
</pre>

    </div>

  </div>

  <div style="margin-top:18px;background:#ede9fe;border:2px solid #c4b5fd;border-radius:14px;padding:14px 16px;">
    <div style="font-size:13px;font-weight:700;color:#0f172a;line-height:1.8;">
      📌 확인해보기<br>
      print(output_size(28, 3, 0, 2)) 의 결과는 얼마일까요?
    </div>
  </div>

  <div style="margin-top:18px;background:#fff3eb;border:2px solid #ffd0b0;border-radius:14px;padding:14px 16px;">
    <div style="font-size:13px;font-weight:700;color:#0f172a;line-height:1.8;">
      💡 핵심<br>
      • Output Size는 Feature Map의 크기이다.<br>
      • Kernel, Padding, Stride에 의해 결정된다.<br>
      • 공식의 분모에는 Stride(S)가 들어간다.
    </div>
  </div>

</div>