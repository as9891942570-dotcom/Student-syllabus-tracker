import { cn } from "@/lib/utils";

export function ProfileCompletionBar({
  percentage,
  className,
}: {
  percentage: number;
  className?: string;
}) {
  const value = Math.max(0, Math.min(100, percentage));
  return (
    <div className={cn("space-y-2", className)}>
      <div className="flex items-center justify-between text-sm">
        <span className="font-medium text-foreground">Profile completion</span>
        <span className="font-semibold text-primary">{value}%</span>
      </div>
      <div className="h-2.5 overflow-hidden rounded-full bg-muted">
        <div
          className="h-full rounded-full bg-primary transition-all duration-500"
          style={{ width: `${value}%` }}
        />
      </div>
    </div>
  );
}
