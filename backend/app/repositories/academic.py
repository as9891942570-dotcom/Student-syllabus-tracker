"""Academic lookup repositories."""

from typing import Optional, Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.board import Board
from app.models.school_class import SchoolClass
from app.models.stream import Stream
from app.repositories.base import BaseRepository


class BoardRepository(BaseRepository[Board]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Board, session)

    async def list_all(self) -> Sequence[Board]:
        result = await self.session.execute(select(Board).order_by(Board.name))
        return result.scalars().all()

    async def get_by_code(self, code: str) -> Optional[Board]:
        result = await self.session.execute(select(Board).where(Board.code == code))
        return result.scalar_one_or_none()


class ClassRepository(BaseRepository[SchoolClass]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(SchoolClass, session)

    async def list_all(self) -> Sequence[SchoolClass]:
        result = await self.session.execute(
            select(SchoolClass).order_by(SchoolClass.grade),
        )
        return result.scalars().all()

    async def get_by_grade(self, grade: int) -> Optional[SchoolClass]:
        result = await self.session.execute(
            select(SchoolClass).where(SchoolClass.grade == grade),
        )
        return result.scalar_one_or_none()


class StreamRepository(BaseRepository[Stream]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Stream, session)

    async def list_all(self) -> Sequence[Stream]:
        result = await self.session.execute(select(Stream).order_by(Stream.name))
        return result.scalars().all()

    async def get_by_code(self, code: str) -> Optional[Stream]:
        result = await self.session.execute(select(Stream).where(Stream.code == code))
        return result.scalar_one_or_none()
