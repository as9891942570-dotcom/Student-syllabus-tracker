"""Syllabus tracking service."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import ForbiddenError, NotFoundError, ValidationAppError
from app.models.chapter import Chapter
from app.models.student_profile import StudentProfile
from app.models.student_topic_progress import StudentTopicProgress
from app.models.subject import Subject
from app.models.topic import Topic
from app.models.user import User
from app.repositories.profile import StudentProfileRepository
from app.repositories.syllabus import (
    ChapterRepository,
    SubjectRepository,
    TopicProgressRepository,
    TopicRepository,
)
from app.schemas.syllabus import (
    ChapterResponse,
    SubjectDetailResponse,
    SubjectResponse,
    SyllabusCompletionResponse,
    SyllabusStructureResponse,
    TopicProgressUpdate,
    TopicResponse,
)
from app.services.academic_seed import seed_academic_lookups
from app.services.syllabus_seed import seed_syllabus_for_scope


def _pct(completed: int, total: int) -> int:
    if total <= 0:
        return 0
    return int(round((completed / total) * 100))


class SyllabusService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.profiles = StudentProfileRepository(session)
        self.subjects = SubjectRepository(session)
        self.chapters = ChapterRepository(session)
        self.topics = TopicRepository(session)
        self.progress = TopicProgressRepository(session)

    async def _require_profile(self, user: User) -> StudentProfile:
        await seed_academic_lookups(self.session)
        profile = await self.profiles.get_by_user_id(user.id)
        if profile is None:
            raise ValidationAppError("Complete your student profile first")
        if not profile.board_id or not profile.class_id:
            raise ValidationAppError("Select board and class in your profile first")
        if profile.school_class and profile.school_class.requires_stream and not profile.stream_id:
            raise ValidationAppError("Select a stream in your profile first")
        return profile

    async def _ensure_subjects(self, profile: StudentProfile) -> list[Subject]:
        assert profile.board_id and profile.class_id and profile.school_class
        stream_code = profile.stream.code if profile.stream else None
        return await seed_syllabus_for_scope(
            self.session,
            board_id=profile.board_id,
            class_id=profile.class_id,
            stream_id=profile.stream_id,
            stream_code=stream_code,
            grade=profile.school_class.grade,
        )

    async def _progress_map(
        self,
        user_id: UUID,
        subjects: list[Subject],
    ) -> dict[UUID, StudentTopicProgress]:
        topic_ids = [
            topic.id
            for subject in subjects
            for chapter in subject.chapters
            for topic in chapter.topics
        ]
        return await self.progress.map_for_user(user_id, topic_ids)

    def _topic_response(
        self,
        topic: Topic,
        progress_map: dict[UUID, StudentTopicProgress],
    ) -> TopicResponse:
        row = progress_map.get(topic.id)
        return TopicResponse(
            id=topic.id,
            title=topic.title,
            sort_order=topic.sort_order,
            is_completed=bool(row and row.is_completed),
            completed_at=row.completed_at if row else None,
        )

    def _chapter_response(
        self,
        chapter: Chapter,
        progress_map: dict[UUID, StudentTopicProgress],
        *,
        include_topics: bool,
    ) -> ChapterResponse:
        topic_responses = [
            self._topic_response(topic, progress_map) for topic in chapter.topics
        ]
        completed = sum(1 for t in topic_responses if t.is_completed)
        total = len(topic_responses)
        return ChapterResponse(
            id=chapter.id,
            title=chapter.title,
            sort_order=chapter.sort_order,
            topic_count=total,
            completed_topic_count=completed,
            completion_percentage=_pct(completed, total),
            topics=topic_responses if include_topics else [],
        )

    def _subject_response(
        self,
        subject: Subject,
        progress_map: dict[UUID, StudentTopicProgress],
        *,
        include_chapters: bool,
        include_topics: bool,
    ) -> SubjectDetailResponse | SubjectResponse:
        chapters = [
            self._chapter_response(ch, progress_map, include_topics=include_topics)
            for ch in subject.chapters
        ]
        topic_count = sum(c.topic_count for c in chapters)
        completed = sum(c.completed_topic_count for c in chapters)
        base = dict(
            id=subject.id,
            name=subject.name,
            code=subject.code,
            sort_order=subject.sort_order,
            chapter_count=len(chapters),
            topic_count=topic_count,
            completed_topic_count=completed,
            completion_percentage=_pct(completed, topic_count),
        )
        if include_chapters:
            return SubjectDetailResponse(**base, chapters=chapters)
        return SubjectResponse(**base)

    async def list_subjects(self, user: User) -> list[SubjectResponse]:
        profile = await self._require_profile(user)
        subjects = await self._ensure_subjects(profile)
        progress_map = await self._progress_map(user.id, subjects)
        return [
            self._subject_response(
                s,
                progress_map,
                include_chapters=False,
                include_topics=False,
            )
            for s in subjects
        ]

    async def get_subject_chapters(self, user: User, subject_id: UUID) -> SubjectDetailResponse:
        profile = await self._require_profile(user)
        await self._ensure_subjects(profile)
        subject = await self.subjects.get_with_tree(subject_id)
        if subject is None:
            raise NotFoundError("Subject not found")
        self._assert_subject_in_scope(profile, subject)
        progress_map = await self._progress_map(user.id, [subject])
        detail = self._subject_response(
            subject,
            progress_map,
            include_chapters=True,
            include_topics=False,
        )
        assert isinstance(detail, SubjectDetailResponse)
        return detail

    async def get_chapter_topics(self, user: User, chapter_id: UUID) -> ChapterResponse:
        profile = await self._require_profile(user)
        await self._ensure_subjects(profile)
        chapter = await self.chapters.get_with_topics(chapter_id)
        if chapter is None:
            raise NotFoundError("Chapter not found")
        self._assert_subject_in_scope(profile, chapter.subject)
        progress_map = await self.progress.map_for_user(
            user.id,
            [t.id for t in chapter.topics],
        )
        return self._chapter_response(chapter, progress_map, include_topics=True)

    async def get_structure(self, user: User) -> SyllabusStructureResponse:
        profile = await self._require_profile(user)
        subjects = await self._ensure_subjects(profile)
        progress_map = await self._progress_map(user.id, subjects)
        details: list[SubjectDetailResponse] = []
        total_topics = 0
        completed_topics = 0
        for subject in subjects:
            detail = self._subject_response(
                subject,
                progress_map,
                include_chapters=True,
                include_topics=True,
            )
            assert isinstance(detail, SubjectDetailResponse)
            details.append(detail)
            total_topics += detail.topic_count
            completed_topics += detail.completed_topic_count
        return SyllabusStructureResponse(
            subjects=details,
            overall_completion_percentage=_pct(completed_topics, total_topics),
            total_topics=total_topics,
            completed_topics=completed_topics,
        )

    async def get_completion(self, user: User) -> SyllabusCompletionResponse:
        subjects = await self.list_subjects(user)
        total_topics = sum(s.topic_count for s in subjects)
        completed_topics = sum(s.completed_topic_count for s in subjects)
        total_chapters = sum(s.chapter_count for s in subjects)
        return SyllabusCompletionResponse(
            overall_completion_percentage=_pct(completed_topics, total_topics),
            total_subjects=len(subjects),
            total_chapters=total_chapters,
            total_topics=total_topics,
            completed_topics=completed_topics,
            subjects=subjects,
        )

    async def set_topic_progress(
        self,
        user: User,
        topic_id: UUID,
        payload: TopicProgressUpdate,
    ) -> TopicResponse:
        profile = await self._require_profile(user)
        await self._ensure_subjects(profile)
        topic = await self.topics.get_with_chapter(topic_id)
        if topic is None:
            raise NotFoundError("Topic not found")
        self._assert_subject_in_scope(profile, topic.chapter.subject)

        row = await self.progress.get_for_user_topic(user.id, topic_id)
        now = datetime.now(timezone.utc)
        if row is None:
            row = StudentTopicProgress(
                user_id=user.id,
                topic_id=topic_id,
                is_completed=payload.is_completed,
                completed_at=now if payload.is_completed else None,
            )
            await self.progress.create(row)
        else:
            row.is_completed = payload.is_completed
            row.completed_at = now if payload.is_completed else None
            await self.progress.update(row)

        return TopicResponse(
            id=topic.id,
            title=topic.title,
            sort_order=topic.sort_order,
            is_completed=row.is_completed,
            completed_at=row.completed_at,
        )

    def _assert_subject_in_scope(self, profile: StudentProfile, subject: Subject) -> None:
        if subject.board_id != profile.board_id or subject.class_id != profile.class_id:
            raise ForbiddenError("Subject is outside your profile syllabus")
        expected_scope = profile.stream.code if profile.stream else "NONE"
        if subject.stream_scope != expected_scope:
            raise ForbiddenError("Subject is outside your profile syllabus")
