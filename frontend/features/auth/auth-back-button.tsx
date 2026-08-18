"use client";

import { ArrowLeft } from "lucide-react";
import { useRouter } from "next/navigation";

const PUBLIC_AUTH_PATHS = new Set([
  "/",
  "/login",
  "/register",
  "/forgot-password",
]);

function sameOriginPublicPreviousPath(): string | null {
  if (typeof window === "undefined") return null;
  const referrer = document.referrer;
  if (!referrer) return null;
  try {
    const url = new URL(referrer);
    if (url.origin !== window.location.origin) return null;
    if (!PUBLIC_AUTH_PATHS.has(url.pathname)) return null;
    if (url.pathname === window.location.pathname) return null;
    return url.pathname + url.search + url.hash;
  } catch {
    return null;
  }
}

export function AuthBackButton({ fallback = "/" }: { fallback?: string }) {
  const router = useRouter();

  const onBack = () => {
    const previous = sameOriginPublicPreviousPath();
    if (previous) {
      router.back();
      return;
    }
    router.push(fallback);
  };

  return (
    <button
      type="button"
      onClick={onBack}
      className="mb-4 inline-flex items-center gap-1.5 text-sm font-semibold text-muted-foreground transition hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary"
      aria-label="Back"
    >
      <ArrowLeft className="h-4 w-4" aria-hidden="true" />
      Back
    </button>
  );
}
