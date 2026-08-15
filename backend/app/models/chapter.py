"""Chapter model under a subject."""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.subject import Subject
    from app.models.topic import Topic


class Chapter(Base):
    __tablename__ = "chapters"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    subject_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("subjects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    curriculum_version: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="CBSE 2026-27",
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    subject: Mapped[Subject] = relationship("Subject", back_populates="chapters")
    topics: Mapped[list[Topic]] = relationship(
        "Topic",
        back_populates="chapter",
        cascade="all, delete-orphan",
        order_by="Topic.sort_order",
    )
