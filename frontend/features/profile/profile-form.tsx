"use client";

import { useMemo, useState } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

import { ProfileCompletionBar } from "@/features/profile/completion-bar";
import {
  getProfileErrorMessage,
  useBoardsQuery,
  useClassesQuery,
  useProfileQuery,
  useStreamsQuery,
  useUpdateProfileMutation,
  useUploadPhotoMutation,
} from "@/features/profile/hooks";
import {
  profileFormSchema,
  type ProfileFormValues,
} from "@/features/profile/schemas";
import { resolveMediaUrl } from "@/lib/api";
import type { Profile } from "@/types/profile";
import { cn } from "@/lib/utils";

type Props = {
  profile: Profile;
  submitLabel: string;
  onSuccess?: (profile: Profile) => void;
};

export function ProfileForm({ profile, submitLabel, onSuccess }: Props) {
  const boardsQuery = useBoardsQuery();
  const classesQuery = useClassesQuery();
  const streamsQuery = useStreamsQuery();
  const liveProfileQuery = useProfileQuery();
  const updateMutation = useUpdateProfileMutation();
  const photoMutation = useUploadPhotoMutation();
  const [photoPreview, setPhotoPreview] = useState<string | null>(
    resolveMediaUrl(profile.photo_url),
  );
  const [localError, setLocalError] = useState<string | null>(null);

  const initialClassId = profile.school_class?.id ?? "";
  const {
    register,
    handleSubmit,
    watch,
    setValue,
    formState: { errors },
  } = useForm<ProfileFormValues>({
    resolver: zodResolver(profileFormSchema),
    defaultValues: {
      full_name: profile.full_name ?? "",
      mobile: profile.mobile ?? "",
      board_id: profile.board?.id ?? "",
      class_id: initialClassId,
      stream_id: profile.stream?.id ?? "",
      requires_stream: profile.school_class?.requires_stream ?? false,
    },
  });

  const classId = watch("class_id");
  const requiresStream = watch("requires_stream");

  const selectedClass = useMemo(
    () => classesQuery.data?.find((item) => item.id === classId),
    [classesQuery.data, classId],
  );

  const onClassChange = (value: string) => {
    setValue("class_id", value, { shouldValidate: true });
    const next = classesQuery.data?.find((item) => item.id === value);
    const needsStream = Boolean(next?.requires_stream);
    setValue("requires_stream", needsStream, { shouldValidate: true });
    if (!needsStream) {
      setValue("stream_id", "", { shouldValidate: true });
    }
  };

  const onPhotoChange = async (fileList: FileList | null) => {
    const file = fileList?.[0];
    if (!file) return;
    setLocalError(null);
    try {
      const updated = await photoMutation.mutateAsync(file);
      setPhotoPreview(resolveMediaUrl(updated.photo_url));
      onSuccess?.(updated);
    } catch (error) {
      setLocalError(getProfileErrorMessage(error));
    }
  };

  const onSubmit = handleSubmit(async (values) => {
    setLocalError(null);
    try {
      const updated = await updateMutation.mutateAsync({
        full_name: values.full_name,
        mobile: values.mobile,
        board_id: values.board_id,
        class_id: values.class_id,
        stream_id: values.requires_stream ? values.stream_id || undefined : undefined,
        clear_stream: !values.requires_stream,
      });
      onSuccess?.(updated);
    } catch (error) {
      setLocalError(getProfileErrorMessage(error));
    }
  });

  const loadingLookups =
    boardsQuery.isLoading || classesQuery.isLoading || streamsQuery.isLoading;
  const lookupError =
    boardsQuery.isError || classesQuery.isError || streamsQuery.isError;

  // Prefer live profile completion from query cache after mutations
  const completion =
    liveProfileQuery.data?.completion_percentage ?? profile.completion_percentage;

  return (
    <form onSubmit={onSubmit} className="space-y-6" noValidate>
      <ProfileCompletionBar percentage={completion} />

      <div className="flex flex-col items-start gap-4 sm:flex-row sm:items-center">
        <div className="flex h-24 w-24 items-center justify-center overflow-hidden rounded-full border border-border bg-muted">
          {photoPreview ? (
            // eslint-disable-next-line @next/next/no-img-element
            <img
              src={photoPreview}
              alt="Profile"
              className="h-full w-full object-cover"
            />
          ) : (
            <span className="text-xs text-muted-foreground">No photo</span>
          )}
        </div>
        <div>
          <label className="inline-flex cursor-pointer rounded-full border border-border bg-card px-4 py-2 text-sm font-semibold hover:border-primary/40">
            {photoMutation.isPending ? "Uploading..." : "Upload photo"}
            <input
              type="file"
              accept="image/png,image/jpeg,image/webp"
              className="hidden"
              onChange={(e) => onPhotoChange(e.target.files)}
            />
          </label>
          <p className="mt-2 text-xs text-muted-foreground">
            JPEG, PNG, or WebP up to 2MB
          </p>
        </div>
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        <Field label="Full name" error={errors.full_name?.message}>
          <input
            className={inputClass}
            {...register("full_name")}
            autoComplete="name"
          />
        </Field>
        <Field label="Mobile" error={errors.mobile?.message}>
          <input
            className={inputClass}
            {...register("mobile")}
            inputMode="numeric"
            autoComplete="tel"
          />
        </Field>
      </div>

      {loadingLookups ? (
        <p className="text-sm text-muted-foreground">Loading boards and classes...</p>
      ) : null}
      {lookupError ? (
        <p className="text-sm text-destructive">
          Could not load academic options. Try refreshing.
        </p>
      ) : null}

      <div className="grid gap-4 md:grid-cols-2">
        <Field label="Board" error={errors.board_id?.message}>
          <select className={inputClass} {...register("board_id")}>
            <option value="">Select board</option>
            {boardsQuery.data?.map((board) => (
              <option key={board.id} value={board.id}>
                {board.name}
              </option>
            ))}
          </select>
        </Field>
        <Field label="Class" error={errors.class_id?.message}>
          <select
            className={inputClass}
            value={classId}
            onChange={(e) => onClassChange(e.target.value)}
          >
            <option value="">Select class</option>
            {classesQuery.data?.map((item) => (
              <option key={item.id} value={item.id}>
                {item.name}
              </option>
            ))}
          </select>
        </Field>
      </div>

      {requiresStream || selectedClass?.requires_stream ? (
        <Field label="Stream" error={errors.stream_id?.message}>
          <select className={inputClass} {...register("stream_id")}>
            <option value="">Select stream</option>
            {streamsQuery.data?.map((stream) => (
              <option key={stream.id} value={stream.id}>
                {stream.name}
              </option>
            ))}
          </select>
        </Field>
      ) : (
        <p className="rounded-xl border border-border bg-muted/40 px-3 py-2 text-sm text-muted-foreground">
          Stream selection is only required for Class 11 and 12.
        </p>
      )}

      {localError ? (
        <p className="rounded-xl border border-destructive/30 bg-destructive/10 px-3 py-2 text-sm text-destructive">
          {localError}
        </p>
      ) : null}

      <button
        type="submit"
        disabled={updateMutation.isPending || photoMutation.isPending}
        className="h-11 w-full rounded-xl bg-primary text-sm font-semibold text-primary-foreground transition hover:brightness-110 disabled:opacity-70 md:w-auto md:px-8"
      >
        {updateMutation.isPending ? "Saving..." : submitLabel}
      </button>
    </form>
  );
}

function Field({
  label,
  error,
  children,
}: {
  label: string;
  error?: string;
  children: React.ReactNode;
}) {
  return (
    <div>
      <label className="mb-1.5 block text-sm font-medium">{label}</label>
      {children}
      {error ? <p className="mt-1 text-xs text-destructive">{error}</p> : null}
    </div>
  );
}

const inputClass = cn(
  "h-11 w-full rounded-xl border border-border bg-background px-3 text-sm outline-none ring-primary focus:ring-2",
);
