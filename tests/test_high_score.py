"""
Tests for HighScoreManager.
"""

from __future__ import annotations

from datetime import datetime

from src.high_score import HighScoreManager
from src.models import ScoreEntry


def create_score(
    player: str,
    score: int,
) -> ScoreEntry:
    return ScoreEntry(
        player=player,
        score=score,
        category="Programming",
        difficulty="Easy",
        word="python",
        won=True,
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )


def test_manager_creation():
    manager = HighScoreManager()

    assert manager is not None


def test_add_score():
    manager = HighScoreManager()

    initial = manager.total_games()

    manager.add_score(
        create_score(
            "Tester",
            500,
        )
    )

    assert manager.total_games() == initial + 1


def test_best_score():
    manager = HighScoreManager()

    manager.add_score(
        create_score(
            "High",
            9999,
        )
    )

    assert manager.best_score() >= 9999


def test_get_top_scores():
    manager = HighScoreManager()

    scores = manager.get_top_scores()

    assert isinstance(
        scores,
        list,
    )
