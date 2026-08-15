"""CBSE Class 11 English Core literature/skills banks (no Physics fallback)."""

from __future__ import annotations

from app.data.quiz_banks.common import q, register_keys, register_subject_keywords
from app.data.quiz_concepts import QuestionBank

BANK_PORTRAIT: QuestionBank = [
    q("In 'The Portrait of a Lady', the grandmother's customary dress is associated with:", "Spotless white", ["Bright red silk only", "Military khaki", "A school blazer"]),
    q("The sparrows' behaviour after the grandmother's death suggests:", "They too seemed to mourn; they did not eat the crumbs", ["They attacked the mourners", "They nested in the portrait", "They sang loudly in joy"]),
    q("The author compares the grandmother's face to:", "Winter landscape / crumpled and pale imagery of age", ["A monsoon cloud bursting rain as youth", "A cricket pitch", "A steam engine"]),
    q("'We're Not Afraid to Die' is primarily a narrative of:", "A family's struggle to survive a storm at sea", ["A desert caravan", "A classroom protest", "A palace intrigue"]),
    q("In 'Discovering Tut', Howard Carter is associated with:", "The excavation of Tutankhamun's tomb", ["Translating the Constitution", "Building the Aswan Dam", "Writing Hornbill poems"]),
    q("'The Ailing Planet' discusses primarily:", "The deteriorating state of the Earth's environment", ["A school playground injury", "A fictional planet of gold", "A cricket injury"]),
]

BANK_POEMS_11: QuestionBank = [
    q("In 'A Photograph', the cardboard shows:", "The poet's mother as a girl at the beach", ["A war memorial", "A classroom slate", "A railway ticket"]),
    q("'The Laburnum Top' is turned into a machine of sound by the arrival of:", "The goldfinch", ["A peacock", "An owl", "A crow"]),
    q("'The Voice of the Rain' identifies the rain as:", "The poem of the earth that returns to originate from the land and sea", ["A battle cry", "A king's speech", "A school bell"]),
    q("'Childhood' by Markus Natten traces the loss of childhood to:", "The realisation that adults are hypocrites / Hell and Heaven are not in geography", ["Winning a race", "Buying a bicycle", "Moving house only"]),
    q("In 'Father to Son', the father feels:", "He does not understand his son / they live like strangers", ["He has won a prize with his son", "They share identical hobbies without conflict", "The son is still an infant"]),
    q("Snapshots 'The Address' is about:", "A daughter seeking her mother's belongings after the war", ["A cricket match", "A river cruise", "A science fair"]),
]

BANK_SKILLS_11: QuestionBank = [
    q("A classified advertisement should be:", "Brief, clear and in an appropriate format", ["A five-act play", "A science derivation", "A balance sheet"]),
    q("Note making from a passage typically uses:", "Headings, sub-headings and abbreviations", ["A cash book", "A chemical equation as the only notes", "A cricket scorecard"]),
    q("The past perfect tense is used for:", "An action completed before another past action", ["Future plans only", "Commands only", "Adjectives only"]),
    q("Determiners include words like:", "A, an, the, some, many", ["Run, jump, swim", "Quickly, slowly", "And, but, or as verbs"]),
    q("A speech for school should have:", "A greeting, body with points, and a conclusion", ["Only a title and nothing else", "Only chemical formulae", "Only a table of logs"]),
    q("Reordering of sentences tests:", "Coherence and grammatical links between jumbled sentences", ["Handwriting only", "Map pointing", "Mental arithmetic"]),
]


def register() -> None:
    register_keys(
        [
            "The Portrait of a Lady",
            "We're Not Afraid to Die",
            "Discovering Tut",
            "The Ailing Planet",
            "The Adventure",
            "Silk Road",
        ],
        BANK_PORTRAIT,
    )
    register_keys(
        [
            "A Photograph",
            "The Laburnum Top",
            "The Voice of the Rain",
            "Childhood",
            "Father to Son",
            "The Summer of the Beautiful White Horse",
            "The Address",
            "Mother's Day",
            "Birth",
            "The Tale of Melon City",
        ],
        BANK_POEMS_11,
    )
    register_keys(
        [
            "Note making",
            "Poster",
            "Classified advertisement",
            "Speech",
            "Debate",
            "Unseen Passage – Comprehension",
            "Note making from a passage",
            "Summary writing",
            "Tenses",
            "Reordering of sentences",
            "Determiners",
            "Transformation of sentences",
        ],
        BANK_SKILLS_11,
    )
    register_subject_keywords(
        "ENG",
        [
            (("portrait of a lady", "grandmother", "tutankhamun", "ailing planet"), BANK_PORTRAIT),
            (("photograph", "laburnum", "goldfinch", "voice of the rain", "father to son", "the address"), BANK_POEMS_11),
            (("note making", "poster", "debate", "determiner", "unseen passage", "summary writing"), BANK_SKILLS_11),
        ],
    )
