"""CBSE 2026–27 Classes 9–10 syllabus metadata.

Sources:
- CBSE Secondary Curriculum 2026–27 (cbseacademic.nic.in/curriculum_2027.html)
- NCERT Class 9 Mathematics Ganita Manjari and Class 9 Social Science
  Understanding Society: India and Beyond, Part 1
- Class 9 Science: Exploration textbook TOC was not fully verified from ncert.nic.in;
  chapters follow the last published CBSE/NCERT Class 9 Science course structure.
- Class 10 Mathematics, Science and Social Science follow the CBSE 2026–27
  secondary course structure / current NCERT textbooks.
"""

from __future__ import annotations

from app.data.cbse_2026_27.schema import SubjectSpec, chapter, subject

CLASS_9: list[SubjectSpec] = [
    subject(
        "MATH",
        "Mathematics",
        [
            chapter(
                "Orienting Yourself: The Use of Coordinates",
                ["Coordinate plane", "Plotting points", "Reading graphs"],
            ),
            chapter(
                "Introduction to Linear Polynomials",
                ["Polynomials in one variable", "Zeroes of a polynomial", "Linear polynomials"],
            ),
            chapter(
                "The World of Numbers",
                ["Real numbers", "Irrational numbers", "Number line representation"],
            ),
            chapter(
                "Exploring Algebraic Identities",
                ["Standard identities", "Expanding products", "Factorisation ideas"],
            ),
            chapter(
                "I'm Up and Down, and Round and Round",
                ["Linear motion graphs", "Circular ideas", "Relating algebra and graphs"],
            ),
            chapter(
                "Measuring Space: Perimeter and Area",
                ["Perimeter of plane figures", "Area of triangles and quadrilaterals", "Composite figures"],
            ),
            chapter(
                "The Mathematics of Maybe: Introduction to Probability",
                ["Chance and outcomes", "Experimental probability", "Simple events"],
            ),
            chapter(
                "Predicting What Comes Next: Exploring Sequences",
                ["Number sequences", "Patterns and rules", "Next-term reasoning"],
            ),
        ],
    ),
    subject(
        "SCI",
        "Science",
        [
            chapter(
                "Matter in Our Surroundings",
                ["States of matter", "Change of state", "Diffusion and evaporation"],
            ),
            chapter(
                "Is Matter Around Us Pure?",
                ["Mixtures and solutions", "Separation of mixtures", "Compounds and elements"],
            ),
            chapter(
                "Atoms and Molecules",
                ["Laws of chemical combination", "Atoms and molecules", "Mole concept basics"],
            ),
            chapter(
                "Structure of the Atom",
                ["Electrons protons neutrons", "Atomic models", "Valency and atomic number"],
            ),
            chapter(
                "The Fundamental Unit of Life",
                ["Cell theory", "Cell organelles", "Prokaryotic and eukaryotic cells"],
            ),
            chapter(
                "Tissues",
                ["Plant tissues", "Animal tissues", "Functions of tissues"],
            ),
            chapter(
                "Motion",
                ["Distance and displacement", "Speed and velocity", "Acceleration and graphs"],
            ),
            chapter(
                "Force and Laws of Motion",
                ["Balanced and unbalanced forces", "Newton's laws", "Momentum"],
            ),
            chapter(
                "Gravitation",
                ["Universal gravitation", "Free fall", "Mass and weight"],
            ),
            chapter(
                "Work and Energy",
                ["Work", "Kinetic and potential energy", "Conservation of energy"],
            ),
            chapter(
                "Sound",
                ["Production of sound", "Propagation and speed", "Reflection and echo"],
            ),
            chapter(
                "Improvement in Food Resources",
                ["Crop production", "Animal husbandry", "Food security ideas"],
            ),
        ],
    ),
    subject(
        "SST",
        "Social Science",
        [
            chapter(
                "Understanding Social Science",
                ["What social science studies", "History geography civics economics together", "Sources and enquiry"],
            ),
            chapter(
                "Shaping of the Earth's Surface",
                ["Internal processes", "External processes", "Landforms"],
            ),
            chapter(
                "Atmosphere and Climate",
                ["Composition of atmosphere", "Weather and climate", "Climatic controls"],
            ),
            chapter(
                "Early Humans and Beginning of Civilisation",
                ["Hunter-gatherers", "Beginnings of farming", "Early cities"],
            ),
            chapter(
                "State and Society up to 1000 CE",
                ["Early states", "Society and economy", "Cultural life"],
            ),
            chapter(
                "Democracy",
                ["What is democracy", "Features of democracy", "Why democracy"],
            ),
            chapter(
                "Elections",
                ["Why elections", "Electoral process", "Free and fair elections"],
            ),
            chapter(
                "Building Blocks in Economics",
                ["Wants and resources", "Production and consumption", "The economic problem"],
            ),
            chapter(
                "The Price Puzzle",
                ["Demand", "Supply", "How prices are formed"],
            ),
        ],
    ),
    subject(
        "ENG",
        "English",
        [
            chapter(
                "Beehive Prose",
                ["The Fun They Had", "The Sound of Music", "The Little Girl", "A Truly Beautiful Mind"],
            ),
            chapter(
                "Beehive Stories and Drama",
                ["The Snake and the Mirror", "My Childhood", "Reach for the Top", "Kathmandu", "If I Were You"],
            ),
            chapter(
                "Beehive Poems",
                ["The Road Not Taken", "Wind", "Rain on the Roof", "The Lake Isle of Innisfree"],
            ),
            chapter(
                "Moments",
                ["The Lost Child", "The Adventures of Toto", "Iswaran the Storyteller", "In the Kingdom of Fools"],
            ),
        ],
    ),
]

CLASS_10: list[SubjectSpec] = [
    subject(
        "MATH",
        "Mathematics",
        [
            chapter("Real Numbers", ["Fundamental theorem of arithmetic", "Revisiting irrational numbers", "Decimal expansions"]),
            chapter("Polynomials", ["Zeroes of a polynomial", "Relationship between zeroes and coefficients", "Division algorithm idea"]),
            chapter("Pair of Linear Equations in Two Variables", ["Graphical method", "Algebraic methods", "Applications"]),
            chapter("Quadratic Equations", ["Standard form", "Nature of roots", "Solving quadratic equations"]),
            chapter("Arithmetic Progressions", ["nth term", "Sum of n terms", "Applications"]),
            chapter("Triangles", ["Similar triangles", "Criteria for similarity", "Pythagoras theorem"]),
            chapter("Coordinate Geometry", ["Distance formula", "Section formula", "Area of a triangle"]),
            chapter("Introduction to Trigonometry", ["Trigonometric ratios", "Identities", "Values of standard angles"]),
            chapter("Some Applications of Trigonometry", ["Heights and distances", "Angle of elevation", "Angle of depression"]),
            chapter("Circles", ["Tangent to a circle", "Number of tangents from a point", "Properties of tangents"]),
            chapter("Areas Related to Circles", ["Perimeter and area of a circle", "Sectors and segments", "Combinations of plane figures"]),
            chapter("Surface Areas and Volumes", ["Surface area of solids", "Volume of solids", "Combination of solids"]),
            chapter("Statistics", ["Mean", "Median", "Mode of grouped data"]),
            chapter("Probability", ["Classical probability", "Simple events", "Complementary events"]),
        ],
    ),
    subject(
        "SCI",
        "Science",
        [
            chapter("Chemical Reactions and Equations", ["Writing chemical equations", "Types of reactions", "Oxidation and reduction"]),
            chapter("Acids, Bases and Salts", ["Properties of acids and bases", "pH", "Important salts"]),
            chapter("Metals and Non-metals", ["Physical properties", "Chemical properties", "Ionic compounds"]),
            chapter("Carbon and its Compounds", ["Covalent bonding", "Functional groups", "Soaps and detergents"]),
            chapter("Life Processes", ["Nutrition", "Respiration", "Transportation and excretion"]),
            chapter("Control and Coordination", ["Nervous system", "Hormones in animals", "Coordination in plants"]),
            chapter("How do Organisms Reproduce?", ["Asexual reproduction", "Sexual reproduction in plants", "Reproduction in humans"]),
            chapter("Heredity", ["Traits and variation", "Mendel's experiments", "Sex determination"]),
            chapter("Light — Reflection and Refraction", ["Reflection by spherical mirrors", "Refraction", "Lenses"]),
            chapter("The Human Eye and the Colourful World", ["Human eye", "Defects of vision", "Dispersion and scattering"]),
            chapter("Electricity", ["Electric current and circuit", "Ohm's law", "Heating effect of current"]),
            chapter("Magnetic Effects of Electric Current", ["Magnetic field", "Force on a current-carrying conductor", "Electromagnetic induction"]),
            chapter("Our Environment", ["Ecosystems", "Food chains and webs", "Ozone and waste"]),
        ],
    ),
    subject(
        "SST",
        "Social Science",
        [
            chapter("The Rise of Nationalism in Europe", ["French Revolution and nation", "Making of nationalism in Europe", "Nation-states"]),
            chapter("Nationalism in India", ["First World War and nationalism", "Non-Cooperation and Civil Disobedience", "Sense of collective belonging"]),
            chapter("The Making of a Global World", ["Pre-modern world", "Nineteenth-century world economy", "Post-war era"]),
            chapter("The Age of Industrialisation", ["Before the Industrial Revolution", "Factories come up", "Industrialisation in India"]),
            chapter("Print Culture and the Modern World", ["First printed books", "Print revolution", "Print in India"]),
            chapter("Resources and Development", ["Types of resources", "Resource planning", "Land and soil resources"]),
            chapter("Forest and Wildlife Resources", ["Flora and fauna in India", "Conservation", "Community and conservation"]),
            chapter("Water Resources", ["Water scarcity", "Multipurpose projects", "Rainwater harvesting"]),
            chapter("Agriculture", ["Types of farming", "Cropping patterns", "Food security ideas"]),
            chapter("Minerals and Energy Resources", ["Mineral occurrence", "Conventional energy", "Non-conventional energy"]),
            chapter("Manufacturing Industries", ["Importance of manufacturing", "Classification of industries", "Industrial pollution"]),
            chapter("Lifelines of National Economy", ["Transport", "Communication", "International trade"]),
            chapter("Power Sharing", ["Belgium and Sri Lanka", "Forms of power sharing", "Why power sharing"]),
            chapter("Federalism", ["What is federalism", "Federalism in India", "Decentralisation"]),
            chapter("Gender, Religion and Caste", ["Gender and politics", "Religion and politics", "Caste and politics"]),
            chapter("Political Parties", ["Why parties", "National and state parties", "Challenges to parties"]),
            chapter("Outcomes of Democracy", ["Accountable government", "Economic outcomes", "Dignity and freedom"]),
            chapter("Development", ["What development means", "National income ideas", "Sustainability"]),
            chapter("Sectors of the Indian Economy", ["Primary secondary tertiary", "Organised and unorganised", "Employment"]),
            chapter("Money and Credit", ["Money as a medium of exchange", "Formal credit", "Informal credit"]),
            chapter("Globalisation and the Indian Economy", ["Production across countries", "Foreign trade", "Impact of globalisation"]),
        ],
    ),
    subject(
        "ENG",
        "English",
        [
            chapter(
                "First Flight Prose",
                ["A Letter to God", "Nelson Mandela: Long Walk to Freedom", "Two Stories about Flying", "From the Diary of Anne Frank"],
            ),
            chapter(
                "First Flight India and Everyday Life",
                ["Glimpses of India", "Mijbil the Otter", "Madam Rides the Bus", "The Sermon at Benares", "The Proposal"],
            ),
            chapter(
                "First Flight Poems",
                ["Dust of Snow", "Fire and Ice", "A Tiger in the Zoo", "The Ball Poem", "Amanda"],
            ),
            chapter(
                "Footprints without Feet",
                ["A Triumph of Surgery", "The Thief's Story", "The Midnight Visitor", "A Question of Trust", "Footprints without Feet"],
            ),
        ],
    ),
]
