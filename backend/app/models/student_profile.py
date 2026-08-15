"""Student profile ORM model."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import DateTime, ForeignKey, Integer, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.board import Board
    from app.models.school_class import SchoolClass
    from app.models.stream import Stream
    from app.models.user import User


class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
        index=True,
    )
    mobile: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
    photo_url: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    board_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        Uuid,
        ForeignKey("boards.id", ondelete="SET NULL"),
        nullable=True,
    )
    class_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        Uuid,
        ForeignKey("classes.id", ondelete="SET NULL"),
        nullable=True,
    )
    stream_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        Uuid,
        ForeignKey("streams.id", ondelete="SET NULL"),
        nullable=True,
    )
    total_xp: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    total_coins: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    user: Mapped[User] = relationship("User", back_populates="profile")
    board: Mapped[Optional[Board]] = relationship("Board", back_populates="profiles")
    school_class: Mapped[Optional[SchoolClass]] = relationship(
        "SchoolClass",
        back_populates="profiles",
    )
    stream: Mapped[Optional[Stream]] = relationship("Stream", back_populates="profiles")
