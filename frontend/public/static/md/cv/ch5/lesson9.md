<div style="background:#eef2ff;border:2px solid #c7d2fe;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">✍️</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        실습: VGG Block 완성하기
      </div>
      <div style="font-size:14px;color:#64748b;">
        VGG16의 핵심 구조를 직접 작성해보세요.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #c7d2fe;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    아래 코드는 VGG16의<br>
    첫 번째 Block입니다.<br>
    빈칸을 채워<br>
    Conv → ReLU → Conv → ReLU → MaxPool<br>
    구조를 완성해보세요.<br>

  </div>


  <div style="margin-top:18px;background:#f8fafc;border:1.5px solid #cbd5e1;border-radius:14px;padding:16px;">
    <b>작성하면서 확인할 내용</b><br><br>
    • Conv Layer는 몇 번 등장하는가?<br>
    • ReLU는 왜 Conv 뒤에 오는가?<br>
    • MaxPool은 Feature Map 크기를 어떻게 변화시키는가?<br>
    • 왜 kernel_size=3을 사용하는가?

  </div>

  <div style="margin-top:18px;background:#ddd6fe;border:2px solid #a78bfa;border-radius:14px;padding:14px;">
    <b>학습 포인트</b><br><br>

    VGG16의 핵심은 복잡한 구조가 아니라
    단순한 3×3 Convolution을 반복적으로 사용하는 것입니다.

  </div>

  <div style="margin-top:18px;background:#c7d2fe;border:2px solid #818cf8;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    VGG16은 Conv → ReLU → Conv → ReLU → MaxPool 구조를 반복하여 깊은 CNN을 구성합니다.
  </div>

</div>