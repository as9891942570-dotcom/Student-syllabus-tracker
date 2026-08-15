"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";

import { AppShell } from "@/components/layout/app-shell";
import {
  getAuthErrorMessage,
  useLoginMutation,
} from "@/features/auth/hooks";
import { useAuthStore } from "@/stores/auth-store";
import {
  academicLabel,
  listDeviceAccounts,
} from "@/stores/device-accounts";

const switchSchema = z.object({
  password: z.string().min(1, "Password is required"),
});

type SwitchForm = z.infer<typeof switchSchema>;

export default function SwitchAccountPage() {
  const currentUser = useAuthStore((s) => s.user);
  const accounts = useMemo(() => listDeviceAccounts(), []);
  const others = accounts.filter((account) => account.userId !== currentUser?.id);
  const [selectedId, setSelectedId] = useState(others[0]?.userId ?? "");
  const selected = others.find((account) => account.userId === selectedId) ?? others[0];
  const loginMutation = useLoginMutation();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<SwitchForm>({
    resolver: zodResolver(switchSchema),
    defaultValues: { password: "" },
  });

  const onSubmit = handleSubmit((values) => {
    if (!selected) return;
    loginMutation.mutate({
      user_id: selected.userId,
      password: values.password,
    });
  });

  return (
    <AppShell title="Switch Account">
      <div className="max-w-md space-y-6 text-left">
        <div>
          <h2 className="font-display text-2xl font-semibold">Switch Account</h2>
          <p className="mt-1 text-sm text-muted-foreground">
            Choose a saved student on this device. Email is not required again —
            enter that account&apos;s password only.
          </p>
        </div>

        {currentUser ? (
          <p className="rounded-xl border border-border bg-card px-3 py-2 text-sm">
            Current: <span className="font-semibold">{currentUser.full_name}</span>
          </p>
        ) : null}

        {others.length === 0 ? (
          <p className="text-sm text-muted-foreground">
            No other accounts are saved on this device yet.{" "}
            <Link href="/login" className="font-semibold text-primary">
              Add another account
            </Link>
          </p>
        ) : (
          <ul className="space-y-2">
            {others.map((account) => (
              <li key={account.userId}>
                <button
                  type="button"
                  onClick={() => setSelectedId(account.userId)}
                  className={`w-full rounded-xl border px-3 py-2 text-left text-sm ${
                    selected?.userId === account.userId
                      ? "border-primary bg-primary/10"
                      : "border-border hover:border-primary/40"
                  }`}
                >
                  <span className="block font-medium">{account.fullName}</span>
                  <span className="text-xs text-muted-foreground">
                    {academicLabel(account)}
                  </span>
                </button>
              </li>
            ))}
          </ul>
        )}

        {selected ? (
          <form onSubmit={onSubmit} className="space-y-4" noValidate>
            <p className="text-sm">
              Switching to <span className="font-semibold">{selected.fullName}</span>
            </p>
            <div>
              <label className="mb-1.5 block text-sm font-medium">Password</label>
              <input
                type="password"
                autoComplete="current-password"
                className="h-11 w-full rounded-xl border border-border bg-background px-3 text-sm outline-none ring-primary focus:ring-2"
                {...register("password")}
              />
              {errors.password ? (
                <p className="mt-1 text-xs text-destructive">{errors.password.message}</p>
              ) : null}
            </div>
            {loginMutation.isError ? (
              <p className="rounded-xl border border-destructive/30 bg-destructive/10 px-3 py-2 text-sm text-destructive">
                {getAuthErrorMessage(loginMutation.error)}
              </p>
            ) : null}
            <button
              type="submit"
              disabled={loginMutation.isPending}
              className="h-11 w-full rounded-xl bg-primary text-sm font-semibold text-primary-foreground disabled:opacity-70"
            >
              {loginMutation.isPending ? "Switching..." : "Switch Account"}
            </button>
          </form>
        ) : null}

        <Link href="/login" className="inline-block text-sm font-semibold text-primary">
          + Add another account
        </Link>
      </div>
    </AppShell>
  );
}
