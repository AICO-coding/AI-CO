<div style="background-color:#e6f5ff;border:2px solid #c2e4ff;border-radius:14px;padding:18px;font-family:'Nunito',sans-serif,'Malgun Gothic';">
  <h3 style="margin-top:0;margin-bottom:14px;color:#0f172a;font-weight:900;font-size:17px;">🧩 Dataset + DataLoader 완성하기</h3>
  <div style="line-height:1.85;color:#334155;font-size:14px;margin-bottom:16px;">
    붓꽃(iris) 데이터로 <b>정규화 → Dataset → DataLoader</b> 파이프라인을 완성해요.<br>
    L2·L3에서 배운 내용을 이어서 직접 구현해보세요!
  </div>
  <div style="font-size:13px;font-weight:800;color:#334155;margin-bottom:10px;">TODO 가이드</div>
  <div style="display:flex;flex-direction:column;gap:7px;margin-bottom:16px;">
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;line-height:1.5;display:flex;gap:8px;align-items:flex-start;">
      <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:1px 7px;border-radius:20px;flex-shrink:0;margin-top:2px;">1</span>
      <div><b>blank1</b> — 평균=0, 분산=1로 정규화하는 클래스 인스턴스</div>
    </div>
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;line-height:1.5;display:flex;gap:8px;align-items:flex-start;">
      <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:1px 7px;border-radius:20px;flex-shrink:0;margin-top:2px;">2</span>
      <div><b>blank2</b> — train 데이터: fit과 transform 동시 적용</div>
    </div>
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;line-height:1.5;display:flex;gap:8px;align-items:flex-start;">
      <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:1px 7px;border-radius:20px;flex-shrink:0;margin-top:2px;">3</span>
      <div><b>blank3</b> — <code style="font-family:'JetBrains Mono',monospace;font-size:11px;">__len__</code>: 전체 샘플 수 반환 (self.X의 길이)</div>
    </div>
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;line-height:1.5;display:flex;gap:8px;align-items:flex-start;">
      <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:1px 7px;border-radius:20px;flex-shrink:0;margin-top:2px;">4</span>
      <div><b>blank4</b> — <code style="font-family:'JetBrains Mono',monospace;font-size:11px;">__getitem__</code>: i번째 X와 y 동시 반환 (튜플)</div>
    </div>
    <div style="background:#fff;border:1px solid #c2e4ff;border-radius:8px;padding:9px 13px;font-size:13px;color:#334155;line-height:1.5;display:flex;gap:8px;align-items:flex-start;">
      <span style="background:#FF6B00;color:#fff;font-size:10px;font-weight:900;padding:1px 7px;border-radius:20px;flex-shrink:0;margin-top:2px;">5</span>
      <div><b>blank5·6·7</b> — DataLoader 클래스명, 배치 크기(32), 셔플 여부(True)</div>
    </div>
  </div>
  <div style="background-color:#fff3eb;border:2px solid #ffd0b0;padding:12px 14px;border-radius:10px;color:#0f172a;font-weight:bold;font-size:13px;display:flex;align-items:flex-start;gap:10px;">
    <div style="color:#FF6B00;font-size:16px;margin-top:-2px;">⚡</div>
    <div style="line-height:1.6;">성공하면 Xb.shape = <code style="font-family:'JetBrains Mono',monospace;font-size:12px;">torch.Size([32, 4])</code>가 출력돼요!</div>
  </div>
</div>

<br>

<div style="background-color:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:14px 16px;font-family:'Nunito',sans-serif;">
  <div style="color:#94a3b8;font-size:12px;font-weight:800;margin-bottom:6px;display:flex;align-items:center;gap:5px;">
    <span>🏆</span> Mission 연결
  </div>
  <div style="color:#64748b;font-size:13px;line-height:1.6;">
    미션 TODO 2·3·4에서 똑같은 패턴을 써요.<br>
    데이터만 붓꽃 → 캘리포니아 집값으로 바뀔 뿐이에요!
  </div>
</div>