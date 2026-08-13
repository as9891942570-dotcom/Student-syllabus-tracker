"""Application exception hierarchy and FastAPI handlers."""

from typing import Any, Optional

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class AppException(Exception):
    """Base application error."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "app_error",
        status_code: int = 400,
        details: Optional[Any] = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.status_code = status_code
        self.details = details


class NotFoundError(AppException):
    def __init__(self, message: str = "Resource not found", **kwargs: Any) -> None:
        super().__init__(message, code="not_found", status_code=404, **kwargs)


class UnauthorizedError(AppException):
    def __init__(self, message: str = "Unauthorized", **kwargs: Any) -> None:
        super().__init__(message, code="unauthorized", status_code=401, **kwargs)


class ForbiddenError(AppException):
    def __init__(self, message: str = "Forbidden", **kwargs: Any) -> None:
        super().__init__(message, code="forbidden", status_code=403, **kwargs)


class ConflictError(AppException):
    def __init__(self, message: str = "Conflict", **kwargs: Any) -> None:
        super().__init__(message, code="conflict", status_code=409, **kwargs)


class ValidationAppError(AppException):
    def __init__(self, message: str = "Validation error", **kwargs: Any) -> None:
        super().__init__(message, code="validation_error", status_code=422, **kwargs)


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppException)
    async def app_exception_handler(_: Request, exc: AppException) -> JSONResponse:
        body: dict[str, Any] = {
            "detail": exc.message,
            "code": exc.code,
        }
        if exc.details is not None:
            body["details"] = exc.details
        return JSONResponse(status_code=exc.status_code, content=body)

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(_: Request, exc: Exception) -> JSONResponse:
        # HTTPException / validation errors use more-specific handlers via MRO.
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error", "code": "internal_error"},
        )
