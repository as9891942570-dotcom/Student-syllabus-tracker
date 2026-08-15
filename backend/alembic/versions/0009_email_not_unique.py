"""Allow multiple student accounts to share one email.

Revision ID: 0009_email_not_unique
Revises: 0008_coins
Create Date: 2026-08-15
"""

from typing import Sequence, Union

from alembic import op

revision: str = "0009_email_not_unique"
down_revision: Union[str, None] = "0008_coins"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_index("ix_users_email", table_name="users")
    op.create_index("ix_users_email", "users", ["email"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_users_email", table_name="users")
    op.create_index("ix_users_email", "users", ["email"], unique=True)
