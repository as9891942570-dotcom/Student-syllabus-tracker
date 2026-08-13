"use client";

import Link from "next/link";
import { Check, Play, Swords, X } from "lucide-react";

import {
  getStudyErrorMessage,
  useStartSessionMutation,
} from "@/features/study/hooks";
import { useTopicQuizzesQuery } from "@/features/quiz/hooks";
import { useToggleTopicMutation } from "@/features/syllabus/hooks";
import type { Topic } from "@/types/syllabus";
import { cn } from "@/lib/utils";

function TopicQuizLink({ topicId }: { topicId: string }) {
  const quizzes = useTopicQuizzesQuery(topicId);
  const quiz = quizzes.data?.[0];

  if (quizzes.isLoading) {
    return (
      <span className="inline-flex items-center justify-center rounded-full border border-border px-3 py-1.5 text-xs text-muted-foreground">
        Quiz...
      </span>
    );
  }

  if (!quiz) {
    return null;
  }

  return (
    <Link
      href={`/quiz/${quiz.id}`}
      className="inline-flex items-center justify-center gap-1.5 rounded-full border border-accent/40 bg-accent/10 px-3 py-1.5 text-xs font-semibold text-accent hover:bg-accent/20"
    >
      <Swords className="h-3.5 w-3.5" />
      Quiz
    </Link>
  );
}

export function TopicChecklist({
  topics,
  subjectId,
  chapterId,
}: {
  topics: Topic[];
  subjectId: string;
  chapterId: string;
}) {
  const toggle = useToggleTopicMutation(subjectId, chapterId);
  const startSession = useStartSessionMutation();

  return (
    <ul className="space-y-2">
      {topics.map((topic) => {
        const pending =
          toggle.isPending && toggle.variables?.topicId === topic.id;
        const starting =
          startSession.isPending && startSession.variables === topic.id;
        return (
          <li
            key={topic.id}
            className={cn(
              "rounded-xl border px-3 py-3 transition",
              topic.is_completed
                ? "border-primary/30 bg-primary/10"
                : "border-border bg-card",
            )}
          >
            <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
              <button
                type="button"
                disabled={pending}
                onClick={() =>
                  toggle.mutate({
                    topicId: topic.id,
                    isCompleted: !topic.is_completed,
                  })
                }
                className="flex min-w-0 flex-1 items-center gap-3 text-left"
              >
                <span
                  className={cn(
                    "flex h-6 w-6 shrink-0 items-center justify-center rounded-md border",
                    topic.is_completed
                      ? "border-primary bg-primary text-primary-foreground"
                      : "border-border bg-background",
                  )}
                >
                  {topic.is_completed ? (
                    <Check className="h-3.5 w-3.5" />
                  ) : null}
                </span>
                <span
                  className={cn(
                    "text-sm font-medium",
                    topic.is_completed && "text-primary",
                  )}
                >
                  {topic.title}
                </span>
              </button>
              <div className="flex flex-wrap items-center gap-2">
                <TopicQuizLink topicId={topic.id} />
                <button
                  type="button"
                  disabled={starting || startSession.isPending}
                  onClick={() => startSession.mutate(topic.id)}
                  className="inline-flex items-center justify-center gap-1.5 rounded-full bg-primary px-3 py-1.5 text-xs font-semibold text-primary-foreground hover:brightness-110 disabled:opacity-70"
                >
                  <Play className="h-3.5 w-3.5" />
                  {starting ? "Starting..." : "Start Session"}
                </button>
              </div>
            </div>
            {startSession.isError && startSession.variables === topic.id ? (
              <p className="mt-2 flex items-start gap-1 text-xs text-destructive">
                <X className="mt-0.5 h-3 w-3 shrink-0" />
                {getStudyErrorMessage(startSession.error)}
              </p>
            ) : null}
          </li>
        );
      })}
    </ul>
  );
}
