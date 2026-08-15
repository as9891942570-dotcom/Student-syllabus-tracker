"use client";

import { useQuery } from "@tanstack/react-query";

import { progressionApi } from "@/lib/api";
import { queryKeys } from "@/lib/query-keys";

export function useProgressionQuery() {
  return useQuery({
    queryKey: queryKeys.progression.me,
    queryFn: () => progressionApi.me(),
  });
}
