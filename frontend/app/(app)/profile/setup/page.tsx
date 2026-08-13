"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";

import { AppShell } from "@/components/layout/app-shell";
import { Skeleton } from "@/components/common/skeleton";
import { ProfileCompletionBar } from "@/features/profile/completion-bar";
import { ProfileForm } from "@/features/profile/profile-form";
import { useProfileQuery } from "@/features/profile/hooks";

export default function ProfileSetupPage() {
  const router = useRouter();
  const profileQuery = useProfileQuery();

  if (profileQuery.isLoading) {
    return (
      <AppShell title="Profile setup">
        <Skeleton className="h-64 w-full max-w-2xl" />
      </AppShell>
    );
  }

  if (!profileQuery.data) {
    return (
      <AppShell title="Profile setup">
        <p className="text-sm text-destructive">Unable to load profile.</p>
      </AppShell>
    );
  }

  if (profileQuery.data.is_complete) {
    return (
      <AppShell title="Profile setup">
        <div className="max-w-xl space-y-4">
          <ProfileCompletionBar percentage={100} />
          <p className="text-sm text-muted-foreground">
            Your profile is already complete.
          </p>
          <div className="flex gap-3">
            <Link
              href="/profile"
              className="rounded-full bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground"
            >
              View profile
            </Link>
            <Link
              href="/dashboard"
              className="rounded-full border border-border px-4 py-2 text-sm font-semibold"
            >
              Go to dashboard
            </Link>
          </div>
        </div>
      </AppShell>
    );
  }

  return (
    <AppShell title="Profile setup">
      <div className="mx-auto w-full max-w-2xl space-y-4">
        <div>
          <h2 className="font-display text-2xl font-semibold">
            Complete your student profile
          </h2>
          <p className="mt-1 text-sm text-muted-foreground">
            Dashboard unlocks after your profile is 100% complete.
          </p>
        </div>
        <ProfileForm
          profile={profileQuery.data}
          submitLabel="Save and continue"
          onSuccess={(updated) => {
            if (updated.is_complete) {
              router.replace("/dashboard");
            } else {
              profileQuery.refetch();
            }
          }}
        />
      </div>
    </AppShell>
  );
}
