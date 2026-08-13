"""Student profile and academic lookup APIs."""

from typing import Annotated

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db
from app.models.user import User
from app.schemas.profile import (
    BoardResponse,
    ClassResponse,
    ProfileResponse,
    ProfileUpdateRequest,
    StreamResponse,
)
from app.services.profile import ProfileService

router = APIRouter(tags=["profile"])


@router.get("/boards", response_model=list[BoardResponse])
async def list_boards(
    session: Annotated[AsyncSession, Depends(get_db)],
    _: Annotated[User, Depends(get_current_user)],
) -> list[BoardResponse]:
    return await ProfileService(session).list_boards()


@router.get("/classes", response_model=list[ClassResponse])
async def list_classes(
    session: Annotated[AsyncSession, Depends(get_db)],
    _: Annotated[User, Depends(get_current_user)],
) -> list[ClassResponse]:
    return await ProfileService(session).list_classes()


@router.get("/streams", response_model=list[StreamResponse])
async def list_streams(
    session: Annotated[AsyncSession, Depends(get_db)],
    _: Annotated[User, Depends(get_current_user)],
) -> list[StreamResponse]:
    return await ProfileService(session).list_streams()


@router.get("/profile/me", response_model=ProfileResponse)
async def get_my_profile(
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> ProfileResponse:
    return await ProfileService(session).get_profile(current_user)


@router.put("/profile/me", response_model=ProfileResponse)
async def update_my_profile(
    payload: ProfileUpdateRequest,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> ProfileResponse:
    return await ProfileService(session).update_profile(current_user, payload)


@router.post("/profile/me/photo", response_model=ProfileResponse)
async def upload_my_photo(
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
    file: Annotated[UploadFile, File(...)],
) -> ProfileResponse:
    return await ProfileService(session).upload_photo(current_user, file)
