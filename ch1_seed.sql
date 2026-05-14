-- ================================================================
-- Ch1. Tensor & Numpy Seed Data
-- 실행 전: alembic upgrade head (content_type → problem_type 적용)
-- ================================================================

-- problems 먼저 INSERT (lessons가 problem_id FK 참조하므로)

INSERT INTO problems (id, track, chapter, problem_type, content, answer, hints, created_at) VALUES

-- 레슨 3: torch.tensor 생성
(101, 'ML', 'ch1', 'code_fill',
'{
  "instruction": "torch.tensor()를 사용해서 1D Tensor를 생성하세요.",
  "template_code": "import torch\n\nx = _____([1.0, 2.0, 3.0])\nprint(x.shape)  # torch.Size([3])\nprint(x.dtype)  # torch.float32",
  "blanks": [{"id": 1, "position": "torch.tensor 함수명"}]
}',
'{
  "blanks": [{"id": 1, "answer": "torch.tensor"}]
}',
'{
  "list": [
    "torch 모듈의 기본 Tensor 생성 함수입니다.",
    "numpy의 np.array()와 비슷한 역할을 합니다."
  ]
}',
NOW()),

-- 레슨 4: matmul 구현
(102, 'ML', 'ch1', 'code_fill',
'{
  "instruction": "torch.matmul()로 두 행렬의 곱을 계산하세요. (행렬곱 = @)",
  "template_code": "import torch\n\nA = torch.tensor([[1.0, 2.0], [3.0, 4.0]])  # shape: [2, 2]\nB = torch.tensor([[1.0], [2.0]])              # shape: [2, 1]\n\nC = torch._____(A, B)  # shape: [2, 1]\nprint(C)\n# tensor([[ 5.],\n#         [11.]])",
  "blanks": [{"id": 1, "position": "행렬곱 함수명"}]
}',
'{
  "blanks": [{"id": 1, "answer": "matmul"}]
}',
'{
  "list": [
    "행렬 곱셈 함수입니다. @ 연산자와 동일합니다.",
    "A @ B 로도 쓸 수 있어요."
  ]
}',
NOW()),

-- 레슨 5: 마무리 퀴즈
(103, 'ML', 'ch1', 'quiz',
'{
  "question": "shape이 [3, 4]인 Tensor A를 A.reshape(2, -1) 하면 결과 shape은?",
  "sub": "전체 원소 개수를 힌트로 생각해보세요.",
  "options": [
    "[2, 3]",
    "[2, 6]",
    "[2, 4]",
    "[3, 4]"
  ]
}',
'{
  "answer_idx": 1,
  "explanation": "3×4 = 12개 원소, reshape(2, -1)에서 -1은 자동 계산 → 12÷2 = 6. 결과는 [2, 6]입니다."
}',
'{
  "list": ["전체 원소 개수 = 3 × 4 = 12개"]
}',
NOW());


-- ================================================================
-- lessons INSERT
-- ================================================================

INSERT INTO lessons (track, chapter_id, title, content_type, content, problem_id, order_index) VALUES

-- 레슨 1: concept - Tensor란?
('ML', 'ch1', 'Tensor란 무엇인가', 'concept',
'{
  "visual_type": "tensor_intro",
  "explanation": "Tensor는 PyTorch의 기본 데이터 단위입니다. numpy의 ndarray와 비슷하지만 GPU 연산이 가능합니다.\n\n• 0D Tensor → 스칼라 (숫자 하나)\n• 1D Tensor → 벡터\n• 2D Tensor → 행렬\n• 3D+ Tensor → 배치 데이터, 이미지 등",
  "formula": "import torch\n\n# 스칼라\nt0 = torch.tensor(3.14)\n\n# 벡터 (1D)\nt1 = torch.tensor([1.0, 2.0, 3.0])\n\n# 행렬 (2D)\nt2 = torch.tensor([[1.0, 2.0], [3.0, 4.0]])",
  "key_point": "Tensor는 GPU로 옮길 수 있어서 딥러닝 연산에 최적화되어 있습니다."
}',
NULL, 1),

-- 레슨 2: concept - shape과 reshape
('ML', 'ch1', 'shape과 reshape', 'concept',
'{
  "visual_type": "tensor_shape",
  "explanation": "shape은 Tensor의 각 차원 크기를 나타냅니다.\nreshape()으로 데이터는 유지한 채 shape을 바꿀 수 있습니다.\n\n• x.shape → 현재 shape 확인\n• x.reshape(행, 열) → shape 변환\n• -1 사용 시 자동 계산",
  "formula": "import torch\n\nx = torch.zeros(3, 4)  # shape: [3, 4]\nprint(x.shape)         # torch.Size([3, 4])\n\n# reshape: 12개 원소 → [2, 6]\ny = x.reshape(2, -1)\nprint(y.shape)         # torch.Size([2, 6])",
  "key_point": "신경망에서 shape이 맞지 않으면 에러가 납니다. 항상 shape을 먼저 확인하세요."
}',
NULL, 2),

-- 레슨 3: code_fill - torch.tensor 생성
('ML', 'ch1', 'torch.tensor 생성', 'code_fill',
'{}',
101, 3),

-- 레슨 4: code_fill - matmul 구현
('ML', 'ch1', 'matmul 구현', 'code_fill',
'{}',
102, 4),

-- 레슨 5: quiz - Ch1 마무리 퀴즈
('ML', 'ch1', 'Ch1 마무리 퀴즈', 'quiz',
'{}',
103, 5);
