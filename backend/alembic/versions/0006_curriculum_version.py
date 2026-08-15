"""Add curriculum_version and is_active to syllabus tables.

Revision ID: 0006_curriculum_version
Revises: 0005_quizzes
Create Date: 2026-08-13
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "0006_curriculum_version"
down_revision: Union[str, None] = "0005_quizzes"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "subjects",
        sa.Column(
            "curriculum_version",
            sa.String(length=32),
            nullable=False,
            server_default="CBSE 2026-27",
        ),
    )
    op.add_column(
        "subjects",
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("true"),
        ),
    )
    op.add_column(
        "chapters",
        sa.Column(
            "curriculum_version",
            sa.String(length=32),
            nullable=False,
            server_default="CBSE 2026-27",
        ),
    )
    op.add_column(
        "chapters",
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("true"),
        ),
    )
    op.add_column(
        "topics",
        sa.Column(
            "curriculum_version",
            sa.String(length=32),
            nullable=False,
            server_default="CBSE 2026-27",
        ),
    )
    op.add_column(
        "topics",
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("true"),
        ),
    )


def downgrade() -> None:
    op.drop_column("topics", "is_active")
    op.drop_column("topics", "curriculum_version")
    op.drop_column("chapters", "is_active")
    op.drop_column("chapters", "curriculum_version")
    op.drop_column("subjects", "is_active")
    op.drop_column("subjects", "curriculum_version")
