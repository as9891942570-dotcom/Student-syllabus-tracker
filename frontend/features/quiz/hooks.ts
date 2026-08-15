"use client";

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useRouter } from "next/navigation";

import { ApiError, quizApi } from "@/lib/api";
import { queryKeys } from "@/lib/query-keys";

export function useTopicQuizzesQuery(topicId: string) {
  return useQuery({
    queryKey: queryKeys.quiz.topic(topicId),
    queryFn: () => quizApi.listForTopic(topicId),
    enabled: Boolean(topicId),
  });
}

export function useQuizDetailQuery(quizId: string) {
  return useQuery({
    queryKey: queryKeys.quiz.detail(quizId),
    queryFn: () => quizApi.getQuiz(quizId),
    enabled: Boolean(quizId),
  });
}

export function useQuizAttemptQuery(attemptId: string) {
  return useQuery({
    queryKey: queryKeys.quiz.attempt(attemptId),
    queryFn: () => quizApi.getAttempt(attemptId),
    enabled: Boolean(attemptId),
    refetchInterval: (query) =>
      query.state.data?.status === "active" ? 5000 : false,
  });
}

export function useCurrentQuestionQuery(attemptId: string, enabled = true) {
  return useQuery({
    queryKey: queryKeys.quiz.question(attemptId),
    queryFn: () => quizApi.currentQuestion(attemptId),
    enabled: Boolean(attemptId) && enabled,
  });
}

export function useQuizHistoryQuery() {
  return useQuery({
    queryKey: queryKeys.quiz.history,
    queryFn: () => quizApi.history(),
  });
}

export function useStartQuizMutation() {
  const router = useRouter();
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (quizId: string) => quizApi.start(quizId),
    onSuccess: (attempt) => {
      queryClient.setQueryData(queryKeys.quiz.active, attempt);
      queryClient.setQueryData(queryKeys.quiz.attempt(attempt.id), attempt);
      router.push(`/quiz/attempt/${attempt.id}`);
    },
  });
}

export function useSubmitAnswerMutation(attemptId: string) {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (optionId: string) => quizApi.submitAnswer(attemptId, optionId),
    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: queryKeys.quiz.attempt(attemptId),
      });
      await queryClient.invalidateQueries({
        queryKey: queryKeys.quiz.question(attemptId),
      });
    },
  });
}

export function useNextQuestionMutation(attemptId: string) {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: () => quizApi.next(attemptId),
    onSuccess: async (attempt) => {
      queryClient.setQueryData(queryKeys.quiz.attempt(attemptId), attempt);
      await queryClient.invalidateQueries({
        queryKey: queryKeys.quiz.question(attemptId),
      });
    },
  });
}

export function useCompleteQuizMutation(attemptId: string) {
  const router = useRouter();
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: () => quizApi.complete(attemptId),
    onSuccess: async (attempt) => {
      queryClient.setQueryData(queryKeys.quiz.attempt(attemptId), attempt);
      queryClient.setQueryData(queryKeys.quiz.active, null);
      await queryClient.invalidateQueries({ queryKey: queryKeys.profile.me });
      await queryClient.invalidateQueries({ queryKey: queryKeys.syllabus.subjects });
      await queryClient.invalidateQueries({
        queryKey: queryKeys.syllabus.completion,
      });
      await queryClient.invalidateQueries({ queryKey: queryKeys.quiz.history });
      await queryClient.invalidateQueries({ queryKey: queryKeys.progression.me });
      await queryClient.invalidateQueries({ queryKey: ["syllabus", "chapters"] });
      router.push(`/quiz/attempt/${attemptId}/result`);
    },
  });
}

export function getQuizErrorMessage(error: unknown): string {
  if (error instanceof ApiError) {
    if (error.status === 401) return "Please sign in to take quizzes.";
    if (error.status === 403) return "You cannot access this quiz attempt.";
    if (error.status === 404) return "Quiz not found or unavailable.";
    if (error.status === 409) return error.message;
    return error.message;
  }
  if (error instanceof Error) return error.message;
  return "Something went wrong. Please try again.";
}
