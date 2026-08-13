"use client";

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";

import { ApiError, profileApi } from "@/lib/api";
import { queryKeys } from "@/lib/query-keys";
import type { ProfileUpdatePayload } from "@/types/profile";

export function useProfileQuery() {
  return useQuery({
    queryKey: queryKeys.profile.me,
    queryFn: () => profileApi.getMe(),
  });
}

export function useBoardsQuery() {
  return useQuery({
    queryKey: queryKeys.profile.boards,
    queryFn: () => profileApi.listBoards(),
  });
}

export function useClassesQuery() {
  return useQuery({
    queryKey: queryKeys.profile.classes,
    queryFn: () => profileApi.listClasses(),
  });
}

export function useStreamsQuery() {
  return useQuery({
    queryKey: queryKeys.profile.streams,
    queryFn: () => profileApi.listStreams(),
  });
}

export function useUpdateProfileMutation() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (payload: ProfileUpdatePayload) => profileApi.updateMe(payload),
    onSuccess: (data) => {
      queryClient.setQueryData(queryKeys.profile.me, data);
    },
  });
}

export function useUploadPhotoMutation() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (file: File) => profileApi.uploadPhoto(file),
    onSuccess: (data) => {
      queryClient.setQueryData(queryKeys.profile.me, data);
    },
  });
}

export function getProfileErrorMessage(error: unknown): string {
  if (error instanceof ApiError) return error.message;
  if (error instanceof Error) return error.message;
  return "Something went wrong. Please try again.";
}
