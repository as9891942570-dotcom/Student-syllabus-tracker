"""Seed topic-specific quizzes for all active CBSE topics (idempotent)."""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.db.session import AsyncSessionLocal, init_database_schema
from app.services.quiz_seed import ensure_quizzes_for_all_active_topics
from app.services.syllabus_seed import seed_all_cbse_syllabus


async def main() -> None:
    await init_database_schema()
    async with AsyncSessionLocal() as session:
        counts = await seed_all_cbse_syllabus(session)
        await session.commit()
        first = await ensure_quizzes_for_all_active_topics(session)
        await session.commit()
        second = await ensure_quizzes_for_all_active_topics(session)
        await session.commit()

    print("Syllabus:", counts)
    print("Quiz seed first:", first)
    print("Quiz seed second:", second)
    if second["topics"] != first["topics"]:
        raise SystemExit(1)
    print("Idempotent topic quiz seed OK.")


if __name__ == "__main__":
    asyncio.run(main())
