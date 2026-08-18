import Link from "next/link";

import { ThemeToggle } from "@/components/common/theme-toggle";

export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen bg-hero-grid">
      <div className="mx-auto flex w-full min-w-0 max-w-md flex-col px-4 py-8">
        <div className="mb-8 flex items-center justify-between">
          <Link
            href="/"
            className="font-display text-2xl font-bold text-primary"
          >
            EduQuest
          </Link>
          <ThemeToggle />
        </div>
        {children}
      </div>
    </div>
  );
}
