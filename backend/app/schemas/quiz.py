"""Quiz Pydantic schemas. Correct answers are never included in question payloads."""

from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, computed_field


class QuizOptionPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    text: str
    sort_order: int


class QuizSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    topic_id: UUID
    title: str
    time_limit_seconds: int
    question_count: int
    is_active: bool


class QuizDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    topic_id: UUID
    topic_title: str
    chapter_id: UUID
    chapter_title: str
    subject_id: UUID
    subject_name: str
    title: str
    time_limit_seconds: int
    question_count: int
    is_active: bool


class QuizQuestionPublic(BaseModel):
    id: UUID
    prompt: str
    sort_order: int
    question_number: int
    total_questions: int
    options: list[QuizOptionPublic]
    already_answered: bool = False
    selected_option_id: Optional[UUID] = None
    correct_option_id: Optional[UUID] = None


class SubmitAnswerRequest(BaseModel):
    option_id: UUID


class SubmitAnswerResponse(BaseModel):
    question_id: UUID
    selected_option_id: UUID
    is_correct: bool
    correct_option_id: UUID
    attempt_id: UUID
    answered_count: int
    correct_count: int
    incorrect_count: int


class QuizAttemptResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    quiz_id: UUID
    quiz_title: str
    topic_id: UUID
    topic_title: str
    chapter_id: UUID
    chapter_title: str
    subject_id: UUID
    subject_name: str
    status: str
    current_question_index: int
    total_questions: int
    answered_count: int
    correct_count: int
    incorrect_count: int
    # Stored 0–100 percentage for compatibility. Display 8/10 via correct_count.
    score: int
    percentage: int
    passed: bool = False
    xp_earned: int
    total_xp: int
    coins_earned: int = 0
    total_coins: int = 0
    topic_completed: bool
    next_topic_unlocked: bool = False
    next_topic_id: Optional[UUID] = None
    next_topic_title: Optional[str] = None
    xp_awarded: bool = True
    coins_awarded: bool = False
    level: int = 1
    level_floor_xp: int = 0
    next_level_xp: int = 100
    level_progress_percentage: int = 0
    started_at: datetime
    expires_at: datetime
    ended_at: Optional[datetime]
    seconds_remaining: int

    @computed_field
    @property
    def correct_answers(self) -> int:
        return self.correct_count

    @computed_field
    @property
    def wrong_answers(self) -> int:
        return self.incorrect_count


class QuizHistoryItem(BaseModel):
    id: UUID
    quiz_id: UUID
    quiz_title: str
    topic_id: UUID
    topic_title: str
    status: str
    score: int
    percentage: int
    passed: bool = False
    xp_earned: int
    total_questions: int
    correct_count: int
    incorrect_count: int = 0
    started_at: datetime
    ended_at: Optional[datetime]
    completed: bool
