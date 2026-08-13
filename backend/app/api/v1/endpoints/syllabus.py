"""Syllabus tracking API routes."""

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db
from app.models.user import User
from app.schemas.syllabus import (
    ChapterResponse,
    SubjectDetailResponse,
    SubjectResponse,
    SyllabusCompletionResponse,
    SyllabusStructureResponse,
    TopicProgressUpdate,
    TopicResponse,
)
from app.services.syllabus import SyllabusService

router = APIRouter(prefix="/syllabus", tags=["syllabus"])


@router.get("/subjects", response_model=list[SubjectResponse])
async def list_my_subjects(
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> list[SubjectResponse]:
    return await SyllabusService(session).list_subjects(current_user)


@router.get("/subjects/{subject_id}", response_model=SubjectDetailResponse)
async def get_subject_with_chapters(
    subject_id: UUID,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> SubjectDetailResponse:
    return await SyllabusService(session).get_subject_chapters(current_user, subject_id)


@router.get("/chapters/{chapter_id}/topics", response_model=ChapterResponse)
async def get_chapter_topics(
    chapter_id: UUID,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> ChapterResponse:
    return await SyllabusService(session).get_chapter_topics(current_user, chapter_id)


@router.get("/structure", response_model=SyllabusStructureResponse)
async def get_syllabus_structure(
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> SyllabusStructureResponse:
    return await SyllabusService(session).get_structure(current_user)


@router.get("/completion", response_model=SyllabusCompletionResponse)
async def get_syllabus_completion(
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> SyllabusCompletionResponse:
    return await SyllabusService(session).get_completion(current_user)


@router.patch("/topics/{topic_id}/progress", response_model=TopicResponse)
async def update_topic_progress(
    topic_id: UUID,
    payload: TopicProgressUpdate,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> TopicResponse:
    return await SyllabusService(session).set_topic_progress(
        current_user,
        topic_id,
        payload,
    )
