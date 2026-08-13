"use client";

import Link from "next/link";
import { motion } from "framer-motion";

import { Skeleton } from "@/components/common/skeleton";
import {
  getQuizErrorMessage,
  useQuizHistoryQuery,
} from "@/features/quiz/hooks";

export default function QuizHistoryPage() {
  const historyQuery = useQuizHistoryQuery();

  if (historyQuery.isLoading) {
    return (
      <div className="mx-auto flex min-h-screen max-w-2xl flex-col gap-3 px-4 py-8">
        <Skeleton className="h-10 w-48" />
        <Skeleton className="h-24 w-full" />
        <Skeleton className="h-24 w-full" />
      </div>
    );
  }

  if (historyQuery.isError) {
    return (
      <div className="flex min-h-screen items-center justify-center px-4 text-center">
        <div>
          <h1 className="font-display text-xl font-semibold">
            Could not load history
          </h1>
          <p className="mt-2 text-sm text-muted-foreground">
            {getQuizErrorMessage(historyQuery.error)}
          </p>
        </div>
      </div>
    );
  }

  const items = historyQuery.data ?? [];

  return (
    <div className="min-h-screen bg-hero-grid px-4 py-8 md:px-6">
      <div className="mx-auto w-full max-w-2xl">
        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-accent">
          Battle log
        </p>
        <h1 className="mt-2 font-display text-3xl font-bold">Quiz history</h1>
        <p className="mt-1 text-sm text-muted-foreground">
          Previous quiz attempts and XP earned.
        </p>

        {items.length === 0 ? (
          <div className="mt-10 rounded-3xl border border-dashed border-border px-6 py-12 text-center">
            <p className="font-display text-lg font-semibold">No quizzes yet</p>
            <p className="mt-2 text-sm text-muted-foreground">
              Start a quiz from any topic checklist.
            </p>
            <Link
              href="/subjects"
              className="mt-4 inline-block text-sm font-semibold text-primary"
            >
              Browse subjects
            </Link>
          </div>
        ) : (
          <ul className="mt-8 space-y-3">
            {items.map((item, index) => (
              <motion.li
                key={item.id}
                initial={{ opacity: 0, y: 8 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.04 }}
                className="rounded-2xl border border-border bg-card px-4 py-4"
              >
                <div className="flex flex-wrap items-start justify-between gap-2">
                  <div>
                    <p className="font-display text-lg font-semibold">
                      {item.quiz_title}
                    </p>
                    <p className="text-sm text-muted-foreground">
                      {item.topic_title}
                    </p>
                  </div>
                  <span className="rounded-full bg-primary/15 px-2.5 py-1 text-xs font-semibold text-primary">
                    {item.completed ? item.status : "in progress"}
                  </span>
                </div>
                <div className="mt-3 flex flex-wrap gap-4 text-sm">
                  <span>
                    Score <strong>{item.score}</strong>
                  </span>
                  <span>
                    <strong>{item.percentage}%</strong>
                  </span>
                  <span className="text-xp">
                    +{item.xp_earned} XP
                  </span>
                  <span className="text-muted-foreground">
                    {new Date(item.started_at).toLocaleString()}
                  </span>
                </div>
                {item.completed ? (
                  <Link
                    href={`/quiz/attempt/${item.id}/result`}
                    className="mt-3 inline-block text-sm font-semibold text-primary"
                  >
                    View result
                  </Link>
                ) : null}
              </motion.li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
