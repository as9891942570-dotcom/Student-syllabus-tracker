"""Student level calculation from total XP (single source of truth).

Thresholds (initial Phase 7):
  Level 1: 0–99
  Level 2: 100–249
  Level 3: 250–499
  Level 4: 500–999
  Level 5: 1000–1999

After level 5, floors continue by doubling (2000, 4000, 8000, …)
so thresholds stay easy to extend later.
"""

from __future__ import annotations

from dataclasses import dataclass


# Explicit floors for levels 1–5, then doubled thereafter.
_BASE_LEVEL_FLOORS: tuple[int, ...] = (0, 100, 250, 500, 1000, 2000)


def level_floors_up_to(total_xp: int) -> list[int]:
    """Return level floor XP values covering at least ``total_xp``."""
    floors = list(_BASE_LEVEL_FLOORS)
    xp = max(0, int(total_xp))
    while floors[-1] <= xp:
        floors.append(floors[-1] * 2)
    # Ensure one floor beyond current XP so "next level" is defined.
    if floors[-1] <= xp:
        floors.append(floors[-1] * 2)
    return floors


@dataclass(frozen=True)
class LevelProgress:
    level: int
    total_xp: int
    level_floor_xp: int
    next_level_xp: int
    xp_into_level: int
    xp_needed_for_next: int
    level_progress_percentage: int


def calculate_level_progress(total_xp: int) -> LevelProgress:
    """Map total XP → current level and progress toward the next level."""
    xp = max(0, int(total_xp))
    floors = level_floors_up_to(xp)

    level = 1
    for index, floor in enumerate(floors):
        if xp >= floor:
            level = index + 1
        else:
            break

    # If XP reached the last known floor exactly, ensure a next floor exists.
    while level >= len(floors):
        floors.append(floors[-1] * 2)

    level_floor = floors[level - 1]
    next_level_xp = floors[level]
    into = xp - level_floor
    needed = max(next_level_xp - level_floor, 1)
    pct = int(round(min(into, needed) / needed * 100))

    return LevelProgress(
        level=level,
        total_xp=xp,
        level_floor_xp=level_floor,
        next_level_xp=next_level_xp,
        xp_into_level=into,
        xp_needed_for_next=needed,
        level_progress_percentage=pct,
    )


def calculate_level(total_xp: int) -> int:
    return calculate_level_progress(total_xp).level
