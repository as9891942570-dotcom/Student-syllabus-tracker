"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";

import { AppShell } from "@/components/layout/app-shell";
import { Skeleton } from "@/components/common/skeleton";
import { ProfileForm } from "@/features/profile/profile-form";
import { useProfileQuery } from "@/features/profile/hooks";

export default function ProfileEditPage() {
  const router = useRouter();
  const profileQuery = useProfileQuery();

  if (profileQuery.isLoading || !profileQuery.data) {
    return (
      <AppShell title="Edit profile">
        <Skeleton className="h-64 w-full max-w-2xl" />
      </AppShell>
    );
  }

  return (
    <AppShell title="Edit profile">
      <div className="mx-auto w-full max-w-2xl space-y-4">
        <div className="flex items-center justify-between gap-3">
          <div>
            <h2 className="font-display text-2xl font-semibold">Edit profile</h2>
            <p className="mt-1 text-sm text-muted-foreground">
              Update your name, mobile, and photo. Board, class, and stream stay
              locked after setup.
            </p>
          </div>
          <Link
            href="/profile"
            className="text-sm font-semibold text-primary hover:underline"
          >
            Cancel
          </Link>
        </div>
        <ProfileForm
          profile={profileQuery.data}
          submitLabel="Save changes"
          onSuccess={() => router.replace("/profile")}
        />
      </div>
    </AppShell>
  );
}
