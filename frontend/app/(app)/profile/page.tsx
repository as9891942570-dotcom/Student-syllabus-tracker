"use client";

import Link from "next/link";

import { AppShell } from "@/components/layout/app-shell";
import { Skeleton } from "@/components/common/skeleton";
import { ProfileCompletionBar } from "@/features/profile/completion-bar";
import { useProfileQuery } from "@/features/profile/hooks";
import { resolveMediaUrl } from "@/lib/api";

export default function ProfileViewPage() {
  const profileQuery = useProfileQuery();

  if (profileQuery.isLoading) {
    return (
      <AppShell title="Profile">
        <Skeleton className="h-64 w-full max-w-2xl" />
      </AppShell>
    );
  }

  if (!profileQuery.data) {
    return (
      <AppShell title="Profile">
        <p className="text-sm text-destructive">Unable to load profile.</p>
      </AppShell>
    );
  }

  const profile = profileQuery.data;
  const photo = resolveMediaUrl(profile.photo_url);

  return (
    <AppShell title="Profile">
      <div className="mx-auto w-full max-w-2xl space-y-6">
        <div className="flex flex-wrap items-start justify-between gap-4">
          <div className="flex items-center gap-4">
            <div className="flex h-20 w-20 items-center justify-center overflow-hidden rounded-full border border-border bg-muted">
              {photo ? (
                // eslint-disable-next-line @next/next/no-img-element
                <img
                  src={photo}
                  alt={profile.full_name}
                  className="h-full w-full object-cover"
                />
              ) : (
                <span className="text-xs text-muted-foreground">No photo</span>
              )}
            </div>
            <div>
              <h2 className="font-display text-2xl font-semibold">
                {profile.full_name}
              </h2>
              <p className="text-sm text-muted-foreground">{profile.email}</p>
            </div>
          </div>
          <Link
            href="/profile/edit"
            className="rounded-full bg-primary px-4 py-2 text-sm font-semibold text-primary-foreground"
          >
            Edit profile
          </Link>
        </div>

        <ProfileCompletionBar percentage={profile.completion_percentage} />

        {!profile.is_complete ? (
          <div className="rounded-xl border border-warning/30 bg-warning/10 px-4 py-3 text-sm">
            Finish your profile to unlock the dashboard.{" "}
            <Link href="/profile/setup" className="font-semibold text-primary">
              Continue setup
            </Link>
          </div>
        ) : null}

        <dl className="grid gap-4 rounded-2xl border border-border bg-card p-5 sm:grid-cols-2">
          <Item label="Mobile" value={profile.mobile ?? "—"} />
          <Item label="Board" value={profile.board?.name ?? "—"} />
          <Item label="Class" value={profile.school_class?.name ?? "—"} />
          <Item
            label="Stream"
            value={
              profile.school_class?.requires_stream
                ? (profile.stream?.name ?? "—")
                : "Not applicable"
            }
          />
        </dl>
      </div>
    </AppShell>
  );
}

function Item({ label, value }: { label: string; value: string }) {
  return (
    <div>
      <dt className="text-xs uppercase tracking-wide text-muted-foreground">
        {label}
      </dt>
      <dd className="mt-1 font-medium text-foreground">{value}</dd>
    </div>
  );
}
