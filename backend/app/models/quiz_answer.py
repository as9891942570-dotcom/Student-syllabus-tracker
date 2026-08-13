"""Per-question answer within a quiz attempt."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Boolean, DateTime, ForeignKey, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.quiz_attempt import QuizAttempt
    from app.models.quiz_option import QuizOption
    from app.models.quiz_question import QuizQuestion


class QuizAnswer(Base):
    __tablename__ = "quiz_answers"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    attempt_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("quiz_attempts.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    question_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("quiz_questions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    selected_option_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        Uuid,
        ForeignKey("quiz_options.id", ondelete="SET NULL"),
        nullable=True,
    )
    is_correct: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    answered_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    attempt: Mapped[QuizAttempt] = relationship("QuizAttempt", back_populates="answers")
    question: Mapped[QuizQuestion] = relationship("QuizQuestion")
    selected_option: Mapped[Optional[QuizOption]] = relationship("QuizOption")
