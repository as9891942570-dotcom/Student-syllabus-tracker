"""CBSE Class 12 Chemistry concept MCQ banks."""

from __future__ import annotations

from app.data.quiz_banks.common import q, register_keys, register_subject_keywords
from app.data.quiz_concepts import QuestionBank

# ---------------------------------------------------------------------------
# Solutions
# ---------------------------------------------------------------------------

BANK_SOLUTION_TYPES: QuestionBank = [
    q(
        "A homogeneous mixture of two or more components whose composition can vary within certain limits is called a:",
        "Solution",
        ["Compound with fixed stoichiometry", "Heterogeneous colloid only", "Pure element"],
    ),
    q(
        "In a solution of sugar in water, sugar is the:",
        "Solute",
        ["Solvent", "Suspension", "Emulsifier only"],
    ),
    q(
        "Brass (copper and zinc) is an example of a:",
        "Solid in solid solution (alloy)",
        ["Gas in liquid solution", "Liquid in gas solution", "Solid in gas aerosol only"],
    ),
    q(
        "Air is best classified as a:",
        "Gas in gas solution",
        ["Solid solution", "Liquid in solid solution", "Suspension of dust only"],
    ),
    q(
        "A solution in which no more solute dissolves at a given temperature is:",
        "Saturated solution",
        ["Unsaturated solution", "Superheated gas", "Ideal gas only"],
    ),
    q(
        "For a binary liquid solution, if both components follow Raoult's law over the entire range of composition, the solution is:",
        "Ideal",
        ["Always non-ideal", "Always a colloid", "Always a suspension"],
    ),
    q(
        "Henry's law is most directly applicable to:",
        "Dissolution of a gas in a liquid",
        ["Mixing of two immiscible liquids", "Fusion of a pure metal", "Sublimation of iodine only"],
    ),
    q(
        "Sea water is primarily a:",
        "Liquid solution (solid solutes in water)",
        ["Gas in solid solution", "Solid in gas solution", "Pure compound"],
    ),
]

BANK_CONCENTRATION_TERMS: QuestionBank = [
    q(
        "Molarity (M) of a solution is defined as:",
        "Number of moles of solute per litre of solution",
        ["Moles of solute per kg of solvent", "Mass of solute per 100 g solution", "Moles of solvent per litre"],
    ),
    q(
        "Molality (m) uses which quantity in the denominator?",
        "Mass of solvent in kg",
        ["Volume of solution in L", "Volume of solute in mL", "Number of formula units only"],
    ),
    q(
        "The mole fraction of a component in a binary solution is:",
        "Moles of that component divided by total moles of all components",
        ["Mass percent divided by 100", "Molarity divided by molality", "Always equal to 1 for any solute"],
    ),
    q(
        "On dilution of a solution (adding solvent), which concentration term decreases for a given solute amount?",
        "Molarity",
        ["Molality", "Mole fraction of solute", "Mass percent (if no evaporation)"],
    ),
    q(
        "A 0.50 M NaCl solution means:",
        "0.50 mol NaCl dissolved in enough water to make 1.00 L of solution",
        ["0.50 g NaCl in 1 L water", "0.50 mol NaCl in 1 kg water", "0.50 mol NaCl in 0.50 L solution"],
    ),
    q(
        "For dilution at constant temperature, the relation M1V1 = M2V2 applies when:",
        "The same solute is diluted with the same solvent and volume additivity holds",
        ["Temperature changes drastically", "A chemical reaction consumes solute", "Two different solutes are mixed"],
    ),
    q(
        "Parts per million (ppm) expresses concentration as:",
        "Mass (or sometimes volume) of solute per million parts of solution",
        ["Moles per litre only", "Always moles per kg solvent", "Only for gases at STP"],
    ),
    q(
        "Which pair is both intensive properties of a solution?",
        "Molarity and mole fraction",
        ["Mass of solute and volume of solvent", "Total moles and total mass", "Beaker size and stirrer speed"],
    ),
]

BANK_COLLIGATIVE: QuestionBank = [
    q(
        "Colligative properties depend on:",
        "The number of solute particles in solution, not their chemical identity",
        ["Only the colour of the solute", "Only the density of the solvent", "The shape of the container"],
    ),
    q(
        "According to Raoult's law for a non-volatile solute, relative lowering of vapour pressure equals:",
        "Mole fraction of solute",
        ["Molality of solvent", "Density of solution", "Refractive index of solvent"],
    ),
    q(
        "Elevation in boiling point (Delta Tb) is given by Delta Tb = Kb m, where m is:",
        "Molality of the solution",
        ["Molarity of the solution", "Mole fraction of solvent only", "Normality in all cases"],
    ),
    q(
        "For the same molal concentration, which aqueous solution shows the greatest depression in freezing point?",
        "1 m NaCl (i ≈ 2)",
        ["1 m glucose (i = 1)", "1 m urea (i = 1)", "1 m sucrose (i = 1)"],
    ),
    q(
        "Osmotic pressure of a dilute solution is given by pi = iCRT, where C is:",
        "Molar concentration of solute",
        ["Molal concentration", "Mass percent", "Normality always without i"],
    ),
    q(
        "Van't Hoff factor (i) for BaCl2 in very dilute aqueous solution is ideally:",
        "3",
        ["1", "2", "0"],
    ),
    q(
        "Which is NOT a colligative property?",
        "Refractive index change used alone as a bulk property",
        ["Lowering of vapour pressure", "Elevation in boiling point", "Osmotic pressure"],
    ),
    q(
        "If observed molar mass of an electrolyte from colligative measurement is less than normal molar mass, it indicates:",
        "Dissociation in solution (i > 1)",
        ["Association of solute molecules", "Solvent evaporation only", "Measurement at zero kelvin"],
    ),
]

# ---------------------------------------------------------------------------
# Electrochemistry
# ---------------------------------------------------------------------------

BANK_ELECTROCHEMICAL_CELLS: QuestionBank = [
    q(
        "In a galvanic (voltaic) cell, spontaneous redox reaction produces:",
        "Electrical energy",
        ["Only heat with no voltage", "Light without electron flow", "A non-spontaneous process"],
    ),
    q(
        "At the anode of a galvanic cell:",
        "Oxidation occurs",
        ["Reduction occurs", "No electron release occurs", "Cations are always reduced"],
    ),
    q(
        "The salt bridge in a galvanic cell primarily:",
        "Maintains electrical neutrality by allowing ion migration",
        ["Stores electrons for later use", "Acts as the cathode", "Prevents all ion movement"],
    ),
    q(
        "In the Daniell cell (Zn | Zn2+ || Cu2+ | Cu), the anode is:",
        "Zinc electrode",
        ["Copper electrode", "Salt bridge only", "Platinum inert electrode always"],
    ),
    q(
        "Standard cell potential E°cell for a spontaneous galvanic cell is:",
        "Positive",
        ["Always zero", "Always negative", "Undefined for all cells"],
    ),
    q(
        "For a cell E°cell = E°cathode - E°anode. If E°(Cu2+/Cu) = +0.34 V and E°(Zn2+/Zn) = -0.76 V, E°cell for Daniell cell is:",
        "+1.10 V",
        ["-1.10 V", "+0.42 V", "-0.42 V"],
    ),
    q(
        "An electrolytic cell differs from a galvanic cell because:",
        "Electrical energy drives a non-spontaneous reaction",
        ["It never uses electrodes", "It cannot involve ions", "It always has E°cell > 0 without external power"],
    ),
    q(
        "Cell notation lists:",
        "Anode (oxidation) on the left, cathode (reduction) on the right",
        ["Cathode on the left always", "Only aqueous species without electrodes", "Salt bridge as the first entry"],
    ),
]

BANK_NERNST: QuestionBank = [
    q(
        "The Nernst equation at 298 K has the form E = E° - (0.0591/n) log Q for:",
        "Electrode or cell potential under non-standard conditions",
        ["Ideal gas law calculations only", "Rate constant of first-order reactions", "Colligative property calculations"],
    ),
    q(
        "In the Nernst equation, n represents:",
        "Number of moles of electrons transferred in the half-reaction",
        ["Order of reaction", "Number of ligands in a complex", "Avogadro number"],
    ),
    q(
        "If Q < K for a galvanic cell at 298 K, the cell potential E compared to E° is:",
        "Greater than E°",
        ["Always equal to E°", "Always less than E°", "Always zero"],
    ),
    q(
        "For the half-cell Cu2+ + 2e- -> Cu, increasing [Cu2+] at fixed temperature will:",
        "Increase the electrode potential",
        ["Decrease the electrode potential", "Leave potential unchanged always", "Reverse the electrode identity"],
    ),
    q(
        "When a galvanic cell is completely discharged (reactants at equilibrium), the cell potential becomes:",
        "Zero",
        ["Equal to E° always", "Infinite", "Negative of Faraday constant"],
    ),
    q(
        "The reaction quotient Q for a cell reaction includes:",
        "Products and reactants raised to stoichiometric powers (activities or concentrations as used)",
        ["Only temperature terms", "Only pressure of inert gas", "Only catalyst concentration"],
    ),
    q(
        "For Zn(s) + Cu2+(aq) -> Zn2+(aq) + Cu(s), if [Zn2+] increases while [Cu2+] decreases, Ecell will:",
        "Decrease compared to standard conditions",
        ["Increase compared to standard conditions", "Remain exactly E° always", "Become independent of concentration"],
    ),
    q(
        "Nernst equation reduces to E = E° when:",
        "All species are in standard states (Q = 1)",
        ["Temperature is 0 K only", "Current is maximum", "Salt bridge is removed"],
    ),
]

BANK_ELECTROLYSIS_CONDUCTANCE: QuestionBank = [
    q(
        "Specific conductance (kappa) is defined as:",
        "Conductance of a solution placed between two electrodes 1 cm apart with 1 cm2 area",
        ["Resistance of 1 ohm wire only", "Molar mass times density", "Rate of electrolysis"],
    ),
    q(
        "Molar conductance (Lambda m) equals:",
        "kappa × (1000 / M) for molarity M in mol L-1",
        ["kappa / density always", "Resistance times area", "Faraday constant divided by time"],
    ),
    q(
        "For strong electrolytes, molar conductance increases on dilution because:",
        "Inter-ionic interactions decrease",
        ["Degree of dissociation decreases", "Ions disappear completely", "Solvent becomes an insulator"],
    ),
    q(
        "Kohlrausch's law states that at infinite dilution, molar conductance of an electrolyte is:",
        "Sum of molar ionic conductances of constituent ions",
        ["Product of ionic charges only", "Independent of ion type", "Zero for all salts"],
    ),
    q(
        "During electrolysis of molten NaCl, the product at the cathode is:",
        "Sodium metal",
        ["Chlorine gas at cathode", "Oxygen from Na only", "Hydrogen always"],
    ),
    q(
        "Faraday's first law of electrolysis relates:",
        "Mass deposited to quantity of charge passed",
        ["Mass to colour of solution", "Volume to pressure only", "Rate to activation energy only"],
    ),
    q(
        "One faraday (96500 C mol-1) corresponds to:",
        "Charge of 1 mol of electrons",
        ["Mass of 1 mol of protons", "Energy of 1 mol photons", "1 mole of any ion without charge"],
    ),
    q(
        "Weak electrolytes show much larger increase in molar conductance on dilution than strong electrolytes mainly because:",
        "Degree of ionisation increases significantly on dilution",
        ["They become covalent solids", "Ions combine to form molecules irreversibly at all concentrations", "Solvent decomposes"],
    ),
]

# ---------------------------------------------------------------------------
# Chemical Kinetics
# ---------------------------------------------------------------------------

BANK_RATE_OF_REACTION: QuestionBank = [
    q(
        "The rate of a reaction is defined as:",
        "Change in concentration of a reactant or product per unit time",
        ["Total mass of flask per hour", "Volume of gas at STP only", "Equilibrium constant value"],
    ),
    q(
        "For 2N2O5 -> 4NO2 + O2, the rate in terms of N2O5 is:",
        "-(1/2) d[N2O5]/dt if using stoichiometric coefficient convention for rate expression",
        ["d[N2O5]/dt always positive", "d[O2]/dt without any factor", "Independent of stoichiometry always"],
    ),
    q(
        "Instantaneous rate of reaction is obtained from:",
        "Slope of tangent to concentration vs time curve at a given time",
        ["Average of initial and final rates only", "Equilibrium constant", "Activation energy alone"],
    ),
    q(
        "For a zero-order reaction, rate depends on concentration as:",
        "Rate = k (independent of concentration)",
        ["Rate = k[A]", "Rate = k[A]^2 always", "Rate = k/[A]"],
    ),
    q(
        "Units of rate constant k for a first-order reaction are:",
        "s-1 (or time-1)",
        ["mol L-1 s-1", "L mol-1 s-1", "L2 mol-2 s-1"],
    ),
    q(
        "If a graph of concentration vs time is a straight line with negative slope for reactant A, the order with respect to A is:",
        "Zero",
        ["First", "Second", "Cannot be determined"],
    ),
    q(
        "Rate law r = k[A]^m[B]^n is determined:",
        "Experimentally",
        ["Always from balanced equation coefficients only", "From molecular mass only", "From colour of solution"],
    ),
    q(
        "When rate doubles on doubling [A] while [B] is constant, order with respect to A is:",
        "1",
        ["0", "2", "-1"],
    ),
]

BANK_FACTORS_AFFECTING_RATE: QuestionBank = [
    q(
        "According to collision theory, reaction rate increases with temperature mainly because:",
        "More collisions have energy >= activation energy",
        ["Molecules become larger", "Activation energy always increases", "Catalyst is always formed"],
    ),
    q(
        "A catalyst increases reaction rate by:",
        "Providing an alternative pathway with lower activation energy",
        ["Increasing equilibrium constant always", "Consuming products permanently", "Increasing activation energy"],
    ),
    q(
        "For heterogeneous catalysis, increasing surface area of solid catalyst generally:",
        "Increases reaction rate",
        ["Decreases rate always", "Has no effect ever", "Stops the reaction"],
    ),
    q(
        "For gaseous reactants, increasing pressure at constant temperature usually increases rate because:",
        "Concentrations (or partial pressures) of gaseous species increase",
        ["Activation energy becomes zero", "Order of reaction always doubles", "Catalyst is destroyed"],
    ),
    q(
        "The Arrhenius equation k = A exp(-Ea/RT) shows that rate constant k:",
        "Increases exponentially with temperature for positive Ea",
        ["Decreases with temperature always", "Is independent of Ea", "Equals A at all temperatures"],
    ),
    q(
        "Light can increase rate of some reactions (photochemical) by:",
        "Providing energy to excite reactant molecules",
        ["Lowering molecular mass", "Removing activation energy completely", "Converting products to reactants at equilibrium"],
    ),
    q(
        "In general, increasing concentration of reactants in the same phase increases rate because:",
        "Frequency of effective collisions increases",
        ["Equilibrium shifts to products only without affecting rate", "Catalyst concentration always decreases", "Order becomes zero"],
    ),
    q(
        "Nature of reactants affects rate because:",
        "Bond strengths and molecular complexity influence activation energy",
        ["All reactions have identical Ea", "Only colour matters", "Only solvent density matters exclusively"],
    ),
]

BANK_INTEGRATED_RATE: QuestionBank = [
    q(
        "Integrated rate law for first-order reaction is:",
        "ln[A] = ln[A]0 - kt",
        ["[A] = [A]0 + kt", "[A] = [A]0 - kt for all orders", "ln[A] = kt^2"],
    ),
    q(
        "Half-life (t1/2) for a first-order reaction:",
        "Is independent of initial concentration",
        ["Is proportional to initial concentration", "Doubles when [A]0 doubles", "Is zero at all temperatures"],
    ),
    q(
        "For first-order reaction, t1/2 =",
        "0.693/k",
        ["k/0.693", "1/k^2", "2/k always"],
    ),
    q(
        "A plot of ln[A] vs time giving a straight line indicates:",
        "First-order kinetics",
        ["Zero-order kinetics", "Second-order kinetics always", "Third-order only"],
    ),
    q(
        "For zero-order reaction, integrated form is:",
        "[A] = [A]0 - kt",
        ["ln[A] = ln[A]0 - kt", "1/[A] = 1/[A]0 + kt", "[A] = kt^2"],
    ),
    q(
        "For second-order reaction 2A -> products, integrated law is:",
        "1/[A] = 1/[A]0 + 2kt (or equivalent with stoichiometric factor)",
        ["[A] = [A]0 - kt", "ln[A] = ln[A]0 - kt", "[A]^2 = constant always"],
    ),
    q(
        "Time required for 75% completion of a first-order reaction is:",
        "2 × t1/2",
        ["t1/2", "3 × t1/2", "0.5 × t1/2"],
    ),
    q(
        "For a second-order reaction, half-life t1/2 is:",
        "Inversely proportional to initial concentration",
        ["Independent of initial concentration", "Always 0.693/k", "Proportional to square of k only"],
    ),
]

# ---------------------------------------------------------------------------
# The d- and f-Block Elements
# ---------------------------------------------------------------------------

BANK_TRANSITION_ELEMENTS: QuestionBank = [
    q(
        "Transition elements are defined as d-block elements having:",
        "Partially filled d orbitals in ground state or common oxidation states",
        ["Completely filled d orbitals only in all states", "No variable valency", "Only +1 oxidation state"],
    ),
    q(
        "Variable oxidation states in transition metals arise mainly due to:",
        "Similar energy of (n-1)d and ns electrons",
        ["Only noble gas configuration", "Absence of d orbitals", "Fixed ionisation always removing all d electrons first"],
    ),
    q(
        "Transition metal ions are often coloured because of:",
        "d-d electronic transitions in partially filled d subshell",
        ["s-s transitions only", "Complete absence of unpaired electrons always", "Nuclear fusion in nucleus"],
    ),
    q(
        "Which pair is NOT considered a true transition element by strict d-orbital definition?",
        "Zn and Cd (common +2, d10 in M2+)",
        ["Fe and Cu", "Cr and Mn", "Ni and Co"],
    ),
    q(
        "Transition metals show catalytic activity partly because they:",
        "Provide multiple oxidation states and surfaces for adsorption",
        ["Have no unpaired electrons ever", "Are always gases", "Cannot form complexes"],
    ),
    q(
        "Highest oxidation state of manganese in KMnO4 is:",
        "+7",
        ["+2", "+4", "+6"],
    ),
    q(
        "Interstitial compounds are formed when small atoms (H, B, C, N) occupy:",
        "Interstitial sites in transition metal lattices",
        ["Only ionic crystal anion sites exclusively in NaCl", "Only gas phase", "Only f-block metals exclusively"],
    ),
    q(
        "Magnetic moment of transition metal ions is often calculated using:",
        "Number of unpaired electrons (spin-only approximation)",
        ["Only atomic mass", "Only density", "Only melting point"],
    ),
]

BANK_LANTHANOIDS: QuestionBank = [
    q(
        "Lanthanoids are:",
        "4f inner-transition series (Ce to Lu)",
        ["3d transition series", "5d series only", "Alkali metals"],
    ),
    q(
        "The most common oxidation state of lanthanoids is:",
        "+3",
        ["+1 only", "+7 only", "0 only"],
    ),
    q(
        "Lanthanoid contraction refers to:",
        "Steady decrease in atomic/ionic radii across the series due to poor shielding by 4f electrons",
        ["Expansion of atoms due to f filling", "Increase in atomic radius from La to Lu", "Only melting point trend"],
    ),
    q(
        "Lanthanoid contraction causes:",
        "Similar radii of 4d and 5d transition pairs (e.g. Zr/Hf)",
        ["Identical chemistry of alkali metals", "Increase in atomic size of Hf over Zr", "Zero ionisation energy change"],
    ),
    q(
        "Separation of individual lanthanoids is difficult because:",
        "Their chemical properties are very similar",
        ["They are all gases", "They do not form ions", "They have no 4f electrons"],
    ),
    q(
        "Cerium shows +4 oxidation state in compounds like CeO2 because:",
        "Ce4+ has stable empty or half-filled f configuration relative to neighbouring states in that compound",
        ["Ce has no f electrons", "Oxygen forces -4 on cerium only", "Ce is an alkali metal"],
    ),
    q(
        "Lanthanoid compounds are used in:",
        "Alloy steels and glass polishing (e.g. mischmetal)",
        ["Only noble gas liquefaction exclusively", "Only polymerisation of ethene without catalyst", "Only ammonia synthesis iron catalyst"],
    ),
    q(
        "Which statement about lanthanoids is correct?",
        "They are silvery white metals with high melting points",
        ["They are all liquids at room temperature", "They lack f electrons", "They belong to p-block"],
    ),
]

BANK_IMPORTANT_COMPOUNDS_D_BLOCK: QuestionBank = [
    q(
        "Acidified K2Cr2O7 is a strong oxidising agent; in basic medium chromate-dichromate equilibrium favours:",
        "Chromate (CrO4)2- (yellow)",
        ["Only Cr2O7 (orange) exclusively at all pH", "Elemental chromium only", "MnO4- always"],
    ),
    q(
        "KMnO4 in acidic medium is reduced to Mn2+ (colourless/light pink) while itself acts as:",
        "Oxidising agent",
        ["Reducing agent only", "Catalyst only without redox", "Precipitating agent for Cl- only"],
    ),
    q(
        "Potassium permanganate (KMnO4) has manganese in oxidation state:",
        "+7",
        ["+2", "+4", "+6"],
    ),
    q(
        "K2Cr2O7 is preferred in volumetric analysis as primary standard because it:",
        "Is available pure and stable as solid",
        ["Decomposes in minutes in air", "Is always a reducing agent", "Has Mn as central atom"],
    ),
    q(
        "Green colour of NiSO4 solutions and complex ions arises from:",
        "d-d transitions in Ni2+ (partially filled d)",
        ["Only charge transfer from SO4 only without metal involvement", "Only s-p transition", "Nuclear isomerism"],
    ),
    q(
        "When K2Cr2O7 reacts with KI in acidic medium, I- is oxidised to I2; this reaction is used to:",
        "Estimate oxidising capacity / in iodometric titrations",
        ["Prepare ammonia", "Make graphite electrodes only", "Synthesise methane directly"],
    ),
    q(
        "Magnetic nature of Fe, Co, Ni metals is related to:",
        "Unpaired d electrons and domain structure",
        ["Only noble gas cores", "Only p orbital pairing", "Only ionic radius of anions"],
    ),
    q(
        "Interstitial carbides of transition metals (e.g. Fe3C in steel) differ from ionic carbides because:",
        "Carbon occupies holes in metal lattice rather than forming simple ionic lattice alone",
        ["They contain no carbon", "They are always gases", "They cannot conduct electricity"],
    ),
]

# ---------------------------------------------------------------------------
# Coordination Compounds
# ---------------------------------------------------------------------------

BANK_WERNERS_THEORY: QuestionBank = [
    q(
        "According to Werner's theory, primary valence of a metal in a complex is:",
        "Ionisable bonds satisfied by anions (oxidation state related)",
        ["Non-ionisable bonds to ligands only", "Always zero", "Equal to coordination number always"],
    ),
    q(
        "Secondary valence in Werner's theory corresponds to:",
        "Coordination number (directional bonds to ligands)",
        ["Only ionic charge on metal without ligands", "Mass of ligands only", "Number of counter ions in crystal always equal without exception"],
    ),
    q(
        "In [Co(NH3)6]Cl3, primary valence of Co is:",
        "3",
        ["6", "0", "1"],
    ),
    q(
        "In [Co(NH3)6]Cl3, secondary valence (coordination number) of Co is:",
        "6",
        ["3", "4", "2"],
    ),
    q(
        "Werner's theory explains why some metal salts exist as:",
        "Complex ions with definite geometry in solution and solid",
        ["Only monatomic gases", "Only covalent network without ions", "Only isotopes"],
    ),
    q(
        "Ligands in Werner's coordination sphere are bound by:",
        "Secondary valence (coordinate bonds)",
        ["Primary valence only with full ionisation always", "Only hydrogen bonds exclusively", "Only van der Waals forces in all complexes"],
    ),
    q(
        "[Pt(NH3)2Cl2] has coordination number of Pt equal to:",
        "4",
        ["2", "6", "8"],
    ),
    q(
        "Which observation supported Werner's theory over chain theory?",
        "Conductivity of cobalt ammine chlorides matched number of ionisable Cl- ions",
        ["All cobalt compounds had identical colour always", "Complexes never isomerise", "Ligands are always monodentate only"],
    ),
]

BANK_COORD_NOMENCLATURE: QuestionBank = [
    q(
        "In IUPAC naming of coordination compounds, ligands are named:",
        "Before the metal",
        ["After the metal always without exception", "Only by colour", "Only by molecular mass"],
    ),
    q(
        "The ligand CN- is named:",
        "cyano",
        ["chloro", "ammine", "aqua"],
    ),
    q(
        "For complex anion [Fe(CN)6]4-, the metal name becomes:",
        "ferrate(II)",
        ["iron(II) without -ate", "ferric only", "Fe ion only"],
    ),
    q(
        "Oxidation state of central metal in nomenclature is indicated by:",
        "Roman numeral in parentheses after metal name",
        ["Greek prefix before ligand only", "Subscript on ligand only", "Colour code"],
    ),
    q(
        "Name of [Co(NH3)6]Cl3 is:",
        "Hexaamminecobalt(III) chloride",
        ["Trichlorocobalt hexaammine", "Cobalt ammine trichloride only without oxidation state", "Hexamine cobalt chloride(0)"],
    ),
    q(
        "Multiple ligands of the same type use prefixes di-, tri-, tetra- except when the ligand name already contains:",
        "Such prefixes (e.g. ethylenediamine abbreviated en)",
        ["Metal name", "Roman numerals", "Charge on complex only"],
    ),
    q(
        "In [Cr(H2O)6]Cl3, ligand water is named:",
        "aqua",
        ["hydroxo always", "oxo", "hydrido"],
    ),
    q(
        "The complex cation [Cu(NH3)4]2+ is named:",
        "tetraamminecopper(II) ion",
        ["cupric tetrammine without ammine prefix", "copper ammonia four ion only", "diamminecopper(II) ion"],
    ),
]

BANK_BONDING_ISOMERISM: QuestionBank = [
    q(
        "Crystal field theory explains colour of complexes due to:",
        "Splitting of d orbitals and d-d transitions",
        ["Only ionic radius of Na+", "Only ligand mass", "Only s-s transitions"],
    ),
    q(
        "In octahedral field, d orbitals split into:",
        "t2g and eg sets",
        ["Only one degenerate level", "Only p orbitals", "Only f orbitals"],
    ),
    q(
        "Geometrical isomerism in square planar [Pt(NH3)2Cl2] gives:",
        "Cis and trans isomers",
        ["Optical isomers only", "Linkage isomers only", "No isomers possible"],
    ),
    q(
        "Optical isomerism in octahedral complexes requires:",
        "Chiral arrangement (non-superimposable mirror images)",
        ["Always cis geometry only without chirality", "Only monodentate ligands forbidden", "Only ionic bonds"],
    ),
    q(
        "Linkage isomerism is shown by ambidentate ligands such as:",
        "NO2- (nitro vs nitrito binding)",
        ["NH3 only", "H2O only", "Cl- only"],
    ),
    q(
        "Coordination isomerism occurs when:",
        "Ligands are exchanged between cationic and anionic complex ions",
        ["Only ionisation isomers differ in ionisable groups", "Only optical activity in ethanol", "Only chain length in polymer"],
    ),
    q(
        "Strong field ligands cause:",
        "Large crystal field splitting (high Delta)",
        ["Zero splitting always", "Only ionic bonding without orbitals", "Only paramagnetism always regardless of electrons"],
    ),
    q(
        "Ionisation isomerism example:",
        "[Co(NH3)5Br]SO4 vs [Co(NH3)5SO4]Br",
        ["[Co(NH3)6]Cl3 vs [CoCl(NH3)5]Cl2 only as ionisation pair always", "Cis-trans only", "Optical only"],
    ),
]

# ---------------------------------------------------------------------------
# Haloalkanes and Haloarenes
# ---------------------------------------------------------------------------

BANK_HALO_CLASS_NOM: QuestionBank = [
    q(
        "General formula of alkyl halide (haloalkane) is:",
        "R-X",
        ["Ar-X only always", "R-OH", "R-COOH"],
    ),
    q(
        "In CH3CHBrCH3, the bromine is on a carbon bonded to one other carbon; this is a:",
        "Secondary (2°) alkyl halide",
        ["Primary alkyl halide", "Tertiary alkyl halide", "Vinyl halide"],
    ),
    q(
        "IUPAC name of CH3CH2CH2Cl is:",
        "1-chloropropane",
        ["Chloropropane without locant always", "3-chloropropane", "Propyl chloride only (common name not IUPAC)"],
    ),
    q(
        "C6H5Cl is classified as:",
        "Haloarene (aryl halide)",
        ["Allylic halide", "Vinyl halide", "Geminal dihalide"],
    ),
    q(
        "Allylic halide has C-X bond on carbon:",
        "Adjacent to C=C double bond",
        ["Directly on sp2 C of double bond (vinylic)", "Only on benzene ring", "Only on quaternary carbon"],
    ),
    q(
        "Geminal dihalide has two halogens on:",
        "Same carbon atom",
        ["Adjacent carbons always (vicinal)", "Terminal carbons only of chain", "Only aromatic ring without alkyl"],
    ),
    q(
        "Vicinal dihalide has halogens on:",
        "Adjacent carbon atoms",
        ["Same carbon always", "Para positions on benzene only", "Only primary carbons separated by two bonds"],
    ),
    q(
        "Common name tert-butyl chloride corresponds to IUPAC:",
        "2-chloro-2-methylpropane",
        ["1-chlorobutane", "Chloromethylpropane without locant", "4-chloro-2-methylpropane"],
    ),
]

BANK_CX_BOND: QuestionBank = [
    q(
        "C-X bond length among halogens increases in order:",
        "C-F < C-Cl < C-Br < C-I",
        ["C-I < C-F < C-Cl", "All equal", "C-Cl < C-F < C-I"],
    ),
    q(
        "C-X bond enthalpy (strength) generally decreases:",
        "From C-F to C-I",
        ["From C-I to C-F", "Remains constant", "Only depends on solvent"],
    ),
    q(
        "C-X bond in haloalkanes is:",
        "Polar covalent with partial positive carbon",
        ["Purely ionic always", "Non-polar always", "Metallic"],
    ),
    q(
        "Reactivity of alkyl halides toward SN2 in typical order (same alkyl group) is:",
        "RI > RBr > RCl > RF (weaker bond, better leaving group for I)",
        ["RF > RCl > RBr > RI always in all media", "All identical", "Only RF reacts ever"],
    ),
    q(
        "In C-X bond, which halogen gives most polar bond with carbon?",
        "Fluorine",
        ["Iodine", "Bromine only without F", "Astatine in all textbooks data"],
    ),
    q(
        "Bond polarity of C-X decreases down the group mainly because:",
        "Electronegativity difference between C and X decreases",
        ["Atomic number of carbon changes", "X becomes more electronegative down group", "Mass of carbon increases"],
    ),
    q(
        "In haloarenes, C-Cl bond has partial double bond character due to:",
        "Resonance between lone pair on Cl and benzene ring",
        ["Only ionic attraction", "Only hyperconjugation in alkyl only", "Absence of pi system"],
    ),
    q(
        "Which statement about C-X bond in vinyl chloride (CH2=CHCl) is correct?",
        "C-Cl bond is shorter and stronger than in CH3CH2Cl partly due to sp2 carbon and resonance",
        ["Weaker than tertiary alkyl chloride always", "Purely ionic", "Cannot undergo any substitution ever under any condition"],
    ),
]

BANK_HALO_REACTIONS: QuestionBank = [
    q(
        "SN2 mechanism is characterised by:",
        "Backside attack and inversion of configuration at chiral carbon",
        ["Carbocation intermediate always", "Racemisation always", "Only tertiary halides"],
    ),
    q(
        "SN1 reaction rate depends on:",
        "Concentration of alkyl halide only (first order)",
        ["Concentration of nucleophile only", "Both halide and nucleophile first order always", "Neither concentration"],
    ),
    q(
        "Tertiary alkyl halides favour SN1 in polar protic solvents because:",
        "Stable tertiary carbocation forms",
        ["Steric hindrance favours SN2", "No leaving group ability", "Always elimination only"],
    ),
    q(
        "Alcoholic KOH with alkyl halide mainly promotes:",
        "Elimination (dehydrohalogenation) to alkene",
        ["Substitution to ether always", "Addition to double bond", "Polymerisation of halide alone"],
    ),
    q(
        "Wurtz reaction couples two alkyl halides using:",
        "Sodium metal in dry ether",
        ["Alcoholic KOH", "Zn/HCl", "Aqueous AgNO3"],
    ),
    q(
        "Finkelstein reaction exchanges halogen using:",
        "NaI in acetone (SN2, NaX precipitates for Cl/Br)",
        ["Conc. H2SO4 only", "Only LiAlH4", "Only Br2 in CCl4"],
    ),
    q(
        "Saytzeff rule predicts:",
        "Major alkene is the more substituted one in elimination",
        ["Least substituted alkene always", "Only anti addition product", "Only Markovnikov alcohol"],
    ),
    q(
        "Haloarenes are less reactive toward nucleophilic substitution than haloalkanes mainly due to:",
        "C-X partial double bond character and resonance stabilisation",
        ["Stronger C-X ionic character only", "Higher leaving group ability of F in arenes", "Absence of pi electrons in ring"],
    ),
]

# ---------------------------------------------------------------------------
# Alcohols, Phenols and Ethers
# ---------------------------------------------------------------------------

BANK_ALC_CLASS: QuestionBank = [
    q(
        "Primary alcohol has -OH attached to carbon bonded to:",
        "One other carbon (or none in methanol)",
        ["Two other carbons", "Three other carbons", "Aromatic ring only"],
    ),
    q(
        "CH3CH(OH)CH3 is a:",
        "Secondary alcohol",
        ["Primary alcohol", "Tertiary alcohol", "Phenol"],
    ),
    q(
        "Phenol (C6H5OH) differs from alcohols because:",
        "OH is directly attached to sp2 hybridised carbon of benzene ring",
        ["It has no OH group", "It is always a gas", "It cannot form hydrogen bonds"],
    ),
    q(
        "Tertiary alcohol example is:",
        "(CH3)3COH",
        ["CH3CH2OH", "CH3CH2CH2OH", "C6H5OH only without others"],
    ),
    q(
        "Ethers have general formula:",
        "R-O-R'",
        ["R-COOH", "R-CHO", "R-NH2"],
    ),
    q(
        "Diethyl ether is classified as:",
        "Simple symmetrical ether",
        ["Mixed unsymmetrical ether only", "Phenol", "Carboxylic acid"],
    ),
    q(
        "Allylic alcohol has OH on carbon:",
        "Adjacent to C=C",
        ["On sp2 carbon of C=C (vinylic alcohol)", "On benzene ring", "On quaternary carbon only"],
    ),
    q(
        "Which is a polyhydric alcohol?",
        "Ethane-1,2-diol (glycol)",
        ["Methanol only", "Diethyl ether", "Benzene"],
    ),
]

BANK_ALC_PREP: QuestionBank = [
    q(
        "Acid-catalysed hydration of alkene gives alcohol following:",
        "Markovnikov addition of water",
        ["Anti-Markovnikov always without peroxide", "Only phenol", "Only ether always"],
    ),
    q(
        "Hydroboration-oxidation of alkene gives alcohol with:",
        "Anti-Markovnikov regiochemistry",
        ["Markovnikov alcohol always", "Only ketone", "Only alkane"],
    ),
    q(
        "Grignard reagent (RMgX) with formaldehyde followed by hydrolysis gives:",
        "Primary alcohol",
        ["Tertiary alcohol always", "Phenol only", "Carboxylic acid directly without CO2"],
    ),
    q(
        "Grignard with ketone R2CO gives after hydrolysis:",
        "Tertiary alcohol",
        ["Primary alcohol", "Aldehyde", "Ester directly"],
    ),
    q(
        "Industrial preparation of ethanol by fermentation uses:",
        "Enzymes from yeast converting sugars",
        ["Only electrolysis of brine", "Only Wurtz reaction", "Only Rosenmund reduction"],
    ),
    q(
        "Phenol is industrially prepared from cumene via:",
        "Cumene hydroperoxide route (oxidation to phenol and acetone)",
        ["Direct hydration of benzene with water at room temperature", "Fermentation of glucose", "Ozonolysis of ethyne only"],
    ),
    q(
        "Williamson ether synthesis involves:",
        "SN2 reaction of alkoxide ion with primary alkyl halide",
        ["Electrophilic substitution on benzene with OH", "Polymerisation of ethene", "Cannizzaro reaction"],
    ),
    q(
        "Reduction of aldehyde with NaBH4 gives:",
        "Primary alcohol",
        ["Secondary alcohol always", "Ketone", "Carboxylic acid without protonation"],
    ),
]

BANK_ALC_PROPS: QuestionBank = [
    q(
        "Lucas test distinguishes alcohols using:",
        "Anhydrous ZnCl2 and conc. HCl (cloudiness/turbidity rate)",
        ["Tollens' reagent", "Fehling's solution", "I2/NaOH haloform only for all alcohols"],
    ),
    q(
        "Tertiary alcohol reacts fastest in Lucas test because:",
        "SN1 formation of stable carbocation is easy",
        ["SN2 is fastest for tertiary", "No reaction occurs for tertiary", "Only phenol reacts"],
    ),
    q(
        "Acid-catalysed dehydration of alcohol gives:",
        "Alkene (more substituted by Saytzeff)",
        ["Only ether at all temperatures without exception", "Alkane always", "Aldehyde directly always"],
    ),
    q(
        "Phenol is more acidic than ethanol mainly due to:",
        "Resonance stabilisation of phenoxide ion",
        ["Higher molecular mass only", "Absence of hydrogen bonding", "sp3 carbon bearing OH"],
    ),
    q(
        "Esterification of alcohol with carboxylic acid is catalysed by:",
        "Conc. H2SO4 (acid catalyst)",
        ["Only Na metal", "Only LiAlH4", "Only Br2/Fe"],
    ),
    q(
        "Reimer-Tiemann reaction converts phenol to:",
        "Salicylaldehyde (o-hydroxybenzaldehyde)",
        ["Benzoic acid", "Aniline", "Nitrobenzene"],
    ),
    q(
        "Hydrogen bonding causes boiling point of ethanol to be:",
        "Higher than diethyl ether of similar mass",
        ["Lower than methane", "Equal to ethane", "Lower than all hydrocarbons without exception including C20"],
    ),
    q(
        "Phenol gives violet colour with neutral FeCl3 due to:",
        "Formation of coloured complex with phenol",
        ["Only oxidation to quinone always required first", "Only NaOH test", "Only iodoform"],
    ),
]

# ---------------------------------------------------------------------------
# Aldehydes, Ketones and Carboxylic Acids
# ---------------------------------------------------------------------------

BANK_CARBONYL: QuestionBank = [
    q(
        "Carbonyl carbon in aldehydes and ketones is:",
        "sp2 hybridised and electrophilic",
        ["sp3 and nucleophilic only", "Linear with sp hybridisation", "Always tetrahedral without pi bond"],
    ),
    q(
        "Aldehydes are generally more reactive than ketones toward nucleophilic addition because:",
        "Less steric hindrance and less +I effect from alkyl groups",
        ["Ketones have no C=O bond", "Aldehydes cannot form hydrates", "Ketones always have leaving groups"],
    ),
    q(
        "Tollens' test (ammoniacal AgNO3) is positive for:",
        "Aldehydes (silver mirror)",
        ["Ketones generally", "Ethers", "Saturated hydrocarbons"],
    ),
    q(
        "Fehling's solution tests for:",
        "Aliphatic aldehydes (red Cu2O precipitate on heating)",
        ["Aromatic aldehydes always equally fast without exception", "Ketones generally", "Amines only"],
    ),
    q(
        "Nucleophilic addition to C=O begins with attack at:",
        "Carbonyl carbon",
        ["Carbonyl oxygen only permanently", "Alpha carbon always first", "Beta carbon only"],
    ),
    q(
        "Acetal formation from aldehyde/ketone requires:",
        "Two equivalents of alcohol and acid catalyst",
        ["Only one mole water added", "Only base without alcohol", "Only hydrogen gas"],
    ),
    q(
        "Which gives positive iodoform test?",
        "Ethanal (acetaldehyde) and methyl ketones",
        ["Benzaldehyde only", "All ketones without methyl group", "All carboxylic acids"],
    ),
    q(
        "Cyanohydrin formation uses:",
        "HCN (or KCN then acid) adding to carbonyl",
        ["Only NaBH4", "Only O3", "Only Br2 water"],
    ),
]

BANK_CARBOXYLIC_ACIDS: QuestionBank = [
    q(
        "Carboxylic acids show higher boiling points than alcohols of similar mass partly because they form:",
        "Dimers via strong hydrogen bonding",
        ["Only ionic lattices in gas phase", "Only London forces weaker than ethers always", "Only covalent networks like diamond"],
    ),
    q(
        "Acidity of carboxylic acids increases when electron-withdrawing groups are:",
        "Closer to COOH group",
        ["Farther without effect", "Always alkyl groups increase acidity by +I", "Only halogen on beta carbon with no trend"],
    ),
    q(
        "Order of acidity:",
        "HCOOH > CH3COOH > CH3CH2COOH",
        ["CH3CH2COOH > CH3COOH > HCOOH", "All equal", "Ethanol > acetic acid"],
    ),
    q(
        "Carboxylic acids react with NaHCO3 to liberate:",
        "CO2 gas",
        ["H2 always from all organic acids", "Cl2", "NH3"],
    ),
    q(
        "Esterification is reversible; to favour ester product one can:",
        "Remove water or use excess alcohol",
        ["Add large water only", "Use only dilute base", "Cool to absolute zero only without reagents"],
    ),
    q(
        "Decarboxylation of sodium propanoate with soda lime gives:",
        "Ethane",
        ["Methane", "Propane", "Ethene directly always"],
    ),
    q(
        "Hell-Volhard-Zelinsky (HVZ) reaction halogenates:",
        "Alpha position of carboxylic acids",
        ["Beta position only always", "Benzene ring without catalyst", "Terminal methyl only in all acids"],
    ),
    q(
        "Reduction of carboxylic acid to primary alcohol uses:",
        "LiAlH4 (strong reducing agent)",
        ["NaBH4 alone typically ineffective for -COOH", "O3 only", "Br2/Fe only"],
    ),
]

BANK_ALDEHYDE_REACTIONS: QuestionBank = [
    q(
        "Aldol condensation requires:",
        "Aldehydes/ketones with alpha hydrogen and dilute base",
        ["Only aromatic aldehydes without alpha H always succeed", "Only acid without alpha H", "Only ketones without alpha H always"],
    ),
    q(
        "Cannizzaro reaction is shown by:",
        "Aldehydes without alpha hydrogen (e.g. HCHO, C6H5CHO)",
        ["Acetaldehyde primarily", "All ketones", "All carboxylic acids"],
    ),
    q(
        "Clemmensen reduction converts C=O to CH2 using:",
        "Zn-Hg amalgam and conc. HCl",
        ["LiAlH4 in ether only for all carbonyls without distinction", "O3", "NaOH only"],
    ),
    q(
        "Wolff-Kishner reduction uses:",
        "Hydrazine and strong base with heat (C=O to CH2)",
        ["Zn-Hg/HCl", "H2/Pd only at RTP without heat", "Br2 water"],
    ),
    q(
        "Cross aldol between benzaldehyde and acetaldehyde often gives:",
        "Mixed condensation products; benzaldehyde lacks alpha H so self-aldol of acetaldehyde or crossed products",
        ["Only Cannizzaro of both", "Only polymer of benzene", "Only methane"],
    ),
    q(
        "Oxidation of aldehyde with Tollens' or Fehling's converts RCHO to:",
        "RCOOH (carboxylate under basic Fehling's conditions)",
        ["RCH3 always", "R-O-R", "RCl"],
    ),
    q(
        "Baeyer-Villiger oxidation converts ketone to:",
        "Ester (migration of group to oxygen)",
        ["Aldehyde always", "Alkane only", "Carboxylic acid without rearrangement"],
    ),
    q(
        "Stephen reduction converts nitrile to aldehyde using:",
        "SnCl2 and HCl (partial reduction)",
        ["LiAlH4 to amine always only", "Ozonolysis", "Fermentation"],
    ),
]

# ---------------------------------------------------------------------------
# Amines
# ---------------------------------------------------------------------------

BANK_AMINE_CLASS: QuestionBank = [
    q(
        "Primary amine has general formula:",
        "RNH2",
        ["R2NH", "R3N", "R-O-NH2 only as primary always"],
    ),
    q(
        "Aniline (C6H5NH2) is a:",
        "Primary aromatic amine",
        ["Secondary amine", "Tertiary amine", "Nitro compound"],
    ),
    q(
        "(CH3)3N is a:",
        "Tertiary amine",
        ["Primary amine", "Secondary amine", "Amide"],
    ),
    q(
        "Secondary amine has formula:",
        "R2NH",
        ["RNH2", "R3N", "RCONH2"],
    ),
    q(
        "Basicity of amines in aqueous solution is influenced by:",
        "+I effect, solvation, and steric hindrance",
        ["Only molecular mass", "Only colour", "Only aromatic ring without electronic effects"],
    ),
    q(
        "Aliphatic amines are generally more basic than ammonia because:",
        "Alkyl groups donate electron density toward nitrogen",
        ["Alkyl groups withdraw electrons strongly", "They cannot accept H+", "They are always neutral"],
    ),
    q(
        "Aniline is less basic than aliphatic amines primarily because:",
        "Lone pair on N is delocalised into benzene ring",
        ["Nitrogen has no lone pair", "Aniline is always protonated in water fully", "Only steric factor without resonance"],
    ),
    q(
        "Quaternary ammonium salt has nitrogen with:",
        "Four covalent bonds and positive charge (R4N+)",
        ["Three bonds only always neutral", "No nitrogen atom", "Only ionic Na+ and Cl- without N"],
    ),
]

BANK_AMINE_PREP: QuestionBank = [
    q(
        "Reduction of nitrobenzene with Sn/HCl or Fe/HCl gives:",
        "Aniline",
        ["Nitrosobenzene only as final product always", "Benzoic acid", "Azoxybenzene only without further reduction"],
    ),
    q(
        "Gabriel phthalimide synthesis prepares:",
        "Primary amines only (no secondary/tertiary via same route simply)",
        ["Tertiary amines directly always", "Nitro compounds", "Diazonium salts directly as stable product at RTP"],
    ),
    q(
        "Hoffmann bromamide degradation converts amide to amine with:",
        "One fewer carbon (migration from carbonyl carbon)",
        ["One more carbon always", "No change in carbon count ever", "Direct conversion to nitrile without steps"],
    ),
    q(
        "Reductive amination converts carbonyl to amine using:",
        "NH3 or amine with H2/Ni or NaBH3CN type reducing conditions",
        ["Only O3", "Only Br2 water", "Only HVZ reagents"],
    ),
    q(
        "Alkylation of ammonia with excess alkyl halide tends to give:",
        "Mixture of primary, secondary, tertiary amines and quaternary salt",
        ["Only primary amine always in one step uncontrollably stopped", "Only tertiary always first", "No reaction"],
    ),
    q(
        "Preparation of aniline from chlorobenzene at high T with NaOH is:",
        "Not standard lab route; reduction of nitrobenzene is common CBSE route",
        ["Same as Gabriel synthesis", "Same as Sandmeyer only", "Direct SN2 at RTP in water instantly"],
    ),
    q(
        "Hydrolysis of nitrile (RCN) with LiAlH4 gives:",
        "Primary amine RCH2NH2",
        ["Carboxylic acid only with LiAlH4", "Tertiary amine always", "Aldehyde without reduction"],
    ),
    q(
        "Ammonolysis of alkyl halides is:",
        "SN2 substitution giving alkyl amine (further alkylation possible)",
        ["Electrophilic aromatic substitution", "Free radical halogenation", "Polymerisation of ammonia only"],
    ),
]

BANK_DIAZONIUM: QuestionBank = [
    q(
        "Benzenediazonium chloride is prepared from aniline at:",
        "0-5°C with NaNO2 and dilute HCl",
        ["100°C with conc. H2SO4 only", "Room temperature without cooling always stable days", "Direct from nitrobenzene without reduction"],
    ),
    q(
        "Diazonium salts are unstable above about 5-10°C because they:",
        "Decompose (often losing N2)",
        ["Become more stable polymers", "Convert to benzene irreversibly without N2 loss only", "Precipitate as gold mirrors"],
    ),
    q(
        "Coupling of benzenediazonium ion with phenol in alkaline medium gives:",
        "Orange-red azo dye",
        ["Silver mirror", "Chlorobenzene only", "Benzoic acid directly"],
    ),
    q(
        "Sandmeyer reaction replaces diazonium group with Cl or Br using:",
        "CuCl or CuBr",
        ["Only Na metal in ether", "Only LiAlH4", "Only O3"],
    ),
    q(
        "Gattermann reaction uses:",
        "Cu powder/HCl or HBr instead of CuCl/CuBr for halogen replacement",
        ["Zn-Hg only", "Fehling's solution", "Tollens' only"],
    ),
    q(
        "When diazonium salt reacts with water (warm), product is:",
        "Phenol",
        ["Aniline again", "Nitrobenzene", "Benzene without OH"],
    ),
    q(
        "Diazonium group (-N2+) is a good leaving group because:",
        "Very stable N2 gas forms",
        ["It is a strong nucleophile always", "It adds across double bonds only", "It never leaves"],
    ),
    q(
        "Azo compounds contain functional group:",
        "-N=N- linking two aromatic rings typically",
        ["-N=N=O only always", "-CO-NH- only", "-O-O- peroxide only"],
    ),
]

# ---------------------------------------------------------------------------
# Biomolecules
# ---------------------------------------------------------------------------

BANK_CARBOHYDRATES: QuestionBank = [
    q(
        "General formula of many monosaccharides is:",
        "(CH2O)n (hydrates of carbon)",
        ["CnH2n only always without oxygen", "Only (CH2)n", "Only amino acid formula"],
    ),
    q(
        "Glucose and fructose are:",
        "Monosaccharides (hexoses) and functional isomers (aldose vs ketose)",
        ["Disaccharides always", "Polysaccharides", "Only lipids"],
    ),
    q(
        "Sucrose is a non-reducing sugar because:",
        "Anomeric carbon atoms of both units are involved in glycosidic linkage (no free -CHO/-hemiacetal)",
        ["It has no OH groups", "It is a protein", "It cannot hydrolyse"],
    ),
    q(
        "Maltose gives two glucose units on hydrolysis and is:",
        "Reducing sugar (free anomeric hemiacetal on one glucose)",
        ["Non-reducing like sucrose always", "A polysaccharide", "An amino acid"],
    ),
    q(
        "Starch contains polymers of glucose with linkage:",
        "alpha-glycosidic (amylose/amylopectin)",
        ["Only beta-glycosidic like cellulose exclusively", "Peptide bonds", "Ester linkages only"],
    ),
    q(
        "Cellulose differs from starch because cellulose has:",
        "beta-1,4-glycosidic linkages between glucose units",
        ["alpha-1,4 only like amylose exclusively", "Only fructose units", "Only triple bonds"],
    ),
    q(
        "Anomeric carbon in cyclic glucose is:",
        "Carbon-1 (originally carbonyl in open chain)",
        ["Carbon-6 only always", "Any carbon without definition", "Carbon in benzene ring"],
    ),
    q(
        "Fehling's test positive result indicates:",
        "Reducing sugar (or aldehyde) present",
        ["Protein only", "Only saturated fat", "Only nucleic acid"],
    ),
]

BANK_PROTEINS: QuestionBank = [
    q(
        "Proteins are polymers of:",
        "Alpha-amino acids linked by peptide bonds",
        ["Monosaccharides only", "Fatty acids only", "Nucleotides only without amino acids"],
    ),
    q(
        "Peptide bond (-CO-NH-) is formed by:",
        "Condensation between -COOH of one amino acid and -NH2 of another",
        ["Oxidation of side chains only", "Hydrogenation of C=C in backbone", "Only ionic attraction"],
    ),
    q(
        "Primary structure of protein refers to:",
        "Sequence of amino acids in polypeptide chain",
        ["Alpha helix folding only", "Quaternary association of four subunits only", "Only disulphide count without sequence"],
    ),
    q(
        "Alpha helix is an example of:",
        "Secondary structure stabilised by hydrogen bonds along backbone",
        ["Primary structure", "Only quaternary structure", "Only random coil without H-bonds ever"],
    ),
    q(
        "Denaturation of protein involves:",
        "Loss of secondary/tertiary/quaternary structure without breaking peptide bonds usually",
        ["Hydrolysis of all peptide bonds always first step", "Conversion to glucose", "Only increase in primary structure sequence change"],
    ),
    q(
        "Biuret test detects:",
        "Proteins/peptides (peptide bonds) — violet colour with Cu2+ in alkaline medium",
        ["Only reducing sugars", "Only lipids", "Only DNA bases without protein"],
    ),
    q(
        "Disulphide bridges (-S-S-) stabilise protein structure between:",
        "Cysteine side chains",
        ["Glycine only always", "Carboxyl groups only", "Aromatic rings only without sulfur"],
    ),
    q(
        "Enzymes are biological catalysts made largely of:",
        "Protein (with specific active site)",
        ["Only DNA", "Only starch", "Only inorganic salts without protein ever"],
    ),
]

BANK_NUCLEIC_VITAMINS: QuestionBank = [
    q(
        "DNA nucleotides contain bases:",
        "Adenine, guanine, cytosine, thymine",
        ["Uracil instead of thymine", "Only A and G", "Only cytosine and uracil"],
    ),
    q(
        "Complementary base pairing in DNA is:",
        "A with T (2 H-bonds), G with C (3 H-bonds)",
        ["A with G always", "T with C always", "U with A in DNA double helix"],
    ),
    q(
        "RNA differs from DNA in that RNA has:",
        "Ribose sugar and uracil instead of thymine (generally single stranded)",
        ["Deoxyribose and thymine always double stranded only", "No phosphate groups", "Only protein backbone"],
    ),
    q(
        "A nucleotide consists of:",
        "Base + pentose sugar + phosphate group",
        ["Only base and sugar without phosphate always", "Only amino acid", "Only fatty acid and glycerol"],
    ),
    q(
        "Vitamin C is:",
        "Water-soluble vitamin (ascorbic acid)",
        ["Fat-soluble vitamin D only class", "Only stored in liver as retinol", "A mineral not vitamin"],
    ),
    q(
        "Deficiency of vitamin D in children causes:",
        "Rickets",
        ["Scurvy", "Beriberi", "Night blindness from vitamin A only confusion as D symptom"],
    ),
    q(
        "Vitamin B complex vitamins are generally:",
        "Water-soluble",
        ["Fat-soluble like A,D,E,K all", "Only synthesized in skin by UV", "Only stored in adipose without excretion ever"],
    ),
    q(
        "Hydrogen bonding between complementary strands stabilises:",
        "DNA double helix structure",
        ["Only primary protein sequence", "Only glycogen granules without base pairing", "Only saturated hydrocarbon chains"],
    ),
]

# ---------------------------------------------------------------------------
# Chapter-topic banks (colliding titles across chapters)
# ---------------------------------------------------------------------------

CHAPTER_TOPIC_BANKS: dict[tuple[str, str], QuestionBank] = {
    ("Alcohols, Phenols and Ethers", "Preparation"): BANK_ALC_PREP,
    ("Amines", "Preparation"): BANK_AMINE_PREP,
    ("Alcohols, Phenols and Ethers", "Classification"): BANK_ALC_CLASS,
}


def register() -> None:
    """Register all Class 12 Chemistry concept banks."""
    from app.data.quiz_concepts import GLOBAL_CHAPTER_TOPIC_BANKS

    register_keys(["Types of solutions"], BANK_SOLUTION_TYPES)
    register_keys(["Concentration terms"], BANK_CONCENTRATION_TERMS)
    register_keys(["Colligative properties"], BANK_COLLIGATIVE)

    register_keys(["Electrochemical cells"], BANK_ELECTROCHEMICAL_CELLS)
    register_keys(["Nernst equation"], BANK_NERNST)
    register_keys(["Electrolysis and conductance"], BANK_ELECTROLYSIS_CONDUCTANCE)

    register_keys(["Rate of a reaction"], BANK_RATE_OF_REACTION)
    register_keys(["Factors affecting rate"], BANK_FACTORS_AFFECTING_RATE)
    register_keys(["Integrated rate equations"], BANK_INTEGRATED_RATE)

    register_keys(["Transition elements"], BANK_TRANSITION_ELEMENTS)
    register_keys(["Lanthanoids"], BANK_LANTHANOIDS)
    register_keys(["Important compounds"], BANK_IMPORTANT_COMPOUNDS_D_BLOCK)

    register_keys(["Werner's theory"], BANK_WERNERS_THEORY)
    register_keys(["Nomenclature"], BANK_COORD_NOMENCLATURE)
    register_keys(["Bonding and isomerism"], BANK_BONDING_ISOMERISM)

    register_keys(["Classification and nomenclature"], BANK_HALO_CLASS_NOM)
    register_keys(["Nature of C–X bond", "Nature of C-X bond"], BANK_CX_BOND)
    register_keys(["Reactions"], BANK_HALO_REACTIONS)

    # "Classification" and "Preparation" for Alcohols/Amines live in CHAPTER_TOPIC_BANKS only.
    register_keys(["Properties and reactions"], BANK_ALC_PROPS)

    register_keys(["Carbonyl compounds"], BANK_CARBONYL)
    register_keys(["Carboxylic acids"], BANK_CARBOXYLIC_ACIDS)
    register_keys(["Important reactions"], BANK_ALDEHYDE_REACTIONS)

    register_keys(["Classification of amines"], BANK_AMINE_CLASS)
    register_keys(["Diazonium salts"], BANK_DIAZONIUM)

    register_keys(["Carbohydrates"], BANK_CARBOHYDRATES)
    register_keys(["Proteins"], BANK_PROTEINS)
    register_keys(["Nucleic acids and vitamins"], BANK_NUCLEIC_VITAMINS)

    GLOBAL_CHAPTER_TOPIC_BANKS.update(CHAPTER_TOPIC_BANKS)

    register_subject_keywords(
        "CHEM",
        [
            (("colligative", "vant hoff", "raoult", "osmotic pressure", "elevation in boiling"), BANK_COLLIGATIVE),
            (("molarity", "molality", "mole fraction", "ppm", "normality"), BANK_CONCENTRATION_TERMS),
            (("homogeneous mixture", "saturated solution", "henry's law"), BANK_SOLUTION_TYPES),
            (("nernst", "reaction quotient q", "0.0591"), BANK_NERNST),
            (("galvanic", "daniell cell", "salt bridge", "anode", "cathode"), BANK_ELECTROCHEMICAL_CELLS),
            (("kohlrausch", "molar conductance", "electrolysis", "faraday"), BANK_ELECTROLYSIS_CONDUCTANCE),
            (("rate constant", "order of reaction", "rate law", "instantaneous rate"), BANK_RATE_OF_REACTION),
            (("arrhenius", "activation energy", "collision theory", "catalyst"), BANK_FACTORS_AFFECTING_RATE),
            (("half-life", "integrated rate", "first order", "zero order"), BANK_INTEGRATED_RATE),
            (("lanthanoid contraction", "4f", "cerium"), BANK_LANTHANOIDS),
            (("kmno4", "k2cr2o7", "interstitial compound"), BANK_IMPORTANT_COMPOUNDS_D_BLOCK),
            (("transition element", "variable oxidation", "d-d transition"), BANK_TRANSITION_ELEMENTS),
            (("werner", "primary valence", "secondary valence", "coordination number"), BANK_WERNERS_THEORY),
            (("hexaammine", "ligand", "coordination compound name"), BANK_COORD_NOMENCLATURE),
            (("crystal field", "geometrical isomer", "linkage isomer"), BANK_BONDING_ISOMERISM),
            (("haloalkane", "alkyl halide", "sn1", "sn2", "wurtz"), BANK_HALO_REACTIONS),
            (("c-x bond", "leaving group", "haloarene"), BANK_CX_BOND),
            (("allylic halide", "vicinal dihalide", "haloarene nomenclature"), BANK_HALO_CLASS_NOM),
            (("lucas test", "reimer-tiemann", "phenol acidity", "williamson ether"), BANK_ALC_PROPS),
            (("hydroboration", "grignard", "fermentation ethanol"), BANK_ALC_PREP),
            (("primary alcohol", "secondary alcohol", "diethyl ether"), BANK_ALC_CLASS),
            (("tollens", "fehling", "nucleophilic addition carbonyl", "iodoform"), BANK_CARBONYL),
            (("carboxylic acid dimer", "hvz", "hell-volhard"), BANK_CARBOXYLIC_ACIDS),
            (("aldol", "cannizzaro", "clemmensen", "wolff-kishner"), BANK_ALDEHYDE_REACTIONS),
            (("aniline", "gabriel phthalimide", "hoffmann bromamide"), BANK_AMINE_PREP),
            (("primary amine", "tertiary amine", "quaternary ammonium"), BANK_AMINE_CLASS),
            (("diazonium", "sandmeyer", "azo dye"), BANK_DIAZONIUM),
            (("glycosidic", "reducing sugar", "sucrose", "starch", "cellulose"), BANK_CARBOHYDRATES),
            (("peptide bond", "biuret", "alpha helix", "denaturation"), BANK_PROTEINS),
            (("dna base pairing", "nucleotide", "vitamin c", "vitamin d", "uracil"), BANK_NUCLEIC_VITAMINS),
        ],
    )


__all__ = ["CHAPTER_TOPIC_BANKS", "register"]
