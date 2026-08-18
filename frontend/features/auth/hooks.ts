"use client";

import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useRouter } from "next/navigation";

import { ApiError, authApi } from "@/lib/api";
import { useAuthStore } from "@/stores/auth-store";
import { rememberDeviceAccount } from "@/stores/device-accounts";
import type { LoginPayload, RegisterPayload, TokenResponse } from "@/types/auth";

function applyAuthSession(
  queryClient: ReturnType<typeof useQueryClient>,
  data: TokenResponse,
) {
  queryClient.clear();
  rememberDeviceAccount(data.user);
  useAuthStore.getState().setSession({
    accessToken: data.access_token,
    refreshToken: data.refresh_token,
    user: data.user,
  });
}

export function useLoginMutation() {
  const router = useRouter();
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (payload: LoginPayload) => authApi.login(payload),
    onSuccess: (data) => {
      applyAuthSession(queryClient, data);
      router.replace("/dashboard");
    },
  });
}

export function useRegisterMutation() {
  const router = useRouter();
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (payload: RegisterPayload) => authApi.register(payload),
    onSuccess: (data) => {
      applyAuthSession(queryClient, data);
      router.replace("/dashboard");
    },
  });
}

export function useLogoutMutation() {
  const router = useRouter();
  const queryClient = useQueryClient();
  const refreshToken = useAuthStore((s) => s.refreshToken);
  const clearSession = useAuthStore((s) => s.clearSession);

  return useMutation({
    mutationFn: async () => {
      try {
        await authApi.logout(refreshToken);
      } catch (error) {
        if (!(error instanceof ApiError && error.status === 401)) {
          throw error;
        }
      }
    },
    onSettled: () => {
      queryClient.clear();
      clearSession();
      router.replace("/login");
    },
  });
}

export function getAuthErrorMessage(error: unknown): string {
  if (error instanceof ApiError) {
    if (error.status >= 500) {
      return "Unable to connect to the server. Please try again.";
    }
    return error.message;
  }
  if (error instanceof TypeError) {
    return "Unable to connect to the server. Please try again.";
  }
  if (error instanceof Error) {
    const lowered = error.message.toLowerCase();
    if (
      lowered.includes("failed to fetch") ||
      lowered.includes("network") ||
      lowered.includes("load failed")
    ) {
      return "Unable to connect to the server. Please try again.";
    }
    return error.message;
  }
  return "Something went wrong. Please try again.";
}
