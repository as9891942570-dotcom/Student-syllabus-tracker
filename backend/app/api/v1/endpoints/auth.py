"""Authentication API routes."""

from typing import Annotated, Optional
from uuid import UUID

from fastapi import APIRouter, Cookie, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user, get_current_user_id_optional
from app.dependencies.db import get_db
from app.models.user import User
from app.schemas.auth import (
    ForgotPasswordRequest,
    LoginRequest,
    MessageResponse,
    RefreshRequest,
    RegisterRequest,
    TokenResponse,
    UserResponse,
)
from app.services.auth import AuthService
from app.utils.cookies import (
    REFRESH_COOKIE_NAME,
    clear_refresh_cookie,
    set_refresh_cookie,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse, status_code=201)
async def register(
    payload: RegisterRequest,
    response: Response,
    session: Annotated[AsyncSession, Depends(get_db)],
) -> TokenResponse:
    result = await AuthService(session).register(payload)
    set_refresh_cookie(response, result.refresh_token)
    return result


@router.post("/login", response_model=TokenResponse)
async def login(
    payload: LoginRequest,
    response: Response,
    session: Annotated[AsyncSession, Depends(get_db)],
) -> TokenResponse:
    result = await AuthService(session).login(payload)
    set_refresh_cookie(response, result.refresh_token)
    return result


@router.post("/refresh", response_model=TokenResponse)
async def refresh(
    response: Response,
    session: Annotated[AsyncSession, Depends(get_db)],
    payload: RefreshRequest = RefreshRequest(),
    refresh_token_cookie: Annotated[
        Optional[str],
        Cookie(alias=REFRESH_COOKIE_NAME),
    ] = None,
) -> TokenResponse:
    token = payload.refresh_token or refresh_token_cookie
    result = await AuthService(session).refresh(token)
    set_refresh_cookie(response, result.refresh_token)
    return result


@router.post("/logout", response_model=MessageResponse)
async def logout(
    response: Response,
    session: Annotated[AsyncSession, Depends(get_db)],
    payload: RefreshRequest = RefreshRequest(),
    refresh_token_cookie: Annotated[
        Optional[str],
        Cookie(alias=REFRESH_COOKIE_NAME),
    ] = None,
    user_id: Annotated[Optional[UUID], Depends(get_current_user_id_optional)] = None,
) -> MessageResponse:
    token = payload.refresh_token or refresh_token_cookie
    await AuthService(session).logout(token, user_id=user_id)
    clear_refresh_cookie(response)
    return MessageResponse(message="Logged out successfully")


@router.post("/forgot-password", response_model=MessageResponse)
async def forgot_password(
    payload: ForgotPasswordRequest,
    session: Annotated[AsyncSession, Depends(get_db)],
) -> MessageResponse:
    message = await AuthService(session).forgot_password(payload)
    return MessageResponse(message=message, code="forgot_password_stub")


@router.get("/me", response_model=UserResponse)
async def me(
    current_user: Annotated[User, Depends(get_current_user)],
) -> UserResponse:
    return UserResponse.model_validate(current_user)
