"""Subject/topic concept banks for Class 12 PCM (and extras).

Importing this package registers banks into app.data.quiz_concepts.CONCEPT_BANKS
and subject-scoped keyword maps.
"""

from __future__ import annotations

from . import (
    biology,
    chemistry_11,
    chemistry_12,
    chemistry_12_extra,
    commerce_arts,
    english_11,
    english_12,
    english_12_extra,
    mathematics_11,
    mathematics_12,
    mathematics_12_extra,
    middle_school,
    physics_11,
    physics_12_extra,
)


def register_all() -> None:
    chemistry_12.register()
    chemistry_12_extra.register()
    chemistry_11.register()
    mathematics_12.register()
    mathematics_12_extra.register()
    mathematics_11.register()
    english_12.register()
    english_12_extra.register()
    english_11.register()
    physics_11.register()
    physics_12_extra.register()
    biology.register()
    middle_school.register()
    commerce_arts.register()


__all__ = ["register_all"]
