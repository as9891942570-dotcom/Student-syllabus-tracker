"use client";

import Link from "next/link";
import { useParams } from "next/navigation";
import { motion } from "framer-motion";
import { Sparkles, Unlock } from "lucide-react";

import { Skeleton } from "@/components/common/skeleton";
import { LevelProgressBar } from "@/features/progression/level-progress-bar";
import {
  getQuizErrorMessage,
  useQuizAttemptQuery,
} from "@/features/quiz/hooks";

export default function QuizResultPage() {
  const params = useParams<{ attemptId: string }>();
  const attemptQuery = useQuizAttemptQuery(params.attemptId);

  if (attemptQuery.isLoading) {
    return (
      <div className="mx-auto flex min-h-screen max-w-lg flex-col justify-center gap-4 px-4">
        <Skeleton className="h-40 w-full" />
      </div>
    );
  }

  if (
    attemptQuery.isError ||
    !attemptQuery.data ||
    attemptQuery.data.status === "active"
  ) {
    return (
      <div className="flex min-h-screen items-center justify-center px-4 text-center">
        <div>
          <h1 className="font-display text-xl font-semibold">No result yet</h1>
          <p className="mt-2 text-sm text-muted-foreground">
            {attemptQuery.isError
              ? getQuizErrorMessage(attemptQuery.error)
              : "Finish the quiz to see your score."}
          </p>
          <Link href="/subjects" className="mt-4 inline-block text-primary">
            Back to subjects
          </Link>
        </div>
      </div>
    );
  }

  const result = attemptQuery.data;

  return (
    <div className="flex min-h-screen items-center justify-center bg-hero-grid px-4 py-10">
      <motion.div
        initial={{ opacity: 0, scale: 0.96 }}
        animate={{ opacity: 1, scale: 1 }}
        className="w-full max-w-md rounded-3xl border border-border bg-card p-6 shadow-glow"
      >
        <div className="text-center">
          <p className="text-xs font-semibold uppercase tracking-[0.2em] text-accent">
            {result.status === "expired" ? "Time up" : "Quiz complete"}
          </p>
          <h1 className="mt-2 font-display text-3xl font-bold">
            {result.quiz_title}
          </h1>
          <p className="mt-1 text-sm text-muted-foreground">
            {result.subject_name} · {result.topic_title}
          </p>
        </div>

        {result.topic_completed ? (
          <motion.p
            initial={{ opacity: 0, y: 6 }}
            animate={{ opacity: 1, y: 0 }}
            className="mt-4 rounded-2xl bg-primary/10 px-3 py-2 text-center text-sm font-semibold text-primary"
          >
            Topic Completed ✓
          </motion.p>
        ) : null}

        <motion.div
          initial={{ scale: 0.8, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ delay: 0.15, type: "spring", stiffness: 160 }}
          className="mt-6 flex flex-col items-center rounded-2xl bg-primary/10 px-4 py-6"
        >
          <Sparkles className="h-8 w-8 text-xp" />
          <p className="mt-2 text-sm font-medium text-muted-foreground">
            {result.xp_awarded === false ? "XP already claimed" : "XP earned"}
          </p>
          <p className="font-display text-5xl font-bold text-xp">
            +{result.xp_earned}
          </p>
          <p className="mt-1 text-xs text-muted-foreground">
            Total XP: {result.total_xp}
          </p>
          <p className="mt-3 text-sm font-medium text-muted-foreground">
            {result.coins_awarded === false && (result.coins_earned ?? 0) === 0
              ? result.topic_completed
                ? "Coins already claimed"
                : "No coins (score below 60%)"
              : "Coins earned"}
          </p>
          <p className="font-display text-3xl font-bold text-coin">
            +{result.coins_earned ?? 0}
          </p>
          <p className="mt-1 text-xs text-muted-foreground">
            Total coins: {result.total_coins ?? 0}
          </p>
        </motion.div>

        {result.next_topic_unlocked && result.next_topic_title ? (
          <p className="mt-4 flex items-center justify-center gap-2 text-sm font-semibold text-accent">
            <Unlock className="h-4 w-4" />
            Next Topic Unlocked: {result.next_topic_title} 🔓
          </p>
        ) : null}

        {typeof result.level === "number" &&
        typeof result.next_level_xp === "number" ? (
          <div className="mt-5">
            <LevelProgressBar
              level={result.level}
              totalXp={result.total_xp}
              nextLevelXp={result.next_level_xp}
              levelFloorXp={result.level_floor_xp ?? 0}
              progressPercentage={result.level_progress_percentage ?? 0}
            />
          </div>
        ) : null}

        <div className="mt-6 grid grid-cols-2 gap-3 text-center">
          <ResultStat label="Score" value={`${result.score}`} />
          <ResultStat label="Percentage" value={`${result.percentage}%`} />
          <ResultStat label="Total" value={`${result.total_questions}`} />
          <ResultStat label="Answered" value={`${result.answered_count}`} />
          <ResultStat label="Correct" value={`${result.correct_count}`} />
          <ResultStat label="Incorrect" value={`${result.incorrect_count}`} />
        </div>

        <div className="mt-8 flex flex-col gap-3">
          {result.next_topic_unlocked ? (
            <Link
              href={`/subjects/${result.subject_id}/chapters/${result.chapter_id}`}
              className="rounded-full bg-primary px-4 py-3 text-center text-sm font-semibold text-primary-foreground"
            >
              Continue to next topic
            </Link>
          ) : (
            <Link
              href={`/quiz/${result.quiz_id}`}
              className="rounded-full bg-primary px-4 py-3 text-center text-sm font-semibold text-primary-foreground"
            >
              Retry Quiz
            </Link>
          )}
          <Link
            href={`/subjects/${result.subject_id}/chapters/${result.chapter_id}`}
            className="rounded-full border border-border px-4 py-3 text-center text-sm font-semibold"
          >
            Back to Topic
          </Link>
          <Link
            href="/quiz/history"
            className="text-center text-sm text-muted-foreground hover:text-foreground"
          >
            View quiz history
          </Link>
        </div>
      </motion.div>
    </div>
  );
}

function ResultStat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-2xl border border-border bg-background px-3 py-3">
      <p className="text-xs text-muted-foreground">{label}</p>
      <p className="font-display text-xl font-bold">{value}</p>
    </div>
  );
}
