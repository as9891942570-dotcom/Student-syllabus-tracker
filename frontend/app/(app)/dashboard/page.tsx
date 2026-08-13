"use client";

import Link from "next/link";

import { AppShell } from "@/components/layout/app-shell";
import { EmptyState } from "@/components/common/empty-state";
import { ApiHealthBadge } from "@/features/health/api-health-badge";
import { useLogoutMutation } from "@/features/auth/hooks";
import { ProfileCompletionBar } from "@/features/profile/completion-bar";
import { useProfileQuery } from "@/features/profile/hooks";
import { useAuthStore } from "@/stores/auth-store";

export default function DashboardPage() {
  const user = useAuthStore((s) => s.user);
  const logout = useLogoutMutation();
  const profileQuery = useProfileQuery();

  return (
    <AppShell title="Dashboard">
      <div className="space-y-6">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <h2 className="font-display text-2xl font-semibold">
              Welcome{user ? `, ${user.full_name.split(" ")[0]}` : ""}
            </h2>
            <p className="mt-1 text-sm text-muted-foreground">
              Track your syllabus from My Subjects. Gamification comes later.
            </p>
          </div>
          <div className="flex items-center gap-3">
            <ApiHealthBadge />
            <Link
              href="/subjects"
              className="rounded-full border border-border px-4 py-2 text-sm font-semibold hover:border-primary/40"
            >
              My Subjects
            </Link>
            <Link
              href="/profile"
              className="rounded-full border border-border px-4 py-2 text-sm font-semibold hover:border-primary/40"
            >
              Profile
            </Link>
            <button
              type="button"
              onClick={() => logout.mutate()}
              disabled={logout.isPending}
              className="rounded-full border border-border px-4 py-2 text-sm font-semibold hover:border-primary/40 disabled:opacity-70"
            >
              {logout.isPending ? "Signing out..." : "Log out"}
            </button>
          </div>
        </div>

        {profileQuery.data ? (
          <ProfileCompletionBar
            percentage={profileQuery.data.completion_percentage}
            className="max-w-md"
          />
        ) : null}

        <EmptyState
          title="Syllabus tracking is live"
          description="Open My Subjects to view chapters, mark topics complete, and watch progress climb."
        />
      </div>
    </AppShell>
  );
}
