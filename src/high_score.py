"""
High score management.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from src.models import ScoreEntry


HIGH_SCORE_FILE = Path("data/high_scores.json")


class HighScoreManager:
    """Manage persistent high scores."""

    def __init__(self) -> None:
        self._ensure_file_exists()
        self.high_scores = self._load()

    def _ensure_file_exists(self) -> None:
        """Ensure the leaderboard file exists and contains valid JSON."""

        HIGH_SCORE_FILE.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not HIGH_SCORE_FILE.exists():
            HIGH_SCORE_FILE.write_text(
                "[]",
                encoding="utf-8",
            )
            return

        if HIGH_SCORE_FILE.stat().st_size == 0:
            HIGH_SCORE_FILE.write_text(
                "[]",
                encoding="utf-8",
            )
            return

        try:
            with HIGH_SCORE_FILE.open(
                "r",
                encoding="utf-8",
            ) as file:
                json.load(file)

        except json.JSONDecodeError:
            HIGH_SCORE_FILE.write_text(
                "[]",
                encoding="utf-8",
            )

    def _load(self) -> list[ScoreEntry]:
        """Load leaderboard."""

        with HIGH_SCORE_FILE.open(
            "r",
            encoding="utf-8",
        ) as file:

            data = json.load(file)

        return [
            ScoreEntry(**entry)
            for entry in data
        ]

    def save(self) -> None:
        """Persist leaderboard."""

        with HIGH_SCORE_FILE.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                [
                    asdict(score)
                    for score in self.high_scores
                ],
                file,
                indent=4,
            )

    def add_score(
        self,
        score: ScoreEntry,
    ) -> None:
        """Add a score."""

        self.high_scores.append(score)

        self.high_scores.sort(
            key=lambda item: item.score,
            reverse=True,
        )

        self.high_scores = self.high_scores[:5]

        self.save()

    def top_scores(self) -> list[ScoreEntry]:
        """Return leaderboard."""

        return self.high_scores