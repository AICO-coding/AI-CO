<div style="background-color: #eef7ff; border: 2px solid #c2e4ff; border-radius: 12px; padding: 20px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <h3 style="margin-top: 0; color: #0f172a; font-weight: 900;">NumPy vs PyTorch Tensor</h3>
  <div style="line-height: 2.2; color: #334155; font-size: 14px;">
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">np.array()</span> — CPU 전용<br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">torch.tensor()</span> — GPU 가능<br>
    <span style="background: #fff; border: 1px solid #ffd0b0; color: #FF6B00; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 13px;">from_numpy()</span> — <b style="color: #1681c4;">메모리 공유!</b>
  </div>

  <div style="background-color: #0f172a; color: #c3e88d; padding: 15px; border-radius: 10px; font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 1.8; margin-top: 15px;">
    np.array([1,2,3])      → ndarray (CPU만)<br>
    torch.tensor([1,2,3]) → Tensor  (GPU 가능)<br>
    torch.from_numpy(arr) → 메모리 공유! ⚠️
  </div>

  <div style="background-color: #fff3eb; border: 2px solid #ffd0b0; padding: 12px 15px; border-radius: 10px; margin-top: 15px; color: #0f172a; font-weight: bold; font-size: 13px; display: flex; align-items: center; gap: 10px;">
    <span style="color: #FF6B00; font-size: 16px;">⚡</span> int + float 혼용 → RuntimeError! .float() 또는 .long()으로 타입 맞추기
  </div>
</div>

<br>

<div style="background-color: #1e1e2e; border: 2px solid #e2e8f0; border-radius: 12px; overflow: hidden; font-family: 'JetBrains Mono', monospace; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  <div style="background-color: #0d0d1a; border-bottom: 1px solid #1a1a2e; padding: 10px 15px; display: flex; align-items: center; justify-content: space-between;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <div style="width: 10px; height: 10px; background: #ff5f57; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #ffbd2e; border-radius: 50%;"></div>
      <div style="width: 10px; height: 10px; background: #28ca41; border-radius: 50%;"></div>
      <span style="color: #6060a0; margin-left: 8px; font-size: 12px;">📄 reference.py</span>
    </div>
    <div style="background-color: rgba(255,107,0,.2); color: #FF6B00; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; font-family: 'Nunito', sans-serif;">
      참고 코드 ← 보고 채워요
    </div>
  </div>
  
  <div style="padding: 15px 0; color: #cdd6f4; font-size: 13px; line-height: 1.8; overflow-x: auto;">
<pre style="margin: 0; background: transparent; border: none; padding: 0;"><code><div style="padding: 0 15px;"><span style="color: #cba6f7;">import</span> torch, numpy <span style="color: #cba6f7;">as</span> np</div>
<div style="padding: 0 15px;">arr = np.array([<span style="color: #fab387;">1.</span>, <span style="color: #fab387;">2.</span>, <span style="color: #fab387;">3.</span>])</div>
<div style="background: rgba(255,107,0,.09); border-left: 2px solid #FF6B00; padding: 0 13px; margin-top: 8px;"><span style="color: #545478; font-style: italic;"># from_numpy: 메모리 공유!</span></div><div style="background: rgba(255,107,0,.09); border-left: 2px solid #FF6B00; padding: 0 13px;">t = torch.from_numpy(arr)</div><div style="padding: 0 15px;">arr[<span style="color: #fab387;">0</span>] = <span style="color: #fab387;">999.</span></div><div style="background: rgba(255,107,0,.09); border-left: 2px solid #FF6B00; padding: 0 13px;">print(t)   <span style="color: #545478; font-style: italic;"># tensor([999., 2., 3.])</span></div>
<div style="padding: 0 15px; margin-top: 8px;"><span style="color: #545478; font-style: italic;"># Tensor → NumPy</span></div><div style="background: rgba(255,107,0,.09); border-left: 2px solid #FF6B00; padding: 0 13px;">back = t.numpy()   <span style="color: #545478; font-style: italic;"># CPU만 가능!</span></div></code></pre>
  </div>
</div>

<br>

<div style="background-color: #f8fafc; border: 2px solid #e2e8f0; border-radius: 10px; padding: 14px 16px; font-family: 'Nunito', sans-serif, 'Malgun Gothic';">
  <div style="color: #94a3b8; font-size: 12px; font-weight: 800; margin-bottom: 6px; display: flex; align-items: center; gap: 5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color: #64748b; font-size: 13px; line-height: 1.6;">
    미션 전처리에서 torch.tensor(df.values)로 pandas → Tensor 변환해요.
  </div>
</div>