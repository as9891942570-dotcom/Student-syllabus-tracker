"""Verify Class 12 PCM English Core structure and sample quizzes via live API."""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import httpx
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import get_settings
from app.models.chapter import Chapter
from app.models.quiz import Quiz
from app.models.quiz_question import QuizQuestion
from app.models.school_class import SchoolClass
from app.models.stream import Stream
from app.models.subject import Subject
from app.models.topic import Topic
from app.services.topic_quiz_builder import build_topic_questions, is_meta_question

BASE = "http://127.0.0.1:8001/api/v1"
EMAIL = "engverify1408@gmail.com"
PASSWORD = "Secret123!"

SAMPLES = [
    ("Flamingo – Prose", "The Last Lesson"),
    ("Flamingo – Poetry", "A Roadside Stand"),
    ("Vistas – Supplementary Reader", "The Tiger King"),
    ("Writing Skills", "Notice Writing"),
    ("Grammar / Language", "Modal Auxiliaries"),
]


async def report_db() -> None:
    settings = get_settings()
    print("DB", settings.database_url)
    engine = create_async_engine(settings.database_url, echo=False)
    Session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    async with Session() as db:
        subj = (
            await db.execute(
                select(Subject)
                .join(SchoolClass)
                .join(Stream)
                .where(
                    SchoolClass.grade == 12,
                    Stream.name == "Science (PCM)",
                    Subject.code == "ENG",
                    Subject.is_active.is_(True),
                )
            )
        ).scalar_one()
        chapters = (
            await db.execute(
                select(Chapter)
                .where(Chapter.subject_id == subj.id, Chapter.is_active.is_(True))
                .order_by(Chapter.sort_order)
            )
        ).scalars().all()
        print("ENG chapters", len(chapters))
        total_topics = 0
        total_q = 0
        for ch in chapters:
            topics = (
                await db.execute(
                    select(Topic).where(Topic.chapter_id == ch.id, Topic.is_active.is_(True)).order_by(Topic.sort_order)
                )
            ).scalars().all()
            total_topics += len(topics)
            qs = (
                await db.execute(
                    select(QuizQuestion.prompt)
                    .join(Quiz)
                    .join(Topic)
                    .where(Topic.chapter_id == ch.id, Topic.is_active.is_(True), Quiz.is_active.is_(True))
                )
            ).scalars().all()
            meta = sum(1 for p in qs if is_meta_question(p))
            total_q += len(qs)
            print(f"  {ch.title}: topics={len(topics)} questions={len(qs)} meta={meta}")
            for t in topics:
                bank = build_topic_questions(topic_title=t.title, chapter_title=ch.title, subject_code="ENG", grade=12)
                if not bank:
                    print("    UNMAPPED", t.title)
        print("TOTAL topics", total_topics, "questions", total_q)
        assert total_topics == 31, total_topics
        assert len(chapters) == 6, len(chapters)
    await engine.dispose()


async def report_api() -> None:
    async with httpx.AsyncClient(timeout=60.0) as client:
        login = await client.post(f"{BASE}/auth/login", json={"email": EMAIL, "password": PASSWORD})
        if login.status_code != 200:
            await client.post(
                f"{BASE}/auth/register",
                json={"email": EMAIL, "password": PASSWORD, "full_name": "Eng Verify"},
            )
            login = await client.post(f"{BASE}/auth/login", json={"email": EMAIL, "password": PASSWORD})
        token = login.json()["access_token"]
        h = {"Authorization": f"Bearer {token}"}
        boards = (await client.get(f"{BASE}/boards", headers=h)).json()
        classes = (await client.get(f"{BASE}/classes", headers=h)).json()
        streams = (await client.get(f"{BASE}/streams", headers=h)).json()
        board = next(b for b in boards if "CBSE" in b["name"].upper() or b["code"] == "CBSE")
        klass = next(c for c in classes if c["grade"] == 12)
        stream = next(s for s in streams if s["name"] == "Science (PCM)")
        await client.put(
            f"{BASE}/profile/me",
            headers=h,
            json={"board_id": board["id"], "class_id": klass["id"], "stream_id": stream["id"]},
        )
        subjects = (await client.get(f"{BASE}/syllabus/subjects", headers=h)).json()
        eng = next(s for s in subjects if s["code"] == "ENG")
        print("API ENG chapters", eng["chapter_count"], "topics", eng["topic_count"])
        assert eng["chapter_count"] == 6
        assert eng["topic_count"] == 31
        detail = (await client.get(f"{BASE}/syllabus/subjects/{eng['id']}", headers=h)).json()
        by_title = {c["title"]: c for c in detail["chapters"]}
        for ch_title, topic_title in SAMPLES:
            chapter = by_title[ch_title]
            ch_full = (await client.get(f"{BASE}/syllabus/chapters/{chapter['id']}/topics", headers=h)).json()
            topic = next(t for t in ch_full["topics"] if t["title"] == topic_title)
            for prev in ch_full["topics"]:
                if prev["title"] == topic_title:
                    break
                await client.patch(
                    f"{BASE}/syllabus/topics/{prev['id']}/progress",
                    headers=h,
                    json={"is_completed": True},
                )
            quizzes = (await client.get(f"{BASE}/quizzes/topics/{topic['id']}", headers=h)).json()
            quiz = quizzes[0]
            start = await client.post(f"{BASE}/quizzes/{quiz['id']}/start", headers=h)
            if start.status_code == 409:
                active = await client.get(f"{BASE}/quiz-attempts/active", headers=h)
                if active.status_code == 200 and active.json():
                    await client.post(f"{BASE}/quiz-attempts/{active.json()['id']}/complete", headers=h)
                start = await client.post(f"{BASE}/quizzes/{quiz['id']}/start", headers=h)
            attempt = start.json()
            q = (await client.get(f"{BASE}/quiz-attempts/{attempt['id']}/current-question", headers=h)).json()
            print("=" * 60)
            print("CHAPTER:", ch_title)
            print("TOPIC:", topic_title)
            print("QUESTION:", q["prompt"])
            for i, opt in enumerate(q["options"]):
                print(f"  {'ABCD'[i]}: {opt['text']}")
            await client.post(f"{BASE}/quiz-attempts/{attempt['id']}/complete", headers=h)


if __name__ == "__main__":
    asyncio.run(report_db())
    asyncio.run(report_api())
