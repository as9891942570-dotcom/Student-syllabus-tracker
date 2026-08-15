"""Manual API check: coins awarded on first successful topic quiz (>=60%)."""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from uuid import UUID

import httpx
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.db.session import AsyncSessionLocal
from app.models.quiz import Quiz
from app.models.quiz_question import QuizQuestion

BASE = "http://127.0.0.1:8001/api/v1"
EMAIL = "coinsverify1508@gmail.com"
PASSWORD = "Secret123!"


async def correct_option_ids(quiz_id: str) -> list:
    async with AsyncSessionLocal() as session:
        quiz = (
            await session.execute(
                select(Quiz)
                .where(Quiz.id == UUID(quiz_id))
                .options(
                    selectinload(Quiz.questions).selectinload(QuizQuestion.options),
                ),
            )
        ).scalar_one()
        ids = []
        for q in sorted(quiz.questions, key=lambda x: x.sort_order):
            opt = next(o for o in q.options if o.is_correct)
            ids.append(opt.id)
        return ids


async def main() -> None:
    async with httpx.AsyncClient(timeout=60.0) as client:
        login = await client.post(f"{BASE}/auth/login", json={"email": EMAIL, "password": PASSWORD})
        if login.status_code != 200:
            await client.post(
                f"{BASE}/auth/register",
                json={"email": EMAIL, "password": PASSWORD, "full_name": "Coins Verify"},
            )
            login = await client.post(f"{BASE}/auth/login", json={"email": EMAIL, "password": PASSWORD})
        token = login.json()["access_token"]
        h = {"Authorization": f"Bearer {token}"}

        boards = (await client.get(f"{BASE}/boards", headers=h)).json()
        classes = (await client.get(f"{BASE}/classes", headers=h)).json()
        streams = (await client.get(f"{BASE}/streams", headers=h)).json()
        board = next(b for b in boards if b["code"] == "CBSE" or "CBSE" in b["name"].upper())
        klass = next(c for c in classes if c["grade"] == 12)
        stream = next(s for s in streams if s["name"] == "Science (PCM)")
        await client.put(
            f"{BASE}/profile/me",
            headers=h,
            json={
                "board_id": board["id"],
                "class_id": klass["id"],
                "stream_id": stream["id"],
                "mobile": "9876543210",
            },
        )
        me = (await client.get(f"{BASE}/profile/me", headers=h)).json()
        print("BEFORE xp=", me.get("total_xp"), "coins=", me.get("total_coins"))

        subjects = (await client.get(f"{BASE}/syllabus/subjects", headers=h)).json()
        phy = next(s for s in subjects if s["code"] == "PHY")
        detail = (await client.get(f"{BASE}/syllabus/subjects/{phy['id']}", headers=h)).json()

        # Find first incomplete unlocked topic with a quiz
        topic = None
        quiz_id = None
        for ch_summary in detail["chapters"]:
            ch = (await client.get(f"{BASE}/syllabus/chapters/{ch_summary['id']}/topics", headers=h)).json()
            for t in ch["topics"]:
                if t.get("is_locked") or t.get("is_completed"):
                    continue
                quizzes = (await client.get(f"{BASE}/quizzes/topics/{t['id']}", headers=h)).json()
                if quizzes:
                    topic = t
                    quiz_id = quizzes[0]["id"]
                    break
            if topic:
                break

        if topic is None:
            print("No incomplete unlocked topic found — using first unlocked for retry check")
            ch = (await client.get(f"{BASE}/syllabus/chapters/{detail['chapters'][0]['id']}/topics", headers=h)).json()
            topic = next(t for t in ch["topics"] if not t.get("is_locked"))
            quizzes = (await client.get(f"{BASE}/quizzes/topics/{topic['id']}", headers=h)).json()
            quiz_id = quizzes[0]["id"]

        print("TOPIC", topic["title"], "completed=", topic["is_completed"])

        active = await client.get(f"{BASE}/quiz-attempts/active", headers=h)
        if active.status_code == 200 and active.json():
            await client.post(f"{BASE}/quiz-attempts/{active.json()['id']}/complete", headers=h)

        correct_ids = await correct_option_ids(quiz_id)
        start = await client.post(f"{BASE}/quizzes/{quiz_id}/start", headers=h)
        attempt_id = start.json()["id"]
        total = start.json()["total_questions"]
        # Answer 80% correctly
        need = max(1, int(total * 0.8 + 0.999))
        for i in range(total):
            q = (await client.get(f"{BASE}/quiz-attempts/{attempt_id}/current-question", headers=h)).json()
            if i < need:
                option_id = str(correct_ids[i])
            else:
                option_id = q["options"][0]["id"]
                if option_id == str(correct_ids[i]):
                    option_id = q["options"][1]["id"]
            await client.post(
                f"{BASE}/quiz-attempts/{attempt_id}/answers",
                headers=h,
                json={"option_id": option_id},
            )
            if i < total - 1:
                await client.post(f"{BASE}/quiz-attempts/{attempt_id}/next", headers=h)

        done = (await client.post(f"{BASE}/quiz-attempts/{attempt_id}/complete", headers=h)).json()
        print(
            "FIRST complete %=",
            done.get("percentage"),
            "topic_completed=",
            done.get("topic_completed"),
            "coins_earned=",
            done.get("coins_earned"),
            "coins_awarded=",
            done.get("coins_awarded"),
            "total_coins=",
            done.get("total_coins"),
            "xp=",
            done.get("total_xp"),
            "next_unlocked=",
            done.get("next_topic_unlocked"),
        )
        me2 = (await client.get(f"{BASE}/profile/me", headers=h)).json()
        print("AFTER xp=", me2.get("total_xp"), "coins=", me2.get("total_coins"))

        # Retry
        start2 = await client.post(f"{BASE}/quizzes/{quiz_id}/start", headers=h)
        attempt2 = start2.json()["id"]
        for i in range(total):
            await client.post(
                f"{BASE}/quiz-attempts/{attempt2}/answers",
                headers=h,
                json={"option_id": str(correct_ids[i])},
            )
            if i < total - 1:
                await client.post(f"{BASE}/quiz-attempts/{attempt2}/next", headers=h)
        retry = (await client.post(f"{BASE}/quiz-attempts/{attempt2}/complete", headers=h)).json()
        print(
            "RETRY coins_earned=",
            retry.get("coins_earned"),
            "coins_awarded=",
            retry.get("coins_awarded"),
            "total_coins=",
            retry.get("total_coins"),
        )
        me3 = (await client.get(f"{BASE}/profile/me", headers=h)).json()
        print("REFRESH xp=", me3.get("total_xp"), "coins=", me3.get("total_coins"))


if __name__ == "__main__":
    asyncio.run(main())
