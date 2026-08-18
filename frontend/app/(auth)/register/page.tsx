import Link from "next/link";

import { AuthBackButton } from "@/features/auth/auth-back-button";
import { GuestGuard } from "@/features/auth/guest-guard";
import { RegisterForm } from "@/features/auth/register-form";

export default function RegisterPage() {
  return (
    <GuestGuard>
      <div className="rounded-2xl border border-border bg-card p-6 shadow-glow">
        <AuthBackButton />
        <h1 className="font-display text-2xl font-bold">Create your quest</h1>
        <p className="mt-2 text-sm text-muted-foreground">
          Join EduQuest and start tracking your syllabus progress.
        </p>
        <div className="mt-6">
          <RegisterForm />
        </div>
        <p className="mt-4 text-sm text-muted-foreground">
          Already studying?{" "}
          <Link href="/login" className="font-semibold text-primary">
            Log in
          </Link>
        </p>
      </div>
    </GuestGuard>
  );
}
