"""Class 11–12 Commerce and Humanities banks. Never use Physics fallback."""

from __future__ import annotations

from app.data.quiz_banks.common import q, register_keys, register_subject_keywords
from app.data.quiz_concepts import QuestionBank

BANK_ACC: QuestionBank = [
    q("The accounting equation is:", "Assets = Liabilities + Capital", ["Assets = Capital − Liabilities only as the unique form", "Revenue = Assets", "Cash = Profit always"]),
    q("A journal is:", "The book of original entry", ["A balance sheet", "A cash flow only", "An audit report only"]),
    q("Depreciation is:", "Allocation of the depreciable amount of an asset over its useful life", ["An increase in asset value always", "A liability to owners", "Cash withdrawn by the partner"]),
    q("A trial balance checks:", "Arithmetical accuracy of ledger balances", ["Whether the firm is solvent always", "Market price of shares", "GST rates"]),
    q("Goodwill is:", "An intangible asset representing reputation", ["A current liability always", "Cash in hand", "A type of bill of exchange"]),
    q("A cash flow statement classifies cash flows into:", "Operating, investing and financing activities", ["Debit and credit only", "Assets and drawings only", "Personal and real only"]),
]

BANK_BST: QuestionBank = [
    q("Management is:", "A process of planning, organising, staffing, directing and controlling", ["Only a government department", "Only accounting", "A type of machine"]),
    q("Fayol's principle of unity of command means:", "An employee should receive orders from one superior", ["Many bosses for one worker", "No planning", "Only piece-rate wages"]),
    q("Delegation means:", "Entrusting responsibility and authority to a subordinate", ["Centralising all decisions", "Closing a department", "Hiring consultants only"]),
    q("Working capital is associated with:", "Day-to-day operations and current assets/liabilities", ["Only purchase of land", "Only dividends", "Only audit fees"]),
    q("SEBI regulates:", "The securities market in India", ["Income tax only", "Municipal water", "School textbooks"]),
    q("A consumer has the right to:", "Be informed, safety, choose, and seek redressal", ["Ignore all labels", "Print currency", "Fix GST"]),
]

BANK_ECO: QuestionBank = [
    q("GDP measures:", "The market value of final goods and services produced in a country in a period", ["Only gold reserves", "Population only", "Rainfall"]),
    q("Inflation refers to:", "A sustained rise in the general price level", ["A fall in money supply only as definition", "A budget surplus", "A trade surplus always"]),
    q("The central bank of India is:", "The Reserve Bank of India", ["SEBI", "NABARD as the unique central bank", "A commercial bank branch"]),
    q("Demand usually slopes:", "Downward from left to right", ["Upward always without exception", "As a vertical line only", "As a circle"]),
    q("A production possibility curve shows:", "Trade-offs between two goods given resources", ["Only inflation", "Only money supply", "Election results"]),
    q("Fiscal deficit is:", "Total expenditure minus total receipts excluding borrowings", ["Exports minus imports", "GDP minus NDP", "Tax minus subsidy only"]),
]

BANK_HIST: QuestionBank = [
    q("Harappan civilisation is also known as:", "The Indus Valley civilisation", ["The Gupta empire", "The Mughal court", "The British Raj"]),
    q("Ashoka is associated with the:", "Mauryan empire", ["Chola navy only", "Vijayanagara as his only capital", "French Revolution"]),
    q("The revolt of 1857 began in:", "Meerut", ["New York", "Tokyo", "Cape Town"]),
    q("Mahatma Gandhi led:", "Non-Cooperation, Civil Disobedience and Quit India movements", ["The October Revolution in Russia", "American independence", "The Meiji Restoration"]),
    q("The Constituent Assembly drafted:", "The Constitution of India", ["The Magna Carta of England as India's only text", "A company prospectus", "A municipal by-law only"]),
    q("Ashokan inscriptions were often written in:", "Brahmi / Prakrit", ["English only", "Latin", "Binary code"]),
]

BANK_POL: QuestionBank = [
    q("The Indian Constitution came into force on:", "26 January 1950", ["15 August 1947 as the Constitution date", "26 November 1949 as the only enforcement date", "1 April 1935"]),
    q("Fundamental Rights are listed in:", "Part III of the Constitution", ["The Directive Principles only", "The Preamble as a justiciable list", "Schedule X only"]),
    q("The Rajya Sabha is:", "The Council of States", ["The House of the People", "A high court", "A panchayat"]),
    q("Judicial review means:", "Courts can examine the constitutionality of laws", ["The executive writes all judgments", "Parliament cannot meet", "Elections are banned"]),
    q("Federalism in India divides power between:", "The Union and the States", ["Two private companies", "Only municipalities", "Political parties and media"]),
    q("Secularism in the Indian Constitution means:", "The state does not favour one religion", ["Ban on all religions", "State religion is one faith", "No citizenship"]),
]

BANK_GEO: QuestionBank = [
    q("Plate tectonics explains:", "Movement of Earth's lithospheric plates", ["Only monsoon rains as a complete theory", "Election cycles", "Stock markets"]),
    q("The atmosphere's most abundant gas is:", "Nitrogen", ["Ozone only", "Argon as majority", "Hydrogen as majority in lower air"]),
    q("Monsoon in India is associated with:", "Seasonal reversal of winds and rainfall", ["Only snowfall in Chennai every month", "Desertification of the Himalaya only", "Tides only"]),
    q("Population density is:", "Number of people per unit area", ["GDP per factory", "Rain per cloud", "Cars per highway only"]),
    q("A watershed is:", "The area draining into a river system", ["A type of monsoon cloud", "A mountain peak only", "A desert dune"]),
    q("HDI includes dimensions of:", "Health, education and living standard", ["Only military strength", "Only coastline length", "Only forest fires"]),
]


def register() -> None:
    register_keys(
        [
            "Meaning of accounting",
            "Accounting equation",
            "Rules of debit and credit",
            "Journal",
            "Trial balance",
            "Meaning of depreciation",
            "Partnership deed",
            "Goodwill",
            "Operating activities",
            "Investing activities",
            "Financing activities",
        ],
        BANK_ACC,
    )
    register_subject_keywords("ACC", [
        (("accounting equation", "journal", "depreciation", "trial balance", "goodwill", "cash flow"), BANK_ACC),
    ])
    register_keys(
        [
            "Concept of management",
            "Fayol's principles",
            "Delegation and decentralisation",
            "Financial planning",
            "Stock exchange and SEBI",
            "Consumer rights",
        ],
        BANK_BST,
    )
    register_subject_keywords("BST", [
        (("management", "fayol", "delegation", "working capital", "sebi", "consumer"), BANK_BST),
    ])
    register_keys(
        [
            "GDP and related aggregates",
            "Functions of money",
            "Central bank",
            "Demand and elasticity",
            "Production possibility curve",
            "Deficit measures",
        ],
        BANK_ECO,
    )
    register_subject_keywords("ECO", [
        (("gdp", "inflation", "reserve bank", "demand", "fiscal deficit", "production possibility"), BANK_ECO),
    ])
    register_keys(
        [
            "Harappan civilisation",
            "Mauryan empire",
            "The revolt of 1857",
            "Non-Cooperation",
            "The Constituent Assembly",
        ],
        BANK_HIST,
    )
    register_subject_keywords("HIST", [
        (("harappan", "maurya", "1857", "gandhi", "constituent", "ashoka"), BANK_HIST),
    ])
    register_keys(
        [
            "Fundamental Rights",
            "Why we need a parliament",
            "Independence of the judiciary",
            "What is federalism",
            "What is secularism",
        ],
        BANK_POL,
    )
    register_subject_keywords("POL", [
        (("fundamental rights", "constitution", "rajya sabha", "judicial review", "federalism", "secularism"), BANK_POL),
    ])
    register_keys(
        [
            "Plate tectonics",
            "Monsoon",
            "Distribution of population",
            "Growth vs development",
            "HDI",
            "Watershed management",
        ],
        BANK_GEO,
    )
    register_subject_keywords("GEO", [
        (("plate tectonic", "monsoon", "population density", "watershed", "hdi", "atmosphere"), BANK_GEO),
    ])
