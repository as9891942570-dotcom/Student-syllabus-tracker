"""Phase 8 CBSE 2026–27 syllabus database tests."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data.cbse_2026_27.catalog import (
    STREAM_CODES,
    subjects_for_scope,
    validate_catalog,
)
from app.data.cbse_2026_27.schema import CURRICULUM_VERSION
from app.models.board import Board
from app.models.chapter import Chapter
from app.models.school_class import SchoolClass
from app.models.stream import Stream
from app.models.student_topic_progress import StudentTopicProgress
from app.models.subject import Subject
from app.models.topic import Topic
from app.schemas.auth import RegisterRequest
from app.schemas.profile import ProfileUpdateRequest
from app.services.academic_seed import seed_academic_lookups
from app.services.auth import AuthService
from app.services.profile import ProfileService
from app.services.syllabus import SyllabusService
from app.services.syllabus_seed import (
    count_active_cbse_syllabus,
    seed_all_cbse_syllabus,
    seed_syllabus_for_scope,
)


async def _profile_for(
    session: AsyncSession,
    email: str,
    *,
    grade: int,
    stream_code: str | None,
):
    tokens = await AuthService(session).register(
        RegisterRequest(email=email, password="Secret123!", full_name="CBSE Student"),
    )
    user = await AuthService(session).get_user(tokens.user.id)
    profile_service = ProfileService(session)
    await profile_service.ensure_lookups()
    boards = await profile_service.list_boards()
    cbse = next(board for board in boards if board.code == "CBSE")
    classes = await profile_service.list_classes()
    streams = await profile_service.list_streams()
    school_class = next(item for item in classes if item.grade == grade)
    stream = next((item for item in streams if item.code == stream_code), None)
    profile = await profile_service.get_or_create_profile(user)
    profile.photo_url = "/media/profiles/demo.jpg"
    await profile_service.profiles.update(profile)
    await profile_service.update_profile(
        user,
        ProfileUpdateRequest(
            mobile="9876543210",
            board_id=cbse.id,
            class_id=school_class.id,
            stream_id=stream.id if stream else None,
        ),
    )
    return user


def test_catalog_is_valid() -> None:
    errors = validate_catalog()
    assert errors == []
    assert CURRICULUM_VERSION == "CBSE 2026-27"


@pytest.mark.asyncio
async def test_classes_board_and_stream_rules(db_session: AsyncSession) -> None:
    await seed_academic_lookups(db_session)
    boards = (await db_session.execute(select(Board))).scalars().all()
    classes = (await db_session.execute(select(SchoolClass))).scalars().all()
    streams = (await db_session.execute(select(Stream))).scalars().all()

    assert any(board.code == "CBSE" for board in boards)
    assert {item.grade for item in classes} == set(range(6, 13))
    assert {item.code for item in streams} == set(STREAM_CODES)

    for item in classes:
        if item.grade <= 10:
            assert item.requires_stream is False
        else:
            assert item.requires_stream is True


@pytest.mark.asyncio
async def test_class_6_to_10_have_no_stream_subjects(db_session: AsyncSession) -> None:
    required = {"MATH", "SCI", "ENG", "SST"}
    for grade in range(6, 11):
        user = await _profile_for(
            db_session,
            f"cbse{grade}@example.com",
            grade=grade,
            stream_code=None,
        )
        subjects = await SyllabusService(db_session).list_subjects(user)
        codes = {subject.code for subject in subjects}
        assert required <= codes
        assert all(subject.chapter_count >= 1 for subject in subjects)
        for subject in subjects:
            detail = await SyllabusService(db_session).get_subject_chapters(user, subject.id)
            assert detail.chapters
            assert detail.chapters == sorted(detail.chapters, key=lambda item: item.sort_order)
            chapter = await SyllabusService(db_session).get_chapter_topics(
                user,
                detail.chapters[0].id,
            )
            assert chapter.topics
            assert [topic.sort_order for topic in chapter.topics] == list(
                range(len(chapter.topics)),
            )


@pytest.mark.asyncio
async def test_stream_subject_sets(db_session: AsyncSession) -> None:
    expected = {
        "SCIENCE_PCM": {"PHY", "CHEM", "MATH", "ENG"},
        "SCIENCE_PCB": {"PHY", "CHEM", "BIO", "ENG"},
        "SCIENCE_PCMB": {"PHY", "CHEM", "MATH", "BIO", "ENG"},
        "COMMERCE": {"ACC", "BST", "ECO", "ENG"},
        "ARTS": {"HIST", "POL", "GEO", "ENG"},
    }
    for grade in (11, 12):
        for stream_code, codes in expected.items():
            user = await _profile_for(
                db_session,
                f"{stream_code.lower()}_{grade}@example.com",
                grade=grade,
                stream_code=stream_code,
            )
            subjects = await SyllabusService(db_session).list_subjects(user)
            assert {subject.code for subject in subjects} == codes
            physics = next((subject for subject in subjects if subject.code == "PHY"), None)
            if physics is not None:
                detail = await SyllabusService(db_session).get_subject_chapters(user, physics.id)
                assert detail.chapter_count >= 9
                chapter = await SyllabusService(db_session).get_chapter_topics(
                    user,
                    detail.chapters[0].id,
                )
                assert chapter.topics[0].is_locked is False
                assert chapter.topics[1].is_locked is True


@pytest.mark.asyncio
async def test_class_12_pcm_physics_topic_flow(db_session: AsyncSession) -> None:
    user = await _profile_for(
        db_session,
        "c12pcm@example.com",
        grade=12,
        stream_code="SCIENCE_PCM",
    )
    subjects = await SyllabusService(db_session).list_subjects(user)
    physics = next(subject for subject in subjects if subject.code == "PHY")
    detail = await SyllabusService(db_session).get_subject_chapters(user, physics.id)
    assert detail.chapters[0].title == "Electric Charges and Fields"
    chapter = await SyllabusService(db_session).get_chapter_topics(user, detail.chapters[0].id)
    assert len(chapter.topics) > 3
    assert chapter.topics[0].title == "Electric charge"
    assert any(t.title == "Coulomb's law" for t in chapter.topics)
    assert any(t.title == "Electric field lines" for t in chapter.topics)
    assert chapter.topics[0].is_locked is False
    assert chapter.topics[0].is_current is True
    assert chapter.topics[1].is_locked is True


@pytest.mark.asyncio
async def test_class_12_pcm_english_core_structure(db_session: AsyncSession) -> None:
    user = await _profile_for(
        db_session,
        "c12eng@example.com",
        grade=12,
        stream_code="SCIENCE_PCM",
    )
    subjects = await SyllabusService(db_session).list_subjects(user)
    english = next(subject for subject in subjects if subject.code == "ENG")
    detail = await SyllabusService(db_session).get_subject_chapters(user, english.id)
    assert english.topic_count == 31
    assert english.chapter_count == 6
    titles = [chapter.title for chapter in detail.chapters]
    assert titles == [
        "Flamingo – Prose",
        "Flamingo – Poetry",
        "Vistas – Supplementary Reader",
        "Writing Skills",
        "Reading Skills",
        "Grammar / Language",
    ]
    prose = await SyllabusService(db_session).get_chapter_topics(user, detail.chapters[0].id)
    poetry = await SyllabusService(db_session).get_chapter_topics(user, detail.chapters[1].id)
    vistas = await SyllabusService(db_session).get_chapter_topics(user, detail.chapters[2].id)
    writing = await SyllabusService(db_session).get_chapter_topics(user, detail.chapters[3].id)
    reading = await SyllabusService(db_session).get_chapter_topics(user, detail.chapters[4].id)
    grammar = await SyllabusService(db_session).get_chapter_topics(user, detail.chapters[5].id)
    assert len(prose.topics) == 8
    assert len(poetry.topics) == 5
    assert len(vistas.topics) == 6
    assert len(writing.topics) == 5
    assert len(reading.topics) == 3
    assert len(grammar.topics) == 4
    assert any(t.title == "Poets and Pancakes" for t in prose.topics)
    assert any(t.title == "A Roadside Stand" for t in poetry.topics)
    assert any(t.title == "Memories of Childhood" for t in vistas.topics)
    assert writing.topics[0].title == "Notice Writing"
    assert reading.topics[0].title == "Unseen Passage – Comprehension"
    assert grammar.topics[0].title == "Integrated Grammar Usage"


@pytest.mark.asyncio
async def test_class_11_pcm_chem_math_english_are_not_thin(db_session: AsyncSession) -> None:
    user = await _profile_for(
        db_session,
        "c11depth@example.com",
        grade=11,
        stream_code="SCIENCE_PCM",
    )
    subjects = await SyllabusService(db_session).list_subjects(user)
    chem = next(s for s in subjects if s.code == "CHEM")
    math = next(s for s in subjects if s.code == "MATH")
    eng = next(s for s in subjects if s.code == "ENG")
    assert chem.chapter_count == 9
    assert chem.topic_count > 40
    assert math.chapter_count == 14
    assert math.topic_count > 50
    assert eng.chapter_count == 6
    titles = [
        c.title
        for c in (await SyllabusService(db_session).get_subject_chapters(user, eng.id)).chapters
    ]
    assert titles[0].startswith("Hornbill")
    assert any(t.startswith("Snapshots") for t in titles)


@pytest.mark.asyncio
async def test_class_12_biology_has_ncert_depth(db_session: AsyncSession) -> None:
    user = await _profile_for(
        db_session,
        "c12bio@example.com",
        grade=12,
        stream_code="SCIENCE_PCB",
    )
    subjects = await SyllabusService(db_session).list_subjects(user)
    bio = next(s for s in subjects if s.code == "BIO")
    assert bio.chapter_count == 13
    assert bio.topic_count > 50
    detail = await SyllabusService(db_session).get_subject_chapters(user, bio.id)
    flower = await SyllabusService(db_session).get_chapter_topics(user, detail.chapters[0].id)
    assert any(t.title == "Double fertilisation" for t in flower.topics)


@pytest.mark.asyncio
async def test_duplicate_safe_seed(db_session: AsyncSession) -> None:
    first = await seed_all_cbse_syllabus(db_session)
    second = await seed_all_cbse_syllabus(db_session)
    assert first == second
    assert first["classes"] == 7
    assert first["streams"] == 5
    assert first["subjects"] > 40
    assert first["chapters"] > 200
    assert first["topics"] > 600

    total_subjects = await db_session.scalar(select(func.count()).select_from(Subject))
    await seed_all_cbse_syllabus(db_session)
    total_after = await db_session.scalar(select(func.count()).select_from(Subject))
    assert total_subjects == total_after
    assert await count_active_cbse_syllabus(db_session) == first


@pytest.mark.asyncio
async def test_seed_deactivates_placeholders_without_deleting_progress(
    db_session: AsyncSession,
) -> None:
    await seed_academic_lookups(db_session)
    board = (await db_session.execute(select(Board).where(Board.code == "CBSE"))).scalar_one()
    school_class = (
        await db_session.execute(select(SchoolClass).where(SchoolClass.grade == 10))
    ).scalar_one()
    placeholder = Subject(
        name="Mathematics",
        code="MATH",
        board_id=board.id,
        class_id=school_class.id,
        stream_scope="NONE",
        sort_order=0,
        curriculum_version="placeholder",
        is_active=True,
    )
    db_session.add(placeholder)
    await db_session.flush()
    chapter = Chapter(
        subject_id=placeholder.id,
        title="Number Systems",
        sort_order=0,
        curriculum_version="placeholder",
        is_active=True,
    )
    db_session.add(chapter)
    await db_session.flush()
    topic = Topic(
        chapter_id=chapter.id,
        title="Natural numbers",
        sort_order=0,
        curriculum_version="placeholder",
        is_active=True,
    )
    db_session.add(topic)
    await db_session.flush()

    user = await _profile_for(
        db_session,
        "keepprogress@example.com",
        grade=10,
        stream_code=None,
    )
    topic_id = topic.id
    chapter_id = chapter.id
    placeholder_id = placeholder.id
    db_session.add(
        StudentTopicProgress(
            user_id=user.id,
            topic_id=topic_id,
            is_completed=True,
            completed_at=datetime.now(timezone.utc),
        ),
    )
    await db_session.flush()

    subjects = await seed_syllabus_for_scope(
        db_session,
        board_id=board.id,
        class_id=school_class.id,
        stream_id=None,
        stream_code=None,
        grade=10,
    )
    topic = await db_session.get(Topic, topic_id)
    chapter = await db_session.get(Chapter, chapter_id)
    progress = (
        await db_session.execute(
            select(StudentTopicProgress).where(StudentTopicProgress.topic_id == topic_id),
        )
    ).scalar_one()
    assert topic is not None
    assert chapter is not None
    assert topic.is_active is False
    assert chapter.is_active is False
    assert progress.is_completed is True
    math = next(subject for subject in subjects if subject.code == "MATH")
    assert math.id == placeholder_id
    official_titles = {item["title"] for item in subjects_for_scope(10, None)[0]["chapters"]}
    active_titles = {item.title for item in math.chapters if item.is_active}
    assert "Real Numbers" in active_titles
    assert "Number Systems" not in active_titles
    assert official_titles <= active_titles
