"""CBSE Class 11 Chemistry concept banks (subject-scoped; no Physics fallback)."""

from __future__ import annotations

from app.data.quiz_banks.common import q, register_keys, register_subject_keywords
from app.data.quiz_concepts import QuestionBank

BANK_MOLE: QuestionBank = [
    q("The SI unit of amount of substance is the:", "Mole", ["Gram", "Litre", "Equivalent"]),
    q("Avogadro's number is approximately:", "6.022 × 10^23", ["3.14 × 10^8", "1.6 × 10^-19", "9.8"]),
    q("Limiting reagent is the reactant that:", "Is completely consumed first", ["Always has the largest mass", "Is always the product", "Never affects yield"]),
    q("Molar mass of H2O is approximately:", "18 g mol^-1", ["16 g mol^-1", "2 g mol^-1", "32 g mol^-1"]),
    q("One mole of any gas at STP occupies:", "22.4 L", ["1 L", "100 mL", "44.8 mg"]),
    q("Empirical formula gives:", "Simplest whole-number atom ratio", ["Molecular geometry", "Bond angles", "pH"]),
]

BANK_ATOM: QuestionBank = [
    q("The principal quantum number n indicates:", "Main energy level / size of orbital", ["Spin only", "Shape only", "Number of bonds"]),
    q("s-orbitals are:", "Spherical", ["Dumb-bell shaped", "Double dumb-bell", "Planar rings only"]),
    q("Hund's rule states that:", "Electrons occupy degenerate orbitals singly with parallel spins first", ["All electrons pair immediately", "n must equal l", "Orbitals fill randomly"]),
    q("Heisenberg uncertainty relates:", "Position and momentum", ["Mass and volume", "Colour and charge", "pH and pKa"]),
    q("Bohr's model successfully explained:", "Hydrogen line spectrum", ["Bonding in methane", "Radioactivity of uranium", "pH of water"]),
    q("The azimuthal quantum number l for a p-orbital is:", "1", ["0", "2", "3"]),
]

BANK_BOND: QuestionBank = [
    q("VSEPR theory predicts geometry from:", "Repulsion among electron pairs around the central atom", ["Nuclear spin", "Mass number", "Colour of the compound"]),
    q("sp3 hybridisation of carbon gives:", "Tetrahedral geometry", ["Linear geometry", "Square planar always", "Octahedral"]),
    q("A hydrogen bond is:", "A strong dipole-dipole attraction involving H and F, O or N", ["A covalent sigma bond between two hydrogens only", "Ionic lattice energy", "Metallic bonding"]),
    q("Ionic bond typically forms between:", "A metal and a non-metal with large electronegativity difference", ["Two identical noble gases", "Two identical metals only as the only possibility", "Two identical non-metals only"]),
    q("According to MOT, O2 is:", "Paramagnetic", ["Always diamagnetic", "Ionic solid", "A proton donor"]),
    q("Lattice enthalpy is high when ions are:", "Small and highly charged", ["Large and singly charged only", "Neutral atoms", "Gaseous molecules with no charge"]),
]

BANK_PERIOD: QuestionBank = [
    q("Modern periodic law states that properties of elements are a periodic function of their:", "Atomic number", ["Atomic mass", "Mass number only", "Neutron number"]),
    q("Across a period, atomic radius generally:", "Decreases", ["Increases always", "Remains exactly constant", "Becomes infinite"]),
    q("Ionisation enthalpy is the energy required to:", "Remove an electron from a gaseous atom", ["Add an electron only", "Break a covalent bond in a molecule always", "Melt a metal"]),
    q("Electronegativity of fluorine is:", "The highest among the elements commonly compared", ["The lowest of all", "Zero", "Equal to helium's"]),
    q("Electron gain enthalpy is typically most negative for:", "Halogens", ["Alkali metals", "Noble gases as a rule of strongly negative values", "Lanthanoids only"]),
    q("s-block elements in group 1 are:", "Alkali metals", ["Halogens", "Noble gases", "Inner transition metals"]),
]

BANK_REDOX: QuestionBank = [
    q("Oxidation number of oxygen in most compounds is:", "-2", ["+2 always", "0 in all oxides", "+1 in water"]),
    q("In a redox reaction, the oxidising agent:", "Gets reduced", ["Always loses electrons", "Is never a reactant", "Must be oxygen gas"]),
    q("Oxidation number of S in H2SO4 is:", "+6", ["+4", "-2", "0"]),
    q("A disproportionation reaction is one in which:", "The same element is both oxidised and reduced", ["Only oxidation occurs", "No electron transfer occurs", "A catalyst is the product"]),
    q("The oxidation number of an element in its elemental form is:", "0", ["+1", "-1", "Equal to group number always"]),
    q("KMnO4 in acidic medium is a strong:", "Oxidising agent", ["Reducing agent only", "Buffer", "Indicator of pH 7 only"]),
]

BANK_ORG: QuestionBank = [
    q("Carbon is tetravalent because it has:", "Four valence electrons and forms four bonds", ["Two valence electrons", "A complete octet already", "Only ionic bonds"]),
    q("A homologous series differs by:", "A CH2 unit", ["A benzene ring always", "A metal ion", "A neutron"]),
    q("IUPAC name of CH3CH2OH is:", "Ethanol", ["Methanol", "Ethane", "Phenol"]),
    q("Structural isomers have:", "Same molecular formula but different structures", ["Different molecular formulae", "Same boiling point always", "Identical connectivity always"]),
    q("A nucleophile is a species that:", "Donates an electron pair", ["Accepts an electron pair only as electrophile", "Is always a cation", "Has no lone pair as a rule"]),
    q("Lassaigne's test is used in organic analysis for:", "Detection of N, S, and halogens", ["Measuring pH", "Finding molecular mass by Dumas of metals", "Separating azeotropes"]),
]

BANK_HYDRO: QuestionBank = [
    q("Alkanes are generally:", "Saturated hydrocarbons", ["Aromatic only", "Always acidic like phenols", "Ionic solids"]),
    q("Markovnikov addition of HBr to propene gives mainly:", "2-bromopropane", ["1-bromopropane as the only product", "Bromobenzene", "Ethene"]),
    q("Benzene undergoes typically:", "Electrophilic substitution", ["Nucleophilic substitution as the default", "Free radical addition only like alkanes", "Ionic precipitation"]),
    q("The general formula of alkenes is:", "CnH2n", ["CnH2n+2", "CnH2n-2", "CnH2n+1"]),
    q("Acetylene (ethyne) has a:", "Triple bond between carbons", ["Only single bonds", "Ionic lattice", "Metallic bond"]),
    q("Conformations of ethane include:", "Staggered and eclipsed", ["Chair and boat of benzene", "Linear and square planar carbon", "Octahedral carbon"]),
]

BANK_EQUIL: QuestionBank = [
    q("Kc is the equilibrium constant in terms of:", "Concentrations", ["Only partial pressures of solids", "pH only", "Temperature as the only variable"]),
    q("Le Chatelier's principle predicts the shift when:", "A system at equilibrium is disturbed", ["A reaction has not started", "Catalyst mass is infinite", "No products exist"]),
    q("pH of a 10^-3 M HCl solution is approximately:", "3", ["11", "7", "0"]),
    q("A buffer solution resists:", "Change in pH on small addition of acid or base", ["Change in temperature only", "Change in colour always", "Change in mass"]),
    q("The first law of thermodynamics is conservation of:", "Energy", ["Entropy always at 0 K", "Mass number", "Spin"]),
    q("Gibbs energy G =:", "H - TS", ["H + TS", "PV only", "q + w without state functions"]),
]


def register() -> None:
    register_keys(
        [
            "Nature of matter",
            "Laws of chemical combination",
            "Dalton's atomic theory",
            "Atomic and molecular masses",
            "Mole concept",
            "Percentage composition",
            "Stoichiometry and limiting reagent",
            "Reactions in solutions",
            "Mole concept and stoichiometry",
            "Matter and laws of chemical combination",
        ],
        BANK_MOLE,
    )
    register_subject_keywords(
        "CHEM",
        [
            (("mole", "avogadro", "stoichiometr", "limiting reagent", "empirical"), BANK_MOLE),
            (("quantum", "orbital", "hund", "bohr", "heisenberg", "electronic configuration"), BANK_ATOM),
            (("hybridisation", "vsepr", "hydrogen bond", "lattice enthalpy", "mot"), BANK_BOND),
            (("equilibrium", "le chatelier", "buffer", "gibbs", "kc", "ph of"), BANK_EQUIL),
        ],
    )
    register_keys(
        [
            "Discovery of electron proton and neutron",
            "Atomic models of Thomson and Rutherford",
            "Bohr's model of hydrogen atom",
            "Dual nature of matter",
            "Heisenberg uncertainty principle",
            "Quantum numbers",
            "Shapes of orbitals",
            "Electronic configuration and Hund's rule",
            "Atomic models",
            "Bohr model",
            "Quantum numbers and electronic configuration",
        ],
        BANK_ATOM,
    )
    register_keys(
        [
            "Kossel-Lewis approach",
            "Ionic bond and lattice enthalpy",
            "Bond parameters",
            "VSEPR theory",
            "Valence bond theory",
            "Hybridisation",
            "Molecular orbital theory",
            "Hydrogen bonding",
            "Ionic and covalent bonds",
            "VSEPR and hybridisation",
        ],
        BANK_BOND,
    )
    register_keys(
        [
            "Physical equilibrium",
            "Equilibrium in chemical processes",
            "Law of chemical equilibrium and Kc",
            "Le Chatelier's principle",
            "Ionic equilibrium in solution",
            "Acids bases and pH",
            "Buffer solutions and solubility product",
            "System surroundings and state functions",
            "First law of thermodynamics",
            "Gibbs energy and spontaneity",
            "Physical and chemical equilibrium",
            "Ionic equilibrium and pH",
        ],
        BANK_EQUIL,
    )
    register_keys(
        [
            "Genesis of periodic classification",
            "Modern periodic law and the long form table",
            "Electronic configuration and the periodic table",
            "Atomic radius",
            "Ionisation enthalpy",
            "Electron gain enthalpy",
            "Electronegativity",
            "Periodic trends in chemical properties",
        ],
        BANK_PERIOD,
    )
    register_keys(
        [
            "Classical idea of oxidation and reduction",
            "Redox reactions in terms of electron transfer",
            "Oxidation number",
            "Types of redox reactions",
            "Balancing redox reactions",
            "Redox reactions as the basis of titrations",
        ],
        BANK_REDOX,
    )
    register_keys(
        [
            "Tetravalence of carbon",
            "Structural representations of organic compounds",
            "Classification and homologous series",
            "Nomenclature of organic compounds",
            "Isomerism",
            "Fundamental concepts in organic reaction mechanism",
            "Methods of purification",
            "Qualitative and quantitative analysis",
        ],
        BANK_ORG,
    )
    register_keys(
        [
            "Classification of hydrocarbons",
            "Alkanes structure and conformations",
            "Preparation and reactions of alkanes",
            "Alkenes structure and isomerism",
            "Preparation and reactions of alkenes",
            "Alkynes",
            "Aromatic hydrocarbons",
            "Carcinogenicity and toxicity",
        ],
        BANK_HYDRO,
    )
    register_subject_keywords(
        "CHEM",
        [
            (("periodic", "ionisation", "electronegativ", "atomic radius"), BANK_PERIOD),
            (("redox", "oxidation number", "oxidation"), BANK_REDOX),
            (("homologous", "nomenclature", "isomerism", "tetravalen"), BANK_ORG),
            (("alkane", "alkene", "alkyne", "aromatic hydrocarbon", "benzene"), BANK_HYDRO),
        ],
    )
