"""Seed the complete CBSE 2026–27 syllabus (idempotent).

Run from the backend directory:

    python scripts/seed_cbse_syllabus.py
"""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

# Allow `python scripts/seed_cbse_syllabus.py` from backend/.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.data.cbse_2026_27.catalog import validate_catalog
from app.db.session import AsyncSessionLocal, init_database_schema
from app.services.syllabus_seed import count_active_cbse_syllabus, seed_all_cbse_syllabus


async def main() -> None:
    errors = validate_catalog()
    if errors:
        print("Catalog validation failed:")
        for error in errors:
            print(f"  - {error}")
        raise SystemExit(1)

    await init_database_schema()
    async with AsyncSessionLocal() as session:
        first = await seed_all_cbse_syllabus(session)
        await session.commit()
        second = await seed_all_cbse_syllabus(session)
        await session.commit()
        after = await count_active_cbse_syllabus(session)

    print("CBSE 2026–27 syllabus seed complete.")
    print(f"First run:  {first}")
    print(f"Second run: {second}")
    print(f"Verified:   {after}")
    if first != second:
        print("WARNING: row counts changed on the second run.")
        raise SystemExit(1)
    print("Idempotent: no duplicate rows created.")


if __name__ == "__main__":
    asyncio.run(main())
