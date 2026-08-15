"use client";

import { useEffect } from "react";
import { MobileBottomNav } from "@/components/layout/mobile-bottom-nav";
import { Sidebar } from "@/components/layout/sidebar";
import { TopBar } from "@/components/layout/top-bar";
import { useProfileQuery } from "@/features/profile/hooks";
import { useAuthStore } from "@/stores/auth-store";
import { rememberDeviceAccount } from "@/stores/device-accounts";

export function AppShell({
  children,
  title,
}: {
  children: React.ReactNode;
  title: string;
}) {
  const profileQuery = useProfileQuery();
  const user = useAuthStore((s) => s.user);
  const xp = profileQuery.data?.total_xp ?? 0;
  const coins = profileQuery.data?.total_coins ?? 0;
  const level = profileQuery.data?.level ?? 1;

  useEffect(() => {
    if (!user || !profileQuery.data) return;
    rememberDeviceAccount(user, {
      className: profileQuery.data.school_class?.name,
      streamName: profileQuery.data.stream?.name,
      boardName: profileQuery.data.board?.name,
    });
  }, [user, profileQuery.data]);

  return (
    <div className="flex min-h-screen bg-background">
      <Sidebar />
      <div className="flex min-h-screen flex-1 flex-col">
        <TopBar title={title} xp={xp} level={level} coins={coins} />
        <main className="flex-1 px-4 py-6 pb-24 md:px-6 md:pb-8">{children}</main>
        <MobileBottomNav />
      </div>
    </div>
  );
}
