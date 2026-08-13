"use client";

import Link from "next/link";
import { useParams } from "next/navigation";
import { motion } from "framer-motion";
import { Sparkles } from "lucide-react";

import { Skeleton } from "@/components/common/skeleton";
import { useStudySessionQuery } from "@/features/study/hooks";

export default function StudyResultPage() {
  const params = useParams<{ sessionId: string }>();
  const sessionQuery = useStudySessionQuery(params.sessionId);

  if (sessionQuery.isLoading) {
    return (
      <div className="mx-auto flex min-h-screen max-w-lg flex-col justify-center gap-4 px-4">
        <Skeleton className="h-40 w-full" />
      </div>
    );
  }

  if (!sessionQuery.data || sessionQuery.data.status !== "completed") {
    return (
      <div className="flex min-h-screen items-center justify-center px-4 text-center">
        <div>
          <h1 className="font-display text-xl font-semibold">No result yet</h1>
          <Link href="/subjects" className="mt-4 inline-block text-primary">
            Back to subjects
          </Link>
        </div>
      </div>
    );
  }

  const session = sessionQuery.data;
  const minutes = Math.floor(session.duration_seconds / 60);
  const seconds = session.duration_seconds % 60;

  return (
    <div className="flex min-h-screen items-center justify-center bg-hero-grid px-4 py-10">
      <motion.div
        initial={{ opacity: 0, scale: 0.96 }}
        animate={{ opacity: 1, scale: 1 }}
        className="w-full max-w-md rounded-3xl border border-border bg-card p-6 shadow-glow"
      >
        <div className="text-center">
          <p className="text-xs font-semibold uppercase tracking-[0.2em] text-accent">
            Quest complete
          </p>
          <h1 className="mt-2 font-display text-3xl font-bold">
            {session.topic_title}
          </h1>
          <p className="mt-1 text-sm text-muted-foreground">
            {session.subject_name} · {session.chapter_title}
          </p>
        </div>

        <motion.div
          initial={{ scale: 0.8, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ delay: 0.15, type: "spring", stiffness: 160 }}
          className="mt-8 flex flex-col items-center rounded-2xl bg-primary/10 px-4 py-6"
        >
          <Sparkles className="h-8 w-8 text-xp" />
          <p className="mt-2 text-sm font-medium text-muted-foreground">XP earned</p>
          <p className="font-display text-5xl font-bold text-xp">+{session.xp_earned}</p>
          <p className="mt-1 text-xs text-muted-foreground">
            Total XP: {session.total_xp}
          </p>
        </motion.div>

        <div className="mt-6 grid grid-cols-3 gap-3 text-center">
          <ResultStat label="Score" value={`${session.score}%`} />
          <ResultStat
            label="Time"
            value={`${minutes}:${seconds.toString().padStart(2, "0")}`}
          />
          <ResultStat
            label="Checks"
            value={`${session.correct_count}/${session.correct_count + session.incorrect_count}`}
          />
        </div>

        <div className="mt-8 flex flex-col gap-3">
          <Link
            href="/subjects"
            className="rounded-full bg-primary px-4 py-3 text-center text-sm font-semibold text-primary-foreground"
          >
            Continue questing
          </Link>
          <Link
            href="/syllabus"
            className="rounded-full border border-border px-4 py-3 text-center text-sm font-semibold"
          >
            View syllabus progress
          </Link>
        </div>
      </motion.div>
    </div>
  );
}

function ResultStat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl bg-muted/70 px-2 py-3">
      <p className="text-[10px] uppercase text-muted-foreground">{label}</p>
      <p className="mt-1 font-display text-lg font-semibold">{value}</p>
    </div>
  );
}
