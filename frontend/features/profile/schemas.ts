import { z } from "zod";

export const profileFormSchema = z
  .object({
    full_name: z.string().min(2, "Name must be at least 2 characters").max(120),
    mobile: z
      .string()
      .min(10, "Enter a valid mobile number")
      .max(15, "Enter a valid mobile number")
      .regex(/^\d+$/, "Mobile number must contain digits only"),
    board_id: z.string().uuid("Select a board"),
    class_id: z.string().uuid("Select a class"),
    stream_id: z.string().uuid().optional().or(z.literal("")),
    requires_stream: z.boolean(),
  })
  .superRefine((data, ctx) => {
    if (data.requires_stream && !data.stream_id) {
      ctx.addIssue({
        code: "custom",
        path: ["stream_id"],
        message: "Select a stream for Class 11 or 12",
      });
    }
    if (!data.requires_stream && data.stream_id) {
      ctx.addIssue({
        code: "custom",
        path: ["stream_id"],
        message: "Stream is only for Class 11 and 12",
      });
    }
  });

export type ProfileFormValues = z.infer<typeof profileFormSchema>;
