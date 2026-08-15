"""Authentication request/response schemas."""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    full_name: str = Field(min_length=2, max_length=120)


class LoginRequest(BaseModel):
    email: Optional[EmailStr] = None
    user_id: Optional[UUID] = None
    password: str = Field(min_length=1, max_length=128)

    @model_validator(mode="after")
    def require_identity(self) -> "LoginRequest":
        if self.user_id is None and not self.email:
            raise ValueError("Email or saved account is required")
        return self


class RefreshRequest(BaseModel):
    refresh_token: Optional[str] = None


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: EmailStr
    full_name: str
    is_active: bool
    created_at: datetime


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: UserResponse


class MessageResponse(BaseModel):
    message: str
    code: str = "ok"
