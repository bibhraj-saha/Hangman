"""
Hangman game engine.
"""

from __future__ import annotations

from src.config import CONFIG
from src.logger import get_logger
from src.models import GameState, WordEntry

logger = get_logger(__name__)


class GameEngine:
    """Core Hangman game engine."""

    def __init__(
        self,
        entry: WordEntry,
    ) -> None:
        self.entry = entry

        self.state = GameState(
            word=entry.word,
            remaining_attempts=CONFIG["game"]["max_attempts"],
        )

        logger.info(
            "New game started | Category=%s Difficulty=%s WordLength=%d",
            entry.category,
            entry.difficulty,
            len(entry.word),
        )

    def guess(
        self,
        letter: str,
    ) -> bool:
        letter = letter.lower()

        if letter in self.state.guessed_letters:
            return False

        if letter in self.state.incorrect_letters:
            return False

        if letter in self.state.word:
            self.state.guessed_letters.add(letter)

            logger.info(
                "Correct guess: %s",
                letter,
            )

            return True

        self.state.remaining_attempts -= 1

        self.state.incorrect_letters.add(letter)

        logger.info(
            "Incorrect guess: %s",
            letter,
        )

        return False

    def current_word(self) -> str:
        return " ".join(
            letter if letter in self.state.guessed_letters else "_"
            for letter in self.state.word
        )

    def is_won(self) -> bool:
        return all(letter in self.state.guessed_letters for letter in self.state.word)

    def is_lost(self) -> bool:
        return self.state.remaining_attempts == 0
