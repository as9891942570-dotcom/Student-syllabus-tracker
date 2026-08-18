"use client";

import { useEffect } from "react";
import { Loader2 } from "lucide-react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

import {
  getAuthErrorMessage,
  useRegisterMutation,
} from "@/features/auth/hooks";
import { PasswordInput } from "@/features/auth/password-input";
import {
  registerSchema,
  type RegisterFormValues,
} from "@/features/auth/schemas";

export function RegisterForm() {
  const registerMutation = useRegisterMutation();
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<RegisterFormValues>({
    resolver: zodResolver(registerSchema),
    defaultValues: {
      full_name: "",
      email: "",
      password: "",
      confirm_password: "",
    },
  });

  const email = watch("email");
  const password = watch("password");
  const confirmPassword = watch("confirm_password");
  const fullName = watch("full_name");

  useEffect(() => {
    if (registerMutation.isError) {
      registerMutation.reset();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps -- clear error when fields change
  }, [email, password, confirmPassword, fullName]);

  const onSubmit = handleSubmit((values) => {
    if (registerMutation.isPending) return;
    registerMutation.reset();
    registerMutation.mutate({
      full_name: values.full_name,
      email: values.email,
      password: values.password,
    });
  });

  return (
    <form onSubmit={onSubmit} className="space-y-4" noValidate>
      <div>
        <label htmlFor="full_name" className="mb-1.5 block text-sm font-medium">
          Full name
        </label>
        <input
          id="full_name"
          type="text"
          autoComplete="name"
          className="h-11 w-full rounded-xl border border-border bg-background px-3 text-sm outline-none ring-primary focus:ring-2"
          {...register("full_name")}
        />
        {errors.full_name ? (
          <p className="mt-1 text-xs text-destructive" role="alert">
            {errors.full_name.message}
          </p>
        ) : null}
      </div>

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

      <div>
        <label htmlFor="password" className="mb-1.5 block text-sm font-medium">
          Password
        </label>
        <PasswordInput
          id="password"
          autoComplete="new-password"
          {...register("password")}
        />
        {errors.password ? (
          <p className="mt-1 text-xs text-destructive" role="alert">
            {errors.password.message}
          </p>
        ) : null}
      </div>

      <div>
        <label
          htmlFor="confirm_password"
          className="mb-1.5 block text-sm font-medium"
        >
          Confirm password
        </label>
        <PasswordInput
          id="confirm_password"
          autoComplete="new-password"
          {...register("confirm_password")}
        />
        {errors.confirm_password ? (
          <p className="mt-1 text-xs text-destructive" role="alert">
            {errors.confirm_password.message}
          </p>
        ) : null}
      </div>

      {registerMutation.isError ? (
        <p
          className="rounded-xl border border-destructive/30 bg-destructive/10 px-3 py-2 text-sm text-destructive"
          role="alert"
          aria-live="polite"
        >
          {getAuthErrorMessage(registerMutation.error)}
        </p>
      ) : null}

      <button
        type="submit"
        disabled={registerMutation.isPending}
        aria-busy={registerMutation.isPending}
        className="inline-flex h-11 w-full items-center justify-center gap-2 rounded-xl bg-primary text-sm font-semibold text-primary-foreground transition hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-70"
      >
        {registerMutation.isPending ? (
          <>
            <Loader2 className="h-4 w-4 animate-spin" aria-hidden="true" />
            Creating account...
          </>
        ) : (
          "Create account"
        )}
      </button>
    </form>
  );
}
