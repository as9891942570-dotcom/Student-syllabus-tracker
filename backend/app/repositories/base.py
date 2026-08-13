"""Generic async CRUD repository base."""

from typing import Any, Generic, Optional, Sequence, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import Base

ModelT = TypeVar("ModelT", bound=Base)


class BaseRepository(Generic[ModelT]):
    """Reusable data-access helpers for SQLAlchemy models."""

    def __init__(self, model: Type[ModelT], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def get(self, entity_id: Any) -> Optional[ModelT]:
        return await self.session.get(self.model, entity_id)

    async def list(self, *, skip: int = 0, limit: int = 100) -> Sequence[ModelT]:
        result = await self.session.execute(
            select(self.model).offset(skip).limit(limit),
        )
        return result.scalars().all()

    async def create(self, entity: ModelT) -> ModelT:
        self.session.add(entity)
        await self.session.flush()
        await self.session.refresh(entity)
        return entity

    async def update(self, entity: ModelT) -> ModelT:
        self.session.add(entity)
        await self.session.flush()
        await self.session.refresh(entity)
        return entity

    async def delete(self, entity: ModelT) -> None:
        await self.session.delete(entity)
        await self.session.flush()
