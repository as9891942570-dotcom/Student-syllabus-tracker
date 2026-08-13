"use client";

import Link from "next/link";
import { useParams } from "next/navigation";

import { AppShell } from "@/components/layout/app-shell";
import { EmptyState } from "@/components/common/empty-state";
import { Skeleton } from "@/components/common/skeleton";
import { ChapterCard } from "@/features/syllabus/chapter-card";
import { ProgressBar } from "@/features/syllabus/progress-bar";
import { useSubjectQuery } from "@/features/syllabus/hooks";

export default function SubjectChaptersPage() {
  const params = useParams<{ subjectId: string }>();
  const subjectId = params.subjectId;
  const subjectQuery = useSubjectQuery(subjectId);

  return (
    <AppShell title="Chapters">
      <div className="mx-auto w-full max-w-3xl space-y-6">
        <Link
          href="/subjects"
          className="text-sm font-semibold text-primary hover:underline"
        >
          ← Back to subjects
        </Link>

        {subjectQuery.isLoading ? <Skeleton className="h-48 w-full" /> : null}

        {subjectQuery.isError ? (
          <EmptyState
            title="Subject not found"
            description="This subject may be outside your syllabus scope."
          />
        ) : null}

        {subjectQuery.data ? (
          <>
            <div>
              <p className="text-xs font-semibold uppercase tracking-wide text-accent">
                {subjectQuery.data.code}
              </p>
              <h2 className="mt-1 font-display text-2xl font-semibold">
                {subjectQuery.data.name}
              </h2>
              <div className="mt-4 max-w-md">
                <ProgressBar
                  percentage={subjectQuery.data.completion_percentage}
                />
              </div>
            </div>
            <div className="space-y-3">
              {subjectQuery.data.chapters.map((chapter) => (
                <ChapterCard
                  key={chapter.id}
                  subjectId={subjectId}
                  chapter={chapter}
                />
              ))}
            </div>
          </>
        ) : null}
      </div>
    </AppShell>
  );
}
