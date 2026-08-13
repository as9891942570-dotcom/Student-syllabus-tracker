"use client";

import { useQuery } from "@tanstack/react-query";
import { motion } from "framer-motion";

import { Skeleton } from "@/components/common/skeleton";
import { apiFetch } from "@/lib/api";
import { queryKeys } from "@/lib/query-keys";
import type { HealthResponse } from "@/types/api";
import { cn } from "@/lib/utils";

export function ApiHealthBadge() {
  const { data, isLoading, isError } = useQuery({
    queryKey: queryKeys.health,
    queryFn: () => apiFetch<HealthResponse>("/health"),
    refetchInterval: 30_000,
  });

  if (isLoading) {
    return <Skeleton className="h-8 w-40 rounded-full" />;
  }

  const healthy = data?.status === "healthy";
  const label = isError
    ? "API offline"
    : healthy
      ? "API healthy"
      : "API degraded";

  return (
    <motion.div
      initial={{ opacity: 0, y: 6 }}
      animate={{ opacity: 1, y: 0 }}
      className={cn(
        "inline-flex items-center gap-2 rounded-full border px-3 py-1.5 text-xs font-semibold",
        isError || !healthy
          ? "border-warning/40 bg-warning/10 text-warning"
          : "border-success/40 bg-success/10 text-success",
      )}
    >
      <span
        className={cn(
          "h-2 w-2 rounded-full",
          isError || !healthy ? "bg-warning" : "bg-success",
        )}
      />
      {label}
      {data ? (
        <span className="font-normal text-muted-foreground">
          v{data.version}
        </span>
      ) : null}
    </motion.div>
  );
}
