"""Quiz API routes."""

from typing import Annotated, Optional
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.auth import get_current_user
from app.dependencies.db import get_db
from app.models.user import User
from app.schemas.quiz import (
    QuizAttemptResponse,
    QuizDetail,
    QuizHistoryItem,
    QuizQuestionPublic,
    QuizSummary,
    SubmitAnswerRequest,
    SubmitAnswerResponse,
)
from app.services.quiz import QuizService

router = APIRouter(tags=["quizzes"])


@router.get("/quizzes/topics/{topic_id}", response_model=list[QuizSummary])
async def list_quizzes_for_topic(
    topic_id: UUID,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> list[QuizSummary]:
    return await QuizService(session).list_for_topic(current_user, topic_id)


@router.get("/quizzes/{quiz_id}", response_model=QuizDetail)
async def get_quiz(
    quiz_id: UUID,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> QuizDetail:
    return await QuizService(session).get_quiz(current_user, quiz_id)


@router.post("/quizzes/{quiz_id}/start", response_model=QuizAttemptResponse, status_code=201)
async def start_quiz(
    quiz_id: UUID,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> QuizAttemptResponse:
    return await QuizService(session).start(current_user, quiz_id)


@router.get("/quiz-attempts/active", response_model=Optional[QuizAttemptResponse])
async def get_active_attempt(
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> Optional[QuizAttemptResponse]:
    return await QuizService(session).get_active(current_user)


@router.get("/quiz-attempts/history", response_model=list[QuizHistoryItem])
async def quiz_history(
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> list[QuizHistoryItem]:
    return await QuizService(session).history(current_user)


@router.get("/quiz-attempts/{attempt_id}", response_model=QuizAttemptResponse)
async def get_attempt(
    attempt_id: UUID,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> QuizAttemptResponse:
    return await QuizService(session).get_attempt(current_user, attempt_id)


@router.get(
    "/quiz-attempts/{attempt_id}/current-question",
    response_model=QuizQuestionPublic,
)
async def get_current_question(
    attempt_id: UUID,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> QuizQuestionPublic:
    return await QuizService(session).current_question(current_user, attempt_id)


@router.post(
    "/quiz-attempts/{attempt_id}/answers",
    response_model=SubmitAnswerResponse,
)
async def submit_answer(
    attempt_id: UUID,
    payload: SubmitAnswerRequest,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> SubmitAnswerResponse:
    return await QuizService(session).submit_answer(current_user, attempt_id, payload)


@router.post(
    "/quiz-attempts/{attempt_id}/next",
    response_model=QuizAttemptResponse,
)
async def next_question(
    attempt_id: UUID,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> QuizAttemptResponse:
    return await QuizService(session).next_question(current_user, attempt_id)


@router.post(
    "/quiz-attempts/{attempt_id}/complete",
    response_model=QuizAttemptResponse,
)
async def complete_quiz(
    attempt_id: UUID,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> QuizAttemptResponse:
    return await QuizService(session).complete(current_user, attempt_id)


@router.get(
    "/quiz-attempts/{attempt_id}/result",
    response_model=QuizAttemptResponse,
)
async def quiz_result(
    attempt_id: UUID,
    session: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
) -> QuizAttemptResponse:
    return await QuizService(session).get_result(current_user, attempt_id)
