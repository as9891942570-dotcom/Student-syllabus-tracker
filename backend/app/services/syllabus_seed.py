"""Seed syllabus subjects/chapters/topics for a board+class(+stream) scope."""

from __future__ import annotations

from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.chapter import Chapter
from app.models.subject import Subject
from app.models.topic import Topic

# Tracking-only outlines (no teaching content).
SUBJECTS_6_TO_10: list[tuple[str, str, list[tuple[str, list[str]]]]] = [
    (
        "MATH",
        "Mathematics",
        [
            ("Number Systems", ["Natural numbers", "Integers", "Fractions"]),
            ("Algebra Basics", ["Expressions", "Linear equations", "Practice set"]),
        ],
    ),
    (
        "SCI",
        "Science",
        [
            ("Matter & Materials", ["States of matter", "Properties", "Changes"]),
            ("Living World", ["Cells", "Organisms", "Environment"]),
        ],
    ),
    (
        "ENG",
        "English",
        [
            ("Reading Skills", ["Comprehension", "Vocabulary", "Summary"]),
            ("Writing Skills", ["Paragraphs", "Letters", "Grammar review"]),
        ],
    ),
    (
        "SST",
        "Social Science",
        [
            ("History Themes", ["Timeline", "Key events", "Revision checklist"]),
            ("Geography Basics", ["Maps", "Resources", "Climate"]),
        ],
    ),
]

STREAM_SUBJECTS: dict[str, list[tuple[str, str, list[tuple[str, list[str]]]]]] = {
    "SCIENCE_PCM": [
        ("PHY", "Physics", [("Mechanics", ["Motion", "Forces", "Energy"]), ("Waves", ["Sound", "Light", "Practice"])]),
        ("CHEM", "Chemistry", [("Atomic Structure", ["Atoms", "Periodic table", "Bonding"]), ("Reactions", ["Types", "Equations", "Practice"])]),
        ("MATH", "Mathematics", [("Algebra", ["Polynomials", "Progressions", "Practice"]), ("Calculus Intro", ["Limits", "Derivatives", "Applications"])]),
        ("ENG", "English", [("Core Skills", ["Reading", "Writing", "Grammar"])]),
    ],
    "SCIENCE_PCB": [
        ("PHY", "Physics", [("Mechanics", ["Motion", "Forces", "Energy"]), ("Optics", ["Reflection", "Refraction", "Practice"])]),
        ("CHEM", "Chemistry", [("Atomic Structure", ["Atoms", "Periodic table", "Bonding"]), ("Organic Intro", ["Hydrocarbons", "Functional groups", "Practice"])]),
        ("BIO", "Biology", [("Cell Biology", ["Cell structure", "Division", "Practice"]), ("Human Physiology", ["Systems overview", "Health", "Practice"])]),
        ("ENG", "English", [("Core Skills", ["Reading", "Writing", "Grammar"])]),
    ],
    "SCIENCE_PCMB": [
        ("PHY", "Physics", [("Mechanics", ["Motion", "Forces", "Energy"])]),
        ("CHEM", "Chemistry", [("Atomic Structure", ["Atoms", "Periodic table", "Bonding"])]),
        ("BIO", "Biology", [("Cell Biology", ["Cell structure", "Division", "Practice"])]),
        ("MATH", "Mathematics", [("Algebra", ["Polynomials", "Progressions", "Practice"])]),
        ("ENG", "English", [("Core Skills", ["Reading", "Writing", "Grammar"])]),
    ],
    "COMMERCE": [
        ("ACC", "Accountancy", [("Basics", ["Journal", "Ledger", "Trial balance"])]),
        ("BST", "Business Studies", [("Business Env", ["Forms of business", "Trade", "Practice"])]),
        ("ECO", "Economics", [("Micro Intro", ["Demand", "Supply", "Market"])]),
        ("ENG", "English", [("Core Skills", ["Reading", "Writing", "Grammar"])]),
    ],
    "ARTS": [
        ("HIST", "History", [("Themes", ["Ancient", "Medieval", "Modern overview"])]),
        ("POL", "Political Science", [("Civics", ["Constitution", "Rights", "Governance"])]),
        ("GEO", "Geography", [("Human Geo", ["Population", "Resources", "Maps"])]),
        ("ENG", "English", [("Core Skills", ["Reading", "Writing", "Grammar"])]),
    ],
}


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
    existing = await session.execute(
        select(Subject)
        .where(
            Subject.board_id == board_id,
            Subject.class_id == class_id,
            Subject.stream_scope == stream_scope,
        )
        .options(
            selectinload(Subject.chapters).selectinload(Chapter.topics),
        )
        .order_by(Subject.sort_order),
    )
    subjects = list(existing.scalars().all())
    if subjects:
        return subjects

    if grade >= 11:
        if not stream_code or stream_code not in STREAM_SUBJECTS:
            return []
        blueprint = STREAM_SUBJECTS[stream_code]
    else:
        blueprint = SUBJECTS_6_TO_10

    created: list[Subject] = []
    for subject_order, (code, name, chapters) in enumerate(blueprint):
        subject = Subject(
            name=name,
            code=code,
            board_id=board_id,
            class_id=class_id,
            stream_id=stream_id if grade >= 11 else None,
            stream_scope=stream_scope,
            sort_order=subject_order,
        )
        session.add(subject)
        await session.flush()
        for chapter_order, (chapter_title, topic_titles) in enumerate(chapters):
            chapter = Chapter(
                subject_id=subject.id,
                title=chapter_title,
                sort_order=chapter_order,
            )
            session.add(chapter)
            await session.flush()
            for topic_order, topic_title in enumerate(topic_titles):
                session.add(
                    Topic(
                        chapter_id=chapter.id,
                        title=topic_title,
                        sort_order=topic_order,
                    ),
                )
        created.append(subject)

    await session.flush()
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
    return list(result.scalars().all())
