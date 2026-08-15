export type AuthUser = {
  id: string;
  email: string;
  full_name: string;
  is_active: boolean;
  created_at: string;
};

export type TokenResponse = {
  access_token: string;
  refresh_token: string;
  token_type: string;
  user: AuthUser;
};

export type MessageResponse = {
  message: string;
  code?: string;
};

export type RegisterPayload = {
  email: string;
  password: string;
  full_name: string;
};

export type LoginPayload = {
  email?: string;
  user_id?: string;
  password: string;
};
