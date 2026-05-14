export const mockLessonData = {

  // ── ML 분류 챕터 1: 분류 문제의 이해 ──────────────────────
  "ML/ml_c1": {
    track: "ML",
    chapter: "ml_c1",
    completionRate: 0,
    lastLessonId: null,
    lessons: [
      {
        lessonId: 1,
        title: "회귀 vs 분류",
        contentType: "text",
        content: {
          text: "머신러닝 문제는 크게 두 가지로 나뉩니다.\n\n회귀(Regression)는 연속적인 숫자를 예측합니다. 분류(Classification)는 어떤 그룹(클래스)에 속하는지 판별합니다.",
          examples: [
            { label: "회귀 예시", value: "내일 기온이 몇 도일까? → 23.5°C" },
            { label: "분류 예시", value: "내일 비가 올까? → 예 / 아니오" },
          ],
        },
        orderIndex: 1,
        isCompleted: false,
      },
      {
        lessonId: 2,
        title: "분류 모델의 출력",
        contentType: "text",
        content: {
          text: "분류 모델의 출력은 확률입니다.\n\n예를 들어 0.73이 출력되면 '73% 확률로 양성(1)'이라는 뜻입니다. 이 값을 threshold 0.5를 기준으로 0 또는 1로 변환합니다.",
          examples: [
            { label: "threshold 적용", value: "출력 0.73 → threshold 0.5 → 예측 클래스 1 (양성)" },
          ],
        },
        orderIndex: 2,
        isCompleted: false,
      },
      {
        lessonId: 3,
        title: "Binary vs Multi-class",
        contentType: "text",
        content: {
          text: "Binary Classification은 클래스가 2개입니다.\nMulti-class Classification은 클래스가 3개 이상입니다.",
          examples: [
            { label: "Binary", value: "스팸/정상, 생존/사망" },
            { label: "Multi-class", value: "손글씨 0~9, 꽃 종류 (iris 3종)" },
          ],
        },
        orderIndex: 3,
        isCompleted: false,
      },
      {
        lessonId: 4,
        title: "확인 문제 1",
        contentType: "problem",
        problem: {
          problemId: 101,
          problemType: "객관식",
          content: {
            question: "다음 중 분류(Classification) 문제인 것은?",
            options: [
              "내일 주식 가격 예측",
              "이메일이 스팸인지 판별",
              "다음 달 매출 예측",
              "집의 면적에 따른 가격 예측",
            ],
          },
          hints: [
            "출력값이 연속적인 숫자인지, 특정 그룹인지 생각해보세요.",
            "스팸/정상은 두 가지 중 하나를 선택하는 문제입니다.",
          ],
        },
        orderIndex: 4,
        isCompleted: false,
      },
      {
        lessonId: 5,
        title: "실생활 분류 사례",
        contentType: "text",
        content: {
          text: "분류는 일상 곳곳에 쓰입니다.",
          examples: [
            { label: "의료 진단", value: "CT 이미지 → 암 여부 판별" },
            { label: "이메일 필터", value: "메일 내용 → 스팸/정상" },
            { label: "이미지 태깅", value: "사진 → 고양이/강아지/새 분류" },
          ],
        },
        orderIndex: 5,
        isCompleted: false,
      },
      {
        lessonId: 6,
        title: "확인 문제 2",
        contentType: "problem",
        problem: {
          problemId: 102,
          problemType: "객관식",
          content: {
            question: "손글씨 숫자(0~9) 분류는 어떤 유형인가?",
            options: [
              "회귀",
              "Binary Classification",
              "Multi-class Classification",
              "비지도 학습",
            ],
          },
          hints: [
            "클래스가 몇 개인지 세어보세요.",
            "0부터 9까지 총 10개의 숫자가 있습니다.",
          ],
        },
        orderIndex: 6,
        isCompleted: false,
      },
    ],
  },

  // ── ML 분류 챕터 2: sklearn으로 로지스틱 회귀 ─────────────
  "ML/ml_c2": {
    track: "ML",
    chapter: "ml_c2",
    completionRate: 0,
    lastLessonId: null,
    lessons: [
      {
        lessonId: 10,
        title: "로지스틱 회귀란?",
        contentType: "text",
        content: {
          text: "이름은 '회귀'지만 실제로는 분류 알고리즘입니다.\n선형 회귀의 출력을 Sigmoid 함수에 통과시켜 0~1 사이의 확률로 변환합니다.",
          examples: [
            { label: "선형 회귀", value: "y = wx + b" },
            { label: "로지스틱 회귀", value: "y = sigmoid(wx + b)" },
          ],
        },
        orderIndex: 1,
        isCompleted: false,
      },
      {
        lessonId: 11,
        title: "sklearn 3줄 분류기",
        contentType: "problem",
        problem: {
          problemId: 201,
          problemType: "code_fill",
          content: {
            question: "sklearn으로 로지스틱 회귀 분류기를 완성하세요.",
            code_template: "from sklearn.linear_model import LogisticRegression\n\nmodel = LogisticRegression()\nmodel.__blank__(X_train, y_train)\npred = model.__blank__(X_test)\nprob = model.__blank__(X_test)",
            blank_count: 3,
          },
          hints: [
            "학습 메서드는 fit입니다.",
            "클래스 예측은 predict, 확률 예측은 predict_proba입니다.",
          ],
        },
        orderIndex: 2,
        isCompleted: false,
      },
      {
        lessonId: 12,
        title: "predict vs predict_proba",
        contentType: "text",
        content: {
          text: "predict()는 최종 클래스(0 또는 1)를 반환합니다.\npredict_proba()는 각 클래스에 속할 확률을 반환합니다. 두 번째 열이 클래스 1(양성)의 확률입니다.",
          examples: [
            { label: "predict()", value: "[0, 1, 1, 0]" },
            { label: "predict_proba()", value: "[[0.8, 0.2], [0.1, 0.9], ...]" },
          ],
        },
        orderIndex: 3,
        isCompleted: false,
      },
      {
        lessonId: 13,
        title: "확인 문제",
        contentType: "problem",
        problem: {
          problemId: 202,
          problemType: "객관식",
          content: {
            question: "predict_proba()의 출력에서 클래스 1(양성)의 확률은 몇 번째 열인가?",
            options: [
              "첫 번째 열 (인덱스 0)",
              "두 번째 열 (인덱스 1)",
              "마지막 열",
              "별도 설정 필요",
            ],
          },
          hints: [
            "predict_proba()는 [P(class=0), P(class=1)] 순서로 반환합니다.",
          ],
        },
        orderIndex: 4,
        isCompleted: false,
      },
    ],
  },

  // ── CV 챕터 1: 이미지와 텐서의 이해 ──────────────────────
  "CV/cv_1": {
    track: "CV",
    chapter: "cv_1",
    completionRate: 0,
    lastLessonId: null,
    lessons: [
      {
        lessonId: 100,
        title: "픽셀(Pixel)이란?",
        contentType: "text",
        content: {
          text: "이미지는 아주 작은 점들의 모임으로 이루어져 있습니다. 이 작은 한 칸을 픽셀(pixel)이라고 합니다.\n\n예를 들어 224×224 이미지는 가로 224칸 × 세로 224칸, 총 50,176개의 픽셀로 구성됩니다.",
          examples: [
            { label: "총 픽셀 수", value: "224 × 224 = 50,176개" },
          ],
        },
        orderIndex: 1,
        isCompleted: false,
      },
      {
        lessonId: 101,
        title: "RGB 색상 표현",
        contentType: "text",
        content: {
          text: "컴퓨터는 색을 RGB(Red, Green, Blue) 3개의 값으로 표현합니다. 각 값은 0~255 범위를 가집니다.",
          examples: [
            { label: "(255, 0, 0)", value: "빨강" },
            { label: "(0, 255, 0)", value: "초록" },
            { label: "(255, 255, 255)", value: "흰색" },
            { label: "(0, 0, 0)", value: "검정" },
          ],
        },
        orderIndex: 2,
        isCompleted: false,
      },
      {
        lessonId: 102,
        title: "Tensor Shape",
        contentType: "text",
        content: {
          text: "PyTorch에서 이미지는 [채널, 높이, 너비] 형태의 Tensor로 표현합니다.",
          examples: [
            { label: "RGB 이미지", value: "[3, 224, 224] → 채널 3개(RGB), 높이 224, 너비 224" },
            { label: "Grayscale 이미지", value: "[1, 224, 224] → 채널 1개" },
          ],
        },
        orderIndex: 3,
        isCompleted: false,
      },
      {
        lessonId: 103,
        title: "확인 문제 1",
        contentType: "problem",
        problem: {
          problemId: 301,
          problemType: "객관식",
          content: {
            question: "해상도가 1920×1080인 이미지의 총 픽셀 수는?",
            options: [
              "1,920개",
              "1,080개",
              "2,073,600개",
              "3,000개",
            ],
          },
          hints: [
            "가로 픽셀 수 × 세로 픽셀 수를 계산하세요.",
          ],
        },
        orderIndex: 4,
        isCompleted: false,
      },
      {
        lessonId: 104,
        title: "ToTensor 변환",
        contentType: "problem",
        problem: {
          problemId: 302,
          problemType: "code_fill",
          content: {
            question: "PIL 이미지를 Tensor로 변환하는 코드를 완성하세요.",
            code_template: "from PIL import Image\nfrom torchvision import transforms\n\nimage = Image.__blank__(\"cat.jpg\")\n\ntransform = transforms.__blank__()\ntensor = transform(image)",
            blank_count: 2,
          },
          hints: [
            "이미지 파일을 여는 PIL 메서드는 open입니다.",
            "Tensor로 변환하는 transform은 ToTensor입니다.",
          ],
        },
        orderIndex: 5,
        isCompleted: false,
      },
    ],
  },

  // ── NLP 챕터 1: NLP 기초 개념 ─────────────────────────────
  "NLP/nlp_1": {
    track: "NLP",
    chapter: "nlp_1",
    completionRate: 0,
    lastLessonId: null,
    lessons: [
      {
        lessonId: 200,
        title: "NLP란 무엇인가",
        contentType: "text",
        content: {
          text: "NLP(자연어 처리)는 컴퓨터가 인간의 언어를 이해하고 생성하는 기술입니다.",
          examples: [
            { label: "정보 검색", value: "구글 검색" },
            { label: "감정 분석", value: "리뷰 긍정/부정 판별" },
            { label: "기계 번역", value: "한국어 → 영어 번역" },
            { label: "챗봇", value: "질문에 자동 답변" },
          ],
        },
        orderIndex: 1,
        isCompleted: false,
      },
      {
        lessonId: 201,
        title: "컴퓨터는 언어를 어떻게 보는가",
        contentType: "text",
        content: {
          text: "컴퓨터는 텍스트를 숫자로 변환해서 처리합니다. 이 과정이 토큰화와 임베딩입니다.",
          examples: [
            { label: "원문", value: "나는 학교에 간다" },
            { label: "토큰화", value: "['나는', '학교에', '간다']" },
            { label: "숫자 변환", value: "[102, 4521, 893]" },
          ],
        },
        orderIndex: 2,
        isCompleted: false,
      },
      {
        lessonId: 202,
        title: "토큰화(Tokenization)",
        contentType: "text",
        content: {
          text: "토큰화는 문장을 의미 단위(토큰)로 나누는 과정입니다. 단어 단위, 문자 단위, 서브워드 단위 등 다양한 방식이 있습니다.",
          examples: [
            { label: "단어 단위", value: "I love NLP → ['I', 'love', 'NLP']" },
            { label: "문자 단위", value: "cat → ['c', 'a', 't']" },
          ],
        },
        orderIndex: 3,
        isCompleted: false,
      },
      {
        lessonId: 203,
        title: "확인 문제",
        contentType: "problem",
        problem: {
          problemId: 401,
          problemType: "객관식",
          content: {
            question: "토큰화(Tokenization)의 목적으로 가장 적절한 것은?",
            options: [
              "이미지를 숫자로 변환",
              "문장을 의미 단위로 분리",
              "모델의 정확도를 높임",
              "데이터를 압축",
            ],
          },
          hints: [
            "컴퓨터가 텍스트를 처리하려면 먼저 어떻게 해야 할까요?",
          ],
        },
        orderIndex: 4,
        isCompleted: false,
      },
    ],
  },
};

// ─────────────────────────────────────────────────────────────
// 목업 fetch 함수 — 나중에 실제 API로 교체
// ─────────────────────────────────────────────────────────────

export function getLessonData(track, chapter) {
  const key = `${track}/${chapter}`;
  return mockLessonData[key] ?? null;
}