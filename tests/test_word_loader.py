"""
Tests for WordLoader.
"""

from __future__ import annotations

from src.word_loader import WordLoader


def test_loader_creation():
    loader = WordLoader()

    assert loader is not None


def test_categories_exist():
    loader = WordLoader()

    categories = loader.get_categories()

    assert len(categories) > 0

    assert "Animals" in categories


def test_difficulties_exist():
    loader = WordLoader()

    difficulties = loader.get_difficulties(
        "Animals",
    )

    assert "Easy" in difficulties

    assert "Medium" in difficulties

    assert "Hard" in difficulties


def test_random_word_returns_entry():
    loader = WordLoader()

    word = loader.get_random_word(
        "Animals",
        "Easy",
    )

    assert word.word != ""

    assert word.category == "Animals"

    assert word.difficulty == "Easy"


def test_multiple_random_words():
    loader = WordLoader()

    words = set()

    for _ in range(10):
        entry = loader.get_random_word(
            "Animals",
            "Easy",
        )

        words.add(entry.word)

    assert len(words) >= 1
