"""rename lessons columns and add part

Revision ID: 3f8a12b9c5d7
Revises: 69e85def6f44
Create Date: 2026-05-21 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f8a12b9c5d7'
down_revision: Union[str, Sequence[str], None] = '69e85def6f44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # lessons: 컬럼명 변경
    op.alter_column('lessons', 'chapter_id', new_column_name='chapter')
    op.alter_column('lessons', 'content_type', new_column_name='lesson_type')
    # lessons: part 컬럼 추가
    op.add_column('lessons', sa.Column('part', sa.String(), nullable=True))
    # progress: part 컬럼 추가
    op.add_column('progress', sa.Column('part', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('progress', 'part')
    op.drop_column('lessons', 'part')
    op.alter_column('lessons', 'lesson_type', new_column_name='content_type')
    op.alter_column('lessons', 'chapter', new_column_name='chapter_id')
