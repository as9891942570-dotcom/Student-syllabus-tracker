"""Quiz repositories."""

from __future__ import annotations

from typing import Optional
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.chapter import Chapter
from app.models.quiz import Quiz
from app.models.quiz_answer import QuizAnswer
from app.models.quiz_attempt import QuizAttempt
from app.models.quiz_option import QuizOption
from app.models.quiz_question import QuizQuestion
from app.models.topic import Topic
from app.repositories.base import BaseRepository


class QuizRepository(BaseRepository[Quiz]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Quiz, session)

    async def list_for_topic(self, topic_id: UUID) -> list[Quiz]:
        result = await self.session.execute(
            select(Quiz)
            .where(Quiz.topic_id == topic_id, Quiz.is_active.is_(True))
            .options(selectinload(Quiz.questions))
            .order_by(Quiz.sort_order, Quiz.title),
        )
        return list(result.scalars().unique().all())

    async def get_with_questions(self, quiz_id: UUID) -> Optional[Quiz]:
        result = await self.session.execute(
            select(Quiz)
            .where(Quiz.id == quiz_id)
            .options(
                selectinload(Quiz.questions).selectinload(QuizQuestion.options),
                selectinload(Quiz.topic)
                .selectinload(Topic.chapter)
                .selectinload(Chapter.subject),
            ),
        )
        return result.scalar_one_or_none()


class QuizQuestionRepository(BaseRepository[QuizQuestion]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(QuizQuestion, session)

    async def get_with_options(self, question_id: UUID) -> Optional[QuizQuestion]:
        result = await self.session.execute(
            select(QuizQuestion)
            .where(QuizQuestion.id == question_id)
            .options(selectinload(QuizQuestion.options)),
        )
        return result.scalar_one_or_none()


class QuizOptionRepository(BaseRepository[QuizOption]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(QuizOption, session)


class QuizAttemptRepository(BaseRepository[QuizAttempt]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(QuizAttempt, session)

    def _load_options(self):
        return [
            selectinload(QuizAttempt.answers),
            selectinload(QuizAttempt.quiz)
            .selectinload(Quiz.questions)
            .selectinload(QuizQuestion.options),
            selectinload(QuizAttempt.quiz)
            .selectinload(Quiz.topic)
            .selectinload(Topic.chapter)
            .selectinload(Chapter.subject),
        ]

    async def get_active_for_user(self, user_id: UUID) -> Optional[QuizAttempt]:
        result = await self.session.execute(
            select(QuizAttempt)
            .where(QuizAttempt.user_id == user_id, QuizAttempt.status == "active")
            .options(*self._load_options())
            .limit(1),
        )
        return result.scalar_one_or_none()

    async def get_for_user(
        self,
        attempt_id: UUID,
        user_id: UUID,
    ) -> Optional[QuizAttempt]:
        result = await self.session.execute(
            select(QuizAttempt)
            .where(QuizAttempt.id == attempt_id, QuizAttempt.user_id == user_id)
            .options(*self._load_options()),
        )
        return result.scalar_one_or_none()

    async def list_history(self, user_id: UUID, *, limit: int = 50) -> list[QuizAttempt]:
        result = await self.session.execute(
            select(QuizAttempt)
            .where(QuizAttempt.user_id == user_id)
            .options(
                selectinload(QuizAttempt.quiz)
                .selectinload(Quiz.topic)
                .selectinload(Topic.chapter)
                .selectinload(Chapter.subject),
            )
            .order_by(QuizAttempt.started_at.desc())
            .limit(limit),
        )
        return list(result.scalars().unique().all())

    async def has_prior_xp_for_quiz(
        self,
        user_id: UUID,
        quiz_id: UUID,
        *,
        exclude_attempt_id: UUID | None = None,
    ) -> bool:
        """True if the student already earned XP from a finished attempt on this quiz."""
        stmt = select(func.count()).select_from(QuizAttempt).where(
            QuizAttempt.user_id == user_id,
            QuizAttempt.quiz_id == quiz_id,
            QuizAttempt.status.in_(("completed", "expired")),
            QuizAttempt.xp_earned > 0,
        )
        if exclude_attempt_id is not None:
            stmt = stmt.where(QuizAttempt.id != exclude_attempt_id)
        result = await self.session.execute(stmt)
        return int(result.scalar_one()) > 0


class QuizAnswerRepository(BaseRepository[QuizAnswer]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(QuizAnswer, session)

    async def get_for_attempt_question(
        self,
        attempt_id: UUID,
        question_id: UUID,
    ) -> Optional[QuizAnswer]:
        result = await self.session.execute(
            select(QuizAnswer).where(
                QuizAnswer.attempt_id == attempt_id,
                QuizAnswer.question_id == question_id,
            ),
        )
        return result.scalar_one_or_none()
