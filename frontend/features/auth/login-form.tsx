"use client";

import { useEffect, useMemo, useState } from "react";
import Link from "next/link";
import { Loader2 } from "lucide-react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

import {
  getAuthErrorMessage,
  useLoginMutation,
} from "@/features/auth/hooks";
import { PasswordInput } from "@/features/auth/password-input";
import { loginSchema, type LoginFormValues } from "@/features/auth/schemas";
import { academicLabel, listDeviceAccounts } from "@/stores/device-accounts";
import { ApiError } from "@/lib/api";

function loginErrorMessage(error: unknown): string {
  if (error instanceof ApiError && error.status === 401) {
    return "Invalid email or password";
  }
  return getAuthErrorMessage(error);
}

export function LoginForm() {
  const loginMutation = useLoginMutation();
  const deviceAccounts = useMemo(() => listDeviceAccounts(), []);
  const [selectedUserId, setSelectedUserId] = useState<string | null>(null);
  const {
    register,
    handleSubmit,
    setValue,
    watch,
    formState: { errors },
  } = useForm<LoginFormValues>({
    resolver: zodResolver(loginSchema),
    defaultValues: { email: "", password: "" },
  });

  const email = watch("email");
  const password = watch("password");
  const selected = deviceAccounts.find((account) => account.userId === selectedUserId);

  useEffect(() => {
    if (loginMutation.isError) {
      loginMutation.reset();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps -- clear error when credentials change
  }, [email, password, selectedUserId]);

  const onSubmit = handleSubmit((values) => {
    if (loginMutation.isPending) return;
    loginMutation.reset();
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
                      shouldValidate: Boolean(next),
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
            <p className="mt-1 text-xs text-destructive" role="alert">
              {errors.email.message}
            </p>
          ) : null}
        </div>
      )}

      <div>
        <div className="mb-1.5 flex items-center justify-between gap-2">
          <label htmlFor="password" className="block text-sm font-medium">
            Password
          </label>
          <Link
            href="/forgot-password"
            className="shrink-0 text-xs font-medium text-primary hover:underline"
          >
            Forgot password?
          </Link>
        </div>
        <PasswordInput
          id="password"
          autoComplete="current-password"
          {...register("password")}
        />
        {errors.password ? (
          <p className="mt-1 text-xs text-destructive" role="alert">
            {errors.password.message}
          </p>
        ) : null}
      </div>

      {loginMutation.isError ? (
        <p
          className="rounded-xl border border-destructive/30 bg-destructive/10 px-3 py-2 text-sm text-destructive"
          role="alert"
          aria-live="polite"
        >
          {loginErrorMessage(loginMutation.error)}
        </p>
      ) : null}

      <button
        type="submit"
        disabled={loginMutation.isPending}
        aria-busy={loginMutation.isPending}
        className="inline-flex h-11 w-full items-center justify-center gap-2 rounded-xl bg-primary text-sm font-semibold text-primary-foreground transition hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-70"
      >
        {loginMutation.isPending ? (
          <>
            <Loader2 className="h-4 w-4 animate-spin" aria-hidden="true" />
            Signing in...
          </>
        ) : (
          "Log in"
        )}
      </button>
    </form>
  );
}
