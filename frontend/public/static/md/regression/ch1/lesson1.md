<div style="background-color: #e6f5ff; border: 2px solid #c2e4ff; border-radius: 14px; padding: 18px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <h3 style="margin-top: 0; margin-bottom: 14px; color: #0f172a; font-weight: 900; font-size: 17px;">Tensor = n차원 배열</h3>
  
  <div style="line-height: 1.85; color: #334155; font-size: 14px; margin-bottom: 18px;">
    딥러닝의 모든 데이터는 <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 1px 6px; border-radius: 4px; font-family: 'JetBrains Mono', monospace; font-size: 12.5px;">Tensor</span> 로 표현돼요.<br>
    NumPy ndarray와 비슷하지만 결정적 차이가 있어요.
  </div>
  
  <div style="font-size: 13px; font-weight: 800; color: #334155; margin-bottom: 10px;">차원별 구조</div>
  
  <pre style="background-color: #0f172a; color: #c3e88d; padding: 14px; border-radius: 10px; font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.9; overflow-x: auto; margin: 0;"><code>0D 스칼라  shape=()         ex) 42.0
1D 벡터   shape=(3,)       ex) [1, 2, 3]
2D 행렬   shape=(2,3)      ex) [[1,2],[3,4]]
3D 배치   shape=(8,28,28)  ex) MNIST 이미지 8장</code></pre>
  
  <div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 12px 14px; border-radius: 10px; margin-top: 16px; color: #0f172a; font-weight: bold; font-size: 13px; display: flex; align-items: flex-start; gap: 10px;">
    <div style="color: #FF6B00; font-size: 16px; margin-top: -2px;">⚡</div>
    <div style="line-height: 1.6;">GPU 연산 가능! NumPy는 CPU 전용.<br>.to('cuda') 한 줄로 GPU 이동!</div>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <div style="color: #94a3b8; font-size: 12px; font-weight: 800; margin-bottom: 6px; display: flex; align-items: center; gap: 5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.6;">
    캘리포니아 미션 첫 단계에서<br>
    pandas 데이터를 Tensor로 변환해요.
  </div>
</div>