import Link from "next/link";

import { ThemeToggle } from "@/components/common/theme-toggle";
import { ApiHealthBadge } from "@/features/health/api-health-badge";
import { LandingHeroMotion } from "@/features/marketing/landing-hero-motion";

export default function LandingPage() {
  return (
    <div className="relative min-h-screen overflow-hidden bg-hero-grid">
      <header className="mx-auto flex w-full max-w-6xl items-center justify-between px-4 py-5 md:px-6">
        <span className="font-display text-2xl font-bold tracking-tight text-primary md:text-3xl">
          EduQuest
        </span>
        <div className="flex items-center gap-2 md:gap-3">
          <ThemeToggle />
          <Link
            href="/login"
            className="rounded-full px-3 py-2 text-sm font-semibold text-foreground hover:text-primary"
          >
            Log in
          </Link>
          <Link
            href="/register"
            className="rounded-full bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground shadow-glow transition hover:brightness-110"
          >
            Start free
          </Link>
        </div>
      </header>

      <main className="mx-auto flex w-full max-w-6xl flex-col gap-10 px-4 pb-20 pt-10 md:px-6 md:pt-16">
        <LandingHeroMotion />
        <div className="flex flex-wrap items-center gap-3">
          <ApiHealthBadge />
          <p className="text-sm text-muted-foreground">
            Phase 1 scaffold — API health wired for local Docker.
          </p>
        </div>
      </main>
    </div>
  );
}
