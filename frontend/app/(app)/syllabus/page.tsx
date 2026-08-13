"use client";

import Link from "next/link";

import { AppShell } from "@/components/layout/app-shell";
import { EmptyState } from "@/components/common/empty-state";
import { Skeleton } from "@/components/common/skeleton";
import { ProgressBar } from "@/features/syllabus/progress-bar";
import { SubjectCard } from "@/features/syllabus/subject-card";
import { useSyllabusCompletionQuery } from "@/features/syllabus/hooks";

export default function SyllabusOverviewPage() {
  const completionQuery = useSyllabusCompletionQuery();

  return (
    <AppShell title="Syllabus">
      <div className="space-y-6">
        <div>
          <h2 className="font-display text-2xl font-semibold">
            Syllabus overview
          </h2>
          <p className="mt-1 text-sm text-muted-foreground">
            Overall completion across every subject in your profile scope.
          </p>
        </div>

        {completionQuery.isLoading ? <Skeleton className="h-40 w-full" /> : null}

        {completionQuery.isError ? (
          <EmptyState
            title="Could not load syllabus"
            description="Check your profile board/class settings and try again."
          />
        ) : null}

        {completionQuery.data ? (
          <>
            <div className="rounded-2xl border border-border bg-card p-5 md:max-w-lg">
              <p className="text-sm font-medium text-muted-foreground">
                Overall syllabus completion
              </p>
              <p className="mt-2 font-display text-4xl font-bold text-primary">
                {completionQuery.data.overall_completion_percentage}%
              </p>
              <div className="mt-4">
                <ProgressBar
                  percentage={
                    completionQuery.data.overall_completion_percentage
                  }
                />
              </div>
              <p className="mt-3 text-sm text-muted-foreground">
                {completionQuery.data.completed_topics} of{" "}
                {completionQuery.data.total_topics} topics ·{" "}
                {completionQuery.data.total_chapters} chapters ·{" "}
                {completionQuery.data.total_subjects} subjects
              </p>
            </div>

            <div className="flex items-center justify-between">
              <h3 className="font-display text-lg font-semibold">Subjects</h3>
              <Link
                href="/subjects"
                className="text-sm font-semibold text-primary hover:underline"
              >
                Open My Subjects
              </Link>
            </div>
            <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
              {completionQuery.data.subjects.map((subject) => (
                <SubjectCard key={subject.id} subject={subject} />
              ))}
            </div>
          </>
        ) : null}
      </div>
    </AppShell>
  );
}
