"""Board + class + stream syllabus catalog.

EduQuest loads the student syllabus from this module. To add or update
chapters/topics, edit the data files under app.data.cbse_2026_27 (or a
future board-specific package) — application services stay unchanged.

Currently CBSE, ICSE, and State Board share the same NCERT-aligned
concept catalog (real chapter/topic names, no filler titles). Board is
still part of the lookup key so a distinct ICSE/State tree can be added
here later without changing SyllabusService.
"""

from __future__ import annotations

from typing import Optional

from app.data.cbse_2026_27.catalog import STREAM_CODES, subjects_for_scope, validate_blueprint
from app.data.cbse_2026_27.schema import SubjectSpec

SUPPORTED_BOARDS = ("CBSE", "ICSE", "STATE")
SUPPORTED_GRADES = tuple(range(6, 13))

_BOARD_ALIASES = {
    "CBSE": "CBSE",
    "ICSE": "ICSE",
    "STATE": "STATE",
    "STATE BOARD": "STATE",
    "STATEBOARD": "STATE",
}


def normalize_board_code(board_code: str | None) -> str:
    raw = (board_code or "CBSE").strip().upper()
    return _BOARD_ALIASES.get(raw, raw)


def subjects_for_profile(
    board_code: str,
    grade: int,
    stream_code: str | None,
) -> list[SubjectSpec]:
    """Return the subject/chapter/topic tree for an academic profile."""
    board = normalize_board_code(board_code)
    if board not in SUPPORTED_BOARDS:
        return []
    if grade not in SUPPORTED_GRADES:
        return []
    effective_stream = stream_code if grade >= 11 else None
    # Shared academic catalog keyed by board so board-specific data can land here.
    _ = board
    return list(subjects_for_scope(grade, effective_stream))


def validate_profile_blueprint(
    board_code: str,
    grade: int,
    stream_code: Optional[str],
) -> list[str]:
    blueprint = subjects_for_profile(board_code, grade, stream_code)
    if not blueprint:
        return [f"No syllabus for {board_code} class {grade} stream {stream_code}"]
    return validate_blueprint(blueprint)
