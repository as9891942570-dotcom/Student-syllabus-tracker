"""EduQuest CBSE Class 12 Physics — concept banks for topics beyond core quiz_concepts coverage."""

from __future__ import annotations

from app.data.quiz_banks.common import QuestionBank, q, register_keys, register_subject_keywords

# ---------------------------------------------------------------------------
# Electrostatic Potential and Capacitance
# ---------------------------------------------------------------------------

BANK_ELECTROSTATIC_POTENTIAL: QuestionBank = [
    q(
        "Electrostatic potential at a point is defined as the work done per unit charge in bringing a test charge from infinity to that point:",
        "Without acceleration",
        ["With acceleration only", "Against gravity only", "Only inside conductors"],
    ),
    q(
        "The SI unit of electrostatic potential is:",
        "Volt (V)",
        ["Joule per coulomb is equivalent but not the SI name", "Newton", "Weber"],
    ),
    q(
        "Electrostatic potential is a:",
        "Scalar quantity",
        ["Vector quantity", "Tensor quantity", "Always negative scalar only"],
    ),
    q(
        "If the electrostatic potential is constant in a region, the electric field in that region is:",
        "Zero",
        ["Maximum", "Always radial outward", "Equal to potential value"],
    ),
    q(
        "Potential difference between two points A and B is V_A − V_B. A positive charge moved from A to B:",
        "Loses potential energy if V_A > V_B",
        ["Always gains energy regardless of potentials", "Never experiences force", "Always doubles its charge"],
    ),
    q(
        "1 volt is equivalent to:",
        "1 joule per coulomb",
        ["1 coulomb per joule", "1 newton per metre", "1 tesla per ampere"],
    ),
    q(
        "Along the direction of the electric field, electrostatic potential:",
        "Decreases",
        ["Increases", "Remains always zero", "Oscillates sinusoidally"],
    ),
]

BANK_POTENTIAL_POINT_CHARGE: QuestionBank = [
    q(
        "Electrostatic potential due to a point charge q at distance r in vacuum is V =:",
        "k q / r",
        ["k q r", "k q / r²", "q / 4πr"],
    ),
    q(
        "At infinite distance from an isolated point charge, the potential is taken as:",
        "Zero",
        ["Infinite", "Equal to kq", "Equal to the field magnitude"],
    ),
    q(
        "For a positive point charge, electrostatic potential near the charge is:",
        "Positive",
        ["Negative", "Always zero", "Independent of sign of q"],
    ),
    q(
        "If distance from a point charge is doubled, the potential becomes:",
        "Half the original value",
        ["One-fourth", "Double", "Unchanged"],
    ),
    q(
        "Potential due to a point charge q = +2 μC at 3 m is (k ≈ 9×10⁹ N·m²/C²):",
        "6000 V",
        ["600 V", "60 V", "6×10⁶ V"],
    ),
    q(
        "The potential due to a negative point charge at a finite distance is:",
        "Negative",
        ["Positive", "Zero always", "Complex valued"],
    ),
    q(
        "Superposition of potentials from multiple point charges is valid because potential is a:",
        "Scalar",
        ["Vector that adds with angles", "Pseudoscalar only in vacuum", "Non-linear quantity"],
    ),
]

BANK_POTENTIAL_DIPOLE: QuestionBank = [
    q(
        "On the axial line of an electric dipole at large distance r, potential varies approximately as:",
        "1 / r²",
        ["1 / r", "1 / r³", "Independent of r"],
    ),
    q(
        "On the equatorial line of an electric dipole, electrostatic potential at any point is:",
        "Zero",
        ["Maximum", "k p / r", "Always negative only"],
    ),
    q(
        "Potential due to a dipole moment p at distance r on axis (r >> separation) is approximately:",
        "k p cos θ / r²",
        ["k p / r", "k p r", "Zero always"],
    ),
    q(
        "For an electric dipole, the potential at the midpoint of the dipole on the equatorial plane is:",
        "Zero",
        ["Infinite", "Maximum positive", "Equal to k q / a"],
    ),
    q(
        "The dipole potential at a far point depends on angle θ between position vector and dipole moment as:",
        "cos θ",
        ["sin θ only", "tan θ", "Independent of θ"],
    ),
    q(
        "Compared to a single charge, dipole potential falls off faster at large r because leading term is:",
        "Dipole (1/r²) not monopole (1/r)",
        ["Monopole dominates always", "Both fall as 1/r", "Potential is constant at large r"],
    ),
    q(
        "Work done in rotating a dipole in a uniform electric field depends on:",
        "Initial and final orientation of dipole moment",
        ["Only mass of dipole", "Only temperature", "Speed of rotation only"],
    ),
]

BANK_EQUIPOTENTIAL: QuestionBank = [
    q(
        "Equipotential surfaces are surfaces on which:",
        "Potential is the same at every point",
        ["Field is zero everywhere in space", "Charge density is maximum", "Current is constant"],
    ),
    q(
        "Electric field lines are ______ to equipotential surfaces:",
        "Perpendicular",
        ["Parallel", "At 45° always", "Unrelated in direction"],
    ),
    q(
        "No work is done in moving a charge along an equipotential surface because:",
        "Potential difference is zero",
        ["Force is infinite", "Charge becomes zero", "Field is parallel to displacement"],
    ),
    q(
        "Equipotential surfaces near an isolated point charge are:",
        "Concentric spheres",
        ["Parallel planes only", "Straight lines through origin", "Hyperbolas only"],
    ),
    q(
        "For a uniform electric field, equipotential surfaces are:",
        "Planes perpendicular to the field",
        ["Spheres centered at infinity", "Cylinders along field", "Random curves"],
    ),
    q(
        "Two equipotential surfaces can intersect only if:",
        "They cannot intersect (except at singularities); distinct surfaces do not cross",
        ["They always cross at right angles twice", "Field is zero everywhere", "Charge is zero in universe"],
    ),
    q(
        "Closely spaced equipotential surfaces indicate:",
        "Stronger electric field (steeper potential gradient)",
        ["Weaker field", "Zero field", "Uniform zero potential"],
    ),
]

BANK_PE_SYSTEM_CHARGES: QuestionBank = [
    q(
        "Electrostatic potential energy of two charges q₁ and q₂ separated by r is:",
        "k q₁ q₂ / r",
        ["k q₁ q₂ r", "k (q₁ + q₂) / r", "q₁ q₂ / r² only without k"],
    ),
    q(
        "Potential energy of a system of charges is minimum when:",
        "Unlike charges are closer and like charges farther (for bound systems)",
        ["All like charges are closest", "All charges at infinity with higher U", "Charge is zero"],
    ),
    q(
        "Work done in assembling charges into a configuration equals:",
        "Final potential energy of the configuration",
        ["Always zero", "Kinetic energy only", "Thermal energy only"],
    ),
    q(
        "If three identical positive charges are placed at corners of an equilateral triangle, the net potential energy is:",
        "Positive (mutual repulsion stored as energy)",
        ["Always negative", "Always zero", "Purely magnetic"],
    ),
    q(
        "Potential energy of a charge q in potential V is:",
        "U = q V",
        ["U = q / V", "U = V / q always", "U = q V²"],
    ),
    q(
        "When a positive charge moves to lower potential, its potential energy:",
        "Decreases",
        ["Increases", "Doubles always", "Becomes infinite"],
    ),
    q(
        "For two positive charges brought from infinity to separation r, external work done is:",
        "Positive",
        ["Negative", "Zero always", "Independent of distance"],
    ),
]

BANK_CONDUCTORS_ES: QuestionBank = [
    q(
        "In electrostatic equilibrium, the electric field inside a conductor is:",
        "Zero",
        ["Maximum at centre", "Same as outside always", "Uniform non-zero"],
    ),
    q(
        "Excess charge on an isolated conductor in equilibrium resides:",
        "On the outer surface",
        ["Uniformly throughout volume", "Only at geometric centre", "Nowhere"],
    ),
    q(
        "The interior of a conductor in electrostatic equilibrium is at:",
        "Constant potential",
        ["Varying potential", "Zero potential always", "Infinite potential"],
    ),
    q(
        "Just outside a charged conductor surface, electric field is:",
        "Perpendicular to the surface",
        ["Parallel to surface", "Zero always", "Tangential only"],
    ),
    q(
        "A cavity inside a conductor shields the interior from external static fields (electrostatic shielding) because:",
        "Field inside bulk conductor is zero and induced charges cancel external field in cavity if no internal charge",
        ["Conductors block all radiation frequencies equally", "Gravity cancels field", "Charge cannot exist on surface"],
    ),
    q(
        "Charge given to a hollow conductor distributes:",
        "On the outer surface",
        ["On inner surface only", "Uniform in shell volume", "At a single point inside"],
    ),
    q(
        "Two conductors connected by a wire in equilibrium have:",
        "Same potential",
        ["Different potentials always", "Zero charge always", "Infinite field between them"],
    ),
]

BANK_DIELECTRICS: QuestionBank = [
    q(
        "When a dielectric is placed in an electric field, it develops:",
        "Polarisation (induced dipole moments)",
        ["Free current loops only", "Permanent monopoles", "No response"],
    ),
    q(
        "Dielectric constant κ is defined as the ratio:",
        "E₀ / E (vacuum field to field in medium)",
        ["E / E₀", "Charge density ratio only", "Resistance ratio"],
    ),
    q(
        "Polarisation P is related to electric field in linear isotropic dielectric as P =:",
        "ε₀ χ_e E",
        ["ε₀ E / χ_e", "q E only", "B × E"],
    ),
    q(
        "In a dielectric, the net electric field compared to vacuum for same free charge is:",
        "Reduced",
        ["Increased", "Unchanged always", "Reversed in direction always"],
    ),
    q(
        "Bound surface charge appears on a dielectric because of:",
        "Misalignment cancellation leaving net surface dipole layers",
        ["Free electrons only", "Nuclear fusion", "Gravity"],
    ),
    q(
        "For κ = 4, the field inside the dielectric is ______ the vacuum field for same configuration:",
        "One-fourth",
        ["Four times", "Same", "Sixteen times"],
    ),
    q(
        "Permanent dipoles in dielectrics align with field giving:",
        "Orientation polarisation",
        ["No effect", "Only conduction", "Magnetic monopoles"],
    ),
]

BANK_CAPACITANCE: QuestionBank = [
    q(
        "Capacitance of an isolated conductor is defined as C =:",
        "Q / V",
        ["V / Q", "Q V", "Q² V"],
    ),
    q(
        "SI unit of capacitance is:",
        "Farad (F)",
        ["Ohm", "Henry", "Tesla"],
    ),
    q(
        "Capacitance of a parallel plate capacitor (area A, separation d, vacuum) is:",
        "ε₀ A / d",
        ["ε₀ d / A", "A d / ε₀", "ε₀ A d"],
    ),
    q(
        "Inserting a dielectric of constant κ between plates (Q constant) ______ the potential difference:",
        "Decreases by factor κ",
        ["Increases by κ", "Leaves V unchanged", "Makes V infinite"],
    ),
    q(
        "If plate area is doubled and separation halved (vacuum), capacitance becomes:",
        "Four times the original",
        ["Twice", "Half", "Unchanged"],
    ),
    q(
        "1 farad is a:",
        "Very large capacitance; practical units are μF, nF, pF",
        ["Typical value for a small ceramic cap only", "Unit of inductance", "Unit of resistance"],
    ),
    q(
        "Capacitance depends on:",
        "Geometry and medium between plates",
        ["Only on charge Q", "Only on voltage brand", "Temperature alone"],
    ),
]

BANK_CAP_COMBINATION: QuestionBank = [
    q(
        "Capacitors in parallel have equivalent capacitance:",
        "C_eq = C₁ + C₂ + …",
        ["1/C_eq = 1/C₁ + 1/C₂", "C_eq = C₁ C₂ / (C₁ + C₂) always", "Average of capacitances"],
    ),
    q(
        "Capacitors in series have:",
        "Same charge on each capacitor",
        ["Same voltage on each always", "Different charge proportional to C always", "Zero charge"],
    ),
    q(
        "For two capacitors in series: 1/C_eq =",
        "1/C₁ + 1/C₂",
        ["C₁ + C₂", "C₁ C₂", "C₁ / C₂"],
    ),
    q(
        "Capacitors in parallel have:",
        "Same potential difference across each",
        ["Same charge always", "Zero voltage", "Reciprocal capacitances add"],
    ),
    q(
        "Two identical capacitors in series give C_eq =:",
        "C / 2",
        ["2 C", "C", "C²"],
    ),
    q(
        "Two identical capacitors in parallel give C_eq =:",
        "2 C",
        ["C / 2", "C", "C²"],
    ),
    q(
        "Series combination is used when need higher:",
        "Total voltage rating (voltage divides)",
        ["Capacitance only", "Charge without limit", "Current capacity"],
    ),
]

BANK_CAP_ENERGY: QuestionBank = [
    q(
        "Energy stored in a capacitor charged to Q at voltage V is:",
        "U = ½ Q V = ½ C V² = Q² / (2C)",
        ["U = Q V", "U = C V", "U = Q / C only"],
    ),
    q(
        "Energy density in electric field of a capacitor is:",
        "u = ½ ε₀ E² (in vacuum)",
        ["u = E only", "u = ½ B²", "u = Q E"],
    ),
    q(
        "If voltage across an isolated capacitor is doubled, stored energy becomes:",
        "Four times (U ∝ V²)",
        ["Twice", "Half", "Unchanged"],
    ),
    q(
        "When a dielectric fills a charged isolated capacitor, stored energy:",
        "Decreases (work done by field on dielectric)",
        ["Increases always", "Stays same always", "Becomes infinite"],
    ),
    q(
        "A 10 μF capacitor at 100 V stores energy approximately:",
        "0.05 J",
        ["0.5 J", "5 J", "0.005 J"],
    ),
    q(
        "During charging, energy supplied by battery partly appears as:",
        "Stored field energy and some dissipation in resistance",
        ["Only heat in vacuum gap", "Only magnetic energy", "Zero work"],
    ),
    q(
        "Discharging a capacitor through a resistor converts stored energy mainly to:",
        "Heat in the resistor",
        ["Increased capacitance", "Nuclear energy", "Permanent magnetisation only"],
    ),
]

# ---------------------------------------------------------------------------
# Current Electricity (leftovers)
# ---------------------------------------------------------------------------

BANK_CELLS_EMR: QuestionBank = [
    q(
        "EMF of a cell is defined as:",
        "Work done per unit charge in moving a charge through the complete circuit including interior of cell",
        ["Terminal voltage always", "Only voltage across external resistor", "Current times resistance only"],
    ),
    q(
        "Terminal voltage V of a cell with EMF ε, internal resistance r, current I is:",
        "V = ε − I r",
        ["V = ε + I r", "V = I r only", "V = ε / I"],
    ),
    q(
        "When a cell is on open circuit (I = 0), terminal voltage equals:",
        "EMF ε",
        ["Zero", "I r", "Half of ε always"],
    ),
    q(
        "Internal resistance causes terminal voltage to be ______ EMF when current flows:",
        "Less than",
        ["Greater than", "Equal to always", "Unrelated"],
    ),
    q(
        "Cells in series add:",
        "EMFs (if aligned) and internal resistances",
        ["Only capacitances", "Only voltages in parallel sense", "Nothing"],
    ),
    q(
        "A cell of EMF 2 V and internal resistance 0.5 Ω drives 0.4 A through external load. Terminal voltage is:",
        "1.8 V",
        ["2.0 V", "1.6 V", "0.2 V"],
    ),
    q(
        "Maximum current from a cell (short circuit external R = 0) is:",
        "I_max = ε / r",
        ["Zero", "ε r", "Infinite without limit"],
    ),
]

BANK_KIRCHHOFF: QuestionBank = [
    q(
        "Kirchhoff's junction rule (KCL) is based on conservation of:",
        "Charge",
        ["Energy only", "Momentum only", "Mass"],
    ),
    q(
        "Kirchhoff's loop rule (KVL) is based on conservation of:",
        "Energy (electrostatic potential in steady DC)",
        ["Charge only", "Angular momentum", "Entropy only"],
    ),
    q(
        "At a junction, algebraic sum of currents:",
        "Is zero (sum of in = sum of out)",
        ["Is always positive", "Equals voltage", "Equals resistance"],
    ),
    q(
        "Traversing a resistor in direction of current, potential change is:",
        "− I R (drop)",
        ["+ I R always", "Zero", "I / R"],
    ),
    q(
        "Traversing a cell from negative to positive terminal inside the cell:",
        "Potential increases by ε",
        ["Decreases by ε", "Unchanged", "Drops by I r only with no rise"],
    ),
    q(
        "In a single loop with 10 V battery and 2 Ω + 3 Ω in series, current is:",
        "2 A",
        ["5 A", "0.5 A", "10 A"],
    ),
    q(
        "Number of independent loop equations needed equals:",
        "Number of independent loops in the network",
        ["Number of junctions only", "Always one", "Number of resistors squared"],
    ),
]

BANK_WHEATSTONE: QuestionBank = [
    q(
        "Wheatstone bridge is balanced when:",
        "P/Q = R/S (ratio of adjacent arm resistances equal)",
        ["P + Q = R + S", "All resistances equal only", "Current in galvanometer is maximum"],
    ),
    q(
        "In balanced Wheatstone bridge, galvanometer current is:",
        "Zero",
        ["Maximum", "Equal to supply current", "Always ½ supply"],
    ),
    q(
        "If P = 2 Ω, Q = 4 Ω, R = 3 Ω, unknown S for balance is:",
        "6 Ω",
        ["1.5 Ω", "12 Ω", "5 Ω"],
    ),
    q(
        "Wheatstone bridge is used to measure:",
        "Unknown resistance accurately",
        ["Capacitance only", "EMF without any resistor", "Frequency of AC only without modification"],
    ),
    q(
        "When bridge is not balanced, galvanometer shows:",
        "Non-zero deflection",
        ["Always full scale fixed", "Zero always", "Random thermal noise only"],
    ),
    q(
        "Meter bridge is a practical form of:",
        "Wheatstone bridge using a uniform wire",
        ["Only series circuit", "Parallel capacitors only", "AC resonant circuit only"],
    ),
    q(
        "Sensitivity of bridge increases with:",
        "Higher galvanometer sensitivity and nearer balance",
        ["Open circuiting galvanometer", "Very unbalanced arms only", "Removing power supply"],
    ),
]

# ---------------------------------------------------------------------------
# Moving Charges and Magnetism
# ---------------------------------------------------------------------------

BANK_MAGNETIC_FORCE: QuestionBank = [
    q(
        "Magnetic force on a moving charge q with velocity v in magnetic field B is:",
        "F = q (v × B)",
        ["F = q v B parallel", "F = q v / B", "Always zero"],
    ),
    q(
        "Direction of magnetic force on positive charge is given by:",
        "Right-hand rule for v × B",
        ["Left-hand rule for parallel vectors", "Opposite to v always", "Along B always"],
    ),
    q(
        "If v is parallel or antiparallel to B, magnetic force is:",
        "Zero",
        ["Maximum q v B", "Half maximum", "Infinite"],
    ),
    q(
        "Magnetic force on a charge does:",
        "No work (force perpendicular to displacement)",
        ["Always positive work", "Always negative work", "Work equal to q V"],
    ),
    q(
        "Force on current element I dl in field B is:",
        "dF = I dl × B",
        ["I dl B parallel", "B × dl / I", "Zero always"],
    ),
    q(
        "A proton moving east in a uniform upward B field experiences force toward:",
        "North (for positive charge, v × B)",
        ["South", "East", "Downward only"],
    ),
    q(
        "Magnitude of force on charge q at speed v perpendicular to B is:",
        "q v B",
        ["q v / B", "q B / v", "Zero"],
    ),
]

BANK_MOTION_MAGNETIC_FIELD: QuestionBank = [
    q(
        "A charged particle entering uniform B perpendicular to v moves in:",
        "A circle (uniform circular motion)",
        ["A straight line always", "A parabola in uniform B", "A spiral always in uniform B"],
    ),
    q(
        "Radius of circular path: r =",
        "m v / (q B)",
        ["q B / m v", "m v B", "q v / m"],
    ),
    q(
        "Cyclotron frequency ω = q B / m is independent of:",
        "Speed and radius of particle",
        ["Magnetic field B", "Charge q", "Mass m"],
    ),
    q(
        "If speed doubles, radius of circular path in same B:",
        "Doubles",
        ["Halves", "Unchanged", "Quadruples"],
    ),
    q(
        "Time period of revolution in magnetic field T =",
        "2π m / (q B)",
        ["2π q B / m", "m / q B", "q B m"],
    ),
    q(
        "Kinetic energy of particle in uniform magnetic field (speed constant):",
        "Remains constant",
        ["Increases linearly with time", "Decreases to zero always", "Doubles each revolution"],
    ),
    q(
        "Helical path occurs when velocity has components:",
        "Parallel and perpendicular to B",
        ["Only parallel to B", "Only perpendicular to B", "Zero velocity"],
    ),
]

BANK_COMBINED_EB_FIELDS: QuestionBank = [
    q(
        "In crossed uniform E and B with v = E/B perpendicular to both, net force on charge is:",
        "Zero (velocity selector condition)",
        ["Maximum q E B", "Only electric force", "Only magnetic force always"],
    ),
    q(
        "Velocity selector passes particles with speed:",
        "v = E / B",
        ["v = E B", "v = B / E squared", "Any speed"],
    ),
    q(
        "If v > E/B in velocity selector, particle deflects toward side where magnetic force exceeds electric:",
        "Direction depends on sign of charge",
        ["Always up regardless of charge", "Never deflects", "Always along E"],
    ),
    q(
        "Hall effect measures:",
        "Transverse voltage due to magnetic deflection of carriers",
        ["Gravitational mass only", "Speed of light in vacuum only", "Nuclear binding energy"],
    ),
    q(
        "In Hall effect, electric field builds until:",
        "Magnetic and electric forces on carriers balance transversely",
        ["Current becomes zero always", "B becomes zero", "Temperature is absolute zero"],
    ),
    q(
        "Mass spectrometer uses magnetic field to separate ions by:",
        "Mass-to-charge ratio (different radii for same v)",
        ["Colour only", "Nuclear spin only", "Only temperature"],
    ),
    q(
        "Total Lorentz force on charge q is:",
        "F = q (E + v × B)",
        ["F = q E only always", "F = q B only", "F = m a gravity only"],
    ),
]

BANK_BIOT_SAVART: QuestionBank = [
    q(
        "Biot–Savart law gives magnetic field due to:",
        "Steady current element",
        ["Changing electric flux only", "Static charge alone", "Sound waves"],
    ),
    q(
        "Field due to current element I dl at distance r is proportional to:",
        "I dl × r̂ / r²",
        ["I dl r", "r² / I", "1 / r only without dl"],
    ),
    q(
        "Permeability μ₀ appears in SI form of Biot–Savart as constant relating:",
        "Current and magnetic field",
        ["Charge and voltage only", "Mass and energy", "Frequency and wavelength only"],
    ),
    q(
        "Direction of field from straight wire given by:",
        "Right-hand grip rule",
        ["Left-hand rule for electric force", "Parallel to wire always", "Random"],
    ),
    q(
        "Field at centre of circular loop radius R carrying I is:",
        "μ₀ I / (2 R)",
        ["μ₀ I R / 2", "μ₀ I / R²", "Zero"],
    ),
    q(
        "If current doubles in same geometry, |B|:",
        "Doubles",
        ["Halves", "Unchanged", "Quadruples always"],
    ),
    q(
        "Biot–Savart is analogous to Coulomb's law for:",
        "Magnetic field from steady currents",
        ["Electric field from moving monopoles", "Gravity from mass elements only without field", "AC displacement current alone"],
    ),
]

BANK_LOOP_AXIS_FIELD: QuestionBank = [
    q(
        "On axis of circular loop at distance x from centre, field varies and at far points (x >> R):",
        "Behaves like magnetic dipole field",
        ["Vanishes as 1/x", "Constant everywhere", "Like monopole 1/x² only"],
    ),
    q(
        "At centre of circular loop of N turns, field is:",
        "N times single-turn centre field",
        ["Same as single turn always", "1/N of single turn", "Zero for multiple turns"],
    ),
    q(
        "Axis field of loop carrying clockwise current when viewed along axis:",
        "Points opposite to right-hand thumb direction for that current sense",
        ["Always radial outward only", "Always zero on axis", "Uniform infinite field"],
    ),
    q(
        "Two identical coaxial loops with same current direction produce on-axis field that:",
        "Adds algebraically along axis",
        ["Always cancels to zero", "Is purely electric", "Depends only on mass"],
    ),
    q(
        "Magnetic field at axial point very close to wire loop centre compared to very far away is:",
        "Larger near the loop",
        ["Smaller near the loop", "Same magnitude always", "Undefined"],
    ),
    q(
        "For loop radius 0.1 m, I = 5 A, field at centre ≈ (μ₀ = 4π×10⁻⁷):",
        "3.14×10⁻⁵ T",
        ["3.14×10⁻³ T", "Zero", "3.14 T"],
    ),
    q(
        "Axis field symmetry of single circular loop is:",
        "Revolution symmetry about loop axis",
        ["No symmetry", "Only planar mirror at rim", "Spherical only"],
    ),
]

BANK_AMPERE_LAW: QuestionBank = [
    q(
        "Ampère's circuital law relates:",
        "Line integral ∮ B·dl to enclosed current μ₀ I_enc",
        ["Surface integral of E only", "Charge density alone", "Displacement current without B"],
    ),
    q(
        "For infinite straight wire carrying I, |B| at distance r is:",
        "μ₀ I / (2π r)",
        ["μ₀ I / (2 r²)", "μ₀ I r", "Zero"],
    ),
    q(
        "Ampère's law is most convenient for calculating B when symmetry is:",
        "High (wire, solenoid, toroid)",
        ["Absent", "Only in vacuum with no currents", "Only for static charges"],
    ),
    q(
        "∮ B·dl around a loop enclosing no net current gives:",
        "Zero net circulation (if no displacement current contribution)",
        ["μ₀ I always", "Infinite value", "Electric flux"],
    ),
    q(
        "If current enclosed doubles, |B| at same point for wire symmetry:",
        "Doubles",
        ["Halves", "Unchanged", "Four times"],
    ),
    q(
        "Ampère's law in differential form is:",
        "∇ × B = μ₀ j (steady current, ignoring displacement term)",
        ["∇ · B = μ₀ j", "∇ × E = B", "B = μ₀ j r"],
    ),
    q(
        "Direction of B around straight wire by right-hand rule:",
        "Circles wire; thumb along current",
        ["Radial outward only", "Parallel to wire only", "Along current always"],
    ),
]

BANK_SOLENOID_TOROID: QuestionBank = [
    q(
        "Inside long ideal solenoid with n turns per unit length, B =",
        "μ₀ n I",
        ["μ₀ I / r", "Zero", "μ₀ n I / r"],
    ),
    q(
        "Field outside long solenoid (ideal infinitely long) is approximately:",
        "Zero",
        ["Same as inside", "Twice inside value", "Uniform infinite everywhere"],
    ),
    q(
        "In a toroid with N total turns and mean radius R, field inside core B ≈",
        "μ₀ N I / (2π R)",
        ["μ₀ N I R", "Zero everywhere", "μ₀ I / R²"],
    ),
    q(
        "Field inside toroid depends on:",
        "Current and number of turns per unit length of toroid path",
        ["Only external uniform E", "Only charge on plates", "Gravitational g"],
    ),
    q(
        "Solenoid produces nearly uniform B inside along:",
        "Axis of solenoid",
        ["Radial direction", "Perpendicular to axis only", "Random direction"],
    ),
    q(
        "If solenoid current reversed, B inside:",
        "Reverses direction",
        ["Unchanged", "Doubles magnitude only", "Vanishes permanently"],
    ),
    q(
        "Toroid confines field mainly:",
        "Inside the core (closed flux paths)",
        ["Outside only", "At infinity only", "In empty space uniformly"],
    ),
]

BANK_PARALLEL_CURRENT_FORCE: QuestionBank = [
    q(
        "Two parallel wires with currents in same direction:",
        "Attract each other",
        ["Repel", "No force", "Rotate only without translation"],
    ),
    q(
        "Two parallel wires with currents in opposite directions:",
        "Repel each other",
        ["Attract", "No force", "Always cancel currents"],
    ),
    q(
        "Force per unit length between parallel wires distance d, currents I₁, I₂:",
        "F/L = μ₀ I₁ I₂ / (2π d)",
        ["μ₀ d / (I₁ I₂)", "I₁ I₂ d", "Zero always"],
    ),
    q(
        "Definition of ampere (SI) uses:",
        "Force between two parallel current-carrying wires",
        ["Charge of electron alone", "Speed of light alone", "Planck constant alone"],
    ),
    q(
        "If distance between wires doubles, force per length:",
        "Halves",
        ["Doubles", "Quadruples", "Unchanged"],
    ),
    q(
        "Magnetic force between wires is basis for defining:",
        "The ampere",
        ["The candela", "The mole", "The kelvin only from wires"],
    ),
    q(
        "Each wire creates B at the other; force is:",
        "Magnetic force on current in field of other wire",
        ["Gravitational only", "Electrostatic only at steady state", "Nuclear only"],
    ),
]

BANK_TORQUE_DIPOLE: QuestionBank = [
    q(
        "Torque on magnetic dipole moment m in uniform B is:",
        "τ = m × B",
        ["τ = m B parallel", "Zero always", "τ = m / B"],
    ),
    q(
        "Potential energy of dipole in field U =",
        "− m · B",
        ["m × B", "m B always positive", "Zero"],
    ),
    q(
        "Stable equilibrium for dipole in uniform B when m is:",
        "Parallel to B (minimum U)",
        ["Antiparallel to B", "Perpendicular to B", "Zero moment"],
    ),
    q(
        "Current loop magnetic moment magnitude m =",
        "N I A (N turns, area A)",
        ["I / A", "A / I", "B A only"],
    ),
    q(
        "Maximum torque on dipole in uniform B occurs when m and B are:",
        "Perpendicular",
        ["Parallel", "Antiparallel stable", "Zero angle only"],
    ),
    q(
        "If current in loop doubles, magnetic moment:",
        "Doubles",
        ["Halves", "Unchanged", "Quadruples always"],
    ),
    q(
        "Work done rotating dipole against field increases:",
        "Potential energy of orientation",
        ["Kinetic energy of electrons in wire only without field", "Capacitance", "Inductance only"],
    ),
]

BANK_GALVANOMETER: QuestionBank = [
    q(
        "Moving coil galvanometer works on:",
        "Torque on current loop in magnetic field",
        ["Photoelectric effect", "Nuclear fission", "Capacitive charging only"],
    ),
    q(
        "Galvanometer deflection is proportional to:",
        "Current through coil",
        ["Square of resistance only", "EMF squared only", "Time only"],
    ),
    q(
        "To convert galvanometer to ammeter, connect:",
        "Low resistance shunt in parallel",
        ["High resistance in series only", "Capacitor in series", "Inductor in parallel only"],
    ),
    q(
        "To convert galvanometer to voltmeter, connect:",
        "High resistance multiplier in series",
        ["Shunt in parallel only", "Short wire across coil", "Battery in parallel only"],
    ),
    q(
        "Figure of merit of galvanometer relates:",
        "Deflection per unit current",
        ["Mass per charge", "Voltage to capacitance", "Frequency to wavelength only"],
    ),
    q(
        "Restoring torque in galvanometer is provided by:",
        "Spring or suspension fibres",
        ["Gravity only on coil", "Air drag only without spring", "Magnetic monopole"],
    ),
    q(
        "Sensitivity of galvanometer is higher when:",
        "More deflection for same current (larger k)",
        ["Coil has zero turns", "Magnetic field is zero", "Spring is infinitely stiff"],
    ),
]

# ---------------------------------------------------------------------------
# Magnetism and Matter
# ---------------------------------------------------------------------------

BANK_MAGNETISM_GAUSS: QuestionBank = [
    q(
        "Gauss's law for magnetism states that the net magnetic flux through any closed surface is:",
        "Zero",
        ["Equal to enclosed magnetic monopole charge", "Equal to enclosed current", "Infinite for every surface"],
    ),
    q(
        "Zero net magnetic flux through a closed surface implies:",
        "Magnetic monopoles do not exist (or net monopole charge is zero)",
        ["Electric field is always zero", "Current is always zero", "Magnetic field is always zero everywhere"],
    ),
    q(
        "Magnetic field lines are:",
        "Continuous closed loops (no beginning or end)",
        ["Always starting on N poles and ending in empty space forever", "Identical to electric field lines of point charges", "Undefined outside magnets"],
    ),
    q(
        "If magnetic monopoles existed, Gauss's law for magnetism would involve:",
        "A non-zero term proportional to enclosed magnetic charge",
        ["Only electric permittivity", "Only gravitational constant", "Only temperature"],
    ),
    q(
        "The SI unit of magnetic flux is the:",
        "Weber (Wb)",
        ["Tesla only without area", "Ampere", "Coulomb"],
    ),
    q(
        "Magnetic flux through a surface is:",
        "The surface integral of B · dA",
        ["Only the magnitude of B at one point", "Only electric flux", "Only current times time"],
    ),
    q(
        "A bar magnet's field lines outside go from:",
        "North pole to south pole",
        ["South to north outside", "Only in circles around the centre with no poles", "Randomly with no preferred direction"],
    ),
]

BANK_BAR_MAGNET: QuestionBank = [
    q(
        "Magnetic field lines outside a bar magnet run:",
        "From north to south externally (closed loops through interior)",
        ["From south to north externally always starting at infinity", "Only inside magnet", "Randomly without closure"],
    ),
    q(
        "Geographic north pole of Earth is near magnetic:",
        "South pole (so north-seeking pole of compass points north)",
        ["North pole", "Equator only", "No pole"],
    ),
    q(
        "Axial line field of bar magnet at large distance varies as:",
        "1/r³ (dipole field)",
        ["1/r", "1/r²", "Constant"],
    ),
    q(
        "Neutral point is where:",
        "Net magnetic field is zero due to superposition",
        ["Temperature is zero", "Magnet has no poles", "Only gravity acts"],
    ),
    q(
        "Magnetic dipole moment of bar magnet has SI unit:",
        "A·m²",
        ["Tesla", "Weber per ampere only without area", "Coulomb metre"],
    ),
    q(
        "Breaking a bar magnet produces:",
        "Two smaller dipoles (each with N and S)",
        ["Isolated north monopoles", "No poles", "Electric monopoles only"],
    ),
    q(
        "Tangent law uses:",
        "Two perpendicular fields to find resultant direction",
        ["Only electric fields", "Only gravitational fields", "Only nuclear forces"],
    ),
]

BANK_MAGNETISATION: QuestionBank = [
    q(
        "Magnetisation M is defined as:",
        "Magnetic moment per unit volume",
        ["Field per unit charge", "Flux per unit mass", "Current per unit area only without moment"],
    ),
    q(
        "Relation B = μ₀ (H + M) defines:",
        "Magnetic induction in material",
        ["Electric displacement only", "Only vacuum field", "Gravitational field"],
    ),
    q(
        "Magnetic intensity H is related to free current by:",
        "Ampère's law form with H",
        ["Coulomb's law only", "Ohm's law", "Snell's law"],
    ),
    q(
        "Susceptibility χ links M and H as M =",
        "χ H (for linear isotropic materials)",
        ["H / χ only", "χ / H squared", "Zero always"],
    ),
    q(
        "Unit of H in SI:",
        "A/m",
        ["Tesla only", "Weber", "Henry"],
    ),
    q(
        "When material magnetises, contribution to B from M is:",
        "μ₀ M added to μ₀ H",
        ["Subtracted always", "Zero in all materials", "Replaces H entirely always"],
    ),
    q(
        "Demagnetising field in sample opposes:",
        "Applied magnetisation in some geometries",
        ["Gravity", "Electric charge only", "Light speed"],
    ),
]

BANK_MAGNETIC_PROPERTIES: QuestionBank = [
    q(
        "Diamagnetic materials have susceptibility:",
        "Small and negative",
        ["Large positive", "Infinite", "Always zero exactly"],
    ),
    q(
        "Paramagnetic materials align with field and have χ:",
        "Small positive",
        ["Large negative", "Zero only", "Complex imaginary only"],
    ),
    q(
        "Ferromagnetic materials exhibit:",
        "Strong spontaneous magnetisation and hysteresis",
        ["χ slightly negative only", "No domains", "Perfect diamagnetism only"],
    ),
    q(
        "Curie temperature is:",
        "Temperature above which ferromagnet loses permanent magnetisation behaviour",
        ["Speed of sound in iron", "Nuclear boiling point", "Optical frequency of laser"],
    ),
    q(
        "Hysteresis loop area represents:",
        "Energy loss per cycle (heat)",
        ["Stored charge", "Gravitational PE only", "Zero always"],
    ),
    q(
        "Relative permeability μ_r of vacuum is:",
        "1",
        ["Zero", "Infinity", "4π"],
    ),
    q(
        "Bismuth is classic example of:",
        "Diamagnet",
        ["Ferromagnet", "Superconductor at room temperature always", "Paramagnet with χ >> 1"],
    ),
]

BANK_PERMANENT_MAGNETS: QuestionBank = [
    q(
        "Permanent magnets are made from:",
        "Hard ferromagnetic materials with high coercivity",
        ["Soft iron only", "Copper wire", "Pure aluminium"],
    ),
    q(
        "Electromagnet uses:",
        "Soft iron core and coil; magnetism when current flows",
        ["Permanent steel core only without coil", "Capacitor plates only", "No current ever"],
    ),
    q(
        "Coercivity is:",
        "Reverse field needed to reduce magnetisation to zero",
        ["Initial susceptibility only", "Speed of domain walls", "Electric resistance"],
    ),
    q(
        "Retentivity is:",
        "Residual magnetisation when H returns to zero",
        ["Maximum B always", "Temperature coefficient", "Inductance value"],
    ),
    q(
        "Soft iron is used in electromagnet cores because:",
        "High μ and low hysteresis loss",
        ["High coercivity", "Zero conductivity", "Diamagnetic χ << 0"],
    ),
    q(
        "Steel retains magnetism better than soft iron due to:",
        "Higher coercivity",
        ["Lower coercivity", "Zero retentivity", "No domains"],
    ),
    q(
        "Demagnetising can be done by:",
        "Heating above Curie point or AC field decay",
        ["Cooling to 0 K only always", "Static charge only", "Increasing coercivity only"],
    ),
]

# ---------------------------------------------------------------------------
# Electromagnetic Induction
# ---------------------------------------------------------------------------

BANK_FARADAY_HENRY: QuestionBank = [
    q(
        "Faraday's experiments showed that changing magnetic flux through a coil induces:",
        "EMF and current if circuit closed",
        ["Only static charge on coil", "Only heat without EMF", "Gravitational waves"],
    ),
    q(
        "Relative motion between magnet and coil induces current because:",
        "Magnetic flux through coil changes",
        ["Electric charge of magnet changes", "Gravity varies", "Coil resistance becomes zero"],
    ),
    q(
        "Lenz's law is observed in Faraday's experiments as opposition to:",
        "Change causing induction",
        ["Constant flux only", "Zero motion", "Open circuit always"],
    ),
    q(
        "Galvanometer deflection in Faraday's experiment depends on:",
        "Rate of change of flux",
        ["Only total flux regardless of change", "Colour of magnet", "Mass of coil only"],
    ),
    q(
        "Induced current direction reverses when:",
        "Direction of relative motion or flux change reverses",
        ["Speed is constant non-zero", "Flux is constant", "Temperature is constant"],
    ),
    q(
        "Henry's contribution includes study of:",
        "Self-induction and mutual induction",
        ["Photoelectric effect only", "Nuclear fission only", "Special relativity only"],
    ),
    q(
        "EM induction requires:",
        "Changing magnetic flux (or motional EMF in conductor cutting B)",
        ["Static uniform B only with no motion", "Zero area loop", "Only electric field without B"],
    ),
]

BANK_MAGNETIC_FLUX: QuestionBank = [
    q(
        "Magnetic flux through surface Φ_B =",
        "∫ B · dA",
        ["B / A only", "B × A vector always", "Zero always"],
    ),
    q(
        "SI unit of magnetic flux is:",
        "Weber (Wb)",
        ["Tesla", "Henry per second only without weber", "Ampere turn squared only"],
    ),
    q(
        "For uniform B perpendicular to plane area A, flux magnitude is:",
        "B A",
        ["B / A", "B A cos 90° always", "Zero always"],
    ),
    q(
        "If angle between B and area normal is θ, flux is:",
        "B A cos θ",
        ["B A sin θ only", "B + A", "Independent of θ"],
    ),
    q(
        "1 weber equals:",
        "1 tesla × 1 square metre",
        ["1 volt per second for EMF relation context", "1 joule only always", "1 coulomb per metre"],
    ),
    q(
        "Flux through closed surface in absence of magnetic monopoles:",
        "Zero (Gauss law for magnetism)",
        ["Infinite always", "Equal to enclosed electric charge", "Always B times volume"],
    ),
    q(
        "Doubling area while B and orientation fixed:",
        "Doubles flux",
        ["Halves flux", "Unchanged", "Quadruples flux always"],
    ),
]

BANK_FARADAY_LAW: QuestionBank = [
    q(
        "Faraday's law of induction: induced EMF ε =",
        "− dΦ_B / dt",
        ["Φ_B / dt without sign", "dB only", "Constant flux"],
    ),
    q(
        "Magnitude of induced EMF is proportional to:",
        "Rate of change of magnetic flux",
        ["Total flux only", "Resistance only", "Capacitance only"],
    ),
    q(
        "For N turns, induced EMF magnitude:",
        "N |dΦ/dt|",
        ["|dΦ/dt| / N", "Independent of N", "N² dΦ/dt always"],
    ),
    q(
        "If flux changes uniformly from 0 to 0.5 Wb in 0.1 s in one turn, |ε| =",
        "5 V",
        ["0.5 V", "50 V", "0.05 V"],
    ),
    q(
        "Induced EMF can exist even when:",
        "Circuit is open (no current)",
        ["Only when current flows", "Only in vacuum without B", "Only at absolute zero"],
    ),
    q(
        "Faraday's law is one of:",
        "Maxwell's equations (third/Faraday equation)",
        ["Newton's laws", "Snell's law", "Boyle's law"],
    ),
    q(
        "Increasing flux into coil induces EMF that drives current creating B:",
        "Opposing the increase (Lenz)",
        ["Adding to increase", "Perpendicular only without opposition", "Zero always"],
    ),
]

BANK_LENZ_LAW: QuestionBank = [
    q(
        "Lenz's law states induced current opposes:",
        "The change in flux that produced it",
        ["Constant flux", "All magnetic fields everywhere", "Gravity"],
    ),
    q(
        "Lenz's law is a consequence of:",
        "Conservation of energy",
        ["Conservation of charge only", "Breaking of symmetry without energy", "Nuclear force"],
    ),
    q(
        "When north pole approaches coil face, induced current makes near face:",
        "North pole (repelling approach)",
        ["South pole always attracting", "No magnetic effect", "Electric monopole"],
    ),
    q(
        "Without Lenz opposition, induced currents would:",
        "Create energy from nowhere (violating conservation)",
        ["Reduce resistance to zero always", "Stop all motion instantly always", "Have no effect"],
    ),
    q(
        "Negative sign in ε = −dΦ/dt encodes:",
        "Lenz's law direction",
        ["Coulomb repulsion", "Ohm's law", "Hooke's law"],
    ),
    q(
        "When magnet recedes from coil, induced current tends to:",
        "Attract magnet (oppose recession)",
        ["Repel magnet further faster without limit", "Do nothing", "Reverse magnetisation permanently"],
    ),
    q(
        "Lenz rule uses:",
        "Right-hand rule plus opposition to flux change",
        ["Only left-hand rule for electric force on static charge", "Snell's law", "Malus law only"],
    ),
]

BANK_MOTIONAL_EMF: QuestionBank = [
    q(
        "Motional EMF in rod length l moving speed v perpendicular to B:",
        "ε = B l v",
        ["B l / v", "v B / l", "Zero if rod moves parallel to B"],
    ),
    q(
        "Motional EMF arises due to:",
        "Magnetic force on free charges in moving conductor",
        ["Static electric field only inside rod", "Nuclear decay", "Capacitive displacement only"],
    ),
    q(
        "Induced electric field in region of changing flux is:",
        "Non-conservative (curl E ≠ 0)",
        ["Always conservative like electrostatics", "Zero always", "Only gravitational"],
    ),
    q(
        "Railway metal rod 1 m long at 10 m/s perpendicular to 0.5 T field: ε =",
        "5 V",
        ["0.5 V", "50 V", "0.05 V"],
    ),
    q(
        "If rod moves parallel to B, motional EMF:",
        "Zero",
        ["Maximum Blv", "Infinite", "Equal to EMF of battery always"],
    ),
    q(
        "Motional and transformer EMF both contribute to:",
        "Total induced EMF in circuit",
        ["Only static charge separation without B", "Only nuclear energy", "Only optical path difference"],
    ),
    q(
        "Charges accumulate on rod ends until:",
        "Electric field balances magnetic force on carriers",
        ["Temperature is infinite", "Rod melts always", "B becomes zero"],
    ),
]

BANK_EDDY_CURRENTS: QuestionBank = [
    q(
        "Eddy currents are:",
        "Circulating induced currents in bulk conductors",
        ["Only in insulators", "Only in vacuum", "Static charges on surface only"],
    ),
    q(
        "Eddy currents produce:",
        "Joule heating and magnetic damping",
        ["Only cooling", "Only light emission always", "No magnetic effects"],
    ),
    q(
        "Laminations in transformer core reduce:",
        "Eddy current losses",
        ["Hysteresis only completely", "Magnetic flux", "Induced EMF to zero always"],
    ),
    q(
        "Magnetic braking in trains uses:",
        "Eddy currents opposing motion",
        ["Static friction only", "Photoelectric effect", "Nuclear recoil"],
    ),
    q(
        "Induction furnace uses eddy currents to:",
        "Heat metal by I²R losses",
        ["Cool metal", "Create permanent magnetism only", "Measure wavelength"],
    ),
    q(
        "Thin slits or coated laminations increase:",
        "Electrical resistance to eddy paths",
        ["Magnetic monopole density", "Speed of sound in core", "Nuclear cross section"],
    ),
    q(
        "Eddy current damping in galvanometer helps:",
        "Quick settling of coil",
        ["Infinite oscillation", "Zero deflection always", "Increase overshoot without limit"],
    ),
]

BANK_INDUCTANCE: QuestionBank = [
    q(
        "Self-inductance L defined by ε =",
        "− L dI/dt",
        ["L I only", "dI/dt / L", "L / dI/dt"],
    ),
    q(
        "SI unit of inductance is:",
        "Henry (H)",
        ["Farad", "Weber per tesla only without henry name", "Ohm second only as alias confusion"],
    ),
    q(
        "Energy stored in inductor U =",
        "½ L I²",
        ["L I", "I² / L", "L² I"],
    ),
    q(
        "For solenoid L ∝:",
        "n² A (turns density squared times area)",
        ["1/n", "Only length without turns", "Zero if current flows"],
    ),
    q(
        "Mutual inductance M relates flux in one coil to current in:",
        "Other coil",
        ["Same coil only always", "Vacuum only", "Capacitor plate"],
    ),
    q(
        "Two coils on same core have M:",
        "Positive when flux links both (sign depends on winding sense)",
        ["Always zero", "Always negative only without meaning", "Equal to capacitance"],
    ),
    q(
        "1 H inductance with dI/dt = 2 A/s gives induced EMF magnitude:",
        "2 V",
        ["0.5 V", "4 V", "1 V"],
    ),
]

BANK_AC_GENERATOR: QuestionBank = [
    q(
        "AC generator converts:",
        "Mechanical rotation to alternating EMF",
        ["DC battery to AC without motion", "Heat to static charge only", "Light to mass"],
    ),
    q(
        "EMF in rotating coil in uniform B varies as:",
        "sin ωt (sinusoidal for uniform rotation)",
        ["Constant DC always", "Exponential decay only", "Step function only"],
    ),
    q(
        "Maximum EMF ε₀ =",
        "N B A ω",
        ["N B / A ω", "B A only without ω", "ω / N B A"],
    ),
    q(
        "Slip rings in AC generator allow:",
        "Continuous rotation while maintaining contact",
        ["Split ring commutation for DC only", "Zero output always", "Only static connection"],
    ),
    q(
        "Frequency of output f =",
        "ω / (2π) = rotational frequency × poles factor for sync machines simplified single coil: rotations per second",
        ["A ω only", "B / N", "Independent of rotation"],
    ),
    q(
        "Increasing number of turns N in coil:",
        "Increases peak EMF proportionally",
        ["Decreases EMF", "No effect on EMF", "Removes AC nature"],
    ),
    q(
        "Brush and slip ring assembly connects:",
        "Rotating coil to external circuit",
        ["Only stator to ground without motion", "Capacitor plates only", "Nuclear fuel rods"],
    ),
]

# ---------------------------------------------------------------------------
# Alternating Current
# ---------------------------------------------------------------------------

BANK_AC_RESISTOR: QuestionBank = [
    q(
        "For v = V₀ sin ωt across resistor, current is:",
        "In phase with voltage",
        ["π/2 ahead", "π/2 behind", "Opposite phase always"],
    ),
    q(
        "RMS value of sinusoidal current I_rms =",
        "I₀ / √2",
        ["I₀", "I₀ √2", "2 I₀"],
    ),
    q(
        "Average power in pure resistor over cycle for v, i sinusoidal in phase:",
        "V_rms I_rms",
        ["Zero", "V₀ I₀", "V_rms I₀ only without rms current"],
    ),
    q(
        "If peak voltage is 311 V, RMS voltage ≈",
        "220 V",
        ["311 V", "155 V", "440 V"],
    ),
    q(
        "Phasor for resistor: voltage and current phasors are:",
        "Collinear (same direction)",
        ["Perpendicular", "Opposite always", "Unrelated"],
    ),
    q(
        "Ohm's law in AC for resistor:",
        "V_rms = I_rms R",
        ["V₀ = I_rms R only always wrong mix", "V = I R with DC peak only without care", "I = V C"],
    ),
    q(
        "Heating effect uses:",
        "RMS current (Joule heat ∝ I_rms² R)",
        ["Peak current squared only as average", "Instantaneous only averaged wrong", "Zero for AC"],
    ),
]

BANK_AC_PHASORS: QuestionBank = [
    q(
        "Phasor represents AC quantity as:",
        "Rotating vector whose projection gives instantaneous value",
        ["Static scalar only", "DC offset only", "Random noise"],
    ),
    q(
        "Phasor length usually represents:",
        "Peak or RMS magnitude (convention must be consistent)",
        ["Phase only", "Frequency numerically always", "Resistance value"],
    ),
    q(
        "Phase difference φ between two phasors gives:",
        "Relative timing of zero crossings / peaks",
        ["Sum of amplitudes always", "Product of frequencies", "DC component only"],
    ),
    q(
        "Adding two AC voltages of same frequency uses:",
        "Phasor addition",
        ["Scalar addition of peaks always valid without phase", "Only multiplication", "Division of frequencies"],
    ),
    q(
        "Angular frequency in phasor rotation ω =",
        "2π f",
        ["f / 2π", "1 / T squared", "V / I"],
    ),
    q(
        "If current phasor lags voltage phasor by 90°, element is likely:",
        "Inductor (pure)",
        ["Resistor", "Capacitor (pure leads)", "Battery DC"],
    ),
    q(
        "Phasor diagram for LCR series helps find:",
        "Resultant voltage and impedance angle",
        ["Nuclear decay rate", "Gravitational mass", "Only DC resistance without reactance"],
    ),
]

BANK_AC_INDUCTOR: QuestionBank = [
    q(
        "Inductive reactance X_L =",
        "ω L",
        ["L / ω", "1 / ω L", "ω / L"],
    ),
    q(
        "In pure inductor, current ______ voltage by π/2:",
        "Lags",
        ["Leads", "Is in phase", "Is opposite"],
    ),
    q(
        "If frequency doubles, X_L:",
        "Doubles",
        ["Halves", "Unchanged", "Quadruples"],
    ),
    q(
        "Peak voltage V₀ across inductor with peak current I₀:",
        "V₀ = I₀ X_L",
        ["V₀ = I₀ / X_L", "V₀ = I₀ L only without ω", "V₀ = 0 always"],
    ),
    q(
        "Average power consumed by pure inductor over full cycle:",
        "Zero",
        ["V_rms I_rms", "Maximum always", "Negative always"],
    ),
    q(
        "Unit of X_L is:",
        "Ohm (Ω)",
        ["Henry only", "Farad", "Weber"],
    ),
    q(
        "L = 0.1 H at 50 Hz: X_L ≈",
        "31.4 Ω",
        ["3.14 Ω", "314 Ω", "0.314 Ω"],
    ),
]

BANK_AC_CAPACITOR: QuestionBank = [
    q(
        "Capacitive reactance X_C =",
        "1 / (ω C)",
        ["ω C", "C / ω", "1 / C only"],
    ),
    q(
        "In pure capacitor, current ______ voltage by π/2:",
        "Leads",
        ["Lags", "Is in phase", "Is zero always"],
    ),
    q(
        "If frequency doubles, X_C:",
        "Halves",
        ["Doubles", "Unchanged", "Quadruples"],
    ),
    q(
        "Peak current through capacitor I₀ with peak voltage V₀:",
        "I₀ = V₀ / X_C",
        ["I₀ = V₀ X_C", "I₀ = V₀ C ω squared", "Zero"],
    ),
    q(
        "Average power in pure capacitor:",
        "Zero",
        ["Maximum heat always", "V_rms I_rms always positive", "Only negative"],
    ),
    q(
        "C = 100 μF at 50 Hz: X_C ≈",
        "32 Ω",
        ["320 Ω", "3.2 Ω", "3200 Ω"],
    ),
    q(
        "Capacitor blocks:",
        "DC steady current (open circuit at DC)",
        ["All AC always", "All frequencies equally without reactance change", "Only radio waves"],
    ),
]

BANK_AC_LCR: QuestionBank = [
    q(
        "Impedance of series LCR: Z =",
        "√(R² + (X_L − X_C)²)",
        ["R + L + C", "X_L X_C only", "1 / R"],
    ),
    q(
        "At resonance X_L = X_C, impedance equals:",
        "R (minimum)",
        ["Zero always", "Infinity always", "X_L + X_C"],
    ),
    q(
        "Resonant angular frequency ω₀ =",
        "1 / √(L C)",
        ["√(L C)", "L C", "1 / L C"],
    ),
    q(
        "Phase of current relative to voltage in series LCR:",
        "tan φ = (X_L − X_C) / R",
        ["φ = 0 always", "φ = 90° always", "Undefined always"],
    ),
    q(
        "Below resonance (X_C > X_L), circuit is:",
        "Capacitive (current leads voltage)",
        ["Inductive", "Purely resistive", "Short circuit always"],
    ),
    q(
        "Quality factor Q measures:",
        "Sharpness of resonance (energy storage vs dissipation)",
        ["Only DC resistance", "Only capacitance without L", "Speed of light"],
    ),
    q(
        "R = 10 Ω, X_L = 30 Ω, X_C = 10 Ω: |Z| =",
        "18.3 Ω approx (√(100 + 400))",
        ["50 Ω", "10 Ω", "30 Ω"],
    ),
]

BANK_AC_POWER: QuestionBank = [
    q(
        "Instantaneous power p = v i for AC. Average power P =",
        "V_rms I_rms cos φ",
        ["V₀ I₀ always", "Zero always for any AC", "V_rms I_rms without cos φ always"],
    ),
    q(
        "Power factor cos φ is:",
        "Ratio of real power to apparent power",
        ["X_L / X_C", "Peak over RMS only", "Frequency ratio"],
    ),
    q(
        "Pure inductor or capacitor alone has power factor:",
        "Zero (no average power)",
        ["One", "Infinite", "Negative only always"],
    ),
    q(
        "Apparent power S =",
        "V_rms I_rms",
        ["P cos φ only", "Zero always", "I² R only without voltage"],
    ),
    q(
        "Choke coil (high L, low R) limits:",
        "AC current while allowing small DC if any",
        ["Only DC always blocks AC passes fully", "Only voltage DC component to zero always", "Frequency to increase without limit"],
    ),
    q(
        "Wattless current refers to:",
        "Reactive component (90° out of phase) carrying no average power",
        ["DC component only", "Resistive current only", "Zero current"],
    ),
    q(
        "Improving power factor means:",
        "Increasing cos φ toward 1 (reduce reactive fraction)",
        ["Decreasing real power only", "Adding pure inductance only", "Removing all load"],
    ),
]

BANK_LC_OSCILLATIONS: QuestionBank = [
    q(
        "LC circuit oscillation frequency f =",
        "1 / (2π √(L C))",
        ["2π √(L C)", "1 / L C", "√(L / C) only"],
    ),
    q(
        "Energy in LC oscillation transfers between:",
        "Electric field of C and magnetic field of L",
        ["Only heat in R always if ideal no R", "Nuclear binding", "Gravitational PE only"],
    ),
    q(
        "At maximum charge on capacitor, current in ideal LC is:",
        "Zero",
        ["Maximum", "Negative infinity", "Constant DC value"],
    ),
    q(
        "Total energy in ideal LC U =",
        "½ Q₀² / C = ½ L I₀²",
        ["Q₀ C", "L I only", "Zero always"],
    ),
    q(
        "If L quadruples, frequency:",
        "Halves",
        ["Doubles", "Quadruples", "Unchanged"],
    ),
    q(
        "LC oscillations are analogous to:",
        "Mechanical spring-mass oscillations",
        ["Static equilibrium only", "Random walk", "Nuclear decay only"],
    ),
    q(
        "Damping in real LC with R causes:",
        "Amplitude decay (damped oscillations)",
        ["Frequency becomes zero instantly", "Infinite amplitude", "Permanent DC without source"],
    ),
]

BANK_TRANSFORMERS: QuestionBank = [
    q(
        "Ideal transformer equation:",
        "V_p / V_s = N_p / N_s = I_s / I_p",
        ["V_p = V_s always", "N_p = N_s I_p", "Power doubles always"],
    ),
    q(
        "Step-up transformer has:",
        "More secondary turns than primary",
        ["Fewer secondary turns", "Equal turns always", "Zero primary turns"],
    ),
    q(
        "Transformer works on:",
        "Mutual induction (AC only for continuous flux change)",
        ["Steady DC without ripple", "Static charge only", "Gravity"],
    ),
    q(
        "Efficiency of real transformer reduced by:",
        "Copper losses, iron losses, flux leakage",
        ["Only colour of core paint", "Only primary voltage being AC", "Using laminations improves not reduces"],
    ),
    q(
        "If turns ratio 1:10, primary 220 V RMS, secondary RMS ≈",
        "2200 V (ideal)",
        ["22 V", "220 V", "22000 V"],
    ),
    q(
        "Core material for transformer is usually:",
        "Soft iron / silicon steel laminations",
        ["Copper wire bulk only without coil", "Air gap only always", "Permanent magnet steel only"],
    ),
    q(
        "Power in ideal transformer:",
        "Input power equals output power (neglecting losses)",
        ["Output always greater without input", "Zero output always", "Only reactive never real"],
    ),
]

# ---------------------------------------------------------------------------
# Electromagnetic Waves
# ---------------------------------------------------------------------------

BANK_DISPLACEMENT_CURRENT: QuestionBank = [
    q(
        "Displacement current density is:",
        "ε₀ dE/dt",
        ["μ₀ dB/dt only", "Conductivity × E only always named displacement", "Zero always"],
    ),
    q(
        "Maxwell added displacement current to Ampère's law because:",
        "Continuity of current in capacitive / changing E regions",
        ["Magnetic monopoles exist", "Charge is not conserved", "Gravity varies"],
    ),
    q(
        "In charging capacitor gap, displacement current:",
        "Equals conduction current in wires (continuity)",
        ["Is zero always", "Is infinite", "Opposite to conduction always without matching"],
    ),
    q(
        "Displacement current produces:",
        "Magnetic field like conduction current",
        ["Only electric field without B", "Only heat", "Gravitational waves"],
    ),
    q(
        "Ampère–Maxwell law: ∮ B·dl = μ₀ (I_conduction + ε₀ dΦ_E/dt)",
        "Includes displacement term ε₀ dΦ_E/dt",
        ["Ignores changing E", "Only static fields", "Uses only H without B"],
    ),
    q(
        "Changing electric flux through surface implies:",
        "Non-zero displacement current contribution",
        ["Zero magnetic effects always", "Only static Coulomb law", "No field anywhere"],
    ),
    q(
        "Displacement current resolves paradox of:",
        "Capacitor gap in Ampère's law for steady conduction current alone",
        ["Ohm's law in resistor", "Snell's law", "Boyle's law"],
    ),
]

BANK_MAXWELL_EQUATIONS: QuestionBank = [
    q(
        "Gauss law for electricity: ∇·E =",
        "ρ / ε₀",
        ["Zero always", "μ₀ J", "B / ε₀"],
    ),
    q(
        "Gauss law for magnetism: ∇·B =",
        "0 (no magnetic monopoles)",
        ["ρ / ε₀", "μ₀ I", "Infinite always"],
    ),
    q(
        "Faraday law: ∇×E =",
        "− ∂B/∂t",
        ["μ₀ J", "Zero", "∂E/∂t only"],
    ),
    q(
        "Ampère–Maxwell law: ∇×B =",
        "μ₀ J + μ₀ ε₀ ∂E/∂t",
        ["μ₀ J only without displacement", "E / c only", "Zero"],
    ),
    q(
        "Maxwell's equations predict:",
        "Electromagnetic waves propagating at c",
        ["Only static fields forever", "Only sound waves", "Only nuclear radiation"],
    ),
    q(
        "Symmetry between changing B inducing E and changing E inducing B leads to:",
        "Self-sustaining EM wave",
        ["Static equilibrium only", "Only DC circuits", "Only gravity waves"],
    ),
    q(
        "In vacuum with no charges/currents, wave equation follows from:",
        "Coupled Maxwell equations for E and B",
        ["Ohm's law alone", "Coulomb law alone", "Newton's third law alone"],
    ),
]

BANK_EM_WAVES: QuestionBank = [
    q(
        "In EM wave, E and B are:",
        "Mutually perpendicular and perpendicular to propagation direction",
        ["Parallel to each other and direction", "Random", "Only E exists"],
    ),
    q(
        "Speed of EM wave in vacuum c =",
        "1 / √(μ₀ ε₀)",
        ["μ₀ ε₀", "√(μ₀ / ε₀) only without inverse", "Only 3×10⁸ without relation"],
    ),
    q(
        "Relation between E₀ and B₀ in plane wave:",
        "E₀ = c B₀",
        ["E₀ = B₀", "E₀ = B₀ / c", "E₀ B₀ = c"],
    ),
    q(
        "EM wave carries:",
        "Energy and momentum",
        ["Only charge", "Only mass rest energy without momentum", "Only magnetic monopoles"],
    ),
    q(
        "Average energy density in EM wave u ∝:",
        "E₀² and B₀²",
        ["Only B₀", "Only frequency squared always alone", "Zero in vacuum"],
    ),
    q(
        "Radiation pressure from EM wave indicates:",
        "Momentum transfer to surfaces",
        ["Only heat without momentum", "Static charge build-up only", "Nuclear fusion"],
    ),
    q(
        "Polarisation of EM wave refers to:",
        "Direction of oscillating E field",
        ["Magnetic monopole direction", "Sound wave phase", "Nuclear spin only"],
    ),
]

BANK_EM_SPECTRUM: QuestionBank = [
    q(
        "Order of EM spectrum by increasing frequency:",
        "Radio, microwave, IR, visible, UV, X-ray, gamma",
        ["Gamma first then radio", "Only visible exists", "Random order"],
    ),
    q(
        "All EM waves in vacuum travel with:",
        "Same speed c",
        ["Speed proportional to frequency only in vacuum", "Zero speed for radio", "Speed depends on amplitude only"],
    ),
    q(
        "Visible light wavelength range approximately:",
        "400 nm to 700 nm",
        ["1 m to 10 m", "Only 550 nm single value", "Less than 1 pm always"],
    ),
    q(
        "X-rays produced when:",
        "High-energy electrons decelerate or inner shell transitions",
        ["Only chemical reactions in beaker always", "Only sound waves", "Only DC resistor heating alone"],
    ),
    q(
        "Microwave ovens use frequency near:",
        "2.45 GHz (water absorption band)",
        ["50 Hz mains only", "Visible green only", "Gamma rays"],
    ),
    q(
        "Relation c = f λ applies to:",
        "All electromagnetic waves",
        ["Only sound in air", "Only mechanical waves", "Only DC"],
    ),
    q(
        "Infrared radiation is strongly associated with:",
        "Molecular vibrations and thermal emission",
        ["Nuclear fission only", "Only cosmic ray primary only without thermal link", "Static magnetic fields only"],
    ),
]

# ---------------------------------------------------------------------------
# Ray Optics and Optical Instruments
# ---------------------------------------------------------------------------

BANK_SPHERICAL_MIRRORS: QuestionBank = [
    q(
        "Mirror formula:",
        "1/f = 1/v + 1/u",
        ["f = u v", "f = u + v", "1/f = u v"],
    ),
    q(
        "Sign convention (Cartesian): object distance u for real object is:",
        "Negative (often in CBSE convention)",
        ["Positive always", "Zero", "Complex"],
    ),
    q(
        "Focal length of concave mirror is taken as:",
        "Negative in Cartesian sign convention used in NCERT",
        ["Positive always", "Zero", "Infinite always"],
    ),
    q(
        "Magnification m =",
        "− v / u = h_i / h_o",
        ["u / v only without sign", "f / u squared", "Always +1"],
    ),
    q(
        "Concave mirror forms real inverted image when object is:",
        "Beyond F (|u| > |f|) for real object cases",
        ["Always virtual only", "At any position always virtual", "Only at infinity virtual always"],
    ),
    q(
        "Radius of curvature R and focal length f:",
        "f = R / 2",
        ["f = 2 R", "f = R²", "f = 1 / R"],
    ),
    q(
        "Object at centre of curvature of concave mirror: image is:",
        "At C, same size, real inverted",
        ["At infinity", "Virtual upright magnified at mirror", "At focus same size"],
    ),
]

BANK_REFRACTION: QuestionBank = [
    q(
        "Snell's law:",
        "n₁ sin θ₁ = n₂ sin θ₂",
        ["n₁ cos θ₁ = n₂ cos θ₂", "sin θ₁ = sin θ₂ always", "n₁ / n₂ = θ₁ / θ₂"],
    ),
    q(
        "Refractive index n =",
        "c / v (speed of light in vacuum over medium)",
        ["v / c", "sin θ always", "1 / wavelength only"],
    ),
    q(
        "Light bends toward normal when entering denser medium because:",
        "Speed decreases (n increases)",
        ["Speed increases", "Frequency changes drastically", "Wavelength unchanged in vacuum"],
    ),
    q(
        "Apparent depth real depth relation for normal viewing near surface:",
        "Real depth = apparent depth × n (approximately for small angles)",
        ["Apparent equals real always", "Real = apparent / n squared only always wrong", "Independent of n"],
    ),
    q(
        "If n = 1.5, speed of light in medium v =",
        "2 × 10⁸ m/s approx",
        ["3 × 10⁸ m/s", "1.5 × 10⁸ m/s", "4.5 × 10⁸ m/s"],
    ),
    q(
        "Frequency of light:",
        "Same across media (determined by source)",
        ["Changes with n directly", "Zero in glass", "Doubles in water always"],
    ),
    q(
        "Wavelength in medium λ_medium =",
        "λ_vacuum / n",
        ["λ_vacuum × n", "Unchanged from vacuum always", "n / c only"],
    ),
]

BANK_TIR: QuestionBank = [
    q(
        "Critical angle sin θ_c =",
        "n₂ / n₁ for denser to rarer (n₁ > n₂)",
        ["n₁ / n₂ inverted wrong for standard denser to rarer setup", "1 always", "Zero"],
    ),
    q(
        "Total internal reflection occurs when:",
        "Light travels denser to rarer and angle exceeds critical angle",
        ["Any refraction at flat surface", "Normal incidence always", "Rarer to denser always"],
    ),
    q(
        "For glass n=1.5 to air, critical angle ≈",
        "42°",
        ["90°", "0°", "60° exactly always"],
    ),
    q(
        "Optical fibre uses:",
        "Total internal reflection to guide light",
        ["Only diffraction", "Only polarisation without reflection", "Only absorption"],
    ),
    q(
        "During TIR, all light is:",
        "Reflected (no refracted transmitted ray)",
        ["Fully transmitted", "Fully absorbed always", "Converted to sound"],
    ),
    q(
        "Critical angle exists only when light goes from:",
        "Optically denser to rarer medium",
        ["Rarer to denser", "Same n both sides", "Vacuum to vacuum"],
    ),
    q(
        "Brightness in fibre decreases mainly due to:",
        "Absorption and scattering (not TIR itself if ideal)",
        ["TIR failure at every bend ideally", "Polarisation only", "Gravity"],
    ),
]

BANK_LENSES: QuestionBank = [
    q(
        "Lens maker's formula (thin lens in air): 1/f =",
        "(n − 1)(1/R₁ − 1/R₂)",
        ["n R₁ R₂", "(n + 1)/f", "R₁ + R₂ only"],
    ),
    q(
        "Power of lens P =",
        "1 / f (metre) in dioptre",
        ["f in cm", "n only", "R only"],
    ),
    q(
        "Convex lens converges parallel rays to:",
        "Real focus on far side",
        ["Virtual focus on same side for parallel rays", "No focus", "Centre of lens always"],
    ),
    q(
        "Two thin lenses in contact: power adds as:",
        "P = P₁ + P₂",
        ["1/P = 1/P₁ + 1/P₂ always wrong for contact thin", "P = P₁ P₂", "Zero always"],
    ),
    q(
        "Magnifying glass is:",
        "Convex lens producing virtual erect magnified image",
        ["Concave mirror only", "Plane mirror", "Prism only"],
    ),
    q(
        "Object between F and optical centre of convex lens gives:",
        "Virtual erect magnified image",
        ["Real inverted diminished", "No image", "Real at infinity always"],
    ),
    q(
        "Concave lens always produces:",
        "Virtual erect diminished image (for real object)",
        ["Real magnified image always", "Inverted real image", "Image at infinity only"],
    ),
]

BANK_PRISM: QuestionBank = [
    q(
        "Minimum deviation condition in prism:",
        "Symmetrical path (i = e, r₁ = r₂)",
        ["Grazing incidence only", "Normal incidence only always min dev", "Zero angle of prism"],
    ),
    q(
        "Refractive index from minimum deviation n =",
        "sin((A + δ_m)/2) / sin(A/2)",
        ["sin A / sin δ", "A / δ_m", "δ_m only"],
    ),
    q(
        "Dispersion in prism occurs because:",
        "n varies with wavelength",
        ["All colours same speed always", "Only reflection", "Only diffraction without refraction"],
    ),
    q(
        "Violet bends ______ than red in prism:",
        "More (greater n for violet)",
        ["Less", "Same angle always", "Not at all"],
    ),
    q(
        "Angular dispersion is:",
        "Difference in deviation for two wavelengths",
        ["Sum of angles only", "Always zero", "Only polarisation angle"],
    ),
    q(
        "Thin prism deviation δ ≈",
        "(n − 1) A for small angles",
        ["n A squared", "A / n only", "Zero always"],
    ),
    q(
        "Prism separates white light by:",
        "Different refractive indices for colours",
        ["Absorption only", "Polarisation only", "Gravity"],
    ),
]

BANK_OPTICAL_INSTRUMENTS: QuestionBank = [
    q(
        "Simple microscope magnification at near point ≈",
        "1 + D / f (D = 25 cm)",
        ["D f", "f / D only", "1 − D/f"],
    ),
    q(
        "Compound microscope uses:",
        "Two convex lenses (objective and eyepiece)",
        ["One concave lens only", "Mirror objective only always", "Prism eyepiece only"],
    ),
    q(
        "Astronomical telescope magnification for relaxed eye:",
        "− f_o / f_e (angular magnification magnitude)",
        ["f_e / f_o", "f_o + f_e", "Product f_o f_e"],
    ),
    q(
        "Normal adjustment of telescope:",
        "Final image at infinity (parallel rays out)",
        ["At near point only always", "At objective", "At retina without lens"],
    ),
    q(
        "Resolving power of microscope increases with:",
        "Higher NA (numerical aperture) and shorter wavelength",
        ["Lower aperture", "Longer wavelength only", "Removing objective"],
    ),
    q(
        "Eye's far point for normal eye is approximately:",
        "Infinity",
        ["25 cm", "1 m", "Zero"],
    ),
    q(
        "Hypermetropia corrected using:",
        "Convex lens",
        ["Concave lens", "Prism only", "No lens ever"],
    ),
]

# ---------------------------------------------------------------------------
# Wave Optics
# ---------------------------------------------------------------------------

BANK_HUYGENS: QuestionBank = [
    q(
        "Huygens' principle: every point on wavefront acts as:",
        "Source of secondary wavelets",
        ["Absorber only", "Static charge", "Magnetic monopole"],
    ),
    q(
        "New wavefront is:",
        "Envelope of secondary wavelets",
        ["Single ray only", "Random points", "Backward wave only"],
    ),
    q(
        "Huygens explains:",
        "Reflection and refraction of waves",
        ["Photoelectric effect alone", "Nuclear decay alone", "Only DC circuits"],
    ),
    q(
        "Secondary wavelets spread:",
        "In all forward directions (common formulation)",
        ["Only backward", "Only along incident ray", "Only perpendicular to E"],
    ),
    q(
        "Plane wavefront from distant source has rays:",
        "Parallel (perpendicular to front)",
        ["Converging to point always", "Random", "Circular always"],
    ),
    q(
        "Huygens construction assumes:",
        "Linear superposition of wavelets",
        ["Nonlinear only", "No interference", "Static fields only"],
    ),
    q(
        "Spherical wavefront intensity decreases with distance because:",
        "Energy spreads over larger area (I ∝ 1/r² for spherical)",
        ["Frequency decreases", "Speed increases beyond c", "Wavelength zero"],
    ),
]

BANK_HUYGENS_REFL_REFR: QuestionBank = [
    q(
        "Laws of reflection from wave theory:",
        "Angle of incidence equals angle of reflection, same plane",
        ["Snell's law reversed", "No plane requirement", "Only for particles"],
    ),
    q(
        "Refraction from Huygens shows bending due to:",
        "Change in speed (and wavelength) in medium",
        ["Change in frequency primarily", "Gravity", "Magnetic field only"],
    ),
    q(
        "Wavelets in denser medium have:",
        "Shorter wavelength (same frequency)",
        ["Longer wavelength", "Higher speed", "Zero amplitude always"],
    ),
    q(
        "Plane wave incident on interface: reflected wavefront remains:",
        "Plane with reversed propagation component",
        ["Spherical always", "Zero", "Static"],
    ),
    q(
        "Tangential boundary condition for wavefronts gives:",
        "Snell's law in wave form",
        ["Ohm's law", "Coulomb law only", "Boyle law"],
    ),
    q(
        "Phase change on reflection from rarer to denser (EM):",
        "Possible π phase shift depending on polarization and angle (qualitative NCERT)",
        ["Never any shift", "Always destroys wave", "Doubles frequency"],
    ),
    q(
        "Huygens fails to explain:",
        "Straight-line propagation without extra assumptions / diffraction limits historically noted",
        ["Refraction completely", "Reflection completely", "Wave nature completely"],
    ),
]

BANK_COHERENCE: QuestionBank = [
    q(
        "Coherent sources have:",
        "Constant phase difference (same frequency)",
        ["Random phase relation", "Different frequencies always", "No fixed wavelength"],
    ),
    q(
        "Incoherent sources produce:",
        "Rapidly fluctuating interference pattern (averaged out)",
        ["Stable fringes always", "No light", "Only polarised light"],
    ),
    q(
        "Laser light is highly:",
        "Coherent",
        ["Incoherent always", "Only thermal broadband without coherence", "Sound only"],
    ),
    q(
        "Superposition of amplitudes (not intensities) valid for:",
        "Coherent addition before squaring for intensity",
        ["Incoherent sources always first add intensities wrongly for step", "Static fields only", "DC only"],
    ),
    q(
        "Two independent bulbs are:",
        "Incoherent (no stable fringes)",
        ["Perfectly coherent", "Monochromatic guaranteed", "Single photon source"],
    ),
    q(
        "Temporal coherence relates to:",
        "Monochromaticity / phase stability over time",
        ["Only polarisation", "Only amplitude", "Mass of photon"],
    ),
    q(
        "Spatial coherence relates to:",
        "Phase correlation across wavefront",
        ["Only colour", "Only gravity", "Nuclear spin"],
    ),
]

BANK_INTERFERENCE: QuestionBank = [
    q(
        "Young's double slit condition for bright fringe:",
        "Path difference = n λ",
        ["n λ / 2 for bright always wrong (that's dark for standard)", "(n + ½) λ for bright", "Zero only"],
    ),
    q(
        "Fringe width β =",
        "λ D / d",
        ["d D / λ", "λ d / D", "D / λ only"],
    ),
    q(
        "If slit separation d doubles, fringe width:",
        "Halves",
        ["Doubles", "Unchanged", "Quadruples"],
    ),
    q(
        "Central fringe in YDSE is:",
        "Bright (zero path difference)",
        ["Dark always", "Polarised only", "Invisible"],
    ),
    q(
        "Interference requires:",
        "Coherent overlapping waves",
        ["Only one slit", "Only incoherent sources", "Only sound not light"],
    ),
    q(
        "Path difference for dark fringe:",
        "(n + ½) λ",
        ["n λ", "2 n λ always bright", "λ / 4 only bright"],
    ),
    q(
        "Red light compared to blue gives:",
        "Wider fringes (λ larger)",
        ["Narrower fringes always", "Same width always", "No fringes for red"],
    ),
]

BANK_DIFFRACTION: QuestionBank = [
    q(
        "Diffraction is:",
        "Bending/spreading of waves around obstacles and apertures",
        ["Only reflection", "Only refraction without spreading", "Only polarisation"],
    ),
    q(
        "Single slit central maximum width compared to side maxima:",
        "Twice as wide (standard result)",
        ["Same width", "Half width", "Zero width"],
    ),
    q(
        "Condition for first minimum in single slit (angle θ):",
        "a sin θ = λ",
        ["a sin θ = λ / 2", "a sin θ = 2 λ", "sin θ = 0 only"],
    ),
    q(
        "Diffraction becomes significant when aperture size is:",
        "Comparable to wavelength",
        ["Much larger than wavelength always negligible always stated wrong", "Zero", "Infinite"],
    ),
    q(
        "Resolving power of telescope ∝",
        "D / λ (aperture over wavelength)",
        ["λ / D", "f only", "Eyepiece power only without aperture"],
    ),
    q(
        "Rayleigh criterion relates to:",
        "Minimum resolvable separation of sources",
        ["Only prism dispersion", "Only TIR", "Only Coulomb force"],
    ),
    q(
        "Diffraction pattern intensity at very large angles:",
        "Decreases for higher order maxima",
        ["Increases without limit", "Constant for all orders", "Zero at all angles"],
    ),
]

BANK_POLARISATION: QuestionBank = [
    q(
        "Polarisation proves light is:",
        "Transverse wave",
        ["Longitudinal only", "Scalar field", "Static"],
    ),
    q(
        "Malus law intensity I =",
        "I₀ cos² θ",
        ["I₀ sin θ", "I₀ cos θ", "I₀ / cos θ"],
    ),
    q(
        "Unpolarised light intensity after ideal polariser:",
        "Half of original (I₀/2)",
        ["Unchanged", "Zero", "Double"],
    ),
    q(
        "Brewster angle condition:",
        "tan θ_B = n₂ / n₁ (reflected ray perpendicular to refracted)",
        ["sin θ = 1/n always", "θ = 0", "θ = 90° always"],
    ),
    q(
        "Polaroid sheets crossed at 90° transmit:",
        "No light (ideal)",
        ["Full intensity", "Double intensity", "Only UV"],
    ),
    q(
        "Polarisation by scattering (sky blue) involves:",
        "Transverse nature — scattered light partially polarised",
        ["Only reflection from metal", "Only nuclear scattering", "Only gravitational lensing"],
    ),
    q(
        "Angle between transmission axes for half maximum intensity:",
        "45° (cos² 45° = 1/2)",
        ["0°", "90°", "60°"],
    ),
]

# ---------------------------------------------------------------------------
# Atoms (remaining topics)
# ---------------------------------------------------------------------------

BANK_RUTHERFORD: QuestionBank = [
    q(
        "Rutherford scattering showed atom has:",
        "Small dense positively charged nucleus",
        ["Uniform positive pudding", "No nucleus", "Only electrons spread uniformly with no centre"],
    ),
    q(
        "Most α-particles passed through gold foil because:",
        "Atom is mostly empty space",
        ["Strong nuclear repulsion everywhere", "Electrons block all alphas", "Foil was too thin to interact"],
    ),
    q(
        "Large angle scattering of α-particles indicates:",
        "Close encounter with massive positive nucleus",
        ["Electron collision only", "Magnetic monopole", "Gravitational focus only"],
    ),
    q(
        "In Rutherford model, electrons orbit nucleus like:",
        "Planetary model (classical)",
        ["Fixed inside nucleus", "Only outside universe", "No motion"],
    ),
    q(
        "Classical Rutherford model instability because:",
        "Accelerating charge should radiate and spiral in",
        ["Electrons are neutral", "Nucleus is negative", "No EM fields"],
    ),
    q(
        "Distance of closest approach in head-on α scattering set by:",
        "Initial kinetic energy and nuclear charge",
        ["Only foil thickness", "Only electron mass", "Wavelength of visible light only"],
    ),
    q(
        "Nuclear size estimate from scattering uses:",
        "Impact parameter and scattering angle relation",
        ["Only chemical bonding", "Only prism deviation", "Only Ohm's law"],
    ),
]

BANK_ATOMIC_SPECTRA: QuestionBank = [
    q(
        "Continuous spectrum is produced by:",
        "Hot dense solids / liquids (blackbody-like)",
        ["Single atom gas low density only line", "Cold gas only", "Only laser line"],
    ),
    q(
        "Line spectrum indicates:",
        "Discrete energy levels in atoms",
        ["Continuous energies only", "Only nuclear sizes", "Only mechanical waves in string"],
    ),
    q(
        "Emission spectrum bright lines on dark background from:",
        "Excited gas emitting specific wavelengths",
        ["Absorption in cold gas same pattern inverted conceptually", "Only reflection from mirror", "Only radio antenna DC"],
    ),
    q(
        "Absorption spectrum dark lines on continuous background when:",
        "Cooler gas absorbs same wavelengths emitted when excited",
        ["Gas is at 0 K only always", "No light passes", "Only UV without visible"],
    ),
    q(
        "Spectroscopy used to identify:",
        "Elements via unique line patterns",
        ["Only mass of planets without lines", "Only speed of sound", "Only resistor colour code"],
    ),
    q(
        "Fraunhofer lines in solar spectrum are:",
        "Absorption lines from cooler outer layers",
        ["Emission only from core directly observed same", "Diffraction artifacts only", "Polarisation only"],
    ),
    q(
        "Each element's line spectrum is:",
        "Characteristic fingerprint",
        ["Identical for all elements", "Random each time", "Only one line always"],
    ),
]

BANK_H_LINE_SPECTRA: QuestionBank = [
    q(
        "Balmer series of hydrogen lies mainly in:",
        "Visible region (n → 2 transitions)",
        ["Only infrared without other series", "Only gamma rays", "Only radio"],
    ),
    q(
        "Rydberg formula 1/λ = R (1/n₁² − 1/n₂²) with n₂ > n₁ gives:",
        "Wavelengths of spectral lines",
        ["Nuclear masses", "Only speeds without wavelengths", "Capacitance"],
    ),
    q(
        "Lyman series ends on level:",
        "n = 1 (often UV)",
        ["n = 2 always", "n = 3 only", "Continuum only without levels"],
    ),
    q(
        "First line of Balmer series (Hα) corresponds to transition:",
        "3 → 2",
        ["2 → 1", "4 → 1 only", "∞ → 3 only without naming Hα"],
    ),
    q(
        "Series limit occurs when n₂ → ∞ giving:",
        "Ionisation threshold wavelength for that series",
        ["Zero wavelength", "Infinite wavelength always", "No photons"],
    ),
    q(
        "Rydberg constant R ≈",
        "1.097 × 10⁷ m⁻¹",
        ["6.626 × 10⁻³⁴ J s", "9.1 × 10⁻³¹ kg", "3 × 10⁸ m/s"],
    ),
    q(
        "Number of possible spectral lines when electron drops from n to 1 (all steps) for n=4:",
        "6 lines (n(n−1)/2 transitions among levels down cascade counting)",
        ["1 line only", "4 lines only", "Infinite always"],
    ),
]

# ---------------------------------------------------------------------------
# Nuclei
# ---------------------------------------------------------------------------

BANK_NUCLEAR_MASS: QuestionBank = [
    q(
        "Atomic mass unit (u) defined as:",
        "1/12 mass of carbon-12 atom",
        ["Mass of proton exactly 1 without definition", "Mass of electron", "1 kg"],
    ),
    q(
        "Nucleus contains:",
        "Protons and neutrons (nucleons)",
        ["Only electrons", "Only protons always without neutrons for all", "Only photons"],
    ),
    q(
        "Isotopes have same Z different:",
        "Neutron number A − Z",
        ["Proton number", "Chemical symbol always different element", "Charge"],
    ),
    q(
        "Mass defect is:",
        "Difference between sum of nucleon masses and actual nuclear mass",
        ["Extra electron mass", "Only photon mass", "Gravitational mass only"],
    ),
    q(
        "1 u ≈",
        "931.5 MeV/c² energy equivalent",
        ["1 eV", "511 keV only electron", "Zero"],
    ),
    q(
        "In nuclear notation ᴬ_Z X, A is:",
        "Mass number (nucleons)",
        ["Atomic number", "Charge only", "Spin only"],
    ),
    q(
        "Binding energy per nucleon is highest around:",
        "Iron region (peak of curve)",
        ["Hydrogen only", "Uranium only maximum", "Zero for all"],
    ),
]

BANK_NUCLEAR_SIZE: QuestionBank = [
    q(
        "Nuclear radius R ∝",
        "A^(1/3) (R = R₀ A^(1/3))",
        ["A", "A²", "1/A"],
    ),
    q(
        "R₀ in nuclear radius formula is approximately:",
        "1.2 fm",
        ["1.2 m", "1.2 nm", "1.2 Å for nucleus always wrong order"],
    ),
    q(
        "Nuclear density is nearly:",
        "Constant for all nuclei",
        ["Zero", "Inversely proportional to A", "Same as water always"],
    ),
    q(
        "If A increases 8 times, radius increases factor:",
        "2",
        ["8", "4", "1"],
    ),
    q(
        "Electrons cannot reside inside nucleus primarily because:",
        "Uncertainty principle requires large momentum/energy for small confinement",
        ["No electric force", "Only gravity", "Only magnetic monopoles"],
    ),
    q(
        "Nuclear size measured by:",
        "Scattering experiments and hyperfine studies",
        ["Only visible microscope", "Only prism", "Only ammeter"],
    ),
    q(
        "Volume of nucleus ∝",
        "A (since R³ ∝ A)",
        ["A²", "1/A", "Independent of A"],
    ),
]

BANK_BINDING_ENERGY: QuestionBank = [
    q(
        "Mass-energy relation:",
        "E = mc²",
        ["E = mc", "E = m/c²", "E = m + c"],
    ),
    q(
        "Binding energy B =",
        "Δm c² (mass defect times c²)",
        ["m c only", "Zero always", "Only kinetic energy of electrons in shell"],
    ),
    q(
        "Higher binding energy per nucleon means nucleus is:",
        "More stable",
        ["Less stable", "Radioactive always", "Unbound always"],
    ),
    q(
        "Energy released in fusion/fission comes from:",
        "Increase in binding energy per nucleon toward iron peak",
        ["Mass increase", "Electron capture only always", "Chemical bond breaking only"],
    ),
    q(
        "If mass defect 0.1 u, energy released ≈",
        "93.15 MeV",
        ["0.1 MeV", "9315 MeV", "1 eV"],
    ),
    q(
        "Einstein's relation explains:",
        "Equivalence of mass and energy in nuclear reactions",
        ["Only photoelectric effect alone without nuclear link", "Only Snell's law", "Only Hooke's law"],
    ),
    q(
        "Total BE of nucleus increases with A but BE per nucleon:",
        "Peaks then decreases for very heavy nuclei",
        ["Monotonically zero", "Always decreases from H", "Constant 931 MeV each"],
    ),
]

BANK_NUCLEAR_FORCE: QuestionBank = [
    q(
        "Nuclear force is:",
        "Short range, strong, charge independent (approx)",
        ["Long range like gravity only", "Repulsive at all distances", "Only between electrons"],
    ),
    q(
        "Range of nuclear force ≈",
        "1–2 fm",
        ["1 m", "1 nm", "Infinite"],
    ),
    q(
        "Nuclear force saturates meaning:",
        "Each nucleon interacts with neighbours only (not all pairs at once)",
        ["Every nucleon feels all others equally at any A", "Force grows as A² always", "Zero for neutrons"],
    ),
    q(
        "Proton-proton repulsion inside nucleus due to:",
        "Coulomb force",
        ["Strong force only repulsive", "Gravity dominant", "Magnetic monopole"],
    ),
    q(
        "Neutrons help stabilise heavy nuclei by:",
        "Adding strong attraction without Coulomb repulsion",
        ["Increasing proton repulsion", "Removing strong force", "Only adding electrons"],
    ),
    q(
        "Nuclear force is spin-dependent and:",
        "Attractive in triplet state for NN (qualitative)",
        ["Always repulsive", "Independent of spin always exactly", "Only electromagnetic"],
    ),
    q(
        "Yukawa meson theory explains:",
        "Short range via finite mediator mass",
        ["Infinite range gravity", "Only chemical bonding", "Only optics"],
    ),
]

BANK_RADIOACTIVITY: QuestionBank = [
    q(
        "Radioactivity is:",
        "Spontaneous nuclear decay",
        ["Chemical reaction rate", "Electron orbital transition only always called radioactivity wrongly", "Only artificial always"],
    ),
    q(
        "α particle is:",
        "Helium-4 nucleus (2 protons, 2 neutrons)",
        ["Electron", "Proton alone always", "Photon only"],
    ),
    q(
        "β− decay converts neutron to:",
        "Proton + electron + antineutrino",
        ["Neutron only", "Alpha particle", "Only gamma"],
    ),
    q(
        "γ rays are:",
        "High energy photons from excited nucleus",
        ["Charged particles always", "Sound waves", "Only radio AM waves"],
    ),
    q(
        "Half-life T_1/2 is time for:",
        "Activity (or number) to reduce to half",
        ["Quarter always", "Full decay always in one half-life", "Infinite time"],
    ),
    q(
        "Activity A =",
        "λ N (decay constant times number)",
        ["N / λ", "λ only", "Zero always"],
    ),
    q(
        "After 3 half-lives, undecayed fraction:",
        "1/8",
        ["1/3", "1/6", "Zero always"],
    ),
]

BANK_NUCLEAR_ENERGY: QuestionBank = [
    q(
        "Nuclear fission splits:",
        "Heavy nucleus into lighter fragments + neutrons",
        ["Hydrogen only always", "Electrons from atom", "Only chemical bonds"],
    ),
    q(
        "Chain reaction in reactor requires:",
        "Critical mass and neutron moderation/control",
        ["Only water without fuel", "Zero neutrons", "Only fusion fuel"],
    ),
    q(
        "Fusion in stars fuses:",
        "Light nuclei (e.g. hydrogen to helium)",
        ["Uranium", "Lead only", "Electrons only"],
    ),
    q(
        "Moderator in reactor:",
        "Slows neutrons for increased fission cross section in thermal reactors",
        ["Speeds neutrons always", "Absorbs all fuel", "Produces control rods function wrongly alone"],
    ),
    q(
        "Control rods absorb:",
        "Neutrons to regulate reaction rate",
        ["Gamma only always", "All electricity output directly", "Protons from fuel only without neutrons"],
    ),
    q(
        "Fusion advantage includes:",
        "Abundant fuel and less long-lived waste (challenges: ignition)",
        ["No radiation ever", "Room temperature operation always", "Only uses coal"],
    ),
    q(
        "Energy in reactor ultimately converted to electricity via:",
        "Heat → steam → turbine → generator",
        ["Direct photovoltaic from gamma only always", "Only battery chemical", "Only capacitor discharge alone"],
    ),
]

# ---------------------------------------------------------------------------
# Semiconductor Electronics
# ---------------------------------------------------------------------------

BANK_SEMICON_CLASS: QuestionBank = [
    q(
        "Conductivity of metals vs semiconductors at room temperature:",
        "Metals much higher; semiconductors intermediate, increases with T",
        ["Semiconductors always higher than copper", "Insulators conduct best", "All equal"],
    ),
    q(
        "Band gap in insulator is:",
        "Large (> 3 eV typically)",
        ["Zero", "Negative always", "Exactly 0.1 eV for all insulators always"],
    ),
    q(
        "Semiconductor band gap at room temp order:",
        "~1 eV (e.g. Si 1.1 eV)",
        ["10 eV", "0 eV always", "100 eV"],
    ),
    q(
        "Valence band electrons at 0 K in pure semiconductor:",
        "Bound; conduction band empty (ideal)",
        ["All in conduction band", "No bands exist", "Only nuclear levels"],
    ),
    q(
        "Insulators fail to conduct because:",
        "Electrons cannot easily jump large band gap",
        ["No electrons exist", "Only holes in valence band without gap concept", "Only magnetic fields block"],
    ),
    q(
        "Semiconductors useful because conductivity can be:",
        "Tuned by doping and temperature",
        ["Never changed", "Only increased by cooling always without exception", "Only magnetic field without doping"],
    ),
    q(
        "Copper is:",
        "Conductor (overlapping or partially filled bands)",
        ["Intrinsic semiconductor", "Wide gap insulator", "Intrinsic insulator only"],
    ),
]

BANK_INTRINSIC_SC: QuestionBank = [
    q(
        "Intrinsic semiconductor has:",
        "Equal electron and hole concentrations n = p",
        ["n >> p always", "Only electrons", "Only holes without electrons"],
    ),
    q(
        "At higher temperature intrinsic carrier concentration:",
        "Increases",
        ["Decreases always", "Zero always", "Constant always"],
    ),
    q(
        "Pure silicon at room temperature conducts via:",
        "Thermally generated e-h pairs",
        ["Only ions in solution", "Only protons", "Only superconductivity"],
    ),
    q(
        "Product n p in intrinsic material:",
        "n_i² (mass action law)",
        ["Zero", "n_i only", "p only"],
    ),
    q(
        "Intrinsic carrier concentration n_i depends strongly on:",
        "Temperature and band gap",
        ["Only colour", "Only pressure alone without T", "Nuclear mass only"],
    ),
    q(
        "In intrinsic SC, Fermi level lies:",
        "Near middle of band gap",
        ["In conduction band always", "In valence band bottom always", "Outside crystal"],
    ),
    q(
        "Silicon intrinsic at 300 K has conductivity:",
        "Low compared to metals",
        ["Equal to silver", "Infinite", "Zero cannot ever conduct"],
    ),
]

BANK_EXTRINSIC_SC: QuestionBank = [
    q(
        "n-type doping adds:",
        "Pentavalent donor (extra electron)",
        ["Trivalent acceptor", "Only neutrons in lattice", "Only insulator atoms"],
    ),
    q(
        "p-type doping adds:",
        "Trivalent acceptor (creates holes)",
        ["Pentavalent donor only", "Noble gas", "Only metal ions"],
    ),
    q(
        "Majority carriers in n-type:",
        "Electrons",
        ["Holes", "Ions only", "Photons"],
    ),
    q(
        "In extrinsic material, n p still equals:",
        "n_i² (equilibrium product)",
        ["Zero", "n_d only", "p_a only without relation"],
    ),
    q(
        "Donor ionised gives:",
        "Positive fixed charge and free electron",
        ["Negative donor core only without electron", "Only hole in donor atom alone", "Only photon"],
    ),
    q(
        "Acceptor creates:",
        "Hole in valence band and negative fixed acceptor ion",
        ["Free electron majority always in p-type", "Only neutron", "Magnetic monopole"],
    ),
    q(
        "Doping 1 ppm dramatically changes:",
        "Carrier concentration and conductivity",
        ["Band gap by 10 eV always", "Speed of light in vacuum", "Nuclear charge Z"],
    ),
]

BANK_PN_JUNCTION: QuestionBank = [
    q(
        "p-n junction at equilibrium has:",
        "Depletion region with built-in potential",
        ["Uniform field zero everywhere", "No band bending", "Only metal wire"],
    ),
    q(
        "Forward bias reduces:",
        "Barrier width / potential (allows large current)",
        ["Depletion to zero width instantly always wrong extreme", "Always blocks current", "Only reverse current"],
    ),
    q(
        "Reverse bias widens:",
        "Depletion layer (small leakage current)",
        ["Nothing", "Always infinite current", "Removes all dopants"],
    ),
    q(
        "Diffusion current at junction due to:",
        "Carrier concentration gradient",
        ["Only magnetic field", "Only gravity", "Only nuclear force"],
    ),
    q(
        "Drift current in depletion due to:",
        "Built-in electric field on thermally generated carriers",
        ["Only diffusion forever without field", "Sound waves", "Only alpha particles"],
    ),
    q(
        "Built-in potential order for Si junction:",
        "≈ 0.7 V",
        ["10 V always", "0 V always", "100 V"],
    ),
    q(
        "Junction diode allows easy current mainly in:",
        "Forward direction",
        ["Reverse only", "Both equally without bias", "No direction dependence"],
    ),
]

BANK_SEMICON_DIODE: QuestionBank = [
    q(
        "Ideal diode equation involves:",
        "Exponential I–V relation I ∝ e^(qV/kT)",
        ["Linear Ohm only always", "Quadratic only without exp", "Zero current always"],
    ),
    q(
        "Knee voltage of Si diode ≈",
        "0.7 V forward",
        ["5 V", "0 V sharp without drop", "12 V always"],
    ),
    q(
        "Zener diode operates in breakdown for:",
        "Voltage regulation (controlled reverse breakdown)",
        ["Only forward bias always", "Only open circuit", "Only fusion"],
    ),
    q(
        "LED emits light when:",
        "Electrons recombine with holes radiatively",
        ["Only heats without photons", "Only reverse bias without special design", "Only nuclear decay"],
    ),
    q(
        "Photodiode used in:",
        "Reverse bias light detection",
        ["Only rectifier forward only without light use", "Only motor drive", "Only transformer core"],
    ),
    q(
        "Dynamic resistance r_d =",
        "dV/dI near operating point (small signal)",
        ["V × I only always", "R independent of bias", "Zero always"],
    ),
    q(
        "Half-wave rectifier uses:",
        "One diode conducting alternate half cycles",
        ["Four diodes bridge only always required", "Capacitor alone without diode", "Inductor alone"],
    ),
]

BANK_DIODE_RECTIFIER: QuestionBank = [
    q(
        "Full-wave rectifier with centre-tapped transformer needs:",
        "Two diodes",
        ["One diode only for full wave without bridge", "Zero diodes", "Five diodes"],
    ),
    q(
        "Bridge rectifier uses:",
        "Four diodes in bridge configuration",
        ["Two diodes with centre tap only option", "One diode for full wave", "Only resistor"],
    ),
    q(
        "Ripple in rectified output reduced by:",
        "Filter capacitor (smoothing)",
        ["Removing load", "Increasing ripple frequency only without filter", "Open circuit"],
    ),
    q(
        "PIV (peak inverse voltage) rating must exceed:",
        "Maximum reverse voltage across diode in circuit",
        ["Forward current only", "Zero always", "Only RMS forward"],
    ),
    q(
        "Rectifier converts:",
        "AC to pulsating DC",
        ["DC to AC without inverter", "Light to sound", "Only amplifies AC unchanged"],
    ),
    q(
        "Output frequency of full-wave rectified 50 Hz AC:",
        "100 Hz (ripple)",
        ["50 Hz unchanged", "25 Hz", "0 Hz perfect DC without ripple always wrong ideal"],
    ),
    q(
        "Smoothing capacitor placed:",
        "Parallel to load",
        ["Series only always blocks DC wrongly alone", "Inside transformer primary only", "Across input AC only without load effect alone"],
    ),
]

# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

CHAPTER_TOPIC_BANKS: dict[tuple[str, str], QuestionBank] = {}

_TOPIC_REGISTRATIONS: list[tuple[list[str], QuestionBank]] = [
    (["Electrostatic potential"], BANK_ELECTROSTATIC_POTENTIAL),
    (["Potential due to a point charge"], BANK_POTENTIAL_POINT_CHARGE),
    (["Potential due to an electric dipole"], BANK_POTENTIAL_DIPOLE),
    (["Equipotential surfaces"], BANK_EQUIPOTENTIAL),
    (["Potential energy of a system of charges"], BANK_PE_SYSTEM_CHARGES),
    (["Electrostatics of conductors"], BANK_CONDUCTORS_ES),
    (["Dielectrics and polarisation"], BANK_DIELECTRICS),
    (["Capacitors and capacitance"], BANK_CAPACITANCE),
    (["Combination of capacitors"], BANK_CAP_COMBINATION),
    (["Energy stored in a capacitor"], BANK_CAP_ENERGY),
    (["Cells emf and internal resistance"], BANK_CELLS_EMR),
    (["Kirchhoff's rules"], BANK_KIRCHHOFF),
    (["Wheatstone bridge"], BANK_WHEATSTONE),
    (["Magnetic force"], BANK_MAGNETIC_FORCE),
    (["Motion in a magnetic field"], BANK_MOTION_MAGNETIC_FIELD),
    (["Motion in combined electric and magnetic fields"], BANK_COMBINED_EB_FIELDS),
    (["Magnetic field due to a current element Biot-Savart law"], BANK_BIOT_SAVART),
    (["Magnetic field on the axis of a circular current loop"], BANK_LOOP_AXIS_FIELD),
    (["Ampere's circuital law"], BANK_AMPERE_LAW),
    (["The solenoid and the toroid"], BANK_SOLENOID_TOROID),
    (["Force between two parallel currents"], BANK_PARALLEL_CURRENT_FORCE),
    (["Torque on current loop and magnetic dipole"], BANK_TORQUE_DIPOLE),
    (["The moving coil galvanometer"], BANK_GALVANOMETER),
    (["The bar magnet"], BANK_BAR_MAGNET),
    (["Magnetism and Gauss's law", "Magnetism and Gausss law"], BANK_MAGNETISM_GAUSS),
    (["Magnetisation and magnetic intensity"], BANK_MAGNETISATION),
    (["Magnetic properties of materials"], BANK_MAGNETIC_PROPERTIES),
    (["Permanent magnets and electromagnets"], BANK_PERMANENT_MAGNETS),
    (["The experiments of Faraday and Henry"], BANK_FARADAY_HENRY),
    (["Magnetic flux"], BANK_MAGNETIC_FLUX),
    (["Faraday's law of induction"], BANK_FARADAY_LAW),
    (["Lenz's law and conservation of energy"], BANK_LENZ_LAW),
    (["Motional electromotive force"], BANK_MOTIONAL_EMF),
    (["Eddy currents"], BANK_EDDY_CURRENTS),
    (["Inductance"], BANK_INDUCTANCE),
    (["AC generator"], BANK_AC_GENERATOR),
    (["AC voltage applied to a resistor"], BANK_AC_RESISTOR),
    (["Representation of AC current and voltage by phasors"], BANK_AC_PHASORS),
    (["AC voltage applied to an inductor"], BANK_AC_INDUCTOR),
    (["AC voltage applied to a capacitor"], BANK_AC_CAPACITOR),
    (["AC voltage applied to a series LCR circuit"], BANK_AC_LCR),
    (["Power in AC circuit"], BANK_AC_POWER),
    (["LC oscillations"], BANK_LC_OSCILLATIONS),
    (["Transformers"], BANK_TRANSFORMERS),
    (["Displacement current"], BANK_DISPLACEMENT_CURRENT),
    (["Maxwell's equations from Ampere-Maxwell law"], BANK_MAXWELL_EQUATIONS),
    (["Electromagnetic waves"], BANK_EM_WAVES),
    (["Electromagnetic spectrum"], BANK_EM_SPECTRUM),
    (["Reflection of light by spherical mirrors"], BANK_SPHERICAL_MIRRORS),
    (["Refraction"], BANK_REFRACTION),
    (["Total internal reflection"], BANK_TIR),
    (["Refraction at spherical surfaces and by lenses"], BANK_LENSES),
    (["Refraction through a prism"], BANK_PRISM),
    (["Optical instruments"], BANK_OPTICAL_INSTRUMENTS),
    (["Huygens principle"], BANK_HUYGENS),
    (["Refraction and reflection of plane waves using Huygens principle"], BANK_HUYGENS_REFL_REFR),
    (["Coherent and incoherent addition of waves"], BANK_COHERENCE),
    (["Interference of light waves and Young's experiment"], BANK_INTERFERENCE),
    (["Diffraction"], BANK_DIFFRACTION),
    (["Polarisation"], BANK_POLARISATION),
    (["Alpha-particle scattering and Rutherford's nuclear model"], BANK_RUTHERFORD),
    (["Atomic spectra"], BANK_ATOMIC_SPECTRA),
    (["The line spectra of the hydrogen atom"], BANK_H_LINE_SPECTRA),
    (["Atomic masses and composition of nucleus"], BANK_NUCLEAR_MASS),
    (["Size of the nucleus"], BANK_NUCLEAR_SIZE),
    (["Mass-energy and nuclear binding energy"], BANK_BINDING_ENERGY),
    (["Nuclear force"], BANK_NUCLEAR_FORCE),
    (["Radioactivity"], BANK_RADIOACTIVITY),
    (["Nuclear energy"], BANK_NUCLEAR_ENERGY),
    (["Classification of metals semiconductors and insulators"], BANK_SEMICON_CLASS),
    (["Intrinsic semiconductor"], BANK_INTRINSIC_SC),
    (["Extrinsic semiconductor"], BANK_EXTRINSIC_SC),
    (["p-n junction"], BANK_PN_JUNCTION),
    (["Semiconductor diode"], BANK_SEMICON_DIODE),
    (["Application of junction diode as a rectifier"], BANK_DIODE_RECTIFIER),
]

_KEYWORD_ENTRIES: list[tuple[tuple[str, ...], QuestionBank]] = [
    (("electrostatic potential", "potential difference"), BANK_ELECTROSTATIC_POTENTIAL),
    (("point charge", "k q / r"), BANK_POTENTIAL_POINT_CHARGE),
    (("dipole potential", "equatorial potential"), BANK_POTENTIAL_DIPOLE),
    (("equipotential",), BANK_EQUIPOTENTIAL),
    (("potential energy of a system", "assemble charges"), BANK_PE_SYSTEM_CHARGES),
    (("electrostatics of conductors", "conductor surface"), BANK_CONDUCTORS_ES),
    (("dielectric", "polaris"), BANK_DIELECTRICS),
    (("capacitance", "parallel plate capacitor"), BANK_CAPACITANCE),
    (("combination of capacitors", "capacitors in series"), BANK_CAP_COMBINATION),
    (("energy stored in a capacitor", "1/2 c v"), BANK_CAP_ENERGY),
    (("emf", "internal resistance"), BANK_CELLS_EMR),
    (("kirchhoff", "junction rule", "loop rule"), BANK_KIRCHHOFF),
    (("wheatstone", "meter bridge"), BANK_WHEATSTONE),
    (("magnetic force", "v × b", "qvB"), BANK_MAGNETIC_FORCE),
    (("motion in a magnetic field", "cyclotron", "magnetic circular"), BANK_MOTION_MAGNETIC_FIELD),
    (("velocity selector", "crossed electric and magnetic"), BANK_COMBINED_EB_FIELDS),
    (("biot-savart", "biot savart"), BANK_BIOT_SAVART),
    (("circular current loop", "axis of loop"), BANK_LOOP_AXIS_FIELD),
    (("ampere's circuital", "ampere circuital"), BANK_AMPERE_LAW),
    (("solenoid", "toroid"), BANK_SOLENOID_TOROID),
    (("parallel currents", "force per unit length"), BANK_PARALLEL_CURRENT_FORCE),
    (("magnetic dipole", "torque on current loop"), BANK_TORQUE_DIPOLE),
    (("galvanometer", "moving coil"), BANK_GALVANOMETER),
    (("bar magnet", "magnetic dipole moment"), BANK_BAR_MAGNET),
    (("magnetisation", "magnetic intensity"), BANK_MAGNETISATION),
    (("diamagnet", "paramagnet", "ferromagnet", "hysteresis"), BANK_MAGNETIC_PROPERTIES),
    (("permanent magnet", "electromagnet", "coercivity"), BANK_PERMANENT_MAGNETS),
    (("faraday and henry", "induced emf experiment"), BANK_FARADAY_HENRY),
    (("magnetic flux", "weber"), BANK_MAGNETIC_FLUX),
    (("faraday's law", "dphi/dt"), BANK_FARADAY_LAW),
    (("lenz",), BANK_LENZ_LAW),
    (("motional emf", "blv"), BANK_MOTIONAL_EMF),
    (("eddy current",), BANK_EDDY_CURRENTS),
    (("inductance", "self-induct", "henry"), BANK_INDUCTANCE),
    (("ac generator", "slip ring"), BANK_AC_GENERATOR),
    (("ac voltage applied to a resistor", "rms"), BANK_AC_RESISTOR),
    (("phasor",), BANK_AC_PHASORS),
    (("inductive reactance", "ac inductor"), BANK_AC_INDUCTOR),
    (("capacitive reactance", "ac capacitor"), BANK_AC_CAPACITOR),
    (("lcr circuit", "impedance", "resonance"), BANK_AC_LCR),
    (("power factor", "wattless"), BANK_AC_POWER),
    (("lc oscillation",), BANK_LC_OSCILLATIONS),
    (("transformer", "turns ratio"), BANK_TRANSFORMERS),
    (("displacement current",), BANK_DISPLACEMENT_CURRENT),
    (("maxwell", "ampere-maxwell"), BANK_MAXWELL_EQUATIONS),
    (("electromagnetic wave", "E and B perpendicular"), BANK_EM_WAVES),
    (("electromagnetic spectrum",), BANK_EM_SPECTRUM),
    (("spherical mirror", "mirror formula"), BANK_SPHERICAL_MIRRORS),
    (("snell", "refractive index"), BANK_REFRACTION),
    (("total internal reflection", "critical angle"), BANK_TIR),
    (("lens maker", "power of lens"), BANK_LENSES),
    (("prism", "minimum deviation", "dispersion"), BANK_PRISM),
    (("microscope", "telescope", "optical instrument"), BANK_OPTICAL_INSTRUMENTS),
    (("huygens", "wavelet"), BANK_HUYGENS),
    (("huygens principle refraction",), BANK_HUYGENS_REFL_REFR),
    (("coherent", "incoherent"), BANK_COHERENCE),
    (("young's experiment", "double slit", "fringe width"), BANK_INTERFERENCE),
    (("diffraction", "single slit"), BANK_DIFFRACTION),
    (("polaris", "malus"), BANK_POLARISATION),
    (("rutherford", "alpha-particle scattering"), BANK_RUTHERFORD),
    (("atomic spectra", "line spectrum"), BANK_ATOMIC_SPECTRA),
    (("balmer", "rydberg", "hydrogen line"), BANK_H_LINE_SPECTRA),
    (("atomic mass unit", "mass number", "isotope"), BANK_NUCLEAR_MASS),
    (("nuclear radius", "r0 a^1/3"), BANK_NUCLEAR_SIZE),
    (("binding energy", "mass defect"), BANK_BINDING_ENERGY),
    (("nuclear force", "yukawa"), BANK_NUCLEAR_FORCE),
    (("radioactiv", "half-life"), BANK_RADIOACTIVITY),
    (("nuclear fission", "nuclear fusion", "reactor"), BANK_NUCLEAR_ENERGY),
    (("band gap", "intrinsic semiconductor", "extrinsic"), BANK_SEMICON_CLASS),
    (("intrinsic carrier", "ni"), BANK_INTRINSIC_SC),
    (("n-type", "p-type", "doping"), BANK_EXTRINSIC_SC),
    (("p-n junction", "depletion"), BANK_PN_JUNCTION),
    (("semiconductor diode", "zener", "led"), BANK_SEMICON_DIODE),
    (("rectifier", "full-wave", "bridge rectifier"), BANK_DIODE_RECTIFIER),
]


def register() -> None:
    """Register all Class 12 Physics extra banks into quiz_concepts."""
    for titles, bank in _TOPIC_REGISTRATIONS:
        register_keys(titles, bank)
    register_subject_keywords("PHY", _KEYWORD_ENTRIES)
