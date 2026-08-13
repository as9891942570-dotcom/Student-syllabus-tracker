import { AppShell } from "@/components/layout/app-shell";
import { EmptyState } from "@/components/common/empty-state";

export function StubPage({ title }: { title: string }) {
  return (
    <AppShell title={title}>
      <EmptyState
        title={`${title} coming soon`}
        description="Route scaffolded in Phase 1. Feature module lands in a later phase."
      />
    </AppShell>
  );
}
