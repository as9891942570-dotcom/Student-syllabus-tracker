"use client";

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useRouter } from "next/navigation";

import { ApiError, quizApi } from "@/lib/api";
import { queryKeys } from "@/lib/query-keys";
import { useAuthStore } from "@/stores/auth-store";

function useUserId() {
  return useAuthStore((s) => s.user?.id);
}

export function useTopicQuizzesQuery(topicId: string) {
  const accessToken = useAuthStore((s) => s.accessToken);
  const userId = useUserId();
  return useQuery({
    queryKey: queryKeys.quiz.topic(topicId, userId),
    queryFn: () => quizApi.listForTopic(topicId),
    enabled: Boolean(accessToken) && Boolean(topicId),
  });
}

export function useQuizDetailQuery(quizId: string) {
  const accessToken = useAuthStore((s) => s.accessToken);
  const userId = useUserId();
  return useQuery({
    queryKey: queryKeys.quiz.detail(quizId, userId),
    queryFn: () => quizApi.getQuiz(quizId),
    enabled: Boolean(accessToken) && Boolean(quizId),
  });
}

export function useQuizAttemptQuery(attemptId: string) {
  const accessToken = useAuthStore((s) => s.accessToken);
  const userId = useUserId();
  return useQuery({
    queryKey: queryKeys.quiz.attempt(attemptId, userId),
    queryFn: () => quizApi.getAttempt(attemptId),
    enabled: Boolean(accessToken) && Boolean(attemptId),
    refetchInterval: (query) =>
      query.state.data?.status === "active" ? 5000 : false,
  });
}

export function useCurrentQuestionQuery(attemptId: string, enabled = true) {
  const accessToken = useAuthStore((s) => s.accessToken);
  const userId = useUserId();
  return useQuery({
    queryKey: queryKeys.quiz.question(attemptId, userId),
    queryFn: () => quizApi.currentQuestion(attemptId),
    enabled: Boolean(accessToken) && Boolean(attemptId) && enabled,
  });
}

export function useQuizHistoryQuery() {
  const accessToken = useAuthStore((s) => s.accessToken);
  const userId = useUserId();
  return useQuery({
    queryKey: queryKeys.quiz.history(userId),
    queryFn: () => quizApi.history(),
    enabled: Boolean(accessToken),
  });
}

export function useStartQuizMutation() {
  const router = useRouter();
  const queryClient = useQueryClient();
  const userId = useUserId();
  return useMutation({
    mutationFn: (quizId: string) => quizApi.start(quizId),
    onSuccess: (attempt) => {
      queryClient.setQueryData(queryKeys.quiz.active(userId), attempt);
      queryClient.setQueryData(queryKeys.quiz.attempt(attempt.id, userId), attempt);
      router.push(`/quiz/attempt/${attempt.id}`);
    },
  });
}

export function useSubmitAnswerMutation(attemptId: string) {
  const queryClient = useQueryClient();
  const userId = useUserId();
  return useMutation({
    mutationFn: (optionId: string) => quizApi.submitAnswer(attemptId, optionId),
    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: queryKeys.quiz.attempt(attemptId, userId),
      });
      await queryClient.invalidateQueries({
        queryKey: queryKeys.quiz.question(attemptId, userId),
      });
    },
  });
}

export function useNextQuestionMutation(attemptId: string) {
  const queryClient = useQueryClient();
  const userId = useUserId();
  return useMutation({
    mutationFn: () => quizApi.next(attemptId),
    onSuccess: async (attempt) => {
      queryClient.setQueryData(queryKeys.quiz.attempt(attemptId, userId), attempt);
      await queryClient.invalidateQueries({
        queryKey: queryKeys.quiz.question(attemptId, userId),
      });
    },
  });
}

export function useCompleteQuizMutation(attemptId: string) {
  const router = useRouter();
  const queryClient = useQueryClient();
  const userId = useUserId();
  return useMutation({
    mutationFn: () => quizApi.complete(attemptId),
    onSuccess: async (attempt) => {
      queryClient.setQueryData(queryKeys.quiz.attempt(attemptId, userId), attempt);
      queryClient.setQueryData(queryKeys.quiz.active(userId), null);
      await queryClient.invalidateQueries({ queryKey: queryKeys.profile.me(userId) });
      await queryClient.invalidateQueries({
        queryKey: queryKeys.syllabus.subjects(userId),
      });
      await queryClient.invalidateQueries({
        queryKey: queryKeys.syllabus.completion(userId),
      });
      await queryClient.invalidateQueries({ queryKey: queryKeys.quiz.history(userId) });
      await queryClient.invalidateQueries({
        queryKey: queryKeys.progression.me(userId),
      });
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
