"use client";

import Link from "next/link";

import { AppShell } from "@/components/layout/app-shell";
import { EmptyState } from "@/components/common/empty-state";
import { Skeleton } from "@/components/common/skeleton";
import { ProgressBar } from "@/features/syllabus/progress-bar";
import { SubjectCard } from "@/features/syllabus/subject-card";
import {
  useSubjectsQuery,
  useSyllabusCompletionQuery,
} from "@/features/syllabus/hooks";

export default function SubjectsPage() {
  const subjectsQuery = useSubjectsQuery();
  const completionQuery = useSyllabusCompletionQuery();

  return (
    <AppShell title="My Subjects">
      <div className="space-y-6">
        <div className="flex flex-wrap items-end justify-between gap-3">
          <div>
            <h2 className="font-display text-2xl font-semibold">My Subjects</h2>
            <p className="mt-1 text-sm text-muted-foreground">
              Track syllabus completion for your board and class.
            </p>
          </div>
          <Link
            href="/syllabus"
            className="text-sm font-semibold text-primary hover:underline"
          >
            Syllabus overview
          </Link>
        </div>

        {completionQuery.data ? (
          <div className="rounded-2xl border border-border bg-card p-4 md:max-w-md">
            <ProgressBar
              percentage={completionQuery.data.overall_completion_percentage}
            />
            <p className="mt-2 text-xs text-muted-foreground">
              {completionQuery.data.completed_topics}/
              {completionQuery.data.total_topics} topics across{" "}
              {completionQuery.data.total_subjects} subjects
            </p>
          </div>
        ) : null}

        {subjectsQuery.isLoading ? (
          <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
            <Skeleton className="h-40" />
            <Skeleton className="h-40" />
            <Skeleton className="h-40" />
          </div>
        ) : null}

        {subjectsQuery.isError ? (
          <EmptyState
            title="Could not load subjects"
            description="Make sure your profile has board and class set, then retry."
          />
        ) : null}

        {subjectsQuery.data && subjectsQuery.data.length === 0 ? (
          <EmptyState
            title="No subjects yet"
            description="Complete your profile with board, class, and stream (if Class 11–12)."
          />
        ) : null}

        {subjectsQuery.data && subjectsQuery.data.length > 0 ? (
          <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
            {subjectsQuery.data.map((subject) => (
              <SubjectCard key={subject.id} subject={subject} />
            ))}
          </div>
        ) : null}
      </div>
    </AppShell>
  );
}
