"use client";

import Link from "next/link";
import { useParams } from "next/navigation";

import { Skeleton } from "@/components/common/skeleton";
import { QuizResultCard } from "@/features/quiz/quiz-result-card";
import {
  getQuizErrorMessage,
  useQuizResultQuery,
} from "@/features/quiz/hooks";

export default function QuizResultPage() {
  const params = useParams<{ attemptId: string }>();
  const resultQuery = useQuizResultQuery(params.attemptId);

  if (resultQuery.isLoading && !resultQuery.data) {
    return (
      <div className="mx-auto flex min-h-screen max-w-lg flex-col justify-center gap-4 px-4">
        <Skeleton className="h-40 w-full" />
        <Skeleton className="h-24 w-full" />
      </div>
    );
  }

  if (resultQuery.isError || !resultQuery.data) {
    return (
      <div className="flex min-h-screen items-center justify-center px-4 text-center">
        <div>
          <h1 className="font-display text-xl font-semibold">No result yet</h1>
          <p className="mt-2 text-sm text-muted-foreground">
            {resultQuery.isError
              ? getQuizErrorMessage(resultQuery.error)
              : "Finish the quiz to see your score."}
          </p>
          <Link
            href={`/quiz/attempt/${params.attemptId}`}
            className="mt-4 inline-block text-primary"
          >
            Back to quiz
          </Link>
        </div>
      </div>
    );
  }

  if (resultQuery.data.status === "active") {
    return (
      <div className="flex min-h-screen items-center justify-center px-4 text-center">
        <div>
          <h1 className="font-display text-xl font-semibold">Quiz in progress</h1>
          <p className="mt-2 text-sm text-muted-foreground">
            Finish the quiz to see your score.
          </p>
          <Link
            href={`/quiz/attempt/${params.attemptId}`}
            className="mt-4 inline-block text-primary"
          >
            Continue quiz
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-hero-grid px-4 py-10">
      <QuizResultCard result={resultQuery.data} />
    </div>
  );
}
