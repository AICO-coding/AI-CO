<div style="background:#eefaf3;border:2px solid #bfe8d0;border-radius:16px;padding:24px;font-family:Pretendard,'Malgun Gothic',sans-serif;max-width:900px;margin:auto;">

  <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
    <div style="font-size:30px;">🔍</div>
    <div>
      <div style="font-size:20px;font-weight:900;color:#0f172a;">
        Convolution — 특징을 찾는 필터
      </div>
      <div style="font-size:14px;color:#64748b;margin-top:4px;">
        CNN은 이미지를 작은 필터(Filter)로 훑으며 특징을 찾아냅니다.
      </div>
    </div>
  </div>

  <div style="background:white;border:1.5px solid #d1fae5;border-radius:14px;padding:18px;color:#334155;font-size:14px;line-height:2;">
    <div>
      <strong style="color:#10b981;">Convolution</strong>
      = 필터(Filter)를 이미지 위에 이동시키며 계산하는 과정
    </div>
    <div>
      CNN은 작은 영역을 조금씩 살펴보며 특징을 추출합니다.
    </div>
    <div>
      필터는 <strong style="color:#0f172a;">모서리, 선, 패턴</strong> 등을 찾습니다.
    </div>
    <div style="margin-top:8px;padding-left:8px;">
      • 세로선 감지<br>
      • 가로선 감지<br>
      • 경계선 감지
    </div>
  </div>

  <div style="margin-top:18px;background:#0f172a;border-radius:14px;padding:18px;font-family:monospace;font-size:13px;line-height:1.9;color:#cbd5e1;">
    Input Image : (28, 28)<br>
    Filter Size : (3, 3)<br><br>
    Filter slides across image<br>
    ↓<br>
    Multiply + Sum<br>
    ↓<br>
    Feature Map 생성
  </div>

  <div style="margin-top:18px;background:white;border:1.5px solid #d1fae5;border-radius:14px;padding:18px;">
    <div style="font-size:14px;font-weight:700;color:#0f172a;margin-bottom:10px;">
      예시: 3×3 필터 적용
    </div>
    <div style="display:flex;align-items:center;gap:18px;flex-wrap:wrap;font-family:monospace;font-size:13px;">

      <pre style="background:#f8fafc;padding:10px;border-radius:10px;margin:0;">1 2 3
4 5 6
7 8 9</pre>
      <div style="font-size:22px;font-weight:bold;">×</div>
      <pre style="background:#f8fafc;padding:10px;border-radius:10px;margin:0;">1  0 -1
1  0 -1
1  0 -1</pre>
      <div style="font-size:22px;font-weight:bold;">=</div>
      <div style="font-size:20px;font-weight:900;">-6</div>
    </div>
    <div style="margin-top:12px;font-size:13px;color:#64748b;">
      각 위치의 값을 곱한 뒤 모두 더해서 하나의 결과값을 만듭니다.
    </div>
  </div>

  <div style="margin-top:18px;background:#ecfeff;border:2px solid #bae6fd;border-radius:14px;padding:14px;">
    <strong>📌 Convolution 결과물 = Feature Map</strong><br>
    이미지 속 중요한 특징만 강조한 새로운 이미지입니다.
  </div>

  <div style="margin-top:18px;background:#fef3c7;border:2px solid #fde68a;border-radius:14px;padding:14px;">
    <strong>💡 핵심</strong><br>
    Convolution = 필터를 이동시키며 이미지의 특징을 추출하는 과정
  </div>

</div>

</body>
</html>