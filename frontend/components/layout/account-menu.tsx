"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import { LogOut, Settings, UserRound, Users } from "lucide-react";

import { useLogoutMutation } from "@/features/auth/hooks";
import { useAuthStore } from "@/stores/auth-store";
import { listDeviceAccounts } from "@/stores/device-accounts";
import { cn } from "@/lib/utils";

export function AccountMenu({ compact = false }: { compact?: boolean }) {
  const user = useAuthStore((s) => s.user);
  const logout = useLogoutMutation();
  const [open, setOpen] = useState(false);
  const otherAccounts = useMemo(
    () => listDeviceAccounts().filter((account) => account.userId !== user?.id),
    [user?.id, open],
  );

  return (
    <div className="relative">
      <button
        type="button"
        onClick={() => setOpen((value) => !value)}
        className={cn(
          "flex w-full items-center gap-2 rounded-xl border border-border bg-card px-3 py-2 text-left text-sm font-medium hover:border-primary/40",
          compact && "h-9 w-9 justify-center px-0",
        )}
        aria-haspopup="menu"
        aria-expanded={open}
      >
        <UserRound className="h-4 w-4 shrink-0" />
        {compact ? null : (
          <span className="min-w-0 truncate">
            {user?.full_name ?? "Account"}
          </span>
        )}
      </button>
      {open ? (
        <div
          className={cn(
            "absolute z-50 mt-2 min-w-52 rounded-xl border border-border bg-card p-1 shadow-lg",
            compact ? "right-0" : "left-0 right-0",
          )}
        >
          <Link
            href="/profile"
            onClick={() => setOpen(false)}
            className="flex items-center gap-2 rounded-lg px-3 py-2 text-sm hover:bg-muted"
          >
            <UserRound className="h-4 w-4" />
            Profile
          </Link>
          <Link
            href="/settings"
            onClick={() => setOpen(false)}
            className="flex items-center gap-2 rounded-lg px-3 py-2 text-sm hover:bg-muted"
          >
            <Settings className="h-4 w-4" />
            Settings
          </Link>
          <Link
            href="/switch-account"
            onClick={() => setOpen(false)}
            className="flex items-center gap-2 rounded-lg px-3 py-2 text-sm hover:bg-muted"
          >
            <Users className="h-4 w-4" />
            Switch Account
            {otherAccounts.length ? (
              <span className="ml-auto text-xs text-muted-foreground">
                {otherAccounts.length}
              </span>
            ) : null}
          </Link>
          <button
            type="button"
            onClick={() => {
              setOpen(false);
              logout.mutate();
            }}
            disabled={logout.isPending}
            className="flex w-full items-center gap-2 rounded-lg px-3 py-2 text-left text-sm text-destructive hover:bg-destructive/10 disabled:opacity-70"
          >
            <LogOut className="h-4 w-4" />
            {logout.isPending ? "Signing out..." : "Logout"}
          </button>
        </div>
      ) : null}
    </div>
  );
}
