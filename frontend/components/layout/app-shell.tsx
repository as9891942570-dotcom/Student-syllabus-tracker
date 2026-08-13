"use client";

import { MobileBottomNav } from "@/components/layout/mobile-bottom-nav";
import { Sidebar } from "@/components/layout/sidebar";
import { TopBar } from "@/components/layout/top-bar";
import { useProfileQuery } from "@/features/profile/hooks";

export function AppShell({
  children,
  title,
}: {
  children: React.ReactNode;
  title: string;
}) {
  const profileQuery = useProfileQuery();
  const xp = profileQuery.data?.total_xp ?? 0;

  return (
    <div className="flex min-h-screen bg-background">
      <Sidebar />
      <div className="flex min-h-screen flex-1 flex-col">
        <TopBar title={title} xp={xp} />
        <main className="flex-1 px-4 py-6 pb-24 md:px-6 md:pb-8">{children}</main>
        <MobileBottomNav />
      </div>
    </div>
  );
}
