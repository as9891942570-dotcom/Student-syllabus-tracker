"""School class (grade 6–12) lookup model."""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.student_profile import StudentProfile


class SchoolClass(Base):
    __tablename__ = "classes"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    grade: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(64), nullable=False)

    profiles: Mapped[list[StudentProfile]] = relationship(
        "StudentProfile",
        back_populates="school_class",
    )

    @property
    def requires_stream(self) -> bool:
        return self.grade >= 11
