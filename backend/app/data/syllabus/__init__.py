"""Central syllabus data source.

Services should load subjects from this package, not hard-code class/subject lists.
"""

from app.data.syllabus.catalog import (
    SUPPORTED_BOARDS,
    SUPPORTED_GRADES,
    STREAM_CODES,
    subjects_for_profile,
    validate_profile_blueprint,
)

__all__ = [
    "SUPPORTED_BOARDS",
    "SUPPORTED_GRADES",
    "STREAM_CODES",
    "subjects_for_profile",
    "validate_profile_blueprint",
]
