"""API v1 router aggregation."""

from fastapi import APIRouter

from app.api.v1.endpoints import auth, health, profile, quizzes, study_sessions, syllabus

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(profile.router)
api_router.include_router(syllabus.router)
api_router.include_router(study_sessions.router)
api_router.include_router(quizzes.router)
