"use client";

import Link from "next/link";
import { motion } from "framer-motion";

export function LandingHeroMotion() {
  return (
    <section className="grid items-center gap-10 lg:grid-cols-[1.1fr_0.9fr]">
      <motion.div
        initial={{ opacity: 0, y: 16 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.45 }}
      >
        <p className="mb-4 text-sm font-semibold uppercase tracking-[0.2em] text-accent">
          Class 6–12 study tracker
        </p>
        <h1 className="font-display text-4xl font-bold leading-tight tracking-tight text-foreground md:text-6xl">
          Turn your syllabus into a quest.
        </h1>
        <p className="mt-5 max-w-xl text-base text-muted-foreground md:text-lg">
          Track chapters, crush daily goals, earn XP, keep streaks alive, and
          climb the leaderboard — built for students only.
        </p>
        <div className="mt-8 flex flex-wrap gap-3">
          <Link
            href="/register"
            className="rounded-full bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow-glow transition hover:brightness-110"
          >
            Create account
          </Link>
          <Link
            href="/dashboard"
            className="rounded-full border border-border bg-card px-6 py-3 text-sm font-semibold text-foreground transition hover:border-primary/40"
          >
            Preview app shell
          </Link>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, scale: 0.96 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5, delay: 0.1 }}
        className="relative mx-auto w-full max-w-md"
      >
        <div className="absolute -inset-6 rounded-[2rem] bg-primary/10 blur-2xl" />
        <div className="relative overflow-hidden rounded-[1.75rem] border border-border bg-card p-6 shadow-glow">
          <div className="mb-6 flex items-center justify-between">
            <div>
              <p className="text-xs uppercase tracking-wider text-muted-foreground">
                Today
              </p>
              <p className="font-display text-xl font-semibold">Continue Physics</p>
            </div>
            <span className="rounded-full bg-streak/15 px-3 py-1 text-xs font-bold text-streak">
              7 day streak
            </span>
          </div>
          <div className="space-y-4">
            <ProgressRow label="Motion" value={72} />
            <ProgressRow label="Laws of Motion" value={40} />
            <ProgressRow label="Gravitation" value={12} />
          </div>
          <div className="mt-6 grid grid-cols-3 gap-3">
            <Stat label="XP" value="1,240" />
            <Stat label="Level" value="12" />
            <Stat label="Coins" value="380" />
          </div>
        </div>
      </motion.div>
    </section>
  );
}

function ProgressRow({ label, value }: { label: string; value: number }) {
  return (
    <div>
      <div className="mb-1.5 flex items-center justify-between text-sm">
        <span className="font-medium text-foreground">{label}</span>
        <span className="text-muted-foreground">{value}%</span>
      </div>
      <div className="h-2.5 overflow-hidden rounded-full bg-muted">
        <motion.div
          className="h-full rounded-full bg-primary"
          initial={{ width: 0 }}
          animate={{ width: `${value}%` }}
          transition={{ duration: 0.8, delay: 0.2 }}
        />
      </div>
    </div>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl bg-muted/70 px-3 py-3 text-center">
      <p className="text-[11px] uppercase tracking-wide text-muted-foreground">
        {label}
      </p>
      <p className="mt-1 font-display text-lg font-semibold text-foreground">
        {value}
      </p>
    </div>
  );
}
