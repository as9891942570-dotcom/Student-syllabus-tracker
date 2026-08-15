"use client";

import { cn } from "@/lib/utils";

export function LevelProgressBar({
  level,
  totalXp,
  nextLevelXp,
  levelFloorXp,
  progressPercentage,
  className,
}: {
  level: number;
  totalXp: number;
  nextLevelXp: number;
  levelFloorXp: number;
  progressPercentage: number;
  className?: string;
}) {
  return (
    <div
      className={cn(
        "rounded-2xl border border-border bg-card px-4 py-3",
        className,
      )}
    >
      <div className="flex items-center justify-between gap-3">
        <p className="font-display text-lg font-bold">Level {level}</p>
        <p className="text-xs font-semibold text-muted-foreground">
          Next: Level {level + 1}
        </p>
      </div>
      <p className="mt-1 text-sm text-muted-foreground">
        {totalXp} XP / {nextLevelXp} XP
      </p>
      <div className="mt-3 h-2.5 overflow-hidden rounded-full bg-muted">
        <div
          className="h-full rounded-full bg-xp transition-all"
          style={{ width: `${Math.min(Math.max(progressPercentage, 0), 100)}%` }}
        />
      </div>
      <p className="mt-1 text-[11px] text-muted-foreground">
        {Math.max(totalXp - levelFloorXp, 0)} into this level
      </p>
    </div>
  );
}
