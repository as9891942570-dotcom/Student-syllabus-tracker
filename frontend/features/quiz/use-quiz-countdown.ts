"use client";

import { useEffect, useRef, useState } from "react";

/**
 * Backend returns UTC datetimes without a timezone suffix.
 * Browsers treat those as local time, which makes the quiz look expired in
 * timezones ahead of UTC (e.g. IST) and triggers an immediate /complete.
 */
export function parseQuizApiDate(value: string): Date {
  const trimmed = value.trim();
  const hasTimezone = /[zZ]$|[+-]\d{2}:?\d{2}$/.test(trimmed);
  if (
    !hasTimezone &&
    /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}/.test(trimmed)
  ) {
    return new Date(`${trimmed}Z`);
  }
  return new Date(trimmed);
}

/** Client countdown from backend expires_at; backend remains source of truth. */
export function useQuizCountdown(
  expiresAt: string | undefined,
  active: boolean,
) {
  // null = not ready yet (avoids treating an uninitialized value as "expired")
  const [secondsRemaining, setSecondsRemaining] = useState<number | null>(null);

  useEffect(() => {
    if (!expiresAt || !active) {
      setSecondsRemaining(null);
      return;
    }

    const tick = () => {
      const remaining = Math.max(
        0,
        Math.floor(
          (parseQuizApiDate(expiresAt).getTime() - Date.now()) / 1000,
        ),
      );
      setSecondsRemaining(remaining);
    };

    tick();
    const id = window.setInterval(tick, 1000);
    return () => window.clearInterval(id);
  }, [expiresAt, active]);

  return secondsRemaining;
}

export function formatCountdown(totalSeconds: number | null): string {
  if (totalSeconds === null) return "--:--";
  const m = Math.floor(totalSeconds / 60);
  const s = totalSeconds % 60;
  return `${m}:${s.toString().padStart(2, "0")}`;
}

/**
 * Auto-complete only after the timer has been observed as positive and then
 * reaches 0. Prevents duplicate /complete calls.
 */
export function useQuizExpiryComplete(
  secondsRemaining: number | null,
  active: boolean,
  onExpire: () => void,
) {
  const seenPositiveRef = useRef(false);
  const completedRef = useRef(false);

  useEffect(() => {
    if (!active) {
      seenPositiveRef.current = false;
      completedRef.current = false;
      return;
    }

    if (secondsRemaining === null) return;

    if (secondsRemaining > 0) {
      seenPositiveRef.current = true;
      return;
    }

    // secondsRemaining === 0
    if (!seenPositiveRef.current) return;
    if (completedRef.current) return;
    completedRef.current = true;
    onExpire();
  }, [secondsRemaining, active, onExpire]);
}
