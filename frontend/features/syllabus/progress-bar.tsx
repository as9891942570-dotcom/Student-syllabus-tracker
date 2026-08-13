import { cn } from "@/lib/utils";

export function ProgressBar({
  percentage,
  className,
  size = "md",
}: {
  percentage: number;
  className?: string;
  size?: "sm" | "md";
}) {
  const value = Math.max(0, Math.min(100, percentage));
  return (
    <div className={cn("space-y-1.5", className)}>
      <div className="flex items-center justify-between text-xs">
        <span className="text-muted-foreground">Progress</span>
        <span className="font-semibold text-primary">{value}%</span>
      </div>
      <div
        className={cn(
          "overflow-hidden rounded-full bg-muted",
          size === "sm" ? "h-1.5" : "h-2.5",
        )}
      >
        <div
          className="h-full rounded-full bg-primary transition-all duration-300"
          style={{ width: `${value}%` }}
        />
      </div>
    </div>
  );
}
