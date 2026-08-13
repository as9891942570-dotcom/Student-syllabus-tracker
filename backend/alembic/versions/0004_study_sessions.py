"""Add study sessions, daily activity, and profile XP.

Revision ID: 0004_study_sessions
Revises: 0003_syllabus
Create Date: 2026-08-08
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "0004_study_sessions"
down_revision: Union[str, None] = "0003_syllabus"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "student_profiles",
        sa.Column("total_xp", sa.Integer(), nullable=False, server_default="0"),
    )

    op.create_table(
        "study_sessions",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("subject_id", sa.Uuid(), nullable=False),
        sa.Column("chapter_id", sa.Uuid(), nullable=False),
        sa.Column("topic_id", sa.Uuid(), nullable=False),
        sa.Column("status", sa.String(length=20), nullable=False, server_default="active"),
        sa.Column(
            "started_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("ended_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("duration_seconds", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("score", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("correct_count", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("incorrect_count", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("xp_earned", sa.Integer(), nullable=False, server_default="0"),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["chapter_id"], ["chapters.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["subject_id"], ["subjects.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["topic_id"], ["topics.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_study_sessions_user_id"), "study_sessions", ["user_id"])
    op.create_index(op.f("ix_study_sessions_subject_id"), "study_sessions", ["subject_id"])
    op.create_index(op.f("ix_study_sessions_chapter_id"), "study_sessions", ["chapter_id"])
    op.create_index(op.f("ix_study_sessions_topic_id"), "study_sessions", ["topic_id"])
    op.create_index(
        "ix_study_sessions_user_status",
        "study_sessions",
        ["user_id", "status"],
    )

    op.create_table(
        "daily_activities",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("activity_date", sa.Date(), nullable=False),
        sa.Column("sessions_completed", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("study_seconds", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("xp_earned", sa.Integer(), nullable=False, server_default="0"),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "activity_date", name="uq_daily_activity_user_date"),
    )
    op.create_index(op.f("ix_daily_activities_user_id"), "daily_activities", ["user_id"])
    op.create_index(
        op.f("ix_daily_activities_activity_date"),
        "daily_activities",
        ["activity_date"],
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_daily_activities_activity_date"), table_name="daily_activities")
    op.drop_index(op.f("ix_daily_activities_user_id"), table_name="daily_activities")
    op.drop_table("daily_activities")
    op.drop_index("ix_study_sessions_user_status", table_name="study_sessions")
    op.drop_index(op.f("ix_study_sessions_topic_id"), table_name="study_sessions")
    op.drop_index(op.f("ix_study_sessions_chapter_id"), table_name="study_sessions")
    op.drop_index(op.f("ix_study_sessions_subject_id"), table_name="study_sessions")
    op.drop_index(op.f("ix_study_sessions_user_id"), table_name="study_sessions")
    op.drop_table("study_sessions")
    op.drop_column("student_profiles", "total_xp")
