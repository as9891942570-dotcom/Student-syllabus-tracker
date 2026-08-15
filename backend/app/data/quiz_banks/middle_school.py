"""Class 6–10 Science, Maths, Social Science, and English banks. No Physics fallback."""

from __future__ import annotations

from app.data.quiz_banks.common import q, register_keys, register_subject_keywords
from app.data.quiz_concepts import QuestionBank

BANK_SCI_MATTER: QuestionBank = [
    q("Matter exists commonly in how many physical states at room conditions on Earth?", "Three: solid, liquid and gas", ["One only", "Ten", "Plasma only"]),
    q("Evaporation is:", "Change of liquid to vapour at the surface below boiling point", ["Change of gas to solid", "A nuclear reaction", "Melting of ice only"]),
    q("A magnet has:", "Two poles, north and south", ["One pole only", "No poles", "Four electric charges"]),
    q("The SI unit of length is the:", "Metre", ["Litre", "Kilogram", "Ampere"]),
    q("Filtration separates:", "Insoluble solid from a liquid", ["Salt dissolved in water completely as the only method", "Gases from gases by melting", "Heat from light"]),
    q("A balanced diet includes:", "Carbohydrates, proteins, fats, vitamins, minerals and water", ["Only sugar", "Only oils", "Only spices"]),
]

BANK_SCI_LIVING: QuestionBank = [
    q("Living organisms typically show:", "Growth, reproduction and response to stimuli", ["Only rusting", "Only melting", "Absence of cells"]),
    q("Photosynthesis in green plants needs:", "Chlorophyll, light, water and carbon dioxide", ["Nitrogen gas only", "Soil colour only", "Moonlight only as the unique requirement"]),
    q("The basic unit of life is the:", "Cell", ["Organ", "Tissue of granite", "Atom of gold as a living unit"]),
    q("Respiration in organisms releases:", "Energy from food", ["Only nitrogen from air as energy", "Light from chlorophyll as a rule", "Soil minerals as ATP"]),
    q("Habitats are:", "Places where organisms live", ["Only deserts", "Only textbooks", "Only factories"]),
    q("A herbivore eats:", "Plants", ["Only metal", "Only other carnivores as a definition", "Rocks"]),
]

BANK_MATH_NUMBER: QuestionBank = [
    q("A prime number has:", "Exactly two distinct positive factors, 1 and itself", ["No factors", "All even factors", "Infinitely many even factors"]),
    q("The LCM of 4 and 6 is:", "12", ["2", "24", "1"]),
    q("A fraction with numerator smaller than denominator is:", "Proper", ["Improper", "Mixed always", "Negative always"]),
    q("Integers include:", "Positive numbers, negative numbers and zero", ["Only natural numbers greater than 100", "Only fractions between 0 and 1", "Only primes"]),
    q("Place value of 5 in 350 is:", "50", ["5", "500", "0"]),
    q("Perimeter of a rectangle of length 8 and breadth 3 is:", "22", ["24", "11", "5"]),
]

BANK_MATH_GEO: QuestionBank = [
    q("A triangle has how many sides?", "3", ["2", "4", "5"]),
    q("An angle of 90° is:", "A right angle", ["An acute angle only", "A reflex angle", "A straight angle"]),
    q("A line of symmetry divides a figure into:", "Two mirror-image halves", ["Three equal primes", "Random pieces", "Four irrational parts"]),
    q("The sum of angles of a triangle is:", "180°", ["90°", "360°", "0°"]),
    q("Area of a square of side 5 is:", "25", ["10", "20", "5"]),
    q("A circle's radius is:", "Distance from centre to a point on the circle", ["Its diameter times 3", "Its circumference always", "A chord that is longest as radius by definition"]),
]

BANK_SST: QuestionBank = [
    q("Latitudes are:", "Imaginary lines parallel to the equator", ["Lines from pole to pole as longitudes", "Ocean currents", "Plate names"]),
    q("A globe is:", "A spherical model of the Earth", ["A flat political cartoon", "A type of ruler", "A calendar"]),
    q("Harappan cities are known for:", "Planned streets and drainage", ["Skyscrapers of steel", "Printing presses", "Steam engines"]),
    q("A gram sabha is:", "A village assembly of voters", ["A national parliament only", "A type of festival", "A mountain range"]),
    q("Democracy means:", "Rule by the people through participation and votes", ["Rule by one family only as a definition", "Absence of laws", "Rule by the army only"]),
    q("Livelihoods are:", "Ways people earn a living", ["Only hobbies", "Only sports", "Only weather reports"]),
]

BANK_ENG_MS: QuestionBank = [
    q("A fable usually ends with:", "A moral or lesson", ["A chemical equation", "A cricket score only", "A weather forecast only"]),
    q("The past tense of 'go' is:", "Went", ["Goed", "Gone as the simple past only", "Going"]),
    q("A noun names:", "A person, place, thing or idea", ["Only an action", "Only a quality of verbs", "A sentence type"]),
    q("An adjective describes:", "A noun", ["Only a verb always", "A full stop", "A paragraph indent"]),
    q("A synonym of 'happy' is:", "Joyful", ["Sad", "Angry", "Empty"]),
    q("Comprehension of an unseen passage means:", "Understanding and answering from the given text", ["Ignoring the text", "Copying a poem from memory only", "Translating a formula"]),
]


def register() -> None:
    register_keys(
        [
            "Solid liquid gas",
            "Melting and boiling",
            "Evaporation and condensation",
            "Magnetic and non-magnetic materials",
            "Poles of a magnet",
            "Standard units of length",
            "Measuring length",
            "Types of motion",
            "Objects and materials",
            "Properties of materials",
            "Handpicking and sieving",
            "Filtration and sedimentation",
            "Food groups",
            "Balanced diet",
            "Hot and cold",
            "Thermometers",
        ],
        BANK_SCI_MATTER,
    )
    register_keys(
        [
            "Grouping living things",
            "Plants and animals around us",
            "Habitats",
            "Life processes",
            "Growth and movement",
            "What scientists do",
            "Observation and questions",
        ],
        BANK_SCI_LIVING,
    )
    register_subject_keywords("SCI", [
        (("solid", "liquid", "evaporat", "magnet", "filtr", "thermometr", "matter"), BANK_SCI_MATTER),
        (("habitat", "cell", "photosynth", "living", "organism", "herbivore"), BANK_SCI_LIVING),
    ])
    register_keys(
        [
            "Factors and multiples",
            "Prime and composite numbers",
            "Divisibility",
            "Proper and improper fractions",
            "Equivalent fractions",
            "Integers on the number line",
            "Negative numbers",
            "Place value",
            "Comparing numbers",
            "Perimeter of polygons",
            "Area of rectangles",
        ],
        BANK_MATH_NUMBER,
    )
    register_keys(
        [
            "Points and lines",
            "Types of angles",
            "Measuring angles",
            "Line symmetry",
            "Using a ruler and compass",
        ],
        BANK_MATH_GEO,
    )
    register_subject_keywords("MATH", [
        (("prime", "fraction", "integer", "perimeter", "place value", "factor"), BANK_MATH_NUMBER),
        (("angle", "symmetry", "triangle", "circle", "square"), BANK_MATH_GEO),
    ])
    register_keys(
        [
            "Maps and globes",
            "Latitudes and longitudes",
            "Finding places",
            "Harappan cities",
            "Gram sabha",
            "What is government",
            "Why rules are needed",
        ],
        BANK_SST,
    )
    register_subject_keywords("SST", [
        (("latitude", "globe", "harappan", "gram sabha", "democracy", "livelihood", "map"), BANK_SST),
    ])
    register_keys(
        ["A Bottle of Dew", "The Raven and the Fox", "Rama to the Rescue", "The Chair"],
        BANK_ENG_MS,
    )
    register_subject_keywords("ENG", [
        (("fable", "moral", "unseen passage", "noun", "adjective", "synonym"), BANK_ENG_MS),
    ])
