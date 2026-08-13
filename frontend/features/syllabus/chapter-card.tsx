import Link from "next/link";

import { ProgressBar } from "@/features/syllabus/progress-bar";
import type { Chapter } from "@/types/syllabus";

export function ChapterCard({
  subjectId,
  chapter,
}: {
  subjectId: string;
  chapter: Chapter;
}) {
  return (
    <Link
      href={`/subjects/${subjectId}/chapters/${chapter.id}`}
      className="block rounded-2xl border border-border bg-card p-4 transition hover:border-primary/40"
    >
      <div className="mb-3 flex items-center justify-between gap-3">
        <h3 className="font-display text-lg font-semibold">{chapter.title}</h3>
        <span className="text-sm font-semibold text-primary">
          {chapter.completion_percentage}%
        </span>
      </div>
      <ProgressBar percentage={chapter.completion_percentage} size="sm" />
      <p className="mt-2 text-xs text-muted-foreground">
        {chapter.completed_topic_count}/{chapter.topic_count} topics done
      </p>
    </Link>
  );
}
