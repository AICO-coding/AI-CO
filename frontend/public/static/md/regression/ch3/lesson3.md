<div style="background-color:#e6f5ff;border:2px solid #c2e4ff;border-radius:14px;padding:18px;font-family:'Nunito',sans-serif,'Malgun Gothic';">
  <h3 style="margin-top:0;margin-bottom:14px;color:#0f172a;font-weight:900;font-size:17px;">Dataset · DataLoader</h3>
  <div style="line-height:1.85;color:#334155;font-size:14px;margin-bottom:14px;">
    PyTorch의 배치 학습은 <b>Dataset</b>과 <b>DataLoader</b> 두 개가 짝을 이뤄요.<br>
    Dataset은 "데이터 창고", DataLoader는 "자동 배송 시스템"이에요.
  </div>
  <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:14px;">
    <div style="background:#fff;border:2px solid #c2e4ff;border-radius:8px;padding:10px 14px;">
      <div style="font-size:13px;font-weight:900;color:#0f172a;margin-bottom:6px;">Dataset 클래스</div>
      <div style="font-size:12px;color:#334155;line-height:1.7;">
        <code style="font-family:'JetBrains Mono',monospace;color:#FF6B00;background:#fff3eb;border:1px solid #ffd0b0;padding:1px 5px;border-radius:4px;">__len__()</code>
        &nbsp;— DataLoader가 "총 몇 개야?" 물어볼 때 답해줘요<br>
        <code style="font-family:'JetBrains Mono',monospace;color:#FF6B00;background:#fff3eb;border:1px solid #ffd0b0;padding:1px 5px;border-radius:4px;">__getitem__(i)</code>
        &nbsp;— DataLoader가 "i번째 샘플 줘" 할 때 반환해요
      </div>
    </div>
    <div style="background:#fff;border:2px solid #c2e4ff;border-radius:8px;padding:10px 14px;">
      <div style="font-size:13px;font-weight:900;color:#0f172a;margin-bottom:6px;">DataLoader 파라미터</div>
      <div style="font-size:12px;color:#334155;line-height:1.7;">
        <code style="font-family:'JetBrains Mono',monospace;color:#FF6B00;background:#fff3eb;border:1px solid #ffd0b0;padding:1px 5px;border-radius:4px;">batch_size=64</code>
        &nbsp;— 한 번에 묶을 샘플 수 (2의 거듭제곱 권장)<br>
        <code style="font-family:'JetBrains Mono',monospace;color:#FF6B00;background:#fff3eb;border:1px solid #ffd0b0;padding:1px 5px;border-radius:4px;">shuffle=True</code>
        &nbsp;— 매 에폭마다 순서 섞기 → 과적합 방지
      </div>
    </div>
  </div>
  <div style="background-color:#fff3eb;border:2px solid #ffd0b0;padding:12px 14px;border-radius:10px;color:#0f172a;font-weight:bold;font-size:13px;display:flex;align-items:flex-start;gap:10px;">
    <div style="color:#FF6B00;font-size:16px;margin-top:-2px;">⚡</div>
    <div style="line-height:1.6;">Dataset은 직접 만들고, DataLoader는 그걸 가져다 씁니다.<br>for문으로 순회하면 자동으로 배치 묶음이 나와요!</div>
  </div>
</div>

<br>

<div style="background-color:#1e1e2e;border:2px solid #e2e8f0;border-radius:12px;overflow:hidden;font-family:'JetBrains Mono',monospace;box-shadow:0 4px 6px rgba(0,0,0,0.1);">
  <div style="background-color:#0d0d1a;border-bottom:1px solid #1a1a2e;padding:10px 15px;display:flex;align-items:center;justify-content:space-between;">
    <div style="display:flex;align-items:center;gap:6px;">
      <div style="width:10px;height:10px;background:#ff5f57;border-radius:50%;"></div>
      <div style="width:10px;height:10px;background:#ffbd2e;border-radius:50%;"></div>
      <div style="width:10px;height:10px;background:#28ca41;border-radius:50%;"></div>
      <span style="color:#6060a0;margin-left:8px;font-size:12px;">📄 reference.py</span>
    </div>
    <div style="background-color:rgba(255,107,0,.2);color:#FF6B00;padding:4px 10px;border-radius:12px;font-size:11px;font-weight:800;font-family:'Nunito',sans-serif;">참고 코드 ← 보고 채워요</div>
  </div>
  <div style="padding:15px;color:#cdd6f4;font-size:13px;line-height:1.6;overflow-x:auto;">
<pre style="margin:0;background:transparent;border:none;padding:0;"><code><span style="color:#cba6f7;">from</span> torch.utils.data <span style="color:#cba6f7;">import</span> Dataset, DataLoader

<span style="color:#cba6f7;">class</span> <span style="color:#FFB86C;">HousingDataset</span>(Dataset):
    <span style="color:#cba6f7;">def</span> <span style="color:#50FA7B;">__init__</span>(self, X, y):
        self.X, self.y = X, y

    <span style="color:#cba6f7;">def</span> <span style="color:#50FA7B;">__len__</span>(self):
        <span style="color:#cba6f7;">return</span> len(self.X)           <span style="color:#545478;font-style:italic;"># 전체 샘플 수 반환</span>

    <span style="color:#cba6f7;">def</span> <span style="color:#50FA7B;">__getitem__</span>(self, i):
        <span style="color:#cba6f7;">return</span> self.X[i], self.y[i]  <span style="color:#545478;font-style:italic;"># i번째 (X, y) 튜플</span>

<span style="color:#545478;font-style:italic;"># DataLoader: 자동으로 배치 묶기</span>
train_ld = DataLoader(HousingDataset(X_tr, y_tr),
                      batch_size=<span style="color:#fab387;">64</span>, shuffle=<span style="color:#fab387;">True</span>)

<span style="color:#545478;font-style:italic;"># 사용 예시 — for문으로 배치 순회</span>
<span style="color:#cba6f7;">for</span> Xb, yb <span style="color:#cba6f7;">in</span> train_ld:
    print(Xb.shape)  <span style="color:#545478;font-style:italic;"># torch.Size([64, 8])</span>
    <span style="color:#cba6f7;">break</span></code></pre>
  </div>
</div>

<br>

<div style="background-color:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:14px 16px;font-family:'Nunito',sans-serif;">
  <div style="color:#94a3b8;font-size:12px;font-weight:800;margin-bottom:6px;display:flex;align-items:center;gap:5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color:#64748b;font-size:13px;line-height:1.6;">
    TODO 3에서 <code style="background:#f1f5f9;padding:1px 5px;border-radius:4px;font-size:12px;">__len__</code>과 <code style="background:#f1f5f9;padding:1px 5px;border-radius:4px;font-size:12px;">__getitem__</code>을,<br>
    TODO 4에서 <code style="background:#f1f5f9;padding:1px 5px;border-radius:4px;font-size:12px;">DataLoader</code>의 파라미터를 채워요.
  </div>
</div>