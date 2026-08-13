"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  Bell,
  BookOpen,
  Flame,
  LayoutDashboard,
  ListChecks,
  Settings,
  Swords,
  Trophy,
  User,
} from "lucide-react";

import { cn } from "@/lib/utils";

const navItems = [
  { href: "/dashboard", label: "Dashboard", icon: LayoutDashboard },
  { href: "/subjects", label: "Subjects", icon: BookOpen },
  { href: "/syllabus", label: "Syllabus", icon: ListChecks },
  { href: "/quiz/history", label: "Quizzes", icon: Swords },
  { href: "/challenges", label: "Challenges", icon: Flame },
  { href: "/leaderboard", label: "Ranks", icon: Trophy },
  { href: "/notifications", label: "Alerts", icon: Bell },
  { href: "/profile", label: "Profile", icon: User },
  { href: "/settings", label: "Settings", icon: Settings },
];

export function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="hidden h-full w-64 shrink-0 flex-col border-r border-border bg-card/80 px-4 py-6 backdrop-blur md:flex">
      <Link href="/dashboard" className="mb-8 px-2">
        <span className="font-display text-2xl font-bold tracking-tight text-primary">
          EduQuest
        </span>
        <p className="mt-1 text-xs text-muted-foreground">Study. Level up.</p>
      </Link>
      <nav className="flex flex-1 flex-col gap-1">
        {navItems.map((item) => {
          const active =
            pathname === item.href || pathname.startsWith(`${item.href}/`);
          const Icon = item.icon;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={cn(
                "flex items-center gap-3 rounded-xl px-3 py-2.5 text-sm font-medium transition",
                active
                  ? "bg-primary/15 text-primary"
                  : "text-muted-foreground hover:bg-muted hover:text-foreground",
              )}
            >
              <Icon className="h-4 w-4" />
              {item.label}
            </Link>
          );
        })}
      </nav>
    </aside>
  );
}
