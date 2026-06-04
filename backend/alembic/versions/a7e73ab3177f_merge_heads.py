"""merge_heads

Revision ID: a7e73ab3177f
Revises: 3f8a12b9c5d7, b2c3d4e5f6g7
Create Date: 2026-06-04 10:20:40.185382

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7e73ab3177f'
down_revision: Union[str, Sequence[str], None] = ('3f8a12b9c5d7', 'b2c3d4e5f6g7')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
