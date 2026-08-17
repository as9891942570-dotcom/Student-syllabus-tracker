"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { Check, Sparkles, Unlock, X } from "lucide-react";

import { LevelProgressBar } from "@/features/progression/level-progress-bar";
import { quizResultFromAttempt } from "@/features/quiz/result-view";
import { cn } from "@/lib/utils";
import type { QuizAttempt } from "@/types/quiz";

export function QuizResultCard({ result }: { result: QuizAttempt }) {
  const { correct, wrong, total, percentage, passed } =
    quizResultFromAttempt(result);
  const nextUnlocked = Boolean(passed && result.next_topic_unlocked);
  const xpLabel = !passed
    ? "No completion XP"
    : result.xp_awarded === false
      ? "XP already claimed"
      : "XP earned";
  const coinsLabel = !passed
    ? "No coins (need 60%)"
    : result.coins_awarded === false || (result.coins_earned ?? 0) === 0
      ? "Coins already claimed"
      : "Coins earned";
  const chapterHref = `/subjects/${result.subject_id}/chapters/${result.chapter_id}`;

  return (
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

      <div className="mt-6 rounded-2xl border border-border bg-background px-4 py-6 text-center">
        <p className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
          Score
        </p>
        <p className="font-display text-5xl font-bold tabular-nums">
          {correct} / {total}
        </p>
        <p className="mt-2 font-display text-3xl font-bold text-primary">
          {percentage}%
        </p>
        <div className="mt-4 flex justify-center gap-6 text-sm font-semibold">
          <span className="inline-flex items-center gap-1 text-emerald-700 dark:text-emerald-300">
            <Check className="h-4 w-4" />
            {correct} Correct
          </span>
          <span className="inline-flex items-center gap-1 text-destructive">
            <X className="h-4 w-4" />
            {wrong} Wrong
          </span>
        </div>
      </div>

      <div
        className={cn(
          "mt-4 rounded-2xl px-3 py-3 text-center text-sm font-semibold",
          passed
            ? "bg-emerald-500/15 text-emerald-800 dark:text-emerald-300"
            : "bg-destructive/15 text-destructive",
        )}
      >
        {passed
          ? nextUnlocked
            ? `PASS — Next topic unlocked${result.next_topic_title ? `: ${result.next_topic_title}` : ""}!`
            : "PASS — Topic completed!"
          : "FAIL — You need at least 60% to unlock the next topic."}
      </div>

      {nextUnlocked && result.next_topic_title ? (
        <p className="mt-3 flex items-center justify-center gap-2 text-sm font-semibold text-accent">
          <Unlock className="h-4 w-4" />
          Next Topic Unlocked: {result.next_topic_title}
        </p>
      ) : null}

      <div className="mt-5 grid grid-cols-2 gap-3 text-center">
        <div className="rounded-2xl bg-primary/10 px-3 py-4">
          <Sparkles className="mx-auto h-4 w-4 text-xp" />
          <p className="mt-1 text-[11px] font-medium text-muted-foreground">
            {xpLabel}
          </p>
          <p className="font-display text-2xl font-bold text-xp">
            +{result.xp_earned}
          </p>
          <p className="text-[11px] text-muted-foreground">
            Total XP: {result.total_xp}
          </p>
        </div>
        <div className="rounded-2xl bg-primary/10 px-3 py-4">
          <p className="text-[11px] font-medium text-muted-foreground">
            {coinsLabel}
          </p>
          <p className="font-display text-2xl font-bold text-coin">
            +{result.coins_earned ?? 0}
          </p>
          <p className="text-[11px] text-muted-foreground">
            Total coins: {result.total_coins ?? 0}
          </p>
        </div>
      </div>

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

      <div className="mt-8 flex flex-col gap-3">
        {passed ? (
          <Link
            href={chapterHref}
            className="rounded-full bg-primary px-4 py-3 text-center text-sm font-semibold text-primary-foreground"
          >
            Continue to Next Topic
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
          href={chapterHref}
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
  );
}
