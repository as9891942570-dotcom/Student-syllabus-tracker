"""End-to-end: register Class 12 PCM user, fetch quizzes, print real questions via live API."""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import httpx

BASE = "http://127.0.0.1:8001/api/v1"
EMAIL = "pcmverify1408@gmail.com"
PASSWORD = "Secret123!"

SAMPLES = {
    "PHY": [
        ("Electric Charges and Fields", "Electric charge"),
        ("Electric Charges and Fields", "Coulomb's law"),
    ],
    "CHEM": [
        ("Solutions", "Types of solutions"),
        ("Solutions", "Henry's law"),
        ("Electrochemistry", "Nernst equation"),
    ],
    "MATH": [
        ("Relations and Functions", "Types of relations"),
        ("Relations and Functions", "Equivalence relations"),
        ("Matrices", "Types of matrices"),
    ],
    "ENG": [
        ("Flamingo Prose", "The Last Lesson"),
        ("Vistas", "The Tiger King"),
    ],
}


async def main() -> None:
    async with httpx.AsyncClient(timeout=60.0) as client:
        login = await client.post(f"{BASE}/auth/login", json={"email": EMAIL, "password": PASSWORD})
        if login.status_code != 200:
            reg = await client.post(
                f"{BASE}/auth/register",
                json={"email": EMAIL, "password": PASSWORD, "full_name": "PCM Verify"},
            )
            print("REGISTER", reg.status_code)
            login = await client.post(f"{BASE}/auth/login", json={"email": EMAIL, "password": PASSWORD})
        print("LOGIN", login.status_code)
        token = login.json()["access_token"]
        h = {"Authorization": f"Bearer {token}"}

        boards = (await client.get(f"{BASE}/boards", headers=h)).json()
        classes = (await client.get(f"{BASE}/classes", headers=h)).json()
        streams = (await client.get(f"{BASE}/streams", headers=h)).json()
        board = next(b for b in boards if b["code"] in {"CBSE", "cbse"} or "CBSE" in b["name"].upper())
        klass = next(c for c in classes if c["grade"] == 12)
        stream = next(s for s in streams if s["code"] in {"SCIENCE_PCM", "PCM"} or "PCM" in s["name"] and "B" not in s["name"].replace("PCM", ""))
        # prefer exact Science (PCM)
        stream = next((s for s in streams if s["name"] == "Science (PCM)"), stream)
        print("SCOPE", board["name"], klass["name"], stream["name"], stream["code"])

        upd = await client.put(
            f"{BASE}/profile/me",
            headers=h,
            json={"board_id": board["id"], "class_id": klass["id"], "stream_id": stream["id"]},
        )
        print("PROFILE UPDATE", upd.status_code, upd.json().get("missing_fields"), upd.json().get("school_class"), upd.json().get("stream"))

        subjects = (await client.get(f"{BASE}/syllabus/subjects", headers=h)).json()
        print("\n=== SUBJECTS FROM API ===")
        by_code = {}
        for s in subjects:
            print(f"  {s['code']:6} {s['name']:20} chapters={s['chapter_count']} topics={s['topic_count']} id={s['id']}")
            by_code[s["code"]] = s

        for code, pairs in SAMPLES.items():
            subj = by_code[code]
            detail = (await client.get(f"{BASE}/syllabus/subjects/{subj['id']}", headers=h)).json()
            chapters = {c["title"]: c for c in detail["chapters"]}
            print(f"\n======== {code} {subj['name']} ========")
            for ch_title, topic_title in pairs:
                chapter = chapters.get(ch_title)
                if not chapter:
                    print("MISSING CHAPTER", ch_title, "have", list(chapters)[:8])
                    continue
                ch_full = (await client.get(f"{BASE}/syllabus/chapters/{chapter['id']}/topics", headers=h)).json()
                topic = next((t for t in ch_full["topics"] if t["title"] == topic_title), None)
                if not topic:
                    print("MISSING TOPIC", topic_title, "in", [t["title"] for t in ch_full["topics"]])
                    continue
                print(f"TOPIC locked={topic.get('is_locked')} current={topic.get('is_current')} id={topic['id']} title={topic['title']}")
                if topic.get("is_locked"):
                    unlock = await client.patch(
                        f"{BASE}/syllabus/topics/{topic['id']}/progress",
                        headers=h,
                        json={"is_completed": False},
                    )
                    print("  unlock-attempt", unlock.status_code, unlock.text[:160])
                    # complete previous topics in chapter
                    for prev in ch_full["topics"]:
                        if prev["title"] == topic_title:
                            break
                        await client.patch(
                            f"{BASE}/syllabus/topics/{prev['id']}/progress",
                            headers=h,
                            json={"is_completed": True},
                        )
                    ch_full = (await client.get(f"{BASE}/syllabus/chapters/{chapter['id']}/topics", headers=h)).json()
                    topic = next((t for t in ch_full["topics"] if t["title"] == topic_title), topic)
                    print(f"  after unlock locked={topic.get('is_locked')}")
                quizzes = (await client.get(f"{BASE}/quizzes/topics/{topic['id']}", headers=h)).json()
                print("  quizzes", [(q["title"], q["question_count"], q["id"]) for q in quizzes])
                if not quizzes:
                    print("  NO QUIZ LISTED")
                    continue
                quiz = quizzes[0]
                detail_q = (await client.get(f"{BASE}/quizzes/{quiz['id']}", headers=h)).json()
                print("  quiz_detail question_count", detail_q["question_count"], "title", detail_q["title"])
                if detail_q["question_count"] == 0:
                    print("  EMPTY QUIZ VIA API")
                    continue
                # cancel any active attempt by completing if needed - start may 409
                start = await client.post(f"{BASE}/quizzes/{quiz['id']}/start", headers=h)
                if start.status_code == 409:
                    active = await client.get(f"{BASE}/quiz-attempts/active", headers=h)
                    print("  409 active", active.status_code, str(active.json())[:200])
                    if active.status_code == 200 and active.json():
                        aid = active.json()["id"]
                        await client.post(f"{BASE}/quiz-attempts/{aid}/complete", headers=h)
                    start = await client.post(f"{BASE}/quizzes/{quiz['id']}/start", headers=h)
                print("  START", start.status_code)
                if start.status_code not in (200, 201):
                    print("  START ERR", start.text[:400])
                    continue
                attempt = start.json()
                q = (await client.get(f"{BASE}/quiz-attempts/{attempt['id']}/current-question", headers=h)).json()
                print(f"  Q1: {q.get('prompt')}")
                opts = q.get("options") or []
                letters = "ABCD"
                for i, o in enumerate(opts):
                    print(f"    {letters[i]}: {o['text']}")
                # complete without answering to free lock? complete may require answers
                # expire by complete might fail; try complete anyway
                done = await client.post(f"{BASE}/quiz-attempts/{attempt['id']}/complete", headers=h)
                print("  complete", done.status_code, done.text[:120])


if __name__ == "__main__":
    asyncio.run(main())
