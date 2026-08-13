"""Profile and academic lookup schemas."""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class BoardResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    code: str
    name: str


class ClassResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    grade: int
    name: str
    requires_stream: bool


class StreamResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    code: str
    name: str


class ProfileUpdateRequest(BaseModel):
    full_name: Optional[str] = Field(default=None, min_length=2, max_length=120)
    mobile: Optional[str] = Field(default=None, min_length=10, max_length=15)
    board_id: Optional[UUID] = None
    class_id: Optional[UUID] = None
    stream_id: Optional[UUID] = None
    clear_stream: bool = False

    @field_validator("mobile")
    @classmethod
    def validate_mobile(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value
        digits = "".join(ch for ch in value if ch.isdigit())
        if len(digits) < 10 or len(digits) > 15:
            raise ValueError("Mobile number must contain 10–15 digits")
        return digits


class ProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    email: EmailStr
    full_name: str
    mobile: Optional[str]
    photo_url: Optional[str]
    board: Optional[BoardResponse]
    school_class: Optional[ClassResponse]
    stream: Optional[StreamResponse]
    total_xp: int = 0
    completion_percentage: int
    is_complete: bool
    missing_fields: list[str]
    created_at: datetime
    updated_at: datetime
