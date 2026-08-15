"""CBSE 2026–27 Classes 6–10 syllabus metadata.

Sources:
- NCERT textbooks (ncert.nic.in) for Classes 6–8 (NEP/NCF books: Ganita Prakash, Curiosity, Exploring Society, Poorvi)
- CBSE Secondary Curriculum 2026–27 (cbseacademic.nic.in/curriculum_2027.html) for Classes 9–10
- Class 9 Mathematics uses NCERT Ganita Manjari (2026–27)
- Class 9 Social Science uses Understanding Society: India and Beyond, Part 1
- Class 9 Science: Exploration book chapter titles were not fully verified from NCERT TOC;
  the listed Science chapters follow the last published CBSE/NCERT Class 9 Science course structure.
"""

from __future__ import annotations

from app.data.cbse_2026_27.schema import SubjectSpec, chapter, subject


CLASS_6: list[SubjectSpec] = [
    subject(
        "MATH",
        "Mathematics",
        [
            chapter("Patterns in Mathematics", ["Number patterns", "Shape patterns", "Growing patterns"]),
            chapter("Lines and Angles", ["Points and lines", "Types of angles", "Measuring angles"]),
            chapter("Number Play", ["Place value", "Comparing numbers", "Number puzzles"]),
            chapter("Data Handling and Presentation", ["Collecting data", "Pictographs and bar graphs", "Reading data"]),
            chapter("Prime Time", ["Factors and multiples", "Prime and composite numbers", "Divisibility"]),
            chapter("Perimeter and Area", ["Perimeter of polygons", "Area of rectangles", "Units of measurement"]),
            chapter("Fractions", ["Proper and improper fractions", "Equivalent fractions", "Comparing fractions"]),
            chapter("Playing with Constructions", ["Using a ruler and compass", "Constructing lines and angles", "Simple geometric figures"]),
            chapter("Symmetry", ["Line symmetry", "Reflection", "Symmetrical shapes"]),
            chapter("The Other Side of Zero", ["Integers on the number line", "Negative numbers", "Comparing integers"]),
        ],
    ),
    subject(
        "SCI",
        "Science",
        [
            chapter("The Wonderful World of Science", ["What scientists do", "Observation and questions", "Everyday science"]),
            chapter("Diversity in the Living World", ["Grouping living things", "Plants and animals around us", "Habitats"]),
            chapter("Mindful Eating: A Path to a Healthy Body", ["Food groups", "Balanced diet", "Food habits"]),
            chapter("Exploring Magnets", ["Magnetic and non-magnetic materials", "Poles of a magnet", "Uses of magnets"]),
            chapter("Measurement of Length and Motion", ["Standard units of length", "Measuring length", "Types of motion"]),
            chapter("Materials Around Us", ["Objects and materials", "Properties of materials", "Grouping materials"]),
            chapter("Temperature and its Measurement", ["Hot and cold", "Thermometers", "Reading temperature"]),
            chapter("A Journey through States of Water", ["Solid liquid gas", "Melting and boiling", "Evaporation and condensation"]),
            chapter("Methods of Separation in Everyday Life", ["Handpicking and sieving", "Filtration and sedimentation", "Evaporation as separation"]),
            chapter("Living Creatures: Exploring their Characteristics", ["Life processes", "Growth and movement", "Response to surroundings"]),
            chapter("Nature's Treasures", ["Air water soil", "Forests and minerals", "Using resources carefully"]),
            chapter("Beyond Earth", ["The night sky", "Moon and stars", "Earth in space"]),
        ],
    ),
    subject(
        "SST",
        "Social Science",
        [
            chapter("Locating Places on the Earth", ["Maps and globes", "Latitudes and longitudes", "Finding places"]),
            chapter("Oceans and Continents", ["Major continents", "Oceans of the world", "Land and water"]),
            chapter("Landforms and Life", ["Mountains plains plateaus", "How landforms affect life", "Local landforms"]),
            chapter("Timeline and Sources of History", ["Counting time in history", "Sources of the past", "Why timelines matter"]),
            chapter("India, That Is Bharat", ["Names of India", "Unity of the land", "People and regions"]),
            chapter("The Beginnings of Indian Civilisation", ["Early settlements", "Harappan cities", "Life in early cities"]),
            chapter("India's Cultural Roots", ["Languages and traditions", "Stories and knowledge systems", "Shared cultural ideas"]),
            chapter("Unity in Diversity, or Many in the One", ["Diversity in India", "Festivals and food", "Living together"]),
            chapter("Family and Community", ["Family roles", "Community life", "Helping one another"]),
            chapter("Grassroots Democracy — Governance", ["What is government", "Why rules are needed", "Local decision making"]),
            chapter("Grassroots Democracy — Rural Local Government", ["Panchayati raj", "Gram sabha", "Village development"]),
            chapter("Grassroots Democracy — Urban Local Government", ["Municipal bodies", "Urban services", "Citizen participation"]),
            chapter("The Value of Work", ["Kinds of work", "Dignity of labour", "Work in the community"]),
            chapter("Economic Activities Around Us", ["Farming and making goods", "Trade and services", "Livelihoods"]),
        ],
    ),
    subject(
        "ENG",
        "English",
        [
            chapter("Fables and Folk Tales", ["A Bottle of Dew", "The Raven and the Fox", "Rama to the Rescue"]),
            chapter("Friendship", ["The Chair", "Neem Baba", "What a Bird Thought"]),
            chapter("Nurturing Nature", ["The Unlikely Best Friends", "A Friend's Prayer", "The Olive Ridley Turtles"]),
            chapter("Sports and Wellness", ["Change of Heart", "The Winner", "Yoga — A Way of Life"]),
            chapter("Culture and Traditions", ["Hamara Bharat — Incredible India!", "The Kites", "Ila Sachani: Embroidering Dreams with Determination"]),
        ],
    ),
]

CLASS_7: list[SubjectSpec] = [
    subject(
        "MATH",
        "Mathematics",
        [
            chapter("Large Numbers Around Us", ["Indian place-value system", "Lakhs and crores", "Estimating large numbers"]),
            chapter("Arithmetic Expressions", ["Terms and operations", "Order of operations", "Writing expressions"]),
            chapter("A Peek Beyond the Point", ["Decimal place value", "Adding and subtracting decimals", "Decimals on the number line"]),
            chapter("Expressions using Letter-Numbers", ["Letters for numbers", "Simple algebraic expressions", "Evaluating expressions"]),
            chapter("Parallel and Intersecting Lines", ["Intersecting lines", "Parallel lines", "Angles formed by a transversal"]),
            chapter("Number Play", ["Number patterns", "Parity", "Puzzles with numbers"]),
            chapter("A Tale of Three Intersecting Lines", ["Triangles and their sides", "Angle sum in a triangle", "Types of triangles"]),
            chapter("Working with Fractions", ["Multiplying fractions", "Dividing fractions", "Fraction word problems"]),
            chapter("Geometric Twins", ["Congruent figures", "Matching sides and angles", "Recognising congruence"]),
            chapter("Integers — Multiplication and Division", ["Multiplying integers", "Dividing integers", "Rules of signs"]),
            chapter("Finding Common Ground", ["Common factors", "HCF and LCM", "Prime factorisation"]),
            chapter("Another Peek Beyond the Point", ["Multiplying decimals", "Dividing decimals", "Decimal operations in context"]),
            chapter("Connecting the Dots", ["Mean", "Median", "Mode"]),
            chapter("Constructions and Tilings", ["Basic constructions", "Tilings and patterns", "Practical geometry"]),
            chapter("Finding the Unknown", ["Simple equations", "Solving for a letter-number", "Checking solutions"]),
        ],
    ),
    subject(
        "SCI",
        "Science",
        [
            chapter("The Ever-Evolving World of Science", ["Scientific questions", "Observation and evidence", "Science in daily life"]),
            chapter("Exploring Substances: Acidic, Basic and Neutral", ["Acids and bases around us", "Indicators", "Neutral substances"]),
            chapter("Electricity: Circuits and their Components", ["Electric circuits", "Conductors and insulators", "Circuit components"]),
            chapter("The World of Metals and Non-metals", ["Properties of metals", "Properties of non-metals", "Everyday uses"]),
            chapter("Changes Around Us: Physical and Chemical", ["Physical changes", "Chemical changes", "Recognising a chemical change"]),
            chapter("Adolescence: A Stage of Growth and Change", ["Changes at adolescence", "Health and hygiene", "Growing up responsibly"]),
            chapter("Heat Transfer in Nature", ["Conduction convection radiation", "Sea breeze and land breeze", "Insulators"]),
            chapter("Measurement of Time and Motion", ["Measuring time", "Speed", "Distance-time"]),
            chapter("Life Processes in Animals", ["Nutrition in animals", "Breathing and circulation", "Excretion"]),
            chapter("Life Processes in Plants", ["Photosynthesis", "Transport in plants", "Plant growth"]),
            chapter("Light: Shadows and Reflections", ["Shadows", "Reflection of light", "Mirrors"]),
            chapter("Earth, Moon and the Sun", ["Motions of Earth", "Moon phases", "Eclipses"]),
        ],
    ),
    subject(
        "SST",
        "Social Science",
        [
            chapter("Geographical Diversity of India", ["Physical regions of India", "Climate and vegetation", "People and places"]),
            chapter("Understanding the Weather", ["Weather and climate", "Rainfall and temperature", "Reading weather"]),
            chapter("Climates of India", ["Climatic regions", "Monsoon", "How climate affects life"]),
            chapter("New Beginnings: Cities and States", ["Early cities", "Janapadas and mahajanapadas", "New political centres"]),
            chapter("The Rise of Empires", ["Why empires formed", "Administration and trade", "Life in empire times"]),
            chapter("India's Cultural Roots", ["Traditions and learning", "Art and architecture", "Shared heritage"]),
            chapter("The Gupta Era: An Age of Tireless Creativity", ["Gupta polity", "Knowledge and literature", "Art of the period"]),
            chapter("How the Land Becomes Sacred", ["Sacred geography", "Pilgrimage and places", "Cultural landscapes"]),
            chapter("From the Rulers to the Ruled: Types of Governments", ["Forms of government", "Democracy and other systems", "Why government matters"]),
            chapter("The Constitution of India: An Introduction", ["Why a constitution", "Key features", "Rights and duties"]),
            chapter("From Barter to Money", ["Barter", "Need for money", "Modern money"]),
            chapter("Understanding Markets", ["Buyers and sellers", "Local markets", "How prices are formed"]),
            chapter("India and Her Neighbours", ["Neighbouring countries", "Borders and regions", "Connections across borders"]),
            chapter("Empires and Kingdoms: 6th to 10th Centuries", ["Regional kingdoms", "Trade and culture", "Political change"]),
            chapter("Turning Tides: 11th and 12th Centuries", ["New powers", "Society and economy", "Cultural encounters"]),
            chapter("India, a Home to Many", ["Linguistic diversity", "Religious diversity", "Living together"]),
            chapter("The State, the Government and You", ["Levels of government", "How citizens participate", "Public services"]),
            chapter("Infrastructure: Engine of India's Development", ["Transport and energy", "Communication", "Why infrastructure matters"]),
            chapter("Banks and the Magic of Finance", ["What banks do", "Saving and credit", "Role of finance"]),
        ],
    ),
    subject(
        "ENG",
        "English",
        [
            chapter("Learning Together", ["Reading together", "Classroom talk", "Writing a short paragraph"]),
            chapter("Wit and Humour", ["Humorous verse", "Comic situations", "Writing a funny incident"]),
            chapter("Dreams and Discoveries", ["Poems of hope", "Stories of discovery", "Descriptive writing"]),
            chapter("Travel and Adventure", ["Travel writing", "Adventure narrative", "Diary entry"]),
            chapter("Bravehearts", ["Courage in stories", "Character sketch", "Speech and dialogue"]),
        ],
    ),
]

CLASS_8: list[SubjectSpec] = [
    subject(
        "MATH",
        "Mathematics",
        [
            chapter("A Square and A Cube", ["Square numbers", "Cube numbers", "Patterns in squares and cubes"]),
            chapter("Power Play", ["Exponents", "Laws of exponents", "Large numbers in exponential form"]),
            chapter("A Story of Numbers", ["How number systems developed", "Place value", "Rational numbers"]),
            chapter("Quadrilaterals", ["Types of quadrilaterals", "Properties of sides and angles", "Diagonals"]),
            chapter("Number Play", ["Number properties", "Patterns and puzzles", "Reasoning with numbers"]),
            chapter("We Distribute, Yet Things Multiply", ["Distributive property", "Algebraic expressions", "Multiplying expressions"]),
            chapter("Proportional Reasoning-1", ["Ratio", "Equivalent ratios", "Direct proportion"]),
            chapter("Fractions in Disguise", ["Equivalent fractions", "Operations with rational numbers", "Fractions in context"]),
            chapter("The Baudhayana–Pythagoras Theorem", ["Right-angled triangles", "Pythagoras relation", "Simple applications"]),
            chapter("Proportional Reasoning-2", ["Inverse proportion", "Unitary method", "Comparing quantities"]),
            chapter("Exploring Some Geometrical Themes", ["Angles and shapes", "Geometric reasoning", "Visual proofs"]),
            chapter("Tales by Dots and Lines", ["Points lines planes", "Coordinate ideas", "Connecting geometry and numbers"]),
            chapter("Algebra Play", ["Identities", "Simplifying expressions", "Using algebra to generalise"]),
            chapter("Area", ["Area of polygons", "Composite shapes", "Surface ideas"]),
        ],
    ),
    subject(
        "SCI",
        "Science",
        [
            chapter("Exploring the Investigative World of Science", ["Asking scientific questions", "Experiments and evidence", "Science around us"]),
            chapter("The Invisible Living World: Beyond Our Naked Eye", ["Microorganisms", "Useful and harmful microbes", "Seeing the unseen"]),
            chapter("Health: The Ultimate Treasure", ["Health and disease", "Hygiene", "Healthy habits"]),
            chapter("Electricity: Magnetic and Heating Effects", ["Heating effect of current", "Magnetic effect of current", "Everyday electrical devices"]),
            chapter("Exploring Forces", ["Contact and non-contact forces", "Balanced and unbalanced forces", "Effects of force"]),
            chapter("Pressure, Winds, Storms and Cyclones", ["Pressure in fluids", "Winds", "Storms and safety"]),
            chapter("Particulate Nature of Matter", ["Particles of matter", "States of matter", "Diffusion"]),
            chapter("Nature of Matter: Elements, Compounds and Mixtures", ["Elements and compounds", "Mixtures", "Separation ideas"]),
            chapter("The Amazing World of Solutes, Solvents and Solutions", ["Solutions", "Solubility", "Concentration in daily life"]),
            chapter("Light: Mirrors and Lenses", ["Reflection", "Spherical mirrors", "Lenses"]),
            chapter("Keeping Time with the Skies", ["Day and night", "Calendars and seasons", "Celestial cycles"]),
            chapter("How Nature Works in Harmony", ["Ecosystems", "Food chains", "Balance in nature"]),
            chapter("Our Home: Earth, a Unique Life-Sustaining Planet", ["Earth's special features", "Air water soil", "Protecting Earth"]),
        ],
    ),
    subject(
        "SST",
        "Social Science",
        [
            chapter("Natural Resources and Their Use", ["Types of resources", "Using resources", "Conservation"]),
            chapter("Reshaping India's Political Map", ["Medieval political changes", "Regional powers", "Maps of the period"]),
            chapter("The Rise of the Marathas", ["Shivaji and the Maratha polity", "Administration", "Expansion"]),
            chapter("The Colonial Era in India", ["Company power", "Colonial rule", "Impact on economy and society"]),
            chapter("Universal Franchise and India's Electoral System", ["Right to vote", "Elections", "Election Commission"]),
            chapter("The Parliamentary System: Legislature and Executive", ["Parliament", "Law making", "The executive"]),
            chapter("Factors of Production", ["Land labour capital", "Organisation of production", "How goods are produced"]),
        ],
    ),
    subject(
        "ENG",
        "English",
        [
            chapter("Wit and Wisdom", ["Reading for humour and idea", "Vocabulary in context", "Paragraph writing"]),
            chapter("Values and Dispositions", ["Stories of values", "Character and choice", "Diary writing"]),
            chapter("Mystery and Magic", ["Narrative reading", "Descriptive language", "Story writing"]),
            chapter("Environment", ["Nature writing", "Factual reading", "Notice and article"]),
            chapter("Science and Curiosity", ["Informative texts", "Explaining a process", "Report writing"]),
        ],
    ),
]
