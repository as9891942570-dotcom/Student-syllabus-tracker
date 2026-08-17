"""CBSE Class 11 Physics concept banks. Never fallback; exact topic titles first."""

from __future__ import annotations

from app.data.quiz_banks.common import q, register_keys, register_subject_keywords
from app.data.quiz_concepts import QuestionBank

BANK_SI: QuestionBank = [
    q("In the SI system, the base unit of length is the:", "Metre", ["Centimetre", "Foot", "Ångström"]),
    q("The SI system is based on how many base units?", "Seven", ["Three", "Four", "Ten"]),
    q("The SI base unit of mass is the:", "Kilogram", ["Gram", "Pound", "Atomic mass unit"]),
    q("The SI base unit of time is the:", "Second", ["Hour", "Minute", "Day"]),
    q("The SI base unit of electric current is the:", "Ampere", ["Coulomb", "Volt", "Ohm"]),
    q("The SI base unit of thermodynamic temperature is the:", "Kelvin", ["Celsius", "Fahrenheit", "Rankine"]),
    q("The SI base unit of amount of substance is the:", "Mole", ["Gram", "Litre", "Molecule"]),
    q("The SI base unit of luminous intensity is the:", "Candela", ["Lumen", "Lux", "Watt"]),
    q("A derived SI unit among the following is:", "Newton", ["Metre", "Kilogram", "Second"]),
    q("1 nm is equal to:", "10^-9 m", ["10^-6 m", "10^-2 m", "10^9 m"]),
]

BANK_LENGTH: QuestionBank = [
    q("Large astronomical distances are often measured by the:", "Parallax method", ["Vernier caliper only", "Screw gauge only", "Simple pendulum"]),
    q("One astronomical unit (AU) is approximately the:", "Mean distance from the Earth to the Sun", ["Distance light travels in one year", "Radius of the Earth", "Distance to the nearest star"]),
    q("One light year is the:", "Distance travelled by light in vacuum in one year", ["Time taken by light to reach the Sun", "Speed of light in one year", "Distance equal to 1 parsec exactly"]),
    q("1 parsec is defined using an annual parallax of:", "1 arcsecond", ["1 degree", "1 radian", "1 minute of arc only"]),
    q("1 parsec is approximately:", "3.26 light years", ["1 light year", "1 AU", "10^3 m"]),
    q("Very small lengths (such as the size of a nucleus) are of order:", "1 fermi = 10^-15 m", ["1 millimetre", "1 kilometre", "1 light year"]),
    q("1 Ångström is equal to:", "10^-10 m", ["10^-15 m", "10^-2 m", "10^-6 m"]),
    q("The least count of a typical vernier calipers is about:", "0.01 cm (0.1 mm)", ["1 m", "1 km", "10^-15 m"]),
    q("A screw gauge is preferred over a metre scale when measuring the:", "Diameter of a thin wire", ["Distance between two cities", "Height of a building", "Focal length of a telescope in kilometres"]),
    q("If a star has parallax angle p (in arcseconds), its distance in parsec is:", "1/p", ["p", "p²", "206265 / p²"]),
    q("The range of lengths in the visible universe spans roughly:", "10^-15 m (nuclear) to 10^26 m (cosmological)", ["Only metres to kilometres", "Only millimetres", "Only light years"]),
    q("Apparent size of a distant planet can be used to find its diameter if we know:", "Its distance and the angular diameter", ["Only its mass", "Only its colour", "Only its orbital period"]),
]

BANK_MASS: QuestionBank = [
    q("The SI unit of mass is realised by a:", "Kilogram (now defined via the Planck constant)", ["Litre of water only as the unique definition today", "Second of time", "Metre stick"]),
    q("The unified atomic mass unit (u) is:", "1/12 the mass of a carbon-12 atom", ["Mass of one electron", "Mass of one proton exactly as 1 g", "Mass of 1 m³ of water"]),
    q("1 u is approximately:", "1.66 × 10^-27 kg", ["1 kg", "1 g", "9.1 × 10^-31 kg"]),
    q("Masses of atoms and molecules are conveniently expressed in:", "Unified atomic mass unit (u)", ["Light years", "Parsecs", "Newtons"]),
    q("A beam balance compares:", "Masses (independent of local g to first order)", ["Weights that always vary with colour", "Lengths", "Time intervals"]),
    q("A spring balance measures:", "Weight (which depends on local g)", ["Invariant rest mass only with no g dependence", "Time period", "Electric charge"]),
    q("The mass of an electron is of order:", "10^-30 kg", ["1 kg", "10^3 kg", "10^-15 kg"]),
    q("Which instrument is suitable for measuring the mass of a small chemical sample in a lab?", "Physical balance / digital analytical balance", ["Metre scale", "Stopwatch", "Parallax telescope"]),
]

BANK_TIME: QuestionBank = [
    q("The SI second is defined using:", "A caesium atomic clock (hyperfine transition of Cs-133)", ["The solar day only", "A simple pendulum of 1 m", "The year of 365 days exactly"]),
    q("A caesium atomic clock is used as a standard of:", "Time", ["Length", "Mass", "Luminous intensity"]),
    q("The least count of a typical stopwatch used in school experiments is about:", "0.1 s or 0.01 s", ["1 day", "1 year", "10^-15 s"]),
    q("Oscillation period of a simple pendulum can be used to measure:", "Time intervals (via T = 2π√(l/g))", ["Electric charge", "Parallax of a star", "Nuclear radius"]),
    q("One mean solar day is:", "86400 s", ["3600 s", "60 s", "3.15 × 10^7 s exactly as a day"]),
    q("A light-year is a unit of:", "Distance, not time", ["Time only", "Mass", "Frequency"]),
    q("High-precision time transfer on Earth uses:", "Atomic clocks and satellite systems", ["Metre scales", "Vernier calipers", "Spring balances"]),
    q("Frequency of a periodic event is the:", "Number of repetitions per unit time", ["Time for one event only always called frequency", "Mass per second", "Length of a pendulum in metres as frequency"]),
]

BANK_ERRORS: QuestionBank = [
    q("Accuracy of a measurement refers to:", "Closeness to the true value", ["Only the number of digits written", "The colour of the instrument", "The brand of the apparatus"]),
    q("Precision refers to:", "Reproducibility / resolution of repeated measurements", ["Always matching the true value", "The SI unit chosen", "The observer's height"]),
    q("A systematic error:", "Has a definite sign and can often be reduced by correction", ["Is purely random with zero mean always", "Cannot occur in length measurements", "Is due only to parallax of stars"]),
    q("Random errors are reduced by:", "Taking more observations and averaging", ["Changing the SI unit", "Using a longer sentence in the record", "Painting the instrument"]),
    q("Least count error is:", "The error associated with the resolution of the instrument", ["Always 1 metre", "Independent of the instrument", "The same as a wrong formula"]),
    q("Absolute error in a measurement x is:", "|x_measured − x_true| (or deviation from the mean)", ["x / x_true always", "Only the percentage error", "The square of the reading"]),
    q("Percentage error is:", "(Absolute error / true or mean value) × 100%", ["Absolute error × 100 only", "Least count in millimetres", "The number of significant figures"]),
    q("If a quantity is the product xy, relative errors:", "Add: Δz/z = Δx/x + Δy/y", ["Multiply as (Δx)(Δy)", "Cancel always", "Subtract only"]),
]

BANK_SIGFIG: QuestionBank = [
    q("The number of significant figures in 0.00580 is:", "3", ["1", "5", "6"]),
    q("The number of significant figures in 2.50 × 10^4 is:", "3", ["1", "2", "5"]),
    q("When adding 2.3 m and 0.015 m, the result should be quoted as:", "2.3 m", ["2.315 m", "2.31 m always with three decimals", "0.015 m"]),
    q("In multiplication, the result should have:", "Significant figures equal to the least precise factor", ["As many digits as possible", "Always one digit", "Infinite figures"]),
    q("Zeros between non-zero digits are:", "Significant", ["Never significant", "Significant only in integers", "Always dropped"]),
    q("Leading zeros in 0.0024 are:", "Not significant", ["Always significant", "Count as two significant figures", "Make the number exact"]),
    q("Trailing zeros in 2.300 (measured) are:", "Significant", ["Never counted", "Only placeholders without meaning", "Illegal in SI"]),
    q("Rounding 2.746 to three significant figures gives:", "2.75", ["2.74 always", "2.7", "3.00"]),
]

BANK_DIM: QuestionBank = [
    q("Dimensions of length, mass and time are denoted as:", "[L], [M], [T]", ["[N], [J], [W]", "[A], [K], [cd]", "[rad], [sr], [mol]"]),
    q("Force has the dimensional formula:", "[M L T^-2]", ["[M L T^-1]", "[M T^-2]", "[L T^-2]"]),
    q("Energy has the same dimensions as:", "Work", ["Force", "Power", "Momentum"]),
    q("Power has dimensional formula:", "[M L^2 T^-3]", ["[M L T^-2]", "[M L^2 T^-2]", "[M T^-1]"]),
    q("A dimensionless quantity among the following is:", "Strain", ["Stress", "Force", "Velocity"]),
    q("Angle (radian) is:", "Dimensionless", ["[L]", "[T]", "[M]"]),
    q("Dimensional analysis cannot determine:", "A dimensionless numerical constant in a formula", ["The dimensions of a derived quantity", "Consistency of an equation", "Conversion between units of the same dimensions"]),
    q("If v = a t, dimensions of a are those of:", "Acceleration (if v is velocity)", ["Mass", "Time", "Force"]),
]

BANK_DIMEQ: QuestionBank = [
    q("A dimensionally consistent equation:", "Has the same dimensions on both sides", ["May equate length to mass", "Never involves time", "Is always numerically correct"]),
    q("The equation v = u + a t is dimensionally:", "Consistent", ["Inconsistent because u and a differ", "Meaningless", "Only valid in CGS"]),
    q("If E = k m v^n, and E is energy, dimensional analysis gives n =:", "2", ["1", "0", "3"]),
    q("The dimensional formula of gravitational constant G is:", "[M^-1 L^3 T^-2]", ["[M L T^-2]", "[M L^2 T^-2]", "[L T^-1]"]),
    q("Planck's constant h has dimensions of:", "Angular momentum (M L^2 T^-1)", ["Energy only [M L^2 T^-2] without time difference", "Force", "Frequency"]),
    q("Two quantities with different dimensions:", "Cannot be added or equated", ["Can always be added", "Must have the same SI prefix", "Are always dimensionless"]),
    q("Checking dimensions of both sides of an equation is a test of:", "Dimensional consistency, not a proof of the physical law", ["Numerical accuracy to all digits", "The observer's skill only", "The colour of symbols"]),
    q("The dimensional formula of pressure is:", "[M L^-1 T^-2]", ["[M L T^-2]", "[M L^2 T^-2]", "[L T^-1]"]),
]


def register() -> None:
    from app.data.quiz_concepts import GLOBAL_CHAPTER_TOPIC_BANKS

    chapter_map = {
        ("Units and Measurements", "The international system of units"): BANK_SI,
        ("Units and Measurements", "Measurement of length"): BANK_LENGTH,
        ("Units and Measurements", "Measurement of mass"): BANK_MASS,
        ("Units and Measurements", "Measurement of time"): BANK_TIME,
        ("Units and Measurements", "Accuracy precision and errors"): BANK_ERRORS,
        ("Units and Measurements", "Significant figures"): BANK_SIGFIG,
        ("Units and Measurements", "Dimensions of physical quantities"): BANK_DIM,
        ("Units and Measurements", "Dimensional formulae and equations"): BANK_DIMEQ,
    }
    GLOBAL_CHAPTER_TOPIC_BANKS.update(chapter_map)

    register_keys(["The international system of units"], BANK_SI)
    register_keys(["Measurement of length"], BANK_LENGTH)
    register_keys(["Measurement of mass"], BANK_MASS)
    register_keys(["Measurement of time"], BANK_TIME)
    register_keys(["Accuracy precision and errors"], BANK_ERRORS)
    register_keys(["Significant figures"], BANK_SIGFIG)
    register_keys(["Dimensions of physical quantities"], BANK_DIM)
    register_keys(["Dimensional formulae and equations"], BANK_DIMEQ)

    register_subject_keywords(
        "PHY",
        [
            (("measurement of length", "parallax method", "astronomical unit"), BANK_LENGTH),
            (("measurement of mass", "unified atomic mass"), BANK_MASS),
            (("measurement of time", "caesium", "cesium atomic"), BANK_TIME),
            (("international system of units", "si base unit"), BANK_SI),
            (("significant figures",), BANK_SIGFIG),
            (("dimensional formulae", "dimensional formula"), BANK_DIMEQ),
            (("dimensions of physical",), BANK_DIM),
            (("accuracy precision", "least count error"), BANK_ERRORS),
        ],
    )
