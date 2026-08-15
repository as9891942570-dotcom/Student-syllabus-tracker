"""Student progression API routes."""

from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db
from app.models.user import User
from app.schemas.progression import ProgressionResponse
from app.services.progression import ProgressionService

router = APIRouter(prefix="/progression", tags=["progression"])


@router.get("/me", response_model=ProgressionResponse)
async def get_my_progression(
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> ProgressionResponse:
    return await ProgressionService(session).get_me(current_user)
