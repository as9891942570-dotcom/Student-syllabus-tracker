"""CBSE 2026–27 syllabus catalog keyed by class and stream."""

from __future__ import annotations

from typing import Optional

from app.data.cbse_2026_27.classes_6_8 import CLASS_6, CLASS_7, CLASS_8
from app.data.cbse_2026_27.classes_9_10 import CLASS_9, CLASS_10
from app.data.cbse_2026_27.schema import CURRICULUM_VERSION, SubjectSpec
from app.data.cbse_2026_27.senior_subjects import (
    ACCOUNTANCY_11,
    ACCOUNTANCY_12,
    BIOLOGY_11,
    BIOLOGY_12,
    BUSINESS_11,
    BUSINESS_12,
    CHEMISTRY_11,
    CHEMISTRY_12,
    ECONOMICS_11,
    ECONOMICS_12,
    ENGLISH_11,
    ENGLISH_12,
    GEOGRAPHY_11,
    GEOGRAPHY_12,
    HISTORY_11,
    HISTORY_12,
    MATH_11,
    MATH_12,
    PHYSICS_11,
    PHYSICS_12,
    POLITICAL_11,
    POLITICAL_12,
)

CLASSES_6_TO_10: dict[int, list[SubjectSpec]] = {
    6: CLASS_6,
    7: CLASS_7,
    8: CLASS_8,
    9: CLASS_9,
    10: CLASS_10,
}

STREAM_CODES = (
    "SCIENCE_PCM",
    "SCIENCE_PCB",
    "SCIENCE_PCMB",
    "COMMERCE",
    "ARTS",
)

# Core academic subjects per stream. Optional electives (Computer Science,
# Physical Education, Fine Arts, additional languages, etc.) vary by school
# and student choice, so they are not seeded as if every student takes them.
_SENIOR: dict[int, dict[str, list[SubjectSpec]]] = {
    11: {
        "SCIENCE_PCM": [PHYSICS_11, CHEMISTRY_11, MATH_11, ENGLISH_11],
        "SCIENCE_PCB": [PHYSICS_11, CHEMISTRY_11, BIOLOGY_11, ENGLISH_11],
        "SCIENCE_PCMB": [PHYSICS_11, CHEMISTRY_11, MATH_11, BIOLOGY_11, ENGLISH_11],
        "COMMERCE": [ACCOUNTANCY_11, BUSINESS_11, ECONOMICS_11, ENGLISH_11],
        "ARTS": [HISTORY_11, POLITICAL_11, GEOGRAPHY_11, ENGLISH_11],
    },
    12: {
        "SCIENCE_PCM": [PHYSICS_12, CHEMISTRY_12, MATH_12, ENGLISH_12],
        "SCIENCE_PCB": [PHYSICS_12, CHEMISTRY_12, BIOLOGY_12, ENGLISH_12],
        "SCIENCE_PCMB": [PHYSICS_12, CHEMISTRY_12, MATH_12, BIOLOGY_12, ENGLISH_12],
        "COMMERCE": [ACCOUNTANCY_12, BUSINESS_12, ECONOMICS_12, ENGLISH_12],
        "ARTS": [HISTORY_12, POLITICAL_12, GEOGRAPHY_12, ENGLISH_12],
    },
}


def subjects_for_scope(grade: int, stream_code: Optional[str]) -> list[SubjectSpec]:
    if grade < 6 or grade > 12:
        return []
    if grade <= 10:
        return CLASSES_6_TO_10[grade]
    if not stream_code or stream_code not in STREAM_CODES:
        return []
    return _SENIOR[grade][stream_code]


def all_cbse_scopes() -> list[tuple[int, Optional[str]]]:
    scopes: list[tuple[int, Optional[str]]] = [(grade, None) for grade in range(6, 11)]
    for grade in (11, 12):
        for stream in STREAM_CODES:
            scopes.append((grade, stream))
    return scopes


def validate_blueprint(subjects: list[SubjectSpec]) -> list[str]:
    """Return validation errors for a subject blueprint."""
    errors: list[str] = []
    codes: set[str] = set()
    for subject_order, spec in enumerate(subjects):
        code = spec["code"]
        if code in codes:
            errors.append(f"Duplicate subject code {code}")
        codes.add(code)
        if not spec["name"].strip():
            errors.append(f"Empty subject name for {code}")
        chapter_titles: set[str] = set()
        for chapter_order, ch in enumerate(spec["chapters"]):
            title = ch["title"].strip()
            if not title:
                errors.append(f"{code}: empty chapter title at order {chapter_order}")
            if title in chapter_titles:
                errors.append(f"{code}: duplicate chapter title {title!r}")
            chapter_titles.add(title)
            topic_titles: set[str] = set()
            if not ch["topics"]:
                errors.append(f"{code}/{title}: chapter has no topics")
            for topic in ch["topics"]:
                topic_title = topic.strip()
                if not topic_title:
                    errors.append(f"{code}/{title}: empty topic title")
                lowered = topic_title.lower()
                if lowered in {
                    "introduction",
                    "important questions",
                    "practice",
                    "miscellaneous",
                    "practice set",
                    "revision checklist",
                    "grammar review",
                }:
                    errors.append(
                        f"{code}/{title}: placeholder topic {topic_title!r}",
                    )
                if topic_title in topic_titles:
                    errors.append(f"{code}/{title}: duplicate topic {topic_title!r}")
                topic_titles.add(topic_title)
    return errors


def validate_catalog() -> list[str]:
    errors: list[str] = []
    if CURRICULUM_VERSION != "CBSE 2026-27":
        errors.append(f"Unexpected curriculum version {CURRICULUM_VERSION}")
    for grade, stream in all_cbse_scopes():
        blueprint = subjects_for_scope(grade, stream)
        if not blueprint:
            errors.append(f"Missing blueprint for class {grade} stream {stream}")
            continue
        label = f"Class {grade}" + (f"/{stream}" if stream else "")
        for err in validate_blueprint(blueprint):
            errors.append(f"{label}: {err}")
    return errors
