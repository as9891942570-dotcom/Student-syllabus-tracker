"use client";

import { useEffect } from "react";
import { usePathname, useRouter } from "next/navigation";

import { Skeleton } from "@/components/common/skeleton";
import { useProfileQuery } from "@/features/profile/hooks";

const PROFILE_ALLOWLIST = ["/profile/setup", "/profile/edit"];

export function ProfileCompletionGuard({
  children,
}: {
  children: React.ReactNode;
}) {
  const router = useRouter();
  const pathname = usePathname();
  const profileQuery = useProfileQuery();

  const allowedIncomplete =
    PROFILE_ALLOWLIST.some(
      (path) => pathname === path || pathname.startsWith(`${path}/`),
    ) || pathname === "/profile";

  useEffect(() => {
    if (!profileQuery.data) return;
    if (!profileQuery.data.is_complete && !allowedIncomplete) {
      router.replace("/profile/setup");
    }
  }, [allowedIncomplete, profileQuery.data, router]);

  if (profileQuery.isLoading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-background px-4">
        <div className="w-full max-w-md space-y-3">
          <Skeleton className="h-8 w-48" />
          <Skeleton className="h-4 w-full" />
          <Skeleton className="h-32 w-full" />
        </div>
      </div>
    );
  }

  if (profileQuery.isError) {
    return (
      <div className="flex min-h-screen items-center justify-center px-4 text-center">
        <div>
          <h2 className="font-display text-xl font-semibold">
            Could not load profile
          </h2>
          <p className="mt-2 text-sm text-muted-foreground">
            Check that the API is running, then refresh.
          </p>
          <button
            type="button"
            className="mt-4 rounded-full bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground"
            onClick={() => profileQuery.refetch()}
          >
            Retry
          </button>
        </div>
      </div>
    );
  }

  if (
    profileQuery.data &&
    !profileQuery.data.is_complete &&
    !allowedIncomplete
  ) {
    return null;
  }

  return <>{children}</>;
}
