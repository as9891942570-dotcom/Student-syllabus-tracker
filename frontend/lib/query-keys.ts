export const queryKeys = {
  health: ["health"] as const,
  me: ["me"] as const,
  dashboard: ["dashboard"] as const,
  auth: {
    me: ["auth", "me"] as const,
  },
  profile: {
    me: ["profile", "me"] as const,
    boards: ["profile", "boards"] as const,
    classes: ["profile", "classes"] as const,
    streams: ["profile", "streams"] as const,
  },
  syllabus: {
    subjects: ["syllabus", "subjects"] as const,
    subject: (id: string) => ["syllabus", "subjects", id] as const,
    chapter: (id: string) => ["syllabus", "chapters", id] as const,
    completion: ["syllabus", "completion"] as const,
    structure: ["syllabus", "structure"] as const,
  },
  quiz: {
    topic: (topicId: string) => ["quiz", "topic", topicId] as const,
    detail: (quizId: string) => ["quiz", "detail", quizId] as const,
    active: ["quiz", "active"] as const,
    attempt: (id: string) => ["quiz", "attempt", id] as const,
    question: (id: string) => ["quiz", "question", id] as const,
    history: ["quiz", "history"] as const,
    result: (id: string) => ["quiz", "attempt", id, "result"] as const,
  },
  progression: {
    me: ["progression", "me"] as const,
  },
};
