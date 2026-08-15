"""CBSE 2026–27 syllabus metadata."""

from app.data.cbse_2026_27.catalog import (
    STREAM_CODES,
    all_cbse_scopes,
    subjects_for_scope,
    validate_catalog,
)
from app.data.cbse_2026_27.schema import CURRICULUM_VERSION

__all__ = [
    "CURRICULUM_VERSION",
    "STREAM_CODES",
    "all_cbse_scopes",
    "subjects_for_scope",
    "validate_catalog",
]
