"""JWT authentication dependencies."""

from typing import Annotated, Optional
from uuid import UUID

from fastapi import Depends, Header
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import UnauthorizedError
from app.core.security import decode_token
from app.dependencies.db import get_db
from app.models.user import User
from app.services.auth import AuthService

bearer_scheme = HTTPBearer(auto_error=False)


def _extract_bearer_token(
    credentials: Optional[HTTPAuthorizationCredentials],
    authorization: Optional[str],
) -> str:
    if credentials is not None and credentials.scheme.lower() == "bearer":
        return credentials.credentials
    if authorization and authorization.lower().startswith("bearer "):
        return authorization.split(" ", 1)[1].strip()
    raise UnauthorizedError("Missing or invalid Authorization header")


async def get_current_user_id(
    credentials: Annotated[
        Optional[HTTPAuthorizationCredentials],
        Depends(bearer_scheme),
    ] = None,
    authorization: Annotated[Optional[str], Header()] = None,
) -> UUID:
    token = _extract_bearer_token(credentials, authorization)
    try:
        claims = decode_token(token)
    except ValueError as exc:
        raise UnauthorizedError("Invalid or expired access token") from exc

    if claims.get("type") != "access":
        raise UnauthorizedError("Invalid access token type")

    subject = claims.get("sub")
    if not subject:
        raise UnauthorizedError("Invalid access token subject")

    try:
        return UUID(str(subject))
    except ValueError as exc:
        raise UnauthorizedError("Invalid access token subject") from exc


async def get_current_user_id_optional(
    credentials: Annotated[
        Optional[HTTPAuthorizationCredentials],
        Depends(bearer_scheme),
    ] = None,
    authorization: Annotated[Optional[str], Header()] = None,
) -> Optional[UUID]:
    try:
        return await get_current_user_id(credentials, authorization)
    except UnauthorizedError:
        return None


async def get_current_user(
    user_id: Annotated[UUID, Depends(get_current_user_id)],
    session: Annotated[AsyncSession, Depends(get_db)],
) -> User:
    return await AuthService(session).get_user(user_id)


CurrentUserId = Depends(get_current_user_id)
CurrentUser = Depends(get_current_user)
