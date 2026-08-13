"""Study session API routes."""

from typing import Annotated, Optional
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db
from app.models.user import User
from app.schemas.study_session import (
    CompleteSessionRequest,
    SessionActivityRequest,
    StartSessionRequest,
    StudySessionResponse,
)
from app.services.study_session import StudySessionService

router = APIRouter(prefix="/study-sessions", tags=["study-sessions"])


@router.post("/start", response_model=StudySessionResponse, status_code=201)
async def start_session(
    payload: StartSessionRequest,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> StudySessionResponse:
    return await StudySessionService(session).start(current_user, payload)


@router.get("/active", response_model=Optional[StudySessionResponse])
async def get_active_session(
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> Optional[StudySessionResponse]:
    return await StudySessionService(session).get_active(current_user)


@router.get("/{session_id}", response_model=StudySessionResponse)
async def get_session(
    session_id: UUID,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> StudySessionResponse:
    return await StudySessionService(session).get_session(current_user, session_id)


@router.post("/{session_id}/activity", response_model=StudySessionResponse)
async def record_activity(
    session_id: UUID,
    payload: SessionActivityRequest,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> StudySessionResponse:
    return await StudySessionService(session).record_activity(
        current_user,
        session_id,
        payload,
    )


@router.post("/{session_id}/complete", response_model=StudySessionResponse)
async def complete_session(
    session_id: UUID,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
    payload: CompleteSessionRequest = CompleteSessionRequest(),
) -> StudySessionResponse:
    return await StudySessionService(session).complete(
        current_user,
        session_id,
        payload,
    )
