"""Reject meta prompts; require subject-specific concept banks for Class 12 PCM."""

from app.services.quiz_seed import questions_for_topic
from app.services.topic_quiz_builder import (
    is_meta_question,
    resolve_concept_bank,
    validate_question_bank,
)


def test_meta_prompts_are_rejected() -> None:
    bad_prompts = [
        "While studying 'Electric charge', what should a student primarily focus on?",
        "Which statement best describes \"Electric charge\" in the chapter \"Electric Charges and Fields\"?",
        "What should you focus on while studying Electric charge?",
        "Which chapter contains the topic \"Coulomb's law\"?",
        "Which approach best helps you review \"Ohm's law\"?",
    ]
    for prompt in bad_prompts:
        assert is_meta_question(prompt), prompt


def test_meta_options_are_rejected() -> None:
    assert is_meta_question(
        "Any prompt",
        [("The definitions, relations, and applications of 'Electric charge'", True)],
    )


def test_coulomb_bank_is_real_concept_questions() -> None:
    bank = questions_for_topic(
        "Coulomb's law",
        chapter_title="Electric Charges and Fields",
        subject_code="PHY",
        grade=12,
    )
    assert len(bank) >= 8
    assert validate_question_bank("Coulomb's law", bank) == []
    joined = " ".join(p for p, _ in bank).lower()
    assert "while studying" not in joined
    assert "focus on" not in joined
    assert "best describes" not in joined
    assert any("force" in p.lower() or "charge" in p.lower() for p, _ in bank)
    assert any("doubled" in p.lower() or "μc" in p.lower() or "proportional" in p.lower() for p, _ in bank)


def test_electric_charge_bank_not_meta() -> None:
    bank = questions_for_topic("Electric charge", subject_code="PHY", grade=12)
    assert len(bank) >= 8
    for prompt, options in bank:
        assert not is_meta_question(prompt, options)
        assert "definitions, relations, and applications" not in prompt.lower()


def test_unmapped_topic_returns_no_filler() -> None:
    bank = questions_for_topic("Completely Unknown Fantasy Topic XYZ", subject_code="PHY")
    assert bank == []
    assert resolve_concept_bank("Completely Unknown Fantasy Topic XYZ", subject_code="PHY") is None


def test_chemistry_colligative_is_concept_not_physics() -> None:
    bank = questions_for_topic(
        "Colligative properties",
        chapter_title="Solutions",
        subject_code="CHEM",
        grade=12,
    )
    assert len(bank) >= 6
    assert validate_question_bank("Colligative properties", bank) == []
    joined = " ".join(p for p, _ in bank).lower()
    assert "while studying" not in joined
    assert "coulomb" not in joined
    assert any(
        word in joined
        for word in ("osmotic", "raoult", "boiling", "freezing", "vapour", "vapor", "colligative")
    )


def test_math_matrices_not_physics_fallback() -> None:
    bank = questions_for_topic(
        "Types of matrices",
        chapter_title="Matrices",
        subject_code="MATH",
        grade=12,
    )
    assert len(bank) >= 6
    joined = " ".join(p for p, _ in bank).lower()
    assert "electric" not in joined
    assert "matrix" in joined or "matrices" in joined or "row" in joined or "column" in joined


def test_english_last_lesson_literature() -> None:
    bank = questions_for_topic(
        "The Last Lesson",
        chapter_title="Flamingo – Prose",
        subject_code="ENG",
        grade=12,
    )
    assert len(bank) >= 6
    joined = " ".join(p for p, _ in bank).lower()
    assert "while studying" not in joined
    assert any(name in joined for name in ("hamel", "franz", "alsace", "french", "daudet"))


def test_chapter_scoped_preparation_alcohols_vs_amines() -> None:
    alc = questions_for_topic(
        "Preparation",
        chapter_title="Alcohols, Phenols and Ethers",
        subject_code="CHEM",
        grade=12,
    )
    amine = questions_for_topic(
        "Preparation",
        chapter_title="Amines",
        subject_code="CHEM",
        grade=12,
    )
    assert len(alc) >= 6
    assert len(amine) >= 6
    assert [p for p, _ in alc] != [p for p, _ in amine]
    alc_text = " ".join(p for p, _ in alc).lower()
    amine_text = " ".join(p for p, _ in amine).lower()
    assert any(w in alc_text for w in ("alcohol", "phenol", "ether", "alkene", "grignard"))
    assert any(w in amine_text for w in ("amine", "aniline", "amide", "nitro", "gabriel", "hoffmann"))


def test_chemistry_henry_law_is_not_physics() -> None:
    bank = questions_for_topic(
        "Henry's law",
        chapter_title="Solutions",
        subject_code="CHEM",
        grade=12,
    )
    assert len(bank) >= 6
    joined = " ".join(p for p, _ in bank).lower()
    assert "coulomb" not in joined
    assert "while studying" not in joined
    assert any(w in joined for w in ("henry", "gas", "partial pressure", "kh"))


def test_math_equivalence_relations_not_chemistry() -> None:
    bank = questions_for_topic(
        "Equivalence relations",
        chapter_title="Relations and Functions",
        subject_code="MATH",
        grade=12,
    )
    assert len(bank) >= 6
    joined = " ".join(p for p, _ in bank).lower()
    assert "nernst" not in joined
    assert any(w in joined for w in ("reflexive", "symmetric", "transitive", "equivalence"))


def test_english_tiger_king_literature() -> None:
    bank = questions_for_topic(
        "The Tiger King",
        chapter_title="Vistas – Supplementary Reader",
        subject_code="ENG",
        grade=12,
    )
    assert len(bank) >= 6
    joined = " ".join(p for p, _ in bank).lower()
    assert any(w in joined for w in ("tiger", "kalki", "pratibandapuram", "hundredth", "astrologer"))


def test_english_class12_has_new_literature_and_skills_banks() -> None:
    cases = [
        ("Poets and Pancakes", "Flamingo – Prose", ("gemini", "asokamitran", "subbu", "spender")),
        ("A Roadside Stand", "Flamingo – Poetry", ("frost", "roadside", "traffic", "stand")),
        ("Memories of Childhood", "Vistas – Supplementary Reader", ("zitkala", "bama", "hair", "untouch")),
        ("Notice Writing", "Writing Skills", ("notice", "format", "heading", "signature")),
        ("Modal Auxiliaries", "Grammar / Language", ("modal", "must", "should", "can", "might")),
    ]
    for title, chapter, words in cases:
        bank = questions_for_topic(title, chapter_title=chapter, subject_code="ENG", grade=12)
        assert len(bank) >= 8, title
        assert validate_question_bank(title, bank) == []
        joined = " ".join(p for p, _ in bank).lower()
        assert "while studying" not in joined
        assert any(w in joined for w in words), title


def test_chem_does_not_use_physics_keyword_bank() -> None:
    bank = resolve_concept_bank(
        "Bonding and isomerism",
        chapter_title="Coordination Compounds",
        subject_code="CHEM",
    )
    assert bank is not None
    text = " ".join(p for p, _ in bank).lower()
    assert "coulomb" not in text
    assert any(w in text for w in ("isomer", "ligand", "coordination", "crystal field", "geometrical"))


def test_biology_double_fertilisation_is_not_physics() -> None:
    bank = questions_for_topic(
        "Double fertilisation",
        chapter_title="Sexual Reproduction in Flowering Plants",
        subject_code="BIO",
        grade=12,
    )
    assert 1 <= len(bank) <= 20
    joined = " ".join(p for p, _ in bank).lower()
    assert "coulomb" not in joined
    assert "electric" not in joined
    assert any(w in joined for w in ("pollen", "embryo", "angiosperm", "endosperm", "fertilis"))


def test_biology_bt_cotton_is_biology() -> None:
    bank = questions_for_topic(
        "Bt cotton",
        chapter_title="Biotechnology and its Applications",
        subject_code="BIO",
        grade=12,
    )
    assert len(bank) >= 4
    joined = " ".join(p for p, _ in bank).lower()
    assert "thuringiensis" in joined or "cry" in joined or "bt" in joined


def test_class_11_mole_concept_is_chemistry() -> None:
    bank = questions_for_topic(
        "Mole concept",
        chapter_title="Some Basic Concepts of Chemistry",
        subject_code="CHEM",
        grade=11,
    )
    assert len(bank) >= 4
    joined = " ".join(p for p, _ in bank).lower()
    assert "coulomb" not in joined
    assert any(w in joined for w in ("mole", "avogadro", "limiting", "stoichiometr"))


def test_class_11_english_portrait_is_literature() -> None:
    bank = questions_for_topic(
        "The Portrait of a Lady",
        chapter_title="Hornbill – Prose",
        subject_code="ENG",
        grade=11,
    )
    assert len(bank) >= 4
    joined = " ".join(p for p, _ in bank).lower()
    assert "grandmother" in joined or "sparrow" in joined or "portrait" in joined
    assert "coulomb" not in joined
