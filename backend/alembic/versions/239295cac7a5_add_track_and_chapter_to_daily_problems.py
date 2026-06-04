"""add track and chapter to daily_problems

Revision ID: 239295cac7a5
Revises: a7e73ab3177f
Create Date: 2026-06-04 18:43:23.865299

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '239295cac7a5'
down_revision: Union[str, Sequence[str], None] = 'a7e73ab3177f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        "daily_problems",
        sa.Column("track", sa.String(), nullable=True)
    )
    op.add_column(
        "daily_problems",
        sa.Column("chapter", sa.String(), nullable=True)
    )


def downgrade():
    op.drop_column("daily_problems", "chapter")
    op.drop_column("daily_problems", "track")