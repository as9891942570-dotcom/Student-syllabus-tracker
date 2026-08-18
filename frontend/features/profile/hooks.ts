"use client";

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";

import { ApiError, profileApi } from "@/lib/api";
import { queryKeys } from "@/lib/query-keys";
import { useAuthStore } from "@/stores/auth-store";
import type { ProfileUpdatePayload } from "@/types/profile";

export function useProfileQuery() {
  const accessToken = useAuthStore((s) => s.accessToken);
  const userId = useAuthStore((s) => s.user?.id);
  return useQuery({
    queryKey: queryKeys.profile.me(userId),
    queryFn: () => profileApi.getMe(),
    enabled: Boolean(accessToken),
  });
}

export function useBoardsQuery() {
  const accessToken = useAuthStore((s) => s.accessToken);
  return useQuery({
    queryKey: queryKeys.profile.boards,
    queryFn: () => profileApi.listBoards(),
    enabled: Boolean(accessToken),
  });
}

export function useClassesQuery() {
  const accessToken = useAuthStore((s) => s.accessToken);
  return useQuery({
    queryKey: queryKeys.profile.classes,
    queryFn: () => profileApi.listClasses(),
    enabled: Boolean(accessToken),
  });
}

export function useStreamsQuery() {
  const accessToken = useAuthStore((s) => s.accessToken);
  return useQuery({
    queryKey: queryKeys.profile.streams,
    queryFn: () => profileApi.listStreams(),
    enabled: Boolean(accessToken),
  });
}

export function useUpdateProfileMutation() {
  const queryClient = useQueryClient();
  const userId = useAuthStore((s) => s.user?.id);
  return useMutation({
    mutationFn: (payload: ProfileUpdatePayload) => profileApi.updateMe(payload),
    onSuccess: (data) => {
      queryClient.setQueryData(queryKeys.profile.me(userId), data);
    },
  });
}

export function useUploadPhotoMutation() {
  const queryClient = useQueryClient();
  const userId = useAuthStore((s) => s.user?.id);
  return useMutation({
    mutationFn: (file: File) => profileApi.uploadPhoto(file),
    onSuccess: (data) => {
      queryClient.setQueryData(queryKeys.profile.me(userId), data);
    },
  });
}

export function getProfileErrorMessage(error: unknown): string {
  if (error instanceof ApiError) return error.message;
  if (error instanceof Error) return error.message;
  return "Something went wrong. Please try again.";
}
