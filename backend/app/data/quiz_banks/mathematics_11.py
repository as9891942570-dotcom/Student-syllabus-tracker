"""CBSE Class 11 Mathematics concept banks (no Physics fallback)."""

from __future__ import annotations

from app.data.quiz_banks.common import q, register_keys, register_subject_keywords
from app.data.quiz_concepts import QuestionBank

BANK_SETS: QuestionBank = [
    q("If A = {1, 2} and B = {2, 3}, then A ∪ B is:", "{1, 2, 3}", ["{2}", "{1}", "{1, 2, 3, 4}"]),
    q("The power set of {a} has how many elements?", "2", ["1", "0", "3"]),
    q("A relation from A to B is a subset of:", "A × B", ["A ∪ B", "A ∩ B", "B - A"]),
    q("A function f: A → B is one-one if:", "f(x1) = f(x2) implies x1 = x2", ["Every element of A maps to the same image", "Range is empty", "f is not defined at 0"]),
    q("sin²θ + cos²θ equals:", "1", ["0", "tan θ", "2"]),
    q("The general solution of sin θ = 0 is:", "θ = nπ, n ∈ Z", ["θ = (2n+1)π/2", "θ = π/4 only", "θ = 0 only"]),
]

BANK_CALC: QuestionBank = [
    q("lim x→0 (sin x)/x equals:", "1", ["0", "∞", "x"]),
    q("d/dx (x²) is:", "2x", ["x", "2", "x²"]),
    q("The derivative of sin x is:", "cos x", ["-sin x", "tan x", "sec x"]),
    q("An AP with first term a and common difference d has nth term:", "a + (n-1)d", ["ar^(n-1)", "n(n+1)/2", "a/n + d"]),
    q("Sum of an infinite GP with |r| < 1 is:", "a/(1-r)", ["na", "a + nd", "n/2 (2a+(n-1)d)"]),
    q("C(n, r) equals:", "n! / (r!(n-r)!)", ["n^r", "n!", "r!"]),
    q("The slope of the line y = mx + c is:", "m", ["c", "-1/m always", "x-intercept"]),
    q("Distance of point (x1,y1) from line ax+by+c=0 is:", "|ax1+by1+c|/√(a²+b²)", ["a+b+c", "x1+y1", "√(a²+b²)"]),
]


def register() -> None:
    register_keys(
        [
            "Sets and their representations",
            "Types of sets",
            "Subsets",
            "Operations on sets",
            "Complement of a set",
            "Cartesian product of sets",
            "Relations",
            "Functions",
            "Types of functions",
        ],
        BANK_SETS,
    )
    register_keys(
        [
            "Intuitive idea of limit",
            "Limits",
            "Limits of polynomials and rational functions",
            "Limits of trigonometric functions",
            "Derivative",
            "Derivative of a function",
            "Algebra of derivative of functions",
            "Derivative of trigonometric functions",
            "Arithmetic progression",
            "Geometric progression",
            "Permutations",
            "Combinations",
            "Slope of a line",
            "Distance of a point from a line",
            "Binomial theorem for positive integers",
            "Pascal's triangle",
            "Circle",
            "Parabola",
            "Ellipse",
            "Hyperbola",
            "Variance",
            "Standard deviation",
            "Axiomatic approach to probability",
        ],
        BANK_CALC,
    )
    register_subject_keywords(
        "MATH",
        [
            (("sets", "power set", "venn", "cartesian product"), BANK_SETS),
            (("limit", "derivative", "arithmetic progression", "geometric progression", "permutation", "combination", "slope of a line", "binomial", "parabola", "probability", "variance"), BANK_CALC),
        ],
    )
