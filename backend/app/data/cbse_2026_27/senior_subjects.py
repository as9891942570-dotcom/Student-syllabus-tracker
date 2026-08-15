"""Shared Class 11–12 subject blueprints (CBSE 2026–27).

Chapter titles follow current NCERT / CBSE senior secondary course structure.
Topics are concept labels for progression tracking only — not textbook text.

Sources:
- CBSE Senior School Curriculum 2026–27 (cbseacademic.nic.in/curriculum_2027.html)
- NCERT textbooks (ncert.nic.in/textbook.php)
"""

from __future__ import annotations

from app.data.cbse_2026_27.schema import SubjectSpec, chapter, subject

PHYSICS_11: SubjectSpec = subject(
    "PHY",
    "Physics",
    [
        chapter(
            "Units and Measurements",
            [
                "The international system of units",
                "Measurement of length",
                "Measurement of mass",
                "Measurement of time",
                "Accuracy precision and errors",
                "Significant figures",
                "Dimensions of physical quantities",
                "Dimensional formulae and equations",
            ],
        ),
        chapter(
            "Motion in a Straight Line",
            [
                "Position path length and displacement",
                "Average velocity and average speed",
                "Instantaneous velocity and speed",
                "Acceleration",
                "Kinematic equations for uniformly accelerated motion",
                "Relative velocity in one dimension",
            ],
        ),
        chapter(
            "Motion in a Plane",
            [
                "Scalars and vectors",
                "Multiplication of vectors by real numbers",
                "Addition and subtraction of vectors",
                "Resolution of vectors",
                "Motion in a plane with constant acceleration",
                "Projectile motion",
                "Uniform circular motion",
            ],
        ),
        chapter(
            "Laws of Motion",
            [
                "Aristotle's fallacy and the law of inertia",
                "Newton's first law of motion",
                "Newton's second law of motion",
                "Newton's third law of motion",
                "Conservation of momentum",
                "Equilibrium of a particle",
                "Common forces in mechanics",
                "Circular motion and banking of roads",
            ],
        ),
        chapter(
            "Work, Energy and Power",
            [
                "Work done by a constant force",
                "Work done by a variable force",
                "Kinetic energy",
                "Work-energy theorem",
                "Potential energy",
                "Conservation of mechanical energy",
                "Power",
                "Collisions",
            ],
        ),
        chapter(
            "System of Particles and Rotational Motion",
            [
                "Centre of mass",
                "Motion of centre of mass",
                "Linear momentum of a system of particles",
                "Vector product and torque",
                "Angular momentum",
                "Equilibrium of a rigid body",
                "Moment of inertia",
                "Kinematics and dynamics of rotational motion",
            ],
        ),
        chapter(
            "Gravitation",
            [
                "Kepler's laws",
                "Universal law of gravitation",
                "Acceleration due to gravity",
                "Gravitational potential energy",
                "Escape speed",
                "Earth satellites",
                "Energy of an orbiting satellite",
            ],
        ),
        chapter(
            "Mechanical Properties of Solids",
            [
                "Elastic behaviour of solids",
                "Stress and strain",
                "Hooke's law",
                "Stress-strain curve",
                "Elastic moduli",
                "Applications of elastic behaviour",
            ],
        ),
        chapter(
            "Mechanical Properties of Fluids",
            [
                "Pressure",
                "Pascal's law",
                "Atmospheric pressure and gauge pressure",
                "Archimedes' principle",
                "Streamline flow",
                "Bernoulli's principle",
                "Viscosity",
                "Surface tension",
            ],
        ),
        chapter(
            "Thermal Properties of Matter",
            [
                "Temperature and heat",
                "Measurement of temperature",
                "Thermal expansion",
                "Specific heat capacity",
                "Calorimetry",
                "Change of state",
                "Heat transfer",
                "Newton's law of cooling",
            ],
        ),
        chapter(
            "Thermodynamics",
            [
                "Thermal equilibrium",
                "Zeroth law of thermodynamics",
                "Heat internal energy and work",
                "First law of thermodynamics",
                "Specific heat capacity",
                "Thermodynamic processes",
                "Second law of thermodynamics",
                "Reversible and irreversible processes",
                "Carnot engine",
            ],
        ),
        chapter(
            "Kinetic Theory",
            [
                "Molecular nature of matter",
                "Behaviour of gases",
                "Kinetic theory of an ideal gas",
                "Law of equipartition of energy",
                "Specific heat capacity of gases",
                "Mean free path",
            ],
        ),
        chapter(
            "Oscillations",
            [
                "Periodic and oscillatory motions",
                "Simple harmonic motion",
                "Simple harmonic motion and uniform circular motion",
                "Velocity and acceleration in SHM",
                "Force law for SHM",
                "Energy in SHM",
                "The simple pendulum",
                "Damped and forced oscillations",
            ],
        ),
        chapter(
            "Waves",
            [
                "Transverse and longitudinal waves",
                "Displacement relation in a progressive wave",
                "Speed of a travelling wave",
                "Principle of superposition of waves",
                "Reflection of waves",
                "Beats",
                "Doppler effect",
            ],
        ),
    ],
)

PHYSICS_12: SubjectSpec = subject(
    "PHY",
    "Physics",
    [
        chapter(
            "Electric Charges and Fields",
            [
                "Electric charge",
                "Conductors and insulators",
                "Charging by induction",
                "Basic properties of electric charge",
                "Coulomb's law",
                "Forces between multiple charges",
                "Electric field",
                "Electric field lines",
                "Electric flux",
                "Electric dipole",
                "Continuous charge distribution",
                "Gauss's law",
                "Applications of Gauss's law",
            ],
        ),
        chapter(
            "Electrostatic Potential and Capacitance",
            [
                "Electrostatic potential",
                "Potential due to a point charge",
                "Potential due to an electric dipole",
                "Equipotential surfaces",
                "Potential energy of a system of charges",
                "Electrostatics of conductors",
                "Dielectrics and polarisation",
                "Capacitors and capacitance",
                "Combination of capacitors",
                "Energy stored in a capacitor",
            ],
        ),
        chapter(
            "Current Electricity",
            [
                "Electric current",
                "Electric currents in conductors",
                "Ohm's law",
                "Drift of electrons and the origin of resistivity",
                "Limitations of Ohm's law",
                "Resistivity of various materials",
                "Temperature dependence of resistivity",
                "Electrical energy and power",
                "Combination of resistors",
                "Cells emf and internal resistance",
                "Kirchhoff's rules",
                "Wheatstone bridge",
            ],
        ),
        chapter(
            "Moving Charges and Magnetism",
            [
                "Magnetic force",
                "Motion in a magnetic field",
                "Motion in combined electric and magnetic fields",
                "Magnetic field due to a current element Biot-Savart law",
                "Magnetic field on the axis of a circular current loop",
                "Ampere's circuital law",
                "The solenoid and the toroid",
                "Force between two parallel currents",
                "Torque on current loop and magnetic dipole",
                "The moving coil galvanometer",
            ],
        ),
        chapter(
            "Magnetism and Matter",
            [
                "The bar magnet",
                "Magnetism and Gauss's law",
                "Magnetisation and magnetic intensity",
                "Magnetic properties of materials",
                "Permanent magnets and electromagnets",
            ],
        ),
        chapter(
            "Electromagnetic Induction",
            [
                "The experiments of Faraday and Henry",
                "Magnetic flux",
                "Faraday's law of induction",
                "Lenz's law and conservation of energy",
                "Motional electromotive force",
                "Eddy currents",
                "Inductance",
                "AC generator",
            ],
        ),
        chapter(
            "Alternating Current",
            [
                "AC voltage applied to a resistor",
                "Representation of AC current and voltage by phasors",
                "AC voltage applied to an inductor",
                "AC voltage applied to a capacitor",
                "AC voltage applied to a series LCR circuit",
                "Power in AC circuit",
                "LC oscillations",
                "Transformers",
            ],
        ),
        chapter(
            "Electromagnetic Waves",
            [
                "Displacement current",
                "Maxwell's equations from Ampere-Maxwell law",
                "Electromagnetic waves",
                "Electromagnetic spectrum",
            ],
        ),
        chapter(
            "Ray Optics and Optical Instruments",
            [
                "Reflection of light by spherical mirrors",
                "Refraction",
                "Total internal reflection",
                "Refraction at spherical surfaces and by lenses",
                "Refraction through a prism",
                "Optical instruments",
            ],
        ),
        chapter(
            "Wave Optics",
            [
                "Huygens principle",
                "Refraction and reflection of plane waves using Huygens principle",
                "Coherent and incoherent addition of waves",
                "Interference of light waves and Young's experiment",
                "Diffraction",
                "Polarisation",
            ],
        ),
        chapter(
            "Dual Nature of Radiation and Matter",
            [
                "Electron emission",
                "Photoelectric effect",
                "Experimental study of photoelectric effect",
                "Einstein's photoelectric equation",
                "Particle nature of light",
                "Wave nature of matter",
                "Davisson and Germer experiment",
            ],
        ),
        chapter(
            "Atoms",
            [
                "Alpha-particle scattering and Rutherford's nuclear model",
                "Atomic spectra",
                "Bohr model of the hydrogen atom",
                "The line spectra of the hydrogen atom",
                "de Broglie's explanation of Bohr's second postulate",
            ],
        ),
        chapter(
            "Nuclei",
            [
                "Atomic masses and composition of nucleus",
                "Size of the nucleus",
                "Mass-energy and nuclear binding energy",
                "Nuclear force",
                "Radioactivity",
                "Nuclear energy",
            ],
        ),
        chapter(
            "Semiconductor Electronics",
            [
                "Classification of metals semiconductors and insulators",
                "Intrinsic semiconductor",
                "Extrinsic semiconductor",
                "p-n junction",
                "Semiconductor diode",
                "Application of junction diode as a rectifier",
            ],
        ),
    ],
)

CHEMISTRY_11: SubjectSpec = subject(
    "CHEM",
    "Chemistry",
    [
        chapter(
            "Some Basic Concepts of Chemistry",
            [
                "Nature of matter",
                "Laws of chemical combination",
                "Dalton's atomic theory",
                "Atomic and molecular masses",
                "Mole concept",
                "Percentage composition",
                "Stoichiometry and limiting reagent",
                "Reactions in solutions",
            ],
        ),
        chapter(
            "Structure of Atom",
            [
                "Discovery of electron proton and neutron",
                "Atomic models of Thomson and Rutherford",
                "Bohr's model of hydrogen atom",
                "Dual nature of matter",
                "Heisenberg uncertainty principle",
                "Quantum numbers",
                "Shapes of orbitals",
                "Electronic configuration and Hund's rule",
            ],
        ),
        chapter(
            "Classification of Elements and Periodicity in Properties",
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
        ),
        chapter(
            "Chemical Bonding and Molecular Structure",
            [
                "Kossel-Lewis approach",
                "Ionic bond and lattice enthalpy",
                "Bond parameters",
                "VSEPR theory",
                "Valence bond theory",
                "Hybridisation",
                "Molecular orbital theory",
                "Hydrogen bonding",
            ],
        ),
        chapter(
            "Chemical Thermodynamics",
            [
                "System surroundings and state functions",
                "First law of thermodynamics",
                "Enthalpy change",
                "Hess's law",
                "Enthalpies of formation combustion and bond enthalpy",
                "Entropy and the second law",
                "Gibbs energy and spontaneity",
                "Gibbs energy and equilibrium",
            ],
        ),
        chapter(
            "Equilibrium",
            [
                "Physical equilibrium",
                "Equilibrium in chemical processes",
                "Law of chemical equilibrium and Kc",
                "Homogeneous and heterogeneous equilibria",
                "Le Chatelier's principle",
                "Ionic equilibrium in solution",
                "Acids bases and pH",
                "Buffer solutions and solubility product",
            ],
        ),
        chapter(
            "Redox Reactions",
            [
                "Classical idea of oxidation and reduction",
                "Redox reactions in terms of electron transfer",
                "Oxidation number",
                "Types of redox reactions",
                "Balancing redox reactions",
                "Redox reactions as the basis of titrations",
            ],
        ),
        chapter(
            "Organic Chemistry — Some Basic Principles and Techniques",
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
        ),
        chapter(
            "Hydrocarbons",
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
        ),
    ],
)

CHEMISTRY_12: SubjectSpec = subject(
    "CHEM",
    "Chemistry",
    [
        chapter(
            "Solutions",
            [
                "Types of solutions",
                "Concentration terms",
                "Solubility of solids and gases",
                "Henry's law",
                "Vapour pressure of liquid solutions",
                "Raoult's law",
                "Ideal and non-ideal solutions",
                "Colligative properties",
                "Relative lowering of vapour pressure",
                "Elevation of boiling point",
                "Depression of freezing point",
                "Osmotic pressure",
                "Abnormal molar masses",
            ],
        ),
        chapter(
            "Electrochemistry",
            [
                "Electrochemical cells",
                "Galvanic cell and Daniell cell",
                "Nernst equation",
                "Gibbs energy and cell potential",
                "Electrolysis and conductance",
                "Kohlrausch's law",
                "Batteries and fuel cells",
                "Corrosion",
            ],
        ),
        chapter(
            "Chemical Kinetics",
            [
                "Rate of a reaction",
                "Factors affecting rate",
                "Integrated rate equations",
                "Half life of a reaction",
                "Arrhenius equation",
                "Collision theory",
            ],
        ),
        chapter(
            "The d- and f-Block Elements",
            [
                "Transition elements",
                "Electronic configuration of d-block",
                "Lanthanoids",
                "Actinoids",
                "Important compounds",
                "KMnO4 and K2Cr2O7",
            ],
        ),
        chapter(
            "Coordination Compounds",
            [
                "Werner's theory",
                "Ligands and coordination number",
                "Nomenclature",
                "Bonding and isomerism",
                "Valence bond theory of complexes",
                "Crystal field theory",
                "Importance of coordination compounds",
            ],
        ),
        chapter(
            "Haloalkanes and Haloarenes",
            [
                "Classification and nomenclature",
                "Nature of C–X bond",
                "Nucleophilic substitution SN1 and SN2",
                "Reactions",
                "Haloarenes",
            ],
        ),
        chapter(
            "Alcohols, Phenols and Ethers",
            [
                "Classification",
                "Preparation",
                "Properties and reactions",
                "Acidity of phenols",
                "Ethers",
            ],
        ),
        chapter(
            "Aldehydes, Ketones and Carboxylic Acids",
            [
                "Carbonyl compounds",
                "Nucleophilic addition to carbonyl group",
                "Carboxylic acids",
                "Important reactions",
            ],
        ),
        chapter(
            "Amines",
            [
                "Classification of amines",
                "Preparation",
                "Basicity of amines",
                "Diazonium salts",
            ],
        ),
        chapter(
            "Biomolecules",
            [
                "Carbohydrates",
                "Proteins",
                "Enzymes",
                "Nucleic acids and vitamins",
            ],
        ),
    ],
)

BIOLOGY_11: SubjectSpec = subject(
    "BIO",
    "Biology",
    [
        chapter("The Living World", ["What is living", "Diversity of life", "Taxonomy and systematics", "Taxonomic categories", "Taxonomical aids"]),
        chapter("Biological Classification", ["Kingdom Monera", "Kingdom Protista", "Kingdom Fungi", "Kingdom Plantae and Animalia overview", "Viruses viroids and lichens"]),
        chapter("Plant Kingdom", ["Algae", "Bryophytes", "Pteridophytes", "Gymnosperms", "Angiosperms", "Plant life cycles and alternation of generations"]),
        chapter("Animal Kingdom", ["Basis of classification", "Porifera to Ctenophora", "Platyhelminthes to Annelida", "Arthropoda Mollusca Echinodermata", "Chordates", "Vertebrate classes"]),
        chapter("Morphology of Flowering Plants", ["The root", "The stem", "The leaf", "Inflorescence", "The flower", "Fruit and seed", "Semi-technical description"]),
        chapter("Anatomy of Flowering Plants", ["The tissues", "The tissue system", "Anatomy of dicotyledonous plants", "Anatomy of monocotyledonous plants", "Secondary growth"]),
        chapter("Structural Organisation in Animals", ["Epithelial tissue", "Connective tissue", "Muscular and neural tissue", "Organ and organ system", "Frog morphology and anatomy"]),
        chapter("Cell: The Unit of Life", ["Cell theory", "Prokaryotic cells", "Eukaryotic cells", "Endomembrane system", "Mitochondria and plastids", "Cytoskeleton cilia flagella and centrioles", "Nucleus"]),
        chapter("Biomolecules", ["How to analyse chemical composition", "Primary and secondary metabolites", "Proteins", "Polysaccharides", "Nucleic acids", "Enzymes and enzyme action"]),
        chapter("Cell Cycle and Cell Division", ["Cell cycle phases", "Mitosis", "Meiosis I", "Meiosis II", "Significance of mitosis and meiosis"]),
        chapter("Photosynthesis in Higher Plants", ["Photosynthetic pigments", "Light reaction and photophosphorylation", "Calvin cycle", "C4 pathway", "Photorespiration", "Factors affecting photosynthesis"]),
        chapter("Respiration in Plants", ["Glycolysis", "Fermentation", "Aerobic respiration", "Electron transport system and oxidative phosphorylation", "Respiratory quotient"]),
        chapter("Plant Growth and Development", ["Growth rates and phases", "Differentiation and development", "Plant growth regulators", "Photoperiodism", "Vernalisation"]),
        chapter("Breathing and Exchange of Gases", ["Human respiratory system", "Mechanism of breathing", "Exchange of gases", "Transport of gases", "Regulation of respiration", "Disorders of the respiratory system"]),
        chapter("Body Fluids and Circulation", ["Blood", "Lymph", "Circulatory pathways", "Human circulatory system", "Cardiac cycle", "ECG", "Disorders of the circulatory system"]),
        chapter("Excretory Products and their Elimination", ["Human excretory system", "Urine formation", "Function of the tubules", "Regulation of kidney function", "Micturition", "Disorders of the excretory system"]),
        chapter("Locomotion and Movement", ["Types of movement", "Muscle", "Skeletal system", "Joints", "Disorders of the muscular and skeletal system"]),
        chapter("Neural Control and Coordination", ["Human neural system", "Neuron", "Synapse and nerve impulse", "Central neural system", "Reflex action and reflex arc", "Sense organs overview"]),
        chapter("Chemical Coordination and Integration", ["Human endocrine system", "Hormones of heart kidney and GI tract", "Mechanism of hormone action", "Hypothalamus and pituitary", "Thyroid adrenal pancreas gonads"]),
    ],
)

BIOLOGY_12: SubjectSpec = subject(
    "BIO",
    "Biology",
    [
        chapter(
            "Sexual Reproduction in Flowering Plants",
            [
                "Flower as the reproductive structure",
                "Stamen microsporangium and pollen grain",
                "Pistil megasporangium and embryo sac",
                "Pollination",
                "Pollen-pistil interaction",
                "Double fertilisation",
                "Endosperm embryo seed and fruit",
                "Apomixis and polyembryony",
            ],
        ),
        chapter(
            "Human Reproduction",
            [
                "Male reproductive system",
                "Female reproductive system",
                "Spermatogenesis",
                "Oogenesis",
                "Menstrual cycle",
                "Fertilisation and implantation",
                "Pregnancy and embryonic development",
                "Parturition and lactation",
            ],
        ),
        chapter(
            "Reproductive Health",
            [
                "Reproductive health problems and strategies",
                "Population explosion and birth control",
                "Medical termination of pregnancy",
                "Sexually transmitted infections",
                "Infertility",
                "Assisted reproductive technologies",
            ],
        ),
        chapter(
            "Principles of Inheritance and Variation",
            [
                "Mendel's experiments and laws",
                "Incomplete dominance and codominance",
                "Multiple alleles and blood groups",
                "Pleiotropy and polygenic inheritance",
                "Chromosomal theory of inheritance",
                "Linkage and recombination",
                "Sex determination",
                "Mutation and genetic disorders",
            ],
        ),
        chapter(
            "Molecular Basis of Inheritance",
            [
                "DNA as the genetic material",
                "Structure of DNA and RNA",
                "DNA packaging",
                "DNA replication",
                "Transcription",
                "Genetic code and translation",
                "Regulation of gene expression",
                "Human genome project and DNA fingerprinting",
            ],
        ),
        chapter(
            "Evolution",
            [
                "Origin of life",
                "Evidences of evolution",
                "Adaptive radiation",
                "Biological evolution and mechanisms",
                "Hardy-Weinberg principle",
                "Origin and evolution of man",
            ],
        ),
        chapter(
            "Human Health and Disease",
            [
                "Common infectious diseases",
                "Immunity innate and acquired",
                "Vaccination and immunisation",
                "Allergies autoimmunity and lymphoid organs",
                "AIDS and cancer",
                "Drugs and alcohol abuse",
            ],
        ),
        chapter(
            "Microbes in Human Welfare",
            [
                "Microbes in household products",
                "Microbes in industrial products",
                "Microbes in sewage treatment",
                "Microbes in biogas production",
                "Microbes as biocontrol agents",
                "Microbes as biofertilisers",
            ],
        ),
        chapter(
            "Biotechnology: Principles and Processes",
            [
                "Principles of biotechnology",
                "Restriction enzymes",
                "Cloning vectors",
                "Competent host and transformation",
                "Polymerase chain reaction",
                "Downstream processing",
            ],
        ),
        chapter(
            "Biotechnology and its Applications",
            [
                "Biotechnological applications in agriculture",
                "Bt cotton",
                "RNA interference",
                "Biotechnological applications in medicine",
                "Transgenic animals",
                "Ethical issues and biopiracy",
            ],
        ),
        chapter(
            "Organisms and Populations",
            [
                "Organism and its environment",
                "Adaptations",
                "Population attributes",
                "Population growth",
                "Life history variation",
                "Population interactions",
            ],
        ),
        chapter(
            "Ecosystem",
            [
                "Ecosystem structure and function",
                "Productivity",
                "Decomposition",
                "Energy flow",
                "Ecological pyramids",
                "Nutrient cycling",
            ],
        ),
        chapter(
            "Biodiversity and Conservation",
            [
                "Biodiversity and its patterns",
                "Importance of species diversity",
                "Loss of biodiversity",
                "Biodiversity conservation in situ",
                "Biodiversity conservation ex situ",
                "Sacred groves and protected areas",
            ],
        ),
    ],
)

MATH_11: SubjectSpec = subject(
    "MATH",
    "Mathematics",
    [
        chapter("Sets", ["Sets and their representations", "Types of sets", "Subsets", "Power set and universal set", "Venn diagrams", "Operations on sets", "Complement of a set", "Practical problems on union and intersection"]),
        chapter("Relations and Functions", ["Cartesian product of sets", "Relations", "Functions", "Types of functions", "Real-valued functions and their graphs"]),
        chapter("Trigonometric Functions", ["Angles and radian measure", "Trigonometric functions", "Signs of trigonometric functions", "Identities", "Trigonometric equations", "General solution of trigonometric equations"]),
        chapter("Complex Numbers and Quadratic Equations", ["Complex numbers", "Algebra of complex numbers", "Modulus and conjugate", "Argand plane", "Polar representation", "Quadratic equations"]),
        chapter("Linear Inequalities", ["Inequalities", "Algebraic solutions of linear inequalities in one variable", "Graphical representation", "Linear inequalities in two variables", "System of linear inequalities"]),
        chapter("Permutations and Combinations", ["Fundamental principle of counting", "Permutations", "Permutations with repetition and circular permutations", "Combinations", "Simple applications"]),
        chapter("Binomial Theorem", ["Binomial theorem for positive integers", "Pascal's triangle", "General and middle terms", "Simple applications"]),
        chapter("Sequences and Series", ["Sequences", "Arithmetic progression", "Arithmetic mean", "Geometric progression", "Geometric mean", "Sum to n terms of special series"]),
        chapter("Straight Lines", ["Slope of a line", "Various forms of the equation of a line", "General equation of a line", "Distance of a point from a line", "Angle between two lines", "Concurrency of lines"]),
        chapter("Conic Sections", ["Sections of a cone", "Circle", "Parabola", "Ellipse", "Hyperbola"]),
        chapter("Introduction to Three Dimensional Geometry", ["Coordinate axes and coordinate planes in three dimensions", "Coordinates of a point in space", "Distance between two points", "Section formula"]),
        chapter("Limits and Derivatives", ["Intuitive idea of limit", "Limits of polynomials and rational functions", "Limits of trigonometric functions", "Derivative of a function", "Algebra of derivative of functions", "Derivative of trigonometric functions"]),
        chapter("Statistics", ["Measures of dispersion", "Range", "Mean deviation", "Variance", "Standard deviation", "Analysis of frequency distributions"]),
        chapter("Probability", ["Random experiments", "Event", "Axiomatic approach to probability", "Addition theorem of probability", "Conditional events"]),
    ],
)

MATH_12: SubjectSpec = subject(
    "MATH",
    "Mathematics",
    [
        chapter(
            "Relations and Functions",
            [
                "Types of relations",
                "Equivalence relations",
                "Types of functions",
                "Composition and invertible functions",
                "Binary operations",
            ],
        ),
        chapter(
            "Inverse Trigonometric Functions",
            [
                "Basic concepts",
                "Principal values",
                "Properties",
                "Graphs of inverse trigonometric functions",
            ],
        ),
        chapter(
            "Matrices",
            [
                "Types of matrices",
                "Operations on matrices",
                "Transpose and symmetric matrices",
                "Elementary operations and invertible matrices",
            ],
        ),
        chapter(
            "Determinants",
            [
                "Determinant of a square matrix",
                "Properties",
                "Area of a triangle",
                "Minors and cofactors",
                "Adjoint and inverse",
                "System of linear equations using determinants",
            ],
        ),
        chapter(
            "Continuity and Differentiability",
            [
                "Continuity",
                "Differentiability",
                "Exponential and logarithmic derivatives",
                "Derivatives of inverse trigonometric and exponential functions",
                "Second order derivatives",
                "Mean value theorems",
            ],
        ),
        chapter(
            "Application of Derivatives",
            [
                "Rate of change",
                "Increasing and decreasing functions",
                "Tangents and normals",
                "Maxima and minima",
                "Approximation using differentials",
            ],
        ),
        chapter(
            "Integrals",
            [
                "Indefinite integrals",
                "Methods of integration",
                "Integration by parts",
                "Partial fractions in integration",
                "Definite integrals",
                "Fundamental theorem of calculus",
                "Properties of definite integrals",
            ],
        ),
        chapter(
            "Application of Integrals",
            [
                "Area under simple curves",
                "Area between two curves",
                "Applications",
            ],
        ),
        chapter(
            "Differential Equations",
            [
                "Order and degree",
                "General and particular solutions",
                "Formation of a differential equation",
                "First order differential equations",
                "Variables separable",
                "Homogeneous differential equations",
                "Linear differential equations",
            ],
        ),
        chapter(
            "Vector Algebra",
            [
                "Types of vectors",
                "Addition of vectors",
                "Section formula for vectors",
                "Scalar and vector products",
                "Scalar triple product",
            ],
        ),
        chapter(
            "Three Dimensional Geometry",
            [
                "Direction cosines and ratios",
                "Equation of a line",
                "Angle between two lines",
                "Shortest distance between two lines",
                "Plane",
                "Angle between two planes",
            ],
        ),
        chapter(
            "Linear Programming",
            [
                "Linear programming problem",
                "Graphical method",
                "Feasible region",
                "Corner point method",
            ],
        ),
        chapter(
            "Probability",
            [
                "Conditional probability",
                "Multiplication theorem of probability",
                "Bayes' theorem",
                "Random variables",
                "Bernoulli trials and binomial distribution",
            ],
        ),
    ],
)

ENGLISH_11: SubjectSpec = subject(
    "ENG",
    "English Core",
    [
        chapter(
            "Hornbill – Prose",
            [
                "The Portrait of a Lady",
                "We're Not Afraid to Die",
                "Discovering Tut",
                "The Ailing Planet",
                "The Adventure",
                "Silk Road",
            ],
        ),
        chapter(
            "Hornbill – Poetry",
            [
                "A Photograph",
                "The Laburnum Top",
                "The Voice of the Rain",
                "Childhood",
                "Father to Son",
            ],
        ),
        chapter(
            "Snapshots – Supplementary Reader",
            [
                "The Summer of the Beautiful White Horse",
                "The Address",
                "Mother's Day",
                "Birth",
                "The Tale of Melon City",
            ],
        ),
        chapter(
            "Writing Skills",
            [
                "Note making",
                "Poster",
                "Classified advertisement",
                "Speech",
                "Debate",
            ],
        ),
        chapter(
            "Reading Skills",
            [
                "Unseen Passage – Comprehension",
                "Note making from a passage",
                "Summary writing",
            ],
        ),
        chapter(
            "Grammar / Language",
            [
                "Tenses",
                "Reordering of sentences",
                "Determiners",
                "Transformation of sentences",
            ],
        ),
    ],
)

ENGLISH_12: SubjectSpec = subject(
    "ENG",
    "English Core",
    [
        chapter(
            "Flamingo – Prose",
            [
                "The Last Lesson",
                "Lost Spring",
                "Deep Water",
                "The Rattrap",
                "Indigo",
                "Poets and Pancakes",
                "The Interview",
                "Going Places",
            ],
        ),
        chapter(
            "Flamingo – Poetry",
            [
                "My Mother at Sixty-Six",
                "Keeping Quiet",
                "A Thing of Beauty",
                "A Roadside Stand",
                "Aunt Jennifer's Tigers",
            ],
        ),
        chapter(
            "Vistas – Supplementary Reader",
            [
                "The Third Level",
                "The Tiger King",
                "Journey to the End of the Earth",
                "The Enemy",
                "On the Face of It",
                "Memories of Childhood",
            ],
        ),
        chapter(
            "Writing Skills",
            [
                "Notice Writing",
                "Invitation and Reply",
                "Letter Writing",
                "Article Writing",
                "Report Writing",
            ],
        ),
        chapter(
            "Reading Skills",
            [
                "Unseen Passage – Comprehension",
                "Case-based Unseen Passage",
                "Note Making & Summary",
            ],
        ),
        chapter(
            "Grammar / Language",
            [
                "Integrated Grammar Usage",
                "Sentence Structure and Transformation",
                "Modal Auxiliaries",
                "Verb Forms",
            ],
        ),
    ],
)

ACCOUNTANCY_11: SubjectSpec = subject(
    "ACC",
    "Accountancy",
    [
        chapter("Introduction to Accounting", ["Meaning of accounting", "Objectives of accounting", "Basic accounting terms"]),
        chapter("Theory Base of Accounting", ["Accounting principles", "Accounting standards", "Bases of accounting"]),
        chapter("Recording of Transactions — I", ["Accounting equation", "Rules of debit and credit", "Journal"]),
        chapter("Recording of Transactions — II", ["Cash book", "Other subsidiary books", "Ledger"]),
        chapter("Bank Reconciliation Statement", ["Need for BRS", "Causes of difference", "Preparation of BRS"]),
        chapter("Trial Balance and Rectification of Errors", ["Trial balance", "Types of errors", "Rectification"]),
        chapter("Depreciation, Provisions and Reserves", ["Meaning of depreciation", "Methods of depreciation", "Provisions and reserves"]),
        chapter("Bills of Exchange", ["Promissory note and bill of exchange", "Accounting treatment", "Dishonour and renewal"]),
        chapter("Financial Statements", ["Trading account", "Profit and loss account", "Balance sheet"]),
        chapter("Accounts from Incomplete Records", ["Meaning of incomplete records", "Statement of affairs", "Ascertaining profit"]),
    ],
)

ACCOUNTANCY_12: SubjectSpec = subject(
    "ACC",
    "Accountancy",
    [
        chapter("Accounting for Partnership Firms — Fundamentals", ["Partnership deed", "Fixed and fluctuating capital", "Profit sharing"]),
        chapter("Reconstitution — Admission of a Partner", ["New profit sharing ratio", "Goodwill", "Revaluation of assets and liabilities"]),
        chapter("Reconstitution — Retirement and Death of a Partner", ["Gaining ratio", "Settlement of retiring partner", "Deceased partner's share"]),
        chapter("Dissolution of Partnership Firm", ["Modes of dissolution", "Settlement of accounts", "Realisation account"]),
        chapter("Accounting for Share Capital", ["Share capital", "Issue of shares", "Forfeiture and reissue"]),
        chapter("Issue and Redemption of Debentures", ["Issue of debentures", "Interest on debentures", "Redemption of debentures"]),
        chapter("Financial Statements of a Company", ["Statement of Profit and Loss", "Balance Sheet", "Notes to accounts"]),
        chapter("Analysis of Financial Statements", ["Tools of analysis", "Comparative statements", "Common size statements"]),
        chapter("Accounting Ratios", ["Liquidity ratios", "Solvency ratios", "Activity and profitability ratios"]),
        chapter("Cash Flow Statement", ["Operating activities", "Investing activities", "Financing activities"]),
    ],
)

BUSINESS_11: SubjectSpec = subject(
    "BST",
    "Business Studies",
    [
        chapter("Nature and Purpose of Business", ["Human activities", "Business trade and commerce", "Objectives of business"]),
        chapter("Forms of Business Organisation", ["Sole proprietorship", "Partnership", "Company"]),
        chapter("Private, Public and Global Enterprises", ["Private sector", "Public sector", "Global enterprises and joint ventures"]),
        chapter("Business Services", ["Banking", "Insurance", "Communication and warehousing"]),
        chapter("Emerging Modes of Business", ["E-business", "Outsourcing", "Online transactions"]),
        chapter("Social Responsibilities of Business and Business Ethics", ["Concept of social responsibility", "Kinds of social responsibility", "Business ethics"]),
        chapter("Sources of Business Finance", ["Owners' funds", "Borrowed funds", "International sources"]),
        chapter("Small Business and Entrepreneurship", ["Small scale enterprise", "Role of small business", "Entrepreneurship"]),
        chapter("Internal Trade", ["Wholesale trade", "Retail trade", "GST idea"]),
        chapter("International Business", ["Meaning of international business", "Export and import", "WTO idea"]),
    ],
)

BUSINESS_12: SubjectSpec = subject(
    "BST",
    "Business Studies",
    [
        chapter("Nature and Significance of Management", ["Concept of management", "Objectives and importance", "Levels of management"]),
        chapter("Principles of Management", ["Fayol's principles", "Taylor's scientific management", "Comparison of principles"]),
        chapter("Business Environment", ["Meaning of business environment", "Dimensions", "Liberalisation privatisation globalisation"]),
        chapter("Planning", ["Meaning of planning", "Types of plans", "Planning process"]),
        chapter("Organising", ["Organising process", "Structure of organisation", "Delegation and decentralisation"]),
        chapter("Staffing", ["Staffing process", "Recruitment and selection", "Training and development"]),
        chapter("Directing", ["Supervision", "Motivation and leadership", "Communication"]),
        chapter("Controlling", ["Meaning of controlling", "Relationship with planning", "Controlling process"]),
        chapter("Financial Management", ["Financial decisions", "Financial planning", "Capital structure and working capital"]),
        chapter("Financial Markets", ["Money market", "Capital market", "Stock exchange and SEBI"]),
        chapter("Marketing Management", ["Marketing vs selling", "Marketing mix", "Product price place promotion"]),
        chapter("Consumer Protection", ["Importance of consumer protection", "Consumer rights", "Redressal machinery"]),
    ],
)

ECONOMICS_11: SubjectSpec = subject(
    "ECO",
    "Economics",
    [
        chapter("Introduction to Statistics for Economics", ["What is economics", "Meaning of statistics", "Functions of statistics"]),
        chapter("Collection of Data", ["Primary and secondary data", "Census and sampling", "Methods of collection"]),
        chapter("Organisation of Data", ["Raw data", "Classification", "Frequency distribution"]),
        chapter("Presentation of Data", ["Textual presentation", "Tabular presentation", "Diagrammatic presentation"]),
        chapter("Measures of Central Tendency", ["Arithmetic mean", "Median", "Mode"]),
        chapter("Correlation", ["Meaning of correlation", "Scatter diagram", "Karl Pearson's coefficient"]),
        chapter("Index Numbers", ["Meaning of index numbers", "Laspeyres and Paasche", "Consumer price index"]),
        chapter("Introduction to Microeconomics", ["Central problems of an economy", "Production possibility curve", "Positive and normative economics"]),
        chapter("Consumer's Equilibrium and Demand", ["Utility", "Indifference curve idea", "Demand and elasticity"]),
        chapter("Producer Behaviour and Supply", ["Production function", "Cost and revenue", "Supply"]),
        chapter("Forms of Market and Price Determination", ["Perfect competition", "Other market forms", "Price determination"]),
    ],
)

ECONOMICS_12: SubjectSpec = subject(
    "ECO",
    "Economics",
    [
        chapter("National Income and Related Aggregates", ["Circular flow", "GDP and related aggregates", "Methods of calculating national income"]),
        chapter("Money and Banking", ["Functions of money", "Commercial banks", "Central bank"]),
        chapter("Determination of Income and Employment", ["Aggregate demand and supply", "Propensity to consume", "Short-run equilibrium"]),
        chapter("Government Budget and the Economy", ["Meaning of budget", "Receipts and expenditure", "Deficit measures"]),
        chapter("Balance of Payments", ["Current and capital account", "Foreign exchange rate", "Determination of exchange rate"]),
        chapter("Indian Economy on the Eve of Independence", ["Agricultural sector", "Industrial sector", "Foreign trade"]),
        chapter("Indian Economy 1950–1990", ["Goals of five year plans", "Agriculture", "Industry and trade"]),
        chapter("Liberalisation, Privatisation and Globalisation", ["Background of 1991 reforms", "Liberalisation privatisation globalisation", "Outcomes"]),
        chapter("Human Capital Formation in India", ["Human capital", "Education and health", "Growth of human capital"]),
        chapter("Rural Development", ["Credit and marketing", "Agricultural diversification", "Organic farming"]),
        chapter("Employment: Growth, Informalisation and Other Issues", ["Workers and employment", "Informalisation", "Unemployment"]),
        chapter("Environment and Sustainable Development", ["Environment and economy", "Pollution", "Sustainable development"]),
        chapter("Comparative Development Experiences of India and its Neighbours", ["India Pakistan China", "Demographic indicators", "Development strategies"]),
    ],
)

HISTORY_11: SubjectSpec = subject(
    "HIST",
    "History",
    [
        chapter("Writing and City Life", ["Mesopotamia", "Cuneiform writing", "Urban life"]),
        chapter("An Empire Across Three Continents", ["Roman Empire", "Economy and society", "Late antiquity"]),
        chapter("Nomadic Empires", ["The Mongols", "Genghis Khan", "Steppe and sedentary societies"]),
        chapter("The Three Orders", ["Feudal society", "Clergy nobility peasantry", "The changing world of the three orders"]),
        chapter("Changing Cultural Traditions", ["Renaissance", "Humanism", "New ideas in Europe"]),
        chapter("Displacing Indigenous Peoples", ["Settler societies", "Native peoples of America and Australia", "Impact of colonisation"]),
        chapter("Paths to Modernisation", ["Japan", "China", "Different roads to the modern world"]),
    ],
)

HISTORY_12: SubjectSpec = subject(
    "HIST",
    "History",
    [
        chapter("Bricks, Beads and Bones", ["Harappan civilisation", "Subsistence and crafts", "Decline of Harappa"]),
        chapter("Kings, Farmers and Towns", ["Mahajanapadas", "Mauryan empire", "Early historic towns"]),
        chapter("Kinship, Caste and Class", ["Family and kinship", "Varna and jati", "Social differences"]),
        chapter("Thinkers, Beliefs and Buildings", ["Sanchi", "Buddhism and Jainism", "Early temples"]),
        chapter("Through the Eyes of Travellers", ["Al-Biruni", "Ibn Battuta", "Francois Bernier"]),
        chapter("Bhakti-Sufi Traditions", ["Bhakti saints", "Sufi silsilas", "New religious communities"]),
        chapter("An Imperial Capital: Vijayanagara", ["Rayas and nayakas", "The royal centre", "Sacred centre"]),
        chapter("Peasants, Zamindars and the State", ["Agrarian society", "Zamindars", "The Mughal land revenue system"]),
        chapter("Colonialism and the Countryside", ["Bengal and the Permanent Settlement", "The Deccan countryside", "Colonial records"]),
        chapter("Rebels and the Raj", ["The revolt of 1857", "Pattern of the rebellion", "Visual representations"]),
        chapter("Mahatma Gandhi and the Nationalist Movement", ["Non-Cooperation", "Civil Disobedience", "Quit India"]),
        chapter("Framing the Constitution", ["The Constituent Assembly", "The vision of the constitution", "Defining rights"]),
    ],
)

POLITICAL_11: SubjectSpec = subject(
    "POL",
    "Political Science",
    [
        chapter("Constitution: Why and How?", ["Why we need a constitution", "How the Indian Constitution was made", "Outstanding features"]),
        chapter("Rights in the Indian Constitution", ["Bill of Rights", "Fundamental Rights", "Directive Principles"]),
        chapter("Election and Representation", ["Elections and democracy", "Election system in India", "Electoral reforms"]),
        chapter("Executive", ["Parliamentary executive in India", "Prime Minister and Council of Ministers", "Permanent executive"]),
        chapter("Legislature", ["Why we need a parliament", "Two Houses of parliament", "Parliamentary control"]),
        chapter("Judiciary", ["Independence of the judiciary", "Supreme Court", "Judicial review and activism"]),
        chapter("Federalism", ["What is federalism", "Federalism in the Indian Constitution", "Conflicts in India's federal system"]),
        chapter("Local Governments", ["Why local governments", "73rd and 74th Amendments", "Implementation and challenges"]),
        chapter("Constitution as a Living Document", ["Are constitutions static", "Amendments", "Basic structure"]),
        chapter("The Philosophy of the Constitution", ["What is the political philosophy", "Procedural achievements", "National identity"]),
        chapter("Political Theory: An Introduction", ["What is politics", "What is political theory", "Putting political theory to practice"]),
        chapter("Freedom", ["The ideal of freedom", "What is freedom", "Negative and positive liberty"]),
        chapter("Equality", ["Why does equality matter", "What is equality", "How can we promote equality"]),
        chapter("Social Justice", ["What is justice", "Just distribution", "John Rawls and free markets"]),
        chapter("Rights", ["What are rights", "Where do rights come from", "Rights and responsibilities"]),
        chapter("Citizenship", ["Citizen and nation", "Full and equal membership", "Global citizenship"]),
        chapter("Nationalism", ["Nations and nationalism", "National self-determination", "Nationalism and pluralism"]),
        chapter("Secularism", ["What is secularism", "Western and Indian models", "Criticisms of Indian secularism"]),
    ],
)

POLITICAL_12: SubjectSpec = subject(
    "POL",
    "Political Science",
    [
        chapter("The End of Bipolarity", ["Soviet system", "Gorbachev and disintegration", "Consequences and shock therapy"]),
        chapter("Contemporary Centres of Power", ["European Union", "ASEAN", "Rise of China"]),
        chapter("Contemporary South Asia", ["What is South Asia", "The military and democracy", "India's relations in the region"]),
        chapter("International Organisations", ["Why international organisations", "Evolution of the UN", "IMF World Bank WTO"]),
        chapter("Security in the Contemporary World", ["Traditional notions of security", "Non-traditional security", "India's security strategy"]),
        chapter("Environment and Natural Resources", ["Environmental concerns", "Common property resources", "India's stand"]),
        chapter("Globalisation", ["Causes of globalisation", "Political economic cultural consequences", "India and resistance"]),
        chapter("Challenges of Nation-Building", ["Partition", "Integration of princely states", "Reorganisation of states"]),
        chapter("Era of One-Party Dominance", ["Congress dominance", "Nature of Congress dominance", "Emergence of opposition"]),
        chapter("Politics of Planned Development", ["Political contestation", "The early phase of planning", "Land reforms and Green Revolution"]),
        chapter("India's External Relations", ["Nehru's foreign policy", "Sino-Indian war", "India's nuclear policy"]),
        chapter("Challenges to and Restoration of the Congress System", ["1967 elections", "Split in the Congress", "1971 restoration"]),
        chapter("The Crisis of Democratic Order", ["Background to Emergency", "Declaration of Emergency", "Politics after Emergency"]),
        chapter("Regional Aspirations", ["Region and the nation", "Jammu and Kashmir", "North-East and Punjab"]),
        chapter("Recent Developments in Indian Politics", ["Context of the 1990s", "Era of coalitions", "Growing consensus"]),
    ],
)

GEOGRAPHY_11: SubjectSpec = subject(
    "GEO",
    "Geography",
    [
        chapter("Geography as a Discipline", ["What is geography", "Branches of geography", "Physical and human geography"]),
        chapter("The Origin and Evolution of the Earth", ["Early theories", "Modern theories", "Evolution of lithosphere atmosphere hydrosphere"]),
        chapter("Interior of the Earth", ["Sources of information", "Earthquake waves", "Structure of the earth"]),
        chapter("Distribution of Oceans and Continents", ["Continental drift", "Sea-floor spreading", "Plate tectonics"]),
        chapter("Geomorphic Processes", ["Endogenic processes", "Exogenic processes", "Weathering and erosion"]),
        chapter("Landforms and their Evolution", ["Running water", "Groundwater and glaciers", "Waves and wind"]),
        chapter("Composition and Structure of Atmosphere", ["Composition", "Structure", "Elements of weather and climate"]),
        chapter("Solar Radiation, Heat Balance and Temperature", ["Insolation", "Heating and cooling of atmosphere", "Temperature distribution"]),
        chapter("Atmospheric Circulation and Weather Systems", ["Pressure belts", "Winds", "Cyclones"]),
        chapter("Water in the Atmosphere", ["Humidity", "Evaporation and condensation", "Rainfall"]),
        chapter("World Climate and Climate Change", ["Koeppen's classification", "Climate change", "Global warming"]),
        chapter("Water (Oceans)", ["Hydrological cycle", "Relief of the ocean floor", "Temperature and salinity"]),
        chapter("Movements of Ocean Water", ["Waves", "Tides", "Ocean currents"]),
        chapter("Biodiversity and Conservation", ["Biodiversity", "Loss of biodiversity", "Conservation"]),
        chapter("India — Location", ["Size and location", "India and its neighbours", "Standard meridian"]),
        chapter("Structure and Physiography", ["Geological structure", "Physiographic divisions", "The Himalayas and Peninsular Plateau"]),
        chapter("Drainage System", ["Drainage patterns", "Himalayan rivers", "Peninsular rivers"]),
        chapter("Climate", ["Unity and diversity of climate", "Monsoon", "Seasons"]),
        chapter("Natural Vegetation", ["Types of vegetation", "Forest cover", "Wildlife"]),
        chapter("Natural Hazards and Disasters", ["Earthquakes and tsunamis", "Tropical cyclones", "Floods and droughts"]),
    ],
)

GEOGRAPHY_12: SubjectSpec = subject(
    "GEO",
    "Geography",
    [
        chapter("Human Geography — Nature and Scope", ["Nature of human geography", "Schools of thought", "Human and physical geography"]),
        chapter("The World Population", ["Distribution of population", "Density", "Growth of population"]),
        chapter("Human Development", ["Growth vs development", "Four pillars of human development", "HDI"]),
        chapter("Primary Activities", ["Hunting gathering pastoralism", "Agriculture", "Mining"]),
        chapter("Secondary Activities", ["Manufacturing", "Classification of industries", "Household to large scale"]),
        chapter("Tertiary and Quaternary Activities", ["Tertiary activities", "Quaternary activities", "Digital divide"]),
        chapter("Transport and Communication", ["Land water air transport", "Pipelines", "Communication"]),
        chapter("International Trade", ["History of international trade", "WTO", "Gateways of international trade"]),
        chapter("Population: Distribution, Density, Growth and Composition", ["Distribution of population in India", "Growth", "Composition"]),
        chapter("Human Settlements", ["Rural settlements", "Urban settlements", "Urbanisation in India"]),
        chapter("Land Resources and Agriculture", ["Land use", "Agriculture types", "Agricultural development"]),
        chapter("Water Resources", ["Water resources of India", "Water demand and utilisation", "Watershed management"]),
        chapter("Mineral and Energy Resources", ["Types of minerals", "Conventional energy", "Non-conventional energy"]),
        chapter("Planning and Sustainable Development in Indian Context", ["Planning in India", "Target area planning", "Sustainable development"]),
        chapter("Transport and Communication in India", ["Roadways and railways", "Waterways and airways", "Communication networks"]),
        chapter("Geographical Perspective on Selected Issues and Problems", ["Environmental pollution", "Urban waste", "Urbanisation issues"]),
    ],
)
