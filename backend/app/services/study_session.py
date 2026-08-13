"""Gamified study session business logic."""

from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.exceptions import ConflictError, NotFoundError, ValidationAppError
from app.models.study_session import StudySession
from app.models.user import User
from app.repositories.profile import StudentProfileRepository
from app.repositories.study_session import StudySessionRepository
from app.repositories.syllabus import TopicRepository
from app.schemas.study_session import (
    CompleteSessionRequest,
    SessionActivityRequest,
    StartSessionRequest,
    StudySessionResponse,
)
from app.services.academic_seed import seed_academic_lookups
from app.services.syllabus import SyllabusService
from app.services.syllabus_seed import seed_syllabus_for_scope
from app.services.xp import award_xp


def calculate_session_score(correct: int, incorrect: int) -> int:
    total = correct + incorrect
    if total <= 0:
        return 50
    return int(round((correct / total) * 100))


def calculate_session_xp(
    *,
    duration_seconds: int,
    score: int,
    correct_count: int,
) -> int:
    base = 15
    duration_minutes = max(duration_seconds, 0) // 60
    duration_bonus = min(duration_minutes, 20) * 2
    score_bonus = int((max(0, min(score, 100)) / 100) * 20)
    correct_bonus = min(correct_count, 20) * 2
    return base + duration_bonus + score_bonus + correct_bonus


class StudySessionService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.sessions = StudySessionRepository(session)
        self.profiles = StudentProfileRepository(session)
        self.topics = TopicRepository(session)
        self.syllabus = SyllabusService(session)
        self.settings = get_settings()

    async def start(self, user: User, payload: StartSessionRequest) -> StudySessionResponse:
        profile = await self.syllabus._require_profile(user)
        await seed_academic_lookups(self.session)
        await seed_syllabus_for_scope(
            self.session,
            board_id=profile.board_id,  # type: ignore[arg-type]
            class_id=profile.class_id,  # type: ignore[arg-type]
            stream_id=profile.stream_id,
            stream_code=profile.stream.code if profile.stream else None,
            grade=profile.school_class.grade,  # type: ignore[union-attr]
        )

        active = await self.sessions.get_active_for_user(user.id)
        if active is not None:
            raise ConflictError(
                "You already have an active study session. Complete it before starting another.",
            )

        topic = await self.topics.get_with_chapter(payload.topic_id)
        if topic is None:
            raise NotFoundError("Topic not found")
        self.syllabus._assert_subject_in_scope(profile, topic.chapter.subject)

        study_session = StudySession(
            user_id=user.id,
            subject_id=topic.chapter.subject_id,
            chapter_id=topic.chapter_id,
            topic_id=topic.id,
            status="active",
            started_at=datetime.now(timezone.utc),
        )
        study_session = await self.sessions.create(study_session)
        loaded = await self.sessions.get_for_user(study_session.id, user.id)
        assert loaded is not None
        return self._to_response(loaded, profile.total_xp)

    async def get_active(self, user: User) -> StudySessionResponse | None:
        profile = await self.profiles.get_by_user_id(user.id)
        total_xp = profile.total_xp if profile else 0
        active = await self.sessions.get_active_for_user(user.id)
        if active is None:
            return None
        return self._to_response(active, total_xp)

    async def record_activity(
        self,
        user: User,
        session_id,
        payload: SessionActivityRequest,
    ) -> StudySessionResponse:
        profile = await self.profiles.get_by_user_id(user.id)
        if profile is None:
            raise ValidationAppError("Complete your student profile first")

        study_session = await self.sessions.get_for_user(session_id, user.id)
        if study_session is None:
            raise NotFoundError("Study session not found")
        if study_session.status != "active":
            raise ValidationAppError("Only active sessions can record activity")

        if payload.result == "correct":
            study_session.correct_count += 1
        else:
            study_session.incorrect_count += 1
        study_session.score = calculate_session_score(
            study_session.correct_count,
            study_session.incorrect_count,
        )
        await self.sessions.update(study_session)
        return self._to_response(study_session, profile.total_xp)

    async def complete(
        self,
        user: User,
        session_id,
        payload: CompleteSessionRequest,
    ) -> StudySessionResponse:
        profile = await self.profiles.get_by_user_id(user.id)
        if profile is None:
            raise ValidationAppError("Complete your student profile first")

        study_session = await self.sessions.get_for_user(session_id, user.id)
        if study_session is None:
            raise NotFoundError("Study session not found")
        if study_session.status != "active":
            raise ValidationAppError("Session is already completed")

        if payload.correct_count is not None:
            study_session.correct_count = payload.correct_count
        if payload.incorrect_count is not None:
            study_session.incorrect_count = payload.incorrect_count

        ended_at = datetime.now(timezone.utc)
        started = study_session.started_at
        if started.tzinfo is None:
            started = started.replace(tzinfo=timezone.utc)
        duration = max(int((ended_at - started).total_seconds()), 0)

        score = calculate_session_score(
            study_session.correct_count,
            study_session.incorrect_count,
        )
        xp = calculate_session_xp(
            duration_seconds=duration,
            score=score,
            correct_count=study_session.correct_count,
        )

        study_session.ended_at = ended_at
        study_session.duration_seconds = duration
        study_session.score = score
        study_session.xp_earned = xp
        study_session.status = "completed"
        await self.sessions.update(study_session)

        total_xp = await award_xp(
            self.session,
            user_id=user.id,
            xp_amount=xp,
            study_seconds=duration,
            count_as_session=True,
        )

        # Mark topic complete as part of a finished quest (tracking only).
        from app.schemas.syllabus import TopicProgressUpdate

        await self.syllabus.set_topic_progress(
            user,
            study_session.topic_id,
            TopicProgressUpdate(is_completed=True),
        )

        loaded = await self.sessions.get_for_user(study_session.id, user.id)
        assert loaded is not None
        return self._to_response(loaded, total_xp)

    async def get_session(self, user: User, session_id) -> StudySessionResponse:
        profile = await self.profiles.get_by_user_id(user.id)
        total_xp = profile.total_xp if profile else 0
        study_session = await self.sessions.get_for_user(session_id, user.id)
        if study_session is None:
            raise NotFoundError("Study session not found")
        return self._to_response(study_session, total_xp)

    def _to_response(
        self,
        study_session: StudySession,
        total_xp: int,
    ) -> StudySessionResponse:
        return StudySessionResponse(
            id=study_session.id,
            status=study_session.status,
            subject_id=study_session.subject_id,
            subject_name=study_session.subject.name,
            chapter_id=study_session.chapter_id,
            chapter_title=study_session.chapter.title,
            topic_id=study_session.topic_id,
            topic_title=study_session.topic.title,
            started_at=study_session.started_at,
            ended_at=study_session.ended_at,
            duration_seconds=study_session.duration_seconds,
            score=study_session.score,
            correct_count=study_session.correct_count,
            incorrect_count=study_session.incorrect_count,
            xp_earned=study_session.xp_earned,
            total_xp=total_xp,
        )
