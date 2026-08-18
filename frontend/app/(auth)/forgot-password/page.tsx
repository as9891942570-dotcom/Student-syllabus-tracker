"use client";

import { useState } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import Link from "next/link";

import { GuestGuard } from "@/features/auth/guest-guard";
import { AuthBackButton } from "@/features/auth/auth-back-button";
import { authApi, ApiError } from "@/lib/api";

const schema = z.object({
  email: z.string().email("Enter a valid email"),
});

type FormValues = z.infer<typeof schema>;

export default function ForgotPasswordPage() {
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: { email: "" },
  });

  const onSubmit = handleSubmit(async (values) => {
    setError(null);
    setMessage(null);
    try {
      const result = await authApi.forgotPassword(values.email);
      setMessage(result.message);
    } catch (err) {
      setError(
        err instanceof ApiError ? err.message : "Unable to submit request",
      );
    }
  });

  return (
    <GuestGuard>
      <div className="rounded-2xl border border-border bg-card p-6 shadow-glow">
        <AuthBackButton fallback="/login" />
        <h1 className="font-display text-2xl font-bold">Forgot password</h1>
        <p className="mt-2 text-sm text-muted-foreground">
          Email-based password reset is not available yet. Submitting this form
          will not send an email.
        </p>
        <form onSubmit={onSubmit} className="mt-6 space-y-4" noValidate>
          <div>
            <label htmlFor="email" className="mb-1.5 block text-sm font-medium">
              Email
            </label>
            <input
              id="email"
              type="email"
              className="h-11 w-full rounded-xl border border-border bg-background px-3 text-sm outline-none ring-primary focus:ring-2"
              {...register("email")}
            />
            {errors.email ? (
              <p className="mt-1 text-xs text-destructive">
                {errors.email.message}
              </p>
            ) : null}
          </div>
          {error ? (
            <p className="rounded-xl border border-destructive/30 bg-destructive/10 px-3 py-2 text-sm text-destructive">
              {error}
            </p>
          ) : null}
          {message ? (
            <p className="rounded-xl border border-success/30 bg-success/10 px-3 py-2 text-sm text-success">
              {message}
            </p>
          ) : null}
          <button
            type="submit"
            disabled={isSubmitting}
            className="h-11 w-full rounded-xl bg-primary text-sm font-semibold text-primary-foreground disabled:opacity-70"
          >
            {isSubmitting ? "Submitting..." : "Submit"}
          </button>
        </form>
        <p className="mt-4 text-sm text-muted-foreground">
          <Link href="/login" className="font-semibold text-primary">
            Back to login
          </Link>
        </p>
      </div>
    </GuestGuard>
  );
}
