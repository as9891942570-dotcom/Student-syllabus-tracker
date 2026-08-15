"""Idempotent CBSE 2026–27 syllabus seed (subjects / chapters / topics).

Upserts by stable subject code and chapter/topic titles. Unmatched placeholder
rows are deactivated, never deleted, so student progress and quiz attempts remain.
"""

from __future__ import annotations

from typing import Optional
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.data.cbse_2026_27.catalog import (
    all_cbse_scopes,
    subjects_for_scope,
    validate_catalog,
)
from app.data.cbse_2026_27.schema import CURRICULUM_VERSION, SubjectSpec
from app.models.board import Board
from app.models.chapter import Chapter
from app.models.school_class import SchoolClass
from app.models.stream import Stream
from app.models.subject import Subject
from app.models.topic import Topic
from app.services.academic_seed import seed_academic_lookups


def _chapter_map(subject: Subject) -> dict[str, Chapter]:
    return {chapter.title: chapter for chapter in subject.chapters}


def _topic_map(chapter: Chapter) -> dict[str, Topic]:
    return {topic.title: topic for topic in chapter.topics}


async def _load_scope_subjects(
    session: AsyncSession,
    *,
    board_id: UUID,
    class_id: UUID,
    stream_scope: str,
) -> list[Subject]:
    result = await session.execute(
        select(Subject)
        .where(
            Subject.board_id == board_id,
            Subject.class_id == class_id,
            Subject.stream_scope == stream_scope,
        )
        .options(selectinload(Subject.chapters).selectinload(Chapter.topics))
        .order_by(Subject.sort_order),
    )
    return list(result.scalars().unique().all())


async def _upsert_subject_tree(
    session: AsyncSession,
    *,
    board_id: UUID,
    class_id: UUID,
    stream_id: Optional[UUID],
    stream_scope: str,
    blueprint: list[SubjectSpec],
) -> None:
    existing = await _load_scope_subjects(
        session,
        board_id=board_id,
        class_id=class_id,
        stream_scope=stream_scope,
    )
    by_code = {subject.code: subject for subject in existing}
    seen_codes: set[str] = set()

    for subject_order, spec in enumerate(blueprint):
        seen_codes.add(spec["code"])
        subject = by_code.get(spec["code"])
        if subject is None:
            subject = Subject(
                name=spec["name"],
                code=spec["code"],
                board_id=board_id,
                class_id=class_id,
                stream_id=stream_id,
                stream_scope=stream_scope,
                sort_order=subject_order,
                curriculum_version=CURRICULUM_VERSION,
                is_active=True,
            )
            session.add(subject)
            await session.flush()
            by_code[spec["code"]] = subject
            chapters_by_title: dict[str, Chapter] = {}
        else:
            subject.name = spec["name"]
            subject.sort_order = subject_order
            subject.stream_id = stream_id
            subject.curriculum_version = CURRICULUM_VERSION
            subject.is_active = True
            chapters_by_title = _chapter_map(subject)

        seen_chapter_titles: set[str] = set()
        for chapter_order, chapter_spec in enumerate(spec["chapters"]):
            chapter_title = chapter_spec["title"]
            seen_chapter_titles.add(chapter_title)
            chapter = chapters_by_title.get(chapter_title)
            if chapter is None:
                chapter = Chapter(
                    subject_id=subject.id,
                    title=chapter_title,
                    sort_order=chapter_order,
                    curriculum_version=CURRICULUM_VERSION,
                    is_active=True,
                )
                session.add(chapter)
                await session.flush()
                chapters_by_title[chapter_title] = chapter
                topics_by_title: dict[str, Topic] = {}
            else:
                chapter.sort_order = chapter_order
                chapter.curriculum_version = CURRICULUM_VERSION
                chapter.is_active = True
                topics_by_title = _topic_map(chapter)

            seen_topic_titles: set[str] = set()
            for topic_order, topic_title in enumerate(chapter_spec["topics"]):
                seen_topic_titles.add(topic_title)
                topic = topics_by_title.get(topic_title)
                if topic is None:
                    topic = Topic(
                        chapter_id=chapter.id,
                        title=topic_title,
                        sort_order=topic_order,
                        curriculum_version=CURRICULUM_VERSION,
                        is_active=True,
                    )
                    session.add(topic)
                    await session.flush()
                    topics_by_title[topic_title] = topic
                else:
                    topic.sort_order = topic_order
                    topic.curriculum_version = CURRICULUM_VERSION
                    topic.is_active = True

            # Re-load every topic row for this chapter so concurrent duplicates are caught.
            chapter_topics = list(
                (
                    await session.execute(select(Topic).where(Topic.chapter_id == chapter.id))
                ).scalars().all(),
            )
            title_order = {title: idx for idx, title in enumerate(chapter_spec["topics"])}
            kept_titles: set[str] = set()
            for topic in sorted(
                chapter_topics,
                key=lambda item: (
                    0 if item.is_active else 1,
                    item.sort_order,
                    str(item.id),
                ),
            ):
                if topic.title not in seen_topic_titles:
                    topic.is_active = False
                    continue
                if topic.title in kept_titles:
                    topic.is_active = False
                    continue
                kept_titles.add(topic.title)
                topic.is_active = True
                topic.sort_order = title_order[topic.title]
                topic.curriculum_version = CURRICULUM_VERSION
                topics_by_title[topic.title] = topic

        # Deactivate unmatched chapters and collapse concurrent duplicate titles.
        subject_chapters = list(
            (
                await session.execute(select(Chapter).where(Chapter.subject_id == subject.id))
            ).scalars().all(),
        )
        chapter_order = {
            chapter_spec["title"]: idx for idx, chapter_spec in enumerate(spec["chapters"])
        }
        kept_chapter_titles: set[str] = set()
        for chapter in sorted(
            subject_chapters,
            key=lambda item: (
                0 if item.is_active else 1,
                item.sort_order,
                str(item.id),
            ),
        ):
            if chapter.title not in seen_chapter_titles:
                chapter.is_active = False
                for topic in (
                    await session.execute(select(Topic).where(Topic.chapter_id == chapter.id))
                ).scalars().all():
                    topic.is_active = False
                continue
            if chapter.title in kept_chapter_titles:
                chapter.is_active = False
                for topic in (
                    await session.execute(select(Topic).where(Topic.chapter_id == chapter.id))
                ).scalars().all():
                    topic.is_active = False
                continue
            kept_chapter_titles.add(chapter.title)
            chapter.is_active = True
            chapter.sort_order = chapter_order[chapter.title]
            chapter.curriculum_version = CURRICULUM_VERSION
            chapters_by_title[chapter.title] = chapter

    for subject in by_code.values():
        if subject.code not in seen_codes:
            subject.is_active = False
            for chapter in subject.chapters:
                chapter.is_active = False
                for topic in chapter.topics:
                    topic.is_active = False

    await session.flush()
    for subject in by_code.values():
        session.expire(subject)


async def seed_syllabus_for_scope(
    session: AsyncSession,
    *,
    board_id: UUID,
    class_id: UUID,
    stream_id: Optional[UUID],
    stream_code: Optional[str],
    grade: int,
) -> list[Subject]:
    stream_scope = stream_code if stream_code else "NONE"
    board = await session.get(Board, board_id)
    if board is None:
        return []

    blueprint = subjects_for_scope(grade, stream_code if grade >= 11 else None)
    if not blueprint:
        subjects = await _load_scope_subjects(
            session,
            board_id=board_id,
            class_id=class_id,
            stream_scope=stream_scope,
        )
        return [subject for subject in subjects if subject.is_active]

    await _upsert_subject_tree(
        session,
        board_id=board_id,
        class_id=class_id,
        stream_id=stream_id if grade >= 11 else None,
        stream_scope=stream_scope,
        blueprint=blueprint,
    )
    subjects = await _load_scope_subjects(
        session,
        board_id=board_id,
        class_id=class_id,
        stream_scope=stream_scope,
    )
    return [subject for subject in subjects if subject.is_active]


async def count_active_cbse_syllabus(session: AsyncSession) -> dict[str, int]:
    board_id = (
        await session.execute(select(Board.id).where(Board.code == "CBSE"))
    ).scalar_one_or_none()
    if board_id is None:
        return {
            "classes": 0,
            "streams": 0,
            "subjects": 0,
            "chapters": 0,
            "topics": 0,
        }

    classes = await session.scalar(select(func.count()).select_from(SchoolClass))
    streams = await session.scalar(select(func.count()).select_from(Stream))
    subjects = await session.scalar(
        select(func.count()).select_from(Subject).where(
            Subject.board_id == board_id,
            Subject.is_active.is_(True),
        ),
    )
    chapters = await session.scalar(
        select(func.count())
        .select_from(Chapter)
        .join(Subject, Chapter.subject_id == Subject.id)
        .where(Subject.board_id == board_id, Chapter.is_active.is_(True)),
    )
    topics = await session.scalar(
        select(func.count())
        .select_from(Topic)
        .join(Chapter, Topic.chapter_id == Chapter.id)
        .join(Subject, Chapter.subject_id == Subject.id)
        .where(Subject.board_id == board_id, Topic.is_active.is_(True)),
    )
    return {
        "classes": int(classes or 0),
        "streams": int(streams or 0),
        "subjects": int(subjects or 0),
        "chapters": int(chapters or 0),
        "topics": int(topics or 0),
    }


async def seed_all_cbse_syllabus(session: AsyncSession) -> dict[str, int]:
    """Seed every CBSE Class 6–12 scope. Safe to run repeatedly."""
    catalog_errors = validate_catalog()
    if catalog_errors:
        raise ValueError("Syllabus catalog failed validation:\n" + "\n".join(catalog_errors))

    await seed_academic_lookups(session)
    board = (
        await session.execute(select(Board).where(Board.code == "CBSE"))
    ).scalar_one()
    classes = {
        row.grade: row
        for row in (await session.execute(select(SchoolClass))).scalars().all()
    }
    streams = {
        row.code: row
        for row in (await session.execute(select(Stream))).scalars().all()
    }

    for grade, stream_code in all_cbse_scopes():
        school_class = classes[grade]
        stream = streams[stream_code] if stream_code else None
        await seed_syllabus_for_scope(
            session,
            board_id=board.id,
            class_id=school_class.id,
            stream_id=stream.id if stream else None,
            stream_code=stream_code,
            grade=grade,
        )
    return await count_active_cbse_syllabus(session)
