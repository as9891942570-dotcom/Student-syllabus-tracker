"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import { useAuthStore } from "@/stores/auth-store";

export function GuestGuard({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const accessToken = useAuthStore((s) => s.accessToken);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    setReady(true);
  }, []);

  useEffect(() => {
    if (!ready) return;
    if (accessToken) {
      router.replace("/dashboard");
    }
  }, [accessToken, ready, router]);

  if (!ready) {
    return null;
  }

  if (accessToken) {
    return null;
  }

  return <>{children}</>;
}
