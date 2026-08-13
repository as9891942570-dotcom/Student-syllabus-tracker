"""One-shot refresh of local quiz seed content (topic-specific questions)."""

from __future__ import annotations

import asyncio

from app.db.session import AsyncSessionLocal
from app.services.quiz_seed import refresh_all_topic_quizzes


async def main() -> None:
    async with AsyncSessionLocal() as session:
        updated = await refresh_all_topic_quizzes(session)
        await session.commit()
        print(f"Refreshed {updated} quiz(zes) with topic-specific questions.")


if __name__ == "__main__":
    asyncio.run(main())
