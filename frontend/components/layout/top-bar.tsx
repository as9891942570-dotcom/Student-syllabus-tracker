"use client";

import { Coins, Flame, Sparkles } from "lucide-react";

import { AccountMenu } from "@/components/layout/account-menu";
import { ThemeToggle } from "@/components/common/theme-toggle";

export function TopBar({
  title,
  xp = 0,
  level = 1,
  streak = 0,
  coins = 0,
}: {
  title: string;
  xp?: number;
  level?: number;
  streak?: number;
  coins?: number;
}) {
  return (
    <header className="sticky top-0 z-30 flex items-center justify-between gap-3 border-b border-border bg-background/80 px-4 py-3 backdrop-blur md:px-6">
      <div>
        <p className="text-xs font-medium uppercase tracking-wider text-muted-foreground">
          EduQuest
        </p>
        <h1 className="font-display text-lg font-semibold text-foreground md:text-xl">
          {title}
        </h1>
      </div>
      <div className="flex items-center gap-2 md:gap-3">
        <Chip
          icon={<Sparkles className="h-3.5 w-3.5 text-xp" />}
          label={`Lv ${level} · ${xp} XP`}
        />
        <Chip icon={<Flame className="h-3.5 w-3.5 text-streak" />} label={`${streak}`} />
        <Chip icon={<Coins className="h-3.5 w-3.5 text-coin" />} label={`${coins}`} />
        <ThemeToggle />
        <AccountMenu compact />
      </div>
    </header>
  );
}

function Chip({
  icon,
  label,
}: {
  icon: React.ReactNode;
  label: string;
}) {
  return (
    <span className="inline-flex items-center gap-1.5 rounded-full border border-border bg-card px-2.5 py-1 text-xs font-semibold text-foreground">
      {icon}
      {label}
    </span>
  );
}
