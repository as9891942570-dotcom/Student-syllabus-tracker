"""Study session schemas."""

from datetime import datetime
from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class StartSessionRequest(BaseModel):
    topic_id: UUID


class SessionActivityRequest(BaseModel):
    result: Literal["correct", "incorrect"]


class CompleteSessionRequest(BaseModel):
    correct_count: Optional[int] = Field(default=None, ge=0)
    incorrect_count: Optional[int] = Field(default=None, ge=0)


class StudySessionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    status: str
    subject_id: UUID
    subject_name: str
    chapter_id: UUID
    chapter_title: str
    topic_id: UUID
    topic_title: str
    started_at: datetime
    ended_at: Optional[datetime]
    duration_seconds: int
    score: int
    correct_count: int
    incorrect_count: int
    xp_earned: int
    total_xp: int


class SessionResultResponse(StudySessionResponse):
    pass
