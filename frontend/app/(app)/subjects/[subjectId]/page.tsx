"use client";

import Link from "next/link";
import { useParams } from "next/navigation";

import { AppShell } from "@/components/layout/app-shell";
import { EmptyState } from "@/components/common/empty-state";
import { Skeleton } from "@/components/common/skeleton";
import { ChapterCard } from "@/features/syllabus/chapter-card";
import { ProgressBar } from "@/features/syllabus/progress-bar";
import { useSubjectQuery } from "@/features/syllabus/hooks";
import type { Chapter } from "@/types/syllabus";

function englishSectionLabel(title: string): string | null {
  if (title.startsWith("Flamingo")) return "Flamingo";
  if (title.startsWith("Hornbill")) return "Hornbill";
  if (title.startsWith("Vistas")) return "Vistas";
  if (title.startsWith("Snapshots")) return "Snapshots";
  if (title === "Writing Skills") return "Writing Skills";
  if (title === "Reading Skills") return "Reading Skills";
  if (title.startsWith("Grammar")) return "Grammar / Language";
  return null;
}

function groupEnglishChapters(chapters: Chapter[]): { label: string; chapters: Chapter[] }[] {
  const groups: { label: string; chapters: Chapter[] }[] = [];
  for (const chapter of chapters) {
    const label = englishSectionLabel(chapter.title) ?? "Other";
    const last = groups[groups.length - 1];
    if (last && last.label === label) {
      last.chapters.push(chapter);
    } else {
      groups.push({ label, chapters: [chapter] });
    }
  }
  return groups;
}

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
              <p className="mt-1 text-sm text-muted-foreground">
                {subjectQuery.data.chapter_count} sections ·{" "}
                {subjectQuery.data.topic_count} topics
              </p>
              <div className="mt-4 max-w-md">
                <ProgressBar
                  percentage={subjectQuery.data.completion_percentage}
                />
              </div>
            </div>

            {subjectQuery.data.code === "ENG" ? (
              <div className="space-y-6">
                {groupEnglishChapters(subjectQuery.data.chapters).map((group) => (
                  <section key={group.label} className="space-y-3">
                    <h3 className="text-xs font-semibold uppercase tracking-[0.18em] text-muted-foreground">
                      {group.label}
                    </h3>
                    {group.chapters.map((chapter) => (
                      <ChapterCard
                        key={chapter.id}
                        subjectId={subjectId}
                        chapter={chapter}
                      />
                    ))}
                  </section>
                ))}
              </div>
            ) : (
              <div className="space-y-3">
                {subjectQuery.data.chapters.map((chapter) => (
                  <ChapterCard
                    key={chapter.id}
                    subjectId={subjectId}
                    chapter={chapter}
                  />
                ))}
              </div>
            )}
          </>
        ) : null}
      </div>
    </AppShell>
  );
}
