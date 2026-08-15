"""CBSE Class 11–12 Biology concept MCQ banks. Never falls back to Physics."""

from __future__ import annotations

from app.data.quiz_banks.common import q, register_keys, register_subject_keywords
from app.data.quiz_concepts import QuestionBank


def _register(keys: list[str], bank: QuestionBank, *keywords: str) -> None:
    register_keys(keys, bank)
    if keywords:
        register_subject_keywords("BIO", [(keywords, bank)])


BANK_FLOWER: QuestionBank = [
    q("The male reproductive unit of a flower is the:", "Stamen", ["Carpel", "Ovule", "Petal"]),
    q("The process of formation of microspores from a pollen mother cell is:", "Microsporogenesis", ["Megasporogenesis", "Syngamy", "Triple fusion"]),
    q("A typical angiosperm embryo sac is:", "7-celled and 8-nucleate", ["8-celled and 7-nucleate", "2-celled", "16-nucleate"]),
    q("Transfer of pollen from anther to stigma of the same flower is:", "Autogamy", ["Xenogamy", "Geitonogamy only in gymnosperms", "Triple fusion"]),
    q("Double fertilisation in angiosperms produces:", "A zygote and a triploid primary endosperm nucleus", ["Two zygotes", "Only endosperm", "Only a haploid embryo"]),
    q("Apomixis is:", "Production of seeds without fertilisation", ["Fusion of two eggs", "Self-pollination only", "Formation of pollen tetrads"]),
    q("The three cells of the egg apparatus are:", "One egg and two synergids", ["Two eggs and one synergid", "Three antipodals", "Two polar nuclei and one egg"]),
    q("Polyembryony means:", "More than one embryo in a seed", ["More than one ovule in an ovary", "More than one pollen tube", "Absence of endosperm"]),
]

BANK_HUMAN_REPRO: QuestionBank = [
    q("Spermatogenesis occurs in the:", "Seminiferous tubules", ["Epididymis only", "Prostate gland", "Seminal vesicles"]),
    q("The hormone that triggers ovulation is:", "LH (luteinising hormone)", ["FSH only", "Prolactin only", "Oxytocin only"]),
    q("Implantation of the blastocyst occurs in the:", "Endometrium of the uterus", ["Ovary", "Fallopian infundibulum wall as the default site", "Cervix canal lumen only"]),
    q("The corpus luteum secretes mainly:", "Progesterone", ["Testosterone", "Thyroxine", "Adrenaline"]),
    q("Parturition is induced by a complex neuroendocrine mechanism involving:", "Oxytocin", ["Thyroxine only", "Insulin only", "Melatonin only"]),
    q("Oogenesis produces:", "One functional ovum and polar bodies", ["Four equal ova", "Two sperms", "Only polar bodies"]),
    q("The placenta is formed by tissues of:", "Both foetus and mother", ["Only the foetus", "Only the mother", "The ovary alone"]),
    q("Lactation is initiated by:", "Prolactin", ["ADH only", "Calcitonin", "Gastrin"]),
]

BANK_REPRO_HEALTH: QuestionBank = [
    q("An IUD such as Cu-T primarily acts by:", "Increasing phagocytosis of sperms and suppressing fertilisation", ["Killing the ovary", "Blocking FSH permanently", "Surgically cutting vas deferens"]),
    q("MTP is legally allowed in India up to:", "A defined gestational period under the MTP Act with conditions", ["Any time without restriction", "Only after birth", "Never under any law"]),
    q("A common bacterial STI is:", "Gonorrhoea", ["HIV only", "Malaria", "Tetanus"]),
    q("IVF involves:", "Fertilisation outside the body followed by embryo transfer", ["Injection of sperm into the uterus only", "Cloning of a baby", "Hormone-free natural conception only"]),
    q("ZIFT places the zygote in the:", "Fallopian tube", ["Uterus directly as GIFT", "Ovary", "Cervix only"]),
    q("Saheli is:", "A non-steroidal oral contraceptive", ["A copper IUD", "A vaccine against HIV", "A surgical method"]),
]

BANK_MENDEL: QuestionBank = [
    q("Mendel's law of segregation states that alleles:", "Separate during gamete formation", ["Blend in the F1 permanently", "Always stay together", "Mutate each generation"]),
    q("A test cross is a cross of an individual with:", "A homozygous recessive", ["A homozygous dominant", "Another heterozygote only", "Its parent always"]),
    q("ABO blood groups are an example of:", "Multiple alleles and codominance", ["Simple dominance only", "Pleiotropy only", "Sex-limited traits only"]),
    q("Linkage refers to:", "Genes on the same chromosome inherited together", ["Independent assortment of all genes", "Mutation rate", "Codominance"]),
    q("Down's syndrome is caused by:", "Trisomy of chromosome 21", ["Monosomy X", "Deletion of chromosome 1", "Extra Y only always"]),
    q("Colour blindness in humans is typically:", "X-linked", ["Y-linked always", "Autosomal dominant only", "Mitochondrial always"]),
    q("Incomplete dominance in snapdragon flower colour produces a:", "Pink heterozygote", ["Only red or white", "Black flower", "Triploid plant"]),
    q("A pedigree chart is used to:", "Trace inheritance of a trait in a family", ["Measure DNA length", "Count chromosomes in mitosis only", "Sequence a genome"]),
]

BANK_MOLECULAR: QuestionBank = [
    q("Hershey and Chase showed that the genetic material of bacteriophage is:", "DNA", ["Protein coat", "RNA only in all phages", "Lipid envelope"]),
    q("Chargaff's rule states that in DNA:", "A = T and G = C", ["A = G and T = C", "A + T = G + C always as 1:1 with RNA", "U = T"]),
    q("DNA replication is:", "Semi-conservative", ["Conservative only", "Dispersive only", "Random mixing of bases"]),
    q("Transcription is synthesis of:", "RNA from a DNA template", ["DNA from RNA", "Protein from DNA directly", "Lipid from mRNA"]),
    q("The initiator codon is:", "AUG", ["UAA", "UGA", "UAG"]),
    q("The lac operon is an example of:", "Transcriptional regulation in prokaryotes", ["Splicing in eukaryotes only", "DNA fingerprinting", "Crossing over"]),
    q("DNA fingerprinting uses:", "VNTR / repetitive DNA polymorphisms", ["Whole genome cloning of organelles", "Protein sequencing only", "Blood group antigens only"]),
    q("Histones help in:", "DNA packaging in eukaryotes", ["Okazaki fragment ligation only", "Peptide bond formation", "mRNA capping only"]),
]

BANK_EVOLUTION: QuestionBank = [
    q("Oparin–Haldane proposed that life arose from:", "A chemical evolution in a reducing atmosphere", ["Panspermia only", "Sudden special creation as a scientific model", "Always aerobic ponds"]),
    q("Analogous organs indicate:", "Convergent evolution", ["Common ancestry always", "Vestigiality only", "Genetic drift only"]),
    q("Hardy–Weinberg equilibrium assumes:", "No selection mutation migration or non-random mating", ["Strong selection only", "Small population always", "Gene flow every generation"]),
    q("Industrial melanism in Biston betularia is an example of:", "Natural selection", ["Lamarckian inheritance of acquired darkness as proven", "Founder effect only", "Bottleneck only"]),
    q("Homo sapiens originated in:", "Africa (out-of-Africa evidence)", ["Australia first", "Antarctica", "South America as the sole origin"]),
    q("Adaptive radiation is exemplified by:", "Darwin's finches", ["Human mitosis", "Mendel's peas only", "PCR"]),
]

BANK_HEALTH: QuestionBank = [
    q("Innate immunity includes:", "Physical barriers and phagocytes", ["Only antibodies after vaccination", "Only memory B cells", "Only booster doses"]),
    q("Antibodies are produced by:", "B lymphocytes / plasma cells", ["Erythrocytes", "Platelets", "Osteocytes"]),
    q("HIV primarily infects:", "Helper T-cells (CD4+)", ["Mature RBCs", "Platelets only", "Osteoblasts"]),
    q("A vaccine typically provides:", "Active acquired immunity", ["Passive innate barriers only", "Antibiotics", "Allergy always"]),
    q("Malignant tumours are characterised by:", "Metastasis", ["Remaining local always", "Being identical to a cyst", "Never dividing"]),
    q("Opioids bind to receptors in the:", "Central nervous system and GI tract", ["Only in bone matrix", "Only on RBC membranes", "Plant cell walls"]),
]

BANK_MICROBES: QuestionBank = [
    q("Lactobacillus in curd converts lactose mainly to:", "Lactic acid", ["Ethanol only", "Acetic acid only", "Methane"]),
    q("Streptokinase from Streptococcus is used as a:", "Clot buster", ["Antibiotic", "Biofertiliser", "Insecticide"]),
    q("Activated sludge in sewage treatment is:", "Sediment of bacteria and fungi that oxidises organic matter", ["Sand filter only", "Chlorine gas", "Pure methane crystals"]),
    q("Biogas is rich in:", "Methane", ["Oxygen", "Nitrogen dioxide", "Ozone"]),
    q("Azotobacter is used as a:", "Free-living nitrogen-fixing biofertiliser", ["Pathogen of rice blast", "Source of insulin", "Insect biocontrol virus"]),
    q("Bacillus thuringiensis is used as a:", "Microbial biocontrol of insect larvae", ["Fungicide for rust only", "Antiviral drug", "Vaccine against polio"]),
]

BANK_BIOTECH_PROC: QuestionBank = [
    q("Restriction enzymes cut DNA at:", "Specific palindromic recognition sequences", ["Random peptide bonds", "Any AT-rich stretch only", "RNA primers only"]),
    q("A plasmid used in rDNA is a:", "Cloning vector", ["Ribosome", "Spliceosome", "Nucleosome"]),
    q("PCR amplifies DNA using:", "Thermostable DNA polymerase and thermal cycling", ["Ligase only", "Restriction enzymes only", "Reverse transcriptase only always"]),
    q("Selectable markers in plasmids commonly include:", "Antibiotic resistance genes", ["Histone genes", "Chlorophyll genes", "Keratin genes"]),
    q("Competent cells take up DNA more readily after:", "Calcium chloride / heat shock or electroporation", ["Boiling at 100°C for an hour", "Drying completely", "UV sterilisation of DNA"]),
]

BANK_BIOTECH_APP: QuestionBank = [
    q("Bt toxin in Bt cotton is encoded by:", "cry genes of Bacillus thuringiensis", ["Insulin gene of humans", "Nif genes of Rhizobium", "Antibody genes"]),
    q("RNA interference is used in plants to:", "Silence specific mRNA (e.g. Meloidegyne in tobacco)", ["Increase chromosome number", "Fix nitrogen", "Do PCR"]),
    q("The first recombinant therapeutic product approved widely was:", "Humulin (recombinant insulin)", ["Bt cotton as a drug", "Streptomycin", "Penicillin G only"]),
    q("Gene therapy aims to:", "Correct a defective gene in a patient", ["Always clone a whole organism", "Sequence mitochondria only", "Vaccinate plants"]),
    q("Biopiracy refers to:", "Unauthorised use of biological resources / traditional knowledge", ["Legal patenting by the community itself", "Composting", "PCR contamination"]),
    q("A transgenic animal carries:", "A foreign gene in its genome", ["Only extra fat", "No nucleus", "Chloroplasts from plants always"]),
]

BANK_ORG_POP: QuestionBank = [
    q("A population is a group of:", "Individuals of a species in a given area at a given time", ["All species in a biome", "Only producers", "Only fossils"]),
    q("The J-shaped growth curve represents:", "Exponential growth", ["Logistic growth at carrying capacity", "Zero growth", "Decline only"]),
    q("Carrying capacity (K) is:", "Maximum population an environment can support", ["Birth rate", "Mutation rate", "Trophic level number"]),
    q("Mutualism is:", "Both species benefit", ["One benefits one is harmed", "Both harmed", "One benefits other unaffected"]),
    q("Camouflage is an example of:", "Adaptation", ["Mutation always", "Genetic drift always", "Gene flow always"]),
    q("Predation helps in:", "Transfer of energy to higher trophic levels", ["Stopping all evolution", "Removing all producers", "Eliminating decomposition"]),
]

BANK_ECOSYSTEM: QuestionBank = [
    q("Primary productivity is:", "Rate of biomass production by producers", ["Energy used by decomposers only", "Heat loss from earth", "Secondary consumption only"]),
    q("In a typical grazing food chain, energy flow is:", "Unidirectional from producers to consumers", ["Cyclic like nutrients only as energy", "From carnivores to plants", "Equal at every tropic level"]),
    q("The pyramid of energy is always:", "Upright", ["Inverted in ponds", "Spindle shaped", "Absent in forests"]),
    q("The 10 percent law is associated with:", "Lindeman's efficiency of energy transfer", ["Hardy–Weinberg", "Chargaff", "Mendel"]),
    q("Detritivores begin:", "Decomposition of dead organic matter", ["Photosynthesis", "Nitrification only", "Nitrogen fixation only"]),
    q("The standing state of an ecosystem refers to:", "Amount of nutrients in soil/biomass at a given time", ["Number of species worldwide", "Earth's age", "Ozone thickness only"]),
]

BANK_BIODIV: QuestionBank = [
    q("Latitudinal gradient of diversity shows:", "Highest species richness near the equator", ["Highest at poles", "Uniform worldwide", "Highest in deserts only"]),
    q("The 'Evil Quartet' of biodiversity loss includes:", "Habitat loss over-exploitation invasion and co-extinctions", ["Only volcanic eruptions", "Mendelian ratios", "Hardy–Weinberg"]),
    q("In-situ conservation includes:", "National parks and biosphere reserves", ["Cryopreservation of seeds only", "Zoos only", "Tissue culture only"]),
    q("Sacred groves are examples of:", "In-situ conservation traditions", ["Ex-situ gene banks", "GMO farms", "Mining sites"]),
    q("Ex-situ conservation includes:", "Botanical gardens zoos and seed banks", ["National parks only", "Wildlife corridors only", "Reserved forests only"]),
    q("Hotspots of biodiversity are regions with:", "High endemism and high habitat loss", ["No species", "Only marine mammals", "Zero endemism"]),
]

BANK_CELL: QuestionBank = [
    q("Ribosomes are the site of:", "Protein synthesis", ["Photosynthesis", "DNA replication only", "Lipid storage only"]),
    q("Mitochondria are described as:", "Semi-autonomous organelles with their own DNA", ["Only in prokaryotes", "Sites of glycolysis only", "Dead storage bodies"]),
    q("The fluid mosaic model describes:", "Plasma membrane structure", ["Cell wall of bacteria only", "Nuclear lamina only", "Spindle fibres"]),
    q("Lysosomes are rich in:", "Hydrolytic enzymes", ["Chlorophyll", "Haemoglobin", "Cellulose"]),
    q("Nucleolus is involved in:", "rRNA synthesis / ribosome biogenesis", ["ATP synthesis", "Lipid synthesis", "Photosystem II"]),
    q("Prokaryotic cells lack:", "A membrane-bound nucleus", ["Ribosomes", "Plasma membrane", "DNA"]),
]

BANK_PHOTO: QuestionBank = [
    q("The primary CO2 acceptor in C3 plants is:", "RuBP", ["PEP", "Pyruvate", "OAA only"]),
    q("The oxygen released in photosynthesis comes from:", "Water", ["Carbon dioxide", "ATP", "NADPH"]),
    q("C4 plants minimise photorespiration by:", "Kranz anatomy and PEP carboxylase in mesophyll", ["Closing stomata forever", "Lacking chlorophyll a", "Using only CAM at night as C3"]),
    q("PSI and PSII are located in the:", "Thylakoid membrane", ["Stroma as soluble enzymes only", "Mitochondrial matrix", "Cytoplasm"]),
    q("The Calvin cycle occurs in the:", "Stroma", ["Thylakoid lumen only", "Cytosol of animal cells", "Mitochondrial cristae"]),
    q("Photorespiration involves:", "RuBisCO oxygenase activity producing a 2-carbon compound", ["Only CAM plants at night", "Nitrogen fixation", "Glycolysis in roots only"]),
]

BANK_PLANT_RESP: QuestionBank = [
    q("Glycolysis occurs in the:", "Cytoplasm", ["Mitochondrial matrix", "Thylakoid", "Nucleus"]),
    q("Net ATP from glycolysis per glucose is:", "2 ATP", ["38 ATP", "0 ATP", "32 ATP only"]),
    q("The ETS in plants is located on the:", "Inner mitochondrial membrane", ["Cell wall", "Tonoplast only", "Nuclear envelope"]),
    q("Fermentation in yeast produces:", "Ethanol and CO2", ["Lactic acid only in yeast always", "Oxygen", "Starch"]),
    q("RQ of carbohydrates is approximately:", "1", ["0.7", "Infinity", "0"]),
    q("The link reaction converts pyruvate to:", "Acetyl CoA", ["Glucose", "RuBP", "PEP"]),
]

BANK_PHYSIOLOGY: QuestionBank = [
    q("Haemoglobin binds oxygen mainly in:", "Red blood cells", ["Plasma proteins only", "Platelets", "Lymph nodes only"]),
    q("The pacemaker of the heart is the:", "SA node", ["AV bundle only", "Purkinje fibres only as first pacemaker", "Aortic valve"]),
    q("Ultrafiltration of urine occurs in the:", "Glomerulus", ["Collecting duct only", "Urinary bladder", "Urethra"]),
    q("A synapse transmits the impulse by:", "Neurotransmitters across the synaptic cleft", ["Direct cytoplasmic fusion of axons always", "Hormones from the kidney", "Myosin sliding only"]),
    q("Insulin is secreted by:", "Pancreatic β-cells", ["Adrenal cortex", "Thyroid follicles", "Posterior pituitary"]),
    q("The functional unit of contraction in a muscle is the:", "Sarcomere", ["Nephron", "Alveolus", "Neuron soma"]),
]


def register() -> None:
    _register(
        [
            "Flower as the reproductive structure",
            "Stamen microsporangium and pollen grain",
            "Pistil megasporangium and embryo sac",
            "Pollination",
            "Pollen-pistil interaction",
            "Double fertilisation",
            "Endosperm embryo seed and fruit",
            "Apomixis and polyembryony",
            "Pre-fertilisation structures",
            "Pollination and fertilisation",
            "Post-fertilisation changes",
        ],
        BANK_FLOWER,
        "pollination",
        "embryo sac",
        "double fertilisation",
        "microsporangium",
        "apomixis",
    )
    _register(
        [
            "Male reproductive system",
            "Female reproductive system",
            "Spermatogenesis",
            "Oogenesis",
            "Menstrual cycle",
            "Fertilisation and implantation",
            "Pregnancy and embryonic development",
            "Parturition and lactation",
            "Male and female reproductive systems",
            "Gametogenesis",
            "Pregnancy and parturition",
        ],
        BANK_HUMAN_REPRO,
        "spermatogenesis",
        "oogenesis",
        "menstrual",
        "implantation",
        "parturition",
        "lactation",
    )
    _register(
        [
            "Reproductive health problems and strategies",
            "Population explosion and birth control",
            "Medical termination of pregnancy",
            "Sexually transmitted infections",
            "Infertility",
            "Assisted reproductive technologies",
            "Reproductive health problems",
            "Birth control",
        ],
        BANK_REPRO_HEALTH,
        "iud",
        "ivf",
        "saheli",
        "mtp",
        "sti",
        "infertility",
    )
    _register(
        [
            "Mendel's experiments and laws",
            "Incomplete dominance and codominance",
            "Multiple alleles and blood groups",
            "Pleiotropy and polygenic inheritance",
            "Chromosomal theory of inheritance",
            "Linkage and recombination",
            "Sex determination",
            "Mutation and genetic disorders",
            "Mendel's laws",
            "Genetic disorders",
        ],
        BANK_MENDEL,
        "mendel",
        "linkage",
        "codominance",
        "down's",
        "colour blindness",
        "pedigree",
        "test cross",
    )
    _register(
        [
            "DNA as the genetic material",
            "Structure of DNA and RNA",
            "DNA packaging",
            "DNA replication",
            "Transcription",
            "Genetic code and translation",
            "Regulation of gene expression",
            "Human genome project and DNA fingerprinting",
            "DNA as genetic material",
            "Replication transcription translation",
            "Genetic code and regulation",
        ],
        BANK_MOLECULAR,
        "hershey",
        "chargaff",
        "transcription",
        "translation",
        "lac operon",
        "fingerprinting",
        "histone",
        "replication",
    )
    _register(
        [
            "Origin of life",
            "Evidences of evolution",
            "Adaptive radiation",
            "Biological evolution and mechanisms",
            "Hardy-Weinberg principle",
            "Origin and evolution of man",
            "Mechanisms of evolution",
        ],
        BANK_EVOLUTION,
        "oparin",
        "analogous",
        "hardy",
        "industrial melanism",
        "adaptive radiation",
        "homo sapiens",
    )
    _register(
        [
            "Common infectious diseases",
            "Immunity innate and acquired",
            "Vaccination and immunisation",
            "Allergies autoimmunity and lymphoid organs",
            "AIDS and cancer",
            "Drugs and alcohol abuse",
            "Common diseases",
            "Immunity",
            "AIDS cancer and drugs",
        ],
        BANK_HEALTH,
        "innate",
        "antibody",
        "hiv",
        "vaccine",
        "malignant",
        "opioid",
        "immunity",
    )
    _register(
        [
            "Microbes in household products",
            "Microbes in industrial products",
            "Microbes in sewage treatment",
            "Microbes in biogas production",
            "Microbes as biocontrol agents",
            "Microbes as biofertilisers",
            "Microbes in household and industry",
            "Sewage treatment",
            "Biocontrol and biofertilisers",
        ],
        BANK_MICROBES,
        "lactobacillus",
        "streptokinase",
        "activated sludge",
        "biogas",
        "azotobacter",
        "thuringiensis",
        "biofertilis",
    )
    _register(
        [
            "Principles of biotechnology",
            "Restriction enzymes",
            "Cloning vectors",
            "Competent host and transformation",
            "Polymerase chain reaction",
            "Downstream processing",
            "Tools of rDNA technology",
            "Processes of recombinant DNA",
        ],
        BANK_BIOTECH_PROC,
        "restriction",
        "plasmid",
        "pcr",
        "competent",
        "selectable marker",
        "rdna",
    )
    _register(
        [
            "Biotechnological applications in agriculture",
            "Bt cotton",
            "RNA interference",
            "Biotechnological applications in medicine",
            "Transgenic animals",
            "Ethical issues and biopiracy",
            "Bt crops",
            "Ethical issues",
        ],
        BANK_BIOTECH_APP,
        "bt cotton",
        "cry gene",
        "rnai",
        "humulin",
        "biopiracy",
        "transgenic",
        "gene therapy",
    )
    _register(
        [
            "Organism and its environment",
            "Adaptations",
            "Population attributes",
            "Population growth",
            "Life history variation",
            "Population interactions",
            "Organism and environment",
            "Populations",
        ],
        BANK_ORG_POP,
        "carrying capacity",
        "mutualism",
        "camouflage",
        "exponential growth",
        "predation",
        "population",
    )
    _register(
        [
            "Ecosystem structure and function",
            "Productivity",
            "Decomposition",
            "Energy flow",
            "Ecological pyramids",
            "Nutrient cycling",
            "Ecosystem structure",
            "Productivity and energy flow",
        ],
        BANK_ECOSYSTEM,
        "primary productivity",
        "pyramid of energy",
        "10 percent",
        "detritivore",
        "standing state",
        "energy flow",
    )
    _register(
        [
            "Biodiversity and its patterns",
            "Importance of species diversity",
            "Loss of biodiversity",
            "Biodiversity conservation in situ",
            "Biodiversity conservation ex situ",
            "Sacred groves and protected areas",
            "Biodiversity patterns",
            "Conservation strategies",
        ],
        BANK_BIODIV,
        "latitudinal",
        "evil quartet",
        "in-situ",
        "ex-situ",
        "sacred grove",
        "hotspot",
        "endemism",
    )
    _register(
        [
            "Cell theory",
            "Prokaryotic cells",
            "Eukaryotic cells",
            "Endomembrane system",
            "Mitochondria and plastids",
            "Cytoskeleton cilia flagella and centrioles",
            "Nucleus",
            "Prokaryotic and eukaryotic cell",
            "Cell organelles",
        ],
        BANK_CELL,
        "ribosome",
        "mitochondri",
        "fluid mosaic",
        "lysosome",
        "nucleolus",
        "prokaryotic",
    )
    _register(
        [
            "Photosynthetic pigments",
            "Light reaction and photophosphorylation",
            "Calvin cycle",
            "C4 pathway",
            "Photorespiration",
            "Factors affecting photosynthesis",
            "Light reaction",
        ],
        BANK_PHOTO,
        "rubp",
        "photosystem",
        "calvin",
        "c4",
        "photorespiration",
        "thylakoid",
    )
    _register(
        [
            "Glycolysis",
            "Fermentation",
            "Aerobic respiration",
            "Electron transport system and oxidative phosphorylation",
            "Respiratory quotient",
            "How to analyse chemical composition",
        ],
        BANK_PLANT_RESP,
        "glycolysis",
        "fermentation",
        "respiratory quotient",
        "acetyl coa",
        "oxidative phosphorylation",
    )
    _register(
        [
            "Human respiratory system",
            "Mechanism of breathing",
            "Exchange of gases",
            "Transport of gases",
            "Regulation of respiration",
            "Disorders of the respiratory system",
            "Blood",
            "Lymph",
            "Human circulatory system",
            "Cardiac cycle",
            "ECG",
            "Human excretory system",
            "Urine formation",
            "Function of the tubules",
            "Human neural system",
            "Neuron",
            "Synapse and nerve impulse",
            "Muscle",
            "Skeletal system",
            "Human endocrine system",
            "Mechanism of hormone action",
            "Thyroid adrenal pancreas gonads",
        ],
        BANK_PHYSIOLOGY,
        "haemoglobin",
        "sa node",
        "glomerulus",
        "synapse",
        "insulin",
        "sarcomere",
        "cardiac cycle",
        "nephron",
    )
