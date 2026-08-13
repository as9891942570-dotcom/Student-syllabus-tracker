"""Subject model (syllabus tracking only — no teaching content)."""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, Integer, String, UniqueConstraint, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.board import Board
    from app.models.chapter import Chapter
    from app.models.school_class import SchoolClass
    from app.models.stream import Stream


class Subject(Base):
    __tablename__ = "subjects"
    __table_args__ = (
        UniqueConstraint(
            "board_id",
            "class_id",
            "stream_scope",
            "code",
            name="uq_subjects_board_class_scope_code",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    code: Mapped[str] = mapped_column(String(32), nullable=False)
    board_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("boards.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    class_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("classes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    stream_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        Uuid,
        ForeignKey("streams.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )
    # Non-null scope key so uniqueness works for Classes 6–10 (no stream).
    stream_scope: Mapped[str] = mapped_column(String(32), nullable=False, default="NONE")
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    board: Mapped[Board] = relationship("Board")
    school_class: Mapped[SchoolClass] = relationship("SchoolClass")
    stream: Mapped[Optional[Stream]] = relationship("Stream")
    chapters: Mapped[list[Chapter]] = relationship(
        "Chapter",
        back_populates="subject",
        cascade="all, delete-orphan",
        order_by="Chapter.sort_order",
    )
