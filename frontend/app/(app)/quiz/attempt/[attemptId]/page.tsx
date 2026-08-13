"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import Link from "next/link";
import { useParams } from "next/navigation";
import { motion } from "framer-motion";

import { Skeleton } from "@/components/common/skeleton";
import {
  getQuizErrorMessage,
  useCompleteQuizMutation,
  useCurrentQuestionQuery,
  useNextQuestionMutation,
  useQuizAttemptQuery,
  useSubmitAnswerMutation,
} from "@/features/quiz/hooks";
import {
  formatCountdown,
  useQuizCountdown,
  useQuizExpiryComplete,
} from "@/features/quiz/use-quiz-countdown";
import { cn } from "@/lib/utils";

export default function QuizAttemptPage() {
  const params = useParams<{ attemptId: string }>();
  const attemptId = params.attemptId;
  const attemptQuery = useQuizAttemptQuery(attemptId);
  const isActive = attemptQuery.data?.status === "active";
  const questionQuery = useCurrentQuestionQuery(attemptId, isActive);
  const submitMutation = useSubmitAnswerMutation(attemptId);
  const nextMutation = useNextQuestionMutation(attemptId);
  const completeMutation = useCompleteQuizMutation(attemptId);
  const completeMutationRef = useRef(completeMutation);
  completeMutationRef.current = completeMutation;
  const [selectedOptionId, setSelectedOptionId] = useState<string | null>(null);
  const [answeredCorrect, setAnsweredCorrect] = useState<boolean | null>(null);

  const secondsRemaining = useQuizCountdown(
    attemptQuery.data?.expires_at,
    isActive,
  );

  const handleExpire = useCallback(() => {
    const mutation = completeMutationRef.current;
    if (mutation.isPending) return;
    mutation.mutate();
  }, []);

  useQuizExpiryComplete(secondsRemaining, isActive, handleExpire);

  useEffect(() => {
    if (questionQuery.data?.selected_option_id) {
      setSelectedOptionId(questionQuery.data.selected_option_id);
    } else {
      setSelectedOptionId(null);
      setAnsweredCorrect(null);
    }
  }, [questionQuery.data?.id, questionQuery.data?.selected_option_id]);

  if (attemptQuery.isLoading) {
    return (
      <div className="mx-auto flex min-h-screen max-w-lg flex-col gap-4 bg-hero-grid px-4 py-8">
        <Skeleton className="h-10 w-40" />
        <Skeleton className="h-64 w-full" />
      </div>
    );
  }

  if (attemptQuery.isError || !attemptQuery.data) {
    return (
      <div className="flex min-h-screen items-center justify-center px-4 text-center">
        <div>
          <h1 className="font-display text-xl font-semibold">
            Quiz attempt not found
          </h1>
          <p className="mt-2 text-sm text-muted-foreground">
            {getQuizErrorMessage(attemptQuery.error)}
          </p>
          <Link href="/subjects" className="mt-4 inline-block text-primary">
            Back to subjects
          </Link>
        </div>
      </div>
    );
  }

  const attempt = attemptQuery.data;

  if (attempt.status === "completed" || attempt.status === "expired") {
    return (
      <div className="flex min-h-screen items-center justify-center px-4 text-center">
        <div>
          <h1 className="font-display text-xl font-semibold">
            {attempt.status === "expired" ? "Time expired" : "Quiz complete"}
          </h1>
          <Link
            href={`/quiz/attempt/${attemptId}/result`}
            className="mt-4 inline-block rounded-full bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground"
          >
            View results
          </Link>
        </div>
      </div>
    );
  }

  if (questionQuery.isLoading || !questionQuery.data) {
    return (
      <div className="mx-auto flex min-h-screen max-w-lg flex-col gap-4 bg-hero-grid px-4 py-8">
        <Skeleton className="h-10 w-40" />
        <Skeleton className="h-64 w-full" />
      </div>
    );
  }

  if (questionQuery.isError) {
    return (
      <div className="flex min-h-screen items-center justify-center px-4 text-center">
        <div>
          <h1 className="font-display text-xl font-semibold">
            Could not load question
          </h1>
          <p className="mt-2 text-sm text-muted-foreground">
            {getQuizErrorMessage(questionQuery.error)}
          </p>
          <button
            type="button"
            onClick={() => completeMutation.mutate()}
            className="mt-4 rounded-full bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground"
          >
            Finish quiz
          </button>
        </div>
      </div>
    );
  }

  const question = questionQuery.data;
  const progress = (question.question_number / question.total_questions) * 100;
  const isLast = question.question_number >= question.total_questions;
  const alreadyAnswered =
    question.already_answered || answeredCorrect !== null;

  return (
    <div className="min-h-screen bg-hero-grid px-4 py-6 md:px-6">
      <div className="mx-auto flex w-full max-w-lg flex-col gap-5">
        <div className="flex items-start justify-between gap-3">
          <div>
            <p className="text-xs font-semibold uppercase tracking-wider text-accent">
              Quiz battle
            </p>
            <h1 className="font-display text-2xl font-bold">
              {attempt.quiz_title}
            </h1>
            <p className="text-sm text-muted-foreground">
              {attempt.subject_name} · {attempt.topic_title}
            </p>
          </div>
          <div
            className={cn(
              "rounded-full px-3 py-1.5 text-sm font-semibold tabular-nums",
              secondsRemaining !== null && secondsRemaining <= 30
                ? "bg-destructive/15 text-destructive"
                : "bg-primary/15 text-primary",
            )}
          >
            {formatCountdown(secondsRemaining)}
          </div>
        </div>

        <div>
          <div className="mb-1 flex justify-between text-xs text-muted-foreground">
            <span>
              Question {question.question_number} / {question.total_questions}
            </span>
            <span>{Math.round(progress)}%</span>
          </div>
          <div className="h-2 overflow-hidden rounded-full bg-muted">
            <motion.div
              className="h-full bg-primary"
              initial={false}
              animate={{ width: `${progress}%` }}
              transition={{ type: "spring", stiffness: 120, damping: 20 }}
            />
          </div>
        </div>

        <motion.div
          key={question.id}
          initial={{ opacity: 0, x: 16 }}
          animate={{ opacity: 1, x: 0 }}
          className="rounded-3xl border border-border bg-card p-5"
        >
          <p className="font-display text-lg font-semibold leading-snug">
            {question.prompt}
          </p>

          <ul className="mt-5 space-y-2">
            {question.options.map((option) => {
              const selected = selectedOptionId === option.id;
              return (
                <li key={option.id}>
                  <button
                    type="button"
                    disabled={alreadyAnswered || submitMutation.isPending}
                    onClick={() => setSelectedOptionId(option.id)}
                    className={cn(
                      "w-full rounded-2xl border px-4 py-3 text-left text-sm transition",
                      selected
                        ? "border-primary bg-primary/15 font-medium"
                        : "border-border bg-background hover:border-primary/40",
                      alreadyAnswered && !selected && "opacity-60",
                    )}
                  >
                    {option.text}
                  </button>
                </li>
              );
            })}
          </ul>

          {answeredCorrect !== null ? (
            <p
              className={cn(
                "mt-4 text-sm font-medium",
                answeredCorrect ? "text-primary" : "text-destructive",
              )}
            >
              {answeredCorrect ? "Correct!" : "Not quite — keep going."}
            </p>
          ) : null}
        </motion.div>

        <div className="flex flex-col gap-2">
          {!alreadyAnswered ? (
            <button
              type="button"
              disabled={!selectedOptionId || submitMutation.isPending}
              onClick={async () => {
                if (!selectedOptionId) return;
                const res = await submitMutation.mutateAsync(selectedOptionId);
                setAnsweredCorrect(res.is_correct);
              }}
              className="rounded-full bg-primary px-4 py-3 text-sm font-semibold text-primary-foreground disabled:opacity-60"
            >
              {submitMutation.isPending ? "Checking..." : "Submit answer"}
            </button>
          ) : isLast ? (
            <button
              type="button"
              disabled={completeMutation.isPending}
              onClick={() => completeMutation.mutate()}
              className="rounded-full bg-primary px-4 py-3 text-sm font-semibold text-primary-foreground"
            >
              {completeMutation.isPending ? "Finishing..." : "Finish quiz"}
            </button>
          ) : (
            <button
              type="button"
              disabled={nextMutation.isPending}
              onClick={() => nextMutation.mutate()}
              className="rounded-full bg-primary px-4 py-3 text-sm font-semibold text-primary-foreground"
            >
              {nextMutation.isPending ? "Loading..." : "Next question"}
            </button>
          )}

          {(submitMutation.isError ||
            nextMutation.isError ||
            completeMutation.isError) && (
            <p className="text-center text-xs text-destructive">
              {getQuizErrorMessage(
                submitMutation.error ||
                  nextMutation.error ||
                  completeMutation.error,
              )}
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
