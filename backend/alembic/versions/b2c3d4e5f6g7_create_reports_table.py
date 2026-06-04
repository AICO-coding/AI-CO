"""create reports table

Revision ID: b2c3d4e5f6g7
Revises: a1b2c3d4e5f6
Create Date: 2026-06-04 10:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b2c3d4e5f6g7'
down_revision: Union[str, Sequence[str], None] = 'a1b2c3d4e5f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('reports',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('track', sa.String(length=50), nullable=False),
    sa.Column('chapter', sa.String(length=100), nullable=False),
    sa.Column('progress_id', sa.BigInteger(), nullable=False),
    sa.Column('ai_report', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
    sa.ForeignKeyConstraint(['progress_id'], ['progress.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('progress_id', name='uq_report_progress_id')
    )
    op.create_index(op.f('ix_reports_id'), 'reports', ['id'], unique=False)
    op.create_index(op.f('ix_reports_user_id'), 'reports', ['user_id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_reports_user_id'), table_name='reports')
    op.drop_index(op.f('ix_reports_id'), table_name='reports')
    op.drop_table('reports')
