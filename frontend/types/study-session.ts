export type StudySession = {
  id: string;
  status: "active" | "completed" | string;
  subject_id: string;
  subject_name: string;
  chapter_id: string;
  chapter_title: string;
  topic_id: string;
  topic_title: string;
  started_at: string;
  ended_at: string | null;
  duration_seconds: number;
  score: number;
  correct_count: number;
  incorrect_count: number;
  xp_earned: number;
  total_xp: number;
};
