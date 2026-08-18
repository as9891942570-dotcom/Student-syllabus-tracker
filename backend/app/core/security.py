"""JWT and password hashing helpers."""

from datetime import datetime, timedelta, timezone
from typing import Any, Optional
from uuid import uuid4

import bcrypt
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import get_settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
_BCRYPT_PREFIXES = (b"$2a$", b"$2b$", b"$2y$", b"$2x$")


def _as_bytes(value: str | bytes) -> bytes:
    return value.encode("utf-8") if isinstance(value, str) else value


def _bcrypt_secret(plain_password: str) -> bytes:
    # bcrypt only uses 72 bytes; older hashes may have been created that way.
    return _as_bytes(plain_password)[:72]


def _is_bcrypt_hash(hashed_password: str) -> bool:
    raw = _as_bytes(hashed_password)
    return raw.startswith(_BCRYPT_PREFIXES)


def _verify_native_bcrypt(plain_password: str, hashed_password: str) -> bool:
    try:
        return bcrypt.checkpw(_bcrypt_secret(plain_password), _as_bytes(hashed_password))
    except (TypeError, ValueError):
        return False


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify against current passlib hashes and older native bcrypt hashes."""
    ok, _ = verify_password_result(plain_password, hashed_password)
    return ok


def verify_password_result(plain_password: str, hashed_password: str) -> tuple[bool, bool]:
    """Return (is_valid, should_rehash)."""
    if not plain_password or not hashed_password:
        return False, False
    try:
        if pwd_context.verify(plain_password, hashed_password):
            needs_update = False
            try:
                needs_update = bool(pwd_context.needs_update(hashed_password))
            except Exception:
                needs_update = True
            if hashed_password.startswith(("$2a$", "$2y$", "$2x$")):
                needs_update = True
            return True, needs_update
    except Exception:
        pass
    if _is_bcrypt_hash(hashed_password) and _verify_native_bcrypt(
        plain_password,
        hashed_password,
    ):
        return True, True
    return False, False


def password_needs_rehash(hashed_password: str) -> bool:
    """True when a valid hash should be upgraded to the current hasher."""
    if not hashed_password:
        return False
    try:
        if pwd_context.identify(hashed_password):
            return bool(pwd_context.needs_update(hashed_password))
    except (ValueError, TypeError):
        return _is_bcrypt_hash(hashed_password)
    return _is_bcrypt_hash(hashed_password)


def create_access_token(
    subject: str,
    *,
    expires_delta: Optional[timedelta] = None,
    extra_claims: Optional[dict[str, Any]] = None,
) -> str:
    settings = get_settings()
    expire = datetime.now(timezone.utc) + (
        expires_delta
        if expires_delta is not None
        else timedelta(minutes=settings.access_token_expire_minutes)
    )
    payload: dict[str, Any] = {
        "sub": subject,
        "exp": expire,
        "type": "access",
        "jti": str(uuid4()),
    }
    if extra_claims:
        payload.update(extra_claims)
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def create_refresh_token(
    subject: str,
    *,
    expires_delta: Optional[timedelta] = None,
    extra_claims: Optional[dict[str, Any]] = None,
) -> str:
    settings = get_settings()
    expire = datetime.now(timezone.utc) + (
        expires_delta
        if expires_delta is not None
        else timedelta(days=settings.refresh_token_expire_days)
    )
    payload: dict[str, Any] = {
        "sub": subject,
        "exp": expire,
        "type": "refresh",
        "jti": str(uuid4()),
    }
    if extra_claims:
        payload.update(extra_claims)
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def decode_token(token: str) -> dict[str, Any]:
    settings = get_settings()
    try:
        return jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm],
        )
    except JWTError as exc:
        raise ValueError("Invalid token") from exc
