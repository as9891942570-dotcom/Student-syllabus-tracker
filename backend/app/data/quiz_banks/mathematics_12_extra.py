"""EduQuest CBSE Class 12 Mathematics — additional NCERT-section MCQ banks."""

from __future__ import annotations

from app.data.quiz_banks.common import q, register_keys, register_subject_keywords
from app.data.quiz_concepts import QuestionBank

# ---------------------------------------------------------------------------
# Relations and Functions
# ---------------------------------------------------------------------------

BANK_EQUIVALENCE_RELATIONS: QuestionBank = [
    q(
        "On Z, the relation R = {(a, b) : a + b is even} is:",
        "An equivalence relation",
        ["Reflexive only", "Symmetric but not transitive", "Neither reflexive nor symmetric"],
    ),
    q(
        "If R is an equivalence relation on A, the equivalence class [a] of a in A is:",
        "The set of all elements related to a",
        ["The set {a} only", "The complement of {a}", "All pairs (a, b) in A x A"],
    ),
    q(
        "On {1, 2, 3, 4}, R = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 3), (3, 1)} is an equivalence relation. [1] equals:",
        "{1, 3}",
        ["{1}", "{1, 2, 3, 4}", "{3, 4}"],
    ),
    q(
        "Equivalence classes of an equivalence relation on A form a:",
        "Partition of A",
        ["Proper subset of A only", "Single set containing A", "Ordered pair of subsets"],
    ),
    q(
        "On R, the relation R = {(x, y) : x^2 = y^2} is:",
        "An equivalence relation",
        ["Reflexive but not symmetric", "Symmetric but not reflexive", "Not transitive"],
    ),
    q(
        "If R is an equivalence relation on a finite set A with 12 elements and each class has 3 elements, number of classes is:",
        "4",
        ["3", "6", "12"],
    ),
]

BANK_BINARY_OPERATIONS: QuestionBank = [
    q(
        "A binary operation * on a set A is a function from:",
        "A x A to A",
        ["A to A x A", "A to R only", "R x R to Z only"],
    ),
    q(
        "On Z, define a * b = a + b + 1. The identity element e, if it exists, satisfies a * e = a. Then e is:",
        "-1",
        ["0", "1", "No identity exists"],
    ),
    q(
        "On Q \\ {0}, a * b = ab. This operation is:",
        "Commutative and associative",
        ["Commutative but not associative", "Associative but not commutative", "Neither"],
    ),
    q(
        "On Z, a * b = |a - b|. This operation is:",
        "Commutative but not associative",
        ["Associative and commutative", "Associative but not commutative", "Neither commutative nor associative"],
    ),
    q(
        "If * is associative on A with identity e, the inverse of a (if it exists) is an element b such that:",
        "a * b = b * a = e",
        ["a * b = a", "b * a = b", "a * b = a * a"],
    ),
    q(
        "On R, a * b = max(a, b). The identity element is:",
        "No identity element on all R",
        ["0", "-infinity", "1"],
    ),
]

BANK_ITF_GRAPHS: QuestionBank = [
    q(
        "The graph of y = sin^-1 x is obtained by reflecting the graph of y = sin x about:",
        "The line y = x, restricted to principal branch",
        ["The x-axis only", "The y-axis only", "The origin without restriction"],
    ),
    q(
        "The domain of y = cos^-1 x is:",
        "[-1, 1]",
        ["All real numbers", "[0, pi]", "[-pi/2, pi/2]"],
    ),
    q(
        "The graph of y = tan^-1 x has horizontal asymptotes at:",
        "y = pi/2 and y = -pi/2",
        ["y = 0 and y = pi", "x = 1 and x = -1", "No asymptotes"],
    ),
    q(
        "y = sin^-1 x and y = cos^-1 x are reflections of each other about:",
        "y = pi/4 for x in [0, 1]",
        ["The x-axis for all x", "y = x for all x", "The y-axis"],
    ),
    q(
        "The graph of y = cot^-1 x is strictly:",
        "Decreasing on its domain",
        ["Increasing on its domain", "Constant on (-1, 1)", "Discontinuous at x = 0 only"],
    ),
    q(
        "For x in [-1, 1], sin^-1 x + cos^-1 x equals:",
        "pi/2",
        ["pi", "0", "x"],
    ),
]

# ---------------------------------------------------------------------------
# Matrices and Determinants
# ---------------------------------------------------------------------------

BANK_MATRIX_ELEMENTARY_INVERTIBLE: QuestionBank = [
    q(
        "Elementary row operation R_i -> R_i + k R_j corresponds to multiplying on the left by:",
        "An elementary matrix",
        ["A diagonal matrix only", "The identity matrix always", "A permutation matrix only"],
    ),
    q(
        "A square matrix is invertible if and only if it is:",
        "Non-singular (det != 0)",
        ["Symmetric", "Diagonal", "Upper triangular only"],
    ),
    q(
        "If A is invertible, (AB)^-1 equals:",
        "B^-1 A^-1",
        ["A^-1 B^-1", "(AB)^T", "A^-1 + B^-1"],
    ),
    q(
        "Elementary matrices are always:",
        "Invertible",
        ["Singular", "Symmetric", "Orthogonal always"],
    ),
    q(
        "If A is 3x3 with det(A) = 2, then det(A^-1) equals:",
        "1/2",
        ["2", "-2", "1/8"],
    ),
    q(
        "Reducing [A | I] to [I | A^-1] uses only:",
        "Elementary row operations",
        ["Elementary column operations only", "Scalar multiplication of A only", "Transposition only"],
    ),
]

BANK_AREA_TRIANGLE: QuestionBank = [
    q(
        "Area of triangle with vertices (x1, y1), (x2, y2), (x3, y3) is (1/2)|det| where the matrix rows are:",
        "(x1, y1, 1), (x2, y2, 1), (x3, y3, 1)",
        ["(x1, y1), (x2, y2), (x3, y3)", "(1, x1, y1), (1, x2, y2), (1, x3, y3)", "(x1, 1, y1), (x2, 1, y2), (x3, 1, y3)"],
    ),
    q(
        "Vertices (0, 0), (4, 0), (0, 3). Area of the triangle is:",
        "6 square units",
        ["12 square units", "7 square units", "5 square units"],
    ),
    q(
        "If three points are collinear, the determinant in the area formula equals:",
        "0",
        ["1", "Always positive", "Always negative"],
    ),
    q(
        "Area of triangle with vertices (1, 2), (3, 4), (5, 6) is:",
        "0",
        ["2", "4", "sqrt(2)"],
    ),
    q(
        "For vertices (2, 1), (6, 1), (4, 5), area equals:",
        "8 square units",
        ["4 square units", "16 square units", "10 square units"],
    ),
    q(
        "The area formula using determinants gives a non-negative value because we take:",
        "Absolute value of the determinant",
        ["Square root of the determinant", "Negative of the determinant always", "Reciprocal of the determinant"],
    ),
]

BANK_MINORS_COFACTORS: QuestionBank = [
    q(
        "The minor M_ij of a matrix is:",
        "Determinant of the submatrix obtained by deleting row i and column j",
        ["The element a_ij itself", "Sum of row i", "Product of diagonal elements"],
    ),
    q(
        "The cofactor C_ij equals:",
        "(-1)^(i+j) M_ij",
        ["M_ij only", "(-1)^i M_ij", "M_ij / det(A)"],
    ),
    q(
        "For A = [[2, 1], [3, 4]], the cofactor C_11 is:",
        "4",
        ["1", "-3", "2"],
    ),
    q(
        "For the same matrix, cofactor C_12 is:",
        "-3",
        ["3", "-4", "1"],
    ),
    q(
        "The adjoint of A is the transpose of the matrix of:",
        "Cofactors",
        ["Minors only", "Elements of A", "Row sums"],
    ),
    q(
        "Sum of products of elements of a row with their cofactors equals:",
        "det(A)",
        ["0 always", "Trace of A", "1 always"],
    ),
]

BANK_LINEAR_SYSTEMS_DETERMINANTS: QuestionBank = [
    q(
        "For system AX = B with det(A) != 0, Cramer's rule gives x_i as:",
        "det(A_i) / det(A), where A_i is A with column i replaced by B",
        ["det(A) / det(A_i)", "det(A_i) only", "1 / det(A)"],
    ),
    q(
        "If det(A) = 0 for a 3x3 system, the system may have:",
        "No solution or infinitely many solutions",
        ["Exactly one solution always", "Exactly two solutions", "Always infinitely many solutions"],
    ),
    q(
        "Solve using determinants: x + y = 5, x - y = 1. Then x equals:",
        "3",
        ["2", "4", "5"],
    ),
    q(
        "For a homogeneous system AX = 0, if det(A) != 0, the only solution is:",
        "The trivial solution X = 0",
        ["Infinitely many non-zero solutions", "Exactly two solutions", "No solution"],
    ),
    q(
        "If det(A) = 0 and all det(A_i) = 0 for an inconsistent system, the system is:",
        "Consistent with infinitely many solutions (for homogeneous) or needs further check for non-homogeneous",
        ["Always inconsistent", "Always has unique solution", "Always has exactly two solutions"],
    ),
    q(
        "Cramer's rule is practical mainly when:",
        "Matrix size is small (2x2 or 3x3)",
        ["Matrix is 100x100", "Matrix is diagonal only", "det(A) = 0"],
    ),
]

# ---------------------------------------------------------------------------
# Continuity and Differentiability
# ---------------------------------------------------------------------------

BANK_EXP_LOG_DERIVATIVES: QuestionBank = [
    q(
        "Derivative of a^x (a > 0, a != 1) with respect to x is:",
        "a^x ln(a)",
        ["x a^(x-1)", "a^x / x", "ln(a) only"],
    ),
    q(
        "If y = ln x, then dy/dx equals:",
        "1/x",
        ["x", "ln x", "e^x"],
    ),
    q(
        "Derivative of log_a x equals:",
        "1 / (x ln a)",
        ["1/x", "ln a / x", "a^x"],
    ),
    q(
        "If y = e^(2x), then dy/dx equals:",
        "2 e^(2x)",
        ["e^(2x)", "2x e^(x)", "e^x"],
    ),
    q(
        "Derivative of ln(sin x) is:",
        "cot x",
        ["tan x", "1/sin x", "cos x"],
    ),
    q(
        "If y = x^x, x > 0, then dy/dx equals:",
        "x^x (ln x + 1)",
        ["x x^(x-1)", "x^x ln x only", "x^(x-1)"],
    ),
]

BANK_SECOND_ORDER_DERIVATIVES: QuestionBank = [
    q(
        "If f(x) = x^4, then f''(x) equals:",
        "12 x^2",
        ["4 x^3", "24 x", "4 x^2"],
    ),
    q(
        "For y = sin x, d^2y/dx^2 equals:",
        "-sin x",
        ["sin x", "cos x", "-cos x"],
    ),
    q(
        "If y = e^x, then d^2y/dx^2 equals:",
        "e^x",
        ["x e^x", "0", "2 e^x"],
    ),
    q(
        "For y = ln x, the second derivative f''(x) equals:",
        "-1/x^2",
        ["1/x^2", "1/x", "ln x"],
    ),
    q(
        "If f'(x) > 0 and f''(x) < 0 on an interval, the graph is:",
        "Increasing and concave down",
        ["Increasing and concave up", "Decreasing and concave up", "Decreasing and concave down"],
    ),
    q(
        "For y = x e^x, y'' equals:",
        "e^x (x + 2)",
        ["x e^x", "e^x (x + 1)", "2 x e^x"],
    ),
]

BANK_MEAN_VALUE_THEOREMS: QuestionBank = [
    q(
        "Rolle's theorem requires f to be continuous on [a, b], differentiable on (a, b), and:",
        "f(a) = f(b)",
        ["f(a) = 0", "f(b) = 0", "f'(a) = f'(b)"],
    ),
    q(
        "Under Rolle's theorem, there exists c in (a, b) such that:",
        "f'(c) = 0",
        ["f(c) = 0", "f(c) = f(a)", "f''(c) = 0"],
    ),
    q(
        "Lagrange's mean value theorem states: f(b) - f(a) = f'(c)(b - a) for some c in:",
        "(a, b)",
        ["[a, b] including endpoints only", "(0, b)", "[0, 1] always"],
    ),
    q(
        "If f'(x) = 0 for all x in (a, b), then f is:",
        "Constant on [a, b]",
        ["Strictly increasing", "Strictly decreasing", "Always zero"],
    ),
    q(
        "For f(x) = x^2 on [1, 3], the c in Lagrange MVT satisfying f'(c) = (f(3)-f(1))/(3-1) is:",
        "2",
        ["1", "3", "4"],
    ),
    q(
        "Rolle's theorem is a special case of Lagrange MVT when:",
        "f(a) = f(b)",
        ["f is linear", "f'(x) > 0", "a = 0"],
    ),
]

BANK_TANGENTS_NORMALS: QuestionBank = [
    q(
        "Slope of tangent to y = f(x) at x = a is:",
        "f'(a)",
        ["f(a)", "1/f'(a)", "f''(a)"],
    ),
    q(
        "Equation of tangent to y = x^2 at (1, 1) is:",
        "y = 2x - 1",
        ["y = x", "y = 2x + 1", "y = x + 1"],
    ),
    q(
        "Slope of normal to the curve at a point is, if f'(a) != 0:",
        "-1 / f'(a)",
        ["f'(a)", "1 / f'(a)", "-f'(a)"],
    ),
    q(
        "For y = x^3 at x = 1, slope of normal is:",
        "-1/3",
        ["3", "-3", "1/3"],
    ),
    q(
        "Tangent to y = sin x at x = 0 has slope:",
        "1",
        ["0", "-1", "pi/2"],
    ),
    q(
        "If tangent is parallel to x-axis at x = a, then:",
        "f'(a) = 0",
        ["f(a) = 0", "f''(a) = 0", "f(a) = 1"],
    ),
]

BANK_APPROXIMATION_DIFFERENTIALS: QuestionBank = [
    q(
        "Linear approximation: f(a + h) approx f(a) + h f'(a) uses:",
        "First differential df = f'(a) h",
        ["Second derivative only", "Integral of f", "f(a) - h f'(a)"],
    ),
    q(
        "Approximate sqrt(4.1) using f(x) = sqrt(x) at a = 4, h = 0.1. f'(x) = 1/(2 sqrt(x)). Result approx:",
        "2.025",
        ["2.05", "2.1", "2.0025"],
    ),
    q(
        "If dx is small, dy approximates:",
        "Change in y along tangent line",
        ["Exact change in y always", "Second order change only", "Zero always"],
    ),
    q(
        "Approximate (1.02)^3 using f(x) = x^3 at a = 1, h = 0.02. f'(1) = 3. Value approx:",
        "1.06",
        ["1.02", "1.03", "1.002"],
    ),
    q(
        "Relative error in y is approx dy / y when:",
        "y != 0 and changes are small",
        ["y = 0 always", "Only for linear functions", "Never valid"],
    ),
    q(
        "For f(x) = e^x at x = 0, approximate e^0.01 as:",
        "1.01",
        ["1.001", "1.1", "0.99"],
    ),
]

# ---------------------------------------------------------------------------
# Integrals
# ---------------------------------------------------------------------------

BANK_INTEGRATION_BY_PARTS: QuestionBank = [
    q(
        "Integration by parts formula is:",
        "integral u dv = u v - integral v du",
        ["integral u dv = u v + integral v du", "integral u dv = v du", "integral u dv = u/v"],
    ),
    q(
        "To evaluate integral x e^x dx, choose u = x, dv = e^x dx. Then integral equals:",
        "x e^x - e^x + C",
        ["x e^x + C", "e^x + C", "x^2 e^x / 2 + C"],
    ),
    q(
        "integral ln x dx equals:",
        "x ln x - x + C",
        ["ln x + C", "1/x + C", "x ln x + C"],
    ),
    q(
        "For integral x sin x dx, one application of parts gives:",
        "-x cos x + sin x + C",
        ["x cos x + C", "-x sin x + C", "cos x + C"],
    ),
    q(
        "When integrating polynomial times e^x, LIATE suggests taking u as:",
        "The polynomial factor",
        ["e^x", "Either always e^x", "Neither factor"],
    ),
    q(
        "integral x^2 e^x dx after two applications of parts equals:",
        "e^x (x^2 - 2x + 2) + C",
        ["x^2 e^x + C", "2x e^x + C", "e^x (x^2 + 2) + C"],
    ),
]

BANK_PARTIAL_FRACTIONS: QuestionBank = [
    q(
        "Partial fraction decomposition applies to rational functions where:",
        "Denominator factors into linear/quadratic factors",
        ["Numerator is always 1", "Degree of numerator exceeds denominator", "Function is trigonometric"],
    ),
    q(
        "1 / ((x-1)(x+2)) decomposes as:",
        "A/(x-1) + B/(x+2)",
        ["A/(x-1) - B/(x+2) only without constants", "A x + B", "1/(x-1) only"],
    ),
    q(
        "For distinct linear factors, integral of 1/((x-a)(x-b)) dx after decomposition involves:",
        "Logarithms of linear factors",
        ["Inverse trigonometric functions only", "Exponential functions", "No logarithms"],
    ),
    q(
        "If denominator has repeated factor (x-a)^2, include terms:",
        "A/(x-a) + B/(x-a)^2",
        ["A/(x-a) only", "A x + B", "A/(x-a)^3 only"],
    ),
    q(
        "integral dx / (x^2 - 1) using partial fractions gives:",
        "(1/2) ln|(x-1)/(x+1)| + C",
        ["ln|x^2 - 1| + C", "tan^-1 x + C", "1/(x^2 - 1) + C"],
    ),
    q(
        "For an irreducible quadratic factor x^2 + 1 in the denominator, use numerator of form:",
        "Ax + B",
        ["A only", "A x^2 + B x", "Constant only"],
    ),
]

BANK_FUNDAMENTAL_THEOREM_CALCULUS: QuestionBank = [
    q(
        "If F(x) = integral from a to x of f(t) dt, then F'(x) equals:",
        "f(x)",
        ["F(x)", "integral f(x) dx", "f(a)"],
    ),
    q(
        "Fundamental theorem part 2: integral from a to b of f(x) dx equals:",
        "F(b) - F(a) where F' = f",
        ["F(a) - F(b)", "f(b) - f(a)", "F(b) + F(a)"],
    ),
    q(
        "integral from 0 to 2 of 3x^2 dx equals:",
        "8",
        ["6", "4", "12"],
    ),
    q(
        "If f is continuous on [a, b], then d/dx integral from a to x of f(t) dt at x = c equals:",
        "f(c)",
        ["0", "F(c)", "integral from a to c of f(t) dt"],
    ),
    q(
        "integral from 1 to e of 1/x dx equals:",
        "1",
        ["0", "e", "ln e - 1"],
    ),
    q(
        "The FTC connects differentiation and:",
        "Integration",
        ["Limits only", "Series expansion only", "Matrix inversion"],
    ),
]

BANK_DEFINITE_INTEGRAL_PROPERTIES: QuestionBank = [
    q(
        "integral from a to a of f(x) dx equals:",
        "0",
        ["f(a)", "1", "2 f(a)"],
    ),
    q(
        "integral from a to b of f(x) dx equals negative of integral from b to a of f(x) dx when:",
        "a > b",
        ["Always for all a, b", "Never", "Only if f is odd"],
    ),
    q(
        "If f is odd, integral from -a to a of f(x) dx equals:",
        "0",
        ["2 integral from 0 to a", "Always positive", "Depends on a only"],
    ),
    q(
        "If f is even, integral from -a to a of f(x) dx equals:",
        "2 integral from 0 to a of f(x) dx",
        ["0", "integral from 0 to a only", "Negative of integral from 0 to a"],
    ),
    q(
        "integral from a to b of [f(x) + g(x)] dx equals:",
        "integral f + integral g (same limits)",
        ["integral f - integral g", "Product of integrals", "0"],
    ),
    q(
        "For c > 0, integral from a to b of c f(x) dx equals:",
        "c times integral from a to b of f(x) dx",
        ["integral from ca to cb", "c + integral f", "integral f / c"],
    ),
]

# ---------------------------------------------------------------------------
# Differential Equations
# ---------------------------------------------------------------------------

BANK_FORMATION_DE: QuestionBank = [
    q(
        "To form a differential equation from a family of curves with arbitrary constant C, eliminate:",
        "C by differentiation",
        ["x and y", "The highest power of y only", "All variables"],
    ),
    q(
        "Family y = C e^x gives differential equation:",
        "dy/dx = y",
        ["dy/dx = C", "d^2y/dx^2 = y", "dy/dx = e^x"],
    ),
    q(
        "Family y = C x^2 gives:",
        "x dy/dx - 2y = 0",
        ["dy/dx = x^2", "dy/dx = 2C x only without elimination", "y = x dy/dx"],
    ),
    q(
        "Order of the DE formed from y = A sin x + B cos x (two constants) is:",
        "2",
        ["1", "0", "3"],
    ),
    q(
        "Eliminating C from y = C/x gives:",
        "x dy/dx + y = 0",
        ["dy/dx = -C/x^2 only", "y = x", "dy/dx = 1/x"],
    ),
    q(
        "A differential equation formed from a one-parameter family has order equal to:",
        "Number of differentiations needed to eliminate the constant",
        ["Always 1", "Always 2", "Degree of the curve always"],
    ),
]

BANK_VARIABLES_SEPARABLE: QuestionBank = [
    q(
        "A DE is variables separable if it can be written as:",
        "g(y) dy = f(x) dx",
        ["y = f(x) only", "dy/dx = x + y only", "g(y) = f(x) with no differentials"],
    ),
    q(
        "Solve dy/dx = x/y (y != 0). Separating gives:",
        "y dy = x dx, so y^2/2 = x^2/2 + C",
        ["dy = x dx only", "y = x + C", "ln y = x + C"],
    ),
    q(
        "General solution of dy/dx = ky is:",
        "y = C e^(kx)",
        ["y = kx + C", "y = C x^k", "y = e^x + C"],
    ),
    q(
        "For dy/dx = (1 + y^2)/(1 + x^2), after separation integrate to get:",
        "tan^-1 y = tan^-1 x + C",
        ["y = x + C", "ln y = ln x + C", "y^2 = x^2 + C"],
    ),
    q(
        "Particular solution of dy/dx = 2y with y(0) = 3 is:",
        "y = 3 e^(2x)",
        ["y = 2 e^(3x)", "y = 3 + 2x", "y = e^(2x)"],
    ),
    q(
        "Separation requires multiplying by dx and dividing terms so that:",
        "All y terms with dy are on one side and x terms with dx on the other",
        ["All constants vanish", "dy/dx disappears without integration", "Only linear DE allowed"],
    ),
]

BANK_HOMOGENEOUS_DE: QuestionBank = [
    q(
        "A DE dy/dx = F(x, y) is homogeneous if F(tx, ty) equals:",
        "F(x, y) for all t",
        ["t F(x, y)", "F(x, y) + t", "t^2 only"],
    ),
    q(
        "Standard substitution for homogeneous DE is:",
        "y = v x, so dy/dx = v + x dv/dx",
        ["x = v y only", "y = v + x", "v = x y"],
    ),
    q(
        "dy/dx = (x + y)/(x - y) is homogeneous because numerator and denominator are:",
        "Both degree 1 homogeneous polynomials",
        ["Both constants", "Degree 2 only", "Not homogeneous"],
    ),
    q(
        "After substituting y = vx in homogeneous DE, the equation becomes separable in:",
        "v and x",
        ["y only", "x only", "Neither"],
    ),
    q(
        "For dy/dx = y/x, substituting y = vx gives dv/dx =:",
        "0, so v = C and y = C x",
        ["1/x", "v/x", "C x^2"],
    ),
    q(
        "Homogeneous DE of form dy/dx = (y^2 - x^2)/(xy) is solved using:",
        "y = vx substitution",
        ["Integrating factor directly", "Partial fractions in x only", "Laplace transform"],
    ),
]

BANK_LINEAR_DE: QuestionBank = [
    q(
        "Standard form of first order linear DE is:",
        "dy/dx + P(x) y = Q(x)",
        ["dy/dx = P(x) y^2", "dy/dx = Q(x) only", "d^2y/dx^2 + y = 0"],
    ),
    q(
        "Integrating factor for dy/dx + P(x) y = Q(x) is:",
        "e^(integral P(x) dx)",
        ["e^(P(x))", "integral P(x) dx", "1/P(x)"],
    ),
    q(
        "For dy/dx + y = e^x, integrating factor is:",
        "e^x",
        ["e^(-x)", "x e^x", "1"],
    ),
    q(
        "General solution of dy/dx + 2y = 0 is:",
        "y = C e^(-2x)",
        ["y = C e^(2x)", "y = -2 C x", "y = C + 2x"],
    ),
    q(
        "For dy/dx - y/x = x^2, integrating factor is:",
        "1/x",
        ["x", "e^x", "x^2"],
    ),
    q(
        "After multiplying by integrating factor I(x), the left side becomes:",
        "d/dx [I(x) y]",
        ["I(x) only", "y / I(x)", "integral I(x) dx"],
    ),
]

# ---------------------------------------------------------------------------
# Vectors
# ---------------------------------------------------------------------------

BANK_SECTION_FORMULA_VECTORS: QuestionBank = [
    q(
        "Position vector of point dividing AB internally in ratio m : n (A to B) is:",
        "(n a + m b) / (m + n)",
        ["(m a + n b) / (m + n)", "(a + b) / 2 always", "m a - n b"],
    ),
    q(
        "Midpoint of segment joining a and b has position vector:",
        "(a + b) / 2",
        ["a - b", "2(a + b)", "(a + b) / 4"],
    ),
    q(
        "External division of AB in ratio m : n gives position vector:",
        "(n a - m b) / (n - m)",
        ["(n a + m b) / (n + m)", "(m a - n b) / (m - n)", "a + b"],
    ),
    q(
        "If P divides AB in ratio 2 : 3 internally, OP = (3 OA + 2 OB) / 5 means m : n is:",
        "2 : 3 from A to B",
        ["3 : 2 from A to B", "2 : 3 from B to A only", "5 : 1"],
    ),
    q(
        "Centroid of triangle with vertices a, b, c has position vector:",
        "(a + b + c) / 3",
        ["(a + b) / 2", "a + b + c", "(2a + b + c) / 4"],
    ),
    q(
        "If section ratio is 1 : 1 internally, the point is:",
        "The midpoint",
        ["One-third point", "External division point", "Origin always"],
    ),
]

BANK_SCALAR_TRIPLE_PRODUCT: QuestionBank = [
    q(
        "Scalar triple product [a b c] = a . (b x c) equals volume of parallelepiped:",
        "Up to absolute value, volume = |[a b c]|",
        ["Always negative volume", "Sum of edges", "Dot product only without cross"],
    ),
    q(
        "If [a b c] = 0, vectors a, b, c are:",
        "Coplanar",
        ["Orthogonal always", "Parallel always", "Unit vectors always"],
    ),
    q(
        "Scalar triple product is invariant under:",
        "Cyclic permutation of vectors",
        ["Reversal of all three signs only", "Any permutation with odd parity", "Cross product with self"],
    ),
    q(
        "For a = i, b = j, c = k, [a b c] equals:",
        "1",
        ["0", "-1", "3"],
    ),
    q(
        "Swapping two vectors in [a b c] changes sign:",
        "True (anticommutative in pairs)",
        ["False", "Only if vectors are unit", "Only for coplanar vectors"],
    ),
    q(
        "Geometrically, |a . (b x c)| with a as height direction gives:",
        "Volume of parallelepiped formed by a, b, c",
        ["Area of triangle", "Length of a only", "Angle between b and c"],
    ),
]

# ---------------------------------------------------------------------------
# Three-Dimensional Geometry
# ---------------------------------------------------------------------------

BANK_ANGLE_BETWEEN_LINES: QuestionBank = [
    q(
        "Angle theta between lines with direction ratios (a1, b1, c1) and (a2, b2, c2) satisfies:",
        "cos theta = |a1 a2 + b1 b2 + c1 c2| / (d1 d2)",
        ["sin theta = dot product", "cos theta = cross product magnitude", "tan theta = sum of ratios"],
    ),
    q(
        "Direction ratios of line parallel to vector (1, 1, 1) can be:",
        "(2, 2, 2)",
        ["(1, -1, 0) only", "(0, 0, 0)", "(-1, 2, 3) only if perpendicular"],
    ),
    q(
        "If direction ratios are proportional, the lines are:",
        "Parallel",
        ["Perpendicular always", "Skew always", "Intersecting at right angle always"],
    ),
    q(
        "Angle between x-axis and line with direction ratios (1, sqrt(3), 0) is:",
        "60 degrees",
        ["30 degrees", "45 degrees", "90 degrees"],
    ),
    q(
        "Two lines with DRs (1, 0, 0) and (0, 1, 0) are:",
        "Perpendicular",
        ["Parallel", "Coincident", "Skew with angle 45 degrees"],
    ),
    q(
        "Acute angle between lines uses absolute value in dot product formula so that:",
        "cos theta lies between 0 and 1 for acute angle convention",
        ["theta is always obtuse", "DRs must be unit vectors", "Cross product is zero"],
    ),
]

BANK_SHORTEST_DISTANCE_LINES: QuestionBank = [
    q(
        "Shortest distance between two skew lines is along a direction:",
        "Perpendicular to both lines",
        ["Parallel to first line", "Parallel to second line", "Along x-axis always"],
    ),
    q(
        "If two lines intersect, shortest distance between them is:",
        "0",
        ["Infinite", "Product of direction cosines", "Sum of intercepts"],
    ),
    q(
        "Parallel non-coincident lines have shortest distance:",
        "Perpendicular distance between them (constant)",
        ["Zero always", "Undefined always", "Equal to angle between them"],
    ),
    q(
        "Formula for shortest distance between skew lines uses:",
        "|(b-a) . (d1 x d2)| / |d1 x d2|",
        ["Dot product of direction vectors only", "Sum of coordinates", "Determinant of 4x4 only without vectors"],
    ),
    q(
        "Lines r = a + t d1 and r = b + s d2 are skew if they:",
        "Do not intersect and are not parallel",
        ["Are parallel", "Are identical", "Have same intercept"],
    ),
    q(
        "For parallel lines r = a1 + t d and r = a2 + s d, distance is:",
        "|(a2 - a1) x d| / |d|",
        ["|a2 - a1| always", "Zero", "|d1 . d2|"],
    ),
]

BANK_ANGLE_BETWEEN_PLANES: QuestionBank = [
    q(
        "Angle between planes a1 x + b1 y + c1 z + d1 = 0 and a2 x + b2 y + c2 z + d2 = 0 is found using:",
        "Normal vectors (a1, b1, c1) and (a2, b2, c2)",
        ["x-intercepts only", "Constants d1 and d2 only", "Any point on each plane"],
    ),
    q(
        "If n1 . n2 = 0 for normal vectors, planes are:",
        "Perpendicular",
        ["Parallel", "Coincident", "Always at 45 degrees"],
    ),
    q(
        "Planes with normals proportional are:",
        "Parallel (or coincident)",
        ["Perpendicular", "Skew", "Always intersecting at 60 degrees"],
    ),
    q(
        "Angle between planes equals angle between their:",
        "Normals (or supplementary, take acute convention as needed)",
        ["Direction cosines of any line on plane", "Distances from origin only", "Traces on xy-plane only"],
    ),
    q(
        "For planes x + y + z = 1 and x - y = 0, normals (1,1,1) and (1,-1,0) give cos theta =:",
        "0, so planes are perpendicular",
        ["1", "1/sqrt(3) only without checking", "Always parallel"],
    ),
    q(
        "Dihedral angle between half-spaces uses the same formula as angle between:",
        "Normal vectors to the planes",
        ["Position vectors of points", "Cross product of coordinates", "Slopes dy/dx"],
    ),
]

# ---------------------------------------------------------------------------
# Linear Programming
# ---------------------------------------------------------------------------

BANK_CORNER_POINT_METHOD: QuestionBank = [
    q(
        "In LPP with bounded feasible region, optimal value of Z = ax + by occurs at:",
        "A corner point of the feasible region",
        ["Midpoint of any edge always", "Origin always", "Any interior point"],
    ),
    q(
        "Corner points are found by:",
        "Intersecting boundary lines and testing feasibility",
        ["Differentiating Z", "Integrating constraints", "Random sampling only"],
    ),
    q(
        "For maximize Z = 3x + 2y subject to x + y <= 4, x >= 0, y >= 0, corner (4, 0) gives Z =:",
        "12",
        ["8", "6", "4"],
    ),
    q(
        "If feasible region is unbounded and all corner values of Z are below k, then:",
        "Maximum may not exist (Z can increase without bound in feasible direction)",
        ["Maximum is always at origin", "Maximum is always zero", "Minimum and maximum both exist always"],
    ),
    q(
        "To solve graphically, shade the region satisfying all:",
        "Constraints simultaneously",
        ["Objective function only", "One constraint at a time without intersection", "Corner points only"],
    ),
    q(
        "For minimize Z, compare Z at:",
        "All corner points of feasible region",
        ["Only the origin", "Only the point farthest from origin", "Midpoints of edges only"],
    ),
]

# ---------------------------------------------------------------------------
# Probability
# ---------------------------------------------------------------------------

BANK_MULTIPLICATION_THEOREM: QuestionBank = [
    q(
        "Multiplication theorem: P(A and B) = P(A) P(B|A) when:",
        "P(A) > 0",
        ["A and B are always independent", "P(B) = 0 only", "Never valid"],
    ),
    q(
        "If A and B are independent, P(A and B) equals:",
        "P(A) P(B)",
        ["P(A) + P(B)", "P(A|B) only", "P(A) / P(B)"],
    ),
    q(
        "Drawing two cards without replacement from a deck: second card depends on first, so use:",
        "Conditional probability in multiplication rule",
        ["Independence always", "P(A) + P(B)", "Bayes only"],
    ),
    q(
        "P(A and B and C) = P(A) P(B|A) P(C|A and B) is:",
        "General multiplication rule for three events",
        ["Valid only for independent events", "Same as P(A)+P(B)+P(C)", "Always zero"],
    ),
    q(
        "Bag: 3 red, 2 blue. Draw 2 without replacement. P(both red) =:",
        "(3/5)(2/4) = 3/10",
        ["(3/5)^2 = 9/25", "6/25", "1/2"],
    ),
    q(
        "If P(B|A) = P(B), events A and B are:",
        "Independent",
        ["Mutually exclusive", "Exhaustive", "Impossible"],
    ),
]

BANK_BERNOULLI_BINOMIAL: QuestionBank = [
    q(
        "A Bernoulli trial has:",
        "Exactly two outcomes (success/failure)",
        ["Infinitely many outcomes", "Three equally likely outcomes", "Continuous outcomes"],
    ),
    q(
        "For X ~ B(n, p), E(X) equals:",
        "np",
        ["np(1-p)", "p^n", "n/p"],
    ),
    q(
        "Variance of binomial B(n, p) is:",
        "np(1-p)",
        ["np", "p(1-p)", "n^2 p"],
    ),
    q(
        "P(X = r) for X ~ B(n, p) is:",
        "C(n, r) p^r (1-p)^(n-r)",
        ["p^r only", "n p^r", "C(n, r) p^n"],
    ),
    q(
        "10 fair coin tosses, P(exactly 3 heads) uses:",
        "C(10, 3) (1/2)^10",
        ["(1/2)^3", "10 (1/2)^3", "C(10, 3) / 2"],
    ),
    q(
        "In n independent Bernoulli trials with constant p, total successes follows:",
        "Binomial distribution",
        ["Poisson always", "Normal always with n = 1", "Uniform distribution"],
    ),
]

# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

_TOPIC_REGISTRATIONS: list[tuple[list[str], QuestionBank]] = [
    (["Equivalence relations"], BANK_EQUIVALENCE_RELATIONS),
    (["Binary operations"], BANK_BINARY_OPERATIONS),
    (["Graphs of inverse trigonometric functions"], BANK_ITF_GRAPHS),
    (["Elementary operations and invertible matrices"], BANK_MATRIX_ELEMENTARY_INVERTIBLE),
    (["Minors and cofactors"], BANK_MINORS_COFACTORS),
    (["System of linear equations using determinants"], BANK_LINEAR_SYSTEMS_DETERMINANTS),
    (["Exponential and logarithmic derivatives"], BANK_EXP_LOG_DERIVATIVES),
    (["Second order derivatives"], BANK_SECOND_ORDER_DERIVATIVES),
    (["Mean value theorems"], BANK_MEAN_VALUE_THEOREMS),
    (["Tangents and normals"], BANK_TANGENTS_NORMALS),
    (["Approximation using differentials"], BANK_APPROXIMATION_DIFFERENTIALS),
    (["Integration by parts"], BANK_INTEGRATION_BY_PARTS),
    (["Partial fractions in integration"], BANK_PARTIAL_FRACTIONS),
    (["Fundamental theorem of calculus"], BANK_FUNDAMENTAL_THEOREM_CALCULUS),
    (["Properties of definite integrals"], BANK_DEFINITE_INTEGRAL_PROPERTIES),
    (["Formation of a differential equation"], BANK_FORMATION_DE),
    (["Variables separable"], BANK_VARIABLES_SEPARABLE),
    (["Homogeneous differential equations"], BANK_HOMOGENEOUS_DE),
    (["Linear differential equations"], BANK_LINEAR_DE),
    (["Section formula for vectors"], BANK_SECTION_FORMULA_VECTORS),
    (["Scalar triple product"], BANK_SCALAR_TRIPLE_PRODUCT),
    (["Angle between two lines"], BANK_ANGLE_BETWEEN_LINES),
    (["Shortest distance between two lines"], BANK_SHORTEST_DISTANCE_LINES),
    (["Angle between two planes"], BANK_ANGLE_BETWEEN_PLANES),
    (["Corner point method"], BANK_CORNER_POINT_METHOD),
    (["Multiplication theorem of probability"], BANK_MULTIPLICATION_THEOREM),
    (["Bernoulli trials and binomial distribution"], BANK_BERNOULLI_BINOMIAL),
]

_KEYWORD_ENTRIES: list[tuple[tuple[str, ...], QuestionBank]] = [
    (("equivalence class", "partition", "reflexive symmetric transitive"), BANK_EQUIVALENCE_RELATIONS),
    (("binary operation", "associative", "commutative", "identity element"), BANK_BINARY_OPERATIONS),
    (("graph of sin^-1", "graph of cos^-1", "inverse trig graph"), BANK_ITF_GRAPHS),
    (("elementary matrix", "elementary row operation", "invertible matrix"), BANK_MATRIX_ELEMENTARY_INVERTIBLE),
    (("minor", "cofactor", "adjoint"), BANK_MINORS_COFACTORS),
    (("cramer's rule", "cramer", "linear system determinant"), BANK_LINEAR_SYSTEMS_DETERMINANTS),
    (("a^x", "log_a x", "ln x derivative", "exponential derivative"), BANK_EXP_LOG_DERIVATIVES),
    (("second derivative", "f''", "concavity"), BANK_SECOND_ORDER_DERIVATIVES),
    (("rolle", "lagrange", "mean value theorem"), BANK_MEAN_VALUE_THEOREMS),
    (("tangent", "normal", "slope of tangent"), BANK_TANGENTS_NORMALS),
    (("linear approximation", "differential", "delta y"), BANK_APPROXIMATION_DIFFERENTIALS),
    (("integration by parts", "u dv"), BANK_INTEGRATION_BY_PARTS),
    (("partial fraction", "decompose rational"), BANK_PARTIAL_FRACTIONS),
    (("fundamental theorem", "F(b) - F(a)"), BANK_FUNDAMENTAL_THEOREM_CALCULUS),
    (("definite integral property", "even function integral", "odd function integral"), BANK_DEFINITE_INTEGRAL_PROPERTIES),
    (("form differential equation", "eliminate arbitrary constant"), BANK_FORMATION_DE),
    (("separable", "variables separable"), BANK_VARIABLES_SEPARABLE),
    (("homogeneous differential", "y = vx"), BANK_HOMOGENEOUS_DE),
    (("integrating factor", "linear differential"), BANK_LINEAR_DE),
    (("section formula", "internal division", "midpoint vector"), BANK_SECTION_FORMULA_VECTORS),
    (("scalar triple product", "box product", "coplanar vectors"), BANK_SCALAR_TRIPLE_PRODUCT),
    (("angle between lines", "direction ratios"), BANK_ANGLE_BETWEEN_LINES),
    (("shortest distance", "skew lines"), BANK_SHORTEST_DISTANCE_LINES),
    (("angle between planes", "normal vector plane"), BANK_ANGLE_BETWEEN_PLANES),
    (("corner point", "linear programming optimal"), BANK_CORNER_POINT_METHOD),
    (("multiplication theorem", "P(A and B)"), BANK_MULTIPLICATION_THEOREM),
    (("bernoulli", "binomial distribution", "C(n,r) p^r"), BANK_BERNOULLI_BINOMIAL),
]


def register() -> None:
    """Register all Class 12 Mathematics extra banks into quiz_concepts."""
    from app.data.quiz_concepts import GLOBAL_CHAPTER_TOPIC_BANKS

    for titles, bank in _TOPIC_REGISTRATIONS:
        register_keys(titles, bank)
    GLOBAL_CHAPTER_TOPIC_BANKS[("Determinants", "Area of a triangle")] = BANK_AREA_TRIANGLE
    register_subject_keywords("MATH", _KEYWORD_ENTRIES)
