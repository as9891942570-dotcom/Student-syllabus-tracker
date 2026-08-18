"use client";

import { useQuery } from "@tanstack/react-query";

import { progressionApi } from "@/lib/api";
import { queryKeys } from "@/lib/query-keys";
import { useAuthStore } from "@/stores/auth-store";

export function useProgressionQuery() {
  const accessToken = useAuthStore((s) => s.accessToken);
  const userId = useAuthStore((s) => s.user?.id);
  return useQuery({
    queryKey: queryKeys.progression.me(userId),
    queryFn: () => progressionApi.me(),
    enabled: Boolean(accessToken),
  });
}
