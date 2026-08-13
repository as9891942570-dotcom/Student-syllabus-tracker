"use client";

import Link from "next/link";
import { useParams } from "next/navigation";
import { motion } from "framer-motion";
import { Swords } from "lucide-react";

import { Skeleton } from "@/components/common/skeleton";
import {
  getQuizErrorMessage,
  useQuizDetailQuery,
  useStartQuizMutation,
} from "@/features/quiz/hooks";

export default function QuizStartPage() {
  const params = useParams<{ quizId: string }>();
  const quizId = params.quizId;
  const quizQuery = useQuizDetailQuery(quizId);
  const startMutation = useStartQuizMutation();

  if (quizQuery.isLoading) {
    return (
      <div className="mx-auto flex min-h-screen max-w-lg flex-col gap-4 bg-hero-grid px-4 py-10">
        <Skeleton className="h-10 w-48" />
        <Skeleton className="h-64 w-full" />
      </div>
    );
  }

  if (quizQuery.isError || !quizQuery.data) {
    return (
      <div className="flex min-h-screen items-center justify-center px-4 text-center">
        <div>
          <h1 className="font-display text-xl font-semibold">
            Quiz unavailable
          </h1>
          <p className="mt-2 text-sm text-muted-foreground">
            {getQuizErrorMessage(quizQuery.error)}
          </p>
          <Link href="/subjects" className="mt-4 inline-block text-primary">
            Back to subjects
          </Link>
        </div>
      </div>
    );
  }

  const quiz = quizQuery.data;
  if (!quiz.is_active || quiz.question_count === 0) {
    return (
      <div className="flex min-h-screen items-center justify-center px-4 text-center">
        <div>
          <h1 className="font-display text-xl font-semibold">Empty quiz</h1>
          <p className="mt-2 text-sm text-muted-foreground">
            This challenge has no questions yet.
          </p>
          <Link
            href={`/subjects/${quiz.subject_id}/chapters/${quiz.chapter_id}`}
            className="mt-4 inline-block text-primary"
          >
            Back to topic
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-hero-grid px-4 py-10">
      <motion.div
        initial={{ opacity: 0, y: 12 }}
        animate={{ opacity: 1, y: 0 }}
        className="w-full max-w-md rounded-3xl border border-border bg-card p-6 shadow-glow"
      >
        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-accent">
          Quiz challenge
        </p>
        <h1 className="mt-2 font-display text-3xl font-bold">{quiz.title}</h1>
        <p className="mt-3 text-sm text-muted-foreground">
          {quiz.subject_name} · {quiz.chapter_title}
        </p>
        <p className="text-sm font-medium text-foreground">{quiz.topic_title}</p>

        <div className="mt-6 grid grid-cols-2 gap-3 text-center">
          <div className="rounded-2xl bg-primary/10 px-3 py-4">
            <p className="text-xs text-muted-foreground">Questions</p>
            <p className="font-display text-2xl font-bold">{quiz.question_count}</p>
          </div>
          <div className="rounded-2xl bg-primary/10 px-3 py-4">
            <p className="text-xs text-muted-foreground">Time limit</p>
            <p className="font-display text-2xl font-bold">
              {Math.round(quiz.time_limit_seconds / 60)}m
            </p>
          </div>
        </div>

        <button
          type="button"
          disabled={startMutation.isPending}
          onClick={() => startMutation.mutate(quiz.id)}
          className="mt-8 flex w-full items-center justify-center gap-2 rounded-full bg-primary px-4 py-3 text-sm font-semibold text-primary-foreground hover:brightness-110 disabled:opacity-70"
        >
          <Swords className="h-4 w-4" />
          {startMutation.isPending ? "Starting..." : "Start Quiz"}
        </button>

        {startMutation.isError ? (
          <p className="mt-3 text-center text-xs text-destructive">
            {getQuizErrorMessage(startMutation.error)}
          </p>
        ) : null}

        <Link
          href={`/subjects/${quiz.subject_id}/chapters/${quiz.chapter_id}`}
          className="mt-4 block text-center text-sm text-muted-foreground hover:text-foreground"
        >
          Back to topic
        </Link>
      </motion.div>
    </div>
  );
}
