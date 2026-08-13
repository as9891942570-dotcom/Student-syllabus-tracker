import { AuthGuard } from "@/features/auth/auth-guard";
import { ProfileCompletionGuard } from "@/features/profile/profile-completion-guard";

export default function AppGroupLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <AuthGuard>
      <ProfileCompletionGuard>{children}</ProfileCompletionGuard>
    </AuthGuard>
  );
}
