export type QuizSummary = {
  id: string;
  topic_id: string;
  title: string;
  time_limit_seconds: number;
  question_count: number;
  is_active: boolean;
};

export type QuizDetail = {
  id: string;
  topic_id: string;
  topic_title: string;
  chapter_id: string;
  chapter_title: string;
  subject_id: string;
  subject_name: string;
  title: string;
  time_limit_seconds: number;
  question_count: number;
  is_active: boolean;
};

export type QuizOption = {
  id: string;
  text: string;
  sort_order: number;
};

export type QuizQuestion = {
  id: string;
  prompt: string;
  sort_order: number;
  question_number: number;
  total_questions: number;
  options: QuizOption[];
  already_answered: boolean;
  selected_option_id?: string | null;
  correct_option_id?: string | null;
};

export type QuizAttempt = {
  id: string;
  quiz_id: string;
  quiz_title: string;
  topic_id: string;
  topic_title: string;
  chapter_id: string;
  chapter_title: string;
  subject_id: string;
  subject_name: string;
  status: "active" | "completed" | "expired" | string;
  current_question_index: number;
  total_questions: number;
  answered_count: number;
  correct_count: number;
  incorrect_count: number;
  score: number;
  percentage: number;
  xp_earned: number;
  total_xp: number;
  coins_earned?: number;
  total_coins?: number;
  topic_completed: boolean;
  next_topic_unlocked?: boolean;
  next_topic_id?: string | null;
  next_topic_title?: string | null;
  xp_awarded?: boolean;
  coins_awarded?: boolean;
  level?: number;
  level_floor_xp?: number;
  next_level_xp?: number;
  level_progress_percentage?: number;
  started_at: string;
  expires_at: string;
  ended_at?: string | null;
  seconds_remaining: number;
};

export type SubmitAnswerResponse = {
  question_id: string;
  selected_option_id: string;
  is_correct: boolean;
  correct_option_id?: string;
  attempt_id: string;
  answered_count: number;
  correct_count: number;
  incorrect_count: number;
};

export type QuizHistoryItem = {
  id: string;
  quiz_id: string;
  quiz_title: string;
  topic_id: string;
  topic_title: string;
  status: string;
  score: number;
  percentage: number;
  xp_earned: number;
  total_questions: number;
  correct_count: number;
  started_at: string;
  ended_at?: string | null;
  completed: boolean;
};
