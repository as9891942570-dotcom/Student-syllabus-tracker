"use client";

import Link from "next/link";

import { AppShell } from "@/components/layout/app-shell";
import { EmptyState } from "@/components/common/empty-state";
import { Skeleton } from "@/components/common/skeleton";
import { ApiHealthBadge } from "@/features/health/api-health-badge";
import { ProfileCompletionBar } from "@/features/profile/completion-bar";
import { useProfileQuery } from "@/features/profile/hooks";
import { SubjectCard } from "@/features/syllabus/subject-card";
import { useSubjectsQuery } from "@/features/syllabus/hooks";
import { useAuthStore } from "@/stores/auth-store";

export default function DashboardPage() {
  const user = useAuthStore((s) => s.user);
  const profileQuery = useProfileQuery();
  const subjectsQuery = useSubjectsQuery();
  const profile = profileQuery.data;

  return (
    <AppShell title="Dashboard">
      <div className="w-full space-y-6 text-left">
        <div>
          <h2 className="font-display text-2xl font-semibold">
            Welcome{user ? `, ${user.full_name.split(" ")[0]}` : ""}
          </h2>
          <p className="mt-1 text-sm text-muted-foreground">
            Track subjects, complete topic quizzes, and earn XP and coins.
          </p>
          {profile?.school_class ? (
            <p className="mt-1 text-sm text-muted-foreground">
              {profile.board?.name} • {profile.school_class.name}
              {profile.stream ? ` • ${profile.stream.name}` : ""}
            </p>
          ) : null}
          <div className="mt-3">
            <ApiHealthBadge />
          </div>
        </div>

        {profile ? (
          <ProfileCompletionBar
            percentage={profile.completion_percentage}
            className="max-w-md"
          />
        ) : null}

        <div className="flex flex-wrap gap-3">
          <Link
            href="/subjects"
            className="rounded-full bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground"
          >
            My Subjects
          </Link>
        </div>

        {subjectsQuery.isLoading ? (
          <div className="grid max-w-4xl gap-4 sm:grid-cols-2">
            <Skeleton className="h-36" />
            <Skeleton className="h-36" />
          </div>
        ) : null}

        {subjectsQuery.isError ? (
          <EmptyState
            title="Could not load subjects"
            description="Check that the API is running, then refresh."
          />
        ) : null}

        {subjectsQuery.data && subjectsQuery.data.length > 0 ? (
          <div>
            <h3 className="mb-3 font-display text-lg font-semibold">Your subjects</h3>
            <div className="grid max-w-4xl gap-4 sm:grid-cols-2">
              {subjectsQuery.data.map((subject) => (
                <SubjectCard key={subject.id} subject={subject} />
              ))}
            </div>
          </div>
        ) : null}

        {subjectsQuery.data && subjectsQuery.data.length === 0 ? (
          <EmptyState
            title="No subjects yet"
            description="Finish academic profile setup to load your syllabus."
          />
        ) : null}
      </div>
    </AppShell>
  );
}
