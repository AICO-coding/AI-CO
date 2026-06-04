"""
AI 리포트 생성 테스트 스크립트
직접 Claude API를 호출해서 응답을 확인합니다.
"""

from app.services.report.report_service import generate_ai_report
import json

# 테스트 데이터 (임의로 설정)
chapter_title = "Tensor & Numpy"
track = "ML"
total_problems = 6
wrong_count = 1
hint_usage = {
    "dtype 설정": 2,
    "from_numpy 메모리 공유": 1
}
wrong_problems = [
    {
        "title": "dtype 설정하기",
        "userAnswer": "float64",
        "correctAnswer": "float32",
        "explanation": "PyTorch의 기본 dtype은 float32입니다.",
        "type": "code_fill"
    }
]
reveal_used = False

print("=" * 80)
print("🤖 Claude AI 리포트 생성 테스트")
print("=" * 80)
print(f"\n📚 입력 데이터:")
print(f"  - 챕터: {chapter_title}")
print(f"  - 트랙: {track}")
print(f"  - 총 문제: {total_problems}")
print(f"  - 틀린 문제: {wrong_count}")
print(f"  - 정답률: {int((total_problems - wrong_count) / total_problems * 100)}%")
print(f"  - 힌트 사용: {hint_usage}")
print(f"  - 정답공개: {reveal_used}")

print(f"\n⏳ Claude API 호출 중... (1-2초 걸림)")
print("-" * 80)

try:
    # AI 리포트 생성
    ai_report = generate_ai_report(
        chapter_title=chapter_title,
        track=track,
        total_problems=total_problems,
        wrong_count=wrong_count,
        hint_usage=hint_usage,
        wrong_problems=wrong_problems,
        reveal_used=reveal_used
    )

    print("\n✅ AI 응답 성공!\n")
    print("=" * 80)
    print(json.dumps(ai_report, ensure_ascii=False, indent=2))
    print("=" * 80)

    # 각 필드 확인
    print("\n📊 응답 필드 확인:")
    print(f"  ✓ weakConcepts: {ai_report.get('weakConcepts', [])}")
    print(f"  ✓ cobotComment: {ai_report.get('cobotComment', '')[:50]}...")
    print(f"  ✓ summary: {ai_report.get('summary', '')[:50]}...")
    print(f"  ✓ keyPoint: {ai_report.get('keyPoint', '')[:50]}...")
    print(f"  ✓ nextChapter: {ai_report.get('nextChapter', '')[:50]}...")
    print(f"  ✓ opensource 자료: {len(ai_report.get('opensource', []))}개")

except Exception as e:
    print(f"\n❌ API 호출 실패!")
    print(f"오류: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 80)
