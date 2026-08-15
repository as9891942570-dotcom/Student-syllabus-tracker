"""Student progression schemas (XP, level, topic unlock summary)."""

from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class LevelProgressResponse(BaseModel):
    level: int
    total_xp: int
    level_floor_xp: int
    next_level_xp: int
    xp_into_level: int
    xp_needed_for_next: int
    level_progress_percentage: int


class ProgressionTopicSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    chapter_id: UUID
    chapter_title: str
    subject_id: UUID
    subject_name: str
    sort_order: int
    is_completed: bool
    is_locked: bool
    is_current: bool


class ProgressionResponse(BaseModel):
    total_xp: int
    total_coins: int = 0
    level: int
    level_floor_xp: int
    next_level_xp: int
    xp_into_level: int
    xp_needed_for_next: int
    level_progress_percentage: int
    overall_completion_percentage: int
    completed_topic_count: int
    total_topic_count: int
    current_topic: Optional[ProgressionTopicSummary] = None
    next_topic: Optional[ProgressionTopicSummary] = None
    completed_topics: list[ProgressionTopicSummary]
