"""Topic model under a chapter (completion tracking unit)."""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.chapter import Chapter
    from app.models.student_topic_progress import StudentTopicProgress


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    chapter_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("chapters.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    chapter: Mapped[Chapter] = relationship("Chapter", back_populates="topics")
    progress_rows: Mapped[list[StudentTopicProgress]] = relationship(
        "StudentTopicProgress",
        back_populates="topic",
        cascade="all, delete-orphan",
    )
