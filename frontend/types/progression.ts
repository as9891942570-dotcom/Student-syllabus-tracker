export type ProgressionTopic = {
  id: string;
  title: string;
  chapter_id: string;
  chapter_title: string;
  subject_id: string;
  subject_name: string;
  sort_order: number;
  is_completed: boolean;
  is_locked: boolean;
  is_current: boolean;
};

export type Progression = {
  total_xp: number;
  total_coins?: number;
  level: number;
  level_floor_xp: number;
  next_level_xp: number;
  xp_into_level: number;
  xp_needed_for_next: number;
  level_progress_percentage: number;
  overall_completion_percentage: number;
  completed_topic_count: number;
  total_topic_count: number;
  current_topic: ProgressionTopic | null;
  next_topic: ProgressionTopic | null;
  completed_topics: ProgressionTopic[];
};
