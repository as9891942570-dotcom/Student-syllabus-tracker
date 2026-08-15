"""Shared helpers for subject concept banks."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.data.quiz_concepts import QuestionBank

Question = tuple[str, list[tuple[str, bool]]]
QuestionBank = list[Question]


def q(prompt: str, correct: str, wrong: list[str]) -> Question:
    return prompt, [(correct, True)] + [(w, False) for w in wrong]


def register_keys(keys: list[str], bank: QuestionBank) -> None:
    from app.data.quiz_concepts import _register

    _register(keys, bank)


def register_subject_keywords(subject_code: str, entries: list[tuple[tuple[str, ...], QuestionBank]]) -> None:
    from app.data.quiz_concepts import SUBJECT_KEYWORD_BANKS

    code = subject_code.strip().upper()
    SUBJECT_KEYWORD_BANKS.setdefault(code, []).extend(entries)
