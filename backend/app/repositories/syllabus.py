"""Syllabus data-access repositories."""

from typing import Optional, Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.chapter import Chapter
from app.models.student_topic_progress import StudentTopicProgress
from app.models.subject import Subject
from app.models.topic import Topic
from app.repositories.base import BaseRepository


class SubjectRepository(BaseRepository[Subject]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Subject, session)

    async def get_with_tree(self, subject_id: UUID) -> Optional[Subject]:
        result = await self.session.execute(
            select(Subject)
            .where(Subject.id == subject_id)
            .options(selectinload(Subject.chapters).selectinload(Chapter.topics)),
        )
        return result.scalar_one_or_none()

    async def list_for_scope(
        self,
        *,
        board_id: UUID,
        class_id: UUID,
        stream_scope: str,
    ) -> Sequence[Subject]:
        result = await self.session.execute(
            select(Subject)
            .where(
                Subject.board_id == board_id,
                Subject.class_id == class_id,
                Subject.stream_scope == stream_scope,
            )
            .options(selectinload(Subject.chapters).selectinload(Chapter.topics))
            .order_by(Subject.sort_order),
        )
        return result.scalars().all()


class ChapterRepository(BaseRepository[Chapter]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Chapter, session)

    async def get_with_topics(self, chapter_id: UUID) -> Optional[Chapter]:
        result = await self.session.execute(
            select(Chapter)
            .where(Chapter.id == chapter_id)
            .options(selectinload(Chapter.topics), selectinload(Chapter.subject)),
        )
        return result.scalar_one_or_none()

    async def list_by_subject(self, subject_id: UUID) -> Sequence[Chapter]:
        result = await self.session.execute(
            select(Chapter)
            .where(Chapter.subject_id == subject_id)
            .options(selectinload(Chapter.topics))
            .order_by(Chapter.sort_order),
        )
        return result.scalars().all()


class TopicRepository(BaseRepository[Topic]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Topic, session)

    async def get_with_chapter(self, topic_id: UUID) -> Optional[Topic]:
        result = await self.session.execute(
            select(Topic)
            .where(Topic.id == topic_id)
            .options(selectinload(Topic.chapter).selectinload(Chapter.subject)),
        )
        return result.scalar_one_or_none()


class TopicProgressRepository(BaseRepository[StudentTopicProgress]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(StudentTopicProgress, session)

    async def get_for_user_topic(
        self,
        user_id: UUID,
        topic_id: UUID,
    ) -> Optional[StudentTopicProgress]:
        result = await self.session.execute(
            select(StudentTopicProgress).where(
                StudentTopicProgress.user_id == user_id,
                StudentTopicProgress.topic_id == topic_id,
            ),
        )
        return result.scalar_one_or_none()

    async def map_for_user(
        self,
        user_id: UUID,
        topic_ids: Sequence[UUID],
    ) -> dict[UUID, StudentTopicProgress]:
        if not topic_ids:
            return {}
        result = await self.session.execute(
            select(StudentTopicProgress).where(
                StudentTopicProgress.user_id == user_id,
                StudentTopicProgress.topic_id.in_(list(topic_ids)),
            ),
        )
        rows = result.scalars().all()
        return {row.topic_id: row for row in rows}
