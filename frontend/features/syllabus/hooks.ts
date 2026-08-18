"use client";

import { useQuery } from "@tanstack/react-query";

import { syllabusApi } from "@/lib/api";
import { queryKeys } from "@/lib/query-keys";
import { useAuthStore } from "@/stores/auth-store";

export function useSubjectsQuery() {
  const accessToken = useAuthStore((s) => s.accessToken);
  const userId = useAuthStore((s) => s.user?.id);
  return useQuery({
    queryKey: queryKeys.syllabus.subjects(userId),
    queryFn: () => syllabusApi.listSubjects(),
    enabled: Boolean(accessToken),
  });
}

export function useSubjectQuery(subjectId: string) {
  const accessToken = useAuthStore((s) => s.accessToken);
  const userId = useAuthStore((s) => s.user?.id);
  return useQuery({
    queryKey: queryKeys.syllabus.subject(subjectId, userId),
    queryFn: () => syllabusApi.getSubject(subjectId),
    enabled: Boolean(accessToken) && Boolean(subjectId),
  });
}

export function useChapterTopicsQuery(chapterId: string) {
  const accessToken = useAuthStore((s) => s.accessToken);
  const userId = useAuthStore((s) => s.user?.id);
  return useQuery({
    queryKey: queryKeys.syllabus.chapter(chapterId, userId),
    queryFn: () => syllabusApi.getChapterTopics(chapterId),
    enabled: Boolean(accessToken) && Boolean(chapterId),
  });
}

export function useSyllabusCompletionQuery() {
  const accessToken = useAuthStore((s) => s.accessToken);
  const userId = useAuthStore((s) => s.user?.id);
  return useQuery({
    queryKey: queryKeys.syllabus.completion(userId),
    queryFn: () => syllabusApi.getCompletion(),
    enabled: Boolean(accessToken),
  });
}
