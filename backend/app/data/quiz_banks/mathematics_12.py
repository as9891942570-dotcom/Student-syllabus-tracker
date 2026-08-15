"""EduQuest CBSE Class 12 Mathematics concept/numerical MCQ banks."""

from __future__ import annotations

from app.data.quiz_banks.common import QuestionBank, q, register_keys, register_subject_keywords

# ---------------------------------------------------------------------------
# Relations and Functions
# ---------------------------------------------------------------------------

BANK_TYPES_OF_RELATIONS: QuestionBank = [
    q(
        "A relation R on set A is reflexive if for every a in A:",
        "(a, a) belongs to R",
        ["(a, b) belongs to R for all distinct a, b", "No element is related to itself", "Every pair is symmetric only"],
    ),
    q(
        "A relation R on A is symmetric if whenever (a, b) is in R, then:",
        "(b, a) is also in R",
        ["(a, a) is never in R", "(b, c) must be in R for all c", "R has exactly one element"],
    ),
    q(
        "A relation R is transitive if whenever (a, b) and (b, c) are in R, then:",
        "(a, c) is in R",
        ["(c, a) is in R always", "(b, a) is in R", "No third pair is required"],
    ),
    q(
        "An equivalence relation on a set must be:",
        "Reflexive, symmetric, and transitive",
        ["Only reflexive", "Only symmetric", "Reflexive and antisymmetric only"],
    ),
    q(
        "On the set of integers Z, the relation R = {(a, b) : a - b is divisible by 5} is:",
        "An equivalence relation",
        ["Not reflexive", "Not symmetric", "Not transitive"],
    ),
    q(
        "The empty relation on a non-empty set A (no pairs) is:",
        "Symmetric and transitive, but not reflexive",
        ["Reflexive, symmetric, and transitive", "An equivalence relation", "Reflexive only"],
    ),
    q(
        "On {1, 2, 3}, which relation is NOT symmetric?",
        "R = {(1, 2), (2, 3)}",
        ["R = {(1, 1), (2, 2), (3, 3)}", "R = {(1, 2), (2, 1)}", "Universal relation A x A"],
    ),
    q(
        "If a relation on A is both symmetric and antisymmetric, then for a != b in A:",
        "(a, b) and (b, a) cannot both be in R unless a = b",
        ["All pairs must be in R", "R must be empty", "R must contain exactly two pairs"],
    ),
]

BANK_TYPES_OF_FUNCTIONS: QuestionBank = [
    q(
        "A function f: A -> B is one-one (injective) if:",
        "Distinct elements of A have distinct images in B",
        ["Every element of B has a preimage", "f(x) = x for all x", "f is constant"],
    ),
    q(
        "A function f: A -> B is onto (surjective) if:",
        "Every element of B is the image of at least one element of A",
        ["f is one-one only", "Range is a proper subset of B", "Domain equals co-domain always for all functions"],
    ),
    q(
        "A function that is both one-one and onto is called:",
        "Bijective",
        ["Constant", "Identity only", "Many-one always"],
    ),
    q(
        "The function f: R -> R, f(x) = |x| is:",
        "Many-one but onto",
        ["One-one and onto", "One-one but not onto", "Into but not onto R"],
    ),
    q(
        "The identity function I: A -> A is:",
        "Bijective",
        ["Constant", "Not defined on A", "Many-one"],
    ),
    q(
        "f: N -> N, f(n) = n + 1 is:",
        "One-one but not onto N",
        ["Onto but not one-one", "Bijective", "Neither one-one nor onto"],
    ),
    q(
        "A constant function f: A -> B with f(x) = c for all x in A is one-one iff:",
        "|A| = 1",
        ["|B| = 1", "c = 0", "A is infinite"],
    ),
    q(
        "The modulus function f(x) = |x| from R to R is:",
        "Neither one-one nor onto if co-domain is all R",
        ["One-one and onto", "One-one only", "Onto only"],
    ),
]

BANK_COMPOSITION_INVERTIBLE: QuestionBank = [
    q(
        "If f: A -> B and g: B -> C, then (g o f)(x) equals:",
        "g(f(x))",
        ["f(g(x))", "g(x) + f(x)", "f(x)/g(x)"],
    ),
    q(
        "A function f: A -> B is invertible if and only if it is:",
        "Bijective",
        ["Constant", "Many-one", "Into but not onto"],
    ),
    q(
        "If f is invertible, then (f^-1)^-1 equals:",
        "f",
        ["1/f", "f^2", "The identity on B only"],
    ),
    q(
        "For invertible f: A -> B and g: B -> C both invertible, (g o f)^-1 equals:",
        "f^-1 o g^-1",
        ["g^-1 o f^-1", "(g o f)^2", "g o f"],
    ),
    q(
        "If f(x) = 2x + 3 and g(x) = (x - 3)/2, then g is:",
        "The inverse of f on R",
        ["Not related to f", "Equal to f", "f o g is undefined"],
    ),
    q(
        "The domain of g o f is:",
        "All x in domain of f such that f(x) is in domain of g",
        ["Always all real numbers", "Domain of g only", "Empty if f and g are linear"],
    ),
    q(
        "If f: {1,2,3} -> {a,b,c} is a bijection, number of possible f is:",
        "3! = 6",
        ["3", "9", "27"],
    ),
    q(
        "For f(x) = x^3 on R, the inverse f^-1(x) is:",
        "x^(1/3)",
        ["x^3", "-x^3", "1/x^3"],
    ),
]

# ---------------------------------------------------------------------------
# Inverse Trigonometric Functions
# ---------------------------------------------------------------------------

BANK_ITF_BASIC: QuestionBank = [
    q(
        "The principal value branch of sin^-1 x has range:",
        "[-pi/2, pi/2]",
        ["[0, pi]", "[-pi, pi]", "[0, pi/2]"],
    ),
    q(
        "The domain of cos^-1 x is:",
        "[-1, 1]",
        ["R", "[0, pi]", "[-pi/2, pi/2]"],
    ),
    q(
        "sin^-1 x is defined for:",
        "x in [-1, 1]",
        ["All real x", "x >= 0 only", "x in (-1, 1) only excluding endpoints"],
    ),
    q(
        "The range of tan^-1 x is:",
        "(-pi/2, pi/2)",
        ["[0, pi]", "[-pi, pi]", "[0, pi/2]"],
    ),
    q(
        "sin^-1(-x) equals:",
        "-sin^-1 x",
        ["sin^-1 x", "pi - sin^-1 x", "cos^-1 x"],
    ),
    q(
        "For x in [-1, 1], sin^-1 x + cos^-1 x equals:",
        "pi/2",
        ["pi", "0", "2 sin^-1 x"],
    ),
    q(
        "The function sin^-1 x is:",
        "Odd",
        ["Even", "Neither odd nor even", "Constant"],
    ),
    q(
        "tan^-1 x + cot^-1 x for all real x equals:",
        "pi/2",
        ["pi", "0", "tan^-1(1/x)"],
    ),
]

BANK_ITF_PROPERTIES: QuestionBank = [
    q(
        "sin(2 sin^-1 x) equals:",
        "2x sqrt(1 - x^2)",
        ["2x", "x sqrt(1 - x^2)", "1 - 2x^2"],
    ),
    q(
        "cos(2 cos^-1 x) equals:",
        "2x^2 - 1",
        ["2x - 1", "1 - 2x^2 only for all x", "x^2 + 1"],
    ),
    q(
        "tan(sin^-1 x) for |x| <= 1 equals:",
        "x / sqrt(1 - x^2)",
        ["sqrt(1 - x^2) / x", "x", "1 - x^2"],
    ),
    q(
        "sin^-1 x + sin^-1 y = pi/2 implies y equals:",
        "sqrt(1 - x^2) when x^2 + y^2 = 1 in principal branch context",
        ["x", "-x", "1/x"],
    ),
    q(
        "3 sin^-1 x = pi implies x equals:",
        "1",
        ["0", "1/2", "sqrt(3)/2"],
    ),
    q(
        "2 cos^-1 x = pi implies x equals:",
        "0",
        ["1", "-1", "1/2"],
    ),
    q(
        "sin^-1(1) + cos^-1(0) equals:",
        "pi",
        ["pi/2", "3pi/2", "0"],
    ),
    q(
        "For suitable x, sin^-1 x - cos^-1 x equals:",
        "2 sin^-1 x - pi/2",
        ["0 always", "pi/2 always", "2 cos^-1 x"],
    ),
]

BANK_ITF_PRINCIPAL_VALUES: QuestionBank = [
    q(
        "The principal value of sin^-1(1/2) is:",
        "pi/6",
        ["pi/3", "5pi/6", "pi/2"],
    ),
    q(
        "The principal value of cos^-1(-1/2) is:",
        "2pi/3",
        ["pi/6", "pi/3", "5pi/6"],
    ),
    q(
        "The principal value of tan^-1(1) is:",
        "pi/4",
        ["pi/6", "pi/3", "pi/2"],
    ),
    q(
        "The principal value of sin^-1(-1) is:",
        "-pi/2",
        ["pi/2", "3pi/2", "pi"],
    ),
    q(
        "The principal value of cos^-1(0) is:",
        "pi/2",
        ["0", "pi", "-pi/2"],
    ),
    q(
        "The principal value of tan^-1(-sqrt(3)) is:",
        "-pi/3",
        ["pi/3", "2pi/3", "-2pi/3"],
    ),
    q(
        "The principal value of sin^-1(sin(5pi/6)) is:",
        "pi/6",
        ["5pi/6", "-pi/6", "pi/2"],
    ),
    q(
        "The principal value of cos^-1(cos(4pi/3)) is:",
        "2pi/3",
        ["4pi/3", "pi/3", "pi/6"],
    ),
]

# ---------------------------------------------------------------------------
# Matrices
# ---------------------------------------------------------------------------

BANK_MATRIX_TYPES: QuestionBank = [
    q(
        "A matrix with m rows and n columns has order:",
        "m x n",
        ["n x m always", "m + n", "max(m, n)"],
    ),
    q(
        "A square matrix has:",
        "Equal number of rows and columns",
        ["Only one row", "Only one column", "Zero rows"],
    ),
    q(
        "In a diagonal matrix, all non-diagonal entries are:",
        "Zero",
        ["One", "Equal to each other", "Undefined"],
    ),
    q(
        "The identity matrix I_3 has diagonal entries:",
        "All 1, off-diagonal 0",
        ["All 0", "All equal to 3", "1, 2, 3 on diagonal"],
    ),
    q(
        "A scalar matrix is a diagonal matrix with:",
        "All diagonal entries equal",
        ["All entries zero", "Determinant zero always", "No diagonal entries"],
    ),
    q(
        "The zero matrix is:",
        "A matrix with every entry 0",
        ["The identity matrix", "Always invertible", "Always 1 x 1"],
    ),
    q(
        "A row matrix has:",
        "One row",
        ["One column only", "Equal rows and columns", "No rows"],
    ),
    q(
        "If A is 2 x 3 and B is 3 x 4, the product AB is defined with order:",
        "2 x 4",
        ["3 x 3", "2 x 3", "3 x 4"],
    ),
]

BANK_MATRIX_OPERATIONS: QuestionBank = [
    q(
        "Matrix addition A + B is defined when:",
        "A and B have the same order",
        ["A is square only", "B is row matrix only", "Orders are unrelated"],
    ),
    q(
        "If A is m x n and k is a scalar, kA has order:",
        "m x n",
        ["n x m", "m x k", "k x n"],
    ),
    q(
        "For matrices A and B, AB = BA:",
        "Not always true",
        ["Always true", "True iff both are zero", "True for all square matrices"],
    ),
    q(
        "If A is 2 x 3 and B is 3 x 2, then AB is:",
        "2 x 2",
        ["3 x 3", "2 x 3", "Undefined"],
    ),
    q(
        "For any compatible matrices, (AB)C equals:",
        "A(BC)",
        ["(AC)B", "AB + BC", "BA C"],
    ),
    q(
        "If A is invertible, A A^-1 equals:",
        "I (identity of appropriate order)",
        ["Zero matrix", "A^2", "A^-1 A^-1"],
    ),
    q(
        "If A = [[1,2],[3,4]] and B = [[0,1],[1,0]], the (1,1) entry of AB is:",
        "2",
        ["1", "3", "4"],
    ),
    q(
        "Multiplying a matrix by zero scalar gives:",
        "Zero matrix of same order",
        ["Identity matrix", "Undefined matrix", "Original matrix"],
    ),
]

BANK_MATRIX_TRANSPOSE: QuestionBank = [
    q(
        "If A has order m x n, then A^T has order:",
        "n x m",
        ["m x n", "m x m", "n x n"],
    ),
    q(
        "For any matrix A, (A^T)^T equals:",
        "A",
        ["A^T", "-A", "A^-1"],
    ),
    q(
        "A matrix A is symmetric if:",
        "A^T = A",
        ["A^T = -A", "A = -A", "A is diagonal only"],
    ),
    q(
        "A matrix A is skew-symmetric if:",
        "A^T = -A",
        ["A^T = A", "All entries positive", "A is identity"],
    ),
    q(
        "For matrices A, B of same order, (A + B)^T equals:",
        "A^T + B^T",
        ["A^T B^T", "B^T - A^T", "(AB)^T"],
    ),
    q(
        "For compatible A, B, (AB)^T equals:",
        "B^T A^T",
        ["A^T B^T", "(BA)^T", "A^T + B^T"],
    ),
    q(
        "Every diagonal matrix is:",
        "Symmetric",
        ["Skew-symmetric", "Neither symmetric nor skew-symmetric always", "Always zero"],
    ),
    q(
        "If A is skew-symmetric of odd order, then |A| equals:",
        "0",
        ["1", "Always non-zero", "Equal to trace of A"],
    ),
]

# ---------------------------------------------------------------------------
# Determinants
# ---------------------------------------------------------------------------

BANK_DET_SQUARE: QuestionBank = [
    q(
        "The determinant of A = [[a,b],[c,d]] is:",
        "ad - bc",
        ["ac - bd", "a + d", "ab - cd"],
    ),
    q(
        "If A = [[2,1],[4,3]], then |A| equals:",
        "2",
        ["10", "6", "0"],
    ),
    q(
        "If a row of a matrix is all zeros, its determinant is:",
        "0",
        ["1", "Sum of diagonal entries", "Always undefined"],
    ),
    q(
        "If two rows of a matrix are identical, |A| equals:",
        "0",
        ["1", "2|A|", "Product of diagonal entries always"],
    ),
    q(
        "If A is 3 x 3 with |A| = 5, then |2A| equals:",
        "40",
        ["10", "5", "20"],
    ),
    q(
        "For a 2 x 2 matrix, |kA| equals:",
        "k^2 |A|",
        ["k |A|", "2k |A|", "|A|/k"],
    ),
    q(
        "The determinant of an identity matrix I_n is:",
        "1",
        ["0", "n", "n^2"],
    ),
    q(
        "If A is singular, then |A| equals:",
        "0",
        ["1", "Non-zero always", "Equal to trace A"],
    ),
]

BANK_DET_PROPERTIES: QuestionBank = [
    q(
        "Interchanging two rows of a matrix:",
        "Multiplies the determinant by -1",
        ["Leaves determinant unchanged", "Makes determinant zero", "Doubles the determinant"],
    ),
    q(
        "If B is obtained from A by multiplying one row by k, then |B| equals:",
        "k |A|",
        ["|A|/k", "k^2 |A|", "|A| + k"],
    ),
    q(
        "If A and B are square matrices of same order, |AB| equals:",
        "|A| |B|",
        ["|A| + |B|", "|A| - |B|", "|A|/|B|"],
    ),
    q(
        "If A is invertible, |A^-1| equals:",
        "1/|A|",
        ["|A|", "-|A|", "|A|^2"],
    ),
    q(
        "Adding a multiple of one row to another row:",
        "Does not change the determinant",
        ["Always zeroes the determinant", "Doubles the determinant", "Changes sign"],
    ),
    q(
        "For triangular matrix (upper or lower), |A| equals:",
        "Product of diagonal entries",
        ["Sum of diagonal entries", "Zero always", "1 always"],
    ),
    q(
        "If A^T = A, then |A| is:",
        "Equal to |A| (real determinant, unchanged by transpose)",
        ["Always negative", "Always zero", "Undefined"],
    ),
    q(
        "If two columns of A are proportional, then |A| equals:",
        "0",
        ["1", "Product of diagonals", "Non-zero always"],
    ),
]

BANK_DET_ADJOINT_INVERSE: QuestionBank = [
    q(
        "The adjoint of A, adj(A), is the transpose of the matrix of:",
        "Cofactors",
        ["Minors only without sign", "Row sums", "Eigenvalues"],
    ),
    q(
        "If |A| != 0, then A^-1 equals:",
        "(1/|A|) adj(A)",
        ["adj(A) only", "|A| adj(A)", "adj(A)/|A|^2"],
    ),
    q(
        "For invertible A, A (adj A) equals:",
        "|A| I",
        ["I", "adj(A)", "Zero matrix"],
    ),
    q(
        "If A is 2 x 2 with |A| = 3, then |adj(A)| equals:",
        "3",
        ["9", "6", "1"],
    ),
    q(
        "A matrix is invertible iff:",
        "|A| != 0",
        ["|A| = 0", "A is symmetric", "A is diagonal"],
    ),
    q(
        "If A is singular, then A^-1:",
        "Does not exist",
        ["Equals zero matrix", "Equals adj(A)", "Equals I"],
    ),
    q(
        "For 2 x 2 matrix [[a,b],[c,d]] with ad - bc != 0, A^-1 equals:",
        "(1/(ad-bc)) [[d,-b],[-c,a]]",
        ["[[d,-b],[-c,a]] without factor", "[[a,b],[c,d]]", "Transpose of A"],
    ),
    q(
        "If A is invertible and |A| = 2, then |A^-1| equals:",
        "1/2",
        ["2", "4", "-2"],
    ),
]

# ---------------------------------------------------------------------------
# Continuity and Differentiability
# ---------------------------------------------------------------------------

BANK_CONTINUITY: QuestionBank = [
    q(
        "f is continuous at x = a if:",
        "lim(x->a) f(x) = f(a)",
        ["f(a) = 0", "f'(a) exists only", "f is defined only at a"],
    ),
    q(
        "Every polynomial function on R is:",
        "Continuous on R",
        ["Discontinuous everywhere", "Continuous only at integers", "Not defined at x = 0"],
    ),
    q(
        "If f and g are continuous at a, then f + g is:",
        "Continuous at a",
        ["Discontinuous at a", "Undefined at a", "Continuous only if f = g"],
    ),
    q(
        "The function f(x) = |x| is continuous at x = 0 because:",
        "Left and right limits equal f(0)",
        ["It is not defined at 0", "Derivative exists at 0", "It is discontinuous at 0"],
    ),
    q(
        "A removable discontinuity occurs when:",
        "Limit exists but may not equal f(a) or f(a) undefined",
        ["Left and right limits differ", "Function is unbounded", "Function is periodic"],
    ),
    q(
        "If f is continuous on [a,b], then f attains:",
        "Maximum and minimum values on [a,b]",
        ["Only maximum", "No extreme values", "Zero always"],
    ),
    q(
        "The function 1/x is continuous on:",
        "R \\ {0}",
        ["All R", "Only x > 0", "Only integers"],
    ),
    q(
        "If lim(x->a+) f(x) != lim(x->a-) f(x), the discontinuity at a is:",
        "Jump discontinuity",
        ["Removable", "No discontinuity", "Always infinite"],
    ),
]

BANK_DIFFERENTIABILITY: QuestionBank = [
    q(
        "f is differentiable at x = a if:",
        "f'(a) = lim(h->0) (f(a+h) - f(a))/h exists",
        ["f(a) = 0", "f is continuous only", "f is constant"],
    ),
    q(
        "If f is differentiable at a, then f is:",
        "Continuous at a",
        ["Discontinuous at a", "Not necessarily continuous", "Constant near a"],
    ),
    q(
        "The function f(x) = |x| at x = 0 is:",
        "Continuous but not differentiable",
        ["Differentiable", "Neither continuous nor differentiable", "Differentiable with f'(0) = 1"],
    ),
    q(
        "If f'(a) exists, the tangent line slope at (a, f(a)) is:",
        "f'(a)",
        ["f(a)", "1/f'(a)", "Always zero"],
    ),
    q(
        "The derivative of x^n is:",
        "n x^(n-1)",
        ["x^(n-1)", "n x^n", "x^n / n"],
    ),
    q(
        "If f(x) = sin x, then f'(x) equals:",
        "cos x",
        ["-cos x", "sin x", "-sin x"],
    ),
    q(
        "The function with a sharp corner at x = a typically has:",
        "No derivative at a",
        ["Derivative zero", "Derivative undefined only if discontinuous", "Derivative equal to left slope always"],
    ),
    q(
        "If f and g are differentiable, (fg)' equals:",
        "f'g + fg'",
        ["f'g'", "(f/g)'", "f' + g'"],
    ),
]

BANK_DERIV_ITF_EXP: QuestionBank = [
    q(
        "d/dx (sin^-1 x) equals:",
        "1/sqrt(1 - x^2)",
        ["-1/sqrt(1 - x^2)", "cos^-1 x", "1/(1 + x^2)"],
    ),
    q(
        "d/dx (tan^-1 x) equals:",
        "1/(1 + x^2)",
        ["1/sqrt(1 - x^2)", "-1/(1 + x^2)", "sec^2 x"],
    ),
    q(
        "d/dx (e^x) equals:",
        "e^x",
        ["x e^(x-1)", "e^(x-1)", "ln x"],
    ),
    q(
        "d/dx (a^x) for constant a > 0 equals:",
        "a^x ln a",
        ["a^x", "x a^(x-1)", "ln a"],
    ),
    q(
        "d/dx (cos^-1 x) equals:",
        "-1/sqrt(1 - x^2)",
        ["1/sqrt(1 - x^2)", "sin^-1 x", "-1/(1 + x^2)"],
    ),
    q(
        "d/dx (log_e x) for x > 0 equals:",
        "1/x",
        ["ln x", "e^x", "x"],
    ),
    q(
        "d/dx (2^x) equals:",
        "2^x ln 2",
        ["2^x", "x 2^(x-1)", "ln 2"],
    ),
    q(
        "d/dx (cot^-1 x) equals:",
        "-1/(1 + x^2)",
        ["1/(1 + x^2)", "1/sqrt(1-x^2)", "sec^2 x"],
    ),
]

# ---------------------------------------------------------------------------
# Application of Derivatives
# ---------------------------------------------------------------------------

BANK_RATE_OF_CHANGE: QuestionBank = [
    q(
        "If s(t) is displacement, velocity v(t) equals:",
        "ds/dt",
        ["d^2s/dt^2", "s/t", "integral of s"],
    ),
    q(
        "If the radius r of a circle increases at 2 cm/s, dr/dt equals:",
        "2 cm/s",
        ["pi cm/s", "r cm/s", "2pi cm/s"],
    ),
    q(
        "The rate of change of area A of a circle with respect to r is:",
        "dA/dr = 2pi r",
        ["pi r^2", "pi r", "2pi"],
    ),
    q(
        "If y = f(x) and x changes with time, dy/dt equals:",
        "(dy/dx)(dx/dt)",
        ["dy/dx only", "dx/dy", "f'(t)"],
    ),
    q(
        "Acceleration is the rate of change of:",
        "Velocity with respect to time",
        ["Displacement with respect to distance", "Force with respect to mass", "Energy with respect to time only"],
    ),
    q(
        "A spherical balloon's volume V = (4/3)pi r^3. dV/dr equals:",
        "4 pi r^2",
        ["(4/3) pi r^2", "4 pi r", "pi r^3"],
    ),
    q(
        "If cost C(x) gives cost for x units, marginal cost at x is approximated by:",
        "dC/dx",
        ["C/x", "C(x+1) - C(x) only without limit", "integral C"],
    ),
    q(
        "Related rates problems require:",
        "Differentiating an equation relating variables with respect to time",
        ["Only algebra", "Integration first always", "No chain rule"],
    ),
]

BANK_INCREASING_DECREASING: QuestionBank = [
    q(
        "If f'(x) > 0 on an interval, then f is:",
        "Strictly increasing on that interval",
        ["Decreasing", "Constant", "Not continuous"],
    ),
    q(
        "If f'(x) < 0 on (a,b), then f is:",
        "Decreasing on (a,b)",
        ["Increasing", "Constant", "Undefined"],
    ),
    q(
        "Critical points of f occur where:",
        "f'(x) = 0 or f' is undefined",
        ["f(x) = 0 only", "f''(x) = 0 only", "x = 0 only"],
    ),
    q(
        "If f'(x) changes from + to - at x = c, then f has at c:",
        "Local maximum",
        ["Local minimum", "Inflection point always", "No extremum"],
    ),
    q(
        "The function f(x) = x^3 - 3x has critical points at:",
        "x = +/- 1",
        ["x = 0 only", "x = +/- 3", "No critical points"],
    ),
    q(
        "On (0, pi), sin x is:",
        "Increasing",
        ["Decreasing", "Constant", "Not differentiable"],
    ),
    q(
        "If f is increasing on [a,b], then for a < x1 < x2 < b:",
        "f(x1) < f(x2)",
        ["f(x1) > f(x2)", "f(x1) = f(x2)", "f'(x) < 0"],
    ),
    q(
        "f'(x) = 0 at every point of an interval implies f is:",
        "Constant on that interval",
        ["Linear with non-zero slope", "Quadratic", "Always zero function only on R"],
    ),
]

BANK_MAXIMA_MINIMA: QuestionBank = [
    q(
        "A local maximum of f at x = c means:",
        "f(c) >= f(x) for x near c",
        ["f(c) is global minimum", "f'(c) must be undefined", "f''(c) > 0 always"],
    ),
    q(
        "Second derivative test: if f'(c) = 0 and f''(c) > 0, then:",
        "Local minimum at c",
        ["Local maximum at c", "Inflection at c", "No conclusion"],
    ),
    q(
        "On a closed interval [a,b], absolute extrema of continuous f occur at:",
        "Critical points inside (a,b) or endpoints a, b",
        ["Critical points only", "Endpoints only", "Midpoint only"],
    ),
    q(
        "For f(x) = x^2 - 4x + 5, the minimum value is:",
        "1 at x = 2",
        ["5 at x = 0", "0 at x = 2", "-1 at x = 2"],
    ),
    q(
        "If f''(c) < 0 and f'(c) = 0, then f has:",
        "Local maximum at c",
        ["Local minimum", "Neither max nor min", "Discontinuity"],
    ),
    q(
        "The maximum area of a rectangle with perimeter 20 is when sides are:",
        "5 and 5",
        ["10 and 0", "4 and 6 only", "2 and 8 only"],
    ),
    q(
        "For f(x) = -x^2 + 4x, the maximum value on R is:",
        "4",
        ["0", "2", "8"],
    ),
    q(
        "A point of inflection is where:",
        "Concavity changes (often f'' = 0 and sign change)",
        ["f' = 0 always", "f = 0", "Function is undefined"],
    ),
]

# ---------------------------------------------------------------------------
# Integrals
# ---------------------------------------------------------------------------

BANK_INDEFINITE_INTEGRALS: QuestionBank = [
    q(
        "Integral of x^n dx for n != -1 equals:",
        "x^(n+1)/(n+1) + C",
        ["n x^(n-1) + C", "x^n + C", "x^(n+1) + C"],
    ),
    q(
        "Integral of e^x dx equals:",
        "e^x + C",
        ["x e^x + C", "e^(x+1)/(x+1) + C", "ln x + C"],
    ),
    q(
        "Integral of 1/x dx equals:",
        "ln|x| + C",
        ["1/x^2 + C", "x ln x + C", "ln x + C for all x without absolute value always wrong on negatives"],
    ),
    q(
        "Integral of cos x dx equals:",
        "sin x + C",
        ["-sin x + C", "-cos x + C", "cos x + C"],
    ),
    q(
        "Integral of sec^2 x dx equals:",
        "tan x + C",
        ["sec x + C", "sec x tan x + C", "cot x + C"],
    ),
    q(
        "The constant C in indefinite integrals represents:",
        "An arbitrary constant of integration",
        ["Always zero", "The lower limit", "Slope of tangent"],
    ),
    q(
        "Integral of sin x dx equals:",
        "-cos x + C",
        ["cos x + C", "sin x + C", "-sin x + C"],
    ),
    q(
        "d/dx (integral f(x) dx) equals:",
        "f(x)",
        ["F(x) + C", "integral f(x) dx", "f'(x)"],
    ),
]

BANK_METHODS_INTEGRATION: QuestionBank = [
    q(
        "Integration by substitution is useful when integrand contains:",
        "Function and its derivative (up to constant)",
        ["Only polynomials", "Only trigonometric without chain", "Always requires partial fractions"],
    ),
    q(
        "Integral of x e^(x^2) dx uses substitution u =:",
        "x^2",
        ["x", "e^x", "x^3"],
    ),
    q(
        "Integration by parts formula: integral u dv equals:",
        "u v - integral v du",
        ["u v + integral v du", "integral u du + integral v dv", "u' v'"],
    ),
    q(
        "For integral x cos x dx, choose u = x and dv = cos x dx to get:",
        "x sin x + cos x + C",
        ["x sin x - cos x + C", "-x sin x + cos x + C", "sin x + C"],
    ),
    q(
        "Partial fractions apply to rational functions where:",
        "Denominator factors into linear/quadratic factors",
        ["Numerator is zero", "Degree of numerator exceeds denominator without division", "Integrand is e^x"],
    ),
    q(
        "Integral of 1/(x^2 - a^2) dx involves terms like:",
        "(1/(2a)) ln|(x-a)/(x+a)| + C",
        ["ln(x^2) + C", "tan^-1(x/a) only always", "1/(x^2) + C"],
    ),
    q(
        "Integral of 1/(1 + x^2) dx equals:",
        "tan^-1 x + C",
        ["ln(1 + x^2) + C", "sin^-1 x + C", "cot^-1 x + C"],
    ),
    q(
        "To integrate sin^2 x, use identity:",
        "sin^2 x = (1 - cos 2x)/2",
        ["sin^2 x = 1 - cos^2 x only without half angle", "sin x = cos x", "sin^2 x = cos^2 x"],
    ),
]

BANK_DEFINITE_INTEGRALS: QuestionBank = [
    q(
        "Integral from a to b of f(x) dx represents:",
        "Signed area under y = f(x) from x = a to x = b",
        ["Always positive area only", "Slope at b", "f(b) - f(a) always"],
    ),
    q(
        "If F'(x) = f(x), then integral_a^b f(x) dx equals:",
        "F(b) - F(a)",
        ["F(a) - F(b)", "F(b) + F(a)", "f(b) - f(a)"],
    ),
    q(
        "Integral_0^1 x^2 dx equals:",
        "1/3",
        ["1/2", "1", "2/3"],
    ),
    q(
        "For even function f, integral_{-a}^{a} f(x) dx equals:",
        "2 integral_0^a f(x) dx",
        ["0 always", "integral_0^a f(x) dx", "Undefined"],
    ),
    q(
        "For odd function f, integral_{-a}^{a} f(x) dx equals:",
        "0",
        ["2 integral_0^a f(x) dx", "a f(a)", "Undefined always"],
    ),
    q(
        "Integral_0^{pi/2} sin x dx equals:",
        "1",
        ["0", "pi/2", "2"],
    ),
    q(
        "If f(x) >= 0 on [a,b], integral_a^b f(x) dx is:",
        "Non-negative",
        ["Always zero", "Always negative", "Equal to f(b)"],
    ),
    q(
        "Integral_a^a f(x) dx equals:",
        "0",
        ["f(a)", "1", "Undefined"],
    ),
]

# ---------------------------------------------------------------------------
# Application of Integrals
# ---------------------------------------------------------------------------

BANK_AREA_SIMPLE_CURVES: QuestionBank = [
    q(
        "Area bounded by y = f(x), x-axis, x = a, x = b (f >= 0) is:",
        "Integral_a^b f(x) dx",
        ["f(b) - f(a)", "Integral f'(x) dx", "pi integral f(x)^2 dx"],
    ),
    q(
        "Area under y = x from x = 0 to x = 2 equals:",
        "2",
        ["4", "1", "sqrt(2)"],
    ),
    q(
        "Area under y = sqrt(4 - x^2) from x = -2 to 2 is a:",
        "Semicircle of radius 2 with area 2pi",
        ["Rectangle area 8", "Triangle area 4", "Full circle area 4pi"],
    ),
    q(
        "If f(x) <= 0 on [a,b], area between curve and x-axis is:",
        "|Integral_a^b f(x) dx|",
        ["Integral without absolute value always positive", "Zero", "f(a) - f(b)"],
    ),
    q(
        "Area under y = e^x from x = 0 to x = 1 equals:",
        "e - 1",
        ["e", "1", "e + 1"],
    ),
    q(
        "Area bounded by y = x^2, x = 0, x = 2, y = 0 equals:",
        "8/3",
        ["4", "2", "16/3"],
    ),
    q(
        "To find area with respect to y-axis, integrate with respect to:",
        "y (use x = g(y) if needed)",
        ["x only always", "t", "Never possible"],
    ),
    q(
        "Area under y = sin x from 0 to pi equals:",
        "2",
        ["0", "1", "pi"],
    ),
]

BANK_AREA_BETWEEN_CURVES: QuestionBank = [
    q(
        "Area between y = f(x) and y = g(x) on [a,b] where f >= g is:",
        "Integral_a^b (f(x) - g(x)) dx",
        ["Integral (f + g) dx", "f(b) - g(a)", "Integral f dx only"],
    ),
    q(
        "Curves y = x and y = x^2 intersect at:",
        "x = 0 and x = 1",
        ["x = 0 only", "x = -1 and 1", "No intersection"],
    ),
    q(
        "Area between y = x and y = x^2 from 0 to 1 equals:",
        "1/6",
        ["1/2", "1/3", "1/12"],
    ),
    q(
        "When finding area between curves, integration limits are usually:",
        "x-values of intersection points",
        ["Always 0 to 1", "y-intercepts only", "Endpoints of domain of one function only"],
    ),
    q(
        "Area between y = sin x and y = cos x on [0, pi/4] uses integrand:",
        "cos x - sin x (since cos >= sin there)",
        ["sin x - cos x always", "sin x + cos x", "sin x cos x"],
    ),
    q(
        "If two curves cross at x = a and x = b, total area may require:",
        "Splitting integral where upper/lower curves switch",
        ["Single integral always", "No integration", "Only differentiation"],
    ),
    q(
        "Area between parabolas y^2 = x and x = y is found by solving:",
        "Intersection points then integrating difference",
        ["Only one curve", "Adding areas of triangles", "Using determinants"],
    ),
    q(
        "Between x = 0 and x = 1, which is larger: y = x or y = x^2?",
        "y = x (for 0 < x < 1, x > x^2)",
        ["y = x^2", "Equal everywhere", "Depends on x = 0 only"],
    ),
]

BANK_AOI_APPLICATIONS: QuestionBank = [
    q(
        "Volume of solid with cross-section area A(x) from x = a to b is:",
        "Integral_a^b A(x) dx",
        ["A(b) - A(a)", "pi integral A(x) always", "Sum of A at endpoints only"],
    ),
    q(
        "Rotating y = f(x) about x-axis gives volume element:",
        "pi y^2 dx",
        ["2 pi y dx only", "y dx", "pi x^2 dy always"],
    ),
    q(
        "Displacement from velocity v(t) from t = a to t = b is:",
        "Integral_a^b v(t) dt",
        ["v(b) - v(a)", "a v(b)", "Derivative of v"],
    ),
    q(
        "Average value of f on [a,b] is:",
        "(1/(b-a)) integral_a^b f(x) dx",
        ["f((a+b)/2)", "integral f without dividing", "f(b) - f(a)"],
    ),
    q(
        "Work done by variable force F(x) from x = a to b is:",
        "Integral_a^b F(x) dx",
        ["F(b) - F(a) only without integral for variable force", "m g h always", "Zero"],
    ),
    q(
        "Area interpretation of definite integral fails as plain geometry when:",
        "Region is bounded by curves requiring subtraction of areas",
        ["f is linear", "Limits are equal", "f is constant"],
    ),
    q(
        "For a tank draining, if dV/dt = -k sqrt(h), related rates link:",
        "Volume, height, and time via chain rule",
        ["Only algebra", "Bayes theorem", "Matrix inverse"],
    ),
    q(
        "Consumer surplus in economics can be modeled using:",
        "Definite integrals of demand curves",
        ["Arithmetic progression sums", "Determinants only", "Conditional probability only"],
    ),
]

# ---------------------------------------------------------------------------
# Differential Equations
# ---------------------------------------------------------------------------

BANK_DE_ORDER_DEGREE: QuestionBank = [
    q(
        "The order of a differential equation is:",
        "Order of the highest derivative present",
        ["Power of highest derivative always", "Number of arbitrary constants", "Degree of polynomial in x"],
    ),
    q(
        "The degree of a differential equation (when defined) is:",
        "Power of the highest order derivative after making equation polynomial in derivatives",
        ["Same as order always", "Number of variables", "Order of lowest derivative"],
    ),
    q(
        "y'' + 3y' + 2y = 0 has order:",
        "2",
        ["1", "3", "0"],
    ),
    q(
        "dy/dx = x^2 has order:",
        "1",
        ["2", "0", "Undefined"],
    ),
    q(
        "(d^2y/dx^2)^3 + (dy/dx)^2 = 0 has order:",
        "2",
        ["3", "1", "5"],
    ),
    q(
        "Degree is defined only when the equation is:",
        "Polynomial in derivatives",
        ["Linear in x only", "Always for any DE", "Free of constants"],
    ),
    q(
        "y' = sin y has order:",
        "1",
        ["0", "2", "Depends on solution"],
    ),
    q(
        "The general solution of an nth order ODE contains:",
        "n arbitrary independent constants",
        ["No constants", "One constant always", "n^2 constants"],
    ),
]

BANK_DE_GENERAL_PARTICULAR: QuestionBank = [
    q(
        "A general solution of a differential equation contains:",
        "Arbitrary constants equal in number to the order",
        ["No constants", "Fixed numerical values only", "Only particular values"],
    ),
    q(
        "A particular solution is obtained from the general solution by:",
        "Assigning specific values to arbitrary constants using initial/boundary conditions",
        ["Differentiating again", "Removing all variables", "Doubling the order"],
    ),
    q(
        "If y = C e^(2x) is general solution, y = 3 e^(2x) is:",
        "A particular solution with C = 3",
        ["General solution", "Not a solution", "Only homogeneous"],
    ),
    q(
        "Initial condition y(0) = 1 on y = C e^x gives:",
        "C = 1",
        ["C = 0", "C = e", "No particular solution"],
    ),
    q(
        "Two solutions differing by arbitrary constant are:",
        "Members of the same general solution family",
        ["Always identical", "Always incompatible", "Not solutions"],
    ),
    q(
        "For y' = y with y(0) = 2, particular solution is:",
        "y = 2 e^x",
        ["y = e^x", "y = 2x", "y = x^2"],
    ),
    q(
        "Number of arbitrary constants in particular solution is:",
        "Zero",
        ["Equal to order", "One always", "Two always"],
    ),
    q(
        "If general solution is y = C1 cos x + C2 sin x, specifying y(0) and y'(0) gives:",
        "Unique C1, C2 for particular solution",
        ["No solution", "Infinitely many unrelated solutions", "Only C1"],
    ),
]

BANK_DE_FIRST_ORDER: QuestionBank = [
    q(
        "A first order DE has highest derivative:",
        "dy/dx (order 1)",
        ["d^2y/dx^2", "No derivative", "Third derivative"],
    ),
    q(
        "Separable equation form is:",
        "dy/dx = f(x) g(y)",
        ["y'' + y = 0 only", "Linear only", "Always homogeneous of degree 2"],
    ),
    q(
        "For dy/dx = y, separating variables gives:",
        "dy/y = dx (y != 0)",
        ["y dx = dy always without integration", "y = x", "No integration needed"],
    ),
    q(
        "General solution of dy/dx = ky is:",
        "y = C e^(kx)",
        ["y = kx + C", "y = C x^k", "y = e^x only"],
    ),
    q(
        "Linear first order form is:",
        "dy/dx + P(x) y = Q(x)",
        ["y^2 = x", "(dy/dx)^2 = y", "y'' = 0"],
    ),
    q(
        "Integrating factor for dy/dx + y = e^x is:",
        "e^x",
        ["e^(-x)", "x", "1"],
    ),
    q(
        "Homogeneous DE dy/dx = (y/x) has substitution:",
        "y = vx",
        ["x = vy only", "y = x^2", "No substitution"],
    ),
    q(
        "Solution of dy/dx = 1/y with y(1) = 2 satisfies:",
        "y^2/2 = x + C with C = 3/2",
        ["y = x + 1", "y = 2x", "y = ln x"],
    ),
]

# ---------------------------------------------------------------------------
# Vector Algebra
# ---------------------------------------------------------------------------

BANK_VECTOR_TYPES: QuestionBank = [
    q(
        "A vector quantity has:",
        "Magnitude and direction",
        ["Magnitude only", "Direction only", "Neither"],
    ),
    q(
        "Two vectors are equal if they have:",
        "Same magnitude and same direction",
        ["Same initial point only", "Same magnitude only", "Same direction only"],
    ),
    q(
        "A zero vector has:",
        "Magnitude 0 and arbitrary direction",
        ["Magnitude 1", "No representation", "Direction along x only"],
    ),
    q(
        "Unit vector in direction of a is:",
        "a/|a| (if a != 0)",
        ["a x a", "|a| a", "a^2"],
    ),
    q(
        "Collinear vectors lie:",
        "Along the same or parallel lines",
        ["Always perpendicular", "In different planes only", "Only in 3D"],
    ),
    q(
        "Position vector of point P relative to origin O is:",
        "OP vector",
        ["Scalar OP distance only", "Unit vector only", "Zero always"],
    ),
    q(
        "If |a| = 3, then |-a| equals:",
        "3",
        ["-3", "0", "9"],
    ),
    q(
        "A vector in 3D with components (x,y,z) has magnitude:",
        "sqrt(x^2 + y^2 + z^2)",
        ["x + y + z", "x^2 + y^2 + z^2", "max(x,y,z)"],
    ),
]

BANK_VECTOR_ADDITION: QuestionBank = [
    q(
        "Triangle law of vector addition: for sides OA and AB, OB equals:",
        "OA + AB",
        ["OA - AB", "AB - OA", "OA x AB"],
    ),
    q(
        "Parallelogram law gives sum of adjacent sides as:",
        "Diagonal from common point",
        ["Shorter side", "Product of sides", "Zero vector always"],
    ),
    q(
        "Vector addition is:",
        "Commutative: a + b = b + a",
        ["Not commutative", "Only for unit vectors", "Undefined in 3D"],
    ),
    q(
        "a + (-a) equals:",
        "Zero vector",
        ["Unit vector", "2a", "a^2"],
    ),
    q(
        "If a = (1,2,3) and b = (4,5,6), then a + b equals:",
        "(5, 7, 9)",
        ["(4, 10, 18)", "(3, 3, 3)", "(5, 5, 5)"],
    ),
    q(
        "Subtraction a - b equals:",
        "a + (-b)",
        ["b - a always", "a x b", "|a| - |b|"],
    ),
    q(
        "If R is resultant of P and Q, |R| is maximum when:",
        "P and Q are in same direction",
        ["Perpendicular", "Opposite direction", "Unrelated"],
    ),
    q(
        "If |P| = 3 and |Q| = 4 and angle between them 90°, |P + Q| equals:",
        "5",
        ["7", "1", "12"],
    ),
]

BANK_VECTOR_PRODUCTS: QuestionBank = [
    q(
        "Scalar product a . b equals:",
        "|a||b| cos theta",
        ["|a||b| sin theta", "|a x b|", "a + b"],
    ),
    q(
        "If a . b = 0 with non-zero a and b, vectors are:",
        "Perpendicular",
        ["Parallel", "Equal", "Collinear"],
    ),
    q(
        "Vector product a x b has magnitude:",
        "|a||b| sin theta",
        ["|a||b| cos theta", "a . b", "Zero always"],
    ),
    q(
        "Direction of a x b (right-hand rule) is:",
        "Perpendicular to plane of a and b",
        ["Parallel to a", "Parallel to b", "Same as a + b"],
    ),
    q(
        "i . j equals:",
        "0",
        ["1", "-1", "i"],
    ),
    q(
        "i x j equals:",
        "k",
        ["0", "j", "-k"],
    ),
    q(
        "If a = (1,0,0) and b = (0,1,0), then a . b equals:",
        "0",
        ["1", "-1", "2"],
    ),
    q(
        "Area of parallelogram with adjacent sides a and b is:",
        "|a x b|",
        ["a . b", "|a| + |b|", "|a| - |b|"],
    ),
]

# ---------------------------------------------------------------------------
# Three Dimensional Geometry
# ---------------------------------------------------------------------------

BANK_3D_DIRECTION: QuestionBank = [
    q(
        "Direction cosines l, m, n of a line satisfy:",
        "l^2 + m^2 + n^2 = 1",
        ["l + m + n = 1", "l m n = 1", "l = m = n always"],
    ),
    q(
        "Direction ratios (a,b,c) are proportional to:",
        "Direction cosines",
        ["Reciprocals of cosines always", "Slopes only", "Intercept lengths always"],
    ),
    q(
        "If direction ratios are (2,2,1), a possible set of direction cosines scales so that:",
        "Sum of squares of cosines is 1",
        ["Sum of ratios is 1", "Product is 1", "All equal 1"],
    ),
    q(
        "Angle between lines with direction cosines (l1,m1,n1) and (l2,m2,n2) uses:",
        "cos theta = l1 l2 + m1 m2 + n1 n2",
        ["l1 + l2 only", "Cross product only in 2D", "sin theta = sum"],
    ),
    q(
        "Direction cosines of x-axis are:",
        "(1, 0, 0)",
        ["(0,1,0)", "(0,0,1)", "(1,1,1)"],
    ),
    q(
        "If a line makes equal angles with coordinate axes, direction cosines are:",
        "Each +/- 1/sqrt(3)",
        ["All 1", "All 0", "1, 0, 0 only"],
    ),
    q(
        "Direction ratios (0,0,1) represent a line:",
        "Parallel to z-axis",
        ["Parallel to x-axis", "In xy-plane only", "Through origin only"],
    ),
    q(
        "If l = 0 for a line, the line is perpendicular to:",
        "x-axis",
        ["y-axis", "z-axis", "All axes"],
    ),
]

BANK_3D_LINE: QuestionBank = [
    q(
        "Vector equation of line through point a with direction b is:",
        "r = a + lambda b",
        ["r = a . b", "r = a x b only", "r = lambda a only"],
    ),
    q(
        "Cartesian form of line through (x1,y1,z1) with d.r. (a,b,c) is:",
        "(x-x1)/a = (y-y1)/b = (z-z1)/c",
        ["x + y + z = 0", "ax + by + cz = 1 only", "y = mx + c in 3D without z"],
    ),
    q(
        "Angle between two lines depends on:",
        "Their direction vectors/ratios",
        ["Only points on lines", "Only z-intercepts", "Area between lines"],
    ),
    q(
        "Skew lines in 3D are:",
        "Non-parallel, non-intersecting",
        ["Always parallel", "Always intersecting", "Same as coplanar"],
    ),
    q(
        "Shortest distance between parallel lines depends on:",
        "Separation perpendicular to direction",
        ["Sum of lengths", "Dot product of position vectors only", "Always zero"],
    ),
    q(
        "If direction ratios are proportional, lines are:",
        "Parallel",
        ["Perpendicular", "Skew always", "Identical always"],
    ),
    q(
        "Line r = (1,2,3) + t(1,0,0) is parallel to:",
        "x-axis",
        ["y-axis", "z-axis", "xy-plane only"],
    ),
    q(
        "Two lines intersect if:",
        "They share a common point and are not parallel",
        ["They are parallel", "Direction ratios differ", "They are skew"],
    ),
]

BANK_3D_PLANE: QuestionBank = [
    q(
        "Cartesian equation of a plane is:",
        "ax + by + cz + d = 0 (not all a,b,c zero)",
        ["y = mx + c only", "x^2 + y^2 = r^2 only", "r = a + tb"],
    ),
    q(
        "Normal vector to plane ax + by + cz + d = 0 is:",
        "(a, b, c)",
        ["(d, c, b)", "(1,1,1)", "Parallel to plane"],
    ),
    q(
        "Plane parallel to xy-plane has equation:",
        "z = k (constant)",
        ["x = k only", "y = k only", "x + y = 0"],
    ),
    q(
        "Distance of point (x1,y1,z1) from plane ax+by+cz+d=0 is:",
        "|a x1 + b y1 + c z1 + d| / sqrt(a^2+b^2+c^2)",
        ["a x1 + b y1 + c z1", "sqrt(a^2+b^2+c^2) only", "Zero always"],
    ),
    q(
        "If two planes have parallel normals, the planes are:",
        "Parallel or coincident",
        ["Always perpendicular", "Always intersecting at right angle", "Skew"],
    ),
    q(
        "Angle between planes equals angle between their:",
        "Normals",
        ["x-intercepts", "Distances from origin only", "Midpoints"],
    ),
    q(
        "Plane through origin with normal (1,2,3) has equation:",
        "x + 2y + 3z = 0",
        ["x + 2y + 3z = 1", "x = y = z", "z = 0 only"],
    ),
    q(
        "Vector equation of plane with normal n through point r0 is:",
        "(r - r0) . n = 0",
        ["r x n = 0 always", "r = r0 + n", "r . r0 = n"],
    ),
]

# ---------------------------------------------------------------------------
# Linear Programming
# ---------------------------------------------------------------------------

BANK_LP_PROBLEM: QuestionBank = [
    q(
        "A linear programming problem involves:",
        "Optimizing a linear objective function subject to linear constraints",
        ["Quadratic objective only", "No constraints", "Differentiating exponentials"],
    ),
    q(
        "Decision variables in LPP are:",
        "Quantities to be determined (non-negative usually)",
        ["Slack variables only", "Constants fixed", "Derivatives"],
    ),
    q(
        "Constraints in LPP are typically:",
        "Linear inequalities or equations",
        ["Always equalities only", "Non-linear always", "Without variables"],
    ),
    q(
        "Objective function Z = 3x + 2y is:",
        "Linear in x and y",
        ["Quadratic", "Exponential", "Constant"],
    ),
    q(
        "Feasible solutions satisfy:",
        "All constraints simultaneously",
        ["Only objective function", "No constraints", "Only one inequality"],
    ),
    q(
        "In standard form for graphical method, variables are often:",
        "Non-negative",
        ["Always negative", "Complex numbers", "Unrestricted without context"],
    ),
    q(
        "An infeasible LPP has:",
        "No point satisfying all constraints",
        ["Infinite optimal always", "Unique objective always zero", "No objective function"],
    ),
    q(
        "Slack variable is introduced to convert:",
        "Inequality to equality in standard form",
        ["Objective to quadratic", "Two variables to one", "Max to min without sign change"],
    ),
]

BANK_LP_GRAPHICAL: QuestionBank = [
    q(
        "Graphical method applies to LPP with:",
        "Two decision variables",
        ["Three variables always", "No variables", "Any number without limitation"],
    ),
    q(
        "Each linear constraint ax + by <= c graphs as:",
        "A half-plane including origin side (for c >= 0 typical setup)",
        ["A single point", "A circle", "A parabola"],
    ),
    q(
        "Optimal value of Z in bounded feasible region occurs at:",
        "A corner point of feasible region",
        ["Midpoint of any edge always", "Origin always", "Random interior point"],
    ),
    q(
        "To maximize Z = 2x + 3y, evaluate Z at:",
        "Vertices of feasible polygon",
        ["Only (0,0)", "Only one arbitrary point", "No vertices"],
    ),
    q(
        "If feasible region is unbounded, optimal solution may:",
        "Not exist or be unbounded depending on objective",
        ["Always exist at origin", "Always be zero", "Be found without checking corners"],
    ),
    q(
        "Intersection of constraint lines gives:",
        "Candidate corner points",
        ["Always infeasible points", "Only slacks", "Objective directly"],
    ),
    q(
        "For constraints x >= 0, y >= 0, the feasible region lies in:",
        "First quadrant (including axes)",
        ["Second quadrant", "Whole plane always", "Only negative axes"],
    ),
    q(
        "Parallel objective lines Z = constant shift in direction:",
        "Normal to level lines of Z (gradient direction)",
        ["Always vertical", "Random", "Perpendicular to constraints only"],
    ),
]

BANK_LP_FEASIBLE: QuestionBank = [
    q(
        "The feasible region is:",
        "Set of all points satisfying constraints",
        ["Set of optimal points only", "Empty always", "Only boundary without interior"],
    ),
    q(
        "A feasible region for two variables with linear constraints is usually:",
        "A convex polygon (possibly unbounded)",
        ["Always a circle", "Always a single point", "Non-convex always"],
    ),
    q(
        "If no corner point of feasible region gives maximum, and region unbounded:",
        "Maximum may not exist (objective unbounded)",
        ["Maximum is always 0", "Use derivative test", "No feasible region"],
    ),
    q(
        "Corner point method checks:",
        "Value of objective at each vertex of feasible polygon",
        ["Only slack variables", "Only midpoints", "Second derivatives"],
    ),
    q(
        "Redundant constraint:",
        "Does not change the feasible region",
        ["Makes region empty", "Is always objective", "Must be non-linear"],
    ),
    q(
        "For bounded feasible region with non-empty interior, optimal solution for LPP exists:",
        "At least at one corner point (fundamental theorem of LPP)",
        ["Never", "Only in interior always", "Only at origin"],
    ),
    q(
        "Two binding constraints at a corner point mean:",
        "Both equalities hold at that vertex",
        ["Objective is zero", "Region is unbounded", "No solution"],
    ),
    q(
        "Feasible region empty when constraints are:",
        "Mutually inconsistent",
        ["All parallel", "All identical", "Two variables only"],
    ),
]

# ---------------------------------------------------------------------------
# Probability
# ---------------------------------------------------------------------------

BANK_CONDITIONAL_PROB: QuestionBank = [
    q(
        "Conditional probability P(A|B) equals:",
        "P(A intersect B) / P(B), P(B) > 0",
        ["P(A)/P(B)", "P(A union B)", "P(A) P(B)"],
    ),
    q(
        "If A and B are independent, P(A|B) equals:",
        "P(A)",
        ["P(B)", "P(A) P(B)", "0"],
    ),
    q(
        "P(A intersect B) equals:",
        "P(B) P(A|B)",
        ["P(A) + P(B)", "P(A) - P(B)", "1 - P(A union B) always"],
    ),
    q(
        "If P(B) = 0, P(A|B) is:",
        "Undefined (not treated as 0 by definition)",
        ["0 always", "1 always", "Equal to P(A)"],
    ),
    q(
        "Drawing without replacement changes probabilities because events are:",
        "Dependent",
        ["Independent always", "Mutually exclusive always", "Impossible"],
    ),
    q(
        "For two events with P(B) > 0, P(A'|B) equals:",
        "1 - P(A|B)",
        ["P(A'|B')", "P(A|B')", "P(A') P(B)"],
    ),
    q(
        "A bag has 3 red, 2 blue. P(red on first draw) = 3/5. After one red removed, P(red second) =:",
        "2/4 = 1/2",
        ["3/5", "3/4", "1/5"],
    ),
    q(
        "Multiplication theorem: P(A intersect B) = P(A) P(B|A) also equals:",
        "P(B) P(A|B)",
        ["P(A) + P(B)", "P(A union B)", "1"],
    ),
]

BANK_BAYES: QuestionBank = [
    q(
        "Bayes' theorem states P(Ei|A) proportional to:",
        "P(Ei) P(A|Ei)",
        ["P(A) only", "P(Ei) only", "1/P(A|Ei)"],
    ),
    q(
        "In Bayes formula, P(Ei) is called:",
        "Prior probability",
        ["Likelihood only", "Posterior always", "Joint probability of A"],
    ),
    q(
        "P(Ei|A) in Bayes theorem is:",
        "Posterior probability",
        ["Prior", "Marginal of A only", "Always 1"],
    ),
    q(
        "Denominator in Bayes' theorem is:",
        "P(A) = sum P(Ei) P(A|Ei)",
        ["P(Ei) only", "Zero", "P(A|Ei) only"],
    ),
    q(
        "Partition E1, E2, ..., En means:",
        "Mutually exclusive and exhaustive events",
        ["Independent only", "All equal probability", "Single event"],
    ),
    q(
        "If disease prevalence 1% and test sensitivity 99%, Bayes helps find:",
        "P(disease|positive test)",
        ["P(test|healthy) only", "Mean of test scores", "Variance only"],
    ),
    q(
        "Total probability: P(A) equals:",
        "Sum over partition of P(Ei) P(A|Ei)",
        ["P(A|E1) only", "Product of all P(Ei)", "Max P(A|Ei)"],
    ),
    q(
        "Bayes reverses conditioning from P(A|B) to:",
        "P(B|A) using priors and likelihoods",
        ["P(A union B)", "P(A) P(B) always", "P(A - B)"],
    ),
]

BANK_RANDOM_VARIABLES: QuestionBank = [
    q(
        "A discrete random variable takes:",
        "Countable values (often finite)",
        ["All real numbers always", "Only zero", "Continuous interval only"],
    ),
    q(
        "Probability mass function p(x) satisfies:",
        "Sum p(x) = 1 over all x",
        ["Integral equals 0", "p(x) > 1 allowed", "Sum equals 0"],
    ),
    q(
        "Expectation E(X) for discrete X equals:",
        "Sum x p(x)",
        ["Sum p(x) only", "Product of outcomes", "Variance always"],
    ),
    q(
        "Var(X) equals:",
        "E(X^2) - [E(X)]^2",
        ["E(X)^2", "E(X) + E(X^2)", "sqrt(E(X^2))"],
    ),
    q(
        "For fair die, E(X) where X is face value equals:",
        "3.5",
        ["3", "4", "7/3"],
    ),
    q(
        "If Y = aX + b, then E(Y) equals:",
        "a E(X) + b",
        ["a E(X)", "E(X) + b only", "a^2 E(X)"],
    ),
    q(
        "Bernoulli trial random variable has E(X) =:",
        "p (success probability)",
        ["1 - p", "p(1-p)", "0 always"],
    ),
    q(
        "Standard deviation is:",
        "sqrt(Var(X))",
        ["Var(X)^2", "E(X)", "E(X^2) always"],
    ),
]

# ---------------------------------------------------------------------------
# Chapter-scoped banks (colliding generic topic titles)
# ---------------------------------------------------------------------------

CHAPTER_TOPIC_BANKS: dict[tuple[str, str], QuestionBank] = {
    ("Inverse Trigonometric Functions", "Basic concepts"): BANK_ITF_BASIC,
    ("Inverse Trigonometric Functions", "Properties"): BANK_ITF_PROPERTIES,
    ("Determinants", "Properties"): BANK_DET_PROPERTIES,
    ("Application of Integrals", "Applications"): BANK_AOI_APPLICATIONS,
    ("Linear Programming", "Graphical method"): BANK_LP_GRAPHICAL,
}


def register() -> None:
    """Register all Class 12 Mathematics banks."""
    from app.data.quiz_concepts import GLOBAL_CHAPTER_TOPIC_BANKS

    register_keys(["types of relations"], BANK_TYPES_OF_RELATIONS)
    register_keys(["types of functions"], BANK_TYPES_OF_FUNCTIONS)
    register_keys(
        ["composition and invertible functions", "composition and invertible function"],
        BANK_COMPOSITION_INVERTIBLE,
    )
    register_keys(["principal values", "principal value"], BANK_ITF_PRINCIPAL_VALUES)
    register_keys(["types of matrices"], BANK_MATRIX_TYPES)
    register_keys(["operations on matrices"], BANK_MATRIX_OPERATIONS)
    register_keys(
        ["transpose and symmetric matrices", "transpose and symmetric matrix"],
        BANK_MATRIX_TRANSPOSE,
    )
    register_keys(
        ["determinant of a square matrix", "determinant of square matrix"],
        BANK_DET_SQUARE,
    )
    register_keys(["adjoint and inverse"], BANK_DET_ADJOINT_INVERSE)
    register_keys(["continuity"], BANK_CONTINUITY)
    register_keys(["differentiability"], BANK_DIFFERENTIABILITY)
    register_keys(
        [
            "derivatives of inverse trigonometric and exponential functions",
            "derivatives of inverse trigonometric and exponential function",
        ],
        BANK_DERIV_ITF_EXP,
    )
    register_keys(["rate of change"], BANK_RATE_OF_CHANGE)
    register_keys(
        ["increasing and decreasing functions", "increasing and decreasing function"],
        BANK_INCREASING_DECREASING,
    )
    register_keys(["maxima and minima", "maxima and minimum"], BANK_MAXIMA_MINIMA)
    register_keys(["indefinite integrals", "indefinite integral"], BANK_INDEFINITE_INTEGRALS)
    register_keys(["methods of integration", "method of integration"], BANK_METHODS_INTEGRATION)
    register_keys(["definite integrals", "definite integral"], BANK_DEFINITE_INTEGRALS)
    register_keys(
        ["area under simple curves", "area under simple curve"],
        BANK_AREA_SIMPLE_CURVES,
    )
    register_keys(
        ["area between two curves", "area between two curve"],
        BANK_AREA_BETWEEN_CURVES,
    )
    register_keys(["order and degree"], BANK_DE_ORDER_DEGREE)
    register_keys(
        ["general and particular solutions", "general and particular solution"],
        BANK_DE_GENERAL_PARTICULAR,
    )
    register_keys(
        ["first order differential equations", "first order differential equation"],
        BANK_DE_FIRST_ORDER,
    )
    register_keys(["types of vectors"], BANK_VECTOR_TYPES)
    register_keys(["addition of vectors", "addition of vector"], BANK_VECTOR_ADDITION)
    register_keys(
        ["scalar and vector products", "scalar and vector product"],
        BANK_VECTOR_PRODUCTS,
    )
    register_keys(
        ["direction cosines and ratios", "direction cosines and ratio"],
        BANK_3D_DIRECTION,
    )
    register_keys(["equation of a line", "equations of a line"], BANK_3D_LINE)
    register_keys(["plane"], BANK_3D_PLANE)
    register_keys(
        ["linear programming problem", "linear programming problems"],
        BANK_LP_PROBLEM,
    )
    register_keys(["feasible region"], BANK_LP_FEASIBLE)
    register_keys(["conditional probability"], BANK_CONDITIONAL_PROB)
    register_keys(["bayes' theorem", "bayes theorem"], BANK_BAYES)
    register_keys(["random variables", "random variable"], BANK_RANDOM_VARIABLES)

    GLOBAL_CHAPTER_TOPIC_BANKS.update(CHAPTER_TOPIC_BANKS)

    register_subject_keywords(
        "MATH",
        [
            (("sin^-1", "cos^-1", "tan^-1", "inverse trigonometric", "principal value"), BANK_ITF_PRINCIPAL_VALUES),
            (("sin^-1", "cos^-1", "tan^-1", "inverse trigonometric"), BANK_ITF_BASIC),
            (("determinant", "adjoint", "cofactor", "|a|"), BANK_DET_PROPERTIES),
            (("definite integral", "area under", "area between"), BANK_AREA_SIMPLE_CURVES),
            (("feasible region", "corner point", "linear programming", "objective function"), BANK_LP_FEASIBLE),
            (("conditional probability", "bayes", "random variable"), BANK_CONDITIONAL_PROB),
            (("matrix", "matrices", "transpose", "symmetric matrix"), BANK_MATRIX_OPERATIONS),
            (("vector", "scalar product", "cross product", "dot product"), BANK_VECTOR_PRODUCTS),
            (("differential equation", "order and degree", "particular solution"), BANK_DE_FIRST_ORDER),
            (("derivative", "maxima", "minima", "rate of change"), BANK_MAXIMA_MINIMA),
        ],
    )
