"""Student profile business logic."""

from __future__ import annotations

from pathlib import Path
from typing import Optional
from uuid import UUID

from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.exceptions import NotFoundError, ValidationAppError
from app.models.school_class import SchoolClass
from app.models.student_profile import StudentProfile
from app.models.user import User
from app.repositories.academic import BoardRepository, ClassRepository, StreamRepository
from app.repositories.profile import StudentProfileRepository
from app.repositories.user import UserRepository
from app.schemas.profile import (
    BoardResponse,
    ClassResponse,
    ProfileResponse,
    ProfileUpdateRequest,
    StreamResponse,
)
from app.services.academic_seed import seed_academic_lookups


class ProfileService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.profiles = StudentProfileRepository(session)
        self.users = UserRepository(session)
        self.boards = BoardRepository(session)
        self.classes = ClassRepository(session)
        self.streams = StreamRepository(session)
        self.settings = get_settings()

    async def ensure_lookups(self) -> None:
        await seed_academic_lookups(self.session)

    async def list_boards(self) -> list[BoardResponse]:
        await self.ensure_lookups()
        return [BoardResponse.model_validate(b) for b in await self.boards.list_all()]

    async def list_classes(self) -> list[ClassResponse]:
        await self.ensure_lookups()
        return [
            ClassResponse(
                id=c.id,
                grade=c.grade,
                name=c.name,
                requires_stream=c.requires_stream,
            )
            for c in await self.classes.list_all()
        ]

    async def list_streams(self) -> list[StreamResponse]:
        await self.ensure_lookups()
        return [StreamResponse.model_validate(s) for s in await self.streams.list_all()]

    async def get_or_create_profile(self, user: User) -> StudentProfile:
        profile = await self.profiles.get_by_user_id(user.id)
        if profile is not None:
            return profile
        await self.profiles.create(StudentProfile(user_id=user.id))
        loaded = await self.profiles.get_by_user_id(user.id)
        assert loaded is not None
        return loaded

    async def get_profile(self, user: User) -> ProfileResponse:
        profile = await self.get_or_create_profile(user)
        return self._to_response(profile)

    async def update_profile(
        self,
        user: User,
        payload: ProfileUpdateRequest,
    ) -> ProfileResponse:
        await self.ensure_lookups()
        profile = await self.get_or_create_profile(user)

        if payload.full_name is not None:
            user.full_name = payload.full_name.strip()
            await self.users.update(user)

        if payload.mobile is not None:
            profile.mobile = payload.mobile

        if payload.board_id is not None:
            board = await self.boards.get(payload.board_id)
            if board is None:
                raise NotFoundError("Board not found")
            profile.board_id = board.id

        effective_class: Optional[SchoolClass] = profile.school_class
        if payload.class_id is not None:
            effective_class = await self.classes.get(payload.class_id)
            if effective_class is None:
                raise NotFoundError("Class not found")
            profile.class_id = effective_class.id

        class_or_stream_touched = (
            payload.class_id is not None
            or payload.stream_id is not None
            or payload.clear_stream
        )
        if class_or_stream_touched:
            if effective_class is None and profile.class_id is not None:
                effective_class = await self.classes.get(profile.class_id)
            if effective_class is None:
                raise ValidationAppError("Select a class before choosing a stream")

            if not effective_class.requires_stream:
                if payload.stream_id is not None:
                    raise ValidationAppError(
                        "Students in Classes 6–10 cannot select a stream",
                    )
                profile.stream_id = None
            else:
                if payload.clear_stream:
                    raise ValidationAppError(
                        "Students in Classes 11–12 must select a stream before saving",
                    )
                if payload.stream_id is not None:
                    stream = await self.streams.get(payload.stream_id)
                    if stream is None:
                        raise NotFoundError("Stream not found")
                    profile.stream_id = stream.id
                elif profile.stream_id is None:
                    raise ValidationAppError(
                        "Students in Classes 11–12 must select a stream before saving",
                    )

        await self.profiles.update(profile)
        refreshed = await self.profiles.get_by_user_id(user.id)
        assert refreshed is not None
        return self._to_response(refreshed)

    async def upload_photo(self, user: User, file: UploadFile) -> ProfileResponse:
        if not file.content_type or file.content_type not in self.settings.allowed_image_types:
            raise ValidationAppError(
                "Unsupported image type. Use JPEG, PNG, or WebP",
            )

        data = await file.read()
        if not data:
            raise ValidationAppError("Uploaded file is empty")
        if len(data) > self.settings.max_upload_bytes:
            raise ValidationAppError("Profile photo must be 2MB or smaller")

        ext = {
            "image/jpeg": ".jpg",
            "image/png": ".png",
            "image/webp": ".webp",
        }[file.content_type]

        media_root = Path(self.settings.media_root)
        profile_dir = media_root / "profiles"
        profile_dir.mkdir(parents=True, exist_ok=True)

        filename = f"{user.id}{ext}"
        (profile_dir / filename).write_bytes(data)

        profile = await self.get_or_create_profile(user)
        profile.photo_url = f"{self.settings.media_url_path}/profiles/{filename}"
        await self.profiles.update(profile)

        refreshed = await self.profiles.get_by_user_id(user.id)
        assert refreshed is not None
        return self._to_response(refreshed)

    def compute_completion(
        self,
        *,
        full_name: str,
        mobile: Optional[str],
        photo_url: Optional[str],
        board_id: Optional[UUID],
        class_id: Optional[UUID],
        stream_id: Optional[UUID],
        requires_stream: bool,
    ) -> tuple[int, bool, list[str]]:
        checks: list[tuple[str, bool]] = [
            ("full_name", bool(full_name and full_name.strip())),
            ("mobile", bool(mobile)),
            ("photo_url", bool(photo_url)),
            ("board", board_id is not None),
            ("class", class_id is not None),
        ]
        if requires_stream:
            checks.append(("stream", stream_id is not None))

        missing = [name for name, ok in checks if not ok]
        total = len(checks)
        completed = total - len(missing)
        percentage = int(round((completed / total) * 100)) if total else 0
        return percentage, len(missing) == 0, missing

    def _to_response(self, profile: StudentProfile) -> ProfileResponse:
        user = profile.user
        requires_stream = (
            profile.school_class.requires_stream if profile.school_class else False
        )
        percentage, is_complete, missing = self.compute_completion(
            full_name=user.full_name,
            mobile=profile.mobile,
            photo_url=profile.photo_url,
            board_id=profile.board_id,
            class_id=profile.class_id,
            stream_id=profile.stream_id,
            requires_stream=requires_stream,
        )
        return ProfileResponse(
            id=profile.id,
            user_id=profile.user_id,
            email=user.email,
            full_name=user.full_name,
            mobile=profile.mobile,
            photo_url=profile.photo_url,
            board=BoardResponse.model_validate(profile.board) if profile.board else None,
            school_class=(
                ClassResponse(
                    id=profile.school_class.id,
                    grade=profile.school_class.grade,
                    name=profile.school_class.name,
                    requires_stream=profile.school_class.requires_stream,
                )
                if profile.school_class
                else None
            ),
            stream=(
                StreamResponse.model_validate(profile.stream) if profile.stream else None
            ),
            total_xp=profile.total_xp or 0,
            completion_percentage=percentage,
            is_complete=is_complete,
            missing_fields=missing,
            created_at=profile.created_at,
            updated_at=profile.updated_at,
        )
