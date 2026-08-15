"""Student progression overview (XP, level, current/next topics)."""

from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories.profile import StudentProfileRepository
from app.schemas.progression import ProgressionResponse, ProgressionTopicSummary
from app.services.level import calculate_level_progress
from app.services.syllabus import SyllabusService, _visible_chapters, _visible_topics


class ProgressionService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.profiles = StudentProfileRepository(session)
        self.syllabus = SyllabusService(session)

    async def get_me(self, user: User) -> ProgressionResponse:
        profile = await self.syllabus._require_profile(user)
        subjects = await self.syllabus._ensure_subjects(profile)
        progress_map = await self.syllabus._progress_map(user.id, subjects)
        total_xp = profile.total_xp or 0
        level = calculate_level_progress(total_xp)

        summaries: list[ProgressionTopicSummary] = []
        for subject in subjects:
            for chapter in _visible_chapters(subject):
                for topic in self.syllabus._topic_responses_for_chapter(
                    _visible_topics(chapter),
                    progress_map,
                ):
                    summaries.append(
                        ProgressionTopicSummary(
                            id=topic.id,
                            title=topic.title,
                            chapter_id=chapter.id,
                            chapter_title=chapter.title,
                            subject_id=subject.id,
                            subject_name=subject.name,
                            sort_order=topic.sort_order,
                            is_completed=topic.is_completed,
                            is_locked=topic.is_locked,
                            is_current=topic.is_current,
                        ),
                    )

        completed = [t for t in summaries if t.is_completed]
        current = next((t for t in summaries if t.is_current), None)
        next_topic = None
        if current is not None:
            seen_current = False
            for topic in summaries:
                if topic.id == current.id:
                    seen_current = True
                    continue
                if seen_current and not topic.is_completed:
                    next_topic = topic
                    break
        elif summaries:
            # All remaining locked or all complete — first incomplete if any.
            next_topic = next((t for t in summaries if not t.is_completed), None)

        total_topics = len(summaries)
        completed_count = len(completed)
        overall = (
            int(round(completed_count / total_topics * 100)) if total_topics else 0
        )

        return ProgressionResponse(
            total_xp=level.total_xp,
            total_coins=profile.total_coins or 0,
            level=level.level,
            level_floor_xp=level.level_floor_xp,
            next_level_xp=level.next_level_xp,
            xp_into_level=level.xp_into_level,
            xp_needed_for_next=level.xp_needed_for_next,
            level_progress_percentage=level.level_progress_percentage,
            overall_completion_percentage=overall,
            completed_topic_count=completed_count,
            total_topic_count=total_topics,
            current_topic=current,
            next_topic=next_topic,
            completed_topics=completed,
        )
