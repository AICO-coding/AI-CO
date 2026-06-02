"""remove track and chapter from daily_problems

Revision ID: a1b2c3d4e5f6
Revises: 69e85def6f44
Create Date: 2026-06-02 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, Sequence[str], None] = '69e85def6f44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('daily_problems', 'track')
    op.drop_column('daily_problems', 'chapter')


def downgrade() -> None:
    op.add_column('daily_problems', sa.Column('chapter', sa.String(length=100), nullable=True))
    op.add_column('daily_problems', sa.Column('track', sa.String(length=50), nullable=True))
