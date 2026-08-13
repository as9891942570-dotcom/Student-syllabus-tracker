"use client";

import Link from "next/link";
import { useParams } from "next/navigation";

import { AppShell } from "@/components/layout/app-shell";
import { EmptyState } from "@/components/common/empty-state";
import { Skeleton } from "@/components/common/skeleton";
import { ProgressBar } from "@/features/syllabus/progress-bar";
import { TopicChecklist } from "@/features/syllabus/topic-checklist";
import { useChapterTopicsQuery } from "@/features/syllabus/hooks";

export default function ChapterTopicsPage() {
  const params = useParams<{ subjectId: string; chapterId: string }>();
  const { subjectId, chapterId } = params;
  const chapterQuery = useChapterTopicsQuery(chapterId);

  return (
    <AppShell title="Topics">
      <div className="mx-auto w-full max-w-2xl space-y-6">
        <Link
          href={`/subjects/${subjectId}`}
          className="text-sm font-semibold text-primary hover:underline"
        >
          ← Back to chapters
        </Link>

        {chapterQuery.isLoading ? <Skeleton className="h-48 w-full" /> : null}

        {chapterQuery.isError ? (
          <EmptyState
            title="Chapter not found"
            description="Unable to load topics for this chapter."
          />
        ) : null}

        {chapterQuery.data ? (
          <>
            <div>
              <h2 className="font-display text-2xl font-semibold">
                {chapterQuery.data.title}
              </h2>
              <p className="mt-1 text-sm text-muted-foreground">
                Tap a topic to mark it complete or incomplete.
              </p>
              <div className="mt-4">
                <ProgressBar
                  percentage={chapterQuery.data.completion_percentage}
                />
              </div>
            </div>
            <TopicChecklist
              topics={chapterQuery.data.topics}
              subjectId={subjectId}
              chapterId={chapterId}
            />
          </>
        ) : null}
      </div>
    </AppShell>
  );
}
