"""Syllabus tracking schemas."""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class TopicProgressUpdate(BaseModel):
    is_completed: bool


class TopicResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    sort_order: int
    is_completed: bool = False
    completed_at: Optional[datetime] = None


class ChapterResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    sort_order: int
    topic_count: int
    completed_topic_count: int
    completion_percentage: int
    topics: list[TopicResponse] = Field(default_factory=list)


class SubjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    code: str
    sort_order: int
    chapter_count: int
    topic_count: int
    completed_topic_count: int
    completion_percentage: int


class SubjectDetailResponse(SubjectResponse):
    chapters: list[ChapterResponse] = Field(default_factory=list)


class SyllabusStructureResponse(BaseModel):
    subjects: list[SubjectDetailResponse]
    overall_completion_percentage: int
    total_topics: int
    completed_topics: int


class SyllabusCompletionResponse(BaseModel):
    overall_completion_percentage: int
    total_subjects: int
    total_chapters: int
    total_topics: int
    completed_topics: int
    subjects: list[SubjectResponse]
