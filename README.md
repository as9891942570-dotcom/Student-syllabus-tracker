# EduQuest

Gamified student study tracker for Class 6–12 (students only).

## Stack

- **Frontend:** Next.js 15 (App Router), React 19, TypeScript, Tailwind, TanStack Query, Zustand, Framer Motion
- **Backend:** FastAPI, PostgreSQL, SQLAlchemy (async), Alembic, Redis, JWT
- **Infra:** Docker Compose

## Phase 1 status

Monorepo scaffold is ready:

- Backend Clean Architecture skeleton + `/api/v1/health`
- Frontend landing, auth stubs, app shell, theme toggle, API health badge
- Docker Compose for `db`, `redis`, `api`, `web`

## Phase 2 status

Authentication module is ready:

- Backend: register, login, refresh, logout, forgot-password stub, JWT + bcrypt, `users` / `refresh_tokens`
- Frontend: Login / Register / Forgot Password forms (RHF + Zod), Zustand session, protected `(app)` routes
- Tests: `pytest` auth unit + API coverage

## Phase 3 status

Student Profile module is ready:

- Backend: boards/classes/streams lookups, student profile CRUD, photo upload, completion %, Alembic `0002_profile`
- Frontend: `/profile/setup`, `/profile`, `/profile/edit`, completion bar, stream rules for Class 11–12
- Incomplete profiles are redirected away from Dashboard until 100% complete
- Tests: profile service + API coverage

## Phase 4 status

Academic syllabus tracking is ready (no teaching content):

- Backend: subjects/chapters/topics + student topic progress, Alembic `0003_syllabus`
- Scope rules: Classes 6–10 by board+class; Classes 11–12 by board+class+stream
- Frontend: My Subjects, chapters, topic checklist, syllabus overview
- Tests: syllabus service + API coverage

## Phase 5 status

XP foundation (kept; study-session UI/API later removed in Phase 8):

- Backend: `daily_activities`, profile `total_xp` (Alembic `0004_study_sessions` history)
- Study-session feature was removed: progression is topic quiz only

## Phase 6–7 status

Topic quizzes + unlock/XP/level progression are ready.

## Phase 8 status

Complete CBSE 2026–27 syllabus metadata + topic-specific quizzes; study sessions removed.

## Quick start (local — no Docker)

**API (SQLite by default):**
```powershell
cd backend
.\.venv\Scripts\activate   # or: py -3.11 -m venv .venv && pip install -r requirements-dev.txt
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
# or: ..\scripts\start-api.ps1
```

- API: http://127.0.0.1:8000  
- Swagger: http://127.0.0.1:8000/docs  
- Health: http://127.0.0.1:8000/api/v1/health  

**Frontend:**
```powershell
cd frontend
# .env.local should use 127.0.0.1 (not only localhost) on Windows
npm run dev
```

Open http://localhost:3000/register

## Quick start (Docker)

```bash
cp .env.example .env
docker compose up --build
```

- Web: http://localhost:3000  
- API: http://localhost:8000  
- Swagger: http://localhost:8000/docs  
- Health: http://localhost:8000/api/v1/health  

## Local development

### Backend

Requires **Python 3.11 or 3.12** (Docker uses 3.12). Avoid 3.14 locally until wheels catch up.

```bash
cd backend
py -3.11 -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
cp .env.example .env
# Start Postgres + Redis via: docker compose up db redis
uvicorn app.main:app --reload --port 8000
pytest
# Apply migrations when Postgres is running:
# alembic upgrade head
```

### Frontend

```bash
cd frontend
cp .env.example .env.local
npm install
npm run dev
```

## Repository layout

```
frontend/   Next.js app
backend/    FastAPI app
docker-compose.yml
```

## License

Private project — all rights reserved.
