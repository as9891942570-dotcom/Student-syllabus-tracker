"""CBSE 2026–27 syllabus metadata types (tracking only, no teaching content)."""

from __future__ import annotations

from typing import TypedDict

CURRICULUM_VERSION = "CBSE 2026-27"


class TopicSpec(TypedDict):
    title: str


class ChapterSpec(TypedDict):
    title: str
    topics: list[str]


class SubjectSpec(TypedDict):
    code: str
    name: str
    chapters: list[ChapterSpec]


def chapter(title: str, topics: list[str]) -> ChapterSpec:
    return {"title": title, "topics": topics}


def subject(code: str, name: str, chapters: list[ChapterSpec]) -> SubjectSpec:
    return {"code": code, "name": name, "chapters": chapters}
