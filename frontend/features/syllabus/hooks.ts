"use client";

import { useQuery } from "@tanstack/react-query";

import { syllabusApi } from "@/lib/api";
import { queryKeys } from "@/lib/query-keys";

export function useSubjectsQuery() {
  return useQuery({
    queryKey: queryKeys.syllabus.subjects,
    queryFn: () => syllabusApi.listSubjects(),
  });
}

export function useSubjectQuery(subjectId: string) {
  return useQuery({
    queryKey: queryKeys.syllabus.subject(subjectId),
    queryFn: () => syllabusApi.getSubject(subjectId),
    enabled: Boolean(subjectId),
  });
}

export function useChapterTopicsQuery(chapterId: string) {
  return useQuery({
    queryKey: queryKeys.syllabus.chapter(chapterId),
    queryFn: () => syllabusApi.getChapterTopics(chapterId),
    enabled: Boolean(chapterId),
  });
}

export function useSyllabusCompletionQuery() {
  return useQuery({
    queryKey: queryKeys.syllabus.completion,
    queryFn: () => syllabusApi.getCompletion(),
  });
}
