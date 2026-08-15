"""EduQuest CBSE Class 12 Chemistry — additional NCERT-section MCQ banks."""

from __future__ import annotations

from app.data.quiz_banks.common import q, register_keys, register_subject_keywords
from app.data.quiz_concepts import QuestionBank

# ---------------------------------------------------------------------------
# Solutions extras
# ---------------------------------------------------------------------------

BANK_SOLUBILITY_SOLIDS_GASES: QuestionBank = [
    q(
        "According to the general trend, solubility of most solid solutes in water with increasing temperature:",
        "Increases",
        ["Always decreases", "Remains exactly constant for all salts", "Depends only on pressure, not temperature"],
    ),
    q(
        "Solubility of a gas in a liquid at constant temperature decreases when:",
        "Pressure on the gas above the liquid is lowered",
        ["Pressure is increased", "Temperature is lowered slightly", "Solvent is stirred faster only"],
    ),
    q(
        "Which pair best illustrates 'like dissolves like' for non-polar solutes?",
        "Iodine dissolving in carbon tetrachloride",
        ["NaCl dissolving in hexane", "KNO3 dissolving in benzene", "Glucose dissolving in hexane"],
    ),
    q(
        "For a sparingly soluble salt AB(s) <=> A+(aq) + B-(aq), the solubility product Ksp equals:",
        "Product of equilibrium ion concentrations each raised to stoichiometric power",
        ["Sum of ion concentrations", "Molarity of undissolved solid", "Always equal to 1 for any salt"],
    ),
    q(
        "Heating a saturated solution of a gas in a sealed container (constant volume) causes gas solubility to:",
        "Decrease",
        ["Increase always for all gases", "Remain unchanged because pressure is fixed", "Double for every 10 K rise"],
    ),
    q(
        "Which factor does NOT directly change the solubility of a solid in a given liquid solvent?",
        "Colour of the solute crystals",
        ["Temperature", "Nature of solvent", "Common-ion effect for a slightly soluble salt"],
    ),
]

BANK_HENRYS_LAW: QuestionBank = [
    q(
        "Henry's law states that at constant temperature, the partial pressure of a gas over a dilute solution is:",
        "Proportional to its mole fraction in the solution",
        ["Inversely proportional to temperature only", "Independent of concentration", "Equal to its vapour pressure as pure liquid"],
    ),
    q(
        "The mathematical form p = KH x applies when x is:",
        "Mole fraction of the dissolved gas in the liquid phase",
        ["Molality of gas in mol/kg solvent only", "Mass percent of gas", "Normality of gas in all cases"],
    ),
    q(
        "When temperature increases, Henry's law constant KH for a gas in water generally:",
        "Increases",
        ["Decreases", "Becomes zero", "Remains fixed for every gas"],
    ),
    q(
        "Henry's law is used to explain why a sealed soft drink bottle fizzes on opening because:",
        "Decrease in CO2 partial pressure above the liquid lowers dissolved gas concentration",
        ["CO2 becomes more soluble in air", "Temperature rises instantly in the bottle", "Water converts CO2 to carbonate irreversibly"],
    ),
    q(
        "Henry's law is valid for:",
        "Dilute solutions of gases in liquids at moderate pressure",
        ["Concentrated solutions at very high pressure only", "Mixtures of two immiscible liquids", "Solid-solid alloys exclusively"],
    ),
    q(
        "If mole fraction of dissolved O2 in blood is x at a given pO2, doubling pO2 (at same T) makes x approximately:",
        "Double",
        ["Halve", "Unchanged", "Four times only if temperature also doubles"],
    ),
]

BANK_VAPOUR_PRESSURE_LIQUID: QuestionBank = [
    q(
        "Vapour pressure of a pure liquid at a given temperature measures:",
        "Equilibrium pressure of vapour above the liquid in a closed system",
        ["Atmospheric pressure always", "Osmotic pressure of the liquid", "Boiling point elevation directly"],
    ),
    q(
        "Adding a non-volatile solute to a solvent lowers the vapour pressure of the solution because:",
        "Fewer solvent molecules are at the surface available to escape into vapour phase",
        ["Solute molecules increase vapour pressure", "Temperature always drops on mixing", "Solute raises molecular mass of vapour"],
    ),
    q(
        "For a binary liquid solution of two volatile components, total vapour pressure (ideal case) is:",
        "Sum of partial vapour pressures of each component",
        ["Product of individual vapour pressures", "Always equal to vapour pressure of pure solvent", "Independent of composition"],
    ),
    q(
        "Vapour pressure of a liquid increases with temperature because:",
        "More molecules possess energy sufficient to escape into vapour phase",
        ["Molar mass of liquid decreases", "Intermolecular forces strengthen", "Mole fraction of solute increases"],
    ),
    q(
        "At the boiling point of a liquid at 1 atm, its vapour pressure equals:",
        "760 mm Hg (1 atm external pressure)",
        ["Zero always", "Half the atmospheric pressure", "Osmotic pressure of dissolved air only"],
    ),
    q(
        "In a solution, partial vapour pressure of a volatile component A is given by Raoult's law as:",
        "pA = pA° xA",
        ["pA = KH xA for every component", "pA = pA° / xA", "pA = iCRT"],
    ),
]

BANK_RAOULTS_LAW: QuestionBank = [
    q(
        "Raoult's law for a component in an ideal liquid solution states:",
        "Partial vapour pressure equals mole fraction times vapour pressure of pure component",
        ["Total pressure equals sum of pure vapour pressures always doubled", "Partial pressure is independent of composition", "Only applies to non-volatile solutes exclusively"],
    ),
    q(
        "For a binary ideal solution of two volatile liquids, a plot of total vapour pressure versus mole fraction of one component is:",
        "Approximately linear between pure-component vapour pressures",
        ["Always a horizontal line", "Always concave downward only for all pairs", "Independent of intermolecular forces"],
    ),
    q(
        "Raoult's law for a non-volatile solute in solvent gives relative lowering (p° - p)/p° equal to:",
        "Mole fraction of solute",
        ["Molality of solvent", "Van't Hoff factor only", "Elevation in boiling point directly"],
    ),
    q(
        "A solution showing positive deviation from Raoult's law has:",
        "A-A and B-B interactions stronger than A-B interactions",
        ["A-B interactions stronger than A-A and B-B", "No vapour phase", "Zero vapour pressure at all compositions"],
    ),
    q(
        "For component B in an ideal binary liquid mixture, pB equals:",
        "pB° xB",
        ["pB° / xB", "pA° xA always", "KH xB for gases only"],
    ),
    q(
        "Raoult's law breaks down most noticeably when:",
        "Components associate or dissociate strongly in solution",
        ["Both components are ideal gases", "Solute is completely non-volatile at all temperatures", "Mole fractions sum to unity"],
    ),
]

BANK_IDEAL_NON_IDEAL: QuestionBank = [
    q(
        "An ideal solution is characterized by:",
        "Delta H_mix = 0 and components obey Raoult's law over entire composition range",
        ["Large positive Delta H_mix only", "Formation of maximum-boiling azeotrope always", "Complete immiscibility of components"],
    ),
    q(
        "A solution with positive deviation from Raoult's law boils:",
        "At lower temperature than predicted for ideal behaviour at same composition",
        ["Always at higher temperature than either pure component", "Only when non-volatile solute is present", "Never forms vapour phase"],
    ),
    q(
        "Negative deviation from Raoult's law implies:",
        "Stronger interactions between unlike molecules than between like molecules",
        ["Weaker A-B interactions than A-A and B-B", "No change in total vapour pressure", "Only colligative properties are affected"],
    ),
    q(
        "A minimum-boiling azeotrope forms in a non-ideal mixture when:",
        "Positive deviation is large enough that vapour composition equals liquid at a specific composition",
        ["Negative deviation is absent", "Both components are non-volatile", "Osmotic pressure equals vapour pressure"],
    ),
    q(
        "Ethanol-water mixture near ~95% ethanol shows azeotropic behaviour because the solution:",
        "Deviates strongly from Raoult's law due to hydrogen bonding",
        ["Is strictly ideal at all compositions", "Contains only non-volatile solute", "Has zero vapour pressure"],
    ),
    q(
        "For a maximum-boiling azeotrope, total vapour pressure is:",
        "Lower than expected from Raoult's law due to negative deviation",
        ["Higher than either pure component vapour pressure sum", "Zero at the azeotropic composition", "Equal to osmotic pressure"],
    ),
]

BANK_RELATIVE_LOWERING_VP: QuestionBank = [
    q(
        "Relative lowering of vapour pressure is defined as:",
        "(p° - p) / p°",
        ["p / p° only", "Delta Tb / Kb", "pi / CRT"],
    ),
    q(
        "For a non-volatile solute in solvent, relative lowering equals mole fraction of solute. This shows the property is:",
        "Colligative",
        ["Dependent on chemical nature of solute only", "Independent of particle number", "Always zero for electrolytes"],
    ),
    q(
        "If mole fraction of solute is 0.10 in a binary solution with non-volatile solute, relative lowering is:",
        "0.10",
        ["0.90", "1.10", "0.01 always"],
    ),
    q(
        "Relative lowering of vapour pressure for a given mole fraction of non-volatile solute is independent of:",
        "Identity of the solute (for same mole fraction of particles)",
        ["Temperature of measurement", "Presence of solvent vapour", "Total number of moles in solution"],
    ),
    q(
        "For 1 mol non-volatile solute in 9 mol water, relative lowering (approximate, ideal) is:",
        "0.10",
        ["0.90", "0.01", "1.00"],
    ),
    q(
        "Measuring relative lowering of vapour pressure can be used to determine:",
        "Molar mass of non-volatile solute",
        ["Crystal field splitting", "Rate constant of reaction", "Standard electrode potential only"],
    ),
]

BANK_ELEVATION_BOILING: QuestionBank = [
    q(
        "Elevation in boiling point Delta Tb is related to molality by:",
        "Delta Tb = Kb m i",
        ["Delta Tb = Kf m", "Delta Tb = pi / CRT", "Delta Tb = Kb / m"],
    ),
    q(
        "Ebullioscopic constant Kb for water is approximately 0.512 K kg mol-1. Its units show Kb relates:",
        "Temperature rise per molal concentration of particles",
        ["Pressure change per molarity", "Volume change per mole fraction", "Osmotic pressure per degree"],
    ),
    q(
        "For the same molal concentration, which aqueous solution gives the largest Delta Tb?",
        "CaCl2 (i approx 3)",
        ["Glucose (i = 1)", "Urea (i = 1)", "Sucrose (i = 1)"],
    ),
    q(
        "Boiling point elevation occurs because adding non-volatile solute:",
        "Lowers vapour pressure so higher temperature is needed to reach external pressure",
        ["Raises vapour pressure above 1 atm", "Increases freezing point simultaneously", "Removes solvent molecules from liquid entirely"],
    ),
    q(
        "If Delta Tb = 0.512 K for a non-electrolyte in water, molality is approximately:",
        "1 m",
        ["0.1 m", "2 m", "0.512 m exactly always"],
    ),
    q(
        "Which is an application of boiling point elevation?",
        "Determining molar mass of a polymer from Delta Tb measurement",
        ["Measuring radioactivity of actinoids", "Calculating lattice energy of NaCl crystal", "Finding half-life of first-order reaction"],
    ),
]

BANK_DEPRESSION_FREEZING: QuestionBank = [
    q(
        "Depression in freezing point Delta Tf is given by:",
        "Delta Tf = Kf m i",
        ["Delta Tf = Kb m i", "Delta Tf = pi / iCRT", "Delta Tf = Kf / m"],
    ),
    q(
        "Cryoscopic constant Kf for water is about 1.86 K kg mol-1. Adding 1 molal glucose (i=1) lowers freezing point by about:",
        "1.86 K",
        ["0.512 K", "3.72 K", "0 K"],
    ),
    q(
        "Antifreeze (ethylene glycol) in car radiators works primarily by:",
        "Depressing the freezing point of the coolant",
        ["Raising boiling point only with no effect on freezing", "Increasing vapour pressure of water", "Catalysing corrosion"],
    ),
    q(
        "For equal molal concentrations, NaCl depresses freezing point more than glucose because:",
        "NaCl produces more particles in solution (i > 1)",
        ["NaCl is non-polar", "Glucose dissociates into three ions", "Glucose has higher molar mass only"],
    ),
    q(
        "At the freezing point of a solution, which equilibrium holds?",
        "Solid solvent in equilibrium with solution having same chemical potential as solid",
        ["Only vapour-liquid equilibrium", "Gas dissolves according to Henry's law exclusively", "Solute precipitates as pure solid always"],
    ),
    q(
        "If observed Delta Tf is twice that expected for a non-electrolyte at same molality, van't Hoff factor i is:",
        "2",
        ["0.5", "1", "3 always"],
    ),
]

BANK_OSMOTIC_PRESSURE: QuestionBank = [
    q(
        "Osmotic pressure pi of a dilute solution is given by:",
        "pi = i C R T",
        ["pi = Kb m", "pi = p° x", "pi = n R T / V for gas in flask only"],
    ),
    q(
        "Osmosis is the flow of solvent through a semipermeable membrane from:",
        "Region of lower solute concentration to higher solute concentration",
        ["Higher to lower solute concentration always", "Solid phase to gas phase", "Anode to cathode in a cell"],
    ),
    q(
        "A 0.1 M glucose solution at 300 K has osmotic pressure approximately (R = 0.0821 L atm mol-1 K-1):",
        "2.46 atm",
        ["0.246 atm", "24.6 atm", "0.0821 atm"],
    ),
    q(
        "Isotonic solutions have:",
        "Same osmotic pressure",
        ["Same boiling point always", "Same density necessarily", "Zero osmotic pressure"],
    ),
    q(
        "Reverse osmosis is used in desalination because:",
        "Applied pressure greater than pi forces solvent through membrane leaving salt behind",
        ["Salt ions pass through membrane preferentially", "Osmotic pressure is zero in seawater", "Only heat is required with no pressure"],
    ),
    q(
        "Compared to other colligative properties, osmotic pressure is often preferred for molar mass determination because:",
        "It is measurable even for very large molar mass solutes at moderate concentrations",
        ["It is independent of temperature", "It requires no semipermeable membrane", "It works only for volatile solutes"],
    ),
]

BANK_ABNORMAL_MOLAR_MASSES: QuestionBank = [
    q(
        "Abnormal molar mass observed from colligative measurements indicates:",
        "Association or dissociation of solute particles in solution",
        ["Error in weighing only", "Solvent evaporation exclusively", "Ideal behaviour of solute"],
    ),
    q(
        "Acetic acid in benzene shows association; van't Hoff factor i is:",
        "Less than 1",
        ["Greater than 2", "Exactly 3", "Always 1 for all carboxylic acids in water"],
    ),
    q(
        "For KCl in very dilute aqueous solution, observed molar mass from colligative property is lower than formula mass because:",
        "KCl dissociates giving i > 1",
        ["KCl associates into dimers", "KCl is non-electrolyte", "Water dissociates KCl into atoms only"],
    ),
    q(
        "Van't Hoff factor i is defined as:",
        "Observed colligative effect / expected colligative effect for no dissociation or association",
        ["Molar mass / observed molar mass always without conditions", "Number of moles of solvent", "Rate constant ratio k2/k1"],
    ),
    q(
        "If experimental molar mass of solute is half the normal value from osmotic pressure, solute likely:",
        "Dissociates into two particles (i = 2)",
        ["Associates into dimers", "Does not dissolve", "Has i = 0.5 only by definition error"],
    ),
    q(
        "Degree of dissociation alpha for an electrolyte relates to i approximately as i =:",
        "1 + (n - 1) alpha for n ions formed",
        ["1 - alpha always", "alpha / n", "n alpha only with no constant term"],
    ),
]

# ---------------------------------------------------------------------------
# Electrochemistry extras
# ---------------------------------------------------------------------------

BANK_GALVANIC_DANIELL: QuestionBank = [
    q(
        "In a galvanic cell, oxidation occurs at the:",
        "Anode",
        ["Cathode", "Salt bridge only", "External wire midpoint"],
    ),
    q(
        "In the Daniell cell Zn(s)|Zn2+||Cu2+|Cu(s), the cathode reaction is:",
        "Cu2+ + 2e- -> Cu(s)",
        ["Zn(s) -> Zn2+ + 2e-", "2H+ + 2e- -> H2", "Cu(s) -> Cu2+ + 2e-"],
    ),
    q(
        "The salt bridge in a galvanic cell maintains electrical neutrality by:",
        "Allowing ion migration between half-cells",
        ["Blocking all ion movement", "Conducting electrons through glass", "Preventing any cell reaction"],
    ),
    q(
        "Electrons in a galvanic cell flow externally from:",
        "Anode to cathode",
        ["Cathode to anode", "Salt bridge to anode", "Cathode to salt bridge only"],
    ),
    q(
        "Cell emf of a galvanic cell at standard conditions is positive when:",
        "Cell reaction is spontaneous as written",
        ["Reaction is non-spontaneous", "Anode is copper and cathode is zinc in Daniell setup", "No salt bridge is used"],
    ),
    q(
        "Standard cell notation places:",
        "Anode (oxidation half-cell) on the left, cathode on the right",
        ["Cathode on the left always", "Salt bridge inside parentheses only", "Most positive electrode always left"],
    ),
]

BANK_GIBBS_CELL_POTENTIAL: QuestionBank = [
    q(
        "Relationship between standard Gibbs energy change and standard cell emf is:",
        "Delta G° = -n F E°cell",
        ["Delta G° = n F E°cell", "Delta G° = -RT ln E°cell", "Delta G° = E°cell / nF"],
    ),
    q(
        "If E°cell is positive for a cell reaction, Delta G° for the reaction is:",
        "Negative",
        ["Positive", "Zero necessarily", "Undefined"],
    ),
    q(
        "At equilibrium for a galvanic cell, cell potential Ecell equals:",
        "Zero",
        ["E°cell", "Maximum always", "Negative of E°cell always"],
    ),
    q(
        "For the reaction with n electrons transferred, the relation Delta G = -n F Ecell holds when:",
        "Ecell is the cell potential under the conditions of the reaction",
        ["Only at absolute zero", "Only for electrolytic cells", "Only when concentration is 1 M for all ions regardless of E"],
    ),
    q(
        "If Q > K for the cell reaction, Ecell compared to E°cell is:",
        "Less than E°cell (for positive E°cell spontaneous case)",
        ["Always greater than E°cell", "Unchanged", "Always equal to E°cell"],
    ),
    q(
        "Faraday constant F represents:",
        "Charge on one mole of electrons",
        ["Gas constant per mole", "Planck constant per electron", "Ratio of mass to charge of proton"],
    ),
]

BANK_KOHLRAUSCH: QuestionBank = [
    q(
        "Kohlrausch's law states that at infinite dilution, molar conductivity Lambda_m° of an electrolyte equals:",
        "Sum of molar ionic conductivities of constituent ions",
        ["Product of ionic conductivities", "Zero for strong electrolytes", "Equal to specific conductance only"],
    ),
    q(
        "Kohlrausch's law helps calculate Lambda_m° for a weak electrolyte like CH3COOH from:",
        "Lambda_m° of strong electrolytes containing the same ions",
        ["Boiling point elevation data", "Crystal field splitting", "SN1 rate measurements"],
    ),
    q(
        "At infinite dilution, inter-ionic interactions are negligible so:",
        "Ions migrate independently contributing additively to conductivity",
        ["All ions pair into neutral molecules", "Conductivity is zero", "Only cations conduct"],
    ),
    q(
        "For NaCl, Lambda_m° = Lambda°(Na+) + Lambda°(Cl-). This is an application of:",
        "Kohlrausch's law of independent migration of ions",
        ["Raoult's law", "Henry's law", "Arrhenius equation"],
    ),
    q(
        "Degree of dissociation alpha of a weak electrolyte can be estimated from:",
        "Lambda_m / Lambda_m° at a given concentration",
        ["Delta Tf / Kf only", "Osmotic pressure alone without i", "Cell emf at zero concentration"],
    ),
    q(
        "Molar conductivity increases on dilution for a strong electrolyte because:",
        "Inter-ionic attraction decreases allowing ions to move more freely",
        ["Number of ions decreases", "Temperature always rises on dilution", "Ions associate more on dilution"],
    ),
]

BANK_BATTERIES_FUEL_CELLS: QuestionBank = [
    q(
        "A primary battery differs from a secondary (storage) battery because primary cells:",
        "Are not designed for efficient recharge after discharge",
        ["Use only fuel gases", "Have no redox chemistry", "Always have E° = 0"],
    ),
    q(
        "In a lead storage battery during discharge, the anode material is oxidized from:",
        "Pb to PbSO4",
        ["PbO2 to PbSO4", "PbSO4 to Pb only at cathode", "H2SO4 to SO2"],
    ),
    q(
        "Hydrogen-oxygen fuel cell converts:",
        "Chemical energy of fuel directly to electrical energy with water as product",
        ["Heat to nuclear energy", "Electrical energy to permanent stored chemical fuel without input", "Mechanical work to osmotic pressure"],
    ),
    q(
        "Dry cell (Leclanche) uses:",
        "Zinc anode and manganese dioxide cathode with acidic paste electrolyte",
        ["Platinum fuel electrode only", "Molten salt at 1000°C exclusively", "No redox reaction"],
    ),
    q(
        "Fuel cells are attractive for transport applications because they can offer:",
        "High efficiency and low pollution when using hydrogen",
        ["Only primary non-rechargeable operation", "No need for any electrolyte", "Spontaneous corrosion as main output"],
    ),
    q(
        "During charging of a lead-acid battery, external electrical energy drives:",
        "Non-spontaneous reverse of discharge reactions",
        ["Same spontaneous discharge further", "Only salt bridge replacement", "Fuel oxidation without electrons"],
    ),
]

BANK_CORROSION: QuestionBank = [
    q(
        "Rusting of iron requires the presence of:",
        "Oxygen and moisture",
        ["Only dry oxygen", "Only nitrogen", "Inert oil coating on surface during corrosion"],
    ),
    q(
        "In electrochemical corrosion, the metal surface acts as:",
        "Anode where oxidation of metal occurs",
        ["Cathode only always", "Salt bridge", "Inert spectator"],
    ),
    q(
        "Galvanizing iron with zinc protects because zinc:",
        "Is oxidized preferentially (sacrificial protection)",
        ["Is more noble than iron and never corrodes", "Forms an impermeable glass layer", "Increases iron oxidation rate"],
    ),
    q(
        "Cathodic protection connects iron structure to:",
        "A more reactive metal or impressed current to make iron cathodic",
        ["More noble metal to accelerate rust", "Only dry sand", "Positive terminal of battery to oxidize iron faster"],
    ),
    q(
        "Formation of rust Fe2O3.xH2O on iron is an example of:",
        "Electrochemical corrosion involving multiple redox steps",
        ["Physical adsorption only", "SN2 reaction", "Colligative property change"],
    ),
    q(
        "Coating iron with tin protects only while coating is intact; if scratched, iron corrodes faster because:",
        "Iron becomes anodic to tin in the couple",
        ["Tin is more reactive than iron always in all couples", "Tin donates electrons to oxygen only in air", "No electrochemical cell forms"],
    ),
]

# ---------------------------------------------------------------------------
# Chemical kinetics extras
# ---------------------------------------------------------------------------

BANK_HALF_LIFE: QuestionBank = [
    q(
        "For a first-order reaction, half-life t1/2 is:",
        "0.693 / k",
        ["k / 0.693", "Proportional to initial concentration", "Independent of rate constant"],
    ),
    q(
        "Half-life of a first-order reaction is independent of:",
        "Initial concentration of reactant",
        ["Rate constant k", "Temperature", "Activation energy"],
    ),
    q(
        "For a zero-order reaction, half-life is proportional to:",
        "Initial concentration [A]0",
        ["Rate constant only", "Square of initial concentration always", "1/[A]0"],
    ),
    q(
        "If half-life of a first-order reaction is 100 s, rate constant k equals:",
        "0.00693 s-1",
        ["693 s-1", "100 s-1", "0.693 s-1"],
    ),
    q(
        "After two half-lives of a first-order reaction, fraction of reactant remaining is:",
        "1/4",
        ["1/2", "1/8", "Zero always"],
    ),
    q(
        "For a second-order reaction of type rate = k[A]^2, half-life t1/2 equals:",
        "1 / (k [A]0)",
        ["0.693 / k", "k [A]0", "Independent of [A]0"],
    ),
]

BANK_ARRHENIUS: QuestionBank = [
    q(
        "Arrhenius equation is:",
        "k = A exp(-Ea / RT)",
        ["k = A + Ea RT", "k = Ea / RT only", "k = exp(A RT)"],
    ),
    q(
        "A plot of ln k versus 1/T gives a straight line with slope:",
        "-Ea / R",
        ["Ea / R", "-R / Ea", "A / R"],
    ),
    q(
        "Increasing temperature increases rate constant mainly because:",
        "More molecules have energy >= activation energy",
        ["Activation energy always decreases to zero", "Collision frequency alone doubles for every 1 K", "Catalyst is formed thermally"],
    ),
    q(
        "The pre-exponential factor A in Arrhenius equation relates to:",
        "Frequency of collisions and orientation factor",
        ["Only activation energy", "Equilibrium constant K", "Cell potential E°"],
    ),
    q(
        "If Ea is large, the rate constant k is:",
        "Very sensitive to temperature change",
        ["Independent of temperature", "Always equal to A", "Zero at all temperatures"],
    ),
    q(
        "Two reactions with same A but different Ea: at higher temperature the reaction with lower Ea:",
        "Has less dramatic increase in k compared to high-Ea reaction when T increases modestly",
        ["Always slower at all temperatures", "Has k independent of Ea", "Cannot be compared by Arrhenius law"],
    ),
]

BANK_COLLISION_THEORY: QuestionBank = [
    q(
        "According to collision theory, reaction occurs when colliding molecules:",
        "Have energy >= activation energy and proper orientation",
        ["Collide with any energy", "Are always in excited electronic states only", "Never require orientation factor"],
    ),
    q(
        "The steric (orientation) factor p in collision theory accounts for:",
        "Fraction of collisions with correct geometry for reaction",
        ["Nuclear spin only", "Solvent viscosity exclusively", "Van't Hoff factor"],
    ),
    q(
        "Rate of bimolecular gas-phase reaction depends on:",
        "Collision frequency Z and fraction of effective collisions",
        ["Only on catalyst mass", "Only on boiling point elevation", "Osmotic pressure of products"],
    ),
    q(
        "Raising temperature increases reaction rate in collision theory because:",
        "Higher fraction of collisions exceed activation energy",
        ["Orientation factor becomes exactly 1 for all reactions", "Activation energy disappears", "Collision frequency decreases"],
    ),
    q(
        "Collision theory explains why not every collision at room temperature leads to product formation because:",
        "Most collisions lack sufficient energy or proper orientation",
        ["Molecules repel by Pauli exclusion only in gases", "Rate constant is zero below 100°C always", "Only ionic reactions occur in gases"],
    ),
    q(
        "For a given reaction, increasing concentration of reactants increases rate primarily by:",
        "Increasing collision frequency",
        ["Lowering activation energy always", "Changing order to zero", "Increasing half-life"],
    ),
]

# ---------------------------------------------------------------------------
# d- and f-block extras
# ---------------------------------------------------------------------------

BANK_D_BLOCK_CONFIG: QuestionBank = [
    q(
        "General outer configuration of d-block elements is:",
        "(n-1)d^1-10 ns^1-2",
        ["ns^10 (n-1)d^0 always", "nf^1-14 ns^2 only", "np^6 exclusively"],
    ),
    q(
        "Chromium (Z=24) has ground-state configuration [Ar] 3d5 4s1 rather than 3d4 4s2 because:",
        "Half-filled d subshell offers extra stability",
        ["4s is higher energy than 3d always", "3d is completely filled", "Aufbau principle is violated without reason"],
    ),
    q(
        "Copper (Z=29) commonly has configuration [Ar] 3d10 4s1 due to:",
        "Stability of filled d subshell",
        ["Empty d subshell preference", "4f filling first", "Only paramagnetic requirement"],
    ),
    q(
        "Variable oxidation states of transition metals arise mainly because:",
        "Both (n-1)d and ns electrons can participate in bonding",
        ["Only ns electrons ionize", "d orbitals are always fully occupied in compounds", "f orbitals donate electrons first"],
    ),
    q(
        "First transition series corresponds to filling of:",
        "3d orbitals",
        ["4d orbitals", "3f orbitals", "4f orbitals"],
    ),
    q(
        "Which element is a transition metal by definition?",
        "Iron (partially filled d in common oxidation states)",
        ["Zinc in +2 state with d10 configuration in ion", "Argon", "Calcium only as s-block"],
    ),
]

BANK_ACTINOIDS: QuestionBank = [
    q(
        "Actinoids involve progressive filling of:",
        "5f orbitals",
        ["4f orbitals", "3d orbitals", "6p orbitals only"],
    ),
    q(
        "Compared to lanthanoids, actinoids show:",
        "Greater range of oxidation states and radioactivity",
        ["No radioactivity", "Only +3 oxidation state exclusively", "Smaller atomic radii always without exception"],
    ),
    q(
        "Actinoid contraction refers to:",
        "Gradual decrease in atomic/ionic radii across the series",
        ["Expansion due to 6d filling only", "Increase in melting point only", "Loss of nuclear charge"],
    ),
    q(
        "Uranium and thorium are actinoids used historically in part because they:",
        "Occur in nature and exhibit radioactivity/nuclear chemistry",
        ["Are noble gases", "Have filled 5f in ground state always like inert gases", "Form only colourless diamagnetic ions always"],
    ),
    q(
        "Actinoids are placed in the periodic table in:",
        "Period 7 below lanthanoids",
        ["Period 6 d-block only", "Group 18", "s-block exclusively"],
    ),
    q(
        "4f and 5f orbitals in actinoids compared to lanthanoids have:",
        "Poorer shielding leading to more complex chemistry",
        ["Perfect shielding with identical chemistry", "No participation in bonding ever", "Only ionic radius identical to lanthanoids"],
    ),
]

BANK_KMNO4_K2CR2O7: QuestionBank = [
    q(
        "Acidified KMnO4 acts as a strong oxidizing agent; purple MnO4- is reduced to Mn2+ in acidic medium giving:",
        "Colourless solution",
        ["Green Cr3+ solution always", "Brown I2 solution always", "Yellow dichromate"],
    ),
    q(
        "In acidic solution, one mole MnO4- accepts how many moles of electrons to form Mn2+?",
        "5",
        ["3", "6", "1"],
    ),
    q(
        "K2Cr2O7 in acidic medium is reduced to:",
        "Cr3+ (green)",
        ["Mn2+", "CrO4^2- only without change", "Metallic chromium always"],
    ),
    q(
        "Orange dichromate Cr2O7^2- and yellow chromate CrO4^2- exist in equilibrium; adding acid shifts equilibrium:",
        "Towards dichromate (orange)",
        ["Towards chromate only", "To precipitate Cr(OH)3 instantly always", "To eliminate all chromium species"],
    ),
    q(
        "KMnO4 is preferred in some titrations because:",
        "It serves as its own indicator (purple to colourless)",
        ["It is a primary standard without any preparation", "It cannot oxidize any organic compound", "It works only in neutral pH exclusively"],
    ),
    q(
        "Balancing redox with K2Cr2O7 in acid, each Cr2O7^2- requires how many electrons?",
        "6",
        ["3", "5", "10"],
    ),
]

# ---------------------------------------------------------------------------
# Coordination compounds extras
# ---------------------------------------------------------------------------

BANK_LIGANDS_COORD_NUMBER: QuestionBank = [
    q(
        "Coordination number of central metal ion is:",
        "Number of sigma donor atoms directly bonded to the metal",
        ["Total number of ligands regardless of denticity only", "Oxidation state of metal", "Charge on complex ion only"],
    ),
    q(
        "Ethylenediamine (en) is a:",
        "Bidentate ligand",
        ["Monodentate ligand", "Tridentate ligand always", "Ambidentate only with oxygen donor fixed"],
    ),
    q(
        "In [Co(NH3)6]3+, coordination number of Co is:",
        "6",
        ["3", "4", "2"],
    ),
    q(
        "Chelate complexes are more stable than similar monodentate complexes due to:",
        "Chelate effect (entropy and multidentate binding)",
        ["Weaker metal-ligand bonds", "Absence of ring formation", "Higher coordination number always decreasing stability"],
    ),
    q(
        "CN- is an example of:",
        "Monodentate ambidentate ligand (C- or N-bound forms possible)",
        ["Always bridging only ligand", "Hexadentate ligand", "Non-coordinating anion never"],
    ),
    q(
        "Denticity of EDTA4- as ligand is:",
        "6",
        ["2", "4", "1"],
    ),
]

BANK_VBT_COMPLEXES: QuestionBank = [
    q(
        "Valence bond theory explains bonding in [Ni(CN)4]2- as:",
        "dsp2 hybridization giving square planar geometry",
        ["sp3 tetrahedral always", "d2sp3 octahedral", "No hybridization involved"],
    ),
    q(
        "Inner orbital (low-spin) complex typically uses:",
        "(n-1)d orbitals for hybridization with empty ns and np",
        ["Only outer nd orbitals always", "Only s orbitals", "f orbitals exclusively for first-row metals"],
    ),
    q(
        "According to VBT, paramagnetism in a complex indicates:",
        "Presence of unpaired electrons in metal or ligand field",
        ["Always diamagnetic metal only", "Absence of d electrons", "Only ionic bonding without covalency"],
    ),
    q(
        "Octahedral complex with sp3d2 hybridization (outer orbital) is often:",
        "High-spin if weak field ligands",
        ["Always low-spin", "Always square planar", "Always linear"],
    ),
    q(
        "Limitation of valence bond theory for coordination compounds includes:",
        "No quantitative explanation of magnetic behaviour and colour",
        ["Failure to predict geometry entirely", "Inability to count electrons", "Denial of metal-ligand bonding"],
    ),
    q(
        "In VBT, bond formation between metal and ligand is described as:",
        "Donation of electron pair from ligand into empty hybrid orbital of metal",
        ["Complete transfer of metal electrons to ligand only", "Only ionic lattice formation", "Metallic bonding in all complexes"],
    ),
]

BANK_CFT: QuestionBank = [
    q(
        "In octahedral crystal field, five d orbitals split into:",
        "t2g (lower) and eg (higher) sets",
        ["All degenerate", "Only one orbital raised", "4s and 3d only without splitting"],
    ),
    q(
        "Crystal field splitting energy in octahedral field is denoted:",
        "Delta_o",
        ["Delta_t exclusively for all geometries", "Kb", "Ea"],
    ),
    q(
        "Strong field ligands like CN- typically give:",
        "Low-spin complexes with large Delta_o",
        ["High-spin always", "No splitting", "Only tetrahedral geometry always"],
    ),
    q(
        "Colour of many transition metal complexes arises from:",
        "d-d electronic transitions between split d levels",
        ["s-p transitions only", "Nuclear fusion in metal", "Raoult's law deviation"],
    ),
    q(
        "In tetrahedral complexes, crystal field splitting Delta_t is approximately:",
        "Smaller than Delta_o for same metal and ligand set",
        ["Four times Delta_o", "Zero always", "Equal to pairing energy always"],
    ),
    q(
        "CFSE (crystal field stabilization energy) depends on:",
        "Number of electrons in t2g and eg and magnitude of splitting",
        ["Only on ligand mass", "Only on coordination number of counter-ion in crystal lattice outside complex", "Van't Hoff factor"],
    ),
]

BANK_IMPORTANCE_COORD: QuestionBank = [
    q(
        "Haemoglobin binds O2 because iron in porphyrin forms a:",
        "Coordination complex reversible with oxygen",
        ["Pure ionic NaCl-type lattice", "SN2 product only", "Fuel cell electrode exclusively"],
    ),
    q(
        "EDTA is used in water treatment to:",
        "Sequester metal ions by forming stable chelate complexes",
        ["Increase hardness by adding Ca2+", "Oxidize organic waste with MnO4-", "Generate osmotic pressure only"],
    ),
    q(
        "Cisplatin [Pt(NH3)2Cl2] is important in medicine as:",
        "Anticancer agent binding to DNA via coordination",
        ["Vitamin supplement", "Fuel for hydrogen cell", "Dry cell cathode material only"],
    ),
    q(
        "Silver photography historically involved coordination of Ag+ with:",
        "Thiosulfate in fixing bath to form soluble complexes",
        ["Only chloride to insoluble AgCl always in fixer", "Ethanol exclusively", "Glucose in Tollens test only"],
    ),
    q(
        "Electroplating of metals uses coordination/electrochemistry to:",
        "Deposit uniform metal coating via controlled reduction at cathode",
        ["Dissolve cathode preferentially", "Generate osmotic pressure", "Catalyse SN1 reactions"],
    ),
    q(
        "Wilkinson's catalyst (Rh complex) exemplifies importance of coordination compounds in:",
        "Homogeneous catalysis (hydrogenation)",
        ["Nuclear fission", "Corrosion of iron only", "Freezing point depression measurements"],
    ),
]

# ---------------------------------------------------------------------------
# Organic chemistry extras
# ---------------------------------------------------------------------------

BANK_SN1_SN2: QuestionBank = [
    q(
        "SN2 mechanism is characterized by:",
        "One-step bimolecular backside attack with inversion of configuration",
        ["Two-step carbocation intermediate always", "Racemization at chiral center always", "Rate independent of nucleophile concentration"],
    ),
    q(
        "SN1 reaction rate depends on:",
        "Concentration of alkyl halide only (first order)",
        ["Both halide and nucleophile in rate law always", "Only nucleophile concentration", "Square of halide concentration always"],
    ),
    q(
        "Primary alkyl halides typically react with good nucleophiles via:",
        "SN2",
        ["SN1 exclusively", "E1 only at low temperature always", "No substitution possible"],
    ),
    q(
        "Tertiary alkyl halides in polar protic solvents favour:",
        "SN1 and E1 via stable tertiary carbocation",
        ["SN2 exclusively", "Only Williamson synthesis", "No elimination ever"],
    ),
    q(
        "Polar aprotic solvents (e.g. acetone, DMSO) generally favour:",
        "SN2 over SN1",
        ["SN1 over SN2 always", "Neither substitution nor elimination", "Only E2 with no SN2"],
    ),
    q(
        "Steric hindrance at the electrophilic carbon strongly:",
        "Retards SN2",
        ["Accelerates SN2", "Has no effect on either mechanism", "Forces SN1 with primary halides only"],
    ),
]

BANK_HALOARENES: QuestionBank = [
    q(
        "Chlorobenzene is less reactive than chloroethane toward nucleophilic substitution because:",
        "C-Cl partial double bond character from resonance with ring",
        ["C-Cl is longer and weaker only", "Chlorobenzene is primary halide", "Ring is saturated cyclohexane"],
    ),
    q(
        "Haloarenes do not undergo SN reactions easily under normal conditions due to:",
        "Stabilization of C-X bond by delocalization into ring",
        ["Absence of leaving group", "Instability of benzene ring", "High solubility in water only"],
    ),
    q(
        "Fittig reaction couples two aryl halides using:",
        "Sodium metal in dry ether",
        ["Grignard reagent only", "Conc. HNO3", "Br2 in CCl4"],
    ),
    q(
        "Dow process prepares phenol from:",
        "Chlorobenzene by fusion with NaOH at high temperature",
        ["Benzene diazonium salt only", "Toluene oxidation", "Ethanol dehydration"],
    ),
    q(
        "Electrophilic substitution on haloarenes: halogen is:",
        "Ortho-para directing and deactivating",
        ["Meta directing and activating", "Ortho-para directing and strongly activating", "Never directs incoming groups"],
    ),
    q(
        "Wurtz-Fittig reaction involves:",
        "Aryl halide and alkyl halide with sodium to give alkylbenzene",
        ["Two alkyl halides only", "Two aryl halides only with no alkyl halide", "Oxidation of benzene to phenol"],
    ),
]

BANK_PHENOL_ACIDITY: QuestionBank = [
    q(
        "Phenol is more acidic than ethanol because phenoxide ion is stabilized by:",
        "Resonance delocalization of negative charge into the ring",
        ["Inductive effect of ethyl group", "Higher molar mass", "Hydrogen bonding in ethanol only without conjugate base effect"],
    ),
    q(
        "Phenol is less acidic than carboxylic acids because:",
        "Carboxylate ion has greater resonance stabilization involving both oxygens",
        ["Phenol has no O-H bond", "Carboxylic acids have no resonance", "Phenol is fully ionized in water"],
    ),
    q(
        "Electron-withdrawing group (e.g. -NO2) at ortho/para to OH on phenol:",
        "Increases acidity",
        ["Decreases acidity always", "Has no effect", "Converts phenol to alcohol"],
    ),
    q(
        "Phenol reacts with aqueous NaOH but ethanol does not appreciably because:",
        "Phenoxide is sufficiently stabilized to shift equilibrium",
        ["Ethanol is stronger acid", "NaOH reacts only with aromatic compounds by rule", "Ethanol forms dimer with NaOH"],
    ),
    q(
        "Lucas test distinguishes alcohols; phenol gives:",
        "No turbidity with Lucas reagent at room temperature (not a typical alcohol response)",
        ["Immediate turbidity like tertiary alcohol", "Silver mirror", "Iodoform precipitate always"],
    ),
    q(
        "pKa of phenol is approximately:",
        "10",
        ["4-5 like carboxylic acid", "15-16 like ethanol", "0 like strong mineral acid"],
    ),
]

BANK_ETHERS: QuestionBank = [
    q(
        "Williamson ether synthesis involves:",
        "SN2 reaction of alkoxide ion with primary alkyl halide",
        ["Electrophilic addition to alkene", "Friedel-Crafts alkylation of benzene only", "Oxidation of primary alcohol with KMnO4"],
    ),
    q(
        "Ethers have lower boiling points than isomeric alcohols because:",
        "Ethers cannot form intermolecular hydrogen bonding as hydrogen bond donors",
        ["Ethers have higher molar mass always", "Ethers are ionic", "Alcohols lack dipole moment"],
    ),
    q(
        "Cleavage of unsymmetrical ether R-O-R' with excess HI gives:",
        "Mixture of RI and R'I (both alkyl iodides with excess HI)",
        ["Only alcohols", "Only alkenes", "Phenol exclusively for all ethers"],
    ),
    q(
        "Diethyl ether is stored away from flames partly because:",
        "It can form explosive peroxides on long standing with air",
        ["It is ionic and conducts electricity", "It reacts with glass", "It has extremely high boiling point"],
    ),
    q(
        "Functional group of ether is:",
        "R-O-R' (dialkyl or alkyl aryl oxide linkage)",
        ["R-COO-R'", "R-CHO", "R-NH-R'"],
    ),
    q(
        "Anisole (methoxybenzene) is prepared industrially or in lab via:",
        "Williamson synthesis using sodium phenoxide and CH3I",
        ["Hydration of ethylene only", "Fermentation", "Tollens reagent on methanol"],
    ),
]

BANK_NUCLEOPHILIC_ADDITION_CARBONYL: QuestionBank = [
    q(
        "Carbonyl carbon is susceptible to nucleophilic attack because:",
        "It is electrophilic due to C=O polarity and partial positive charge on C",
        ["It is strongly nucleophilic", "It is sp hybridized always", "Oxygen donates lone pair making C negative only without electrophilic character"],
    ),
    q(
        "Addition of HCN to aldehyde produces:",
        "Cyanohydrin",
        ["Gem-dihalide", "Aldol product directly always", "Carboxylic acid without hydrolysis"],
    ),
    q(
        "NaHSO3 adds to carbonyl compounds to form:",
        "Bisulphite addition compound (solid adduct)",
        ["Ester", "Amide directly", "Alkane without oxygen"],
    ),
    q(
        "Grignard reagent R-MgX adds to carbonyl followed by acid workup gives:",
        "Alcohol (secondary if aldehyde, tertiary if ketone)",
        ["Alkane only", "Carboxylic acid without any step", "Ether exclusively"],
    ),
    q(
        "Relative reactivity toward nucleophilic addition: aldehydes vs ketones:",
        "Aldehydes are generally more reactive (less steric hindrance)",
        ["Ketones always more reactive", "Identical reactivity always", "Esters more reactive than both always for same R"],
    ),
    q(
        "Nucleophilic addition to C=O first forms:",
        "Tetrahedral intermediate (alkoxide)",
        ["Carbocation", "Free radical chain", "Aromatic sigma complex only"],
    ),
]

BANK_BASICITY_AMINES: QuestionBank = [
    q(
        "Amines are basic because:",
        "Lone pair on nitrogen can accept a proton",
        ["They donate protons to water", "Nitrogen is always sp hybridized", "They form hydrogen bonds only without proton acceptance"],
    ),
    q(
        "In gas phase, basicity order often is tertiary > secondary > primary > NH3 because:",
        "Inductive effect of alkyl groups stabilizes conjugate acid",
        ["Solvation dominates always in gas phase", "Aromatic resonance increases basicity of aniline", "Tertiary amines cannot accept H+"],
    ),
    q(
        "Aniline is weaker base than ammonia in water because:",
        "Lone pair is delocalized into benzene ring",
        ["Nitrogen is sp3 without lone pair", "Aniline is quaternary ammonium", "Ring withdraws electron density by induction only with no resonance"],
    ),
    q(
        "Electron-donating substituent on aromatic ring increases basicity of aniline because:",
        "It increases electron density on nitrogen",
        ["It removes lone pair from ring", "It converts amine to amide", "It prevents protonation entirely"],
    ),
    q(
        "Quaternary ammonium salts R4N+:",
        "Cannot act as bases by accepting H+ on nitrogen (no lone pair)",
        ["Are strongest bases in water", "Always decompose to aniline", "Are identical to tertiary amines in basicity"],
    ),
    q(
        "Aliphatic amines are generally more basic than ammonia in aqueous solution because:",
        "Alkyl groups donate electron density toward nitrogen",
        ["They are less soluble", "They resist protonation", "They form only hydrogen bonds without proton transfer"],
    ),
]

BANK_ENZYMES: QuestionBank = [
    q(
        "Enzymes are:",
        "Biological catalysts (mostly proteins) that increase rate of specific reactions",
        ["Non-specific thermal catalysts only", "Always DNA molecules", "Inhibitors that slow all metabolism equally"],
    ),
    q(
        "Lock-and-key model of enzyme action proposes:",
        "Substrate fits specific active site shape on enzyme",
        ["Enzyme changes substrate into any random product", "No binding occurs before reaction", "Enzyme is consumed stoichiometrically"],
    ),
    q(
        "Enzyme activity generally decreases sharply when:",
        "Temperature or pH moves far from optimum causing denaturation",
        ["Substrate concentration is low only without denaturation", "Product is removed", "Reaction is exothermic"],
    ),
    q(
        "Enzymes increase reaction rate by:",
        "Lowering activation energy via ES complex formation",
        ["Increasing equilibrium constant K always", "Shifting Delta G to large negative always", "Consuming ATP in every enzyme class without exception"],
    ),
    q(
        "Competitive inhibitor affects enzyme kinetics by:",
        "Competing with substrate for active site; Vmax unchanged, Km increases",
        ["Lowering Vmax and Km equally always", "Binding only at allosteric site always", "Denaturing enzyme irreversibly in all cases"],
    ),
    q(
        "Specificity of enzymes means:",
        "Each enzyme typically catalyses one type of reaction or few closely related substrates",
        ["All enzymes catalyse all reactions in cell", "Enzymes work only at 100°C", "Enzymes are consumed in every turnover"],
    ),
]

# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

_TOPIC_REGISTRATIONS: list[tuple[list[str], QuestionBank]] = [
    (["Solubility of solids and gases"], BANK_SOLUBILITY_SOLIDS_GASES),
    (["Henry's law"], BANK_HENRYS_LAW),
    (["Vapour pressure of liquid solutions"], BANK_VAPOUR_PRESSURE_LIQUID),
    (["Raoult's law"], BANK_RAOULTS_LAW),
    (["Ideal and non-ideal solutions"], BANK_IDEAL_NON_IDEAL),
    (["Relative lowering of vapour pressure"], BANK_RELATIVE_LOWERING_VP),
    (["Elevation of boiling point"], BANK_ELEVATION_BOILING),
    (["Depression of freezing point"], BANK_DEPRESSION_FREEZING),
    (["Osmotic pressure"], BANK_OSMOTIC_PRESSURE),
    (["Abnormal molar masses"], BANK_ABNORMAL_MOLAR_MASSES),
    (["Galvanic cell and Daniell cell"], BANK_GALVANIC_DANIELL),
    (["Gibbs energy and cell potential"], BANK_GIBBS_CELL_POTENTIAL),
    (["Kohlrausch's law"], BANK_KOHLRAUSCH),
    (["Batteries and fuel cells"], BANK_BATTERIES_FUEL_CELLS),
    (["Corrosion"], BANK_CORROSION),
    (["Half life of a reaction"], BANK_HALF_LIFE),
    (["Arrhenius equation"], BANK_ARRHENIUS),
    (["Collision theory"], BANK_COLLISION_THEORY),
    (["Electronic configuration of d-block"], BANK_D_BLOCK_CONFIG),
    (["Actinoids"], BANK_ACTINOIDS),
    (["KMnO4 and K2Cr2O7"], BANK_KMNO4_K2CR2O7),
    (["Ligands and coordination number"], BANK_LIGANDS_COORD_NUMBER),
    (["Valence bond theory of complexes"], BANK_VBT_COMPLEXES),
    (["Crystal field theory"], BANK_CFT),
    (["Importance of coordination compounds"], BANK_IMPORTANCE_COORD),
    (["Nucleophilic substitution SN1 and SN2"], BANK_SN1_SN2),
    (["Haloarenes"], BANK_HALOARENES),
    (["Acidity of phenols"], BANK_PHENOL_ACIDITY),
    (["Ethers"], BANK_ETHERS),
    (["Nucleophilic addition to carbonyl group"], BANK_NUCLEOPHILIC_ADDITION_CARBONYL),
    (["Basicity of amines"], BANK_BASICITY_AMINES),
    (["Enzymes"], BANK_ENZYMES),
]

_KEYWORD_ENTRIES: list[tuple[tuple[str, ...], QuestionBank]] = [
    (("solubility", "ksp", "gas solubility", "like dissolves like"), BANK_SOLUBILITY_SOLIDS_GASES),
    (("henry's law", "kh", "partial pressure gas"), BANK_HENRYS_LAW),
    (("vapour pressure", "partial pressure", "volatile component"), BANK_VAPOUR_PRESSURE_LIQUID),
    (("raoult", "p = p0 x", "ideal liquid solution"), BANK_RAOULTS_LAW),
    (("positive deviation", "negative deviation", "azeotrope", "non-ideal solution"), BANK_IDEAL_NON_IDEAL),
    (("relative lowering", "(p0 - p)/p0"), BANK_RELATIVE_LOWERING_VP),
    (("elevation in boiling", "delta tb", "ebullioscopic", "kb m"), BANK_ELEVATION_BOILING),
    (("depression in freezing", "delta tf", "cryoscopic", "antifreeze"), BANK_DEPRESSION_FREEZING),
    (("osmotic pressure", "isotonic", "reverse osmosis", "semipermeable"), BANK_OSMOTIC_PRESSURE),
    (("abnormal molar mass", "association", "dissociation", "vant hoff factor"), BANK_ABNORMAL_MOLAR_MASSES),
    (("daniell cell", "galvanic cell", "salt bridge", "anode cathode"), BANK_GALVANIC_DANIELL),
    (("delta g", "gibbs energy", "nfe", "cell potential"), BANK_GIBBS_CELL_POTENTIAL),
    (("kohlrausch", "molar conductivity", "lambda", "independent migration"), BANK_KOHLRAUSCH),
    (("lead storage", "fuel cell", "dry cell", "battery discharge"), BANK_BATTERIES_FUEL_CELLS),
    (("corrosion", "rusting", "galvanizing", "cathodic protection"), BANK_CORROSION),
    (("half-life", "t1/2", "first order half"), BANK_HALF_LIFE),
    (("arrhenius", "activation energy", "ln k", "pre-exponential"), BANK_ARRHENIUS),
    (("collision theory", "orientation factor", "effective collision", "steric factor"), BANK_COLLISION_THEORY),
    (("d-block configuration", "3d5 4s1", "chromium copper exception"), BANK_D_BLOCK_CONFIG),
    (("actinoid", "5f", "uranium", "thorium"), BANK_ACTINOIDS),
    (("kmno4", "k2cr2o7", "dichromate", "permanganate titration"), BANK_KMNO4_K2CR2O7),
    (("ligand", "coordination number", "bidentate", "chelate"), BANK_LIGANDS_COORD_NUMBER),
    (("valence bond theory", "dsp2", "inner orbital complex", "hybridization complex"), BANK_VBT_COMPLEXES),
    (("crystal field", "delta_o", "t2g", "eg", "cfse"), BANK_CFT),
    (("cisplatin", "edta", "haemoglobin", "coordination compound application"), BANK_IMPORTANCE_COORD),
    (("sn1", "sn2", "backside attack", "carbocation"), BANK_SN1_SN2),
    (("haloarene", "chlorobenzene", "fittig", "dow process"), BANK_HALOARENES),
    (("phenol acidity", "phenoxide", "pka phenol"), BANK_PHENOL_ACIDITY),
    (("williamson ether", "diethyl ether", "peroxide", "r-o-r"), BANK_ETHERS),
    (("nucleophilic addition", "cyanohydrin", "bisulphite adduct", "carbonyl"), BANK_NUCLEOPHILIC_ADDITION_CARBONYL),
    (("basicity of amine", "aniline weak base", "quaternary ammonium"), BANK_BASICITY_AMINES),
    (("enzyme", "active site", "denaturation", "lock and key"), BANK_ENZYMES),
]


def register() -> None:
    """Register all Class 12 Chemistry extra banks into quiz_concepts."""
    for titles, bank in _TOPIC_REGISTRATIONS:
        register_keys(titles, bank)
    register_subject_keywords("CHEM", _KEYWORD_ENTRIES)
