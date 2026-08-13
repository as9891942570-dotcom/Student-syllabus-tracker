"use client";

import { useEffect } from "react";
import Link from "next/link";

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <html lang="en">
      <body className="flex min-h-screen items-center justify-center bg-background px-4 text-foreground">
        <div className="max-w-md text-center">
          <h1 className="font-display text-3xl font-bold">Something broke</h1>
          <p className="mt-3 text-muted-foreground">
            An unexpected error occurred. Try again or head home.
          </p>
          <div className="mt-6 flex justify-center gap-3">
            <button
              type="button"
              onClick={reset}
              className="rounded-full bg-primary px-5 py-2.5 text-sm font-semibold text-primary-foreground"
            >
              Try again
            </button>
            <Link
              href="/"
              className="rounded-full border border-border px-5 py-2.5 text-sm font-semibold"
            >
              Home
            </Link>
          </div>
        </div>
      </body>
    </html>
  );
}
