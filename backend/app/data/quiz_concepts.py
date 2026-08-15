"""Curated concept/numerical MCQ banks keyed by syllabus concept.

Each bank tests actual knowledge — never meta/study-advice prompts.
Keys are normalized lowercase topic titles (and aliases).
"""

from __future__ import annotations

from typing import Callable

# prompt, [(option_text, is_correct), ...]
Question = tuple[str, list[tuple[str, bool]]]
QuestionBank = list[Question]


def _q(prompt: str, correct: str, wrong: list[str]) -> Question:
    opts = [(correct, True)] + [(w, False) for w in wrong]
    return prompt, opts


# ---------------------------------------------------------------------------
# Physics
# ---------------------------------------------------------------------------

BANK_ELECTRIC_CHARGE: QuestionBank = [
    _q(
        "Electric charge is a fundamental property of matter that can be:",
        "Positive or negative",
        ["Only positive", "Only negative", "Only magnetic"],
    ),
    _q(
        "Like charges:",
        "Repel each other",
        ["Attract each other", "Neither attract nor repel", "Always cancel completely"],
    ),
    _q(
        "Unlike charges:",
        "Attract each other",
        ["Repel each other", "Have no interaction", "Always annihilate instantly"],
    ),
    _q(
        "According to quantization of charge, the charge on an isolated body is:",
        "An integer multiple of the elementary charge e",
        ["Any continuous real number", "Always exactly zero", "Always equal to 1 coulomb"],
    ),
    _q(
        "The SI unit of electric charge is the:",
        "Coulomb (C)",
        ["Ampere (A)", "Volt (V)", "Ohm (Ω)"],
    ),
    _q(
        "Conservation of charge means that in an isolated system the total charge:",
        "Remains constant",
        ["Always increases", "Always decreases", "Becomes zero after any process"],
    ),
    _q(
        "The elementary charge e is approximately:",
        "1.6 × 10-19 C",
        ["1.6 × 1019 C", "9.1 × 10-31 C", "3 × 108 C"],
    ),
    _q(
        "A body is charged by induction when:",
        "Charge redistributes due to a nearby charged object without direct contact for the induced separation",
        ["It is heated strongly", "It is painted a different colour", "It is placed in a vacuum with no fields"],
    ),
    _q(
        "Conductors are materials in which:",
        "Charges can move freely",
        ["Charges cannot move at all", "Only heat can flow", "Only sound can propagate"],
    ),
    _q(
        "Insulators are materials in which:",
        "Charges cannot move freely",
        ["Charges move with infinite speed", "Only magnetic monopoles exist", "Resistance is exactly zero"],
    ),
    _q(
        "If an object loses electrons, it becomes:",
        "Positively charged",
        ["Negatively charged", "Magnetically neutral only", "Electrically undefined"],
    ),
    _q(
        "If an object gains electrons, it becomes:",
        "Negatively charged",
        ["Positively charged", "Always uncharged", "A perfect insulator"],
    ),
]

BANK_COULOMB: QuestionBank = [
    _q(
        "Coulomb's law gives the electrostatic force between:",
        "Two point charges",
        ["Two magnetic poles only", "Two current-carrying wires only", "Two sound sources"],
    ),
    _q(
        "According to Coulomb's law, the force between two point charges is proportional to:",
        "The product of the charges and inversely proportional to the square of their separation",
        [
            "The sum of the charges only",
            "The cube of their separation only",
            "Neither charge nor distance",
        ],
    ),
    _q(
        "If the distance between two point charges is doubled, the electrostatic force becomes:",
        "One-fourth",
        ["Half", "Double", "Four times"],
    ),
    _q(
        "If both charges are doubled while separation is unchanged, the force becomes:",
        "Four times",
        ["Half", "Unchanged", "Eight times"],
    ),
    _q(
        "Two point charges of 2 uC and 3 uC are placed 0.5 m apart in vacuum. The magnitude of the force is proportional to:",
        "(2×3)/(0.5)2",
        ["(2+3)/(0.5)", "(2×3)×(0.5)2", "(2/3)/(0.5)2"],
    ),
    _q(
        "The electrostatic force between two charges in vacuum uses Coulomb's constant k ≈:",
        "9 × 10^9 N m2 C-2",
        ["3 × 10^8 m s-1", "6.67 × 10^-11 N m2 kg-2", "1.6 × 10^-19 C"],
    ),
    _q(
        "Coulomb's force is a:",
        "Central force along the line joining the charges",
        ["Tangential force only", "Non-central force always", "Force that needs a medium always"],
    ),
    _q(
        "In vacuum, Coulomb's law may be written as F =:",
        "(1/(4πε0)) · (q1q2/r2)",
        ["q1q2 r2", "ε0 q1q2 / r", "q1 + q2 / r2"],
    ),
    _q(
        "If the medium between charges has dielectric constant K > 1, the force compared to vacuum:",
        "Decreases by a factor of K",
        ["Increases by a factor of K", "Remains exactly the same", "Becomes zero always"],
    ),
    _q(
        "The superposition principle for electrostatic forces states that:",
        "The net force on a charge is the vector sum of individual forces due to other charges",
        [
            "Only the largest force acts",
            "Forces cancel always",
            "Forces multiply algebraically as scalars only",
        ],
    ),
    _q(
        "Two equal charges of 1 uC each are 1 m apart in vacuum. Using F = k q1q2/r2, F is about:",
        "9 × 10-3 N",
        ["9 × 103 N", "9 N", "9 × 10-9 N"],
    ),
    _q(
        "If one charge is doubled and separation is halved, the force becomes:",
        "Eight times",
        ["Twice", "Half", "Unchanged"],
    ),
    _q(
        "The direction of the force on a positive charge due to another positive charge is:",
        "Away from the other charge",
        ["Towards the other charge", "Perpendicular to the joining line always", "Undefined"],
    ),
    _q(
        "Coulomb's law is valid for:",
        "Point charges (or spherically symmetric charge distributions treated as points)",
        ["Any extended charge of arbitrary shape without approximation", "Only AC currents", "Only magnets"],
    ),
]

BANK_ELECTRIC_FIELD: QuestionBank = [
    _q(
        "Electric field at a point is defined as the force experienced by:",
        "A unit positive test charge placed at that point",
        ["A unit negative mass", "A unit magnetic pole", "A unit of heat"],
    ),
    _q(
        "The SI unit of electric field is:",
        "N/C (or V/m)",
        ["Tesla", "Ohm", "Joule"],
    ),
    _q(
        "Electric field due to a point charge q at distance r is:",
        "E = (1/(4πε0)) · (q/r2)",
        ["E = q r2", "E = q / r", "E = 4πε0 q r"],
    ),
    _q(
        "The direction of electric field due to a positive charge is:",
        "Away from the charge",
        ["Towards the charge", "Tangential in circles only", "Undefined"],
    ),
    _q(
        "The direction of electric field due to a negative charge is:",
        "Towards the charge",
        ["Away from the charge", "Random", "Always vertical"],
    ),
    _q(
        "Electric field lines originate from:",
        "Positive charges (or infinity) and terminate on negative charges (or infinity)",
        ["Negative charges only and end on positive charges only in reverse always incorrectly stated", "Magnets only", "Current only"],
    ),
    _q(
        "Electric field lines never:",
        "Intersect each other",
        ["Start from charges", "Indicate direction of field", "Show relative strength by density"],
    ),
    _q(
        "If the force on a charge of 2 C in a field is 10 N, the electric field magnitude is:",
        "5 N/C",
        ["20 N/C", "2 N/C", "12 N/C"],
    ),
    _q(
        "Electric field is a:",
        "Vector quantity",
        ["Scalar quantity", "Neither scalar nor vector", "Tensor of rank 3 always"],
    ),
    _q(
        "In a uniform electric field, a charged particle experiences:",
        "A constant force",
        ["Zero force always", "A force proportional to velocity only", "No acceleration possible"],
    ),
]

BANK_ELECTRIC_FLUX_GAUSS: QuestionBank = [
    _q(
        "Electric flux through a surface depends on:",
        "The electric field and the area projected normal to the field",
        ["Only the colour of the surface", "Only the mass of the surface", "Neither field nor area"],
    ),
    _q(
        "Gauss's law relates the electric flux through a closed surface to:",
        "The net charge enclosed by the surface",
        ["Only the mass enclosed", "Only the temperature outside", "Only the colour of the surface"],
    ),
    _q(
        "For a closed surface enclosing charge Q in vacuum, ∮ E·dA equals:",
        "Q/ε0",
        ["Q ε0", "ε0 / Q", "Zero always"],
    ),
    _q(
        "If no charge is enclosed by a Gaussian surface, the net flux is:",
        "Zero",
        ["Infinite", "Equal to ε0", "Equal to 1/ε0"],
    ),
    _q(
        "Gauss's law is especially useful for finding fields of:",
        "Highly symmetric charge distributions",
        ["Completely arbitrary charge shapes with no symmetry", "Only moving magnets", "Only sound waves"],
    ),
    _q(
        "The SI unit of electric flux is:",
        "N m2 C-1 (or V m)",
        ["Tesla", "Henry", "Ohm"],
    ),
]

BANK_OHM: QuestionBank = [
    _q(
        "Ohm's law states that for many conductors at constant temperature:",
        "V = IR",
        ["V = I/R", "V = I2R", "V = R/I"],
    ),
    _q(
        "The SI unit of resistance is the:",
        "Ohm (Ω)",
        ["Volt", "Ampere", "Coulomb"],
    ),
    _q(
        "If V = 12 V and I = 3 A, the resistance is:",
        "4 Ω",
        ["36 Ω", "0.25 Ω", "15 Ω"],
    ),
    _q(
        "Resistivity ρ relates to resistance by:",
        "R = ρ ℓ / A",
        ["R = ρ A / ℓ", "R = ρ ℓ A", "R = A / (ρ ℓ)"],
    ),
    _q(
        "For ohmic conductors, the V–I graph is:",
        "A straight line through the origin",
        ["A parabola", "A circle", "A horizontal line at V = 0 only"],
    ),
    _q(
        "If resistance doubles and voltage is unchanged, current becomes:",
        "Half",
        ["Double", "Unchanged", "Four times"],
    ),
    _q(
        "Electrical power in a resistor may be written as:",
        "P = I2R = V2/R = VI",
        ["P = I/R only", "P = V/I only", "P = R/V only"],
    ),
    _q(
        "Drift speed of electrons in a conductor is typically:",
        "Very small compared to the speed of light",
        ["Equal to the speed of light", "Faster than light", "Exactly zero always"],
    ),
]

BANK_NEWTON: QuestionBank = [
    _q(
        "Newton's first law is also called the law of:",
        "Inertia",
        ["Gravitation", "Universal gas", "Reflection"],
    ),
    _q(
        "Newton's second law can be written as:",
        "F = ma (for constant mass)",
        ["F = m/a", "F = a/m", "F = m + a"],
    ),
    _q(
        "Newton's third law states that:",
        "For every action there is an equal and opposite reaction",
        ["Force is mass times velocity", "Energy is always created", "Momentum is never conserved"],
    ),
    _q(
        "A force of 10 N acts on a 2 kg mass. Acceleration is:",
        "5 m/s2",
        ["20 m/s2", "0.2 m/s2", "12 m/s2"],
    ),
    _q(
        "Inertia of a body depends primarily on its:",
        "Mass",
        ["Colour", "Temperature only", "Volume only regardless of mass"],
    ),
    _q(
        "Action and reaction forces act:",
        "On different bodies",
        ["On the same body always cancelling motion", "Only in vacuum", "Only on charged objects"],
    ),
]

BANK_KINEMATICS: QuestionBank = [
    _q(
        "For uniformly accelerated motion, v = u + :",
        "at",
        ["a/t", "a t2", "t/a"],
    ),
    _q(
        "The equation s = ut + (1/2)at2 is valid for:",
        "Constant acceleration",
        ["Variable acceleration only", "Circular motion only", "Zero time only"],
    ),
    _q(
        "Average velocity equals total displacement divided by:",
        "Total time",
        ["Total path length only", "Acceleration", "Mass"],
    ),
    _q(
        "If a body starts from rest and accelerates at 2 m/s2 for 5 s, its speed is:",
        "10 m/s",
        ["2.5 m/s", "7 m/s", "25 m/s"],
    ),
    _q(
        "Displacement is a:",
        "Vector quantity",
        ["Scalar quantity", "Dimensionless number only", "Force"],
    ),
    _q(
        "Speed is a:",
        "Scalar quantity",
        ["Vector quantity", "Tensor", "Force"],
    ),
]

BANK_ENERGY: QuestionBank = [
    _q(
        "Kinetic energy of a mass m moving with speed v is:",
        "(1/2) m v2",
        ["m v", "m v2", "(1/2) m v"],
    ),
    _q(
        "Work done by a constant force F through displacement s in the direction of F is:",
        "F s",
        ["F / s", "F + s", "F s2"],
    ),
    _q(
        "The SI unit of work and energy is the:",
        "Joule",
        ["Watt", "Newton", "Pascal"],
    ),
    _q(
        "Power is:",
        "Rate of doing work",
        ["Force times mass", "Energy times time", "Momentum times velocity always incorrectly"],
    ),
    _q(
        "A 2 kg object moving at 3 m/s has kinetic energy:",
        "9 J",
        ["6 J", "18 J", "3 J"],
    ),
    _q(
        "Mechanical energy is conserved when:",
        "Only conservative forces do work (ideal cases)",
        ["Friction always does maximum work", "Energy is created freely", "Mass changes randomly"],
    ),
]

BANK_PHOTOELECTRIC: QuestionBank = [
    _q(
        "In the photoelectric effect, electrons are emitted when:",
        "Light of sufficiently high frequency falls on a metal surface",
        ["The metal is cooled only", "Only static magnets touch the metal", "Only sound waves hit the metal"],
    ),
    _q(
        "Einstein's photoelectric equation relates photon energy hν to:",
        "Work function plus maximum kinetic energy of photoelectrons",
        ["Only mass of the nucleus", "Only resistance of the metal", "Only temperature in all cases"],
    ),
    _q(
        "The threshold frequency is the:",
        "Minimum frequency needed to emit photoelectrons",
        ["Maximum frequency that never emits electrons", "Frequency of sound only", "Frequency of Earth's rotation"],
    ),
    _q(
        "Increasing intensity of light (above threshold) mainly increases:",
        "The number of photoelectrons emitted per second",
        ["The threshold frequency", "The work function of the metal", "The rest mass of electrons"],
    ),
]

# ---------------------------------------------------------------------------
# Chemistry
# ---------------------------------------------------------------------------

BANK_MOLE: QuestionBank = [
    _q(
        "One mole of any substance contains:",
        "6.022 × 1023 elementary entities",
        ["1000 entities", "12 entities", "Zero entities"],
    ),
    _q(
        "The molar mass of H2O is approximately:",
        "18 g mol-1",
        ["2 g mol-1", "16 g mol-1", "32 g mol-1"],
    ),
    _q(
        "Number of moles = given mass / :",
        "Molar mass",
        ["Atomic number", "Density only", "Volume of universe"],
    ),
    _q(
        "2 moles of CO2 contain how many moles of oxygen atoms?",
        "4",
        ["2", "1", "8"],
    ),
    _q(
        "Avogadro's number is denoted by:",
        "Nₐ (≈ 6.022 × 1023 mol-1)",
        ["c", "h", "G"],
    ),
    _q(
        "0.5 mol of O2 molecules contains how many O2 molecules?",
        "3.011 × 1023",
        ["6.022 × 1023", "1.5 × 1023", "0.5"],
    ),
]

BANK_ATOMIC_STRUCTURE: QuestionBank = [
    _q(
        "The electron was discovered by:",
        "J.J. Thomson",
        ["Rutherford", "Bohr", "Chadwick"],
    ),
    _q(
        "Rutherford's model is based mainly on:",
        "α-particle scattering",
        ["Photoelectric effect only", "Brownian motion only", "Ohm's law"],
    ),
    _q(
        "The nucleus of an atom contains:",
        "Protons and neutrons",
        ["Only electrons", "Only photons", "Only neutrinos"],
    ),
    _q(
        "Atomic number Z equals the number of:",
        "Protons in the nucleus",
        ["Neutrons only", "Electrons in all ions always incorrectly", "Nucleons minus protons only as definition of Z"],
    ),
    _q(
        "Isotopes of an element have the same:",
        "Atomic number but different mass numbers",
        ["Mass number but different atomic numbers", "Number of neutrons only always", "Chemical symbol never"],
    ),
    _q(
        "In Bohr's model, angular momentum of an electron is:",
        "n h / (2π)",
        ["n h", "h / n", "2π n / h"],
    ),
]

BANK_PERIODIC: QuestionBank = [
    _q(
        "In the modern periodic table, elements are arranged mainly by:",
        "Increasing atomic number",
        ["Increasing atomic mass only always", "Alphabetical order", "Date of discovery"],
    ),
    _q(
        "Across a period, atomic radius generally:",
        "Decreases",
        ["Increases", "Remains exactly constant", "Becomes infinite"],
    ),
    _q(
        "Down a group, atomic radius generally:",
        "Increases",
        ["Decreases", "Becomes zero", "Oscillates randomly with no trend"],
    ),
    _q(
        "Noble gases are placed in group:",
        "18",
        ["1", "2", "17"],
    ),
    _q(
        "Electronegativity across a period generally:",
        "Increases",
        ["Decreases", "Is undefined", "Is always zero"],
    ),
]

BANK_CHEMICAL_BONDING: QuestionBank = [
    _q(
        "An ionic bond typically forms between:",
        "A metal and a non-metal by electron transfer",
        ["Two identical noble gases only", "Two neutrons", "Two photons"],
    ),
    _q(
        "A covalent bond involves:",
        "Sharing of electron pairs",
        ["Complete transfer only always", "Sharing of protons", "Sharing of neutrons"],
    ),
    _q(
        "VSEPR theory is used to predict:",
        "Shapes of molecules",
        ["Nuclear binding energy", "Radioactive half-life", "Orbital speed of planets"],
    ),
    _q(
        "In water (H2O), the molecular shape is best described as:",
        "Bent (angular)",
        ["Linear", "Square planar", "Octahedral"],
    ),
    _q(
        "Hybridisation of carbon in methane (CH₄) is:",
        "sp3",
        ["sp", "sp2", "sp3d2"],
    ),
]

BANK_EQUILIBRIUM: QuestionBank = [
    _q(
        "At chemical equilibrium:",
        "Forward and reverse rates are equal",
        ["All reactions have stopped", "Only products remain", "Temperature must be absolute zero"],
    ),
    _q(
        "Le Chatelier's principle predicts the shift when:",
        "A system at equilibrium is disturbed",
        ["No reaction can ever occur", "Only solids melt", "Light speed changes"],
    ),
    _q(
        "For aA + bB ⇌ cC + dD, Kc involves:",
        "Concentrations of products over reactants raised to stoichiometric powers",
        ["Only temperatures", "Only catalyst mass", "Only colour of solutions"],
    ),
    _q(
        "A catalyst:",
        "Speeds up attainment of equilibrium without changing K",
        ["Changes the equilibrium constant permanently in all cases", "Stops reverse reaction forever", "Creates energy from nothing"],
    ),
]

BANK_ORGANIC_BASICS: QuestionBank = [
    _q(
        "The general formula of alkanes is:",
        "CₙH2ₙ₊2",
        ["CₙH2ₙ", "CₙH2ₙ₋2", "CₙHₙ"],
    ),
    _q(
        "Isomers have the same:",
        "Molecular formula but different structures",
        ["Structure but different molecular formulae", "Colour only", "Density only"],
    ),
    _q(
        "The functional group in alcohols is:",
        "–OH",
        ["–COOH only always", "–CHO only always", "–NH2 only always"],
    ),
    _q(
        "Tetravalency of carbon means carbon forms:",
        "Four covalent bonds",
        ["Two bonds only", "Six bonds always", "No bonds"],
    ),
]

# ---------------------------------------------------------------------------
# Mathematics
# ---------------------------------------------------------------------------

BANK_QUADRATIC: QuestionBank = [
    _q(
        "For ax2 + bx + c = 0, the discriminant D is:",
        "b2 − 4ac",
        ["b2 + 4ac", "4ac − b2 always incorrectly signed as definition", "a2 − 4bc"],
    ),
    _q(
        "If D > 0 and perfect square (a,b,c rational), roots are:",
        "Real and distinct (rational if a,b,c rational appropriately)",
        ["Always imaginary", "Always equal", "Always zero"],
    ),
    _q(
        "Sum of roots of ax2 + bx + c = 0 is:",
        "−b/a",
        ["c/a", "b/a", "−c/a"],
    ),
    _q(
        "Product of roots of ax2 + bx + c = 0 is:",
        "c/a",
        ["−b/a", "b/a", "−c/a"],
    ),
    _q(
        "The equation x2 − 5x + 6 = 0 has roots:",
        "2 and 3",
        ["1 and 6", "−2 and −3", "5 and 6"],
    ),
    _q(
        "If D = 0, the quadratic has:",
        "Two equal real roots",
        ["No roots", "Only complex non-real roots", "Infinite roots"],
    ),
]

BANK_LINEAR_EQ: QuestionBank = [
    _q(
        "A linear equation in two variables represents:",
        "A straight line",
        ["A circle", "A parabola", "A hyperbola"],
    ),
    _q(
        "The solution of 2x + 3 = 11 is:",
        "x = 4",
        ["x = 7", "x = 2", "x = 5"],
    ),
    _q(
        "If two lines intersect at one point, the system has:",
        "A unique solution",
        ["No solution", "Infinitely many solutions", "Exactly two unrelated solutions always"],
    ),
    _q(
        "Parallel distinct lines correspond to a system with:",
        "No solution",
        ["Unique solution", "Infinitely many solutions", "Exactly three solutions"],
    ),
]

BANK_TRIG: QuestionBank = [
    _q(
        "sin2θ + cos2θ equals:",
        "1",
        ["0", "2", "tan θ"],
    ),
    _q(
        "tan θ equals:",
        "sin θ / cos θ",
        ["cos θ / sin θ", "sin θ cos θ", "1 / sin θ"],
    ),
    _q(
        "sin 90° equals:",
        "1",
        ["0", "1/2", "√3/2"],
    ),
    _q(
        "cos 0° equals:",
        "1",
        ["0", "−1", "1/2"],
    ),
    _q(
        "The value of sin 30° is:",
        "1/2",
        ["√3/2", "0", "1"],
    ),
    _q(
        "sec θ is the reciprocal of:",
        "cos θ",
        ["sin θ", "tan θ", "cot θ"],
    ),
]

BANK_PROBABILITY: QuestionBank = [
    _q(
        "Probability of an impossible event is:",
        "0",
        ["1", "1/2", "−1"],
    ),
    _q(
        "Probability of a sure event is:",
        "1",
        ["0", "1/2", "2"],
    ),
    _q(
        "If a fair coin is tossed, P(Head) is:",
        "1/2",
        ["1", "0", "2"],
    ),
    _q(
        "P(E) + P(not E) equals:",
        "1",
        ["0", "2", "1/2"],
    ),
    _q(
        "In a fair die, P(getting 5) is:",
        "1/6",
        ["1/5", "5/6", "1"],
    ),
]

BANK_AP: QuestionBank = [
    _q(
        "In an AP, the nth term is:",
        "a + (n − 1)d",
        ["a + nd", "a − (n − 1)d always for all AP", "n a d"],
    ),
    _q(
        "Sum of first n terms of an AP is:",
        "n/2 [2a + (n − 1)d]",
        ["n [a + d]", "a n d", "n/2 (a − d)"],
    ),
    _q(
        "If a = 2, d = 3, the 4th term is:",
        "11",
        ["8", "14", "5"],
    ),
    _q(
        "Common difference of AP 3, 7, 11, 15 is:",
        "4",
        ["3", "7", "1"],
    ),
]

BANK_CALCULUS_LIMITS: QuestionBank = [
    _q(
        "lim(x→0) (sin x)/x equals:",
        "1",
        ["0", "∞", "−1"],
    ),
    _q(
        "The derivative of xⁿ with respect to x is:",
        "n xⁿ-1",
        ["n xⁿ", "xⁿ / n", "nⁿ x"],
    ),
    _q(
        "The derivative of a constant is:",
        "0",
        ["1", "the constant itself", "∞"],
    ),
    _q(
        "∫ xⁿ dx (n ≠ −1) equals:",
        "xⁿ⁺1/(n+1) + C",
        ["n xⁿ-1 + C", "xⁿ + C", "n! + C"],
    ),
]

# ---------------------------------------------------------------------------
# Biology
# ---------------------------------------------------------------------------

BANK_CELL: QuestionBank = [
    _q(
        "The basic structural and functional unit of life is the:",
        "Cell",
        ["Tissue only", "Organ only", "Atom only"],
    ),
    _q(
        "The powerhouse of the cell is the:",
        "Mitochondrion",
        ["Ribosome", "Golgi apparatus", "Lysosome"],
    ),
    _q(
        "Ribosomes are the site of:",
        "Protein synthesis",
        ["Photosynthesis", "Lipid storage only", "DNA replication exclusively in all cells incorrectly"],
    ),
    _q(
        "Plant cells differ from animal cells in having:",
        "Cell wall and chloroplasts (typically)",
        ["Only mitochondria and never ribosomes", "No nucleus ever", "No membrane"],
    ),
    _q(
        "The control centre of the cell is the:",
        "Nucleus",
        ["Vacuole only", "Cell wall", "Centrosome only"],
    ),
    _q(
        "Prokaryotic cells lack a:",
        "True membrane-bound nucleus",
        ["Cell membrane", "DNA", "Ribosomes"],
    ),
]

BANK_PHOTOSYNTHESIS: QuestionBank = [
    _q(
        "Photosynthesis mainly occurs in:",
        "Chloroplasts",
        ["Mitochondria", "Ribosomes", "Lysosomes"],
    ),
    _q(
        "The green pigment essential for photosynthesis is:",
        "Chlorophyll",
        ["Haemoglobin", "Melanin", "Insulin"],
    ),
    _q(
        "Overall photosynthesis converts CO2 and H2O into:",
        "Carbohydrates and oxygen",
        ["Only proteins", "Only urea", "Only nitrogen gas"],
    ),
    _q(
        "Light reaction of photosynthesis mainly produces:",
        "ATP and NADPH (and O2 from water)",
        ["Glucose only in the thylakoid with no ATP", "Urea", "Amino acids only"],
    ),
    _q(
        "The site of the light reaction in chloroplasts is mainly the:",
        "Thylakoid membrane",
        ["Stroma only with no membranes", "Nucleus", "Cell wall"],
    ),
    _q(
        "Oxygen released during photosynthesis comes mainly from:",
        "Water",
        ["Carbon dioxide only", "Nitrogen gas", "Glucose"],
    ),
]

BANK_CALVIN: QuestionBank = [
    _q(
        "The Calvin cycle is part of the:",
        "Dark reaction (biosynthetic phase)",
        ["Krebs cycle only", "Glycolysis only", "Transcription only"],
    ),
    _q(
        "The Calvin cycle mainly fixes:",
        "Carbon dioxide into carbohydrates",
        ["Nitrogen into amino acids only", "Oxygen into ozone only", "Water into hydrogen gas only"],
    ),
    _q(
        "The first stable product commonly associated with C3 Calvin cycle is related to:",
        "A 3-carbon compound (3-PGA)",
        ["A 6-carbon sugar formed instantly as the only step", "Methane", "Urea"],
    ),
    _q(
        "ATP and NADPH used in the Calvin cycle are produced mainly by the:",
        "Light reaction",
        ["Glycolysis only", "Transcription only", "Protein digestion only"],
    ),
    _q(
        "The Calvin cycle takes place mainly in the:",
        "Stroma of the chloroplast",
        ["Mitochondrial matrix only", "Cytoplasm of animal cells only", "Nucleus"],
    ),
    _q(
        "Rubisco is important in the Calvin cycle because it:",
        "Catalyses carboxylation of RuBP",
        ["Digests proteins in the stomach", "Carries oxygen in blood", "Makes ATP in mitochondria only"],
    ),
    _q(
        "Without ATP and NADPH, the Calvin cycle would:",
        "Be unable to synthesise sugars effectively",
        ["Run faster indefinitely", "Produce only magnetic fields", "Replace photosynthesis entirely"],
    ),
    _q(
        "The Calvin cycle is also called the biosynthetic phase because it:",
        "Builds carbohydrates using products of the light reaction",
        ["Breaks glucose only like respiration", "Copies DNA", "Transports electrons in metals"],
    ),
]

BANK_GENETICS: QuestionBank = [
    _q(
        "Mendel is known for experiments on:",
        "Inheritance in pea plants",
        ["Electric motors", "Planetary motion", "Atomic nuclei"],
    ),
    _q(
        "A gene is best described as:",
        "A unit of heredity (segment of DNA influencing a trait)",
        ["A type of protein hormone only", "A carbohydrate storage form", "A cell organelle"],
    ),
    _q(
        "In a monohybrid cross of pure tall and pure dwarf pea plants, F1 are:",
        "All tall (with tall dominant)",
        ["All dwarf", "Half tall half dwarf always in F1 for complete dominance incorrectly", "All medium height always"],
    ),
    _q(
        "DNA stands for:",
        "Deoxyribonucleic acid",
        ["Dinitrogen oxide acid", "Dynamic nuclear atom", "Dual nutrient acid"],
    ),
    _q(
        "Phenotype refers to:",
        "Observable traits",
        ["Only the DNA sequence hidden", "Only chromosome number", "Only mutation rate"],
    ),
]

BANK_HUMAN_PHYSIOLOGY: QuestionBank = [
    _q(
        "The human heart has how many chambers?",
        "Four",
        ["Two", "Three", "Five"],
    ),
    _q(
        "Oxygenated blood in humans is carried from lungs to heart mainly by:",
        "Pulmonary veins",
        ["Pulmonary arteries", "Hepatic portal vein only", "Lymph vessels only"],
    ),
    _q(
        "Nephrons are the functional units of the:",
        "Kidney",
        ["Liver", "Lung", "Brain"],
    ),
    _q(
        "Insulin is secreted by the:",
        "Pancreas",
        ["Thyroid only", "Adrenal medulla only", "Pituitary only"],
    ),
    _q(
        "The largest gland in the human body is the:",
        "Liver",
        ["Pancreas", "Thyroid", "Pituitary"],
    ),
]

# ---------------------------------------------------------------------------
# Social science / commerce samples
# ---------------------------------------------------------------------------

BANK_DEMOCRACY: QuestionBank = [
    _q(
        "In a democracy, the final decision-making power rests with:",
        "The people (through representatives or direct means as applicable)",
        ["A hereditary monarch only by definition of democracy", "The military alone", "Foreign companies alone"],
    ),
    _q(
        "Universal adult franchise means:",
        "All adults have the right to vote",
        ["Only men can vote", "Only taxpayers can vote", "Only the educated can vote"],
    ),
    _q(
        "Free and fair elections are essential to:",
        "Democratic government",
        ["Dictatorship by definition", "Monarchy without elections", "Anarchy"],
    ),
]

BANK_ACCOUNTING_BASICS: QuestionBank = [
    _q(
        "The accounting equation is:",
        "Assets = Liabilities + Capital (Equity)",
        ["Assets = Liabilities − Capital", "Assets + Liabilities = Capital", "Capital = Assets × Liabilities"],
    ),
    _q(
        "A journal entry records:",
        "Debit and credit aspects of a transaction",
        ["Only cash balances monthly", "Only trial balance totals", "Only balance sheet headings"],
    ),
    _q(
        "Debit what comes in and credit what goes out applies mainly to:",
        "Real accounts (traditional rules)",
        ["Only nominal accounts incorrectly stated as sole rule", "Only personal accounts incorrectly as sole rule", "No accounts"],
    ),
    _q(
        "A trial balance is prepared to:",
        "Check arithmetic accuracy of ledger balances",
        ["Replace the balance sheet forever", "Eliminate all errors of principle", "Compute tax automatically"],
    ),
]

BANK_DEMAND_SUPPLY: QuestionBank = [
    _q(
        "Law of demand states that, other things equal, when price rises:",
        "Quantity demanded falls",
        ["Quantity demanded rises", "Demand becomes infinite", "Supply becomes zero"],
    ),
    _q(
        "A rightward shift of the demand curve means:",
        "Increase in demand",
        ["Decrease in demand", "No change in demand", "Supply shock only"],
    ),
    _q(
        "Equilibrium price is where:",
        "Quantity demanded equals quantity supplied",
        ["Demand is zero", "Supply is infinite", "Price is always zero"],
    ),
    _q(
        "Price elasticity of demand measures:",
        "Responsiveness of quantity demanded to price changes",
        ["Only income of sellers", "Only government tax rate formula with no demand", "Only population size"],
    ),
]

# Map: normalized topic key / alias -> bank
CONCEPT_BANKS: dict[str, QuestionBank] = {}

# (chapter_title, topic_title) -> bank for titles that collide across chapters
GLOBAL_CHAPTER_TOPIC_BANKS: dict[tuple[str, str], QuestionBank] = {}

# Subject code -> keyword tuples mapped to banks (filled by quiz_banks/*.register)
SUBJECT_KEYWORD_BANKS: dict[str, list[tuple[tuple[str, ...], QuestionBank]]] = {}


def _register(keys: list[str], bank: QuestionBank) -> None:
    for key in keys:
        CONCEPT_BANKS[key.strip().lower()] = bank


_register(
    [
        "electric charge",
        "basic properties of electric charge",
        "conductors and insulators",
        "charging by induction",
    ],
    BANK_ELECTRIC_CHARGE,
)
_register(
    [
        "coulomb's law",
        "coulombs law",
        "forces between multiple charges",
    ],
    BANK_COULOMB,
)
_register(
    [
        "electric field",
        "electric field lines",
        "electric field due to a point charge",
        "continuous charge distribution",
        "electric dipole",
    ],
    BANK_ELECTRIC_FIELD,
)
_register(
    [
        "electric flux",
        "gauss's law",
        "gausss law",
        "applications of gauss's law",
    ],
    BANK_ELECTRIC_FLUX_GAUSS,
)
_register(
    [
        "ohm's law",
        "ohms law",
        "electric current",
        "electric currents in conductors",
        "drift of electrons and the origin of resistivity",
        "resistivity of various materials",
        "temperature dependence of resistivity",
        "electrical energy and power",
        "combination of resistors",
        "limitations of ohm's law",
    ],
    BANK_OHM,
)
_register(
    [
        "newton's laws",
        "newton's first law of motion",
        "newton's second law of motion",
        "newton's third law of motion",
        "law of inertia",
        "aristotle's fallacy and the law of inertia",
        "conservation of momentum",
        "equilibrium of a particle",
        "common forces in mechanics",
        "circular motion and banking of roads",
        "friction",
        "circular motion dynamics",
    ],
    BANK_NEWTON,
)
_register(
    [
        "position path length and displacement",
        "average velocity and average speed",
        "instantaneous velocity and speed",
        "acceleration",
        "kinematic equations for uniformly accelerated motion",
        "relative velocity in one dimension",
        "position and displacement",
        "average and instantaneous velocity",
        "acceleration and kinematic equations",
        "motion in a straight line",
    ],
    BANK_KINEMATICS,
)
_register(
    [
        "work done by a constant force",
        "work done by a variable force",
        "kinetic energy",
        "work-energy theorem",
        "potential energy",
        "conservation of mechanical energy",
        "power",
        "collisions",
        "work done by a force",
        "kinetic and potential energy",
        "conservation of energy and power",
        "work, energy and power",
    ],
    BANK_ENERGY,
)
_register(
    [
        "mole concept and stoichiometry",
        "atomic and molecular masses",
        "matter and laws of chemical combination",
        "some basic concepts of chemistry",
    ],
    BANK_MOLE,
)
_register(
    [
        "atomic models",
        "bohr model",
        "bohr model of the hydrogen atom",
        "quantum numbers and electronic configuration",
        "structure of atom",
        "structure of the atom",
    ],
    BANK_ATOMIC_STRUCTURE,
)
_register(
    [
        "photoelectric effect",
        "experimental study of photoelectric effect",
        "einstein's photoelectric equation",
        "einstein's equation",
        "electron emission",
        "particle nature of light",
        "wave nature of matter",
        "davisson and germer experiment",
        "de broglie waves",
        "de broglie's explanation of bohr's second postulate",
    ],
    BANK_PHOTOELECTRIC,
)
_register(
    [
        "modern periodic table",
        "periodic trends",
        "valency and oxidation state",
        "classification of elements and periodicity in properties",
    ],
    BANK_PERIODIC,
)
_register(
    [
        "ionic and covalent bonds",
        "vsepr and hybridisation",
        "molecular orbital ideas",
        "chemical bonding and molecular structure",
    ],
    BANK_CHEMICAL_BONDING,
)
_register(
    [
        "physical and chemical equilibrium",
        "law of mass action",
        "ionic equilibrium and ph",
        "equilibrium",
    ],
    BANK_EQUILIBRIUM,
)
_register(
    [
        "tetravalence of carbon",
        "functional groups and nomenclature",
        "isomerism and reaction types",
        "alkanes",
        "alkenes and alkynes",
        "aromatic hydrocarbons",
        "hydrocarbons",
        "organic chemistry — some basic principles and techniques",
    ],
    BANK_ORGANIC_BASICS,
)
_register(
    [
        "quadratic equations",
        "standard form",
        "nature of roots",
        "solving quadratic equations",
    ],
    BANK_QUADRATIC,
)
_register(
    [
        "pair of linear equations in two variables",
        "graphical method",
        "algebraic methods",
        "linear equations",
        "introduction to linear polynomials",
        "simple equations",
        "finding the unknown",
    ],
    BANK_LINEAR_EQ,
)
_register(
    [
        "trigonometric ratios",
        "identities",
        "values of standard angles",
        "introduction to trigonometry",
        "trigonometric functions",
        "angles",
        "identities and equations",
    ],
    BANK_TRIG,
)
_register(
    [
        "probability",
        "classical probability",
        "simple events",
        "complementary events",
        "chance and outcomes",
        "experimental probability",
        "the mathematics of maybe: introduction to probability",
        "axiomatic probability",
        "random experiments",
        "event",
    ],
    BANK_PROBABILITY,
)
_register(
    [
        "arithmetic progressions",
        "nth term",
        "sum of n terms",
        "applications",
        "arithmetic progression",
        "sequences and series",
    ],
    BANK_AP,
)
_register(
    [
        "limits and derivatives",
        "intuitive idea of limit",
        "limits",
        "derivative",
        "continuity",
        "differentiability",
        "integrals",
        "indefinite integrals",
        "methods of integration",
        "definite integrals",
    ],
    BANK_CALCULUS_LIMITS,
)
_register(
    [
        "cell theory",
        "cell organelles",
        "prokaryotic and eukaryotic cells",
        "the fundamental unit of life",
        "cell: the unit of life",
        "cell structure",
    ],
    BANK_CELL,
)
_register(
    [
        "photosynthesis",
        "photosynthetic pigments",
        "light reaction",
        "photosynthesis in higher plants",
    ],
    BANK_PHOTOSYNTHESIS,
)
_register(
    [
        "calvin cycle",
    ],
    BANK_CALVIN,
)
_register(
    [
        "traits and variation",
        "mendel's experiments",
        "sex determination",
        "heredity",
        "mendel's laws",
        "genetic disorders",
        "principles of inheritance and variation",
        "dna as genetic material",
        "replication transcription translation",
        "genetic code and regulation",
        "molecular basis of inheritance",
    ],
    BANK_GENETICS,
)
_register(
    [
        "human circulatory system",
        "cardiac cycle",
        "blood",
        "body fluids and circulation",
        "human excretory system",
        "urine formation",
        "excretory products and their elimination",
        "endocrine glands",
        "hormones",
        "feedback control",
        "chemical coordination and integration",
        "nutrition",
        "respiration",
        "transportation and excretion",
        "life processes",
    ],
    BANK_HUMAN_PHYSIOLOGY,
)
_register(
    [
        "what is democracy",
        "features of democracy",
        "why democracy",
        "democracy",
        "why elections",
        "electoral process",
        "free and fair elections",
        "elections",
    ],
    BANK_DEMOCRACY,
)
_register(
    [
        "accounting equation",
        "rules of debit and credit",
        "journal",
        "ledger",
        "cash book",
        "other subsidiary books",
        "trial balance",
        "types of errors",
        "rectification",
        "theory base of accounting",
        "introduction to accounting",
        "meaning of accounting",
        "objectives of accounting",
        "basic accounting terms",
        "recording of transactions — i",
        "recording of transactions — ii",
        "trial balance and rectification of errors",
    ],
    BANK_ACCOUNTING_BASICS,
)
_register(
    [
        "demand",
        "supply",
        "how prices are formed",
        "the price puzzle",
        "utility",
        "indifference curve idea",
        "demand and elasticity",
        "consumer's equilibrium and demand",
        "production function",
        "cost and revenue",
        "producer behaviour and supply",
    ],
    BANK_DEMAND_SUPPLY,
)

BANK_SQUARES_CUBES: QuestionBank = [
    _q(
        "Which of the following is a perfect square?",
        "36",
        ["20", "18", "40"],
    ),
    _q(
        "The square of 12 is:",
        "144",
        ["124", "132", "156"],
    ),
    _q(
        "Which number is a perfect cube?",
        "27",
        ["18", "20", "30"],
    ),
    _q(
        "The cube of 5 is:",
        "125",
        ["25", "15", "100"],
    ),
    _q(
        "√81 equals:",
        "9",
        ["8", "18", "41"],
    ),
    _q(
        "∛64 equals:",
        "4",
        ["8", "16", "32"],
    ),
    _q(
        "If a number ends with digit 2, can it be a perfect square?",
        "No",
        ["Yes always", "Only if even", "Only if odd"],
    ),
    _q(
        "13 + 23 + ... pattern for cubes is related to:",
        "Square of triangular numbers (sum of first n cubes = (n(n+1)/2)2)",
        ["Only prime numbers", "Only Fibonacci always", "Only odd numbers summing to cubes incorrectly"],
    ),
    _q(
        "The units digit of a perfect square cannot be:",
        "2, 3, 7 or 8",
        ["0 or 5", "1 or 4", "6 or 9"],
    ),
    _q(
        "62 equals:",
        "36",
        ["12", "18", "30"],
    ),
]

BANK_MESOPOTAMIA: QuestionBank = [
    _q(
        "Mesopotamia lies mainly between which rivers?",
        "Tigris and Euphrates",
        ["Nile and Congo", "Indus and Ganga", "Yellow and Yangtze"],
    ),
    _q(
        "The term Mesopotamia literally refers to the land:",
        "Between rivers",
        ["Above mountains only", "Under the sea", "Beyond the Arctic circle"],
    ),
    _q(
        "Early Mesopotamian cities depended heavily on:",
        "Irrigation agriculture",
        ["Only Arctic hunting", "Only desert dunes with no water management", "Only space trade"],
    ),
    _q(
        "A ziggurat in Mesopotamia was primarily a:",
        "Temple tower / religious structure",
        ["Modern railway station", "Iron age factory", "Democratic parliament of India"],
    ),
    _q(
        "Which civilization is most closely associated with the region of Mesopotamia?",
        "Sumerian (among other Mesopotamian cultures)",
        ["Inuit polar culture only", "Maori only", "Aztec only exclusively"],
    ),
    _q(
        "Long-distance trade in Mesopotamia was important because cities needed:",
        "Resources not available locally, such as metals and timber",
        ["Only snow from glaciers", "Only petroleum plastics", "Nothing from outside ever"],
    ),
    _q(
        "Kingship and temple institutions in Mesopotamia were closely linked to:",
        "Urban administration and redistribution",
        ["Only modern stock markets", "Only printing press technology", "Only steam engines"],
    ),
    _q(
        "Floods of the Tigris and Euphrates influenced Mesopotamian life by:",
        "Making irrigation and water control essential for farming",
        ["Eliminating all need for agriculture", "Creating permanent ice sheets", "Stopping all trade forever"],
    ),
]

BANK_CUNEIFORM: QuestionBank = [
    _q(
        "Cuneiform writing was developed in ancient:",
        "Mesopotamia",
        ["China only", "Greece only", "Medieval Europe only"],
    ),
    _q(
        "Cuneiform characters were typically written on:",
        "Clay tablets",
        ["Paper only", "Silk only", "Palm leaves only"],
    ),
    _q(
        "Which tool was commonly used to impress cuneiform signs?",
        "A reed stylus",
        ["A laser printer", "A fountain pen only", "A typewriter"],
    ),
    _q(
        "Cuneiform was used for:",
        "Record-keeping, laws, literature and administration",
        ["Only modern email", "Only binary computer code", "Only Morse telegraphy"],
    ),
    _q(
        "The wedge-shaped appearance of cuneiform signs comes from:",
        "Pressing a stylus into soft clay",
        ["Painting with oil on canvas only", "Carving only in ice", "Printing with movable metal type only"],
    ),
    _q(
        "Which script is closely associated with Mesopotamian record-keeping?",
        "Cuneiform",
        ["Devanagari only", "Latin alphabet only", "Braille only"],
    ),
    _q(
        "Clay tablets with cuneiform could be made more durable by:",
        "Baking / hardening the clay",
        ["Freezing in space", "Dissolving in acid", "Leaving them underwater forever"],
    ),
    _q(
        "Literacy in cuneiform was mainly associated with:",
        "Scribes trained for administration and temple work",
        ["Every child using smartphones", "Only sailors using GPS", "Only farmers using tractors"],
    ),
]

BANK_URBAN_LIFE: QuestionBank = [
    _q(
        "Urban life in early Mesopotamia was centred around:",
        "Cities with temples, trade and administration",
        ["Only isolated caves with no trade", "Only nomadic camps forever", "Only industrial factories"],
    ),
    _q(
        "A city differs from a village primarily by:",
        "Greater density, specialised occupations and administrative institutions",
        ["Having no people", "Having no buildings", "Having only one family always"],
    ),
    _q(
        "Craft specialists in early cities typically:",
        "Produced goods for exchange within urban economies",
        ["Never exchanged anything", "Only hunted polar bears", "Only coded software"],
    ),
    _q(
        "Urban temples often functioned as:",
        "Religious and economic centres",
        ["Only football stadiums", "Only airports", "Only nuclear plants"],
    ),
    _q(
        "Division of labour in cities means:",
        "Different people specialise in different tasks",
        ["Everyone does identical work only", "No work is done", "Only machines vote"],
    ),
    _q(
        "Trade networks supported urban life by:",
        "Bringing in scarce materials and distributing surplus",
        ["Stopping all movement of goods", "Eliminating agriculture everywhere", "Removing writing systems"],
    ),
    _q(
        "Public architecture in early cities often included:",
        "Temples, walls and administrative buildings",
        ["Only skyscraper glass malls of today", "Only subway metros", "Only satellite dishes"],
    ),
    _q(
        "Why is writing important for urban administration?",
        "It helps record transactions, laws and inventories",
        ["It replaces food completely", "It stops irrigation", "It removes the need for language"],
    ),
]

_register(
    [
        "square numbers",
        "cube numbers",
        "patterns in squares and cubes",
        "a square and a cube",
    ],
    BANK_SQUARES_CUBES,
)
_register(["mesopotamia"], BANK_MESOPOTAMIA)
_register(["cuneiform writing"], BANK_CUNEIFORM)
_register(["urban life"], BANK_URBAN_LIFE)


# Keyword → bank for fuzzy matching when exact title not registered
KEYWORD_BANKS: list[tuple[tuple[str, ...], QuestionBank]] = [
    (("coulomb",), BANK_COULOMB),
    (("electric charge", "quantization of charge", "conservation of charge"), BANK_ELECTRIC_CHARGE),
    (("electric field line", "electric field"), BANK_ELECTRIC_FIELD),
    (("gauss", "electric flux"), BANK_ELECTRIC_FLUX_GAUSS),
    (("ohm", "resistivity", "drift"), BANK_OHM),
    (("newton", "inertia", "momentum"), BANK_NEWTON),
    (("kinematic", "displacement", "velocity", "acceleration"), BANK_KINEMATICS),
    (("kinetic energy", "potential energy", "work-energy", "work done"), BANK_ENERGY),
    (("photoelectric", "de broglie", "photon"), BANK_PHOTOELECTRIC),
    (("mole", "avogadro", "stoichiometr"), BANK_MOLE),
    (("bohr", "atomic model", "nucleus", "electron"), BANK_ATOMIC_STRUCTURE),
    (("periodic table", "periodic trend", "electronegativ"), BANK_PERIODIC),
    (("covalent", "ionic bond", "vsepr", "hybridis"), BANK_CHEMICAL_BONDING),
    (("equilibrium", "le chatelier", "kc "), BANK_EQUILIBRIUM),
    (("alkane", "alkene", "functional group", "isomer"), BANK_ORGANIC_BASICS),
    (("quadratic", "discriminant"), BANK_QUADRATIC),
    (("linear equation", "pair of linear"), BANK_LINEAR_EQ),
    (("sin ", "cos ", "tan ", "trigonometr"), BANK_TRIG),
    (("probability", "random experiment"), BANK_PROBABILITY),
    (("arithmetic progression", "common difference"), BANK_AP),
    (("derivative", "integral", "limit"), BANK_CALCULUS_LIMITS),
    (("mitochondr", "ribosome", "cell wall", "prokaryot", "eukaryot", "cell theory", "cell organelle"), BANK_CELL),
    (("photosynth", "chlorophyll", "light reaction"), BANK_PHOTOSYNTHESIS),
    (("calvin",), BANK_CALVIN),
    (("mendel", "heredity", "allele", "phenotype", "genotype", "dna"), BANK_GENETICS),
    (("nephron", "insulin", "circulat", "heart", "liver"), BANK_HUMAN_PHYSIOLOGY),
    (("democracy", "franchise", "election"), BANK_DEMOCRACY),
    (("accounting equation", "journal", "ledger", "trial balance", "debit"), BANK_ACCOUNTING_BASICS),
    (("elasticity", "quantity demanded", "demand curve", "supply curve"), BANK_DEMAND_SUPPLY),
    (("square number", "perfect square", "perfect cube", "cube number"), BANK_SQUARES_CUBES),
    (("mesopotamia", "tigris", "euphrates", "ziggurat"), BANK_MESOPOTAMIA),
    (("cuneiform",), BANK_CUNEIFORM),
    (("urban life", "early cities"), BANK_URBAN_LIFE),
]


def _load_subject_banks() -> None:
    """Register Class 12+ subject modules into CONCEPT_BANKS / chapter maps."""
    from app.data.quiz_banks import register_all

    register_all()


_load_subject_banks()
