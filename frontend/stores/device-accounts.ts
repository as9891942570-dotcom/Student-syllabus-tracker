"use client";

import type { AuthUser } from "@/types/auth";

const STORAGE_KEY = "eduquest-device-accounts";

export type DeviceAccount = {
  userId: string;
  email: string;
  fullName: string;
  className?: string | null;
  streamName?: string | null;
  boardName?: string | null;
};

function isAccount(value: unknown): value is DeviceAccount {
  if (!value || typeof value !== "object") return false;
  const row = value as Record<string, unknown>;
  return (
    typeof row.userId === "string" &&
    typeof row.email === "string" &&
    typeof row.fullName === "string"
  );
}

export function listDeviceAccounts(): DeviceAccount[] {
  if (typeof window === "undefined") return [];
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (!raw) return [];
    const parsed = JSON.parse(raw) as unknown;
    if (!Array.isArray(parsed)) return [];
    return parsed.filter(isAccount);
  } catch {
    return [];
  }
}

export function rememberDeviceAccount(
  user: AuthUser,
  extras?: {
    className?: string | null;
    streamName?: string | null;
    boardName?: string | null;
  },
): void {
  if (typeof window === "undefined") return;
  const previous = listDeviceAccounts().find((account) => account.userId === user.id);
  const next: DeviceAccount = {
    userId: user.id,
    email: user.email,
    fullName: user.full_name,
    className: extras?.className ?? previous?.className ?? null,
    streamName: extras?.streamName ?? previous?.streamName ?? null,
    boardName: extras?.boardName ?? previous?.boardName ?? null,
  };
  const accounts = [next, ...listDeviceAccounts().filter((account) => account.userId !== user.id)].slice(
    0,
    8,
  );
  window.localStorage.setItem(STORAGE_KEY, JSON.stringify(accounts));
}

export function academicLabel(account: DeviceAccount): string {
  const parts = [account.className, account.streamName].filter(Boolean);
  return parts.length ? parts.join(" • ") : "Academic profile pending";
}
