"""
Word database validation utilities.
"""

from __future__ import annotations

import json
from pathlib import Path


class WordDatabaseValidator:
    REQUIRED_LEVELS = (
        "Easy",
        "Medium",
        "Hard",
    )

    def __init__(
        self,
        directory: str = "data/words",
    ):
        self.directory = Path(directory)

        self.errors: list[str] = []

        self.warnings: list[str] = []

    def validate(self):
        for file in sorted(self.directory.glob("*.json")):
            self._validate_file(file)

    def _validate_file(
        self,
        file: Path,
    ):
        try:
            with file.open(
                encoding="utf-8",
            ) as f:
                data = json.load(f)

        except json.JSONDecodeError as error:
            self.errors.append(f"{file.name}: Invalid JSON ({error}).")

            return

        for level in self.REQUIRED_LEVELS:
            if level not in data:
                self.errors.append(f"{file.name}: Missing {level}.")

                continue

            words = data[level]

            if len(words) == 0:
                self.errors.append(f"{file.name}: Empty {level}.")

            duplicates = len(words) != len(set(words))

            if duplicates:
                self.warnings.append(f"{file.name}: Duplicate words in {level}.")

            for word in words:
                if not word.isalpha():
                    self.warnings.append(
                        f"{file.name}: '{word}' contains non alphabetic characters."
                    )

                if word != word.lower():
                    self.warnings.append(f"{file.name}: '{word}' is not lowercase.")

    def summary(self):
        return {
            "errors": self.errors,
            "warnings": self.warnings,
        }
