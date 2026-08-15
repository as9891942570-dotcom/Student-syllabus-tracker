import { useAuthStore } from "@/stores/auth-store";
import type {
  LoginPayload,
  MessageResponse,
  RegisterPayload,
  TokenResponse,
  AuthUser,
} from "@/types/auth";

export const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL ?? "https://student-syllabus-tracker-v1sg.onrender.com/api/v1";

export const API_ORIGIN =
  process.env.NEXT_PUBLIC_API_ORIGIN ??
  "https://student-syllabus-tracker-v1sg.onrender.com";

export function resolveMediaUrl(path?: string | null): string | null {
  if (!path) return null;
  if (path.startsWith("http://") || path.startsWith("https://")) return path;
  return `${API_ORIGIN}${path}`;
}

export class ApiError extends Error {
  status: number;
  code?: string;

  constructor(message: string, status: number, code?: string) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.code = code;
  }
}

type ApiFetchOptions = RequestInit & {
  auth?: boolean;
  skipRefresh?: boolean;
};

let refreshPromise: Promise<string | null> | null = null;

async function parseError(response: Response): Promise<ApiError> {
  let detail = response.statusText;
  let code: string | undefined;
  try {
    const body = (await response.json()) as {
      detail?: string | Array<{ msg?: string }>;
      code?: string;
    };
    if (typeof body.detail === "string") {
      detail = body.detail;
    } else if (Array.isArray(body.detail) && body.detail[0]?.msg) {
      detail = body.detail[0].msg;
    }
    code = body.code;
  } catch {
    // ignore
  }
  return new ApiError(detail, response.status, code);
}

async function refreshAccessToken(): Promise<string | null> {
  const { refreshToken, setSession, clearSession, user } = useAuthStore.getState();
  if (!refreshToken) {
    clearSession();
    return null;
  }

  const response = await fetch(`${API_BASE_URL}/auth/refresh`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({ refresh_token: refreshToken }),
  });

  if (!response.ok) {
    clearSession();
    return null;
  }

  const data = (await response.json()) as TokenResponse;
  setSession({
    accessToken: data.access_token,
    refreshToken: data.refresh_token,
    user: data.user ?? user!,
  });
  return data.access_token;
}

export async function apiFetch<T>(
  path: string,
  init: ApiFetchOptions = {},
): Promise<T> {
  const { auth = false, skipRefresh = false, headers, ...rest } = init;
  const requestHeaders = new Headers(headers);
  const isFormData = typeof FormData !== "undefined" && rest.body instanceof FormData;
  if (!isFormData && !requestHeaders.has("Content-Type") && rest.body) {
    requestHeaders.set("Content-Type", "application/json");
  }

  if (auth) {
    const token = useAuthStore.getState().accessToken;
    if (token) {
      requestHeaders.set("Authorization", `Bearer ${token}`);
    }
  }

  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...rest,
    headers: requestHeaders,
    credentials: "include",
  });

  if (response.status === 401 && auth && !skipRefresh) {
    if (!refreshPromise) {
      refreshPromise = refreshAccessToken().finally(() => {
        refreshPromise = null;
      });
    }
    const newToken = await refreshPromise;
    if (newToken) {
      requestHeaders.set("Authorization", `Bearer ${newToken}`);
      const retry = await fetch(`${API_BASE_URL}${path}`, {
        ...rest,
        headers: requestHeaders,
        credentials: "include",
      });
      if (!retry.ok) {
        throw await parseError(retry);
      }
      if (retry.status === 204) {
        return undefined as T;
      }
      return retry.json() as Promise<T>;
    }
  }

  if (!response.ok) {
    throw await parseError(response);
  }

  if (response.status === 204) {
    return undefined as T;
  }

  return response.json() as Promise<T>;
}

export const authApi = {
  register: (payload: RegisterPayload) =>
    apiFetch<TokenResponse>("/auth/register", {
      method: "POST",
      body: JSON.stringify(payload),
    }),
  login: (payload: LoginPayload) =>
    apiFetch<TokenResponse>("/auth/login", {
      method: "POST",
      body: JSON.stringify(payload),
    }),
  logout: (refreshToken?: string | null) =>
    apiFetch<MessageResponse>("/auth/logout", {
      method: "POST",
      body: JSON.stringify({ refresh_token: refreshToken ?? null }),
      auth: true,
      skipRefresh: true,
    }),
  me: () => apiFetch<AuthUser>("/auth/me", { auth: true }),
  forgotPassword: (email: string) =>
    apiFetch<MessageResponse>("/auth/forgot-password", {
      method: "POST",
      body: JSON.stringify({ email }),
    }),
};

export const profileApi = {
  getMe: () => apiFetch<import("@/types/profile").Profile>("/profile/me", { auth: true }),
  updateMe: (payload: import("@/types/profile").ProfileUpdatePayload) =>
    apiFetch<import("@/types/profile").Profile>("/profile/me", {
      method: "PUT",
      auth: true,
      body: JSON.stringify(payload),
    }),
  uploadPhoto: (file: File) => {
    const form = new FormData();
    form.append("file", file);
    return apiFetch<import("@/types/profile").Profile>("/profile/me/photo", {
      method: "POST",
      auth: true,
      body: form,
    });
  },
  listBoards: () =>
    apiFetch<import("@/types/profile").Board[]>("/boards", { auth: true }),
  listClasses: () =>
    apiFetch<import("@/types/profile").SchoolClass[]>("/classes", { auth: true }),
  listStreams: () =>
    apiFetch<import("@/types/profile").Stream[]>("/streams", { auth: true }),
};

export const syllabusApi = {
  listSubjects: () =>
    apiFetch<import("@/types/syllabus").Subject[]>("/syllabus/subjects", {
      auth: true,
    }),
  getSubject: (subjectId: string) =>
    apiFetch<import("@/types/syllabus").SubjectDetail>(
      `/syllabus/subjects/${subjectId}`,
      { auth: true },
    ),
  getChapterTopics: (chapterId: string) =>
    apiFetch<import("@/types/syllabus").Chapter>(
      `/syllabus/chapters/${chapterId}/topics`,
      { auth: true },
    ),
  getCompletion: () =>
    apiFetch<import("@/types/syllabus").SyllabusCompletion>(
      "/syllabus/completion",
      { auth: true },
    ),
  getStructure: () =>
    apiFetch<import("@/types/syllabus").SyllabusStructure>(
      "/syllabus/structure",
      { auth: true },
    ),
};

export const quizApi = {
  listForTopic: (topicId: string) =>
    apiFetch<import("@/types/quiz").QuizSummary[]>(
      `/quizzes/topics/${topicId}`,
      { auth: true },
    ),
  getQuiz: (quizId: string) =>
    apiFetch<import("@/types/quiz").QuizDetail>(`/quizzes/${quizId}`, {
      auth: true,
    }),
  start: (quizId: string) =>
    apiFetch<import("@/types/quiz").QuizAttempt>(`/quizzes/${quizId}/start`, {
      method: "POST",
      auth: true,
    }),
  getActive: () =>
    apiFetch<import("@/types/quiz").QuizAttempt | null>(
      "/quiz-attempts/active",
      { auth: true },
    ),
  getAttempt: (attemptId: string) =>
    apiFetch<import("@/types/quiz").QuizAttempt>(
      `/quiz-attempts/${attemptId}`,
      { auth: true },
    ),
  currentQuestion: (attemptId: string) =>
    apiFetch<import("@/types/quiz").QuizQuestion>(
      `/quiz-attempts/${attemptId}/current-question`,
      { auth: true },
    ),
  submitAnswer: (attemptId: string, optionId: string) =>
    apiFetch<import("@/types/quiz").SubmitAnswerResponse>(
      `/quiz-attempts/${attemptId}/answers`,
      {
        method: "POST",
        auth: true,
        body: JSON.stringify({ option_id: optionId }),
      },
    ),
  next: (attemptId: string) =>
    apiFetch<import("@/types/quiz").QuizAttempt>(
      `/quiz-attempts/${attemptId}/next`,
      { method: "POST", auth: true },
    ),
  complete: (attemptId: string) =>
    apiFetch<import("@/types/quiz").QuizAttempt>(
      `/quiz-attempts/${attemptId}/complete`,
      { method: "POST", auth: true },
    ),
  result: (attemptId: string) =>
    apiFetch<import("@/types/quiz").QuizAttempt>(
      `/quiz-attempts/${attemptId}/result`,
      { auth: true },
    ),
  history: () =>
    apiFetch<import("@/types/quiz").QuizHistoryItem[]>(
      "/quiz-attempts/history",
      { auth: true },
    ),
};

export const progressionApi = {
  me: () =>
    apiFetch<import("@/types/progression").Progression>("/progression/me", {
      auth: true,
    }),
};
