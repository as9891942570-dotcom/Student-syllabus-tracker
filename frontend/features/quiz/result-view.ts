import type { QuizAttempt, QuizHistoryItem } from "@/types/quiz";

export const QUIZ_PASS_PERCENTAGE = 60;

export function quizResultFromAttempt(result: QuizAttempt) {
  const correct = result.correct_count;
  const wrong = result.incorrect_count;
  const total = result.total_questions;
  const percentage = result.percentage;
  const finished =
    result.status === "completed" || result.status === "expired";
  const passed = finished && percentage >= QUIZ_PASS_PERCENTAGE;
  return { correct, wrong, total, percentage, passed };
}

export function quizHistoryScore(item: QuizHistoryItem) {
  const correct = item.correct_count;
  const total = item.total_questions;
  const percentage = item.percentage;
  const passed =
    Boolean(item.completed) && percentage >= QUIZ_PASS_PERCENTAGE;
  return { correct, total, percentage, passed };
}
