<div style="background:#eff6ff;border:2px solid #93c5fd;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">✏️</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        따라해보기 — CNN Shape 변화
      </div>
      <div style="font-size:14px;color:#64748b;">
        Conv와 Pool의 핵심 파라미터를 직접 채워보세요.
      </div>
    </div>
  </div>

  <div style="background:white;border:1px solid #bfdbfe;border-radius:14px;padding:18px;color:#334155;line-height:2;">
    아래 코드는 CNN에서 가장 흔히 사용되는
    Conv → Pool 흐름입니다.
    <br><br>
    빈칸을 채워
    입력 Shape이 어떻게 변하는지 확인해보세요.

  </div>


  <div style="margin-top:18px;background:#dbeafe;border:2px solid #93c5fd;border-radius:14px;padding:16px;line-height:1.9;">
    <strong>예상 결과</strong><br><br>
    torch.Size([1, 64, 112, 112])
    <br><br>

  </div>

  <div style="margin-top:18px;background:#dbeafe;border:2px solid #60a5fa;border-radius:14px;padding:14px;">
    💡 핵심:<br>
    Conv는 특징을 늘리고 Pool은 크기를 줄인다.
  </div>

</div>