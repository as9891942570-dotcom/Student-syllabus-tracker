import Link from "next/link";

import { ProgressBar } from "@/features/syllabus/progress-bar";
import type { Subject } from "@/types/syllabus";

export function SubjectCard({ subject }: { subject: Subject }) {
  return (
    <Link
      href={`/subjects/${subject.id}`}
      className="block rounded-2xl border border-border bg-card p-5 shadow-sm transition hover:border-primary/40 hover:shadow-glow"
    >
      <div className="mb-4 flex items-start justify-between gap-3">
        <div>
          <p className="text-xs font-semibold uppercase tracking-wide text-accent">
            {subject.code}
          </p>
          <h3 className="mt-1 font-display text-xl font-semibold text-foreground">
            {subject.name}
          </h3>
        </div>
        <span className="rounded-full bg-primary/10 px-2.5 py-1 text-xs font-bold text-primary">
          {subject.completion_percentage}%
        </span>
      </div>
      <ProgressBar percentage={subject.completion_percentage} size="sm" />
      <p className="mt-3 text-xs text-muted-foreground">
        {subject.completed_topic_count}/{subject.topic_count} topics ·{" "}
        {subject.chapter_count} chapters
      </p>
    </Link>
  );
}
