"""
Shared pytest fixtures.
"""

from __future__ import annotations

import pytest

from src.game import GameEngine
from src.models import WordEntry


@pytest.fixture
def sample_word() -> WordEntry:
    return WordEntry(
        word="python",
        category="Programming",
        difficulty="Easy",
        description="Programming language",
    )


@pytest.fixture
def game(sample_word: WordEntry) -> GameEngine:
    return GameEngine(sample_word)
