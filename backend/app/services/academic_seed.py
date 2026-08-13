"""Seed academic lookup data (boards, classes, streams)."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.board import Board
from app.models.school_class import SchoolClass
from app.models.stream import Stream

BOARDS = [
    ("CBSE", "CBSE"),
    ("ICSE", "ICSE"),
    ("STATE", "State Board"),
]

STREAMS = [
    ("SCIENCE_PCM", "Science (PCM)"),
    ("SCIENCE_PCB", "Science (PCB)"),
    ("SCIENCE_PCMB", "Science (PCMB)"),
    ("COMMERCE", "Commerce"),
    ("ARTS", "Arts/Humanities"),
]


async def seed_academic_lookups(session: AsyncSession) -> None:
    existing_boards = (await session.execute(select(Board.id).limit(1))).first()
    if existing_boards is None:
        for code, name in BOARDS:
            session.add(Board(code=code, name=name))

    existing_classes = (await session.execute(select(SchoolClass.id).limit(1))).first()
    if existing_classes is None:
        for grade in range(6, 13):
            session.add(SchoolClass(grade=grade, name=f"Class {grade}"))

    existing_streams = (await session.execute(select(Stream.id).limit(1))).first()
    if existing_streams is None:
        for code, name in STREAMS:
            session.add(Stream(code=code, name=name))

    await session.flush()
