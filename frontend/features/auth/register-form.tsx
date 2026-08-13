"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

import {
  getAuthErrorMessage,
  useRegisterMutation,
} from "@/features/auth/hooks";
import {
  registerSchema,
  type RegisterFormValues,
} from "@/features/auth/schemas";

export function RegisterForm() {
  const registerMutation = useRegisterMutation();
  const {
    register,
    handleSubmit,
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

  const onSubmit = handleSubmit((values) => {
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
          <p className="mt-1 text-xs text-destructive">
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
          <p className="mt-1 text-xs text-destructive">{errors.email.message}</p>
        ) : null}
      </div>

      <div>
        <label htmlFor="password" className="mb-1.5 block text-sm font-medium">
          Password
        </label>
        <input
          id="password"
          type="password"
          autoComplete="new-password"
          className="h-11 w-full rounded-xl border border-border bg-background px-3 text-sm outline-none ring-primary focus:ring-2"
          {...register("password")}
        />
        {errors.password ? (
          <p className="mt-1 text-xs text-destructive">
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
        <input
          id="confirm_password"
          type="password"
          autoComplete="new-password"
          className="h-11 w-full rounded-xl border border-border bg-background px-3 text-sm outline-none ring-primary focus:ring-2"
          {...register("confirm_password")}
        />
        {errors.confirm_password ? (
          <p className="mt-1 text-xs text-destructive">
            {errors.confirm_password.message}
          </p>
        ) : null}
      </div>

      {registerMutation.isError ? (
        <p className="rounded-xl border border-destructive/30 bg-destructive/10 px-3 py-2 text-sm text-destructive">
          {getAuthErrorMessage(registerMutation.error)}
        </p>
      ) : null}

      <button
        type="submit"
        disabled={registerMutation.isPending}
        className="h-11 w-full rounded-xl bg-primary text-sm font-semibold text-primary-foreground transition hover:brightness-110 disabled:cursor-not-allowed disabled:opacity-70"
      >
        {registerMutation.isPending ? "Creating account..." : "Create account"}
      </button>
    </form>
  );
}
