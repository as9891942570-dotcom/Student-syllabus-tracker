import type { QuizAttempt, QuizHistoryItem } from "@/types/quiz";

export const QUIZ_PASS_PERCENTAGE = 60;

type ScoreSource = Pick<
  QuizAttempt,
  | "correct_count"
  | "incorrect_count"
  | "correct_answers"
  | "wrong_answers"
  | "total_questions"
  | "percentage"
  | "passed"
  | "status"
>;

export function quizResultFromAttempt(result: ScoreSource) {
  const correct = result.correct_answers ?? result.correct_count;
  const wrong = result.wrong_answers ?? result.incorrect_count;
  const total = result.total_questions;
  const percentage = result.percentage;
  const finished =
    result.status === "completed" || result.status === "expired";
  const passed =
    typeof result.passed === "boolean"
      ? result.passed
      : finished && percentage >= QUIZ_PASS_PERCENTAGE;
  return { correct, wrong, total, percentage, passed };
}

export function quizHistoryScore(item: QuizHistoryItem) {
  const correct = item.correct_count;
  const total = item.total_questions;
  const percentage = item.percentage;
  const passed =
    typeof item.passed === "boolean"
      ? item.passed
      : Boolean(item.completed) && percentage >= QUIZ_PASS_PERCENTAGE;
  return { correct, total, percentage, passed };
}
