export type Topic = {
  id: string;
  title: string;
  sort_order: number;
  is_completed: boolean;
  completed_at: string | null;
  is_locked: boolean;
  is_current: boolean;
};

export type Chapter = {
  id: string;
  title: string;
  sort_order: number;
  topic_count: number;
  completed_topic_count: number;
  completion_percentage: number;
  topics: Topic[];
};

export type Subject = {
  id: string;
  name: string;
  code: string;
  sort_order: number;
  chapter_count: number;
  topic_count: number;
  completed_topic_count: number;
  completion_percentage: number;
};

export type SubjectDetail = Subject & {
  chapters: Chapter[];
};

export type SyllabusCompletion = {
  overall_completion_percentage: number;
  total_subjects: number;
  total_chapters: number;
  total_topics: number;
  completed_topics: number;
  subjects: Subject[];
};

export type SyllabusStructure = {
  subjects: SubjectDetail[];
  overall_completion_percentage: number;
  total_topics: number;
  completed_topics: number;
};
