"""Shared API schemas."""

from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, ConfigDict

T = TypeVar("T")


class MessageResponse(BaseModel):
    message: str


class HealthDependencyStatus(BaseModel):
    database: bool
    redis: bool


class HealthResponse(BaseModel):
    status: str
    app: str
    version: str
    dependencies: HealthDependencyStatus


class ApiResponse(BaseModel, Generic[T]):
    model_config = ConfigDict(from_attributes=True)

    data: T
    message: Optional[str] = None
