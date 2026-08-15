"""Build real concept/numerical MCQs for a syllabus topic.

Root rule: questions must test knowledge of the topic — never meta/study advice.
"""

from __future__ import annotations

import hashlib
import re

from app.data.quiz_concepts import (
    CONCEPT_BANKS,
    GLOBAL_CHAPTER_TOPIC_BANKS,
    KEYWORD_BANKS,
    SUBJECT_KEYWORD_BANKS,
    QuestionBank,
)

MAX_QUESTIONS_PER_TOPIC = 20

# Reject meta / study-advice / topic-name-echo prompts.
META_PROMPT_PATTERNS: tuple[re.Pattern[str], ...] = tuple(
    re.compile(p, re.I)
    for p in (
        r"while studying",
        r"what should a student",
        r"what should students",
        r"primarily focus on",
        r"important when learning",
        r"best describes",
        r"what does this topic",
        r"how should .* be used in syllabus",
        r"mark progress",
        r"unlock the next topic",
        r"completing the topic",
        r"reviewing the topic",
        r"definitions, relations, and applications",
        r"core concept of \".*\" within",
        r"ideas and methods used to understand",
        r"belongs under which chapter context",
        r"which chapter contains the topic",
        r"stays on-topic for",
        r"avoid other topics",
        r"progress should reflect",
        r"selected syllabus topic",
        r"eduquest",
        r"syllabus progress",
        r"xp be awarded",
        r"tracking a topic as complete",
        r"which approach best helps you review",
        r"ready to mark as progress",
        r"what should you focus on while studying",
    )
)

META_OPTION_PATTERNS: tuple[re.Pattern[str], ...] = tuple(
    re.compile(p, re.I)
    for p in (
        r"^the definitions, relations, and applications",
        r"unrelated entertainment",
        r"skipping the checklist",
        r"teacher'?s lesson",
        r"entertainment trivia",
        r"replace .* with accountancy",
        r"literary devices from poetry",
        r"partnership deed",
    )
)

def normalize_topic_key(topic_title: str) -> str:
    return " ".join(topic_title.strip().lower().split())


def normalize_chapter_key(chapter_title: str) -> str:
    return " ".join(chapter_title.strip().lower().split())


def is_meta_question(prompt: str, options: list[tuple[str, bool]] | None = None) -> bool:
    """True if the question is study-advice / generic / topic-name echo."""
    if any(p.search(prompt) for p in META_PROMPT_PATTERNS):
        return True
    if options:
        for text, _ in options:
            if any(p.search(text) for p in META_OPTION_PATTERNS):
                return True
    return False


def _shuffle_options(
    prompt: str,
    options: list[tuple[str, bool]],
) -> list[tuple[str, bool]]:
    seed = int(hashlib.md5(prompt.encode()).hexdigest()[:8], 16)
    indexed = list(enumerate(options))
    indexed.sort(key=lambda item: (item[0] + seed) % 7)
    ordered = [opt for _, opt in indexed]
    if sum(1 for _, ok in ordered if ok) != 1:
        raise ValueError(f"Question must have exactly one correct option: {prompt}")
    return ordered


def _dedupe_and_cap(bank: QuestionBank, limit: int = MAX_QUESTIONS_PER_TOPIC) -> QuestionBank:
    seen: set[str] = set()
    out: QuestionBank = []
    for prompt, options in bank:
        if is_meta_question(prompt, options):
            continue
        key = normalize_topic_key(prompt)
        if key in seen:
            continue
        if sum(1 for _, ok in options if ok) != 1 or len(options) < 2:
            continue
        seen.add(key)
        out.append((prompt, _shuffle_options(prompt, list(options))))
        if len(out) >= limit:
            break
    return out


def _lookup_chapter_topic(chapter_title: str, topic_title: str) -> QuestionBank | None:
    if not chapter_title or not topic_title:
        return None
    ch = normalize_chapter_key(chapter_title)
    tp = normalize_topic_key(topic_title)
    for (raw_ch, raw_tp), bank in GLOBAL_CHAPTER_TOPIC_BANKS.items():
        if normalize_chapter_key(raw_ch) == ch and normalize_topic_key(raw_tp) == tp:
            return list(bank)
    # Punctuation-insensitive chapter/topic match
    ch_c = re.sub(r"[^a-z0-9\s]", "", ch)
    tp_c = re.sub(r"[^a-z0-9\s]", "", tp)
    for (raw_ch, raw_tp), bank in GLOBAL_CHAPTER_TOPIC_BANKS.items():
        if (
            re.sub(r"[^a-z0-9\s]", "", normalize_chapter_key(raw_ch)) == ch_c
            and re.sub(r"[^a-z0-9\s]", "", normalize_topic_key(raw_tp)) == tp_c
        ):
            return list(bank)
    return None


def _keyword_match(topic_key: str, entries: list[tuple[tuple[str, ...], QuestionBank]]) -> QuestionBank | None:
    best: QuestionBank | None = None
    best_len = 0
    for keywords, bank in entries:
        for kw in keywords:
            if kw in topic_key and len(kw) > best_len:
                best = list(bank)
                best_len = len(kw)
    return best


def resolve_concept_bank(
    topic_title: str,
    *,
    chapter_title: str = "",
    subject_code: str = "",
) -> QuestionBank | None:
    """Return curated concept bank for this topic, or None if unmapped.

    Resolution order:
    1. (chapter, topic) exact map — required for colliding titles
    2. exact topic title in CONCEPT_BANKS
    3. punctuation-insensitive topic title
    4. subject-scoped keyword banks (never cross-subject)
    5. legacy global KEYWORD_BANKS only when subject_code is empty
    """
    # 1. Chapter-scoped banks first (Preparation / Properties / Applications / …)
    chapter_bank = _lookup_chapter_topic(chapter_title, topic_title)
    if chapter_bank is not None:
        return chapter_bank

    key = normalize_topic_key(topic_title)
    if key in CONCEPT_BANKS:
        return list(CONCEPT_BANKS[key])

    # 2. Alias: strip punctuation differences
    compact = re.sub(r"[^a-z0-9\s]", "", key)
    for registered, bank in CONCEPT_BANKS.items():
        if re.sub(r"[^a-z0-9\s]", "", registered) == compact:
            return list(bank)

    code = (subject_code or "").strip().upper()
    # 3. Subject-scoped keywords — never use Physics banks for Chem/Math/English
    if code and code in SUBJECT_KEYWORD_BANKS:
        matched = _keyword_match(key, SUBJECT_KEYWORD_BANKS[code])
        if matched is not None:
            return matched
        # Known subject with no keyword hit: do not fall through to global Physics-heavy banks
        return None

    # 4. Legacy global keywords only when subject is unknown (older call sites / tests)
    if not code:
        return _keyword_match(key, KEYWORD_BANKS)
    return None


def build_topic_questions(
    *,
    topic_title: str,
    chapter_title: str = "",
    subject_code: str = "",
    grade: int = 10,
) -> QuestionBank:
    """
    Return up to 20 real concept/numerical MCQs for the topic.

    If no concept mapping exists, returns an empty list (no generic fillers).
    """
    _ = grade  # reserved for grade-specific banks later
    bank = resolve_concept_bank(
        topic_title,
        chapter_title=chapter_title,
        subject_code=subject_code,
    )
    if not bank:
        return []
    return _dedupe_and_cap(bank)


def validate_question_bank(topic_title: str, bank: QuestionBank) -> list[str]:
    """Return validation errors; empty list means OK."""
    errors: list[str] = []
    if len(bank) > MAX_QUESTIONS_PER_TOPIC:
        errors.append(f"more than {MAX_QUESTIONS_PER_TOPIC} questions")
    prompts = [p for p, _ in bank]
    if len(prompts) != len({normalize_topic_key(p) for p in prompts}):
        errors.append("duplicate prompts")
    for prompt, options in bank:
        if is_meta_question(prompt, options):
            errors.append(f"meta question: {prompt[:80]}")
        if sum(1 for _, ok in options if ok) != 1:
            errors.append(f"bad options: {prompt[:40]}")
        if len(options) < 2:
            errors.append(f"too few options: {prompt[:40]}")
    _ = topic_title
    return errors


def questions_match_topic(prompt: str, topic_title: str) -> bool:
    """
    Legacy helper used by older tests.

    For curated banks, prompts may not literally contain the topic title
    (e.g. Coulomb numericals). Prefer validate_question_bank / is_meta_question.
    """
    if is_meta_question(prompt):
        return False
    topic = normalize_topic_key(topic_title)
    prompt_key = normalize_topic_key(prompt)
    if topic and any(len(w) >= 4 and w in prompt_key for w in topic.split()):
        return True
    return resolve_concept_bank(topic_title) is not None and not is_meta_question(prompt)
