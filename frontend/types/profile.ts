export type Board = {
  id: string;
  code: string;
  name: string;
};

export type SchoolClass = {
  id: string;
  grade: number;
  name: string;
  requires_stream: boolean;
};

export type Stream = {
  id: string;
  code: string;
  name: string;
};

export type Profile = {
  id: string;
  user_id: string;
  email: string;
  full_name: string;
  mobile: string | null;
  photo_url: string | null;
  board: Board | null;
  school_class: SchoolClass | null;
  stream: Stream | null;
  total_xp: number;
  total_coins: number;
  level: number;
  level_floor_xp: number;
  next_level_xp: number;
  xp_into_level: number;
  xp_needed_for_next: number;
  level_progress_percentage: number;
  completion_percentage: number;
  is_complete: boolean;
  academic_locked?: boolean;
  missing_fields: string[];
  created_at: string;
  updated_at: string;
};

export type ProfileUpdatePayload = {
  full_name?: string;
  mobile?: string;
  board_id?: string;
  class_id?: string;
  stream_id?: string | null;
  clear_stream?: boolean;
};
