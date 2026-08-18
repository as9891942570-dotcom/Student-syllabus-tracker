"use client";

import Link from "next/link";
import { Check, Lock, Swords } from "lucide-react";

import { useTopicQuizzesQuery } from "@/features/quiz/hooks";
import {
  topicCardStatus,
  topicQuizLabel,
} from "@/features/syllabus/topic-card-state";
import type { Topic } from "@/types/syllabus";
import { cn } from "@/lib/utils";

function TopicQuizLink({
  topicId,
  locked,
  isCurrent,
  isCompleted,
}: {
  topicId: string;
  locked: boolean;
  isCurrent: boolean;
  isCompleted: boolean;
}) {
  const quizzes = useTopicQuizzesQuery(locked ? "" : topicId);
  const quiz = quizzes.data?.[0];
  const status = topicCardStatus({ is_locked: locked, is_completed: isCompleted });

  if (locked) {
    return (
      <span className="inline-flex items-center justify-center gap-1.5 rounded-full border border-border px-3 py-1.5 text-xs font-semibold text-muted-foreground opacity-60">
        <Lock className="h-3.5 w-3.5" />
        {topicQuizLabel("locked")}
      </span>
    );
  }

  if (quizzes.isLoading) {
    return (
      <span className="inline-flex items-center justify-center rounded-full border border-primary/30 bg-primary/10 px-3 py-1.5 text-xs font-semibold text-primary">
        {topicQuizLabel(status)}...
      </span>
    );
  }

  if (!quiz) {
    return (
      <span className="inline-flex items-center justify-center rounded-full border border-border px-3 py-1.5 text-xs text-muted-foreground">
        Quiz coming soon
      </span>
    );
  }

  return (
    <Link
      href={`/quiz/${quiz.id}`}
      className={cn(
        "inline-flex items-center justify-center gap-1.5 rounded-full px-3 py-1.5 text-xs font-semibold",
        isCurrent
          ? "bg-primary text-primary-foreground hover:brightness-110"
          : "border border-accent/40 bg-accent/10 text-accent hover:bg-accent/20",
      )}
    >
      <Swords className="h-3.5 w-3.5" />
      {topicQuizLabel(status)}
    </Link>
  );
}

export function TopicChecklist({
  topics,
}: {
  topics: Topic[];
  subjectId?: string;
  chapterId?: string;
}) {
  return (
    <ul className="space-y-2">
      {topics.map((topic) => {
        const locked = Boolean(topic.is_locked);
        return (
          <li
            key={topic.id}
            className={cn(
              "rounded-xl border px-3 py-3 transition",
              topic.is_completed
                ? "border-primary/30 bg-primary/10"
                : topic.is_current
                  ? "border-accent/40 bg-accent/5"
                  : locked
                    ? "border-border/70 bg-muted/30 opacity-80"
                    : "border-border bg-card",
            )}
          >
            <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
              <div className="flex min-w-0 flex-1 items-center gap-3">
                <span
                  className={cn(
                    "flex h-6 w-6 shrink-0 items-center justify-center rounded-md border",
                    topic.is_completed
                      ? "border-primary bg-primary text-primary-foreground"
                      : locked
                        ? "border-border bg-muted text-muted-foreground"
                        : "border-border bg-background",
                  )}
                >
                  {topic.is_completed ? (
                    <Check className="h-3.5 w-3.5" />
                  ) : locked ? (
                    <Lock className="h-3.5 w-3.5" />
                  ) : null}
                </span>
                <span className="min-w-0">
                  <span
                    className={cn(
                      "block text-sm font-medium",
                      topic.is_completed && "text-primary",
                      locked && "text-muted-foreground",
                    )}
                  >
                    {topic.title}
                  </span>
                  {topic.is_completed ? (
                    <span className="text-[11px] font-semibold uppercase tracking-wide text-primary">
                      ✓ Completed
                    </span>
                  ) : null}
                  {topic.is_current ? (
                    <span className="text-[11px] font-semibold uppercase tracking-wide text-accent">
                      Current topic
                    </span>
                  ) : null}
                  {locked ? (
                    <span className="text-[11px] text-muted-foreground">
                      🔒 Locked — complete previous topic quiz to unlock
                    </span>
                  ) : null}
                </span>
              </div>
              <div className="flex flex-wrap items-center gap-2">
                <TopicQuizLink
                  topicId={topic.id}
                  locked={locked}
                  isCurrent={Boolean(topic.is_current)}
                  isCompleted={Boolean(topic.is_completed)}
                />
              </div>
            </div>
          </li>
        );
      })}
    </ul>
  );
}
