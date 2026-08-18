export const queryKeys = {
  health: ["health"] as const,
  me: (userId?: string | null) => ["me", userId ?? "anon"] as const,
  dashboard: (userId?: string | null) => ["dashboard", userId ?? "anon"] as const,
  auth: {
    me: (userId?: string | null) => ["auth", "me", userId ?? "anon"] as const,
  },
  profile: {
    me: (userId?: string | null) => ["profile", "me", userId ?? "anon"] as const,
    boards: ["profile", "boards"] as const,
    classes: ["profile", "classes"] as const,
    streams: ["profile", "streams"] as const,
  },
  syllabus: {
    subjects: (userId?: string | null) =>
      ["syllabus", "subjects", userId ?? "anon"] as const,
    subject: (id: string, userId?: string | null) =>
      ["syllabus", "subjects", userId ?? "anon", id] as const,
    chapter: (id: string, userId?: string | null) =>
      ["syllabus", "chapters", userId ?? "anon", id] as const,
    completion: (userId?: string | null) =>
      ["syllabus", "completion", userId ?? "anon"] as const,
    structure: (userId?: string | null) =>
      ["syllabus", "structure", userId ?? "anon"] as const,
  },
  quiz: {
    topic: (topicId: string, userId?: string | null) =>
      ["quiz", "topic", userId ?? "anon", topicId] as const,
    detail: (quizId: string, userId?: string | null) =>
      ["quiz", "detail", userId ?? "anon", quizId] as const,
    active: (userId?: string | null) =>
      ["quiz", "active", userId ?? "anon"] as const,
    attempt: (id: string, userId?: string | null) =>
      ["quiz", "attempt", userId ?? "anon", id] as const,
    question: (id: string, userId?: string | null) =>
      ["quiz", "question", userId ?? "anon", id] as const,
    history: (userId?: string | null) =>
      ["quiz", "history", userId ?? "anon"] as const,
  },
  progression: {
    me: (userId?: string | null) =>
      ["progression", "me", userId ?? "anon"] as const,
  },
};
