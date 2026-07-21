"""
Application data models.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class WordEntry:
    """
    Represents a single playable word.
    """

    category: str
    difficulty: str
    description: str
    word: str


@dataclass(slots=True)
class ScoreEntry:
    """
    Represents one completed game.
    """

    player: str

    score: int

    category: str

    difficulty: str

    word: str

    won: bool

    timestamp: str


@dataclass(slots=True)
class GameState:
    """
    Runtime state of a Hangman game.
    """

    word: str

    remaining_attempts: int

    guessed_letters: set[str] = field(
        default_factory=set
    )

    incorrect_letters: set[str] = field(
        default_factory=set
    )

    score: int = 0