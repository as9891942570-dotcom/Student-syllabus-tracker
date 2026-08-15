"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

import {
  getAuthErrorMessage,
  useLoginMutation,
} from "@/features/auth/hooks";
import { loginSchema, type LoginFormValues } from "@/features/auth/schemas";
import { academicLabel, listDeviceAccounts } from "@/stores/device-accounts";

export function LoginForm() {
  const loginMutation = useLoginMutation();
  const deviceAccounts = useMemo(() => listDeviceAccounts(), []);
  const [selectedUserId, setSelectedUserId] = useState<string | null>(null);
  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm<LoginFormValues>({
    resolver: zodResolver(loginSchema),
    defaultValues: { email: "", password: "" },
  });

  const selected = deviceAccounts.find((account) => account.userId === selectedUserId);

  const onSubmit = handleSubmit((values) => {
    if (selected) {
      loginMutation.mutate({
        user_id: selected.userId,
        password: values.password,
      });
      return;
    }
    loginMutation.mutate(values);
  });

  return (
    <form onSubmit={onSubmit} className="space-y-4" noValidate>
      {deviceAccounts.length ? (
        <div>
          <p className="mb-2 text-xs font-medium uppercase tracking-wide text-muted-foreground">
            Accounts on this device
          </p>
          <ul className="mb-3 space-y-1">
            {deviceAccounts.map((account) => (
              <li key={account.userId}>
                <button
                  type="button"
                  onClick={() => {
                    const next =
                      selectedUserId === account.userId ? null : account.userId;
                    setSelectedUserId(next);
                    setValue("email", next ? account.email : "", {
                      shouldValidate: true,
                    });
                  }}
                  className="w-full rounded-lg border border-border px-3 py-2 text-left text-sm hover:border-primary/40"
                >
                  <span className="block font-medium">{account.fullName}</span>
                  <span className="text-xs text-muted-foreground">
                    {academicLabel(account)}
                  </span>
                </button>
              </li>
            ))}
          </ul>
        </div>
      ) : null}

      {selected ? (
        <p className="rounded-xl border border-primary/30 bg-primary/5 px-3 py-2 text-sm">
          Signing in as <span className="font-semibold">{selected.fullName}</span>
          {" · "}
          {academicLabel(selected)}
        </p>
      ) : (
      <div>
        <label htmlFor="email" className="mb-1.5 block text-sm font-medium">
          Email
        </label>
        <input
          id="email"
          type="email"
          autoComplete="email"
          className="h-11 w-full rounded-xl border border-border bg-background px-3 text-sm outline-none ring-primary focus:ring-2"
          {...register("email")}
        />
        {errors.email ? (
          <p className="mt-1 text-xs text-destructive">{errors.email.message}</p>
        ) : null}
      </div>
      )}

      <div>
        <div className="mb-1.5 flex items-center justify-between">
          <label htmlFor="password" className="block text-sm font-medium">
            Password
          </label>
          <Link
            href="/forgot-password"
            className="text-xs font-medium text-primary hover:underline"
          >
            Forgot password?
          </Link>
        </div>
        <input
          id="password"
          type="password"
          autoComplete="current-password"
          className="h-11 w-full rounded-xl border border-border bg-background px-3 text-sm outline-none ring-primary focus:ring-2"
          {...register("password")}
        />
        {errors.password ? (
          <p className="mt-1 text-xs text-destructive">
            {errors.password.message}
          </p>
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
        className="h-11 w-full rounded-xl bg-primary text-sm font-semibold text-primary-foreground transition hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-70"
      >
        {loginMutation.isPending ? "Signing in..." : "Log in"}
      </button>
    </form>
  );
}
