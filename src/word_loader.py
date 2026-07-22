"""
Word database loader.
"""

from __future__ import annotations

import json
import random
from pathlib import Path

from src.models import WordEntry

WORDS_DIRECTORY = Path("data/words")


class WordLoader:
    """Load Hangman words from JSON category files."""

    def __init__(self) -> None:
        self.word_database = self._load_word_database()

    def _load_word_database(self) -> dict:
        """Load every valid category JSON file."""

        database = {}

        for file_path in sorted(WORDS_DIRECTORY.glob("*.json")):
            # Skip empty files
            if file_path.stat().st_size == 0:
                continue

            with file_path.open(
                "r",
                encoding="utf-8",
            ) as file:
                category = file_path.stem.title()

                database[category] = json.load(file)

        return database

    def get_categories(self) -> list[str]:
        """Return available categories."""

        return sorted(self.word_database.keys())

    def get_difficulties(
        self,
        category: str,
    ) -> list[str]:
        """Return available difficulties."""

        return [
            difficulty
            for difficulty in (
                "Easy",
                "Medium",
                "Hard",
            )
            if difficulty in self.word_database[category]
        ]

    def get_random_word(
        self,
        category: str,
        difficulty: str,
    ) -> WordEntry:
        """Return a random word."""

        data = self.word_database[category]

        return WordEntry(
            category=category,
            difficulty=difficulty,
            description=data["description"],
            word=random.choice(data[difficulty]),
        )
