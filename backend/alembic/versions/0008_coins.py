"""Add total_coins and quiz_attempts.coins_earned.

Revision ID: 0008_coins
Revises: 0007_drop_study_sessions
Create Date: 2026-08-15
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "0008_coins"
down_revision: Union[str, None] = "0007_drop_study_sessions"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "student_profiles",
        sa.Column("total_coins", sa.Integer(), nullable=False, server_default="0"),
    )
    op.add_column(
        "quiz_attempts",
        sa.Column("coins_earned", sa.Integer(), nullable=False, server_default="0"),
    )


def downgrade() -> None:
    op.drop_column("quiz_attempts", "coins_earned")
    op.drop_column("student_profiles", "total_coins")
