export type TopicCardStatus = "completed" | "start" | "locked";

export function topicCardStatus(topic: {
  is_locked?: boolean | null;
  is_completed?: boolean | null;
}): TopicCardStatus {
  if (topic.is_locked) return "locked";
  if (topic.is_completed) return "completed";
  return "start";
}

export function topicQuizLabel(status: TopicCardStatus): string {
  if (status === "locked") return "Locked";
  if (status === "completed") return "Retry Quiz";
  return "Start Quiz";
}
