"""
DB 테이블 확인 스크립트
"""

from sqlalchemy import inspect
from app.core.database import engine

print("=" * 80)
print("📊 DB 테이블 확인")
print("=" * 80)

try:
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    print(f"\n✅ DB 연결 성공!\n")
    print(f"📋 현재 테이블 ({len(tables)}개):")
    print("-" * 80)

    for table in sorted(tables):
        print(f"  • {table}")

    print("\n" + "=" * 80)

    # reports 테이블 확인
    if 'reports' in tables:
        print("✅ reports 테이블: 있음")
        columns = inspector.get_columns('reports')
        print("\n   컬럼:")
        for col in columns:
            print(f"     - {col['name']}: {col['type']}")
    else:
        print("❌ reports 테이블: 없음 (마이그레이션 미적용)")
        print("\n⚠️  reports 테이블이 없으면:")
        print("   - AI 리포트가 저장되지 않음")
        print("   - 폴백 리포트만 반환됨")

except Exception as e:
    print(f"❌ DB 연결 실패: {e}")

print("=" * 80)
