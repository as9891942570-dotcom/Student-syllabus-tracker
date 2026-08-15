"""Quiz system business logic (Phase 6)."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import ConflictError, ForbiddenError, NotFoundError, ValidationAppError
from app.models.quiz import Quiz
from app.models.quiz_answer import QuizAnswer
from app.models.quiz_attempt import QuizAttempt
from app.models.user import User
from app.repositories.profile import StudentProfileRepository
from app.repositories.quiz import (
    QuizAnswerRepository,
    QuizAttemptRepository,
    QuizRepository,
)
from app.repositories.syllabus import TopicProgressRepository, TopicRepository
from app.schemas.quiz import (
    QuizAttemptResponse,
    QuizDetail,
    QuizHistoryItem,
    QuizOptionPublic,
    QuizQuestionPublic,
    QuizSummary,
    SubmitAnswerRequest,
    SubmitAnswerResponse,
)
from app.schemas.syllabus import TopicProgressUpdate
from app.services.academic_seed import seed_academic_lookups
from app.services.coins import award_coins, coin_reward_per_topic
from app.services.level import calculate_level_progress
from app.services.quiz_seed import ensure_quiz_for_topic, ensure_quiz_has_questions
from app.services.syllabus import SyllabusService
from app.services.syllabus_seed import seed_syllabus_for_scope
from app.services.xp import award_xp

# Topic is marked complete when quiz percentage reaches this threshold.
TOPIC_COMPLETE_PERCENTAGE = 60


def calculate_quiz_percentage(*, correct: int, total: int) -> int:
    if total <= 0:
        return 0
    return int(round((correct / total) * 100))


def calculate_quiz_score(*, correct: int, total: int) -> int:
    """Score equals percentage for quizzes (0–100)."""
    return calculate_quiz_percentage(correct=correct, total=total)


def calculate_quiz_xp(*, percentage: int, correct_count: int) -> int:
    """
    Quiz XP (simple, documented):
    - base 20 for completing a quiz
    - up to 30 from percentage (percentage/100 * 30)
    - +2 per correct answer (max 20)
    - +15 perfect score bonus when percentage == 100
    """
    base = 20
    percentage_bonus = int((max(0, min(percentage, 100)) / 100) * 30)
    correct_bonus = min(max(correct_count, 0), 20) * 2
    perfect_bonus = 15 if percentage == 100 else 0
    return base + percentage_bonus + correct_bonus + perfect_bonus


class QuizService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.quizzes = QuizRepository(session)
        self.attempts = QuizAttemptRepository(session)
        self.answers = QuizAnswerRepository(session)
        self.topics = TopicRepository(session)
        self.progress = TopicProgressRepository(session)
        self.profiles = StudentProfileRepository(session)
        self.syllabus = SyllabusService(session)

    async def _prepare_scope(self, user: User):
        profile = await self.syllabus._require_profile(user)
        await seed_academic_lookups(self.session)
        await seed_syllabus_for_scope(
            self.session,
            board_id=profile.board_id,  # type: ignore[arg-type]
            class_id=profile.class_id,  # type: ignore[arg-type]
            stream_id=profile.stream_id,
            stream_code=profile.stream.code if profile.stream else None,
            grade=profile.school_class.grade,  # type: ignore[union-attr]
        )
        return profile

    async def list_for_topic(self, user: User, topic_id: UUID) -> list[QuizSummary]:
        profile = await self._prepare_scope(user)
        topic = await self.topics.get_with_chapter(topic_id)
        if topic is None:
            raise NotFoundError("Topic not found")
        self.syllabus._assert_subject_in_scope(profile, topic.chapter.subject)

        await ensure_quiz_for_topic(self.session, topic.id, topic.title)
        quizzes = await self.quizzes.list_for_topic(topic_id)
        populated = [q for q in quizzes if q.is_active and q.questions]
        return [
            QuizSummary(
                id=q.id,
                topic_id=q.topic_id,
                title=q.title,
                time_limit_seconds=q.time_limit_seconds,
                question_count=len(q.questions),
                is_active=q.is_active,
            )
            for q in populated
        ]

    async def get_quiz(self, user: User, quiz_id: UUID) -> QuizDetail:
        profile = await self._prepare_scope(user)
        quiz = await self.quizzes.get_with_questions(quiz_id)
        if quiz is None or not quiz.is_active:
            raise NotFoundError("Quiz not found")
        self.syllabus._assert_subject_in_scope(profile, quiz.topic.chapter.subject)
        quiz = await ensure_quiz_has_questions(self.session, quiz)
        return self._quiz_detail(quiz)

    async def start(self, user: User, quiz_id: UUID) -> QuizAttemptResponse:
        profile = await self._prepare_scope(user)
        quiz = await self.quizzes.get_with_questions(quiz_id)
        if quiz is None or not quiz.is_active:
            raise NotFoundError("Quiz not found")
        self.syllabus._assert_subject_in_scope(profile, quiz.topic.chapter.subject)
        quiz = await ensure_quiz_has_questions(self.session, quiz)
        await self.syllabus.assert_topic_unlocked(user, quiz.topic_id)

        if not quiz.questions:
            raise ValidationAppError("Quiz has no questions")
        for question in quiz.questions:
            if len(question.options) < 2:
                raise ValidationAppError("Each question must have multiple options")
            correct = [o for o in question.options if o.is_correct]
            if len(correct) != 1:
                raise ValidationAppError("Each question must have exactly one correct option")

        active = await self.attempts.get_active_for_user(user.id)
        if active is not None:
            active = await self._expire_if_needed(active, user)
            if active.status == "active":
                raise ConflictError(
                    "You already have an active quiz attempt. Complete or wait for it to expire.",
                )

        now = datetime.now(timezone.utc)
        attempt = QuizAttempt(
            user_id=user.id,
            quiz_id=quiz.id,
            status="active",
            current_question_index=0,
            total_questions=len(quiz.questions),
            expires_at=now + timedelta(seconds=quiz.time_limit_seconds),
            started_at=now,
        )
        await self.attempts.create(attempt)
        loaded = await self.attempts.get_for_user(attempt.id, user.id)
        assert loaded is not None
        return await self._attempt_response(loaded, user)

    async def get_active(self, user: User) -> QuizAttemptResponse | None:
        attempt = await self.attempts.get_active_for_user(user.id)
        if attempt is None:
            return None
        attempt = await self._expire_if_needed(attempt, user)
        if attempt.status != "active":
            return None
        return await self._attempt_response(attempt, user)

    async def get_attempt(self, user: User, attempt_id: UUID) -> QuizAttemptResponse:
        attempt = await self._get_owned_attempt(user, attempt_id)
        attempt = await self._expire_if_needed(attempt, user)
        return await self._attempt_response(attempt, user)

    async def current_question(self, user: User, attempt_id: UUID) -> QuizQuestionPublic:
        attempt = await self._get_owned_attempt(user, attempt_id)
        attempt = await self._expire_if_needed(attempt, user)
        if attempt.status != "active":
            raise ConflictError("Quiz attempt is no longer active")

        questions = sorted(attempt.quiz.questions, key=lambda q: q.sort_order)
        if not questions:
            raise ValidationAppError("Quiz has no questions")
        index = min(max(attempt.current_question_index, 0), len(questions) - 1)
        question = questions[index]
        prior = await self.answers.get_for_attempt_question(attempt.id, question.id)
        correct_option_id = None
        if prior is not None:
            correct = next((o for o in question.options if o.is_correct), None)
            correct_option_id = correct.id if correct else None
        return QuizQuestionPublic(
            id=question.id,
            prompt=question.prompt,
            sort_order=question.sort_order,
            question_number=index + 1,
            total_questions=len(questions),
            options=[
                QuizOptionPublic(id=o.id, text=o.text, sort_order=o.sort_order)
                for o in sorted(question.options, key=lambda x: x.sort_order)
            ],
            already_answered=prior is not None,
            selected_option_id=prior.selected_option_id if prior else None,
            correct_option_id=correct_option_id,
        )

    async def submit_answer(
        self,
        user: User,
        attempt_id: UUID,
        payload: SubmitAnswerRequest,
    ) -> SubmitAnswerResponse:
        attempt = await self._get_owned_attempt(user, attempt_id)
        attempt = await self._expire_if_needed(attempt, user)
        if attempt.status != "active":
            raise ConflictError("Cannot modify a completed or expired quiz attempt")

        questions = sorted(attempt.quiz.questions, key=lambda q: q.sort_order)
        index = attempt.current_question_index
        if index < 0 or index >= len(questions):
            raise ValidationAppError("No current question available")
        question = questions[index]

        option = next((o for o in question.options if o.id == payload.option_id), None)
        if option is None:
            raise ValidationAppError("Invalid option for this question")

        existing = await self.answers.get_for_attempt_question(attempt.id, question.id)
        if existing is not None:
            raise ConflictError("This question was already answered")

        is_correct = bool(option.is_correct)
        correct_option = next(o for o in question.options if o.is_correct)
        answer = QuizAnswer(
            attempt_id=attempt.id,
            question_id=question.id,
            selected_option_id=option.id,
            is_correct=is_correct,
        )
        await self.answers.create(answer)

        attempt.answered_count += 1
        if is_correct:
            attempt.correct_count += 1
        else:
            attempt.incorrect_count += 1
        await self.attempts.update(attempt)

        return SubmitAnswerResponse(
            question_id=question.id,
            selected_option_id=option.id,
            is_correct=is_correct,
            correct_option_id=correct_option.id,
            attempt_id=attempt.id,
            answered_count=attempt.answered_count,
            correct_count=attempt.correct_count,
            incorrect_count=attempt.incorrect_count,
        )

    async def next_question(self, user: User, attempt_id: UUID) -> QuizAttemptResponse:
        attempt = await self._get_owned_attempt(user, attempt_id)
        attempt = await self._expire_if_needed(attempt, user)
        if attempt.status != "active":
            raise ConflictError("Cannot modify a completed or expired quiz attempt")

        questions = sorted(attempt.quiz.questions, key=lambda q: q.sort_order)
        current = questions[attempt.current_question_index]
        answered = await self.answers.get_for_attempt_question(attempt.id, current.id)
        if answered is None:
            raise ValidationAppError("Answer the current question before moving on")

        if attempt.current_question_index >= len(questions) - 1:
            raise ValidationAppError("Already on the final question. Complete the quiz.")

        attempt.current_question_index += 1
        await self.attempts.update(attempt)
        loaded = await self.attempts.get_for_user(attempt.id, user.id)
        assert loaded is not None
        return await self._attempt_response(loaded, user)

    async def complete(self, user: User, attempt_id: UUID) -> QuizAttemptResponse:
        attempt = await self._get_owned_attempt(user, attempt_id)
        if attempt.status in {"completed", "expired"}:
            return await self._attempt_response(attempt, user)
        return await self._finalize(attempt, user, status="completed")

    async def get_result(self, user: User, attempt_id: UUID) -> QuizAttemptResponse:
        attempt = await self._get_owned_attempt(user, attempt_id)
        attempt = await self._expire_if_needed(attempt, user)
        if attempt.status == "active":
            raise ConflictError("Quiz is still in progress")
        return await self._attempt_response(attempt, user)

    async def history(self, user: User) -> list[QuizHistoryItem]:
        rows = await self.attempts.list_history(user.id)
        return [
            QuizHistoryItem(
                id=a.id,
                quiz_id=a.quiz_id,
                quiz_title=a.quiz.title,
                topic_id=a.quiz.topic_id,
                topic_title=a.quiz.topic.title,
                status=a.status,
                score=a.score,
                percentage=a.percentage,
                xp_earned=a.xp_earned,
                total_questions=a.total_questions,
                correct_count=a.correct_count,
                started_at=a.started_at,
                ended_at=a.ended_at,
                completed=a.status in {"completed", "expired"},
            )
            for a in rows
        ]

    async def _get_owned_attempt(self, user: User, attempt_id: UUID) -> QuizAttempt:
        attempt = await self.attempts.get_for_user(attempt_id, user.id)
        if attempt is None:
            # Distinguish missing vs other user's attempt for security tests.
            other = await self.session.get(QuizAttempt, attempt_id)
            if other is not None:
                raise ForbiddenError("Not allowed to access this quiz attempt")
            raise NotFoundError("Quiz attempt not found")
        return attempt

    async def _expire_if_needed(self, attempt: QuizAttempt, user: User) -> QuizAttempt:
        if attempt.status != "active":
            return attempt
        now = datetime.now(timezone.utc)
        expires = attempt.expires_at
        if expires.tzinfo is None:
            expires = expires.replace(tzinfo=timezone.utc)
        if now >= expires:
            return await self._finalize(attempt, user, status="expired")
        return attempt

    async def _finalize(
        self,
        attempt: QuizAttempt,
        user: User,
        *,
        status: str,
    ) -> QuizAttemptResponse:
        # Reload with relations if needed
        loaded = await self.attempts.get_for_user(attempt.id, user.id)
        assert loaded is not None
        attempt = loaded
        topic_id = attempt.quiz.topic_id

        if attempt.status in {"completed", "expired"}:
            return await self._attempt_response(attempt, user)

        ended_at = datetime.now(timezone.utc)
        total = attempt.total_questions or len(attempt.quiz.questions)
        percentage = calculate_quiz_percentage(
            correct=attempt.correct_count,
            total=total,
        )
        score = calculate_quiz_score(correct=attempt.correct_count, total=total)
        passed = percentage >= TOPIC_COMPLETE_PERCENTAGE
        xp = calculate_quiz_xp(percentage=percentage, correct_count=attempt.correct_count)

        prior_progress = await self.progress.get_for_user_topic(user.id, topic_id)
        already_topic_completed = bool(prior_progress and prior_progress.is_completed)
        already_awarded = await self.attempts.has_prior_xp_for_quiz(
            user.id,
            attempt.quiz_id,
            exclude_attempt_id=attempt.id,
        )
        first_success = passed and not already_topic_completed and not already_awarded
        if not first_success:
            xp = 0
        xp_awarded = first_success and xp > 0

        attempt.status = status
        attempt.ended_at = ended_at
        attempt.score = score
        attempt.percentage = percentage
        attempt.xp_earned = xp
        await self.attempts.update(attempt)

        started = attempt.started_at
        if started.tzinfo is None:
            started = started.replace(tzinfo=timezone.utc)
        duration = max(int((ended_at - started).total_seconds()), 0)

        if xp_awarded:
            await award_xp(
                self.session,
                user_id=user.id,
                xp_amount=xp,
                study_seconds=duration,
                count_as_session=False,
            )

        topic_completed = passed
        next_topic_unlocked = False
        next_topic_id = None
        next_topic_title = None
        coins = 0
        coins_awarded = False

        if topic_completed:
            # Coins only on the first successful topic completion (>=60%).
            if not already_topic_completed:
                coins = coin_reward_per_topic()
                if coins > 0:
                    await award_coins(self.session, user_id=user.id, coins_amount=coins)
                    coins_awarded = True
            attempt.coins_earned = coins
            await self.attempts.update(attempt)

            await self.syllabus.set_topic_progress(
                user,
                topic_id,
                TopicProgressUpdate(is_completed=True),
                enforce_unlock=False,
            )
            nxt = await self.syllabus.get_next_topic_after(user, topic_id)
            if nxt is not None:
                next_topic_id = nxt.id
                next_topic_title = nxt.title
                next_topic_unlocked = not nxt.is_locked
        else:
            attempt.coins_earned = 0
            await self.attempts.update(attempt)

        refreshed = await self.attempts.get_for_user(attempt.id, user.id)
        assert refreshed is not None
        return await self._attempt_response(
            refreshed,
            user,
            topic_completed=topic_completed,
            next_topic_unlocked=next_topic_unlocked,
            next_topic_id=next_topic_id,
            next_topic_title=next_topic_title,
            xp_awarded=xp_awarded,
            coins_awarded=coins_awarded,
        )

    def _quiz_detail(self, quiz: Quiz) -> QuizDetail:
        topic = quiz.topic
        chapter = topic.chapter
        subject = chapter.subject
        return QuizDetail(
            id=quiz.id,
            topic_id=topic.id,
            topic_title=topic.title,
            chapter_id=chapter.id,
            chapter_title=chapter.title,
            subject_id=subject.id,
            subject_name=subject.name,
            title=quiz.title,
            time_limit_seconds=quiz.time_limit_seconds,
            question_count=len(quiz.questions),
            is_active=quiz.is_active,
        )

    async def _attempt_response(
        self,
        attempt: QuizAttempt,
        user: User,
        *,
        topic_completed: bool | None = None,
        next_topic_unlocked: bool = False,
        next_topic_id=None,
        next_topic_title: str | None = None,
        xp_awarded: bool = True,
        coins_awarded: bool = False,
    ) -> QuizAttemptResponse:
        profile = await self.profiles.get_by_user_id(user.id)
        total_xp = profile.total_xp if profile else 0
        total_coins = profile.total_coins if profile else 0
        level = calculate_level_progress(total_xp)
        quiz = attempt.quiz
        topic = quiz.topic
        chapter = topic.chapter
        subject = chapter.subject

        if topic_completed is None:
            row = await self.progress.get_for_user_topic(user.id, topic.id)
            topic_completed = bool(row and row.is_completed)

        if (
            attempt.status in {"completed", "expired"}
            and topic_completed
            and next_topic_id is None
        ):
            nxt = await self.syllabus.get_next_topic_after(user, topic.id)
            if nxt is not None:
                next_topic_id = nxt.id
                next_topic_title = nxt.title
                next_topic_unlocked = not nxt.is_locked

        now = datetime.now(timezone.utc)
        expires = attempt.expires_at
        if expires.tzinfo is None:
            expires = expires.replace(tzinfo=timezone.utc)
        remaining = max(int((expires - now).total_seconds()), 0) if attempt.status == "active" else 0

        return QuizAttemptResponse(
            id=attempt.id,
            quiz_id=quiz.id,
            quiz_title=quiz.title,
            topic_id=topic.id,
            topic_title=topic.title,
            chapter_id=chapter.id,
            chapter_title=chapter.title,
            subject_id=subject.id,
            subject_name=subject.name,
            status=attempt.status,
            current_question_index=attempt.current_question_index,
            total_questions=attempt.total_questions,
            answered_count=attempt.answered_count,
            correct_count=attempt.correct_count,
            incorrect_count=attempt.incorrect_count,
            score=attempt.score,
            percentage=attempt.percentage,
            xp_earned=attempt.xp_earned,
            total_xp=total_xp,
            coins_earned=attempt.coins_earned or 0,
            total_coins=total_coins or 0,
            topic_completed=bool(topic_completed),
            next_topic_unlocked=next_topic_unlocked,
            next_topic_id=next_topic_id,
            next_topic_title=next_topic_title,
            xp_awarded=xp_awarded if attempt.status != "active" else False,
            coins_awarded=(
                (coins_awarded or (attempt.coins_earned or 0) > 0)
                if attempt.status != "active"
                else False
            ),
            level=level.level,
            level_floor_xp=level.level_floor_xp,
            next_level_xp=level.next_level_xp,
            level_progress_percentage=level.level_progress_percentage,
            started_at=attempt.started_at,
            expires_at=attempt.expires_at,
            ended_at=attempt.ended_at,
            seconds_remaining=remaining,
        )
