"use client";

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";

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

export function useToggleTopicMutation(subjectId?: string, chapterId?: string) {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({
      topicId,
      isCompleted,
    }: {
      topicId: string;
      isCompleted: boolean;
    }) => syllabusApi.setTopicProgress(topicId, isCompleted),
    onSuccess: async () => {
      await Promise.all([
        queryClient.invalidateQueries({ queryKey: queryKeys.syllabus.subjects }),
        queryClient.invalidateQueries({ queryKey: queryKeys.syllabus.completion }),
        queryClient.invalidateQueries({ queryKey: queryKeys.syllabus.structure }),
        subjectId
          ? queryClient.invalidateQueries({
              queryKey: queryKeys.syllabus.subject(subjectId),
            })
          : Promise.resolve(),
        chapterId
          ? queryClient.invalidateQueries({
              queryKey: queryKeys.syllabus.chapter(chapterId),
            })
          : Promise.resolve(),
      ]);
    },
  });
}
