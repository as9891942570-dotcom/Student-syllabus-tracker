"use client";

import Link from "next/link";
import { useParams } from "next/navigation";
import { motion } from "framer-motion";
import { Check, X } from "lucide-react";

import { Skeleton } from "@/components/common/skeleton";
import {
  getStudyErrorMessage,
  useCompleteSessionMutation,
  useRecordActivityMutation,
  useStudySessionQuery,
} from "@/features/study/hooks";
import { useSessionTimer } from "@/features/study/use-session-timer";

export default function StudySessionPage() {
  const params = useParams<{ sessionId: string }>();
  const sessionId = params.sessionId;
  const sessionQuery = useStudySessionQuery(sessionId);
  const activityMutation = useRecordActivityMutation(sessionId);
  const completeMutation = useCompleteSessionMutation(sessionId);
  const timer = useSessionTimer(
    sessionQuery.data?.status === "active"
      ? sessionQuery.data.started_at
      : undefined,
  );

  if (sessionQuery.isLoading) {
    return (
      <div className="mx-auto flex min-h-screen max-w-lg flex-col gap-4 bg-hero-grid px-4 py-8">
        <Skeleton className="h-10 w-40" />
        <Skeleton className="h-64 w-full" />
      </div>
    );
  }

  if (sessionQuery.isError || !sessionQuery.data) {
    return (
      <div className="flex min-h-screen items-center justify-center px-4 text-center">
        <div>
          <h1 className="font-display text-xl font-semibold">Session not found</h1>
          <Link href="/subjects" className="mt-4 inline-block text-primary">
            Back to subjects
          </Link>
        </div>
      </div>
    );
  }

  const session = sessionQuery.data;
  if (session.status === "completed") {
    return (
      <div className="flex min-h-screen items-center justify-center px-4 text-center">
        <div>
          <h1 className="font-display text-xl font-semibold">Session complete</h1>
          <Link
            href={`/study/${sessionId}/result`}
            className="mt-4 inline-block rounded-full bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground"
          >
            View results
          </Link>
        </div>
      </div>
    );
  }

  const totalActs = session.correct_count + session.incorrect_count;

  return (
    <div className="min-h-screen bg-hero-grid px-4 py-6 md:px-6">
      <div className="mx-auto flex w-full max-w-lg flex-col gap-5">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-xs font-semibold uppercase tracking-wider text-accent">
              Quest in progress
            </p>
            <h1 className="font-display text-2xl font-bold">{session.topic_title}</h1>
            <p className="text-sm text-muted-foreground">
              {session.subject_name} · {session.chapter_title}
            </p>
          </div>
          <div className="rounded-2xl border border-border bg-card px-4 py-3 text-center shadow-glow">
            <p className="text-[10px] uppercase text-muted-foreground">Timer</p>
            <p className="font-display text-2xl font-bold tabular-nums text-primary">
              {timer.label}
            </p>
          </div>
        </div>

        <div className="grid grid-cols-3 gap-3">
          <Stat label="Score" value={`${session.score}%`} />
          <Stat label="Correct" value={String(session.correct_count)} accent />
          <Stat label="Missed" value={String(session.incorrect_count)} />
        </div>

        <div className="rounded-2xl border border-border bg-card p-5 shadow-glow">
          <p className="text-sm text-muted-foreground">
            Mark each check as a win or review. This powers your session score and XP —
            no lectures, just progress.
          </p>
          <div className="mt-5 grid grid-cols-2 gap-3">
            <button
              type="button"
              disabled={activityMutation.isPending}
              onClick={() => activityMutation.mutate("correct")}
              className="flex flex-col items-center gap-2 rounded-2xl bg-primary px-4 py-6 text-primary-foreground transition hover:brightness-110 disabled:opacity-70"
            >
              <Check className="h-7 w-7" />
              <span className="text-sm font-semibold">Got it</span>
            </button>
            <button
              type="button"
              disabled={activityMutation.isPending}
              onClick={() => activityMutation.mutate("incorrect")}
              className="flex flex-col items-center gap-2 rounded-2xl border border-border bg-muted px-4 py-6 transition hover:border-destructive/40 disabled:opacity-70"
            >
              <X className="h-7 w-7 text-destructive" />
              <span className="text-sm font-semibold">Need review</span>
            </button>
          </div>
          <p className="mt-4 text-center text-xs text-muted-foreground">
            {totalActs} checks logged this session
          </p>
        </div>

        {(activityMutation.isError || completeMutation.isError) && (
          <p className="rounded-xl border border-destructive/30 bg-destructive/10 px-3 py-2 text-sm text-destructive">
            {getStudyErrorMessage(
              activityMutation.error ?? completeMutation.error,
            )}
          </p>
        )}

        <button
          type="button"
          disabled={completeMutation.isPending}
          onClick={() => completeMutation.mutate()}
          className="h-12 rounded-full bg-foreground text-sm font-semibold text-background transition hover:opacity-90 disabled:opacity-70"
        >
          {completeMutation.isPending ? "Finishing quest..." : "Complete Session"}
        </button>
      </div>
    </div>
  );
}

function Stat({
  label,
  value,
  accent,
}: {
  label: string;
  value: string;
  accent?: boolean;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      className="rounded-2xl border border-border bg-card px-3 py-3 text-center"
    >
      <p className="text-[10px] uppercase tracking-wide text-muted-foreground">
        {label}
      </p>
      <p
        className={`mt-1 font-display text-xl font-bold ${accent ? "text-primary" : ""}`}
      >
        {value}
      </p>
    </motion.div>
  );
}
