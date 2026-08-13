"use client";

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useRouter } from "next/navigation";

import { ApiError, studyApi } from "@/lib/api";
import { queryKeys } from "@/lib/query-keys";

export function useActiveSessionQuery() {
  return useQuery({
    queryKey: queryKeys.study.active,
    queryFn: () => studyApi.getActive(),
  });
}

export function useStudySessionQuery(sessionId: string) {
  return useQuery({
    queryKey: queryKeys.study.session(sessionId),
    queryFn: () => studyApi.getSession(sessionId),
    enabled: Boolean(sessionId),
  });
}

export function useStartSessionMutation() {
  const router = useRouter();
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (topicId: string) => studyApi.start(topicId),
    onSuccess: (session) => {
      queryClient.setQueryData(queryKeys.study.active, session);
      queryClient.setQueryData(queryKeys.study.session(session.id), session);
      router.push(`/study/${session.id}`);
    },
  });
}

export function useRecordActivityMutation(sessionId: string) {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (result: "correct" | "incorrect") =>
      studyApi.recordActivity(sessionId, result),
    onSuccess: (session) => {
      queryClient.setQueryData(queryKeys.study.session(sessionId), session);
      queryClient.setQueryData(queryKeys.study.active, session);
    },
  });
}

export function useCompleteSessionMutation(sessionId: string) {
  const router = useRouter();
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: () => studyApi.complete(sessionId),
    onSuccess: async (session) => {
      queryClient.setQueryData(queryKeys.study.session(sessionId), session);
      queryClient.setQueryData(queryKeys.study.active, null);
      await queryClient.invalidateQueries({ queryKey: queryKeys.profile.me });
      await queryClient.invalidateQueries({ queryKey: queryKeys.syllabus.subjects });
      await queryClient.invalidateQueries({
        queryKey: queryKeys.syllabus.completion,
      });
      router.push(`/study/${sessionId}/result`);
    },
  });
}

export function getStudyErrorMessage(error: unknown): string {
  if (error instanceof ApiError) return error.message;
  if (error instanceof Error) return error.message;
  return "Something went wrong. Please try again.";
}
