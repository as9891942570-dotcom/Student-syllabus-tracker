"""Create syllabus tracking tables.

Revision ID: 0003_syllabus
Revises: 0002_profile
Create Date: 2026-08-06
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "0003_syllabus"
down_revision: Union[str, None] = "0002_profile"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "subjects",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("code", sa.String(length=32), nullable=False),
        sa.Column("board_id", sa.Uuid(), nullable=False),
        sa.Column("class_id", sa.Uuid(), nullable=False),
        sa.Column("stream_id", sa.Uuid(), nullable=True),
        sa.Column("stream_scope", sa.String(length=32), nullable=False, server_default="NONE"),
        sa.Column("sort_order", sa.Integer(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["board_id"], ["boards.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["class_id"], ["classes.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["stream_id"], ["streams.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "board_id",
            "class_id",
            "stream_scope",
            "code",
            name="uq_subjects_board_class_scope_code",
        ),
    )
    op.create_index(op.f("ix_subjects_board_id"), "subjects", ["board_id"])
    op.create_index(op.f("ix_subjects_class_id"), "subjects", ["class_id"])
    op.create_index(op.f("ix_subjects_stream_id"), "subjects", ["stream_id"])
    op.create_index(
        "ix_subjects_board_class_scope",
        "subjects",
        ["board_id", "class_id", "stream_scope"],
    )

    op.create_table(
        "chapters",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("subject_id", sa.Uuid(), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("sort_order", sa.Integer(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["subject_id"], ["subjects.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_chapters_subject_id"), "chapters", ["subject_id"])

    op.create_table(
        "topics",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("chapter_id", sa.Uuid(), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("sort_order", sa.Integer(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["chapter_id"], ["chapters.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_topics_chapter_id"), "topics", ["chapter_id"])

    op.create_table(
        "student_topic_progress",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("topic_id", sa.Uuid(), nullable=False),
        sa.Column("is_completed", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["topic_id"], ["topics.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "topic_id", name="uq_student_topic_progress"),
    )
    op.create_index(
        op.f("ix_student_topic_progress_user_id"),
        "student_topic_progress",
        ["user_id"],
    )
    op.create_index(
        op.f("ix_student_topic_progress_topic_id"),
        "student_topic_progress",
        ["topic_id"],
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_student_topic_progress_topic_id"), table_name="student_topic_progress")
    op.drop_index(op.f("ix_student_topic_progress_user_id"), table_name="student_topic_progress")
    op.drop_table("student_topic_progress")
    op.drop_index(op.f("ix_topics_chapter_id"), table_name="topics")
    op.drop_table("topics")
    op.drop_index(op.f("ix_chapters_subject_id"), table_name="chapters")
    op.drop_table("chapters")
    op.drop_index("ix_subjects_board_class_scope", table_name="subjects")
    op.drop_index(op.f("ix_subjects_stream_id"), table_name="subjects")
    op.drop_index(op.f("ix_subjects_class_id"), table_name="subjects")
    op.drop_index(op.f("ix_subjects_board_id"), table_name="subjects")
    op.drop_table("subjects")
