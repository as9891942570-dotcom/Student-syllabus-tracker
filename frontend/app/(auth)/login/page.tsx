import Link from "next/link";

import { GuestGuard } from "@/features/auth/guest-guard";
import { LoginForm } from "@/features/auth/login-form";

export default function LoginPage() {
  return (
    <GuestGuard>
      <div className="rounded-2xl border border-border bg-card p-6 shadow-glow">
        <h1 className="font-display text-2xl font-bold">Welcome back</h1>
        <p className="mt-2 text-sm text-muted-foreground">
          Log in to continue your syllabus quest.
        </p>
        <div className="mt-6">
          <LoginForm />
        </div>
        <p className="mt-4 text-sm text-muted-foreground">
          No account?{" "}
          <Link href="/register" className="font-semibold text-primary">
            Register
          </Link>
        </p>
      </div>
    </GuestGuard>
  );
}
